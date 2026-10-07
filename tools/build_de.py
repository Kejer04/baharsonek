# Deutsche Fassung – wird von build.py mit LANG='de' ausgeführt (exec).
# Bildpfade wie im TR-Teil ("img/…"); page() setzt für /de/ automatisch "../" davor.

QUOTE_VISION = '''<div class="quote reveal"><div class="qm">“</div><blockquote>Unsere Vision: in einer globalen Welt starke Schritte gehen – und gemeinsam mit Ihnen in eine bessere Zukunft.</blockquote><cite>Bahar Sonek</cite></div>'''

AWARDS_DE = [
 ('award-2.jpg','Erfolgreichste Geschäftsfrau des Jahres','„Avrupa\'nın Yıldızları“ – Neriman Dergisi'),
 ('award-1.jpg','Dankesurkunde 2025','Business Channel Türk TV · JMG-Group Gelsenkirchen'),
 ('award-4.jpg','Dank für Ausbildungsbeitrag','Praktikant:innen bei Business Channel Türk TV, 2025'),
 ('award-3.jpg','4. Preis- &amp; Galaabend','Derewa präsentiert – Neriman Dergisi'),
]

# ───────────── STARTSEITE ─────────────
page('index.html','Bahar Sonek – Richtige Unterstützung, starke Zukunft | Gelsenkirchen',
 'Hilfe bei Behördenbriefen, Jobcenter- und Ausländerbehörde-Angelegenheiten, Übersetzungen Türkisch–Deutsch und internationaler Beratung in Gelsenkirchen. Bahar Sonek Creative Dienstleistungen.', f'''
<section class="hero"><div class="wrap hero-grid">
  <div class="reveal">
    <span class="eyebrow">D.G.K.-Regionalpräsidentin Deutschland · International Business Manager</span>
    <h1>Richtige Unterstützung,<br><span class="gold">starke Zukunft.</span></h1>
    <p class="lead">Von Behördenbriefen bis zu internationalen Investitions- und Staatsbürgerschaftsfragen: Wir begleiten Sie Schritt für Schritt – zweisprachig auf Deutsch und Türkisch.</p>
    <div class="btns">
      <a class="btn btn-gold" href="{WA}" target="_blank" rel="noopener">{svg('chat')} Kostenloses Erstgespräch</a>
      <a class="btn btn-ghost" href="leistungen.html">Unsere Leistungen {svg('arrow')}</a>
    </div>
    <div class="hero-stats">
      <div><b>12+ Jahre</b>Berufserfahrung</div>
      <div><b>DE ⇄ TR</b>zweisprachiger Service</div>
      <div><b>D.G.K.</b>Regionalpräsidentin Deutschland</div>
    </div>
  </div>
  <div class="portrait fx-portrait reveal">
    {FX_PORTRAIT}
    <div class="float-card fc-1"><span class="ic"><svg viewBox="0 0 24 24">{I['trophy']}</svg></span><span><b>Geschäftsfrau des Jahres</b>„Avrupa'nın Yıldızları“</span></div>
    <a href="dgk.html" class="float-card fc-2"><img src="img/dgk-logo.png" alt="" style="width:40px;height:40px"><span><b>Weltjugendrat (D.G.K.)</b>Regionalpräsidentin Deutschland</span></a>
  </div>
</div></section>

{dgk_feature()}

<section class="band" style="padding:80px 0"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Unsere Leistungen</span><h2>Bürokratie? <span class="gold">Überlassen Sie uns.</span></h2><p>Briefe, Formulare, Anträge, Termine – wir machen alles verständlich und behalten den Überblick für Sie.</p></div>
  <div class="grid g4">
    <a href="leistungen.html#behoerden" class="card reveal">{ic('doc')}<h3>Behörden</h3><p>Unterstützung bei Dokumenten, Formularen, Anträgen und Schriftverkehr mit Ämtern.</p><span class="more">Details {svg('arrow','width="16"')}</span></a>
    <a href="leistungen.html#behoerden" class="card reveal">{ic('bag')}<h3>Jobcenter</h3><p>Schreiben, Anträge, Termine – richtige Unterstützung in allen Schritten.</p><span class="more">Details {svg('arrow','width="16"')}</span></a>
    <a href="leistungen.html#behoerden" class="card reveal">{ic('mail')}<h3>Ausländerbehörde</h3><p>Aufenthalt, Visum, Anträge und Termine – professionell begleitet.</p><span class="more">Details {svg('arrow','width="16"')}</span></a>
    <a href="leistungen.html#behoerden" class="card reveal">{ic('chat')}<h3>Übersetzungen TR – DE</h3><p>Zuverlässige Übersetzungen für Dokumente, Schreiben und Gespräche.</p><span class="more">Details {svg('arrow','width="16"')}</span></a>
  </div>
</div></section>

<section><div class="wrap split">
  <div class="photo gold-frame reveal"><img src="img/tv-3.jpg" alt="Bahar Sonek Porträt" style="aspect-ratio:4/5"></div>
  <div class="reveal">
    <span class="eyebrow">Wer ist Bahar Sonek?</span>
    <h2>Von Adana nach Gelsenkirchen – <span class="gold">ein inspirierender Weg</span></h2>
    <p>1982 in Gelsenkirchen geboren, Familie aus Adana. Nach dem Abitur am Gymnasium begann sie vor rund 12 Jahren ihren beruflichen Weg in der Versicherungsbranche.</p>
    <p>Mit wachsender Erfahrung gründete sie ihr eigenes Büro, spezialisierte sich auf Staatsbürgerschaften im Ausland und wurde mehrfach ausgezeichnet. Heute ist sie eine vielseitig aktive, visionäre Unternehmerin.</p>
    <div class="btns" style="margin-top:1.6rem"><a class="btn btn-ghost" href="ueber-uns.html">Die ganze Geschichte {svg('arrow')}</a></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Internationale Beratung</span><h2>Leistungen <span class="script gold" style="font-size:1.25em">und Vision</span></h2><p>Mit verlässlichen Lösungen in internationaler Beratung, Investition und Staatsbürgerschaft machen wir Ihre Pläne wahr.</p></div>
  <div class="grid g4">
    <a href="leistungen.html#international" class="card reveal">{ic('globe')}<h3>Staatsbürgerschaft im Ausland</h3><p>Verlässliche Informationen, richtige Orientierung, professionelle Beratung.</p></a>
    <a href="leistungen.html#international" class="card reveal">{ic('house')}<h3>Immobilieninvestition</h3><p>Rentable Investitionsmöglichkeiten für eine sichere Zukunft.</p></a>
    <a href="leistungen.html#international" class="card reveal">{ic('chart')}<h3>Investitionsberatung</h3><p>Mit der richtigen Strategie und internationalem Netzwerk zu Ihren Zielen.</p></a>
    <a href="leistungen.html#international" class="card reveal">{ic('cap')}<h3>Bildung &amp; Karriere</h3><p>Bildungs- und Karrierechancen im Ausland – Ihre Zukunft gestalten.</p></a>
  </div>
  <div style="margin-top:64px">{QUOTE_VISION}</div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Urkunden &amp; Auszeichnungen</span><h2>Wenn Einsatz <span class="gold">gewürdigt wird</span></h2><p>Auszeichnungen für unser Engagement in Unternehmertum, Frauenförderung und internationaler Beratung sind für uns eine große Ehre.</p></div>
  {awards_grid(AWARDS_DE)}
  <div class="sec-head reveal" style="margin:80px auto 40px"><span class="eyebrow">2026</span><h2>Im TV, auf dem Titel, <span class="gold">auf der Bühne</span></h2></div>
  {poster_grid([('altin-meslek-odul.jpg','Beste Übersetzerin &amp; Beraterin des Jahres','5. Altın Meslek &amp; Kariyer Ödülleri · Istanbul'),('bizden-bil-kapak.jpg','Titel „Bizden Bil“','Wirtschafts- und Kunstmagazin · August 2026'),('tele1-canli-yayin.jpg','Live bei TELE1','Deutsch-türkische Kooperationen · 8. August 2026'),('summit-odul.jpg','Life &amp; Beauty Summit','Preisverleihung')])}
  <div class="btns reveal" style="justify-content:center;margin-top:40px"><a class="btn btn-ghost" href="medien-auszeichnungen.html">Medien &amp; Preise {svg('arrow')}</a></div>
</div></section>

<section class="band"><div class="wrap split rev">
  <div class="photo reveal"><img src="img/photographer.jpg" alt="Fotoshooting" style="aspect-ratio:4/5"></div>
  <div class="reveal">
    <span class="eyebrow">Kreative Dienstleistungen</span>
    <h2>Die schönsten Momente <span class="gold">Ihrer besonderen Tage</span></h2>
    <p>Mit eleganten, natürlichen und unvergesslichen Fotos halten wir die schönsten Augenblicke fest – für Hochzeiten, Beschneidungsfeiern, Henna-Abende und alle besonderen Anlässe.</p>
    <ul class="checks"><li>Organisation &amp; Fotografie</li><li>Werbung &amp; Management</li><li>Interviews auf Deutsch &amp; Türkisch</li><li>Bau · Elektro · Türen/Fenster/Terrassen <small class="muted">(mit unseren Partnern)</small></li><li>Immobilien</li></ul>
    <a class="btn btn-gold" href="fotografie.html">Kreative Leistungen {svg('arrow')}</a>
  </div>
</div></section>

<section><div class="wrap">
  <div class="promo reveal">
    <div class="pct">30 %</div>
    <div><h3>Rabattaktion</h3><p>30 % Rabatt auf ausgewählte Beratungsleistungen. Fragen Sie uns nach den Aktionsbedingungen.</p></div>
    <a class="btn" href="{WA}" target="_blank" rel="noopener">Jetzt anfragen</a>
  </div>
</div></section>


<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Aktuelles</span><h2>Neueste <span class="gold">Beiträge</span></h2><p>Ausgewählte Beiträge, Veranstaltungen und Auszeichnungen von unserer Facebook-Seite.</p></div>
  <div class="news-grid" data-news="3"></div>
  <div class="btns reveal" style="justify-content:center;margin-top:40px"><a class="btn btn-ghost" href="aktuelles.html">Alle Beiträge {svg('arrow')}</a></div>
</div></section>
{cta('Gemeinsam sind wir stark.')}
''')

