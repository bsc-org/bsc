/* theme-sync.js
 * Synchronisiert das Material-Farbschema (data-md-color-scheme) mit der
 * .dark-Klasse am <html>-Element, damit die Dark-Overrides des
 * BSC-Settings-CSS (html.dark .bsc-settings-<version> ...) wie in der
 * WebApp funktionieren. Persistenz der Nutzerwahl uebernimmt Material selbst.
 */
(function () {
  'use strict';

  function syncDarkClass() {
    var scheme = document.documentElement.getAttribute('data-md-color-scheme');
    document.documentElement.classList.toggle('dark', scheme === 'slate');
  }

  syncDarkClass();

  if (typeof MutationObserver !== 'undefined') {
    new MutationObserver(syncDarkClass).observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['data-md-color-scheme']
    });
  }
})();
