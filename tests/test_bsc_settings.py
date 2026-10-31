import copy
import html
import importlib.util
import json
import re
import unittest
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("bsc_settings", ROOT / "hooks" / "bsc_settings.py")
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class SettingsLocalizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.translations = renderer.load_translations(ROOT, "v010", "en")

    def render(self, body, locale="de"):
        return renderer._replace_fence_body(body, ROOT, f"test.{locale}.md", locale=locale)

    def test_complete_catalogue_preserves_source_data_and_technical_values(self):
        def technical_values(node):
            if isinstance(node, dict):
                return {key: technical_values(value) for key, value in node.items()
                        if key not in renderer._TRANSLATABLE_KEYS}
            if isinstance(node, list):
                return [technical_values(value) for value in node]
            return node

        renderer.validate_translations(ROOT, "v010", "en")
        for path in (ROOT / "bsc_settings" / "v010" / "params").rglob("*.json"):
            with self.subTest(path=path.name):
                original = json.loads(path.read_text(encoding="utf-8"))
                snapshot = copy.deepcopy(original)
                translated = renderer.localize_settings(original, self.translations)
                self.assertEqual(original, snapshot)
                self.assertEqual(technical_values(original), technical_values(translated))

    def test_original_label_selectors_and_language_cache_isolation(self):
        body = "version: v010\nfile: system.json\nlabel: Benutzer\nprofile: off\ngroups: 1"
        german = self.render(body)
        english = self.render(body, "en")
        self.assertIn("Passwortschutz aktivieren", german)
        self.assertIn("Enable password protection", english)
        self.assertIn("0 disables automatic logout.", english)
        self.assertIn("<b>Users</b>", english)
        self.assertIn("User 1", english)
        self.assertIn("Read-only", english)
        self.assertEqual(self.render(body), german)

    def test_mqtt_original_label_selector_is_resolved_before_translation(self):
        body = "version: v010\nfile: mqtt.json\nlabel: Weitere Daten\nprofile: off"
        english = self.render(body, "en")
        self.assertIn("Other data", english)
        self.assertNotIn("Weitere Daten", english)
        self.assertNotIn("bsc-settings-error", english)

    def test_referenced_options_are_localized_without_changing_values(self):
        context = renderer.RenderContext(ROOT, "v010", {}, renderer.load_type_map(ROOT, "v010"),
                                         "test.en.md", locale="en")
        changed = 0
        for folder in ("combos", "refs"):
            for path in (ROOT / "bsc_settings" / "v010" / "params" / folder).glob("*.json"):
                original = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(original, list):
                    continue
                translated = context.resolve_options([{"$ref": path.stem}])
                self.assertEqual([option.get("v") for option in original],
                                 [option.get("v") for option in translated])
                changed += sum(left.get("l") != right.get("l")
                               for left, right in zip(original, translated))
        self.assertGreater(changed, 0)

    def test_missing_translation_is_an_error(self):
        with self.assertRaisesRegex(renderer.RenderError, "Missing settings translation"):
            renderer.localize_settings({"label": "New untranslated text"}, self.translations)

    def test_html_entities_and_inline_help_markup(self):
        source = {"label": "Eintr&#228;ge", "help": "Zeile<br>zwei\ndrei"}
        localized = renderer.localize_settings(
            source, {"Einträge": "Entries", "Zeile<br>zwei\ndrei": "Line<br>two\nthree"})
        self.assertEqual(renderer.escape_text(localized["label"]), "Entries")
        self.assertEqual(renderer.help_html(localized), "Line<br>two<br>three")

    def test_catalogue_keeps_numbers_and_inline_tags(self):
        for source, translation in self.translations.items():
            with self.subTest(source=source):
                self.assertEqual(re.findall(r"\d+(?:[.,]\d+)?", source),
                                 re.findall(r"\d+(?:[.,]\d+)?", translation))
                self.assertEqual(re.findall(r"</?(?:b|i|br)\s*/?>", source),
                                 re.findall(r"</?(?:b|i|br)\s*/?>", translation))
                self.assertEqual(source, html.unescape(source))

    def test_page_locale_applies_to_regular_and_indented_fences(self):
        class Config(dict):
            config_file_path = str(ROOT / "mkdocs.yml")

        body = "version: v010\nfile: system.json\nlabel: Benutzer\nprofile: off\ngroups: 1"
        regular = f"```bsc-settings\n{body}\n```\n"
        indented = "\n".join("    " + line for line in regular.splitlines()) + "\n"
        page = SimpleNamespace(file=SimpleNamespace(locale="en", src_path="test.en.md"))
        output = renderer.on_page_markdown(regular + "\n" + indented, page,
                                           Config(theme={"language": "de"}), None)
        self.assertEqual(output.count("Enable password protection"), 2)
        self.assertNotIn("```bsc-settings", output)

    def test_profile_graph_uses_english_generated_control(self):
        body = ("version: v010\nfile: inverterCharge.json\nprofile: off\n"
                "section: UI_SECT_INVERTERCHARGE_LADESTROM_REDUZIEREN_TEMPERATURPROFIL")
        english = self.render(body, "en")
        self.assertIn("<summary>Show values</summary>", english)
        self.assertIn("Temperature-profile charge reduction", english)
        self.assertNotIn("Werte anzeigen", english)


if __name__ == "__main__":
    unittest.main()