# ───────────── LEISTUNGEN ─────────────
page('leistungen.html','Leistungen – Bahar Sonek | Beratung, Behördliches, Übersetzungen',
 'Unterstützung bei Behörden, Jobcenter und Ausländerbehörde, Schriftverkehr, Übersetzungen Türkisch–Deutsch, Staatsbürgerschaft im Ausland, Immobilien- und Investitionsberatung.', f'''
{hero('Unsere Leistungen','Richtige Unterstützung <span class="gold">bei allen Anliegen</span>','Verlässlich, schnell, richtig – von Behördenangelegenheiten in Deutschland bis zu Ihren internationalen Projekten.','Leistungen')}

<section id="behoerden"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">01 · Beratung &amp; Behördliches</span><h2>Behördliches <span class="gold">in Deutschland</span></h2><p>Briefe, Formulare und Termine müssen Sie nicht mehr belasten. Wir erklären verständlich – auf Deutsch oder Türkisch.</p></div>
  <div class="grid g3">
    {svc('doc','Behördliche Dokumente &amp; Briefe','Wir unterstützen Sie bei Dokumenten, Formularen, Anträgen und dem Schriftverkehr mit Behörden.',['Familienkasse, Elterngeld, Kindergeld','Finanzamt- und Versicherungsschreiben','Angelegenheiten beim Bürgeramt'])}
    {svc('bag','Jobcenter-Angelegenheiten','Schreiben, Anträge, Termine – wir begleiten Sie durch alle Schritte.',['Bürgergeld-Erstantrag','Weiterbewilligungsantrag','Schreiben verstehen und beantworten'])}
    {svc('mail','Ausländerbehörde','Professionelle Unterstützung bei Aufenthalt, Visum, Anträgen und Terminen.',['Aufenthaltstitel beantragen und verlängern','Visum und Familiennachzug','Terminvorbereitung und Unterlagen'])}
    {svc('letter','Schriftverkehr mit Behörden','Wir helfen beim Verfassen und richtigen Formulieren behördlicher Schreiben.',['Anschreiben und Mitteilungen an Ämter','Fristen im Blick behalten','Unterlagen vollständig zusammenstellen'])}
    {svc('chat','Übersetzungen Türkisch – Deutsch','Übersetzungen für behördliche Dokumente, Schreiben und Unterlagen.',['Übersetzung von Dokumenten und Briefen','Sprachliche Begleitung bei Terminen','Zusammenfassung auf Türkisch'])}
    <div class="card reveal" style="background:var(--grad);color:#1a1307;border:none;display:flex;flex-direction:column;justify-content:center">
      <h3 style="font-size:1.6rem">Egal, welcher Brief</h3>
      <p style="color:#3a2a0e;margin-bottom:18px">Schicken Sie uns ein Foto Ihres Schreibens per WhatsApp – wir besprechen gemeinsam, was zu tun ist.</p>
      <a class="btn" style="background:#1a1307;color:var(--gold2);align-self:flex-start" href="{WA}" target="_blank" rel="noopener">Foto senden</a>
    </div>
  </div>
</div></section>

<section id="international" class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">02 · Internationale Beratung</span><h2>Wir machen Pläne <span class="gold">wahr</span></h2><p>Verlässliche Lösungen in internationaler Beratung, Investition und Staatsbürgerschaft.</p></div>
  <div class="grid g2">
    {svc('globe','Staatsbürgerschaft im Ausland','Mit verlässlichen Informationen, der richtigen Orientierung und professioneller Beratung erleichtern wir Ihre Verfahren. Mit langjähriger Erfahrung begleiten wir Sie bei jedem Schritt.')}
    {svc('house','Immobilieninvestition','Wir unterstützen Sie dabei, Ihre Zukunft mit rentablen Investitionsmöglichkeiten abzusichern – beim Kauf, Verkauf und Investieren in Deutschland und im Ausland.')}
    {svc('chart','Investitionsberatung','Mit der richtigen Strategie und unserem internationalen Netzwerk helfen wir Ihnen, Ihre finanziellen Ziele zu erreichen.')}
    {svc('cap','Bildungs- und Karriereberatung','Wir helfen Ihnen, Ihre Zukunft mit Bildungs- und Karrierechancen im Ausland zu gestalten – Orientierung für junge Menschen und Familien.')}
  </div>
  <div style="margin-top:64px">{QUOTE_VISION}</div>
</div></section>

<section id="zusatz"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">03 · Zusätzliche Leistungen</span><h2>Kreativ &amp; <span class="gold">besonders</span></h2><p>Unsere Zusatzleistungen bieten wir gemeinsam mit verlässlichen Partnern an.</p></div>
  <div class="grid g3">
    {svc('camera','Organisation &amp; Fotografie','Organisation und professionelle Fotografie für Ihre besonderen Anlässe.')}
    {svc('mega','Werbung &amp; Management','Werbung, Präsentation und Management für Ihr Unternehmen und Ihre Projekte.')}
    {svc('ring','Hochzeit · Beschneidung · Henna','Wir planen und verewigen die schönsten Tage Ihres Lebens.')}
    {svc('mic','Interviews auf Deutsch &amp; Türkisch','Zweisprachige Interviews und Moderation mit TV- und Medienerfahrung.')}
    {svc('key','Immobilien','Suche, Vermittlung und Beratung bei Miet- und Kaufimmobilien.')}
    {svc('house','Bau · Elektro · Türen/Fenster/Terrassen','Für Renovierung, Elektroarbeiten, Türen, Fenster und Terrassen – gemeinsam mit unseren Partnern.')}
  </div>
  <div class="btns reveal" style="justify-content:center;margin-top:36px"><a class="btn btn-ghost" href="fotografie.html">Alle kreativen Leistungen {svg('arrow')}</a></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">So arbeiten wir</span><h2>In vier Schritten <span class="gold">zur Lösung</span></h2></div>
  <div class="grid g4 steps">
    <div class="card step reveal">{ic('phone')}<h3>Kontakt</h3><p>Melden Sie sich per WhatsApp, Telefon oder E-Mail und schildern Sie kurz Ihr Anliegen.</p></div>
    <div class="card step reveal">{ic('clock')}<h3>Termin</h3><p>Wir vereinbaren einen passenden Termin in unserem Büro in der Kirchstr. 33.</p></div>
    <div class="card step reveal">{ic('doc')}<h3>Prüfung</h3><p>Wir sehen uns Ihre Unterlagen gemeinsam an und erklären die nächsten Schritte.</p></div>
    <div class="card step reveal">{ic('bolt')}<h3>Begleitung</h3><p>Wir unterstützen bei Schriftverkehr und Anträgen und halten Sie auf dem Laufenden.</p></div>
  </div>
</div></section>

<section><div class="wrap" style="max-width:860px">
  <div class="sec-head reveal"><span class="eyebrow">Häufige Fragen</span><h2>Gut zu <span class="gold">wissen</span></h2></div>
  <div class="reveal">
    <details><summary>Kann ich ohne Termin ins Büro kommen?</summary><p>Damit wir uns Zeit für Sie nehmen können, bitten wir Sie, vorab per WhatsApp oder Telefon einen Termin zu vereinbaren.</p></details>
    <details><summary>Welche Unterlagen soll ich mitbringen?</summary><p>Alle Schreiben zum Thema, Ausweis/Reisepass, Aufenthaltstitel und ggf. frühere Korrespondenz. Wenn Sie unsicher sind, schicken Sie uns vorab ein Foto – wir stellen die Liste gemeinsam zusammen.</p></details>
    <details><summary>Ich spreche nicht gut Deutsch – ist das ein Problem?</summary><p>Nein. Wir erklären alles auf Türkisch und unterstützen Sie beim Schriftverkehr auf Deutsch.</p></details>
    <details><summary>Was kostet die Unterstützung?</summary><p>Die Kosten richten sich nach dem Umfang und werden im Erstgespräch transparent festgelegt. Fragen Sie uns nach aktuellen Aktionen.</p></details>
  </div>
</div></section>
{cta()}
''')

