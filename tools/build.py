# Bahar Sonek sitesi – sayfa oluşturucu (ortak header/footer)
import os, re
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo kökü
WA = "https://wa.me/4915202614684"
TEL = "tel:+4915202614684"

I = {  # ikonlar (stroke)
 'doc':'<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 12h7M9 16h5"/><path d="m15 19 5-5 1.5 1.5-5 5H15z"/>',
 'bag':'<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
 'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 'letter':'<path d="M6 3h12v18H6z"/><path d="M9 8h6M9 12h6M9 16h4"/>',
 'chat':'<path d="M4 5h16v11H9l-5 4z"/><path d="M8 10.5h.01M12 10.5h.01M16 10.5h.01"/>',
 'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
 'house':'<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><circle cx="12" cy="15" r="2.5"/>',
 'chart':'<path d="M4 20V10M10 20V6M16 20v-8M22 20H2"/><path d="m4 7 6-4 6 5 5-4"/>',
 'cap':'<path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11v5c3 2.5 9 2.5 12 0v-5M22 9v6"/>',
 'camera':'<path d="M4 7h4l2-3h4l2 3h4v13H4z"/><circle cx="12" cy="13" r="4"/>',
 'mega':'<path d="M3 10v4h4l7 5V5L7 10z"/><path d="M18 8a5 5 0 0 1 0 8"/>',
 'ring':'<circle cx="12" cy="15" r="6"/><path d="m9 5 3-3 3 3-3 4z"/>',
 'mic':'<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
 'key':'<circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M17 6l3 3M14 9l2 2"/>',
 'tv':'<rect x="3" y="7" width="18" height="13" rx="2"/><path d="m8 3 4 4 4-4"/>',
 'news':'<path d="M4 5h13v14H6a2 2 0 0 1-2-2z"/><path d="M17 9h3v8a2 2 0 0 1-2 2M8 9h5M8 13h5"/>',
 'trophy':'<path d="M8 4h8v6a4 4 0 0 1-8 0z"/><path d="M8 6H4v2a4 4 0 0 0 4 4M16 6h4v2a4 4 0 0 1-4 4M12 14v4M8 21h8"/>',
 'phone':'<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 'pin':'<path d="M12 21s-7-6.5-7-12a7 7 0 0 1 14 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 'insta':'<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
 'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'shield':'<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 'bolt':'<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 'heart':'<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"/>',
 'users':'<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-4 3-6 7-6s7 2 7 6"/><circle cx="17" cy="7" r="2.5"/><path d="M17 12c3 0 5 2 5 5"/>',
 'star':'<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
 'arrow':'<path d="M5 12h14M13 6l6 6-6 6"/>',
 'book':'<path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4z"/><path d="M20 4h-4a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h5z"/>',
}
def ic(n): return f'<span class="ico"><svg viewBox="0 0 24 24">{I[n]}</svg></span>'
def svg(n, extra=''): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" {extra}>{I[n]}</svg>'

# Kemerli portre: arka katman kemerin içinde kırpılır, ön katman yalnızca baş kısmını çerçevenin önüne taşır.
def fx_portrait(src='img/bahar-cutout.webp', w=582, h=995):
    return f'''<div class="fx-stage">
      <span class="fx-halo"></span>
      <div class="fx-panel"><img class="fx-back" src="{src}" alt="Bahar Sonek" width="{w}" height="{h}"></div>
      <img class="fx-front" src="{src}" alt="" aria-hidden="true" width="{w}" height="{h}">
    </div>'''
FX_PORTRAIT = fx_portrait()

WA_SVG = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.4-.7-2.8-1.1-4.6-4-4.8-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2.1 1-2.4c.3-.3.6-.3.8-.3h.6c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.3 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 .9c.3.2.5.2.5.4.1.1.1.7-.1 1.2z"/></svg>'
FB_SVG = '<svg viewBox="0 0 24 24"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v8h4v-8h3l1-4h-4V8z"/></svg>'
IG_SVG = '<svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.4a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM16.5 2h-9A5.5 5.5 0 0 0 2 7.5v9A5.5 5.5 0 0 0 7.5 22h9a5.5 5.5 0 0 0 5.5-5.5v-9A5.5 5.5 0 0 0 16.5 2zm3.7 14.5a3.7 3.7 0 0 1-3.7 3.7h-9a3.7 3.7 0 0 1-3.7-3.7v-9a3.7 3.7 0 0 1 3.7-3.7h9a3.7 3.7 0 0 1 3.7 3.7z"/></svg>'
TT_SVG = '<svg viewBox="0 0 24 24"><path d="M16.5 2h-3.3v13.4a2.9 2.9 0 1 1-2.9-2.9c.3 0 .6 0 .9.1V9.2a6.3 6.3 0 1 0 5.3 6.2V8.6a7.6 7.6 0 0 0 4.4 1.4V6.7a4.4 4.4 0 0 1-4.4-4.7z"/></svg>'
YT_SVG = '<svg viewBox="0 0 24 24"><path d="M22 7.2a3 3 0 0 0-2.1-2.1C18 4.6 12 4.6 12 4.6s-6 0-7.9.5A3 3 0 0 0 2 7.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 16.8a3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-4.8 31 31 0 0 0-.4-4.8zM10 15.1V8.9l5.2 3.1z"/></svg>'

NAV = [('index.html','Ana Sayfa'),('hizmetler.html','Hizmetler'),('hakkimizda.html','Hakkımızda'),
       ('medya-oduller.html','Medya & Ödüller'),('fotografcilik.html','Fotoğrafçılık'),
       ('dgk.html','D.G.K.'),('haberler.html','Haberler'),('iletisim.html','İletişim')]
SOCIAL = f'''<div class="social">
  <a href="https://www.facebook.com/baharsonek.official" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a>
  <a href="https://www.youtube.com/@baharsonek2023" target="_blank" rel="noopener" aria-label="YouTube">{YT_SVG}</a>
</div>'''

LANG = 'tr'
PAIRS = [('index.html','index.html'),('hizmetler.html','leistungen.html'),('hakkimizda.html','ueber-uns.html'),
         ('medya-oduller.html','medien-auszeichnungen.html'),('fotografcilik.html','fotografie.html'),('dgk.html','dgk.html'),
         ('haberler.html','aktuelles.html'),('iletisim.html','kontakt.html'),('impressum.html','impressum.html'),('datenschutz.html','datenschutz.html')]
TR2DE = dict(PAIRS); DE2TR = {d:t for t,d in PAIRS}
NAV_DE = [('index.html','Startseite'),('leistungen.html','Leistungen'),('ueber-uns.html','Über uns'),
          ('medien-auszeichnungen.html','Medien & Preise'),('fotografie.html','Fotografie'),
          ('dgk.html','D.G.K.'),('aktuelles.html','Aktuelles'),('kontakt.html','Kontakt')]
UI = {
 'tr': dict(nav=NAV, home='Ana Sayfa', menu='Ana menü', burger='Menüyü aç', cta='Randevu Al', wa='WhatsApp ile yazın',
            topr='Kirchstr. 33 · 45879 Gelsenkirchen', other='DE', other_title='Deutsche Version',
            ftxt="Doğru destek, güçlü yarınlar. Gelsenkirchen'den Almanya'nın dört bir yanına; resmi işlerden uluslararası danışmanlığa güvenilir, hızlı ve doğru çözümler.",
            fpages='Sayfalar', fsvc='Hizmetler', fcontact='İletişim', country='Almanya', svc='hizmetler.html',
            svclinks=[('resmi','Devlet daireleri işlemleri'),('resmi','Jobcenter işlemleri'),('resmi','Yabancılar dairesi'),('resmi','Türkçe – Almanca çeviri'),('uluslararasi','Yurt dışı vatandaşlık'),('uluslararasi','Gayrimenkul yatırımı')],
            newsjs='assets/haberler.js'),
 'de': dict(nav=NAV_DE, home='Startseite', menu='Hauptmenü', burger='Menü öffnen', cta='Termin vereinbaren', wa='Per WhatsApp schreiben',
            topr='Kirchstr. 33 · 45879 Gelsenkirchen', other='TR', other_title='Türkçe sürüm',
            ftxt='Richtige Unterstützung, starke Zukunft. Von Gelsenkirchen aus für ganz Deutschland: verlässliche, schnelle und richtige Lösungen – vom Behördenbrief bis zur internationalen Beratung.',
            fpages='Seiten', fsvc='Leistungen', fcontact='Kontakt', country='Deutschland', svc='leistungen.html',
            svclinks=[('behoerden','Behördliche Angelegenheiten'),('behoerden','Jobcenter-Angelegenheiten'),('behoerden','Ausländerbehörde'),('behoerden','Übersetzungen Türkisch – Deutsch'),('international','Staatsbürgerschaften im Ausland'),('international','Immobilieninvestitionen')],
            newsjs='assets/haberler-de.js'),
}

