// Vercel sunucusuz fonksiyonu – iletişim formunu e-posta olarak gönderir.
// Hostinger'da aynı işi kontakt.php yapar; Vercel'de /kontakt.php adresi buraya yönlendirilir (vercel.json).
// Gerekli ortam değişkenleri (Vercel → Project → Settings → Environment Variables):
//   SMTP_HOST, SMTP_PORT (465), SMTP_USER, SMTP_PASS, MAIL_TO (varsayılan: baharsonek.official@gmail.com)
const nodemailer = require('nodemailer');

const clean = (v, max = 200) => String(v || '').replace(/<[^>]*>/g, '').replace(/[\r\n]+/g, ' ').trim().slice(0, max);

module.exports = async (req, res) => {
  const body = req.body || {};
  const lang = body.lang === 'de' ? 'de' : 'tr';
  const back = lang === 'de' ? '/de/kontakt.html' : '/iletisim.html';
  const go = (q) => { res.statusCode = 303; res.setHeader('Location', `${back}${q ? '?' + q : ''}#form`); res.end(); };

  if (req.method !== 'POST') return go('');
  if (body.website) return go('gonderildi=1'); // spam tuzağı

  const ad = clean(body.ad), tel = clean(body.tel, 60), konu = clean(body.konu, 120);
  const email = clean(body.email, 200);
  const mesaj = String(body.mesaj || '').replace(/<[^>]*>/g, '').trim().slice(0, 5000);
  if (!ad || !tel || !mesaj || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return go('hata=1');

  const { SMTP_HOST, SMTP_PORT = '465', SMTP_USER, SMTP_PASS, MAIL_TO = 'baharsonek.official@gmail.com' } = process.env;
  if (!SMTP_HOST || !SMTP_USER || !SMTP_PASS) { console.error('SMTP ayarları eksik'); return go('hata=1'); }

  const text = [
    'Web sitesi iletişim formu / Kontaktformular',
    '──────────────────────────────',
    `Ad Soyad / Name:  ${ad}`,
    `Telefon:          ${tel}`,
    `E-posta / E-Mail: ${email}`,
    `Konu / Betreff:   ${konu}`,
    `Dil / Sprache:    ${lang.toUpperCase()}`,
    '──────────────────────────────', '', mesaj, ''
  ].join('\n');

  try {
    const t = nodemailer.createTransport({
      host: SMTP_HOST, port: Number(SMTP_PORT), secure: Number(SMTP_PORT) === 465,
      auth: { user: SMTP_USER, pass: SMTP_PASS }
    });
    await t.sendMail({
      from: `"Bahar Sonek Web" <${SMTP_USER}>`,
      to: MAIL_TO,
      replyTo: email,
      subject: `${lang === 'de' ? 'Kontaktanfrage' : 'Web sitesi mesajı'}: ${konu} – ${ad}`,
      text
    });
    return go('gonderildi=1');
  } catch (e) {
    console.error('E-posta gönderilemedi:', e.message);
    return go('hata=1');
  }
};