# ───────────── ÜBER UNS ─────────────
page('ueber-uns.html','Über uns – Wer ist Bahar Sonek?',
 'Die Geschichte der Unternehmerin Bahar Sonek: 1982 in Gelsenkirchen geboren, Familie aus Adana – von der Versicherungsbranche zum eigenen Büro, von internationaler Beratung zu Auszeichnungen.', f'''
{hero('Über uns','Wer ist <span class="script gold" style="font-size:1.2em">Bahar Sonek?</span>','Ein Weg von einer eher zurückhaltenden jungen Frau zu einer offenen, starken und inspirierenden Unternehmerin.','Über uns')}

<section><div class="wrap split">
  <div class="fx-portrait fx-about reveal">{fx_portrait('img/bahar-hakkimizda.webp',360,610)}</div>
  <div class="reveal">
    <span class="eyebrow">Unsere Geschichte</span>
    <h2>Der Gesellschaft nützen, <span class="gold">Menschen den Weg zeigen</span></h2>
    <p>Bahar Sonek wurde 1982 in Gelsenkirchen geboren. Ihre Familie stammt aus Adana; ihre Schulzeit schloss sie am Gymnasium in Deutschland ab. Vor rund 12 Jahren begann sie ihren beruflichen Weg in der Versicherungsbranche.</p>
    <p>Mit wachsendem Wissen und Erfahrung gründete sie ihr eigenes Büro – ihr Ziel war stets, besser zu werden und sich weiterzuentwickeln. Später spezialisierte sie sich auf Staatsbürgerschaften im Ausland, besuchte zahlreiche Fortbildungen und wurde für ihre Arbeit mehrfach ausgezeichnet.</p>
    <p>Der Gesellschaft zu nützen und Menschen den Weg zu zeigen, ist ihre wichtigste Motivation. Früher eher zurückhaltend, hat dieser Weg sie zu einer offenen, starken und inspirierenden Frau gemacht. Heute ist Bahar Sonek eine visionäre Unternehmerin, die in vielen Bereichen aktiv ist und ihren Weg entschlossen weitergeht.</p>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Der Weg</span><h2>Schritt für Schritt <span class="gold">bis heute</span></h2></div>
  <div class="timeline">
    <div class="tl reveal"><div class="dot">1</div><div><small>1982</small><h3>Geboren in Gelsenkirchen</h3><p>Als Tochter einer Familie aus Adana in Gelsenkirchen geboren.</p></div></div>
    <div class="tl reveal"><div class="dot">2</div><div><small>Schule</small><h3>Gymnasium</h3><p>Schulabschluss am Gymnasium in Deutschland.</p></div></div>
    <div class="tl reveal"><div class="dot">3</div><div><small>vor ca. 12 Jahren</small><h3>Versicherungsbranche</h3><p>Beginn des beruflichen Weges in der Versicherungsbranche.</p></div></div>
    <div class="tl reveal"><div class="dot">4</div><div><small>Selbstständigkeit</small><h3>Eigenes Büro</h3><p>Gründung des eigenen Büros in Gelsenkirchen: Creative Dienstleistungen.</p></div></div>
    <div class="tl reveal"><div class="dot">5</div><div><small>Spezialisierung</small><h3>Internationale Beratung</h3><p>Spezialisierung auf Staatsbürgerschaften im Ausland, zahlreiche Fortbildungen.</p></div></div>
    <div class="tl reveal"><div class="dot">6</div><div><small>Heute</small><h3>Auszeichnungen, Medien und D.G.K.</h3><p>„Beste international erfolgreiche Übersetzerin und Beraterin des Jahres“ (2026) und „Erfolgreichste Geschäftsfrau des Jahres“ („Avrupa'nın Yıldızları“); Sendungen bei TELE1 und Business Channel Türk TV; Regionalpräsidentin des Weltjugendrats in Deutschland.</p></div></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Unsere Werte</span><h2>Was uns <span class="gold">ausmacht</span></h2></div>
  <div class="grid g4">
    <div class="card reveal">{ic('shield')}<h3>Vertrauen</h3><p>Ihre Daten und Unterlagen sind bei uns sicher – Vertraulichkeit hat Vorrang.</p></div>
    <div class="card reveal">{ic('bolt')}<h3>Schnelligkeit</h3><p>Wir behalten Fristen im Blick und erledigen Ihre Anliegen rechtzeitig.</p></div>
    <div class="card reveal">{ic('star')}<h3>Richtigkeit</h3><p>Richtige Informationen, richtige Orientierung – „Richtige Unterstützung“ ist unser Name.</p></div>
    <div class="card reveal">{ic('heart')}<h3>Herzlichkeit</h3><p>Wir hören jedem Menschen zu wie einem Familienmitglied – auf Deutsch oder Türkisch.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Unterwegs</span><h2>Gespräche, Veranstaltungen, <span class="gold">Begegnungen</span></h2></div>
  {poster_grid([('pkm-toplanti.jpg','Geschäftstermine','PKM Unternehmensgruppe'),('musiad-koln.jpg','MÜSİAD NRW-Köln','„Neue Ära für Investitionen in der Türkei“'),('summit-3.jpg','Life &amp; Beauty Summit','Als Gast eingeladen'),('dgk-genel-merkez.jpg','D.G.K.-Zentrale','Teamtreffen')])}
  <div style="margin-top:70px">{QUOTE_VISION}</div>
</div></section>

<section><div class="wrap split rev">
  <div class="photo reveal"><img src="img/dgk-ofis.jpg" alt="D.G.K. Deutschland" style="aspect-ratio:4/3"></div>
  <div class="reveal">
    <span class="eyebrow">Ehrenamt</span>
    <h2>Weltjugendrat – <span class="gold">Regionalpräsidentin Deutschland</span></h2>
    <p>Neben ihrer beruflichen Tätigkeit engagiert sie sich als Regionalpräsidentin des Weltjugendrats (D.G.K.) in Deutschland für junge Menschen.</p>
    <a class="btn btn-ghost" href="dgk.html">D.G.K. Deutschland {svg('arrow')}</a>
  </div>
</div></section>
{cta('Wir hören Ihnen zu.')}
''')