def page(fn, title, desc, body):
    u = UI[LANG]
    nav = ''.join(f'<a href="{h}"{" class=active" if h==fn else ""}>{t.replace("&","&amp;")}</a>' for h,t in u['nav'])
    other = ('de/' + TR2DE.get(fn,'index.html')) if LANG=='tr' else ('../' + DE2TR.get(fn,'index.html'))
    tr_href = fn if LANG=='tr' else '../'+DE2TR.get(fn,'index.html')
    de_href = 'de/'+TR2DE.get(fn,'index.html') if LANG=='tr' else fn
    html = f'''<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="img/portrait-1.jpg">
<meta name="theme-color" content="#0c0a07">
<link rel="alternate" hreflang="tr" href="{tr_href}">
<link rel="alternate" hreflang="de" href="{de_href}">
<link rel="icon" href="img/logo-bs-badge.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="topbar"><div class="wrap">
  <div class="tb-l"><a href="{TEL}">☎ 01520 – 2614684</a><a href="mailto:baharsonek.official@gmail.com">✉ baharsonek.official@gmail.com</a></div>
  <div class="tb-r">{u['topr']} · <span class="langs"><a href="{tr_href}"{' class="on"' if LANG=='tr' else ''} hreflang="tr">Türkçe</a> | <a href="{de_href}"{' class="on"' if LANG=='de' else ''} hreflang="de">Deutsch</a></span></div>
</div></div>
<header class="site"><div class="wrap nav">
  <a href="index.html" class="brand"><img src="img/logo-cv.jpg" alt="Bahar Sonek logo"><span class="bn"><b>Bahar <em class="gold">Sonek</em></b><span>CREATIVE DIENSTLEISTUNGEN</span></span></a>
  <nav class="menu" aria-label="{u['menu']}">{nav}</nav>
  <a class="lang-sw" href="{other}" hreflang="{u['other'].lower()}" title="{u['other_title']}">{u['other']}</a>
  <a class="btn btn-gold cta-head" href="{WA}" target="_blank" rel="noopener">{u['cta']}</a>
  <button class="burger" aria-label="{u['burger']}" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
  <div class="fgrid">
    <div class="fbrand">
      <img src="img/logo-bs-script.jpg" alt="Bahar Sonek Creative">
      <p>{u['ftxt']}</p>
      {SOCIAL}
    </div>
    <div><h4>{u['fpages']}</h4><ul>{''.join(f'<li><a href="{h}">{t.replace("&","&amp;")}</a></li>' for h,t in u['nav'])}</ul></div>
    <div><h4>{u['fsvc']}</h4><ul>{''.join(f'<li><a href="{u["svc"]}#{a}">{t}</a></li>' for a,t in u['svclinks'])}</ul></div>
    <div><h4>{u['fcontact']}</h4><ul>
      <li><a href="{TEL}">01520 – 2614684</a></li>
      <li><a href="mailto:baharsonek.official@gmail.com">baharsonek.official@gmail.com</a></li>
      <li><a href="mailto:baharsonekcreative@gmail.com">baharsonekcreative@gmail.com</a></li>
      <li>Kirchstr. 33<br>45879 Gelsenkirchen, {u['country']}</li>
    </ul></div>
  </div>
  <div class="fbottom">
    <span>© <span data-year>2026</span> Bahar Sonek · Creative Dienstleistungen</span>
    <span><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a> · <a href="#" data-consent-open>{'Cookie-Einstellungen' if LANG=='de' else 'Çerez ayarları'}</a> · <a href="{other}">{u['other_title']}</a></span>
  </div>
</div></footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="{u['wa']}">{WA_SVG}</a>
<script src="{u['newsjs']}"></script>
<script src="assets/haberler-render.js"></script>
<script src="assets/consent.js"></script>
<script src="assets/main.js"></script>
</body>
</html>'''
    out = OUT if LANG=='tr' else os.path.join(OUT,'de')
    os.makedirs(out, exist_ok=True)
    if LANG=='de':
        html = re.sub(r'((?:src|href|content)=")(img|assets)/', r'\1../\2/', html)
    with open(os.path.join(out, fn), 'w', encoding='utf-8') as f: f.write(html)

def hero(eyebrow, h1, p, crumb):
    return f'''<section class="page-hero"><div class="wrap">
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  <p>{p}</p>
  <div class="crumbs"><a href="index.html">{UI[LANG]['home']}</a> &nbsp;/&nbsp; {crumb}</div>
</div></section>'''

def cta(h=None, p=None):
    de = LANG=='de'
    h = h or ('Haben Sie eine Frage?' if de else 'Bir sorunuz mu var?')
    p = p or ('Bringen Sie Ihre Unterlagen, Fragen oder Pläne mit – den Rest lösen wir gemeinsam. Schreiben Sie uns für einen Termin.' if de else 'Evraklarınızı, sorularınızı ya da hayallerinizi getirin; gerisini birlikte çözelim. Randevu için hemen yazın.')
    return f'''<section class="cta-band"><div class="wrap reveal">
  <span class="eyebrow">{'Termin &amp; Information' if de else 'Randevu &amp; Bilgi'}</span>
  <h2>{h}</h2>
  <p>{p}</p>
  <div class="btns"><a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{'Per WhatsApp schreiben' if de else "WhatsApp'tan Yazın"}</a><a class="btn btn-ghost" href="{TEL}">01520 – 2614684</a></div>
</div></section>'''

QUOTE_VIZYON = '''<div class="quote reveal"><div class="qm">“</div><blockquote>Vizyonumuz, global dünyada güçlü adımlar atarak sizinle birlikte daha iyi bir geleceğe yürümektir.</blockquote><cite>Bahar Sonek</cite></div>'''

AWARDS = [
 ('award-2.jpg','Yılın En Başarılı İş Kadını','Avrupa\'nın Yıldızları – Neriman Dergisi'),
 ('award-1.jpg','Teşekkür Belgesi 2025','Business Channel Türk TV · JMG-Group Gelsenkirchen'),
 ('award-4.jpg','Eğitim Katkısı Teşekkür Belgesi','Business Channel Türk TV stajyer öğrencileri, 2025'),
 ('award-3.jpg','4. Ödül &amp; Gala Gecesi','Derewa sunar – Neriman Dergisi'),
]
def poster_grid(items, cols='g4'):
    return f'<div class="grid {cols} posters">' + ''.join(f'''<figure class="poster reveal" data-zoom><img src="img/fb/{i}" alt="{t}"><figcaption><b>{t}</b>{c}</figcaption></figure>''' for i,t,c in items) + '</div>'


VIDEOS = [
 ('SR9uS85WVeE', {'tr':'Bahar Sonek: Almanya\'dan Dünyaya Uzanan Başarı Hikayesi','de':'Bahar Sonek: Eine Erfolgsgeschichte von Deutschland in die Welt'}),
 ('-rHRMLmHeVI', {'tr':'Video röportaj','de':'Video-Interview'}),
 ('HSrAraRoJ5o', {'tr':'Video röportaj','de':'Video-Interview'}),
]
def video_grid():
    de = LANG=='de'
    play = 'Videoyu oynat' if not de else 'Video abspielen'
    yt = "YouTube'da aç" if not de else 'Auf YouTube öffnen'
    cards = ''.join(f'''<div class="video reveal">
      <button class="video-ph" data-yt="{vid}" aria-label="{play}: {t[LANG]}"><img src="img/logo-bs-badge.png" alt=""><span class="play"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span></button>
      <div class="video-meta"><b>{t[LANG]}</b><a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">{yt} →</a></div>
    </div>''' for vid,t in VIDEOS)
    note = ('Videoyu başlattığınızda YouTube (Google) ile bağlantı kurulur ve veri aktarılır. Ayrıntılar Datenschutz sayfasında.' if not de
            else 'Beim Abspielen wird eine Verbindung zu YouTube (Google) hergestellt und es werden Daten übertragen. Details in der Datenschutzerklärung.')
    return f'<div class="grid g3 videos">{cards}</div><p class="muted" style="text-align:center;font-size:.82rem;margin-top:18px">{note}</p>'

def dgk_feature():
    de = LANG=='de'
    if de:
        eb, h, sub = 'Ehrenamt · Weltjugendrat', 'Regionalpräsidentin <span class="gold">Deutschland</span>', 'Dünya Gençlik Konseyi – Weltjugendrat'
        p = 'Bahar Sonek wurde von Generalpräsident Hüseyin Celep zur Regionalpräsidentin des Weltjugendrats (D.G.K.) für Deutschland ernannt. In dieser Rolle setzt sie sich für Bildung, Chancengleichheit und Zukunftsperspektiven junger Menschen und Familien ein – in Deutschland und in Zusammenarbeit mit der Türkei.'
        pills = ['Jugendsolidarität','Bildungsförderung','Chancengleichheit','Unternehmertum &amp; Innovation','Internationale Zusammenarbeit']
        b1, b2, motto = 'Zur D.G.K.-Seite', 'Ehrenamtlich mitmachen', '„Die Kraft der Jugend – die Zukunft der Welt“'
        link2 = 'kontakt.html?konu=D.G.K.'
    else:
        eb, h, sub = 'Toplumsal Görev · D.G.K.', 'Almanya Bölge <span class="gold">Başkanı</span>', 'Dünya Gençlik Konseyi'
        p = 'Bahar Sonek, Dünya Gençlik Konseyi Genel Başkanı Hüseyin Celep tarafından D.G.K. Almanya Bölge Başkanı olarak görevlendirildi. Bu görevle Almanya\'daki gençlerin ve ailelerin eğitimi, fırsat eşitliği ve geleceği için çalışıyor; Türkiye ile Almanya arasında köprü kuruyor.'
        pills = ['Gençlik Dayanışması','Eğitim Desteği','Fırsat Eşitliği','Girişimcilik &amp; İnovasyon','Uluslararası İş Birliği']
        b1, b2, motto = 'D.G.K. Almanya sayfası', 'Gönüllü Ol', '“Gençliğin Gücü, Dünyanın Geleceği”'
        link2 = 'iletisim.html?konu=D.G.K.'
    pl = ''.join(f'<span class="pill">{x}</span>' for x in pills)
    return f'''<section class="dgk-feature-wrap"><div class="wrap">
  <div class="dgk-feature reveal">
    <div class="dgk-emblem"><img src="img/dgk-logo.png" alt="Dünya Gençlik Konseyi"><span class="dgk-badge">{'Regionalpräsidentin' if de else 'Bölge Başkanı'}</span></div>
    <div class="dgk-text">
      <span class="eyebrow">{eb}</span>
      <p class="dgk-sub">{sub}</p>
      <h2>{h}</h2>
      <p class="dgk-name">Bahar Sonek</p>
      <p>{p}</p>
      <div class="pills">{pl}</div>
      <p class="dgk-motto script">{motto}</p>
      <div class="btns"><a class="btn btn-gold" href="dgk.html">{b1} {svg('arrow')}</a><a class="btn btn-ghost" href="{link2}">{b2}</a></div>
    </div>
    <figure class="dgk-poster" data-zoom><img src="img/fb/dgk-almanya-afis.jpg" alt="D.G.K. Almanya Bölge Başkanlığı"></figure>
  </div>
</div></section>'''

