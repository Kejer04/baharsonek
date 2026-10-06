// Mobil menü
const burger = document.querySelector('.burger');
const menu = document.querySelector('.menu');
if (burger && menu) {
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });
}

// Kaydırınca beliren öğeler
const io = 'IntersectionObserver' in window ? new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12 }) : null;
document.querySelectorAll('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('in'));

// Lightbox (belgeler, galeri)
const lb = document.createElement('div');
lb.className = 'lb';
lb.innerHTML = '<img alt="">';
document.body.appendChild(lb);
document.querySelectorAll('[data-zoom]').forEach(el => {
  el.addEventListener('click', () => {
    const img = el.querySelector('img');
    lb.querySelector('img').src = img.src;
    lb.querySelector('img').alt = img.alt;
    lb.classList.add('open');
  });
});
lb.addEventListener('click', () => lb.classList.remove('open'));
document.addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('open'); });

// Harita: yalnızca ziyaretçi onaylayınca Google Maps yüklenir (DSGVO)
const mapBtn = document.querySelector('[data-load-map]');
if (mapBtn) {
  mapBtn.addEventListener('click', () => {
    const box = mapBtn.closest('.map');
    box.innerHTML = '<iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Kirchstr. 33, 45879 Gelsenkirchen" src="https://www.google.com/maps?q=Kirchstr.+33,+45879+Gelsenkirchen&output=embed"></iframe>';
  });
}

// İletişim formu: "E-posta ile Gönder" → kontakt.php (sunucu e-postayı gönderir)
// "WhatsApp ile Gönder" → aynı form içeriği WhatsApp mesajı olarak açılır
const form = document.querySelector('form.contact');
if (form) {
  const waBtn = form.querySelector('[data-wa-send]');
  if (waBtn) waBtn.addEventListener('click', () => {
    if (!form.reportValidity()) return;
    const d = new FormData(form);
    const de = document.documentElement.lang === 'de';
    const msg = de
      ? `Hallo Frau Sonek,\n\nName: ${d.get('ad')}\nTelefon: ${d.get('tel')}\nE-Mail: ${d.get('email')}\nBetreff: ${d.get('konu')}\n\n${d.get('mesaj')}`
      : `Merhaba Bahar Hanım,\n\nAd Soyad: ${d.get('ad')}\nTelefon: ${d.get('tel')}\nE-posta: ${d.get('email')}\nKonu: ${d.get('konu')}\n\n${d.get('mesaj')}`;
    window.open('https://wa.me/4915202614684?text=' + encodeURIComponent(msg), '_blank', 'noopener');
  });
  const q = new URLSearchParams(location.search);
  if (q.has('gonderildi')) document.querySelector('[data-form-ok]')?.removeAttribute('hidden');
  if (q.has('hata')) document.querySelector('[data-form-err]')?.removeAttribute('hidden');
  form.addEventListener('submit', () => { const b = form.querySelector('[type=submit]'); if (b) { b.disabled = true; b.style.opacity = .7; } });
}

// Konu ön seçimi (?konu=...)
const p = new URLSearchParams(location.search).get('konu');
const sel = document.querySelector('select[name="konu"]');
if (p && sel) [...sel.options].forEach(o => { if (o.value === p) o.selected = true; });

document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

// YouTube: yalnızca tıklayınca yüklenir (youtube-nocookie, DSGVO)
document.querySelectorAll('[data-yt]').forEach(btn => {
  btn.addEventListener('click', () => {
    const f = document.createElement('iframe');
    f.src = `https://www.youtube-nocookie.com/embed/${btn.dataset.yt}?autoplay=1&rel=0`;
    f.title = btn.getAttribute('aria-label') || 'YouTube';
    f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
    f.allowFullscreen = true;
    btn.replaceWith(f);
  });
});