# ───────────── MEDIEN & PREISE ─────────────
page('medien-auszeichnungen.html','Medien & Auszeichnungen – Bahar Sonek',
 'TV-Sendungen bei TELE1, Business Channel Türk TV und TLC, Interviews in Zeitungen und Magazinen sowie Auszeichnungen und Urkunden.', f'''
{hero('Medien &amp; Kreatives','Im TV, auf der Bühne, <span class="gold">vor Ort</span>','TV-Sendungen, Interviews und Auszeichnungen für unternehmerisches Engagement.','Medien &amp; Preise')}

<section><div class="wrap split">
  <div class="reveal">
    <span class="eyebrow">TV-Sendungen</span>
    <h2>Gast und <span class="gold">Moderatorin</span></h2>
    <p>Bei Business Channel Türk TV, TLC und weiteren Sendern war sie als Gast und Moderatorin zu sehen. Mit Interviews auf Deutsch und Türkisch bringt sie die Stimme der türkischen Community in Deutschland auf den Bildschirm.</p>
    <ul class="checks"><li>TELE1 – Live-Sendung „Almanya–Türkiye İşbirlikleri“ (8. August 2026)</li><li>Business Channel Türk TV</li><li>TLC</li><li>Interviews auf Deutsch &amp; Türkisch</li></ul>
  </div>
  <div class="tv reveal">
    <figure data-zoom style="cursor:zoom-in"><img src="img/tv-1.jpg" alt="Interview bei TLC"></figure>
    <figure data-zoom style="cursor:zoom-in;margin-top:40px"><img src="img/tv-2.jpg" alt="Im TV-Studio"></figure>
    <figure data-zoom style="cursor:zoom-in"><img src="img/tv-3.jpg" alt="Bahar Sonek"></figure>
  </div>
</div></section>

<section class="band"><div class="wrap grid g2">
  <div class="card reveal">{ic('news')}<h3>Zeitungs- und Magazininterviews</h3><p>Interviews zu Unternehmertum, Frauenförderung und internationaler Beratung. Titelseite der Ausgabe August 2026 des Wirtschafts- und Kunstmagazins „Bizden Bil“; Beiträge u. a. in der Neriman Dergisi.</p></div>
  <div class="card reveal">{ic('trophy')}<h3>„Avrupa'nın Yıldızları“</h3><p>Von der Neriman Dergisi als „Erfolgreichste Geschäftsfrau des Jahres“ ausgezeichnet.</p></div>
  <div class="card reveal">{ic('star')}<h3>Beste Übersetzerin &amp; Beraterin des Jahres</h3><p>Bei den 5. Altın Meslek &amp; Kariyer Ödülleri der Cihat Dündar Organisation (30. Juli 2026, Istanbul) als „Beste international erfolgreiche Übersetzerin und Beraterin des Jahres“ ausgezeichnet.</p></div>
  <div class="card reveal">{ic('globe')}<h3>Beraterin türkischer Unternehmer</h3><p>Tätig in internationaler Übersetzung, Beratung und Öffentlichkeitsarbeit – mit Schwerpunkt auf wirtschaftlicher, kommerzieller und kultureller Zusammenarbeit zwischen Deutschland und der Türkei.</p></div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">2026</span><h2>Sendungen &amp; <span class="gold">Preisverleihungen</span></h2><p>Zum Vergrößern auf die Bilder klicken.</p></div>
  {poster_grid([('tele1-canli-yayin.jpg','Live bei TELE1','Deutsch-türkische Kooperationen · mit Psychologin Alanur Özalp'),('bizden-bil-kapak.jpg','Titel „Bizden Bil“','Wirtschafts- und Kunstmagazin · August 2026'),('altin-meslek-odul.jpg','5. Altın Meslek &amp; Kariyer Ödülleri','30. Juli 2026 · Istanbul, Suzy Event House'),('summit-odul.jpg','Life &amp; Beauty Summit','Preisverleihung')])}
  <div class="sec-head reveal" style="margin:80px auto 40px"><span class="eyebrow">Veranstaltungen</span><h2>Vom <span class="gold">roten Teppich</span></h2></div>
  {poster_grid([('summit-1.jpg','Life &amp; Beauty Summit','Roter Teppich'),('summit-2.jpg','Life &amp; Beauty Summit','Als Gast eingeladen'),('summit-3.jpg','Life &amp; Beauty Summit','DoubleTree by Hilton'),('musiad-koln.jpg','MÜSİAD NRW-Köln','„Neue Ära für Investitionen in der Türkei“')])}
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Urkunden &amp; Auszeichnungen</span><h2>Erfolge &amp; <span class="gold">Preise</span></h2><p>Auszeichnungen für unser Engagement in Unternehmertum, Frauenförderung und internationaler Beratung sind für uns eine große Ehre. Zum Vergrößern anklicken.</p></div>
  {awards_grid(AWARDS_DE)}
  <p class="muted reveal" style="text-align:center;margin-top:30px;font-style:italic">… und viele weitere Urkunden und Danksagungen.</p>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Projekte, die wir unterstützen</span><h2>Buch &amp; <span class="gold">Podcast</span></h2></div>
  <div class="split">
    <div class="photo gold-frame reveal" style="max-width:340px;margin:0 auto"><img src="img/book.jpg" alt="Üzülme Yalnız Değilsin – Melissa İrem Türkeri"></div>
    <div class="reveal">
      <span class="eyebrow">Melissa İrem Türkeri</span>
      <h2>„Üzülme Yalnız Değilsin“</h2>
      <p>Melissa İrem Türkeri begann ihren Weg als Autorin 2024 mit dem Buch „Üzülme Yalnız Değilsin“ (Sei nicht traurig, du bist nicht allein). Mit starken Botschaften und einer sehr persönlichen Erzählweise fand das Buch schnell viele Leserinnen und Leser; im selben Jahr wurde die Autorin dafür ausgezeichnet.</p>
      <div class="card" style="margin-top:20px">{ic('mic')}<h3>Podcast: <span class="script gold" style="font-size:1.3em">Melissa ile Bunu da Konuşalım</span></h3><p>Jede Woche persönliche und inspirierende Gespräche über Leben, Beziehungen, Erfolg und persönliche Entwicklung (auf Türkisch).</p></div>
    </div>
  </div>
  <div class="quote reveal" style="margin-top:50px"><div class="qm">“</div><blockquote>Wenn Worte das Herz berühren, beginnt dort die Veränderung.</blockquote></div>
</div></section>

<section><div class="wrap" style="text-align:center">
  <div class="sec-head reveal"><span class="eyebrow">Video</span><h2>Interviews &amp; <span class="gold">Videos</span></h2><p>Interviews, Sendungen und mehr. Zum Abspielen klicken.</p></div>
  {video_grid()}
  <a class="btn btn-gold reveal" style="margin-top:28px" href="https://www.youtube.com/@baharsonek2023" target="_blank" rel="noopener">{YT_SVG.replace('<svg','<svg fill="currentColor"')} Alle Videos: YouTube-Kanal</a>
</div></section>
{cta('Interviews &amp; Kooperationen', 'Für Sendungen, Interviews, Moderationen oder Kooperationsanfragen kontaktieren Sie uns gern.')}
''')

