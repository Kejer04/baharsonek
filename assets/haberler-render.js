/* Haber kartlarını çizer – TR ve DE için ortak */
(function () {
  const DE = document.documentElement.lang === "de";
  const AY = DE ? ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]
                : ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"];
  const T = DE ? { fb: "Auf Facebook ansehen →", more: "Weiterlesen →", all: "Alle", none: "Noch keine Beiträge." }
               : { fb: "Facebook'ta gör →", more: "Devamını oku →", all: "Tümü", none: "Henüz haber yok." };
  const IKON = {
    "D.G.K.": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "Etkinlik": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "Ödül": '<path d="M8 4h8v6a4 4 0 0 1-8 0z"/><path d="M8 6H4v2a4 4 0 0 0 4 4M16 6h4v2a4 4 0 0 1-4 4M12 14v4M8 21h8"/>',
    "Proje": '<path d="M4 20V10M10 20V6M16 20v-8M22 20H2"/><path d="m4 7 6-4 6 5 5-4"/>',
    "Medya": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="m8 3 4 4 4-4"/>',
    "Duyuru": '<path d="M3 10v4h4l7 5V5L7 10z"/><path d="M18 8a5 5 0 0 1 0 8"/>'
  };
  const KAT = { "Veranstaltung": "Etkinlik", "Auszeichnung": "Ödül", "Projekt": "Proje", "Medien": "Medya" };
  const esc = s => String(s || "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const tarihYaz = h => {
    if (h.tarihYazi !== undefined) return h.tarihYazi;
    const d = new Date(h.tarih + "T12:00:00");
    return isNaN(d) ? h.tarih : `${d.getDate()}${DE ? "." : ""} ${AY[d.getMonth()]} ${d.getFullYear()}`;
  };
  const kart = h => `
    <article class="news reveal in">
      <div class="news-img${h.sigdir ? " contain" : ""}"${h.gorsel ? ` style="--bg:url('${esc(new URL(h.gorsel, document.baseURI).href)}')"` : ""}>${h.gorsel
        ? `<img src="${esc(h.gorsel)}" alt="${esc(h.baslik)}" loading="lazy">`
        : `<div class="news-ph"><svg viewBox="0 0 24 24">${IKON[h.kategori] || IKON[KAT[h.kategori]] || IKON.Duyuru}</svg></div>`}
        <span class="news-cat">${esc(h.kategori)}</span></div>
      <div class="news-body">
        ${tarihYaz(h) ? `<time datetime="${esc(h.tarih)}">${tarihYaz(h)}</time>` : ""}
        <h3>${esc(h.baslik)}</h3>
        <p>${esc(h.ozet)}</p>
        ${h.link ? (/^https?:/.test(h.link) ? `<a class="more" href="${esc(h.link)}" target="_blank" rel="noopener">${T.fb}</a>` : `<a class="more" href="${esc(h.link)}">${T.more}</a>`) : ""}
      </div>
    </article>`;

  const liste = (window.HABERLER || []).slice().sort((a, b) => (b.tarih || "").localeCompare(a.tarih || ""));

  document.querySelectorAll("[data-news]").forEach(box => {
    const limit = parseInt(box.dataset.news, 10) || liste.length;
    const filtre = box.dataset.filter;
    const secili = (filtre ? liste.filter(h => h.kategori === filtre) : liste).slice(0, limit);
    box.innerHTML = secili.map(kart).join("") || `<p class="muted">${T.none}</p>`;
  });

  // Kategori filtreleri (haberler sayfası)
  const bar = document.querySelector("[data-news-filters]");
  const hepsi = document.querySelector("[data-news-all]");
  if (bar && hepsi) {
    const kategoriler = [T.all, ...new Set(liste.map(h => h.kategori))];
    bar.innerHTML = kategoriler.map((k, i) => `<button class="chip${i ? "" : " on"}" data-k="${esc(k)}">${esc(k)}</button>`).join("");
    const ciz = k => hepsi.innerHTML = (k === T.all ? liste : liste.filter(h => h.kategori === k)).map(kart).join("");
    ciz(T.all);
    bar.addEventListener("click", e => {
      const b = e.target.closest("button"); if (!b) return;
      bar.querySelectorAll("button").forEach(x => x.classList.toggle("on", x === b));
      ciz(b.dataset.k);
    });
  }

  // Sosyal akış: onaydan sonra yükle
  const akis = document.querySelector("[data-social-feed]");
  if (akis) {
    if (!window.SOSYAL_AKIS_KODU) { akis.hidden = true; }
    else akis.querySelector("button")?.addEventListener("click", () => {
      const r = document.createRange();
      akis.innerHTML = "";
      akis.appendChild(r.createContextualFragment(window.SOSYAL_AKIS_KODU));
    });
  }
})();
