/* theme-sync.js
 * Synchronisiert das Material-Farbschema (data-md-color-scheme) mit der
 * .dark-Klasse am <html>-Element, damit die Dark-Overrides des
 * BSC-Settings-CSS (html.dark .bsc-settings-<version> ...) wie in der
 * WebApp funktionieren. Persistenz der Nutzerwahl uebernimmt Material selbst.
 *
 * ACHTUNG (Material for MkDocs >= 9.x): Material setzt data-md-color-scheme
 * auf das <body>-Element (base.html + Palette-JS, auch beim Toggle), NICHT
 * auf <html>. Das Attribut wird deshalb primaer am <body> gelesen/beobachtet;
 * <html> bleibt als Fallback fuer aeltere Material-Versionen. Die .dark-Klasse
 * wird weiterhin am <html>-Element gesetzt, weil die CSS-Selektoren
 * html.dark ... erwarten.
 */
(function () {
  'use strict';

  function currentScheme() {
    var body = document.body;
    if (body && body.hasAttribute('data-md-color-scheme')) {
      return body.getAttribute('data-md-color-scheme');
    }
    return document.documentElement.getAttribute('data-md-color-scheme');
  }

  function syncDarkClass() {
    document.documentElement.classList.toggle('dark', currentScheme() === 'slate');
  }

  syncDarkClass();

  if (typeof MutationObserver !== 'undefined') {
    var opts = { attributes: true, attributeFilter: ['data-md-color-scheme'] };
    if (document.body) {
      new MutationObserver(syncDarkClass).observe(document.body, opts);
    }
    new MutationObserver(syncDarkClass).observe(document.documentElement, opts);
  }
})();