# ───────────── FOTOGRAFIE ─────────────
page('fotografie.html','Fotografie & Organisation – Bahar Sonek Creative',
 'Organisation und professionelle Fotografie für Hochzeiten, Beschneidungsfeiern, Henna-Abende und besondere Anlässe. Werbung, Management und Interviews. Gelsenkirchen.', f'''
{hero('Creative Dienstleistungen','Ihre besonderen Tage, <span class="gold">für immer festgehalten</span>','Mit eleganten, natürlichen und unvergesslichen Fotos halten wir die schönsten Momente für Sie fest.','Fotografie')}

<section><div class="wrap split">
  <div class="photo reveal"><img src="img/photographer.jpg" alt="Professionelles Fotoshooting" style="aspect-ratio:4/5"></div>
  <div class="reveal">
    <span class="eyebrow">Bahar Sonek Creative</span>
    <h2>Ihre Erinnerungen <span class="gold">in guten Händen</span></h2>
    <p>Wir halten die schönsten Momente Ihrer besonderen Tage in professionellen Bildern fest – von der Planung über das Shooting bis zum fertigen Album.</p>
    <p>Mit Gespür für türkische Kultur und Traditionen fangen wir die Emotionen eines Henna-Abends, die Freude einer Beschneidungsfeier und die Eleganz Ihrer Hochzeit auf natürliche Weise ein.</p>
    <a class="btn btn-gold" href="kontakt.html?konu=Organisation">Termin anfragen {svg('arrow')}</a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Shootings &amp; Organisation</span><h2>Was wir <span class="gold">machen</span></h2></div>
  <div class="grid g3">
    <div class="card hover reveal">{ic('ring')}<h3>Hochzeit</h3><p>Von den Vorbereitungen bis zum letzten Tanz – natürliche, elegante Bilder.</p></div>
    <div class="card hover reveal">{ic('heart')}<h3>Henna-Abend</h3><p>Bilder voller Emotionen und Farben der Tradition.</p></div>
    <div class="card hover reveal">{ic('star')}<h3>Beschneidungsfeier</h3><p>Der glücklichste Tag Ihrer Familie in fröhlichen, bunten Bildern.</p></div>
    <div class="card hover reveal">{ic('camera')}<h3>Feste &amp; Porträts</h3><p>Verlobung, Geburtstag, Familien- und Business-Porträts.</p></div>
    <div class="card hover reveal">{ic('mega')}<h3>Werbung &amp; Management</h3><p>Imagefotos, Social-Media-Inhalte und Management für Unternehmen.</p></div>
    <div class="card hover reveal">{ic('mic')}<h3>Interviews &amp; Moderation</h3><p>Interviews, Veranstaltungs- und Galamoderation auf Deutsch und Türkisch.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Ablauf</span><h2>Vom Traum <span class="gold">zum Bild</span></h2></div>
  <div class="grid g4 steps">
    <div class="card step reveal"><h3>Kennenlernen</h3><p>Wir sprechen über Datum, Location und Ihr Wunschkonzept.</p></div>
    <div class="card step reveal"><h3>Planung</h3><p>Ablauf, Shotlist und Organisationsdetails werden festgelegt.</p></div>
    <div class="card step reveal"><h3>Der große Tag</h3><p>Sie genießen den Moment – wir halten ihn fest.</p></div>
    <div class="card step reveal"><h3>Übergabe</h3><p>Sorgfältig bearbeitete Bilder erhalten Sie digital.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap split rev">
  <div class="photo reveal"><img src="img/flyer-top.jpg" alt="Visitenkarte Bahar Sonek" style="aspect-ratio:16/9"></div>
  <div class="reveal">
    <span class="eyebrow">Immobilien</span>
    <h2>Gemeinsam Ihr <span class="gold">neues Zuhause finden</span></h2>
    <p>Suche, Bewertung und Vermittlung von Miet- und Kaufimmobilien – auch bei deutschen Unterlagen und Verträgen sind wir an Ihrer Seite.</p>
    <a class="btn btn-ghost" href="kontakt.html?konu=Immobilien">Zu Immobilien anfragen {svg('arrow')}</a>
  </div>
</div></section>
{cta('Ist Ihr Termin noch frei?', 'Reservieren Sie schon jetzt Ihren Termin für Ihren besonderen Tag. Schreiben Sie uns für Verfügbarkeit und Details.')}
''')

