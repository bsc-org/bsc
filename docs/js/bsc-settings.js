/* bsc-settings.js
 * Statische Ergaenzung zum BSC-Settings-Renderer (bsc-settings-v*.css):
 * Spiegelt das WebApp-Verhalten von viewMulticheckAktivLabel() /
 * renderMultiCheckSummary() – beim An-/Abwaehlen einer Option in einem
 * Multicheck-Collapsible (Typ 14) wird die selected-summary mit Tag-Pills
 * der ausgewaehlten Optionen aktualisiert (leer, wenn keine ausgewaehlt).
 * Reine Anzeige: Es wird nichts gespeichert, nur die Summary aktualisiert.
 */
(function () {
  'use strict';

  function updateMulticheckSummary(fieldset) {
    var content = fieldset.closest('.collapsible-content');
    if (!content) return;
    var lblToggle = content.previousElementSibling;
    if (!lblToggle || !lblToggle.classList.contains('lbl-toggle')) return;
    var summary = lblToggle.querySelector('.selected-summary');
    if (!summary) return;

    summary.innerHTML = '';
    var inputs = fieldset.querySelectorAll('input[type="checkbox"]');
    for (var i = 0; i < inputs.length; i++) {
      if (!inputs[i].checked) continue;
      var label = inputs[i].closest('label');
      var span = label ? label.querySelector('span') : null;
      var txt = span ? span.textContent.trim() : '';
      if (!txt) continue;
      var tag = document.createElement('span');
      tag.className = 'tag';
      tag.textContent = txt;
      summary.appendChild(tag);
    }
  }

  document.addEventListener('change', function (ev) {
    var t = ev.target;
    if (!t || t.tagName !== 'INPUT' || t.type !== 'checkbox') return;
    var fieldset = t.closest('fieldset');
    if (!fieldset) return;
    if (!fieldset.closest('.collapsible-content')) return;
    updateMulticheckSummary(fieldset);
  });
})();
