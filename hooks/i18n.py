from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from textwrap import dedent
from urllib.parse import unquote, urlsplit

from mkdocs.exceptions import PluginError


def validate_sources(docs_dir: Path) -> int:
    originals = sorted(path for path in docs_dir.rglob("*.md") if not path.name.endswith(".en.md"))
    settings = re.compile(r"^[ \t]*```bsc-settings\n(.*?)^[ \t]*```", re.MULTILINE | re.DOTALL)
    problems = []
    for original in originals:
        translation = original.with_name(original.stem + ".en.md")
        if not translation.is_file():
            problems.append(f"Missing English translation: {original.relative_to(docs_dir)}")
            continue
        source_blocks = [dedent(block).strip() for block in settings.findall(original.read_text())]
        translated_blocks = [dedent(block).strip() for block in settings.findall(translation.read_text())]
        if source_blocks != translated_blocks:
            problems.append(f"Changed firmware settings selectors: {translation.relative_to(docs_dir)}")
    for translation in docs_dir.rglob("*.en.md"):
        if not translation.with_name(translation.name.removesuffix(".en.md") + ".md").is_file():
            problems.append(f"English page has no German counterpart: {translation.relative_to(docs_dir)}")
    if problems:
        raise PluginError("\n".join(problems))
    return len(originals)


def on_config(config):
    validate_sources(Path(config["docs_dir"]))
    return config


class PageLinks(HTMLParser):
    def __init__(self, path: Path):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.headings: set[str] = set()
        self.links: list[str] = []
        self.languages: dict[str, str] = {}
        self.language = ""
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                self.headings.add(attributes["id"])
        if tag == "html":
            self.language = attributes.get("lang", "")
        for attribute in ("href", "src"):
            if attributes.get(attribute):
                self.links.append(attributes[attribute])
        if tag == "a" and attributes.get("hreflang"):
            self.languages[attributes["hreflang"]] = attributes["href"]


def validate_site(site_dir: Path, docs_dir: Path, base_path: str = "/bsc/") -> int:
    site_dir = site_dir.resolve()

    def resolve_target(path: Path, url_path: str) -> Path:
        decoded = unquote(url_path)
        if decoded.startswith("/"):
            target = site_dir / decoded.removeprefix(base_path).lstrip("/")
        else:
            target = path.parent / decoded if decoded else path
        target = target.resolve()
        return target / "index.html" if target.is_dir() else target

    pages = {
        path: PageLinks(path)
        for path in site_dir.rglob("*.html")
        if "demo" not in path.relative_to(site_dir).parts and path.name != "404.html"
    }
    problems = []
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = resolve_target(path, url.path)
            if not target.is_file():
                problems.append(f"{path.relative_to(site_dir)}: missing {link}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                problems.append(f"{path.relative_to(site_dir)}: missing anchor {link}")
    for original in docs_dir.rglob("*.md"):
        if original.name.endswith(".en.md"):
            continue
        relative = original.relative_to(docs_dir).with_suffix("")
        output = relative.parent / "index.html" if relative.name == "index" else relative / "index.html"
        german, english = pages.get(site_dir / output), pages.get(site_dir / "en" / output)
        if german and english:
            for heading in german.headings - english.headings:
                problems.append(f"Missing original chapter anchor: en/{output}#{heading}")
        for locale, prefix in (("de", Path()), ("en", Path("en"))):
            path = site_dir / prefix / output
            if path not in pages:
                problems.append(f"Missing rendered page: {prefix / output}")
                continue
            page = pages[path]
            if page.language != locale:
                problems.append(f"Wrong HTML language: {prefix / output}: {page.language}")
            for other_locale, other_prefix in (("de", Path()), ("en", Path("en"))):
                link = page.languages.get(other_locale, "")
                target = resolve_target(path, urlsplit(link).path)
                if not link or target != site_dir / other_prefix / output:
                    problems.append(f"Wrong {other_locale} language switch: {prefix / output}: {link}")
    if problems:
        raise PluginError("\n".join(sorted(set(problems))))
    return len(pages)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check bilingual sources, rendered links and language switches.")
    parser.add_argument("site_dir", type=Path, nargs="?", default=Path("site"))
    parser.add_argument("--base-path", default="/bsc/")
    args = parser.parse_args()
    docs = Path(__file__).resolve().parents[1] / "docs"
    count = validate_sources(docs)
    rendered = validate_site(args.site_dir, docs, args.base_path)
    print(f"OK: {count} translation pairs, matching settings blocks, {rendered} rendered pages and local links.")