# ───────────── D.G.K. ─────────────
page('dgk.html','Weltjugendrat (D.G.K.) – Regionalpräsidentschaft Deutschland | Bahar Sonek',
 'Bahar Sonek ist Regionalpräsidentin des Weltjugendrats (Dünya Gençlik Konseyi, D.G.K.) in Deutschland. Förderprogramme für junge Menschen und Familien, Solidarität und internationale Zusammenarbeit.', f'''
{dgk_role_hero()}

<section><div class="wrap split">
  <div class="reveal" style="display:grid;place-items:center">
    <div style="width:min(340px,80vw);aspect-ratio:1;border-radius:50%;padding:10px;box-shadow:0 0 0 1px var(--gold),0 0 0 12px rgba(212,169,74,.08),0 0 90px rgba(212,169,74,.18)">
      <img src="img/dgk-logo.png" alt="Logo des Weltjugendrats (Dünya Gençlik Konseyi)" style="width:100%;height:100%;object-fit:contain">
    </div>
  </div>
  <div class="reveal">
    <span class="eyebrow">Über den Weltjugendrat</span>
    <h2>Die Kraft der Jugend, <span class="gold">die Zukunft der Welt</span></h2>
    <p>Der Weltjugendrat (Dünya Gençlik Konseyi, D.G.K.) mit Sitz in Istanbul setzt sich für die soziale, kulturelle, schulische und wirtschaftliche Entwicklung junger Menschen ein. Seine Arbeit reicht von Bildung und Sport über Kultur, Kunst und Technologie bis zu Unternehmertum und sozialen Projekten.</p>
    <p>Mit der Ernennung durch Generalpräsident Hüseyin Celep wurde Bahar Sonek beauftragt, im Namen des Rates in der Bundesrepublik Deutschland tätig zu sein – als <b style="color:var(--gold2)">Regionalpräsidentin Deutschland</b>.</p>
    <div class="btns"><a class="btn btn-gold" href="kontakt.html?konu=D.G.K.">Ehrenamtlich mitmachen</a><a class="btn btn-ghost" href="https://www.dunyagenclikkonseyi.org" target="_blank" rel="noopener">dunyagenclikkonseyi.org {svg('arrow')}</a></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Regionalpräsidentschaft Deutschland</span><h2>Fünf zentrale <span class="gold">Ziele</span></h2></div>
  <div class="grid g3">
    <div class="card reveal">{ic('users')}<h3>Jugendsolidarität</h3><p>Ein starkes Netzwerk, das junge Menschen in Deutschland zusammenbringt.</p></div>
    <div class="card reveal">{ic('cap')}<h3>Bildungsförderung</h3><p>Orientierung und Unterstützung auf dem Weg durch Schule, Ausbildung und Beruf.</p></div>
    <div class="card reveal">{ic('shield')}<h3>Chancengleichheit</h3><p>Eine Gesellschaft, in der alle jungen Menschen und Familien gleiche Chancen haben.</p></div>
    <div class="card reveal">{ic('chart')}<h3>Unternehmertum &amp; Innovation</h3><p>Begleitung für junge Menschen, die ihre Ideen verwirklichen möchten.</p></div>
    <div class="card reveal">{ic('globe')}<h3>Internationale Zusammenarbeit</h3><p>Projekte und Partnerschaften als Brücke zwischen der Türkei und Deutschland.</p></div>
    <div class="card reveal" style="background:var(--grad);color:#1a1307;border:none;display:grid;place-items:center;text-align:center"><div><span class="script" style="font-size:2.3rem;line-height:1.15;display:block">Gemeinsam schaffen,<br>gemeinsam wachsen</span></div></div>
  </div>
</div></section>

<section><div class="wrap split">
  <figure class="photo gold-frame reveal" data-zoom style="cursor:zoom-in;max-width:440px;margin:0 auto"><img src="img/fb/dgk-destek-programlari.jpg" alt="Plakat: Förderprogramme für junge Menschen und Familien"></figure>
  <div class="reveal">
    <span class="eyebrow">Starke Jugend · Starke Familie · Starke Zukunft</span>
    <h2>Förderprogramme für <span class="gold">junge Menschen und Familien</span></h2>
    <p>Die geplanten Programme werden zeitgleich in der Türkei und in Deutschland umgesetzt – eine Vision, eine gemeinsame Zukunft.</p>
    <ul class="checks">
      <li>Bildungsförderprogramme</li><li>Beschäftigung und berufliche Entwicklung</li><li>Unterstützung für Familien und Gesellschaft</li>
      <li>Jugendprojekte</li><li>Soziale Solidarität und Kultur</li><li>Neue Chancen und internationale Kooperationen</li>
    </ul>
    <a class="btn btn-gold" href="kontakt.html?konu=D.G.K.">Informationen anfordern</a>
  </div>
</div></section>

<section class="band"><div class="wrap split rev">
  <figure class="photo reveal" data-zoom style="cursor:zoom-in"><img src="img/fb/dgk-destek-cagrisi.jpg" alt="Plakat: Aufruf zur Unterstützung"></figure>
  <div class="reveal">
    <span class="eyebrow">Aufruf</span>
    <h2>Soziale Teilhabe <span class="gold">trotz wirtschaftlicher Not</span></h2>
    <div class="quote" style="text-align:left;padding:0;margin:0"><div class="qm">“</div><blockquote style="font-size:1.3rem">Menschen bereichern ihr Leben, indem sie neue Lebensräume entdecken und reisen. Doch wegen wirtschaftlicher Schwierigkeiten bleiben vielen Familien diese Möglichkeiten verwehrt. Indem wir die soziale Solidarität stärken, müssen wir gemeinsam ein gerechteres und zugänglicheres Leben für alle aufbauen.</blockquote><cite>Bahar Sonek</cite></div>
    <p style="margin-top:18px">Mit Projekten, die die soziale Teilhabe benachteiligter junger Menschen und Familien fördern, schenken wir Hoffnung: <b style="color:var(--gold2)">Das Leben berühren, die Jugend zurückgewinnen.</b></p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="quote reveal"><span class="eyebrow">Botschaft der Regionalpräsidentin</span><div class="qm" style="margin-top:14px">“</div><blockquote>Glückliche Menschen bedeuten starke Familien – und starke Familien eine starke Gesellschaft. Gemeinsam müssen wir für eine Zukunft arbeiten, in der alle am sozialen Leben teilhaben, reisen und mit Hoffnung nach vorne blicken können.</blockquote><cite>Bahar Sonek · Regionalpräsidentin D.G.K. Deutschland</cite></div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Ernennung &amp; Team</span><h2>Gemeinsam sind <span class="gold">wir stark</span></h2><p>Zum Vergrößern auf die Bilder klicken.</p></div>
  {poster_grid([('dgk-mazbata.jpg','Ernennungsurkunde','Regionalpräsidentschaft Deutschland des D.G.K.'),('dgk-almanya-afis.jpg','Regionalpräsidentschaft Deutschland','„Die Kraft der Jugend – die Zukunft der Welt“'),('dgk-genel-merkez.jpg','Team der Zentrale','Treffen in der D.G.K.-Zentrale'),('dgk-toplanti.jpg','D.G.K. Deutschland','Gemeinsam mit jungen Menschen')])}
</div></section>
{cta('Mit jungen Menschen, für junge Menschen.', 'Sie möchten sich ehrenamtlich engagieren, unterstützen oder kooperieren? Schreiben Sie uns.')}
''')

