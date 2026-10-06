/* ───────────────────────────────────────────────────────────
   Çerez / Onay yönetimi (Consent) – TR & DE
   Kategori "medya": Google Maps ve YouTube gibi harici içerikler.
   Onay tarayıcıda localStorage'da saklanır (çerez kullanılmaz).
   ─────────────────────────────────────────────────────────── */
(function () {
  const KEY = 'bs_consent_v1';
  const DE = document.documentElement.lang === 'de';
  const T = DE ? {
    title: 'Datenschutz-Einstellungen',
    text: 'Wir verwenden nur technisch notwendige Funktionen. Externe Inhalte wie <b>Google Maps</b> und <b>YouTube</b> laden wir erst mit Ihrer Einwilligung – dabei werden Daten (z. B. Ihre IP-Adresse) an Google übertragen, ggf. auch in die USA. Sie können Ihre Auswahl jederzeit unter „Cookie-Einstellungen“ im Fußbereich ändern.',
    more: 'Datenschutzerklärung', imp: 'Impressum',
    all: 'Alle akzeptieren', need: 'Nur notwendige', save: 'Auswahl speichern', settings: 'Einstellungen',
    c1: 'Notwendig', c1d: 'Speichert Ihre Auswahl. Immer aktiv.',
    c2: 'Externe Medien', c2d: 'Google Maps (Karte auf der Kontaktseite) und YouTube-Videos.'
  } : {
    title: 'Gizlilik ayarları',
    text: 'Sitemizde yalnızca teknik olarak gerekli işlevler kullanılır. <b>Google Haritalar</b> ve <b>YouTube</b> gibi harici içerikler ancak onayınızla yüklenir; bu durumda verileriniz (ör. IP adresiniz) Google\'a, gerekirse ABD\'ye aktarılır. Seçiminizi sayfanın altındaki „Çerez ayarları“ bağlantısından istediğiniz zaman değiştirebilirsiniz.',
    more: 'Gizlilik politikası (Datenschutz)', imp: 'Impressum',
    all: 'Tümünü kabul et', need: 'Sadece gerekli', save: 'Seçimi kaydet', settings: 'Ayarlar',
    c1: 'Gerekli', c1d: 'Seçiminizi saklar. Her zaman aktif.',
    c2: 'Harici medya', c2d: 'Google Haritalar (iletişim sayfasındaki harita) ve YouTube videoları.'
  };

  const read = () => { try { return JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; } };
  const write = (media) => {
    const prev = window.__consent && window.__consent.media;
    const v = { media: !!media, ts: new Date().toISOString() };
    try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {}
    window.__consent = v;
    if (prev && !v.media) { location.reload(); return; }  // onay geri alındı: harici içerikleri kaldır
    apply();
  };
  window.__consent = read();

  // Harici içerikleri onay durumuna göre yükle
  function apply() {
    const ok = window.__consent && window.__consent.media;
    document.querySelectorAll('[data-consent-src]').forEach(box => {
      if (!ok || box.dataset.loaded) return;
      const f = document.createElement('iframe');
      f.src = box.dataset.consentSrc;
      f.title = box.dataset.title || '';
      f.loading = 'lazy';
      f.referrerPolicy = 'no-referrer-when-downgrade';
      f.allowFullscreen = true;
      box.innerHTML = '';
      box.appendChild(f);
      box.dataset.loaded = '1';
    });
  }
  window.bsConsentApply = apply;

  // Harita üzerindeki "Haritayı yükle" düğmesi: medya onayı verir
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-consent-accept-media]');
    if (b) { e.preventDefault(); write(true); hide(); }
    const o = e.target.closest('[data-consent-open]');
    if (o) { e.preventDefault(); show(true); }
  });

  // Banner
  let el;
  function build() {
    el = document.createElement('div');
    el.className = 'cc';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-labelledby', 'cc-title');
    const media = window.__consent ? window.__consent.media : false;
    el.innerHTML = `
      <div class="cc-box">
        <h3 id="cc-title">${T.title}</h3>
        <p>${T.text}</p>
        <div class="cc-opts" hidden>
          <label><input type="checkbox" checked disabled> <span><b>${T.c1}</b><small>${T.c1d}</small></span></label>
          <label><input type="checkbox" data-cc-media ${media ? 'checked' : ''}> <span><b>${T.c2}</b><small>${T.c2d}</small></span></label>
        </div>
        <div class="cc-btns">
          <button class="btn btn-gold" data-cc="all">${T.all}</button>
          <button class="btn btn-ghost" data-cc="need">${T.need}</button>
          <button class="btn btn-link" data-cc="settings">${T.settings}</button>
          <button class="btn btn-ghost" data-cc="save" hidden>${T.save}</button>
        </div>
        <p class="cc-links"><a href="datenschutz.html">${T.more}</a> · <a href="impressum.html">${T.imp}</a></p>
      </div>`;
    document.body.appendChild(el);
    el.addEventListener('click', e => {
      const a = e.target.closest('[data-cc]'); if (!a) return;
      const k = a.dataset.cc;
      if (k === 'all') { write(true); hide(); }
      if (k === 'need') { write(false); hide(); }
      if (k === 'settings') {
        el.querySelector('.cc-opts').hidden = false;
        a.hidden = true; el.querySelector('[data-cc="save"]').hidden = false;
      }
      if (k === 'save') { write(el.querySelector('[data-cc-media]').checked); hide(); }
    });
  }
  function show(settings) {
    if (el) el.remove();
    build();
    if (settings) el.querySelector('[data-cc="settings"]').click();
    requestAnimationFrame(() => el.classList.add('on'));
  }
  function hide() { if (el) { el.classList.remove('on'); setTimeout(() => el && el.remove(), 300); } }

  // Gizlilik/Impressum sayfalarında banner metni okumayı engellemesin diye yine gösterilir ama sayfa okunabilir kalır
  if (!window.__consent) show(false); else apply();
})();