def dgk_role_hero():
    de = LANG=='de'
    crumb = f'<a href="index.html">{UI[LANG]["home"]}</a> &nbsp;/&nbsp; D.G.K.'
    if de:
        t1, t2 = 'Weltjugendrat (Dünya Gençlik Konseyi)', 'Regionalpräsidentin Deutschland'
        p = 'Ernannt von Generalpräsident Hüseyin Celep, vertritt Bahar Sonek den Weltjugendrat in der Bundesrepublik Deutschland.'
        facts = [('Amt','Regionalpräsidentin Deutschland'),('Ernannt durch','Generalpräsident Hüseyin Celep'),('Sitz in Deutschland','Kirchstr. 33, Gelsenkirchen')]
    else:
        t1, t2 = 'Dünya Gençlik Konseyi', 'Almanya Bölge Başkanı'
        p = 'Dünya Gençlik Konseyi Genel Başkanı Hüseyin Celep tarafından görevlendirilen Bahar Sonek, Almanya Federal Cumhuriyeti sınırları içinde konseyi temsil ediyor.'
        facts = [('Görev','D.G.K. Almanya Bölge Başkanı'),('Görevlendiren','Genel Başkan Hüseyin Celep'),('Almanya merkezi','Kirchstr. 33, Gelsenkirchen')]
    fl = ''.join(f'<div><small>{a}</small><b>{b}</b></div>' for a,b in facts)
    return f'''<section class="role-hero"><div class="wrap role-grid">
  <div class="reveal">
    <span class="eyebrow">{t1}</span>
    <h1><span class="gold">{t2}</span><br>Bahar Sonek</h1>
    <p class="lead">{p}</p>
    <div class="role-facts">{fl}</div>
    <div class="crumbs" style="text-align:left">{crumb}</div>
  </div>
  <div class="role-portrait fx-portrait reveal">
    {FX_PORTRAIT}
    <img class="role-logo" src="img/dgk-logo.png" alt="Dünya Gençlik Konseyi">
  </div>
</div></section>'''

def map_section():
    de = LANG=='de'
    q = 'Kirchstr.+33,+45879+Gelsenkirchen'
    lbl = ('Unser Büro','Kirchstr. 33<br>45879 Gelsenkirchen','Route planen','In Google Maps öffnen','Karte: Kirchstr. 33, 45879 Gelsenkirchen') if de else \
          ('Ofisimiz','Kirchstr. 33<br>45879 Gelsenkirchen','Yol Tarifi','Google Maps\'te aç','Harita: Kirchstr. 33, 45879 Gelsenkirchen')
    return f'''<section class="map-top"><div class="wrap">
  <div class="map-live reveal">
    <div class="map-frame" data-consent-src="https://www.google.com/maps?q={q}&hl={LANG}&z=16&output=embed" data-title="{lbl[4]}">
      <div class="map-blocked">
        <p>{'Zum Anzeigen der Karte wird Google Maps geladen. Dabei werden Daten an Google übertragen.' if de else "Haritayı göstermek için Google Haritalar yüklenir; bu sırada Google'a veri aktarılır."} <a href="datenschutz.html">{'Mehr erfahren' if de else 'Ayrıntılar'}</a></p>
        <button class="btn btn-gold" data-consent-accept-media>{'Karte laden' if de else 'Haritayı yükle'}</button>
        <small>{'Ihre Auswahl wird gespeichert. Ändern unter „Cookie-Einstellungen“.' if de else 'Seçiminiz kaydedilir. „Çerez ayarları“ndan değiştirebilirsiniz.'}</small>
      </div>
    </div>
    <div class="map-card">
      {ic('pin')}
      <div><small>{lbl[0]}</small><b>{lbl[1]}</b></div>
      <div class="btns"><a class="btn btn-gold" href="https://www.google.com/maps/dir/?api=1&destination={q}" target="_blank" rel="noopener">{svg('pin')} {lbl[2]}</a><a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&query={q}" target="_blank" rel="noopener">{lbl[3]}</a></div>
    </div>
  </div>
</div></section>'''

def awards_grid(items=None):
    return '<div class="grid g4 awards">' + ''.join(f'''<figure class="award reveal" data-zoom><img src="img/{i}" alt="{t}"><figcaption><b>{t}</b>{s}</figcaption></figure>''' for i,t,s in (items or AWARDS)) + '</div>'

# ───────────── ANA SAYFA ─────────────
page('index.html','Bahar Sonek – Doğru Destek, Güçlü Yarınlar | Gelsenkirchen',
 "Gelsenkirchen'de resmi evrak, Jobcenter, Yabancılar Dairesi işlemleri, Türkçe–Almanca çeviri ve uluslararası danışmanlık. Bahar Sonek Creative Dienstleistungen.", f'''
<section class="hero"><div class="wrap hero-grid">
  <div class="reveal">
    <span class="eyebrow">D.G.K. Almanya Bölge Başkanı · International Business Manager</span>
    <h1>Doğru destek,<br><span class="gold">güçlü yarınlar.</span></h1>
    <p class="lead">Almanya'daki resmi işlerinizden uluslararası yatırım ve vatandaşlık süreçlerine kadar her adımda yanınızdayız. Türkçe anlatıyor, Almanca çözüyoruz.</p>
    <div class="btns">
      <a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{svg('chat')} Ücretsiz Ön Görüşme</a>
      <a class="btn btn-ghost" href="hizmetler.html">Hizmetlerimiz {svg('arrow')}</a>
    </div>
    <div class="hero-stats">
      <div><b>12+ yıl</b>profesyonel deneyim</div>
      <div><b>TR ⇄ DE</b>iki dilde hizmet</div>
      <div><b>D.G.K.</b>Almanya Bölge Başkanı</div>
    </div>
  </div>
  <div class="portrait fx-portrait reveal">
    {FX_PORTRAIT}
    <div class="float-card fc-1"><span class="ic"><svg viewBox="0 0 24 24">{I['trophy']}</svg></span><span><b>Yılın En Başarılı İş Kadını</b>Avrupa'nın Yıldızları</span></div>
    <a href="dgk.html" class="float-card fc-2"><img src="img/dgk-logo.png" alt="" style="width:40px;height:40px"><span><b>Dünya Gençlik Konseyi</b>Almanya Bölge Başkanı</span></a>
  </div>
</div></section>

{dgk_feature()}

<section class="band" style="padding:80px 0"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Hizmet Alanlarımız</span><h2>Bürokrasiyi <span class="gold">bize bırakın</span></h2><p>Mektup, form, başvuru, randevu… Hepsini sizin için anlaşılır ve takip edilebilir hale getiriyoruz.</p></div>
  <div class="grid g4">
    <a href="hizmetler.html#resmi" class="card reveal">{ic('doc')}<h3>Devlet Daireleri</h3><p>Resmi evrak, form, başvuru ve kurum yazışmalarınızda yanınızdayız.</p><span class="more">Detaylar {svg('arrow','width="16"')}</span></a>
    <a href="hizmetler.html#resmi" class="card reveal">{ic('bag')}<h3>Jobcenter</h3><p>Yazılar, başvurular, randevular ve tüm süreçlerde doğru destek.</p><span class="more">Detaylar {svg('arrow','width="16"')}</span></a>
    <a href="hizmetler.html#resmi" class="card reveal">{ic('mail')}<h3>Yabancılar Dairesi</h3><p>Oturum, vize, başvuru ve randevu süreçlerinde profesyonel destek.</p><span class="more">Detaylar {svg('arrow','width="16"')}</span></a>
    <a href="hizmetler.html#resmi" class="card reveal">{ic('chat')}<h3>Türkçe – Almanca Çeviri</h3><p>Resmi evrak, dilekçe ve belgeleriniz için güvenilir çeviri.</p><span class="more">Detaylar {svg('arrow','width="16"')}</span></a>
  </div>
</div></section>

<section><div class="wrap split">
  <div class="photo gold-frame reveal"><img src="img/tv-3.jpg" alt="Bahar Sonek portre" style="aspect-ratio:4/5"></div>
  <div class="reveal">
    <span class="eyebrow">Bahar Sonek Kimdir?</span>
    <h2>Adana'dan Gelsenkirchen'e, <span class="gold">ilham veren bir yolculuk</span></h2>
    <p>1982'de Gelsenkirchen'de doğdu; aslen Adanalı. Eğitimini Almanya'da Gymnasium'da tamamladı ve yaklaşık 12 yıl önce sigorta sektörüyle profesyonel yolculuğuna başladı.</p>
    <p>Bilgi ve deneyimini büyüterek kendi ofisini kurdu, yurt dışı vatandaşlıklar alanında uzmanlaştı ve çalışmaları çeşitli ödüllerle taçlandı. Bugün farklı alanlarda aktif, vizyoner bir girişimci kadın.</p>
    <div class="btns" style="margin-top:1.6rem"><a class="btn btn-ghost" href="hakkimizda.html">Hikâyenin Tamamı {svg('arrow')}</a></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Uluslararası Danışmanlık</span><h2>Hizmetlerimiz <span class="script gold" style="font-size:1.25em">ve Vizyonumuz</span></h2><p>Uluslararası danışmanlık, yatırım ve vatandaşlık alanlarında güvenilir çözümler sunarak hayallerinizi gerçeğe dönüştürüyoruz.</p></div>
  <div class="grid g4">
    <a href="hizmetler.html#uluslararasi" class="card reveal">{ic('globe')}<h3>Yurt Dışı Vatandaşlık</h3><p>Güvenilir bilgi, doğru yönlendirme ve profesyonel danışmanlık.</p></a>
    <a href="hizmetler.html#uluslararasi" class="card reveal">{ic('house')}<h3>Gayrimenkul Yatırımı</h3><p>Kazançlı yatırım fırsatlarıyla geleceğinizi güvenceye alın.</p></a>
    <a href="hizmetler.html#uluslararasi" class="card reveal">{ic('chart')}<h3>Yatırım Danışmanlığı</h3><p>Doğru stratejiler ve uluslararası ağımızla finansal hedeflerinize.</p></a>
    <a href="hizmetler.html#uluslararasi" class="card reveal">{ic('cap')}<h3>Eğitim &amp; Kariyer</h3><p>Yurt dışında eğitim ve kariyer fırsatlarıyla geleceğinizi şekillendirin.</p></a>
  </div>
  <div style="margin-top:64px">{QUOTE_VIZYON}</div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Teşekkür ve Başarı Belgeleri</span><h2>Emeğin <span class="gold">karşılığı</span></h2><p>Girişimcilik, kadın gücü ve uluslararası danışmanlık alanlarındaki katkılarımızdan dolayı aldığımız ödüller bizler için büyük bir onur kaynağıdır.</p></div>
  {awards_grid()}
  <div class="sec-head reveal" style="margin:80px auto 40px"><span class="eyebrow">2026</span><h2>Ekranda, kapakta, <span class="gold">sahnede</span></h2></div>
  {poster_grid([('altin-meslek-odul.jpg','Yılın En İyi Tercümanı ve Danışmanı','5. Altın Meslek &amp; Kariyer Ödülleri · İstanbul'),('bizden-bil-kapak.jpg','Bizden Bil kapağı','İş ve Sanat Dergisi · Ağustos 2026'),('tele1-canli-yayin.jpg','TELE1 canlı yayın','Almanya–Türkiye İşbirlikleri · 8 Ağustos 2026'),('summit-odul.jpg','Life &amp; Beauty Summit','Ödül töreni')])}
  <div class="btns reveal" style="justify-content:center;margin-top:40px"><a class="btn btn-ghost" href="medya-oduller.html">Medya &amp; Ödüller {svg('arrow')}</a></div>
</div></section>

<section class="band"><div class="wrap split rev">
  <div class="photo reveal"><img src="img/photographer.jpg" alt="Fotoğraf çekimi" style="aspect-ratio:4/5"></div>
  <div class="reveal">
    <span class="eyebrow">Kreatif Hizmetler</span>
    <h2>Özel günlerinizin <span class="gold">en güzel anları</span></h2>
    <p>Zarif, doğal ve unutulmaz fotoğraflarla o günün en güzel anlarını sizin için yakalıyoruz. Düğün, sünnet, kına ve tüm özel günleriniz için organizasyon ve fotoğrafçılık.</p>
    <ul class="checks"><li>Organizasyon &amp; fotoğrafçılık</li><li>Reklam &amp; management</li><li>Türkçe &amp; Almanca röportajlar</li><li>İnşaat · elektrik · kapı/pencere/teras <small class="muted">(çözüm ortaklarımızla)</small></li><li>Emlak / Immobilien</li></ul>
    <a class="btn btn-gold" href="fotografcilik.html">Kreatif Hizmetler {svg('arrow')}</a>
  </div>
</div></section>

<section><div class="wrap">
  <div class="promo reveal">
    <div class="pct">%30</div>
    <div><h3>İndirim fırsatı</h3><p>Seçili danışmanlık hizmetlerimizde %30 indirim. Kampanya koşulları için bize ulaşın.</p></div>
    <a class="btn" href="{WA}" target="_blank" rel="noopener">Fırsatı Yakala</a>
  </div>
</div></section>


<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Güncel</span><h2>Son <span class="gold">haberler</span></h2><p>Facebook sayfamızdan öne çıkan paylaşımlar, etkinlikler ve ödüller.</p></div>
  <div class="news-grid" data-news="3"></div>
  <div class="btns reveal" style="justify-content:center;margin-top:40px"><a class="btn btn-ghost" href="haberler.html">Tüm Haberler {svg('arrow')}</a></div>
</div></section>
{cta('Birlikte güçlüyüz.')}
''')