# ───────────── AKTUELLES ─────────────
page('aktuelles.html','Aktuelles – Bahar Sonek',
 'Aktuelle Beiträge, Veranstaltungen, Auszeichnungen und Projekte von Bahar Sonek und dem D.G.K. Deutschland.', f'''
{hero('Aktuelles','Beiträge &amp; <span class="gold">Veranstaltungen</span>','Aktuelle Beiträge, Veranstaltungen, Auszeichnungen und Projekte – zusammengestellt von unserer Facebook-Seite.','Aktuelles')}
<section><div class="wrap">
  <div class="filters" data-news-filters></div>
  <div class="news-grid" data-news-all></div>
</div></section>
<section class="band"><div class="wrap">
  <div class="sec-head reveal"><span class="eyebrow">Social Media</span><h2>Folgen Sie <span class="gold">uns</span></h2><p>Die neuesten Beiträge, Videos und Ankündigungen auf unseren Kanälen.</p></div>
  <div class="social-cards two">
    <a class="social-card reveal" href="https://www.facebook.com/baharsonek.official" target="_blank" rel="noopener">{FB_SVG}<span><b>Facebook</b><small>Bahar Sonek (Official)</small></span></a>
    <a class="social-card reveal" href="https://www.youtube.com/@baharsonek2023" target="_blank" rel="noopener">{YT_SVG}<span><b>YouTube</b><small>@baharsonek2023</small></span></a>
  </div>
  <div class="feed-consent" data-social-feed>
    <h3 style="margin-bottom:8px">Live-Feed aus den sozialen Medien</h3>
    <p class="muted" style="max-width:520px;margin:0 auto 18px">Beim Laden des Feeds werden Daten an den Social-Media-Anbieter übertragen. Details in der <a href="datenschutz.html" style="color:var(--gold2)">Datenschutzerklärung</a>.</p>
    <button class="btn btn-gold">Feed anzeigen</button>
  </div>
</div></section>
{cta('Bleiben Sie informiert', 'Schreiben Sie uns per WhatsApp – wir informieren Sie über Veranstaltungen, Seminare und Neuigkeiten.')}
''')

