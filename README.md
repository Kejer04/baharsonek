# Bahar Sonek – Creative Dienstleistungen

Bahar Sonek'in iki dilli (Türkçe / Almanca) tanıtım sitesi. Gelsenkirchen.

- Türkçe sayfalar: kök klasör (`index.html`, `hizmetler.html`, …)
- Almanca sayfalar: `de/` klasörü (`de/index.html`, `de/leistungen.html`, …)
- Görseller: `img/` · Stil ve betikler: `assets/`

## Yayın

| Ortam | Amaç | İletişim formu |
|---|---|---|
| **Vercel** | Önizleme (Bahar Hanım'a göstermek için) | `api/kontakt.js` (SMTP ile) |
| **Hostinger** | Canlı site | `kontakt.php` (PHP `mail()`) |

### Vercel (önizleme)
1. Vercel → **Add New → Project** → GitHub'daki `bahasonek` reposunu seçin.
2. Framework Preset: **Other**. Build ve Output ayarlarını boş bırakın → **Deploy**.
3. Formun e-posta göndermesi için **Settings → Environment Variables**:
   - `SMTP_HOST` (ör. `smtp.hostinger.com`)
   - `SMTP_PORT` (`465`)
   - `SMTP_USER` (ör. `info@alanadi.de`)
   - `SMTP_PASS` (o posta kutusunun şifresi)
   - `MAIL_TO` (isteğe bağlı, varsayılan: `baharsonek.official@gmail.com`)

   Değişkenleri ekledikten sonra **Redeploy** yapın. Ayarlanmazsa form hata mesajı gösterir; WhatsApp düğmesi her durumda çalışır.
4. Önizleme arama motorlarına kapalıdır (`vercel.json` → `X-Robots-Tag: noindex`, `robots.txt`).

### Hostinger (canlı)
1. `public_html` klasörüne şu dosyaları yükleyin: tüm `.html` dosyaları, `de/`, `assets/`, `img/`, `kontakt.php`, `robots.txt`.
   (`api/`, `tools/`, `vercel.json`, `package.json`, `.vercelignore` gerekmez.)
2. `kontakt.php` içindeki `$GONDEREN` satırını alan adındaki gerçek posta kutusuyla değiştirin (ör. `info@alanadi.de`).
3. `robots.txt` içeriğini canlıya alırken şu hale getirin:
   ```
   User-agent: *
   Allow: /
   ```
4. SSL'i açın, formdan TR ve DE birer deneme mesajı gönderin.

## İçerik güncelleme

- **Haberler:** `assets/haberler.js` (Türkçe) ve `assets/haberler-de.js` (Almanca) – yeni kaydı listenin en üstüne ekleyin. Görsel yolları: Türkçe `img/…`, Almanca `../img/…`.
- **Sayfa metinleri:** HTML sayfaları `tools/build.py` (Türkçe) ve `tools/build_de.py` (Almanca) dosyalarından üretilir. Metni orada değiştirip şunu çalıştırın:
  ```
  python3 tools/build.py
  ```
  (HTML dosyalarını doğrudan düzenlerseniz bir sonraki derlemede üzerine yazılır.)

## Gizlilik (DSGVO)

- Google Haritalar ve YouTube yalnızca ziyaretçi onayıyla yüklenir (`assets/consent.js`). Seçim tarayıcıda saklanır, çerez kullanılmaz.
- **Açık nokta:** Yazı tipleri hâlâ Google Fonts'tan yükleniyor. Yayından önce `assets/fonts/` altına yerel olarak alınmalı.
- Impressum ve Datenschutz metinlerindeki işaretli (sarı) yerler yayından önce tamamlanmalı ve bir uzmana kontrol ettirilmeli.