# ───────────── HİZMETLER ─────────────
def svc(icn,t,p,items=None):
    li = ('<ul class="checks" style="margin:1rem 0 0;font-size:.9rem">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>') if items else ''
    return f'<div class="card hover reveal">{ic(icn)}<h3>{t}</h3><p>{p}</p>{li}</div>'

page('hizmetler.html','Hizmetler – Bahar Sonek | Danışmanlık, Resmi İşler, Çeviri',
 'Devlet daireleri, Jobcenter, Yabancılar Dairesi işlemleri, resmi yazışmalar, Türkçe–Almanca çeviri, yurt dışı vatandaşlık, gayrimenkul ve yatırım danışmanlığı.', f'''
{hero('Hizmetlerimiz','Tüm işlemlerinizde <span class="gold">doğru destek</span>','Güvenilir, hızlı ve doğru çözümler. Almanya\'daki resmi işlerden uluslararası projelerinize kadar.','Hizmetler')}

<section id="resmi"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">01 · Danışmanlık &amp; Resmi İşler</span><h2>Almanya'da <span class="gold">resmi işler</span></h2><p>Mektuplar, formlar ve randevular artık sizi yormasın. Her şeyi Türkçe anlatıyor, Almanca yürütüyoruz.</p></div>
  <div class="grid g3">
    {svc('doc','Devlet Daireleri İşlemleri','Resmi evrak, formlar, başvurular ve kurumlarla yazışmalarınızda yanınızdayız.',['Familienkasse, Elterngeld, Kindergeld','Finanzamt ve sigorta yazışmaları','Belediye (Bürgeramt) işlemleri'])}
    {svc('bag','Jobcenter İşlemleri','Jobcenter yazıları, başvurular, randevular ve tüm süreçlerde doğru destek sağlıyoruz.',['Bürgergeld ilk başvuru','Weiterbewilligungsantrag','Gelen yazıların açıklanması ve yanıtı'])}
    {svc('mail','Yabancılar Dairesi','Yabancılar dairesi işlemleri, oturum, vize, başvuru ve randevu süreçlerinde profesyonel destek.',['Oturum izni başvuru ve uzatma','Vize ve aile birleşimi süreçleri','Randevu ve evrak hazırlığı'])}
    {svc('letter','Resmi Mektup ve Yazışmalar','Resmi mektupların hazırlanması ve doğru şekilde yazılması konusunda yardımcı oluyoruz.',['İtiraz (Widerspruch) yazıları','Kurumlara dilekçe ve bildirimler','Süre takibi ve hatırlatma'])}
    {svc('chat','Türkçe – Almanca Çeviri','Tüm resmi evrak, dilekçe ve belgeleriniz için Türkçe – Almanca çeviri hizmeti.',['Belge ve mektup çevirisi','Görüşmelerde tercüman desteği','Türkçe özet ve açıklama'])}
    <div class="card reveal" style="background:var(--grad);color:#1a1307;border:none;display:flex;flex-direction:column;justify-content:center">
      <h3 style="font-size:1.6rem">Hangi evrak olursa olsun</h3>
      <p style="color:#3a2a0e;margin-bottom:18px">Elinizdeki mektubun fotoğrafını WhatsApp'tan gönderin; ne yapılması gerektiğini birlikte konuşalım.</p>
      <a class="btn" style="background:#1a1307;color:var(--gold2);align-self:flex-start" href="{WA}" target="_blank" rel="noopener">Fotoğrafını Gönder</a>
    </div>
  </div>
</div></section>

<section id="uluslararasi" class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">02 · Uluslararası Danışmanlık</span><h2>Hayallerinizi <span class="gold">gerçeğe</span> dönüştürüyoruz</h2><p>Uluslararası danışmanlık, yatırım ve vatandaşlık alanlarında güvenilir çözümler.</p></div>
  <div class="grid g2">
    {svc('globe','Yurt Dışı Vatandaşlık','Güvenilir bilgi, doğru yönlendirme ve profesyonel danışmanlık ile süreçlerinizi kolaylaştırıyoruz. Yıllardır bu alanda uzmanlaşmış deneyimimizle başvurunuzun her adımında yanınızdayız.')}
    {svc('house','Gayrimenkul Yatırımı','Kazançlı yatırım fırsatlarıyla geleceğinizi güvence altına almanıza destek oluyoruz. Almanya ve yurt dışında emlak alım-satım ve yatırım süreçlerinde danışmanlık.')}
    {svc('chart','Yatırım Danışmanlığı','Doğru stratejiler ve uluslararası ağımızla finansal hedeflerinize ulaşmanıza yardımcı oluyoruz.')}
    {svc('cap','Eğitim ve Kariyer Danışmanlığı','Yurt dışında eğitim ve kariyer fırsatlarıyla geleceğinizi şekillendirmenize katkı sağlıyoruz. Gençler ve aileler için yol gösterici danışmanlık.')}
  </div>
  <div style="margin-top:64px">{QUOTE_VIZYON}</div>
</div></section>

<section id="ek"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">03 · Ek Hizmetler</span><h2>Kreatif &amp; <span class="gold">özel hizmetler</span></h2><p>Ek hizmetlerimizi güvenilir çözüm ortaklarımızla birlikte sunuyoruz.</p></div>
  <div class="grid g3">
    {svc('camera','Organizasyon &amp; Fotoğrafçılık','Özel günleriniz için organizasyon ve profesyonel fotoğraf çekimi.')}
    {svc('mega','Reklam &amp; Management','İşletmeniz ve projeleriniz için reklam, tanıtım ve yönetim desteği.')}
    {svc('ring','Düğün · Sünnet · Kına','Hayatınızın en özel günlerini planlıyor ve ölümsüzleştiriyoruz.')}
    {svc('mic','Türkçe &amp; Almanca Röportajlar','TV ve medya deneyimimizle iki dilde röportaj ve sunum.')}
    {svc('key','Emlak / Immobilien','Kiralık ve satılık gayrimenkullerde arama, aracılık ve danışmanlık.')}
    {svc('house','İnşaat · Elektrik · Kapı/Pencere/Teras','Tadilat, elektrik, kapı-pencere ve teras işleriniz için çözüm ortaklarımızla yanınızdayız.')}
  </div>
  <div class="btns reveal" style="justify-content:center;margin-top:36px"><a class="btn btn-ghost" href="fotografcilik.html">Kreatif hizmetlerin tamamı {svg('arrow')}</a></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Nasıl Çalışıyoruz?</span><h2>Dört adımda <span class="gold">çözüm</span></h2></div>
  <div class="grid g4 steps">
    <div class="card step reveal">{ic('phone')}<h3>İletişim</h3><p>WhatsApp, telefon veya e-posta ile ulaşın, konunuzu kısaca anlatın.</p></div>
    <div class="card step reveal">{ic('clock')}<h3>Randevu</h3><p>Kirchstr. 33'teki ofisimizde size uygun bir zaman belirleyelim.</p></div>
    <div class="card step reveal">{ic('doc')}<h3>İnceleme</h3><p>Evraklarınızı birlikte inceler, yol haritasını Türkçe olarak anlatırız.</p></div>
    <div class="card step reveal">{ic('bolt')}<h3>Takip &amp; Sonuç</h3><p>Yazışma, başvuru ve takibi yürütür, her adımda sizi bilgilendiririz.</p></div>
  </div>
</div></section>

<section><div class="wrap" style="max-width:860px">
  <div class="sec-head reveal"><span class="eyebrow">Sıkça Sorulan Sorular</span><h2>Merak <span class="gold">edilenler</span></h2></div>
  <div class="reveal">
    <details><summary>Randevu almadan ofise gelebilir miyim?</summary><p>Size zaman ayırabilmemiz için önceden WhatsApp veya telefonla randevu almanızı rica ediyoruz.</p></details>
    <details><summary>Hangi evrakları yanımda getirmeliyim?</summary><p>Konuyla ilgili tüm mektuplar, kimlik/pasaport, oturum kartı ve varsa önceki yazışmalar. Emin değilseniz önce fotoğrafını gönderin, listeyi birlikte çıkaralım.</p></details>
    <details><summary>Almanca bilmiyorum, sorun olur mu?</summary><p>Hayır. Tüm süreci Türkçe anlatıyor, kurumlarla Almanca yazışmaları biz yürütüyoruz.</p></details>
    <details><summary>Ücretlendirme nasıl?</summary><p>Ücret, işin kapsamına göre ön görüşmede şeffaf şekilde belirlenir. Güncel kampanyalar için bize ulaşın.</p></details>
  </div>
</div></section>
{cta()}
''')