# ───────────── KONTAKT ─────────────
page('kontakt.html','Kontakt – Bahar Sonek | Kirchstr. 33 Gelsenkirchen',
 'Kontakt zu Bahar Sonek: 01520-2614684, baharsonek.official@gmail.com, Kirchstr. 33, 45879 Gelsenkirchen. Schreiben Sie uns für Informationen und Termine.', f'''
{hero('Kontakt','Informationen &amp; <span class="gold">Termine</span>','Am schnellsten erreichen Sie uns per WhatsApp. Im Büro empfangen wir Sie nach Terminvereinbarung.','Kontakt')}

{map_section()}

<section><div class="wrap grid g2" style="gap:28px;align-items:start">
  <div class="card reveal" style="padding:34px">
    <h3 style="font-size:1.6rem;margin-bottom:10px">Kontaktdaten</h3>
    <div class="cinfo">
      {cline('phone','Telefon / WhatsApp',f'<a href="{TEL}">01520 – 2614684</a>')}
      {cline('mail','E-Mail','<a href="mailto:baharsonek.official@gmail.com">baharsonek.official@gmail.com</a>')}
      {cline('mail','Creative E-Mail','<a href="mailto:baharsonekcreative@gmail.com">baharsonekcreative@gmail.com</a>')}
      {cline('pin','Adresse','Kirchstr. 33, 45879 Gelsenkirchen, Deutschland')}
      {cline('clock','Öffnungszeiten','Nach Vereinbarung')}
    </div>
    {SOCIAL}
  </div>
  <div class="card reveal" style="padding:34px">
    <h3 style="font-size:1.6rem;margin-bottom:6px">Nachricht senden</h3>
    <p style="margin-bottom:20px">Füllen Sie das Formular aus – Ihre Nachricht geht per E-Mail direkt an Bahar Sonek. Alternativ können Sie dieselbe Nachricht per WhatsApp senden.</p>
    <div class="form-msg ok" data-form-ok hidden>Vielen Dank! Ihre Nachricht ist bei uns angekommen – wir melden uns so schnell wie möglich.</div>
    <div class="form-msg err" data-form-err hidden>Die Nachricht konnte nicht gesendet werden. Bitte versuchen Sie es erneut oder kontaktieren Sie uns per WhatsApp / Telefon.</div>
    <form class="contact" id="form" method="post" action="../kontakt.php">
      <input type="hidden" name="lang" value="de">
      <input type="text" name="website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="row">
        <label class="f">Vor- und Nachname<input name="ad" required autocomplete="name"></label>
        <label class="f">Telefon<input name="tel" type="tel" required autocomplete="tel"></label>
      </div>
      <label class="f">E-Mail<input name="email" type="email" required autocomplete="email"></label>
      <label class="f">Betreff<select name="konu">
        <option>Behördliche Angelegenheiten</option><option>Jobcenter</option><option>Ausländerbehörde</option>
        <option>Schriftverkehr mit Behörden</option><option>Übersetzung</option><option>Staatsbürgerschaft im Ausland</option>
        <option>Investition / Immobilieninvestition</option><option value="Immobilien">Immobilien</option>
        <option value="Organisation">Organisation &amp; Fotografie</option><option value="D.G.K.">D.G.K. Deutschland</option><option>Sonstiges</option>
      </select></label>
      <label class="f">Ihre Nachricht<textarea name="mesaj" required placeholder="Wie können wir Ihnen helfen?"></textarea></label>
      <label class="consent"><input type="checkbox" required> <span>Ich habe die <a href="datenschutz.html">Datenschutzerklärung</a> gelesen und bin einverstanden, dass meine Angaben zur Beantwortung meiner Anfrage verwendet werden.</span></label>
      <div class="form-btns">
        <button type="submit" class="btn btn-gold">{svg('mail')} E-Mail senden</button>
        <button type="button" class="btn btn-wa" data-wa-send>{WA_SVG.replace('<svg','<svg fill="currentColor"')} Per WhatsApp senden</button>
      </div>
    </form>
  </div>
</div></section>

''')
