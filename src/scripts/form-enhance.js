// Inquiry-form enhancement (2026-09-11 form critique, breeder round 3). Progressive: without this
// script every form still validates natively and the surrender text box stays visible + optional.
// Runs only on forms carrying the screening contract ([name="resale_screening"]).
(function () {
  var MISMATCH = [
    ['email', 'email_confirm', "Emails don't match."],
    ['phone', 'phone_confirm', "Numbers don't match."],
    ['cell', 'cell_confirm', "Numbers don't match."],
  ];

  function fieldBox(c) {
    // The field's own wrapper — the radio group's fieldset, else the wrapping label, else the
    // control's parent. Messages are appended INSIDE it: inserted after it, a message became a
    // sibling in Tailwind's space-y stack and sat flush on the next field's title (2026-09-11).
    if (c.type === 'radio' || c.type === 'checkbox') return c.closest('fieldset') || c.parentElement;
    return c.closest('label') || c.parentElement;
  }

  function labelOf(c) {
    var fs = (c.type === 'radio' || c.type === 'checkbox') && c.closest('fieldset');
    var el = fs ? fs.querySelector('legend') : (c.id && c.form.querySelector('label[for="' + c.id + '"]')) || c.closest('label');
    var t = el ? el.textContent.replace(/\*/g, '').replace(/\s+/g, ' ').trim() : c.name;
    return t.length > 60 ? t.slice(0, 57).replace(/\s+\S*$/, '') + '…' : t;
  }

  function messageFor(c) {
    if (c.validity.customError) return c.validationMessage;
    if (c.validity.valueMissing) return (c.type === 'radio' || c.type === 'checkbox') ? 'Please choose one.' : 'Please fill this in.';
    if (c.validity.typeMismatch && c.type === 'email') return 'Enter an email like name@example.com.';
    return c.validationMessage || 'Please check this.';
  }

  function clear(form) {
    form.querySelectorAll('.form-err').forEach(function (e) { e.remove(); });
    form.querySelectorAll('[aria-invalid="true"]').forEach(function (e) { e.removeAttribute('aria-invalid'); });
    var s = form.querySelector('.form-err-summary'); if (s) s.remove();
  }

  function clearOne(c) {
    var err = c.form.querySelector('.form-err[data-for="' + c.name + '"]');
    if (err) err.remove();
    c.form.querySelectorAll('[name="' + c.name + '"]').forEach(function (x) { x.removeAttribute('aria-invalid'); });
    if (!c.form.querySelector('.form-err')) { var s = c.form.querySelector('.form-err-summary'); if (s) s.remove(); }
  }

  function checkMismatch(form) {
    MISMATCH.forEach(function (m) {
      var a = form.querySelector('[name="' + m[0] + '"]'), b = form.querySelector('[name="' + m[1] + '"]');
      if (!a || !b) return;
      var norm = function (v) { return m[0] === 'email' ? v.trim().toLowerCase() : v.replace(/\D/g, ''); };
      b.setCustomValidity(b.value && norm(a.value) !== norm(b.value) ? m[2] : '');
    });
  }

  function surrender(form) {
    var radios = form.querySelectorAll('input[type="radio"][name="surrender_history"]');
    var box = form.querySelector('[data-surrender-details]');
    if (!radios.length || !box) return;
    var ta = box.querySelector('textarea');
    function sync() {
      var yes = form.querySelector('input[name="surrender_history"][value="yes"]:checked');
      box.hidden = !yes;
      if (ta) ta.required = !!yes;
    }
    radios.forEach(function (r) { r.addEventListener('change', sync); });
    sync();
  }

  function enhance(form) {
    form.noValidate = true;
    surrender(form);
    form.addEventListener('input', function (e) { if (e.target.name) { checkMismatch(form); clearOne(e.target); } });
    form.addEventListener('change', function (e) { if (e.target.name) clearOne(e.target); });
    form.addEventListener('submit', function (e) {
      clear(form);
      checkMismatch(form);
      if (form.checkValidity()) return;
      e.preventDefault();
      var seen = {}, items = [];
      Array.prototype.forEach.call(form.elements, function (c) {
        if (!c.name || c.type === 'hidden' || c.name === '_gotcha' || seen[c.name] || c.checkValidity()) return;
        seen[c.name] = true;
        var box = fieldBox(c), id = 'err-' + Math.random().toString(36).slice(2, 8);
        var p = document.createElement('span');
        p.className = 'form-err'; p.id = id; p.setAttribute('data-for', c.name); p.textContent = messageFor(c);
        box.appendChild(p);
        form.querySelectorAll('[name="' + c.name + '"]').forEach(function (x) {
          x.setAttribute('aria-invalid', 'true');
          x.setAttribute('aria-describedby', id);
        });
        items.push({ c: c, label: labelOf(c), msg: messageFor(c) });
      });
      var sum = document.createElement('div');
      sum.className = 'form-err-summary'; sum.setAttribute('role', 'alert'); sum.tabIndex = -1;
      var h = document.createElement('p'); h.className = 'form-err-summary-title';
      h.textContent = items.length === 1 ? 'One answer needs a look before we can send this:' : items.length + ' answers need a look before we can send this:';
      var ul = document.createElement('ul');
      items.forEach(function (it) {
        var li = document.createElement('li'), b = document.createElement('button');
        b.type = 'button'; b.textContent = it.label + ': ' + it.msg;
        b.addEventListener('click', function () { it.c.focus(); it.c.scrollIntoView({ block: 'center' }); });
        li.appendChild(b); ul.appendChild(li);
      });
      sum.appendChild(h); sum.appendChild(ul);
      var submit = form.querySelector('[type="submit"]');
      (submit ? submit : form.lastElementChild).insertAdjacentElement('beforebegin', sum);
      sum.scrollIntoView({ block: 'center' });
      sum.focus({ preventScroll: true });
    });
  }

  function init() {
    document.querySelectorAll('form').forEach(function (f) { if (f.querySelector('[name="resale_screening"]')) enhance(f); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