# ───────────── HAKKIMIZDA ─────────────
page('hakkimizda.html','Hakkımızda – Bahar Sonek Kimdir?',
 "1982 Gelsenkirchen doğumlu, aslen Adanalı girişimci Bahar Sonek'in hikâyesi: sigorta sektöründen kendi ofisine, uluslararası danışmanlıktan ödüllere.", f'''
{hero('Hakkımızda','Bahar Sonek <span class="script gold" style="font-size:1.2em">kimdir?</span>','İçine kapanık bir yapıdan girişken, güçlü ve ilham veren bir kadına uzanan bir yolculuk.','Hakkımızda')}

<section><div class="wrap split">
  <div class="fx-portrait fx-about reveal">{fx_portrait('img/bahar-hakkimizda.webp',360,610)}</div>
  <div class="reveal">
    <span class="eyebrow">Hikâyemiz</span>
    <h2>Topluma fayda sağlamak, <span class="gold">insanlara yol göstermek</span></h2>
    <p>Bahar Sonek, 1982 yılında Gelsenkirchen'de doğdu. Aslen Adanalı olan Sonek, eğitimini Almanya'da Gymnasium'da tamamladı. Yaklaşık 12 yıl önce sigorta sektörüyle Almanya'daki profesyonel yolculuğuna başladı.</p>
    <p>Zamanla bilgi ve deneyimini büyüterek kendi ofisini kurdu; hedefi her zaman daha iyisini yapmak ve gelişmek oldu. Kariyerinin ilerleyen dönemlerinde yurt dışı vatandaşlıklar alanında uzmanlaştı, bu alanda birçok eğitime katıldı ve sürecin sonunda çeşitli ödüllerle başarısını taçlandırdı.</p>
    <p>Topluma fayda sağlamak, insanlara yol göstermek onun en temel motivasyonu oldu. Eskiden daha içine kapanık bir yapıya sahipken, bu yolculuk onu girişken, güçlü ve ilham veren bir kadına dönüştürdü. Bugün Bahar Sonek, farklı alanlarda aktif olarak faaliyet gösteren, vizyoner bir girişimci kadın olarak yoluna kararlılıkla devam ediyor.</p>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Yolculuk</span><h2>Adım adım <span class="gold">bugüne</span></h2></div>
  <div class="timeline">
    <div class="tl reveal"><div class="dot">1</div><div><small>1982</small><h3>Gelsenkirchen'de doğdu</h3><p>Aslen Adanalı bir ailenin kızı olarak Gelsenkirchen'de dünyaya geldi.</p></div></div>
    <div class="tl reveal"><div class="dot">2</div><div><small>Eğitim</small><h3>Gymnasium</h3><p>Eğitim hayatını Almanya'da Gymnasium'da tamamladı.</p></div></div>
    <div class="tl reveal"><div class="dot">3</div><div><small>~12 yıl önce</small><h3>Sigorta sektörü</h3><p>Almanya'daki profesyonel yolculuğuna sigorta sektörüyle başladı.</p></div></div>
    <div class="tl reveal"><div class="dot">4</div><div><small>Girişimcilik</small><h3>Kendi ofisi</h3><p>Bilgi ve deneyimini büyüterek Gelsenkirchen'de kendi ofisini kurdu: Creative Dienstleistungen.</p></div></div>
    <div class="tl reveal"><div class="dot">5</div><div><small>Uzmanlık</small><h3>Uluslararası danışmanlık</h3><p>Yurt dışı vatandaşlıklar alanında uzmanlaştı, birçok eğitime katıldı.</p></div></div>
    <div class="tl reveal"><div class="dot">6</div><div><small>Bugün</small><h3>Ödüller, medya ve D.G.K.</h3><p>"Yılın Uluslararası Başarı Gösteren En İyi Tercümanı ve Danışmanı" (2026) ve Avrupa'nın Yıldızları "Yılın En Başarılı İş Kadını" ödülleri; TELE1 ve Business Channel Türk TV'de programlar; Dünya Gençlik Konseyi Almanya Bölge Başkanlığı.</p></div></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Değerlerimiz</span><h2>Bizi biz yapan <span class="gold">ilkeler</span></h2></div>
  <div class="grid g4">
    <div class="card reveal">{ic('shield')}<h3>Güven</h3><p>Bilgileriniz ve belgeleriniz bizimle güvende; gizlilik önceliğimiz.</p></div>
    <div class="card reveal">{ic('bolt')}<h3>Hız</h3><p>Süreleri takip eder, işlemlerinizi zamanında sonuçlandırırız.</p></div>
    <div class="card reveal">{ic('star')}<h3>Doğruluk</h3><p>Doğru bilgi, doğru yönlendirme: adımızdaki "Doğru Destek" sözü.</p></div>
    <div class="card reveal">{ic('heart')}<h3>Samimiyet</h3><p>Her müşterimizi ailemizden biri gibi dinler, Türkçe anlatırız.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Sahada</span><h2>Toplantılar, etkinlikler, <span class="gold">buluşmalar</span></h2></div>
  {poster_grid([('pkm-toplanti.jpg','İş görüşmeleri','PKM Unternehmensgruppe'),('musiad-koln.jpg','MÜSİAD NRW-Köln','"Türkiye\'ye Yatırımda Yeni Dönem"'),('summit-3.jpg','Life &amp; Beauty Summit','Davetli konuk'),('dgk-genel-merkez.jpg','D.G.K. Genel Merkez','Ekip toplantısı')])}
  <div style="margin-top:70px">{QUOTE_VIZYON}</div>
</div></section>

<section><div class="wrap split rev">
  <div class="photo reveal"><img src="img/dgk-ofis.jpg" alt="D.G.K. Almanya" style="aspect-ratio:4/3"></div>
  <div class="reveal">
    <span class="eyebrow">Gönüllü Görev</span>
    <h2>Dünya Gençlik Konseyi <span class="gold">Almanya Bölge Başkanı</span></h2>
    <p>İş hayatının yanında gençlere yönelik sosyal sorumluluk çalışmalarını, Dünya Gençlik Konseyi Almanya Bölge Başkanı olarak sürdürüyor.</p>
    <a class="btn btn-ghost" href="dgk.html">D.G.K. Almanya {svg('arrow')}</a>
  </div>
</div></section>
{cta('Hikâyenizi dinlemeye hazırız.')}
''')

# ───────────── MEDYA & ÖDÜLLER ─────────────
page('medya-oduller.html','Medya & Ödüller – Bahar Sonek',
 "Business Channel Türk TV ve TLC'de programlar, gazete ve dergi röportajları; Avrupa'nın Yıldızları Yılın En Başarılı İş Kadını ödülü ve teşekkür belgeleri.", f'''
{hero('Medya &amp; Kreatif','Ekranda, sahnede, <span class="gold">sahada</span>','TV programları, röportajlar ve girişimciliğe verilen emeğin karşılığı olan ödüller.','Medya &amp; Ödüller')}

<section><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">TV Programları</span>
    <h2>Konuk ve <span class="gold">sunucu</span></h2>
    <p>Business Channel Türk TV, TLC ve çeşitli programlarda konuk ve sunucu olarak yer aldı. Türkçe ve Almanca röportajlarla Almanya'daki Türk toplumunun sesini ekranlara taşıyor.</p>
    <ul class="checks"><li>TELE1 – "Almanya–Türkiye İşbirlikleri" canlı yayını (8 Ağustos 2026)</li><li>Business Channel Türk TV</li><li>TLC</li><li>Türkçe &amp; Almanca röportajlar</li></ul>
  </div>
  <div class="tv reveal">
    <figure data-zoom style="cursor:zoom-in"><img src="img/tv-1.jpg" alt="TLC röportajı"></figure>
    <figure data-zoom style="cursor:zoom-in;margin-top:40px"><img src="img/tv-2.jpg" alt="TV stüdyosu"></figure>
    <figure data-zoom style="cursor:zoom-in"><img src="img/tv-3.jpg" alt="Bahar Sonek"></figure>
  </div>
</div></section>

<section class="band"><div class="wrap grid g2">
  <div class="card reveal">{ic('news')}<h3>Gazete ve Dergi Röportajları</h3><p>Girişimcilik, kadın gücü ve uluslararası danışmanlık alanlarında röportajları yayınlandı. Bizden Bil İş ve Sanat Dergisi'nin Ağustos 2026 sayısında kapak oldu; Neriman Dergisi başta olmak üzere çeşitli yayınlarda yer aldı.</p></div>
  <div class="card reveal">{ic('trophy')}<h3>Avrupa'nın Yıldızları</h3><p>Neriman Dergisi tarafından "Yılın En Başarılı İş Kadını" ödülüne layık görüldü.</p></div>
  <div class="card reveal">{ic('star')}<h3>Yılın En İyi Tercümanı ve Danışmanı</h3><p>Cihat Dündar Organizasyonu'nun 5. Altın Meslek &amp; Kariyer Ödülleri'nde (30 Temmuz 2026, İstanbul) "Yılın Uluslararası Başarı Gösteren En İyi Tercümanı ve Danışmanı" ödülüne layık görüldü.</p></div>
  <div class="card reveal">{ic('globe')}<h3>Türkiye İş İnsanları Danışmanı</h3><p>Uluslararası tercümanlık, danışmanlık ve halkla ilişkiler alanlarında; Almanya ile Türkiye arasındaki ekonomik, ticari ve kültürel iş birliklerinde danışman olarak çalışıyor.</p></div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">2026</span><h2>Yayınlar &amp; <span class="gold">ödül törenleri</span></h2><p>Büyütmek için görsellere tıklayın.</p></div>
  {poster_grid([('tele1-canli-yayin.jpg','TELE1 canlı yayın','Almanya–Türkiye İşbirlikleri · Uzman Psikolog Alanur Özalp ile'),('bizden-bil-kapak.jpg','Bizden Bil kapağı','İş ve Sanat Dergisi · Ağustos 2026'),('altin-meslek-odul.jpg','5. Altın Meslek &amp; Kariyer Ödülleri','30 Temmuz 2026 · İstanbul, Suzy Event House'),('summit-odul.jpg','Life &amp; Beauty Summit','Ödül töreni')])}
  <div class="sec-head reveal" style="margin:80px auto 40px"><span class="eyebrow">Etkinliklerden</span><h2>Kırmızı halıdan <span class="gold">kareler</span></h2></div>
  {poster_grid([('summit-1.jpg','Life &amp; Beauty Summit','Kırmızı halı'),('summit-2.jpg','Life &amp; Beauty Summit','Davetli konuk'),('summit-3.jpg','Life &amp; Beauty Summit','DoubleTree by Hilton'),('musiad-koln.jpg','MÜSİAD NRW-Köln','"Türkiye\'ye Yatırımda Yeni Dönem"')])}
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Teşekkür ve Başarı Belgeleri</span><h2>Başarılar &amp; <span class="gold">Ödüller</span></h2><p>Girişimcilik, kadın gücü ve uluslararası danışmanlık alanlarındaki katkılarımızdan dolayı aldığımız ödüller bizler için büyük bir onur kaynağıdır. Belgeleri büyütmek için tıklayın.</p></div>
  {awards_grid()}
  <p class="muted reveal" style="text-align:center;margin-top:30px;font-style:italic">…ve daha birçok takdir ve teşekkür belgesi.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Desteklediğimiz Projeler</span><h2>Kitap &amp; <span class="gold">Podcast</span></h2></div>
  <div class="split">
    <div class="photo gold-frame reveal" style="max-width:340px;margin:0 auto"><img src="img/book.jpg" alt="Üzülme Yalnız Değilsin – Melissa İrem Türkeri"></div>
    <div class="reveal">
      <span class="eyebrow">Melissa İrem Türkeri</span>
      <h2>“Üzülme Yalnız Değilsin”</h2>
      <p>Melissa İrem Türkeri, yazarlık yolculuğuna 2024 yılında yayımladığı “Üzülme Yalnız Değilsin” adlı kitabıyla başladı. Kısa sürede okuyucuların ilgisini gören eser, güçlü mesajları ve içten anlatımıyla dikkat çekti. Aynı yıl “Yılın En Başarılı Psikoloji ve Hücreye Yazarı” ödülünü aldı.</p>
      <div class="card" style="margin-top:20px">{ic('mic')}<h3>Podcast: <span class="script gold" style="font-size:1.3em">Melissa ile Bunu da Konuşalım</span></h3><p>Her hafta farklı konularıyla hayata, ilişkilere, başarıya ve kişisel gelişime dair samimi ve ilham verici sohbetler.</p></div>
    </div>
  </div>
  <div class="quote reveal" style="margin-top:50px"><div class="qm">“</div><blockquote>Sözler, insanın yüreğine dokunursa değişim orada başlar.</blockquote></div>
</div></section>

<section><div class="wrap" style="text-align:center">
  <div class="sec-head reveal"><span class="eyebrow">Video</span><h2>Röportajlar &amp; <span class="gold">videolar</span></h2><p>Röportajlar, programlar ve daha fazlası. Oynatmak için tıklayın.</p></div>
  {video_grid()}
  <a class="btn btn-gold reveal" style="margin-top:28px" href="https://www.youtube.com/@baharsonek2023" target="_blank" rel="noopener">{YT_SVG.replace('<svg','<svg fill="currentColor"')} Tüm videolar: YouTube kanalı</a>
</div></section>
{cta('Röportaj veya iş birliği için', 'Program, röportaj, etkinlik sunumu veya iş birliği teklifleriniz için bizimle iletişime geçin.')}
''')

# ───────────── FOTOĞRAFÇILIK ─────────────
page('fotografcilik.html','Fotoğrafçılık & Organizasyon – Bahar Sonek Creative',
 'Düğün, sünnet, kına ve özel günleriniz için organizasyon ve profesyonel fotoğrafçılık. Reklam, management ve röportaj hizmetleri. Gelsenkirchen.', f'''
{hero('Creative Dienstleistungen','Özel günleriniz, <span class="gold">ölümsüz kareler</span>','Zarif, doğal ve unutulmaz fotoğraflarla o günün en güzel anlarını sizin için yakalıyoruz.','Fotoğrafçılık')}

<section><div class="wrap split">
  <div class="photo reveal"><img src="img/photographer.jpg" alt="Profesyonel fotoğraf çekimi" style="aspect-ratio:4/5"></div>
  <div class="reveal">
    <span class="eyebrow">Bahar Sonek Creative</span>
    <h2>Anılarınız <span class="gold">emin ellerde</span></h2>
    <p>Özel günlerinizin en güzel anlarını profesyonel karelerle ölümsüzleştiriyoruz. Planlamadan çekime, organizasyondan albüme kadar tüm süreci sizin için yönetiyoruz.</p>
    <p>Türk kültürüne ve geleneklerine hâkim bir ekip olarak; kına gecesinin duygusunu, sünnet şöleninin neşesini ve düğününüzün zarafetini doğal bir dille yakalıyoruz.</p>
    <a class="btn btn-gold" href="iletisim.html?konu=Organizasyon">Tarih Sorun {svg('arrow')}</a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Çekim &amp; Organizasyon</span><h2>Neler <span class="gold">yapıyoruz?</span></h2></div>
  <div class="grid g3">
    <div class="card hover reveal">{ic('ring')}<h3>Düğün</h3><p>Hazırlıktan son dansa kadar günün tamamı; doğal ve zarif kareler.</p></div>
    <div class="card hover reveal">{ic('heart')}<h3>Kına Gecesi</h3><p>Geleneğin duygusunu ve renklerini yansıtan çekimler.</p></div>
    <div class="card hover reveal">{ic('star')}<h3>Sünnet Düğünü</h3><p>Ailenizin en mutlu gününü eğlenceli ve renkli karelerle saklayın.</p></div>
    <div class="card hover reveal">{ic('camera')}<h3>Özel Günler &amp; Portre</h3><p>Nişan, doğum günü, aile ve profesyonel portre çekimleri.</p></div>
    <div class="card hover reveal">{ic('mega')}<h3>Reklam &amp; Management</h3><p>İşletmeler için tanıtım çekimleri, sosyal medya içerikleri ve yönetim.</p></div>
    <div class="card hover reveal">{ic('mic')}<h3>Röportaj &amp; Sunum</h3><p>Türkçe ve Almanca röportaj, etkinlik ve gala sunumları.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Süreç</span><h2>Hayalden <span class="gold">kareye</span></h2></div>
  <div class="grid g4 steps">
    <div class="card step reveal"><h3>Tanışma</h3><p>Tarihinizi, mekânınızı ve hayalinizdeki konsepti konuşuruz.</p></div>
    <div class="card step reveal"><h3>Planlama</h3><p>Akış, çekim listesi ve organizasyon detaylarını netleştiririz.</p></div>
    <div class="card step reveal"><h3>Çekim Günü</h3><p>Siz anın tadını çıkarın; biz en güzel anları yakalayalım.</p></div>
    <div class="card step reveal"><h3>Teslim</h3><p>Özenle düzenlenmiş fotoğraflarınızı dijital olarak teslim ederiz.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap split rev">
  <div class="photo reveal"><img src="img/flyer-top.jpg" alt="Bahar Sonek kartvizit" style="aspect-ratio:16/9"></div>
  <div class="reveal">
    <span class="eyebrow">Emlak / Immobilien</span>
    <h2>Yeni evinizi <span class="gold">birlikte bulalım</span></h2>
    <p>Kiralık ve satılık gayrimenkullerde arama, değerlendirme ve aracılık. Almanca evrak ve sözleşme süreçlerinde de yanınızdayız.</p>
    <a class="btn btn-ghost" href="iletisim.html?konu=Emlak">Emlak İçin Yazın {svg('arrow')}</a>
  </div>
</div></section>
{cta('Tarihiniz hâlâ boş mu?', 'Özel gününüz için takvimimizi şimdiden ayırtın. Müsaitlik ve detaylar için hemen yazın.')}
''')

# ───────────── D.G.K. ─────────────
page('dgk.html','Dünya Gençlik Konseyi Almanya Bölge Başkanlığı – Bahar Sonek',
 "Bahar Sonek, Dünya Gençlik Konseyi (D.G.K.) Almanya Bölge Başkanı. Gençlere ve ailelere destek programları, dayanışma ve uluslararası iş birliği.", f'''
{dgk_role_hero()}

<section><div class="wrap split">
  <div class="reveal" style="display:grid;place-items:center">
    <div style="width:min(340px,80vw);aspect-ratio:1;border-radius:50%;padding:10px;box-shadow:0 0 0 1px var(--gold),0 0 0 12px rgba(212,169,74,.08),0 0 90px rgba(212,169,74,.18)">
      <img src="img/dgk-logo.png" alt="Dünya Gençlik Konseyi logosu" style="width:100%;height:100%;object-fit:contain">
    </div>
  </div>
  <div class="reveal">
    <span class="eyebrow">Hakkında</span>
    <h2>Gençliğin gücü, <span class="gold">dünyanın geleceği</span></h2>
    <p>İstanbul merkezli Dünya Gençlik Konseyi; gençlerin sosyal, kültürel, akademik ve ekonomik alanlarda gelişimini desteklemeyi ve bilinçli bir gençlik yetişmesine katkı sağlamayı amaçlar. Eğitimden spora, kültür-sanattan teknolojiye, girişimcilikten sosyal sorumluluk projelerine kadar geniş bir alanda faaliyet gösterir.</p>
    <p>Konseyin Genel Başkanı Hüseyin Celep tarafından yapılan görevlendirmeyle Bahar Sonek, Almanya Federal Cumhuriyeti sınırları içerisinde konsey adına faaliyet göstermek üzere <b style="color:var(--gold2)">Almanya Bölge Başkanı</b> olarak atanmıştır.</p>
    <div class="btns"><a class="btn btn-gold" href="iletisim.html?konu=D.G.K.">Gönüllü Ol</a><a class="btn btn-ghost" href="https://www.dunyagenclikkonseyi.org" target="_blank" rel="noopener">dunyagenclikkonseyi.org {svg('arrow')}</a></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Almanya Bölge Başkanlığı</span><h2>Beş temel <span class="gold">hedef</span></h2></div>
  <div class="grid g3">
    <div class="card reveal">{ic('users')}<h3>Gençlik Dayanışması</h3><p>Almanya'daki gençleri bir araya getiren, güçlü bir dayanışma ağı.</p></div>
    <div class="card reveal">{ic('cap')}<h3>Eğitim Desteği</h3><p>Okul, meslek ve kariyer yolculuğunda gençlere rehberlik ve destek.</p></div>
    <div class="card reveal">{ic('shield')}<h3>Fırsat Eşitliği</h3><p>Her gencin ve ailenin imkânlara eşit erişebildiği bir toplum.</p></div>
    <div class="card reveal">{ic('chart')}<h3>Girişimcilik &amp; İnovasyon</h3><p>Fikirlerini işe dönüştürmek isteyen gençlere yol arkadaşlığı.</p></div>
    <div class="card reveal">{ic('globe')}<h3>Uluslararası İş Birliği</h3><p>Türkiye ile Almanya arasında köprü olan projeler ve ortaklıklar.</p></div>
    <div class="card reveal" style="background:var(--grad);color:#1a1307;border:none;display:grid;place-items:center;text-align:center"><div><span class="script" style="font-size:2.4rem;line-height:1.1;display:block">Birlikte Üretiyor,<br>Birlikte Büyüyoruz</span></div></div>
  </div>
</div></section>

<section><div class="wrap split">
  <figure class="photo gold-frame reveal" data-zoom style="cursor:zoom-in;max-width:440px;margin:0 auto"><img src="img/fb/dgk-destek-programlari.jpg" alt="Gençlere ve Ailelere Destek Programları afişi"></figure>
  <div class="reveal">
    <span class="eyebrow">Güçlü Gençlik · Güçlü Aile · Güçlü Gelecek</span>
    <h2>Gençlere ve ailelere <span class="gold">destek programları</span></h2>
    <p>Farklı alanlarda planlanan destek programları, Türkiye ve Almanya'da eş zamanlı olarak uygulanacak. Türkiye ve Almanya'da aynı vizyon, ortak gelecek.</p>
    <ul class="checks">
      <li>Eğitim destek programları</li><li>İstihdam ve meslek gelişimi</li><li>Aile ve toplum destekleri</li>
      <li>Gençlik projeleri</li><li>Sosyal dayanışma ve kültür</li><li>Yeni fırsatlar ve uluslararası iş birlikleri</li>
    </ul>
    <a class="btn btn-gold" href="iletisim.html?konu=D.G.K.">Programlar Hakkında Bilgi Al</a>
  </div>
</div></section>

<section class="band"><div class="wrap split rev">
  <figure class="photo reveal" data-zoom style="cursor:zoom-in"><img src="img/fb/dgk-destek-cagrisi.jpg" alt="Destek çağrısı afişi"></figure>
  <div class="reveal">
    <span class="eyebrow">Destek Çağrısı</span>
    <h2>Ekonomik zorluklara karşı <span class="gold">sosyal hayata destek</span></h2>
    <div class="quote" style="text-align:left;padding:0;margin:0"><div class="qm">“</div><blockquote style="font-size:1.3rem">İnsanlar sosyal hayatlarında yaşam alanlarını ve seyahatlerini keşfederek zenginleşir. Ancak ekonomik sıkıntılar nedeniyle birçok aile bu imkânlardan mahrum kalıyor. Sosyal dayanışmayı güçlendirerek, herkes için daha adil ve erişilebilir bir yaşamı birlikte inşa etmeliyiz.</blockquote><cite>Bahar Sonek</cite></div>
    <p style="margin-top:18px">Dezavantajlı gençler ve ailelerin sosyal hayata katılımını destekleyen projelerle geleceğe umut oluyoruz: <b style="color:var(--gold2)">Hayata dokun, gençliği yeniden kazan.</b></p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="quote reveal"><span class="eyebrow">Bölge Başkanının mesajı</span><div class="qm" style="margin-top:14px">“</div><blockquote>Mutlu bireyler, güçlü aileler; güçlü aileler ise güçlü bir toplum demektir. Her vatandaşın sosyal yaşama katılabildiği, seyahat edebildiği ve geleceğe umutla bakabildiği bir gelecek için hep birlikte çalışmalıyız.</blockquote><cite>Bahar Sonek · D.G.K. Almanya Bölge Başkanı</cite></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Görevlendirme &amp; Ekip</span><h2>Birlikte <span class="gold">güçlüyüz</span></h2><p>Büyütmek için görsellere tıklayın.</p></div>
  {poster_grid([('dgk-mazbata.jpg','Mazbata','D.G.K. Almanya Bölge Temsilci Başkanlığı görevlendirmesi'),('dgk-almanya-afis.jpg','Almanya Bölge Başkanlığı','“Gençliğin Gücü, Dünyanın Geleceği”'),('dgk-genel-merkez.jpg','Genel Merkez ekibi','D.G.K. Genel Merkez toplantısı'),('dgk-toplanti.jpg','D.G.K. Almanya','Gençlerle bir arada')])}
</div></section>
{cta('Gençlerle birlikte, gençler için.', 'D.G.K. Almanya çalışmalarına gönüllü olarak katılmak, destek olmak veya iş birliği yapmak için bize yazın.')}
''')

# ───────────── HABERLER ─────────────
page('haberler.html','Haberler – Bahar Sonek | Güncel',
 'Bahar Sonek ve D.G.K. Almanya\'dan güncel haberler, etkinlikler, ödüller ve projeler.', f'''
{hero('Güncel','Haberler &amp; <span class="gold">etkinlikler</span>','Facebook sayfamızdaki paylaşımlardan derlenen güncel haberler, etkinlikler, ödüller ve projeler.','Haberler')}
<section><div class="wrap">
  <div class="filters" data-news-filters></div>
  <div class="news-grid" data-news-all></div>
</div></section>
<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Sosyal Medya</span><h2>Bizi <span class="gold">takip edin</span></h2><p>En yeni paylaşımlar, videolar ve duyurular için sosyal medya hesaplarımız.</p></div>
  <div class="social-cards two">
    <a class="social-card reveal" href="https://www.facebook.com/baharsonek.official" target="_blank" rel="noopener">{FB_SVG}<span><b>Facebook</b><small>Bahar Sonek (Official)</small></span></a>
    <a class="social-card reveal" href="https://www.youtube.com/@baharsonek2023" target="_blank" rel="noopener">{YT_SVG}<span><b>YouTube</b><small>@baharsonek2023</small></span></a>
  </div>
  <div class="feed-consent" data-social-feed>
    <h3 style="margin-bottom:8px">Canlı sosyal medya akışı</h3>
    <p class="muted" style="max-width:520px;margin:0 auto 18px">Akışı yüklediğinizde sosyal medya sağlayıcısına veri aktarılır. Ayrıntılar <a href="datenschutz.html" style="color:var(--gold2)">Datenschutz</a> sayfasında.</p>
    <button class="btn btn-gold">Akışı Göster</button>
  </div>
</div></section>
{cta('Haberdar olun', 'Etkinlikler, seminerler ve duyurular için bize WhatsApp\'tan yazın, sizi bilgilendirelim.')}
''')

# ───────────── İLETİŞİM ─────────────
def cline(icn, label, val):
    return f'<div class="cline">{ic(icn)}<div><small>{label}</small>{val}</div></div>'
page('iletisim.html','İletişim – Bahar Sonek | Kirchstr. 33 Gelsenkirchen',
 'Bahar Sonek ile iletişim: 01520-2614684, baharsonek.official@gmail.com, Kirchstr. 33, 45879 Gelsenkirchen. Bilgi ve randevu için yazın.', f'''
{hero('İletişim','Bilgi ve <span class="gold">randevu</span> için','Size en hızlı WhatsApp üzerinden dönüyoruz. Ofisimize randevu ile bekliyoruz.','İletişim')}

{map_section()}

<section><div class="wrap grid g2" style="gap:28px;align-items:start">
  <div class="card reveal" style="padding:34px">
    <h3 style="font-size:1.6rem;margin-bottom:10px">İletişim bilgileri</h3>
    <div class="cinfo">
      {cline('phone','Telefon / WhatsApp',f'<a href="{TEL}">01520 – 2614684</a>')}
      {cline('mail','E-posta','<a href="mailto:baharsonek.official@gmail.com">baharsonek.official@gmail.com</a>')}
      {cline('mail','Creative E-posta','<a href="mailto:baharsonekcreative@gmail.com">baharsonekcreative@gmail.com</a>')}
      {cline('pin','Adres','Kirchstr. 33, 45879 Gelsenkirchen, Almanya')}
      {cline('clock','Çalışma saatleri','Randevu ile')}
    </div>
    {SOCIAL}
  </div>
  <div class="card reveal" style="padding:34px">
    <h3 style="font-size:1.6rem;margin-bottom:6px">Mesaj gönderin</h3>
    <p style="margin-bottom:20px">Formu doldurun; mesajınız e-posta ile doğrudan Bahar Sonek'e ulaşır. Dilerseniz aynı mesajı WhatsApp'tan da gönderebilirsiniz.</p>
    <div class="form-msg ok" data-form-ok hidden>Teşekkürler! Mesajınız bize ulaştı, en kısa sürede dönüş yapacağız.</div>
    <div class="form-msg err" data-form-err hidden>Mesaj gönderilemedi. Lütfen tekrar deneyin ya da WhatsApp / telefonla ulaşın.</div>
    <form class="contact" id="form" method="post" action="kontakt.php">
      <input type="hidden" name="lang" value="tr">
      <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="row">
        <label class="f">Ad Soyad<input name="ad" required autocomplete="name"></label>
        <label class="f">Telefon<input name="tel" type="tel" required autocomplete="tel"></label>
      </div>
      <label class="f">E-posta<input name="email" type="email" required autocomplete="email"></label>
      <label class="f">Konu<select name="konu">
        <option>Devlet daireleri işlemleri</option><option>Jobcenter</option><option>Yabancılar Dairesi</option>
        <option>Resmi mektup / yazışma</option><option>Çeviri</option><option>Yurt dışı vatandaşlık</option>
        <option>Yatırım / Gayrimenkul</option><option value="Emlak">Emlak / Immobilien</option>
        <option value="Organizasyon">Organizasyon &amp; Fotoğrafçılık</option><option value="D.G.K.">D.G.K. Almanya</option><option>Diğer</option>
      </select></label>
      <label class="f">Mesajınız<textarea name="mesaj" required placeholder="Kısaca nasıl yardımcı olabiliriz?"></textarea></label>
      <label class="consent"><input type="checkbox" required> <span><a href="datenschutz.html">Gizlilik politikasını (Datenschutz)</a> okudum, bilgilerimin talebimi yanıtlamak için kullanılmasını kabul ediyorum.</span></label>
      <div class="form-btns">
        <button type="submit" class="btn btn-gold">{svg('mail')} E-posta ile Gönder</button>
        <button type="button" class="btn btn-wa" data-wa-send>{WA_SVG.replace('<svg','<svg fill="currentColor"')} WhatsApp ile Gönder</button>
      </div>
    </form>
  </div>
</div></section>

''')

# ───────────── YASAL SAYFALAR ─────────────
T = lambda s: f'<span class="todo">{s}</span>'
IMP_BODY = f'''
{hero('Rechtliches','Impressum','Angaben gemäß § 5 DDG','Impressum')}
<section><div class="wrap legal">
  <h2>Anbieter</h2>
  <p>Bahar Sonek<br>Creative Dienstleistungen<br>Kirchstr. 33<br>45879 Gelsenkirchen<br>Deutschland</p>
  <h2>Kontakt</h2>
  <p>Telefon: 01520 – 2614684<br>E-Mail: baharsonek.official@gmail.com</p>
  <h2>Umsatzsteuer</h2>
  <p>Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: {T('USt-IdNr. ergänzen oder Hinweis auf Kleinunternehmerregelung')}</p>
  <h2>Berufsbezeichnung / Aufsicht</h2>
  <p>{T('Falls Versicherungs- oder Immobilienvermittlung: Erlaubnis nach § 34c / § 34d GewO, zuständige IHK und Registernummer ergänzen')}</p>
  <h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
  <p>Bahar Sonek, Anschrift wie oben</p>
  <h2>Verbraucherstreitbeilegung</h2>
  <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
</div></section>
'''
DS_BODY = f'''
{hero('Rechtliches','Datenschutzerklärung','Informationen zur Verarbeitung personenbezogener Daten','Datenschutz')}
<section><div class="wrap legal">
  <p>{T('Entwurf – vor Veröffentlichung von einer Fachperson bzw. mit einem Datenschutz-Generator prüfen und vervollständigen lassen.')}</p>
  <h2>1. Verantwortliche Stelle</h2>
  <p>Bahar Sonek, Creative Dienstleistungen, Kirchstr. 33, 45879 Gelsenkirchen · Tel. 01520 – 2614684 · baharsonek.official@gmail.com</p>
  <h2>2. Hosting</h2>
  <p>{T('Hosting-Anbieter, Serverstandort und Auftragsverarbeitungsvertrag ergänzen')}</p>
  <h2>3. Kontaktaufnahme per WhatsApp, Telefon und E-Mail</h2>
  <p>Wenn Sie das Kontaktformular mit „E-Mail senden“ bzw. „E-posta ile Gönder“ absenden, werden Ihre Angaben (Name, Telefon, E-Mail, Betreff, Nachricht) über unseren Webserver per E-Mail an uns übermittelt und ausschließlich zur Bearbeitung Ihrer Anfrage verwendet (Art. 6 Abs. 1 lit. b DSGVO). Die E-Mail wird über Google Gmail (Google Ireland Ltd.) empfangen. Wählen Sie stattdessen „Per WhatsApp senden“, wird WhatsApp (WhatsApp Ireland Ltd.) mit Ihrer Nachricht geöffnet; es gelten dessen Datenschutzbestimmungen. Anfragen löschen wir, sobald sie erledigt sind und keine Aufbewahrungspflichten bestehen.</p>
  <h2>4. YouTube-Videos</h2>
  <p>Videos werden im erweiterten Datenschutzmodus (youtube-nocookie.com) eingebunden und erst geladen, wenn Sie auf ein Video klicken. Erst dann wird eine Verbindung zu Google Ireland Ltd. hergestellt und z. B. Ihre IP-Adresse übertragen (Art. 6 Abs. 1 lit. a DSGVO).</p>
  <h2>4a. Google Maps</h2>
  <p>Auf der Kontaktseite binden wir Karten von Google Maps (Google Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Irland) ein. Die Karte wird nur geladen, wenn Sie in den Datenschutz-Einstellungen der Kategorie „Externe Medien“ zustimmen oder auf „Karte laden“ klicken. Erst dann werden u. a. Ihre IP-Adresse und Geräteinformationen an Google übertragen, ggf. auch in die USA. Rechtsgrundlage ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO, § 25 Abs. 1 TDDDG), die Sie jederzeit über „Cookie-Einstellungen“ im Fußbereich widerrufen können.</p>
  <h2>4b. Einwilligungsverwaltung</h2>
  <p>Ihre Auswahl im Datenschutz-Banner speichern wir im lokalen Speicher Ihres Browsers (localStorage, Eintrag „bs_consent_v1“: gewählte Kategorien und Zeitpunkt). Diese Information wird nicht an uns oder Dritte übermittelt. Rechtsgrundlage: § 25 Abs. 2 Nr. 2 TDDDG, Art. 6 Abs. 1 lit. c DSGVO.</p>
  <h2>5. Google Fonts</h2>
  <p>{T('Empfehlung: Schriftarten vor Veröffentlichung lokal einbinden, damit keine Verbindung zu Google-Servern entsteht.')}</p>
  <h2>6. Social-Media-Links</h2>
  <p>Links zu Facebook und YouTube sind einfache Verweise; Daten werden erst übertragen, wenn Sie diese anklicken. Ein eingebetteter Social-Media-Feed auf der Seite „Aktuelles“ bzw. „Haberler“ wird erst nach Ihrer Einwilligung per Klick geladen (Art. 6 Abs. 1 lit. a DSGVO). {T('Anbieter des Feeds ergänzen, sobald gewählt')}</p>
  <h2>7. Ihre Rechte</h2>
  <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie ein Beschwerderecht bei der Landesbeauftragten für Datenschutz und Informationsfreiheit NRW.</p>
</div></section>
'''
def legal():
    fix = (lambda b: b.replace('>Ana Sayfa<','>Startseite<')) if LANG=='de' else (lambda b: b)
    page('impressum.html','Impressum – Bahar Sonek','Impressum / Anbieterkennzeichnung gemäß § 5 DDG.', fix(IMP_BODY))
    page('datenschutz.html','Datenschutz – Bahar Sonek','Datenschutzerklärung.', fix(DS_BODY))
legal()

# ───────────── DEUTSCH ─────────────
LANG = 'de'
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'build_de.py'), encoding='utf-8').read())
legal()
print('ok')
