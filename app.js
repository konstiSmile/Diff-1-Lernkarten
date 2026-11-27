(function () {
  'use strict';
  var C = window.CONTENT;
  var KEY = 'lernkiste-v1';
  // Feedback: Google-Apps-Script-Web-App, schreibt in eine private Google-Tabelle
  var FB_URL = 'https://script.google.com/macros/s/AKfycbz4r4-dfoJQUeoy8WQayF3W7S6ddmKt8bujKiew7bUV5JmCUVMop5dhP5pDgDmMZtMm/exec';
  var FB_MAX = 2000, FB_Q = 'lernkiste-fbq', DEV_KEY = 'lernkiste-dev';
  var DEFAULTS = { theme: 'auto', font: 1, cardFilter: 'red', name: '', cardOrder: 'script', testN: 10, examMin: 20, examN: 12, mixMode: 'even', mixSubs: null, stats: 1, statsAsked: 0, lastBackup: 0, ownDirty: 0, ownTip: 0, nagDay: '', mDue: 1, mGoal: 30, mChain: 1, mCount: 1, mMosaic: 1, mBadges: 1, obDone: 0, favs: null, homeHide: null, tint: null, rsMode: 's' };

  // ====================================================================== Helfer
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function nrm(s) { return String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/ß/g, 'ss'); }
  function norm(s) { return String(s).toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]/g, ''); }
  function subj(id) { return C.subjects.filter(function (s) { return s.id === id; })[0]; }
  function chap(sid, cid) { var s = subj(sid); return s && s.chapters.filter(function (c) { return c.id === cid; })[0]; }
  function textOf(html) { var d = document.createElement('div'); d.innerHTML = html; return d.textContent; }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function dayKey(ts) { var d = new Date(ts); return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); }
  function fmt(x) { return (Math.round(x * 10) / 10).toString().replace('.', ','); }
  // Strichsymbole (ersetzen Emojis/Sonderzeichen, v44)
  var IC = {
    x: '<path d="M6 6l12 12M18 6L6 18"/>', back: '<path d="M15 5l-7 7 7 7"/>', check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>', half: '<circle cx="12" cy="12" r="8"/><path d="M12 4v16"/>',
    left: '<path d="M14 6l-6 6 6 6"/>', right: '<path d="M10 6l6 6-6 6"/>', arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>', search: '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>',
    book: '<path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H11v15H5.5A1.5 1.5 0 0 0 4 20.5z"/><path d="M20 5.5A1.5 1.5 0 0 0 18.5 4H13v15h5.5a1.5 1.5 0 0 1 1.5 1.5z"/>',
    cards: '<rect x="3" y="6" width="14" height="14" rx="3"/><path d="M7 3h11a3 3 0 0 1 3 3v11"/>', mc: '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.5"/>',
    tf: '<path d="M4 8.5l2.5 2.5L11 6.5"/><path d="M14 14l6 6M20 14l-6 6"/>', gap: '<rect x="3" y="8" width="18" height="8" rx="2.5"/><path d="M7 12h4"/>',
    clock: '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2M9.5 2.5h5"/>', more: '<circle cx="5" cy="12" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="19" cy="12" r="1.8"/>',
    eyeoff: '<path d="M3 3l18 18"/><path d="M10.6 6.1A9.8 9.8 0 0 1 12 6c5 0 8.5 4 9.5 6a12.6 12.6 0 0 1-2.9 3.6M6.5 7.6C4.5 8.9 3.1 10.7 2.5 12c1 2 4.5 6 9.5 6 1.6 0 3-.4 4.3-1"/><path d="M9.9 10a3 3 0 0 0 4.1 4.1"/>',
    palette: '<path d="M12 3a9 9 0 1 0 0 18c1.2 0 1.8-.8 1.8-1.7 0-1.3-1-1.6-1-2.7 0-1 .8-1.6 1.8-1.6H17a4 4 0 0 0 4-4C21 6.6 17 3 12 3z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7.3" r="1"/><circle cx="14.5" cy="7.3" r="1"/>'
  };
  function ic(n, cls) { return '<svg class="' + (cls || 'i') + '" viewBox="0 0 24 24" aria-hidden="true"' + (n === 'more' ? ' style="fill:currentColor;stroke:none"' : '') + '>' + IC[n] + '</svg>'; }
  var CHEV = '<svg class="chev" viewBox="0 0 8 14" aria-hidden="true"><path d="M1 1l6 6-6 6"/></svg>';
  // v56: aus der Suche geöffnet (hl= im Link) → Zurück führt in die Suche mit dem Suchbegriff
  var lastQ = '';
  function fromSearch() { return /[?&]hl=/.test(location.hash); }
  function backHref(def) { return fromSearch() ? '#/suche' + (lastQ ? '?q=' + encodeURIComponent(lastQ) : '') : def; }
  function backLink(href, label) { return '<a href="' + href + '" style="gap:4px">' + ic('back') + esc(label) + '</a>'; }
  function appName() {
    var n = (DB.settings.name || '').trim().replace(/\s+/g, ' ');
    if (!n) return C.name;
    return n + (/[sßxz]$/i.test(n) ? "'" : 's') + ' Lernkiste';
  }
  function toast(msg, actionLabel, action) {
    $$('.toast').forEach(function (x) { x.remove(); });
    var t = document.createElement('div'); t.className = 'toast' + (msg.length > 40 ? ' long' : ''); t.appendChild(document.createTextNode(msg));
    if (actionLabel) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'toastact'; b.textContent = actionLabel;
      b.onclick = function () { t.remove(); action(); }; t.appendChild(b);
    }
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, actionLabel ? 6000 : 2600);
  }
  // ---- Feedback-Warteschlange (bleibt bei Offline erhalten, eigener Speicher, nicht im Backup)
  function fbQueue(v) {
    try {
      if (v === undefined) { var q = JSON.parse(localStorage.getItem(FB_Q) || '[]'); return Array.isArray(q) ? q : []; }
      if (v.length) localStorage.setItem(FB_Q, JSON.stringify(v.slice(-20))); else localStorage.removeItem(FB_Q);
    } catch (e) {}
    return v || [];
  }
  function fbInfo() { var n = fbQueue().length; return n ? n + (n === 1 ? ' Nachricht wartet' : ' Nachrichten warten') + ' auf Internet' : 'Höchstens ' + FB_MAX + ' Zeichen'; }
  function devId() {
    try {
      var d = localStorage.getItem(DEV_KEY);
      if (!d) { d = 'g' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4); localStorage.setItem(DEV_KEY, d); }
      return d;
    } catch (e) { return 'unbekannt'; }
  }
  var fbBusy = false;
  function fbFlush(done) {
    var q = fbQueue();
    if (fbBusy || !q.length || navigator.onLine === false || !window.fetch) { if (done) done(!q.length); return; }
    fbBusy = true;
    var m = q[0];
    fetch(FB_URL, { method: 'POST', mode: 'no-cors', credentials: 'omit', referrerPolicy: 'no-referrer', headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({ typ: 'feedback', text: m.text, version: C.version, geraet: devId(), seite: m.seite || 'Einstellungen' }) })
      .then(function () {
        fbQueue(fbQueue().filter(function (x) { return !(x.ts === m.ts && x.text === m.text); }));
        fbBusy = false;
        if (fbQueue().length) fbFlush(done); else if (done) done(true);
      })
      .catch(function () { fbBusy = false; if (done) done(false); });
  }
  // ---- Anonyme Nutzungsstatistik (v65: Opt-out, Standard an, abschaltbar in den Einstellungen): keine Geräte-ID
  var statSeen = {}, statHiddenAt = 0;
  // Merker nur auf dem Gerät (nicht im Backup): Datum/Woche der letzten Meldung und ob schon einmal gemeldet. Gesendet werden nur Ja/Nein-Werte.
  var STAT_KEY = 'lernkiste-stat';
  function statMarks() { try { var m = JSON.parse(localStorage.getItem(STAT_KEY) || '{}'); return m && typeof m === 'object' ? m : {}; } catch (e) { return {}; } }
  function statForget() { try { localStorage.removeItem(STAT_KEY); } catch (e) {} }
  function weekKey(ts) {
    var d = new Date(ts), t = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate())), wd = t.getUTCDay() || 7;
    t.setUTCDate(t.getUTCDate() + 4 - wd);
    var y = t.getUTCFullYear(); return y + '-W' + Math.ceil(((t - Date.UTC(y, 0, 1)) / 864e5 + 1) / 7);
  }
  function statPing(art, fach) {
    if (!DB.settings.stats || navigator.onLine === false || !window.fetch) return;
    var body = { typ: 'nutzung', art: art, fach: fach || '', version: C.version }, mark = null;
    if (art === 'start') {
      var now = Date.now(), m = statMarks(), dk = dayKey(now), wk = weekKey(now);
      body.tag = m.d !== dk ? 1 : 0; body.woche = m.w !== wk ? 1 : 0; body.neu = m.e ? 0 : 1;
      mark = { d: dk, w: wk, e: 1 };
    }
    try {
      fetch(FB_URL, { method: 'POST', mode: 'no-cors', credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store', keepalive: true,
        headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(body) })
        .then(function () { if (mark && DB.settings.stats) try { localStorage.setItem(STAT_KEY, JSON.stringify(mark)); } catch (e) {} })
        .catch(function () {});
    } catch (e) {}
  }
  function statFach(sid) {
    if (!DB.settings.stats || statSeen[sid] || !subj(sid)) return;
    statSeen[sid] = 1; statPing('fach', sid);
  }
  function statVisible() {
    if (document.visibilityState === 'hidden') { statHiddenAt = Date.now(); return; }
    if (statHiddenAt && Date.now() - statHiddenAt > 30 * 60 * 1000) { statSeen = {}; statPing('start'); }
    statHiddenAt = 0;
  }
  // ---- Kachel (Overlay) z. B. für den Datenschutz
  var tileEl = null, tileKey = null;
  function closeTile() {
    if (!tileEl) return;
    tileEl.remove(); tileEl = null; document.body.classList.remove('pvopen');
    document.removeEventListener('keydown', tileKey);
  }
  function openTile(title, html, foot) {
    closeTile();
    var w = document.createElement('div'); w.className = 'pvwrap';
    w.innerHTML = '<div class="pvcard" role="dialog" aria-modal="true" aria-label="' + esc(title) + '">' +
      '<div class="pvhead"><b>' + esc(title) + '</b><button type="button" class="pvx" aria-label="Schließen">' + ic('x') + '</button></div>' +
      '<div class="pvbody">' + html + '</div>' +
      (foot || '<button type="button" class="actbtn pvok">Schließen</button>') + '</div>';
    w.onclick = function (e) { if (e.target === w || e.target.closest('.pvx, .pvok')) closeTile(); };
    tileKey = function (e) { if (e.key === 'Escape') closeTile(); };
    document.addEventListener('keydown', tileKey);
    document.body.appendChild(w); document.body.classList.add('pvopen'); tileEl = w;
    cleanups.push(closeTile);
    $('.pvx', w).focus();
  }
  // ---- v50: Einführung beim ersten Öffnen (wischbare Seiten). v65: ohne Statistik-Frage (Statistik ist Opt-out).
  // Nur neue Nutzer: Willkommen + Name · Home-Bildschirm · So lernst du. „Überspringen“ führt zur letzten Seite mit „Los geht’s“.
  var statAskedNow = false, obEl = null;
  function obStandalone() { return (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true; }
  function obPlatform() { var u = navigator.userAgent || ''; if (/iPhone|iPad|iPod/.test(u) || (/Macintosh/.test(u) && navigator.maxTouchPoints > 1)) return 'ios'; if (/Android/.test(u)) return 'android'; return 'other'; }
  function statAsk() {
    if (statAskedNow || obEl) return;
    var st = DB.settings;
    var fresh = !st.obDone && !st.statsAsked && !DB.log.length && !Object.keys(DB.progress).length && !Object.keys(DB.tests).length;
    if (!fresh) { if (!st.obDone) { st.obDone = Date.now(); save(); } return; }
    statAskedNow = true;
    var pages = [];
    {
      pages.push('<div class="obico">' + ic('cards') + '</div><h2>Willkommen in der Lernkiste</h2>' +
        '<p>Karteikarten und Tests für deine Klausuren, offline auf deinem Handy. Dein Lernstand bleibt auf deinem Gerät.</p>' +
        '<label class="oblab" for="obName">Wie heißt du? <span>(optional)</span></label>' +
        '<input class="txt wide obname" id="obName" type="text" maxlength="20" placeholder="Name" autocomplete="off" autocapitalize="words" spellcheck="false" value="' + esc(st.name || '') + '">' +
        '<p class="note">Aus „Konstis Lernkiste“ wird dann deine Lernkiste. Später änderbar.</p>');
      if (!obStandalone()) {
        var pf = obPlatform(), how = pf === 'ios' ? '<ol class="obsteps"><li>Öffne die Seite in <b>Safari</b>.</li><li>Tippe unten auf <b>Teilen</b> (Quadrat mit Pfeil).</li><li>Wähle <b>Zum Home-Bildschirm</b>.</li></ol>'
          : pf === 'android' ? '<ol class="obsteps"><li>Öffne die Seite in <b>Chrome</b>.</li><li>Tippe oben rechts auf <b>⋮</b>.</li><li>Wähle <b>App installieren</b> oder <b>Zum Startbildschirm hinzufügen</b>.</li></ol>'
          : '<ol class="obsteps"><li><b>iPhone:</b> in Safari auf Teilen, dann „Zum Home-Bildschirm“.</li><li><b>Android:</b> in Chrome auf ⋮, dann „App installieren“.</li></ol>';
        pages.push('<div class="obico">' + ic('arrow') + '</div><h2>Auf den Home-Bildschirm</h2><p>Dann startet die Lernkiste wie eine App und funktioniert auch ohne Internet.</p>' + how +
          (pf === 'ios' ? '<p class="note">Wichtig: Die App auf dem Home-Bildschirm hat einen eigenen Speicher. Lerne am besten nur dort.</p>' : ''));
      }
      pages.push('<div class="obico">' + ic('book') + '</div><h2>So lernst du</h2><ul class="obsteps plain">' +
        '<li><b>Fächer</b> → Kapitel wählen, dann Karteikarten oder Tests.</li>' +
        '<li><b>Karten:</b> antippen zum Umdrehen, dann „Gewusst“ oder „Nochmal“.</li>' +
        '<li><b>Tests:</b> Multiple Choice, Richtig/Falsch, Lückentext und Klausur auf Zeit.</li>' +
        '<li><b>Start</b> zeigt, was heute fällig ist, und deinen Lernstand.</li></ul>' +
        '<p class="note">Die App zählt anonym App-Starts und geöffnete Fächer. Ausschalten unter Einstellungen → Daten und App. <button type="button" class="oblink" id="obPriv">Datenschutz</button></p>');
    }
    var last = pages.length - 1, cur = 0;
    var w = obEl = document.createElement('div'); w.className = 'ob'; w.setAttribute('role', 'dialog'); w.setAttribute('aria-modal', 'true'); w.setAttribute('aria-label', 'Einführung');
    w.innerHTML = '<div class="obtop"><button type="button" class="oblink" id="obSkip">Überspringen</button></div>' +
      '<div class="obvp"><div class="obtrack">' + pages.map(function (h, k) { return '<section class="obpage" aria-hidden="' + (k ? 'true' : 'false') + '">' + h + '</section>'; }).join('') + '</div></div>' +
      '<div class="obfoot">' + (last ? '<div class="obdots">' + pages.map(function () { return '<i></i>'; }).join('') + '</div>' : '') +
      '<div class="obbtns" id="obNav"><button type="button" class="primary obbig" id="obNext">Weiter</button></div>' +
      '<div class="obbtns" id="obAsk"><button type="button" class="primary obbig" id="obGo">Los geht’s</button></div></div>';
    document.body.appendChild(w); document.body.classList.add('pvopen');
    var track = $('.obtrack', w), secs = $$('.obpage', w), dots = $$('.obdots i', w);
    function go(k) {
      cur = Math.max(0, Math.min(last, k)); track.style.transform = 'translateX(' + (-100 * cur) + '%)';
      secs.forEach(function (x, n) { x.setAttribute('aria-hidden', n === cur ? 'false' : 'true'); if (n === cur) x.scrollTop = 0; });
      dots.forEach(function (d, n) { d.classList.toggle('on', n === cur); });
      $('#obSkip', w).style.visibility = cur === last ? 'hidden' : 'visible';
      $('#obNav', w).style.display = cur === last ? 'none' : ''; $('#obAsk', w).style.display = cur === last ? '' : 'none';
      if (document.activeElement && document.activeElement.blur && cur === last) document.activeElement.blur();
    }
    var nm = $('#obName', w);
    if (nm) nm.addEventListener('input', function () { st.name = this.value.slice(0, 20); save(); document.title = appName(); });
    $('#obNext', w).onclick = function () { go(cur + 1); };
    $('#obSkip', w).onclick = function () { go(last); };
    $('#obPriv', w).onclick = function () { openTile('Datenschutz', privacyHTML()); };
    var x0 = null, y0 = 0;
    w.addEventListener('touchstart', function (e) { if (e.target.closest('input')) return; x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
    w.addEventListener('touchend', function (e) {
      if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0; x0 = null;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) go(cur + (dx < 0 ? 1 : -1));
    });
    w.addEventListener('keydown', function (e) { if (e.target.tagName === 'INPUT') { if (e.key === 'Enter') go(cur + 1); return; } if (e.key === 'ArrowRight') go(cur + 1); if (e.key === 'ArrowLeft') go(cur - 1); });
    function finish() {
      st.obDone = Date.now(); save();
      w.remove(); obEl = null; document.body.classList.remove('pvopen');
      if (st.name) { var y = window.scrollY; route(); window.scrollTo(0, y); }
    }
    $('#obGo', w).onclick = finish;
    go(0);
  }
  function privacyHTML() {
    return '<div class="pvkey"><b>Das Wichtigste zuerst</b><p>Ich erhebe keine personenbezogenen Daten. Ich bekomme weder deinen Namen noch deine E-Mail-Adresse, IP-Adresse, eine Geräte-Kennung oder deinen Lernstand (außer du richtest den Sync ein, siehe unten). Ich sehe nur Zahlen wie „heute 12 App-Starts, 5-mal Psycho 2“. Ich kann nicht erkennen, wer die App nutzt, mit welchem Gerät oder von wo, und bei der Statistik auch nicht, ob zwei Einträge von derselben Person stammen.</p></div>' +
      '<p><b>Kurz gesagt:</b> Dein Lernstand bleibt auf deinem Gerät. Die App sendet nur etwas, wenn du Feedback schickst, eine Frage oder eine fehlende Erklärung meldest, die Nutzungsstatistik an ist (Standard, abschaltbar) oder du den Sync einrichtest.</p>' +
      '<h4>Auf deinem Gerät</h4>' +
      '<p>Lernstand, Verlauf, gemerkte Begriffe, eigene Karten und Einstellungen (auch dein Name) liegen nur im Speicher deines Browsers. Sie verlassen das Gerät nicht, außer du speicherst selbst ein Backup. Damit die App offline läuft, speichert der Browser außerdem die App-Dateien.</p>' +
      '<h4>Beim Laden der App</h4>' +
      '<p>Die App liegt bei GitHub Pages (GitHub, USA). Wie jeder Webserver verarbeitet GitHub dabei technisch deine IP-Adresse. Die App lädt keine Werbung, keine Tracker und nichts von fremden Seiten.</p>' +
      '<h4>Feedback, „Frage melden“ und „Erklärung fehlt“ (nur wenn du sendest)</h4>' +
      '<p>Gesendet werden dein Text (beim Melden: Grund, Kommentar, Fach und Nummer der Frage; bei „Erklärung fehlt“: der Begriff, Fach und Nummer der Frage), die App-Version und eine zufällige Kennung gegen Spam. Diese Kennung wird beim ersten Feedback auf dem Gerät gespeichert und sagt nichts über dich. Kein Name. Ziel ist eine private Google-Tabelle über Google Apps Script (Google, Server auch in den USA). Google verarbeitet dabei technisch deine IP-Adresse, in der Tabelle landet sie nicht. Schreib bitte keine persönlichen Daten in den Text.</p>' +
      '<h4>Nutzungsstatistik (abschaltbar)</h4>' +
      '<p><b>Die Statistik ist vollständig anonym.</b> Sie zählt nur, <i>wie oft</i> die App und die Fächer geöffnet werden, nicht <i>wer</i> sie öffnet. Kein Eintrag enthält etwas, das auf dich oder dein Gerät schließen lässt.</p>' +
      '<p>Die Statistik ist von Anfang an eingeschaltet. Du kannst sie jederzeit in den Einstellungen unter „Daten und App“ ausschalten. Solange sie an ist, meldet die App beim Öffnen und beim ersten Öffnen eines Fachs: „App-Start“ oder „Fach geöffnet“, welches Fach und die App-Version. Beim Öffnen kommt dazu nur, ob es der erste Start heute, in dieser Woche oder überhaupt auf diesem Gerät ist (ja/nein). So lässt sich zählen, wie viele Geräte die App nutzen, ohne sie zu unterscheiden. Dafür merkt sich die App auf deinem Gerät das Datum der letzten Meldung; das wird nicht gesendet und beim Ausschalten gelöscht. Den Zeitpunkt notiert die Tabelle. Nicht gesendet werden: Name, E-Mail, IP-Adresse, Geräte-ID, Gerätetyp, Standort, Antworten oder Lernstände. Ziel ist dieselbe private Google-Tabelle wie beim Feedback. Ausschalten geht jederzeit hier in den Einstellungen und wirkt sofort.</p>' +
      '<h4>Geräte synchronisieren (nur wenn eingerichtet)</h4>' +
      '<p>Dann wird dein Lernstand an eine Datenbank bei Supabase gesendet: bewertete Karten, Testergebnisse, Verlauf, gemerkte Begriffe und Einstellungen, aber nicht dein Name und keine eigenen Karten. Es gibt kein Konto und keine E-Mail-Adresse. Gespeichert wird der Stand unter einer verschlüsselten Form deines Codes (Hash), der Code selbst bleibt auf deinen Geräten. Supabase verarbeitet dabei technisch deine IP-Adresse. Den Lernstand könnte ich in der Datenbank technisch sehen, aber keiner Person zuordnen. Mit „Online-Kopie löschen“ entfernst du ihn jederzeit.</p>' +
      '<h4>Wie lange</h4>' +
      '<p>Einträge in der Tabelle werden nach spätestens 12 Monaten automatisch gelöscht.</p>' +
      '<h4>Keine Rückschlüsse auf dich</h4>' +
      '<p>In der Tabelle steht nie, wer etwas gesendet hat. Ich kann Einträge keiner Person und keinem Gerät zuordnen (die Spam-Kennung beim Feedback ist reiner Zufall und verrät nichts über dich) und lege auch keine Profile an. Die einzige Ausnahme wäre, wenn du selbst etwas Persönliches in ein Feedback schreibst – deshalb bitte nicht.</p>';
  }
  function isHidden(sid) { return DB.hidden.indexOf(sid) >= 0; }
  function setHidden(sid, on) {
    var i = DB.hidden.indexOf(sid);
    if (on && i < 0) DB.hidden.push(sid);
    if (!on && i >= 0) DB.hidden.splice(i, 1);
    DB.hiddenTs = Date.now();
    save();
  }

  function highlight(root, terms) {
    terms = (terms || []).filter(function (t) { return t.length > 1; });
    if (!root || !terms.length) return;
    var fz = function (t) { return t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/[aou]/gi, function (c) { return ({ a: '[aäÄA]', o: '[oöÖO]', u: '[uüÜU]' })[c.toLowerCase()]; }); };
    var re = new RegExp('(' + terms.map(fz).join('|') + ')', 'gi'), test = new RegExp(re.source, 'i');
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) { return (!n.nodeValue.trim() || (n.parentElement && n.parentElement.closest('math, input, script'))) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; }
    });
    var list = []; while (w.nextNode()) list.push(w.currentNode);
    list.forEach(function (n) {
      if (!test.test(n.nodeValue)) return;
      var span = document.createElement('span');
      span.innerHTML = esc(n.nodeValue).replace(re, '<mark class="hl">$1</mark>');
      n.replaceWith.apply(n, span.childNodes);
    });
  }

  // ====================================================================== Datenschicht
  function rd(k) { try { return JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) { return null; } }
  function normalizeDB(d) {
    d = d || {};
    d.v = 1; d.recent = d.recent || []; d.progress = d.progress || {}; d.tests = d.tests || {}; d.log = d.log || []; d.hidden = d.hidden || []; d.custom = d.custom || {}; d.custom.folders = d.custom.folders || []; d.terms = d.terms && typeof d.terms === 'object' && !Array.isArray(d.terms) ? d.terms : {}; d.badges = (d.badges && typeof d.badges === 'object' && !Array.isArray(d.badges)) ? d.badges : {};
    d.settings = Object.assign({}, DEFAULTS, d.settings || {});
    // v44: neues Design; der alte Standard „Dunkel“ wird einmalig zu „System“
    if (!d.settings.ui44) { if (d.settings.theme === 'dark') d.settings.theme = 'auto'; d.settings.ui44 = 1; d._mig = 1; }
    // v65: Nutzungsstatistik ist jetzt Opt-out (Standard an, keine Startfrage); einmalig bei allen eingeschaltet. Ausschalten danach bleibt.
    if (!d.settings.st65) { d.settings.stats = 1; d.settings.st65 = 1; d._mig = 1; }
    // Psycho: früheres Test-Kapitel „tp“ (Kap. 1 und 2) ist auf k1/k2 verteilt; offene Fehler übernehmen. Alter Schlüssel bleibt.
    var tp = d.tests['psy/tp'];
    if (tp && !tp.moved) {
      ['k1', 'k2'].forEach(function (k) {
        var c = chap('psy', k); if (!c || !c.items) return;
        var ids = {}; c.items.forEach(function (i) { ids[i.id] = 1; });
        var t = d.tests['psy/' + k] = d.tests['psy/' + k] || { best: {}, wrong: [] }; t.best = t.best || {}; t.wrong = t.wrong || [];
        (tp.wrong || []).forEach(function (w) { if (ids[w] && t.wrong.indexOf(w) < 0) t.wrong.push(w); });
      });
      tp.moved = 1;
    }
    return d;
  }
  function migrate(d) {
    // Alter Lernstand (Position -> feste ID) und alte Test-Daten übernehmen. Alte Schlüssel bleiben unangetastet.
    var old = rd('dif1-k1-status'), ch = chap('diff1', 'k1');
    if (old && ch) Object.keys(old).forEach(function (i) { var c = ch.cards[+i]; if (c) d.progress[c.id] = old[i]; });
    var q = rd('quer-k10'), p = rd('psy2');
    if (q) { d.tests['quer/k10'] = { best: q.best || {}, wrong: q.wrong || [] }; if (q.n !== undefined) d.settings.testN = q.n; if (q.min) d.settings.examMin = q.min; if (q.exn) d.settings.examN = q.exn; }
    if (p) d.tests['psy/g'] = { best: p.best || {}, wrong: p.wrong || [] };
  }
  var DB = (function () {
    var d = rd(KEY), fresh = !d;
    d = normalizeDB(d);
    var moved = d.tests['psy/tp'] && d.tests['psy/tp'].moved === 1 && !d.tests['psy/tp'].saved;
    if (fresh) migrate(d);
    var mig = d._mig; delete d._mig;
    if (fresh || moved || mig) { if (moved) d.tests['psy/tp'].saved = 1; try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) {} }
    return d;
  })();
  function save() {
    if (DB.log.length > 20000) DB.log.splice(0, DB.log.length - 20000);
    try { localStorage.setItem(KEY, JSON.stringify(DB)); saveWarned = false; if (!syncApplying) syncMark(); }
    catch (e) {
      if (saveWarned) return; saveWarned = true;
      setTimeout(function () { toast('Achtung: Speichern hat nicht geklappt (Speicher voll oder gesperrt). Bitte mach ein Backup.', 'Backup', shareFile); }, 50);
    }
  }
  var saveWarned = false;
  // ---- Eigene Karten: Merker für Änderungen seit dem letzten Backup und Erinnerung
  function ownTouch() { if (!DB.settings.ownDirty) DB.settings.ownDirty = Date.now(); }
  // v46: eigene Karten vorerst ausgeblendet (Nutzerwunsch). Daten bleiben gespeichert und im Backup; zum Zurückholen OWN_ON = true.
  var OWN_ON = false;
  function ownCount() { if (!OWN_ON) return 0; return DB.custom.folders.reduce(function (n, f) { return n + f.cards.length; }, 0); }
  function backupMarked() { DB.settings.lastBackup = Date.now(); DB.settings.ownDirty = 0; save(); }
  function ownFirstTip() {
    if (DB.settings.ownTip) return; DB.settings.ownTip = Date.now(); save();
    setTimeout(function () { toast('Tipp: Eigene Karten liegen nur auf diesem Gerät. Sichere sie ab und zu mit einem Backup.', 'Backup', shareFile); }, 400);
  }
  var nagDone = false;
  function backupNag() {
    if (nagDone) return; nagDone = true;
    if (ownCount() && !DB.settings.lastBackup && !DB.settings.ownDirty) { DB.settings.ownDirty = Date.now(); save(); }
    var d = DB.settings.ownDirty, today = dayKey(Date.now());
    if (!d || !ownCount() || Date.now() - d < 7 * 864e5 || DB.settings.nagDay === today) return;
    setTimeout(function () {
      if (tileEl || document.body.classList.contains('immersive')) { nagDone = false; return; }
      DB.settings.nagDay = today; save();
      var n = Math.floor((Date.now() - d) / 864e5);
      toast('Deine eigenen Karten sind seit ' + n + ' Tagen nicht gesichert.', 'Backup', shareFile);
    }, 2500);
  }
  function backupHint() {
    if (!ownCount()) return '';
    var lb = DB.settings.lastBackup, d = DB.settings.ownDirty || !lb;
    var txt = d ? (lb ? 'Seit dem letzten Backup (' + new Date(lb).toLocaleDateString('de-DE') + ') hast du Karten geändert.' : 'Deine eigenen Karten sind noch nicht gesichert.')
      : 'Gesichert im Backup vom ' + new Date(lb).toLocaleDateString('de-DE') + '.';
    return '<div class="bkhint' + (d ? ' warn' : '') + '"><div><b>' + (d ? 'Backup empfohlen' : 'Alles gesichert') + '</b><small>' + txt + ' Eigene Karten liegen nur auf diesem Gerät und gehen verloren, wenn die Browserdaten gelöscht werden.</small></div>' +
      (d ? '<button type="button" class="actbtn" id="bkNow">Backup</button>' : '') + '</div>';
  }
  function bindBackupHint() { var b = $('#bkNow'); if (b) b.onclick = shareFile; }
  function ptouch(id) { (DB.ptime = DB.ptime || {})[id] = Date.now(); }
  function logAns(fach, id, score, pts) { var e = [Date.now(), fach, id, Math.round(score * 100) / 100]; if (typeof pts === 'number') e.push(pts); DB.log.push(e); }
  function tests(sid, cid) { var k = sid + '/' + cid, t = DB.tests[k] = DB.tests[k] || {}; t.best = t.best || {}; t.wrong = t.wrong || []; return t; }

  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  function applyPrefs() {
    var t = DB.settings.theme; if (t === 'auto') t = (mq && mq.matches) ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', t);
    document.documentElement.style.fontSize = (15 * DB.settings.font) + 'px';
    document.title = appName();
    var m = $('meta[name="theme-color"]'); if (m) m.setAttribute('content', t === 'dark' ? '#14191B' : '#DFDDD4');
  }
  if (mq && mq.addEventListener) mq.addEventListener('change', applyPrefs);

  // ====================================================================== Gerüst, Navigation
  var view = $('#view'), cleanups = [];
  function onLeave(fn) { cleanups.push(fn); }
  function setImm(b) { document.body.classList.toggle('immersive', !!b); updUI(); }
  function parseHash() {
    var h = location.hash.replace(/^#/, '') || '/', qi = h.indexOf('?'), q = {};
    var path = qi >= 0 ? h.slice(0, qi) : h;
    if (qi >= 0) h.slice(qi + 1).split('&').forEach(function (p) { var kv = p.split('='); if (kv[0]) q[kv[0]] = decodeURIComponent((kv[1] || '').replace(/\+/g, ' ')); });
    return { parts: path.split('/').filter(Boolean), q: q };
  }
  var TABS = [
    { id: 'start', href: '#/', label: 'Start', svg: '<path d="M4 11l8-6 8 6v8a1 1 0 0 1-1 1h-4v-5H9v5H5a1 1 0 0 1-1-1z"/>' },
    { id: 'faecher', href: '#/faecher', label: 'Fächer', svg: '<rect x="3" y="6" width="14" height="14" rx="3"/><path d="M7 3h11a3 3 0 0 1 3 3v11"/>' },
    { id: 'verlauf', href: '#/verlauf', label: 'Statistik', svg: '<path d="M5 20V11M12 20V5M19 20v-6"/>' },
    { id: 'set', href: '#/einstellungen', label: 'Einstellungen', svg: '<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>' }
  ];
  $('#tabbar').innerHTML = '<nav aria-label="Hauptmenü">' + TABS.map(function (t) {
    return '<a class="tab" data-t="' + t.id + '" href="' + t.href + '" aria-label="' + t.label + '"><svg viewBox="0 0 24 24" aria-hidden="true">' + t.svg + '</svg><span class="t">' + t.label + '</span></a>';
  }).join('') + '</nav>';
  function setTab(id) { $$('.tab').forEach(function (a) { var on = a.dataset.t === id; a.classList.toggle('on', on); if (on) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); }); }

  function route() {
    cleanups.splice(0).forEach(function (f) { try { f(); } catch (e) {} });
    setImm(false); view.className = ''; view.removeAttribute('style');
    var r = parseHash(), p = r.parts, tab = 'start';
    if (!p.length) homeView();
    else if (p[0] === 'suche') { tab = ''; searchView(r.q.q || ''); }
    else if (p[0] === 'faecher') { tab = 'faecher'; faecherView(); }
    else if (p[0] === 'verlauf') { tab = 'verlauf'; verlaufView(); }
    else if (p[0] === 'neu' && OWN_ON) { tab = 'faecher'; neuView(p[1], p[2]); }
    else if (p[0] === 'neu') { location.replace('#/faecher'); return; }
    else if (p[0] === 'einstellungen') { tab = 'set'; settingsView(); }
    else if (p[0] === 'mix') { tab = 'faecher'; mixView(p[1]); }
    else if (p[0] === 'faellig') dueView(p[1]);
    else if (p[0] === 'begriffe') kwView(r.q.s || '');
    else if (p[0] === 'f' && p[1] && p[2] === 'u' && p[3]) { tab = 'faecher'; fachView(p[1], p[3]); }
    else if (p[0] === 'f' && p[1] && !p[2]) { tab = 'faecher'; fachView(p[1]); }
    else if (p[0] === 'f' && p[1] && p[2]) { tab = 'faecher'; chapterView(p[1], p[2], r.q); }
    else homeView();
    if (p[0] === 'f' && p[1]) statFach(p[1]);
    statAsk(); backupNag(); badgeCheck();
    setTab(tab);
    if (!(p[0] === 'f' && p[2] && r.q.c)) window.scrollTo(0, 0);
  }

  // ====================================================================== Motivation (v36): Lernstand, Heute fällig, Tagesziel, Lerntage-Kette, Countdown
  function dayNum(x) {
    if (typeof x === 'string') { var p = x.split('-'); return Math.round(Date.UTC(+p[0], +p[1] - 1, +p[2]) / 864e5); }
    var d = new Date(x); return Math.round(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 864e5);
  }
  var LS_CACHE = null, LS_KEY = '';
  // Lernstand je Karte/Frage aus dem Verlauf: n, letzte 5 Werte, Serie richtiger Tage seit dem letzten Fehler
  function learnState() {
    var last = DB.log[DB.log.length - 1], key = DB.log.length + '|' + (last ? last[0] : 0);
    if (LS_CACHE && LS_KEY === key) return LS_CACHE;
    var m = {};
    DB.log.forEach(function (e) {
      var r = m[e[2]] = m[e[2]] || { n: 0, last5: [], streak: 0, okDay: -1, day: 0, s: 0 }, day = dayNum(e[0]), ok = e[3] === 1;
      r.n++; r.s = e[3]; r.day = day; r.last5.push(e[3]); if (r.last5.length > 5) r.last5.shift();
      r.pts = typeof e[4] === 'number' ? e[4] : undefined;
      if (!ok) { r.streak = 0; r.okDay = -1; } else if (day !== r.okDay) { r.streak++; r.okDay = day; }
    });
    LS_CACHE = m; LS_KEY = key; return m;
  }
  var DUE_GAP = [1, 1, 3, 7, 14];
  function levelOf(r) { return !r ? 'neu' : r.streak >= 3 ? 'gemeistert' : r.s === 1 ? 'sicher' : 'gesehen'; }
  function isDue(r, today) { return !!r && today - r.day >= DUE_GAP[Math.min(r.streak, 4)]; }
  function dueLists() {
    var ls = learnState(), today = dayNum(Date.now()), cards = [], items = [], seen = {};
    C.subjects.forEach(function (sx) {
      if (isHidden(sx.id)) return;
      sx.chapters.forEach(function (ch) {
        if (ch.placeholder) return;
        (ch.cards || []).forEach(function (c) { if (!seen[c.id] && isDue(ls[c.id], today)) { seen[c.id] = 1; cards.push(Object.assign({}, c, { _s: sx.id })); } });
        (ch.items || []).forEach(function (it) { if (!seen[it.id] && isDue(ls[it.id], today)) { seen[it.id] = 1; items.push(Object.assign({}, it, { _s: sx.id })); } });
      });
    });
    return { cards: cards, items: items };
  }
  function dueView(part) {
    var d = dueLists(), S = { id: 'due', mix: true, due: true, name: 'Start', href: '#/', chapters: [] };
    view.className = 's-mix';
    if (part === 'karten' && d.cards.length) return cardsView(S, { id: 'due', kind: 'cards', title: 'Heute fällig: Karten', sub: d.cards.length + (d.cards.length === 1 ? ' Karte' : ' Karten') + ' zum Wiederholen', cards: shuffle(d.cards) }, {});
    if (part === 'tests' && d.items.length) return testsView(S, { id: 'due', kind: 'tests', title: 'Heute fällig: Fragen', sub: d.items.length + (d.items.length === 1 ? ' Frage' : ' Fragen') + ' zum Wiederholen', items: d.items }, {});
    location.replace('#/');
  }
  function todayCount() { var t = dayNum(Date.now()), n = 0; for (var i = DB.log.length - 1; i >= 0; i--) { if (dayNum(DB.log[i][0]) !== t) break; n++; } return n; }
  // Lerntage-Kette: ein Pausetag pro Kalenderwoche reißt die Kette nicht; heute darf noch fehlen
  function chainOf() {
    var days = {}; DB.log.forEach(function (e) { days[dayNum(e[0])] = 1; });
    var t = dayNum(Date.now()), n = 0, used = {};
    for (var i = 0; i < 1000; i++) {
      var d = t - i;
      if (days[d]) { n++; continue; }
      if (i === 0) continue;
      var wk = weekKey(d * 864e5 + 432e5);
      if (!used[wk]) { used[wk] = 1; continue; }
      break;
    }
    return n;
  }
  function examDays() {
    var t = dayNum(Date.now());
    return C.subjects.filter(function (s) { return s.exam && !isHidden(s.id); }).map(function (s) { return { s: s, d: dayNum(s.exam) - t }; })
      .filter(function (x) { return x.d >= 0; }).sort(function (a, b) { return a.d - b.d; });
  }
  function todayHTML() {
    var st = DB.settings, rows = [];
    if (st.mGoal || st.mChain) {
      var n = todayCount(), g = st.mGoal, ring = '';
      if (g) {
        var f = Math.min(1, n / g), L = 2 * Math.PI * 20;
        ring = '<svg class="ring' + (n >= g ? ' done' : '') + '" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="20" class="rb"/>' +
          (f > 0 ? '<circle cx="24" cy="24" r="20" class="rf" stroke-dasharray="' + (L * f).toFixed(1) + ' ' + L.toFixed(1) + '"/>' : '') + '</svg>';
      }
      var head = g ? (n >= g ? 'Tagesziel erreicht · ' + n : 'Heute ' + n + ' von ' + g) : 'Heute ' + n + (n === 1 ? ' Antwort' : ' Antworten');
      rows.push('<div class="tdrow" id="tdGoal">' + ring + '<div class="tdtxt"><b>' + head + '</b>' + (st.mChain ? '<small>Lerntage in Folge: ' + chainOf() + '</small>' : '') + '</div></div>');
    }
    return rows.length ? '<div class="group today">' + rows.join('') + '</div>' : '';
  }

  // ====================================================================== Motivation (v37): Mosaik je Kapitel, Abzeichen
  var CROWN = '<svg class="crown" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8l4.5 4L12 5l4.5 7L21 8l-2 11H5z"/></svg>';
  function heat(r) { if (!r) return 'hn'; var a = r.last5.reduce(function (x, y) { return x + y; }, 0) / r.last5.length; return a < 0.2 ? 'h0' : a < 0.45 ? 'h1' : a < 0.65 ? 'h2' : a < 0.85 ? 'h3' : 'h4'; }
  function mosaicHTML(items) {
    var ls = learnState(), nm = 0;
    var tiles = items.map(function (it, i) { var r = ls[it.id], m = levelOf(r) === 'gemeistert'; if (m) nm++; return '<button type="button" class="mt ' + heat(r) + '" data-mi="' + i + '" aria-label="Frage ' + (i + 1) + '">' + (m ? CROWN : '') + '</button>'; }).join('');
    var seen = items.filter(function (it) { return ls[it.id]; }).length;
    return '<div class="mosaic"><div class="mhead"><b>Fragen-Übersicht</b><span>' + seen + ' / ' + items.length + ' geübt' + (nm ? ' · ' + nm + ' gemeistert' : '') + '</span></div>' +
      '<div class="mgrid">' + tiles + '</div><div id="minfo" class="minfo">Farbe nach den letzten 5 Antworten, grau = neu, Krone = gemeistert. Antippen für Details.</div></div>';
  }
  function wireMosaic(items, practice) {
    $$('.mgrid .mt').forEach(function (b) {
      b.onclick = function () {
        var i = +b.dataset.mi, it = items[i], r = learnState()[it.id];
        $$('.mgrid .mt.on').forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on');
        var avg = r ? Math.round(r.last5.reduce(function (x, y) { return x + y; }, 0) / r.last5.length * 100) : 0;
        var last = !r ? '' : r.pts !== undefined ? 'zuletzt ' + r.pts + '/4' : r.s === 1 ? 'zuletzt richtig' : r.s > 0 ? 'zuletzt teilweise' : 'zuletzt falsch';
        $('#minfo').innerHTML = '<span><b>Frage ' + (i + 1) + '</b> · ' + TYPES[it.type] + '<br>' + (r ? r.n + '× beantwortet · Ø ' + avg + ' % · ' + last + ' · ' + levelOf(r) : 'noch nicht geübt') + '</span><button type="button" class="actbtn" id="mGo">Üben ›</button>';
        $('#mGo').onclick = function () { practice(it.id); };
      };
    });
  }
  var BADGES = [
    ['first', 'Erste Antwort', 'Die erste Karte oder Frage beantwortet'],
    ['goal', 'Tagesziel erreicht', 'An einem Tag das Tagesziel geschafft'],
    ['chain7', '7 Lerntage', 'Lerntage-Kette von 7 Tagen'],
    ['chain30', '30 Lerntage', 'Lerntage-Kette von 30 Tagen'],
    ['n100', '100 Antworten', 'Insgesamt 100 Karten und Fragen'],
    ['n1000', '1000 Antworten', 'Insgesamt 1000 Karten und Fragen'],
    ['allsubj', 'Alle Fächer geübt', 'In jedem Fach mindestens einmal geübt'],
    ['chapseen', 'Kapitel durch', 'Alle Karten und Fragen eines Kapitels einmal geübt'],
    ['chapmaster', 'Kapitel gemeistert', 'Alle Fragen eines Kapitels gemeistert'],
    ['exam1', 'Note 1,x', 'Zeit-Simulation mit Note 1,7 oder besser']
  ];
  function badgeCheck() {
    if (!DB.settings.mBadges) return;
    var got = DB.badges, ls = learnState(), L = DB.log.length, fresh = [];
    function has(id, cond) { if (got[id] || !cond()) return; got[id] = Date.now(); fresh.push(id); }
    has('first', function () { return L > 0; });
    has('goal', function () { var g = DB.settings.mGoal || 30, c = {}; return DB.log.some(function (e) { var d = dayNum(e[0]); c[d] = (c[d] || 0) + 1; return c[d] >= g; }); });
    var ch = chainOf();
    has('chain7', function () { return ch >= 7; }); has('chain30', function () { return ch >= 30; });
    has('n100', function () { return L >= 100; }); has('n1000', function () { return L >= 1000; });
    has('allsubj', function () { var s = {}; DB.log.forEach(function (e) { s[e[1]] = 1; }); return C.subjects.every(function (x) { return s[x.id]; }); });
    function chaps(fn) { return C.subjects.some(function (x) { return x.chapters.some(function (c) { return !c.placeholder && fn(c); }); }); }
    has('chapseen', function () { return chaps(function (c) { var a = (c.cards || []).concat(c.items || []); return a.length && a.every(function (z) { return ls[z.id]; }); }); });
    has('chapmaster', function () { return chaps(function (c) { return c.items && c.items.length && c.items.every(function (z) { return levelOf(ls[z.id]) === 'gemeistert'; }); }); });
    has('exam1', function () { return Object.keys(DB.tests).some(function (k) { var b = DB.tests[k].best; return b && b.exam >= 85; }); });
    if (fresh.length) {
      save();
      if (!document.body.classList.contains('immersive')) toast('Abzeichen: ' + BADGES.filter(function (b) { return b[0] === fresh[0]; })[0][1] + (fresh.length > 1 ? ' (+' + (fresh.length - 1) + ')' : ''));
    }
  }
  function badgesHTML() {
    if (!DB.settings.mBadges) return '';
    var got = DB.badges, n = BADGES.filter(function (b) { return got[b[0]]; }).length;
    return '<div class="group badges"><div class="bhead"><b>Abzeichen</b><span>' + n + ' von ' + BADGES.length + '</span></div><div class="bgrid">' + BADGES.map(function (b) {
      var t = got[b[0]];
      return '<div class="bdg' + (t ? ' got' : '') + '"><b>' + b[1] + '</b><small>' + (t ? new Date(t).toLocaleDateString('de-DE') : b[2]) + '</small></div>';
    }).join('') + '</div></div>';
  }

  // ====================================================================== Start / Fach
  function subjStats(s) {
    var allPlaceholder = s.chapters.every(function (ch) { return ch.placeholder; }), r = progOf(s.chapters, true);
    return { txt: allPlaceholder ? 'Inhalte folgen' : progTxt(r), pct: r.pct, placeholder: allPlaceholder };
  }
  var LAST_KEY = 'lernkiste-last', MON = ['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'];
  function getLast() { var l = rd(LAST_KEY); return l && l.h && l.t ? l : null; }
  function setLast(o) { o.ts = Date.now(); try { localStorage.setItem(LAST_KEY, JSON.stringify(o)); } catch (e) {} }
  // Lernstand (v52): Fragen sind der Maßstab (zuletzt ganz richtig). Karten zählen nur, wo es keine Fragen gibt.
  // Ohne Gerüst; mit agg auch ohne „nicht klausurrelevant“. Geteilte IDs zählen einmal.
  function progOf(chs, agg) {
    var ls = learnState(), seen = {}, r = { n: 0, k: 0, nc: 0, kc: 0, na: 0, ka: 0, pct: 0 };
    chs.forEach(function (ch) {
      if (ch.placeholder || (agg && /nicht klausurrelevant/i.test(ch.note || ''))) return;
      (ch.cards || []).forEach(function (c) { if (seen[c.id]) return; seen[c.id] = 1; r.nc++; if (DB.progress[c.id] === 'known') r.kc++; });
      (ch.items || []).forEach(function (it) { if (seen[it.id]) return; seen[it.id] = 1; r.n++; var x = ls[it.id]; if (x && x.s === 1) r.k++; });
      (ch.tasks || []).forEach(function (t) { if (seen[t.id]) return; seen[t.id] = 1; r.na++; var x = ls[t.id]; if (x && x.s === 1) r.ka++; }); // v64: Aufgaben zählen wie Fragen
    });
    if (agg && !r.n && !r.nc && !r.na) return progOf(chs, false);
    var nq = r.n + r.na, kq = r.k + r.ka;
    r.pct = nq ? kq / nq * 100 : r.nc ? r.kc / r.nc * 100 : 0;
    return r;
  }
  function progTxt(r) {
    return [r.n ? (r.k ? r.k + '/' + r.n + ' Fragen' : r.n + ' Fragen') : '', r.na ? (r.ka ? r.ka + '/' + r.na + ' Aufgaben' : r.na + ' Aufgaben') : '', r.nc ? (r.kc ? r.kc + '/' + r.nc + ' Karten' : r.nc + ' Karten') : ''].filter(Boolean).join(' · ');
  }
  function subjPct(s) { return Math.round(progOf(s.chapters, true).pct); }
  // ====================================================================== Favoriten, Farben, Startseite anpassen (v62)
  var TINTS = [['', 'Standard'], ['sage', 'Salbei'], ['peach', 'Pfirsich'], ['honey', 'Honig'], ['sky', 'Himmel'], ['lilac', 'Flieder']];
  function stTouch() { DB.settings._ts = Date.now(); save(); }
  function favList() { return Array.isArray(DB.settings.favs) ? DB.settings.favs : []; }
  function isFav(k) { return favList().indexOf(k) >= 0; }
  function setFav(k, on) { var l = favList().filter(function (x) { return x !== k; }); if (on) l.push(k); DB.settings.favs = l; stTouch(); }
  function homeHidden(sid) { return (DB.settings.homeHide || []).indexOf(sid) >= 0; }
  function setHomeHidden(sid, on) { var l = (DB.settings.homeHide || []).filter(function (x) { return x !== sid; }); if (on) l.push(sid); DB.settings.homeHide = l; stTouch(); }
  function tintMap() { return DB.settings.tint && typeof DB.settings.tint === 'object' ? DB.settings.tint : {}; }
  function setTint(k, v) { var m = Object.assign({}, tintMap()); if (v) m[k] = v; else delete m[k]; DB.settings.tint = m; stTouch(); }
  // Schlüssel: „sid“ (Fach), „sid/u/gid“ (Unterbereich), „sid/cid“ (Kapitel); Farbe erbt Fach → Unterbereich → Kapitel
  function tintOf(sid, gid, cid) { var m = tintMap(); return (cid && m[sid + '/' + cid]) || (gid && m[sid + '/u/' + gid]) || m[sid] || ''; }
  function tintCls(t) { return t ? ' tinted t-' + t : ''; }
  function favInfo(k) {
    var p = k.split('/'), s = subj(p[0]); if (!s) return null;
    if (p[1] === 'u') { var g = (s.groups || []).filter(function (x) { return x.id === p[2]; })[0]; if (!g) return null;
      var chs = s.chapters.filter(function (c) { return c.group === g.id; });
      return { s: s, short: g.name, title: g.name, href: '#/f/' + s.id + (chs.length === 1 ? '/' + chs[0].id : '/u/' + g.id) }; }
    var ch = chap(p[0], p[1]); if (!ch) return null;
    var t0 = ch.title.split(' · ')[0];
    return { s: s, short: t0.replace(/^Kapitel /, 'Kap. '), title: ch.title, href: '#/f/' + s.id + '/' + ch.id };
  }
  var STAR = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"/></svg>';
  function favChips(sid) {
    var l = favList().map(function (k) { var f = favInfo(k); return f && f.s.id === sid ? '<a class="favchip" href="' + f.href + '" data-lp="fav" data-k="' + esc(k) + '">' + STAR + esc(f.short) + '</a>' : ''; }).join('');
    return l ? '<div class="favchips">' + l + '</div>' : '';
  }
  // Langes Drücken (Touch) bzw. Rechtsklick öffnet das Menü; danach wird der Klick geschluckt
  function wireLongPress(root, open) {
    $$('[data-lp]', root).forEach(function (el) {
      var tm = 0, x0 = 0, y0 = 0, fired = false;
      el.addEventListener('touchstart', function (e) { if (e.target.closest('[data-lp]') !== el) return; var t = e.touches[0]; x0 = t.clientX; y0 = t.clientY; fired = false; clearTimeout(tm);
        tm = setTimeout(function () { fired = true; el.classList.remove('lpdown'); if (navigator.vibrate) try { navigator.vibrate(12); } catch (x) {} open(el); }, 480); el.classList.add('lpdown'); }, { passive: true });
      el.addEventListener('touchmove', function (e) { var t = e.touches[0]; if (Math.abs(t.clientX - x0) > 10 || Math.abs(t.clientY - y0) > 10) { clearTimeout(tm); el.classList.remove('lpdown'); } }, { passive: true });
      ['touchend', 'touchcancel'].forEach(function (n) { el.addEventListener(n, function () { clearTimeout(tm); el.classList.remove('lpdown'); }); });
      el.addEventListener('contextmenu', function (e) { if (e.target.closest('[data-lp]') !== el) return; e.preventDefault(); clearTimeout(tm); if (!fired) { fired = true; open(el); } });
      el.addEventListener('click', function (e) { if (fired) { e.preventDefault(); e.stopPropagation(); fired = false; } }, true);
    });
  }
  function tintPicker(k, inherit) {
    var cur = tintMap()[k] || '', x = TINTS.filter(function (t) { return t[0] === cur; })[0] || TINTS[0];
    return '<div class="tintrow" role="radiogroup" aria-label="Farbe">' + TINTS.map(function (t) {
      var lab = !t[0] && inherit ? 'Wie das Fach' : t[1];
      return '<button type="button" class="sw2 ' + (t[0] ? 't-' + t[0] : 'none') + (cur === t[0] ? ' on' : '') + '" data-t="' + t[0] + '" role="radio" aria-checked="' + (cur === t[0]) + '" aria-label="' + lab + '"></button>';
    }).join('') + '</div><p class="tintlab">' + (!cur && inherit ? 'Wie das Fach' : x[1]) + '</p>';
  }
  // Menü zu einem Fach (Startseite / Fächer) oder einem Unterbereich/Kapitel
  function lpMenu(kind, k, rerender) {
    var p = k.split('/'), s = subj(p[0]), h = '', name, inherit = kind !== 'subj';
    if (kind === 'fav') { var f = favInfo(k); setFav(k, false); rerender(); toast('„' + (f ? f.short : '') + '“ aus den Favoriten genommen', 'Rückgängig', function () { setFav(k, true); rerender(); }); return; }
    if (kind === 'subj') name = s.name; else { var fi = favInfo(k); name = fi ? fi.title : k; }
    if (kind !== 'subj') h += '<button type="button" class="lprow" id="lpFav">' + STAR + (isFav(k) ? 'Aus den Favoriten nehmen' : 'Favorisieren') + '</button>';
    if (kind === 'subj') h += '<button type="button" class="lprow" id="lpHide">' + ic('eyeoff') + 'Ausblenden</button>';
    h += '<div class="lprow nob">' + ic('palette') + 'Farbe' + (inherit ? '' : '<small>gilt auch für die Unterbereiche</small>') + '</div><div id="tintBox">' + tintPicker(k, inherit) + '</div>';
    openTile(name, h);
    function wire() {
      $$('#tintBox .sw2').forEach(function (b) { b.onclick = function () { setTint(k, b.dataset.t); $('#tintBox').innerHTML = tintPicker(k, inherit); wire(); rerender(); }; });
    }
    wire();
    var fb = $('#lpFav'); if (fb) fb.onclick = function () { var on = !isFav(k); setFav(k, on); closeTile(); rerender(); toast(on ? 'Als Favorit auf der Startseite' : 'Aus den Favoriten genommen'); };
    var hb = $('#lpHide'); if (hb) hb.onclick = function () {
      $('.pvbody').innerHTML = '<p class="lpq">Wo soll „' + esc(s.name) + '“ ausgeblendet werden?</p><button type="button" class="lprow" id="lpH1">Nur auf der Startseite</button><button type="button" class="lprow" id="lpH2">Auch bei den Fächern</button>';
      $('#lpH1').onclick = function () { setHomeHidden(s.id, true); closeTile(); rerender(); toast('„' + s.name + '“ nicht mehr auf der Startseite', 'Rückgängig', function () { setHomeHidden(s.id, false); rerender(); }); };
      $('#lpH2').onclick = function () { setHidden(s.id, true); closeTile(); rerender(); toast('„' + s.name + '“ ausgeblendet', 'Rückgängig', function () { setHidden(s.id, false); rerender(); }); };
    };
  }
  function homeView() {
    var st = DB.settings, now = new Date(), hr = now.getHours(), nm = (st.name || '').trim();
    var greet = (hr >= 5 && hr < 11 ? 'Guten Morgen' : hr >= 11 && hr < 18 ? 'Guten Tag' : 'Guten Abend') + (nm ? ', ' + nm : '') + '!';
    var d = st.mDue ? dueLists() : { cards: [], items: [] }, nc = d.cards.length, ni = d.items.length, last = getLast();
    var line = nc && ni ? nc + (nc === 1 ? ' Karte' : ' Karten') + ' und ' + ni + (ni === 1 ? ' Frage warten' : ' Fragen warten') + ' auf dich.'
      : nc ? nc + (nc === 1 ? ' Karte wartet' : ' Karten warten') + ' auf dich.' : ni ? ni + (ni === 1 ? ' Frage wartet' : ' Fragen warten') + ' auf dich.'
      : st.mDue ? 'Heute ist nichts fällig. ' + (last ? 'Mach weiter, wo du aufgehört hast.' : 'Such dir ein Fach aus.') : last ? 'Mach weiter, wo du aufgehört hast.' : 'Such dir ein Fach aus und leg los.';
    var goHref = nc ? '#/faellig/karten' : ni ? '#/faellig/tests' : last ? last.h : '#/faecher';
    var h = '<div class="hhead"><div class="who">' + (nm ? '<div class="avatar" aria-hidden="true">' + esc(nm.charAt(0).toUpperCase()) + '</div>' : '') +
      '<div><div class="hdate">' + now.toLocaleDateString('de-DE', { weekday: 'long', day: 'numeric', month: 'long' }) + '</div><h1 class="htitle">Übersicht</h1></div></div>' +
      '<a class="rbtn" href="#/suche" aria-label="Suche">' + ic('search') + '</a></div>';
    h += '<div class="hello"><div class="stk a"></div><div class="stk b"></div><div class="stk c"><i></i><i></i><i></i></div>' +
      '<div class="txt"><b>' + esc(greet) + '</b><span>' + line + '</span></div>' +
      '<a class="go1" id="goLearn" href="' + goHref + '"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5l12 7-12 7z"/></svg>Lernen starten</a></div>';
    var exAll = examDays(), ex = exAll.filter(function (x) { return !homeHidden(x.s.id); }), shown = {};
    if (ex.length) {
      h += '<div class="sechead"><b>Deine Klausuren</b><a href="#/faecher">Alle Fächer</a></div><div class="exams">' + ex.map(function (x) {
        var dt = new Date(x.s.exam + 'T12:00:00'), p = subjPct(x.s); shown[x.s.id] = 1;
        var when = x.d === 0 ? 'heute' : x.d === 1 ? 'morgen' : 'in ' + x.d + ' Tagen';
        return '<div class="exwrap' + tintCls(tintOf(x.s.id)) + '" data-lp="subj" data-k="' + x.s.id + '"><a class="exrow" href="#/f/' + x.s.id + '"><div class="exdate"><b>' + dt.getDate() + '</b><span>' + MON[dt.getMonth()] + '</span></div>' +
          '<div class="exmid"><div class="l1"><b>' + esc(x.s.name) + '</b><span>' + p + ' %</span></div>' +
          '<div class="bar" role="img" aria-label="Lernstand ' + p + ' Prozent"><div style="width:' + p + '%"></div></div>' +
          (st.mCount ? '<small>' + when + (x.s.examTime ? ' · ' + esc(x.s.examTime) : '') + '</small>' : '') + '</div>' + CHEV + '</a>' + favChips(x.s.id) + '</div>';
      }).join('') + '</div>';
    } else h += '<div class="sechead"><b>Deine Fächer</b><a href="#/faecher">Alle Fächer</a></div>';
    // Favoriten von Fächern ohne eigene Zeile (von der Startseite genommen oder ohne Klausur)
    var rest = C.subjects.filter(function (x) { return !shown[x.id] && !isHidden(x.id) && favChips(x.id); });
    if (rest.length) h += '<div class="exams">' + rest.map(function (x) {
      return '<div class="exwrap favonly' + tintCls(tintOf(x.id)) + '"><a class="favhead" href="#/f/' + x.id + '">' + esc(x.name) + CHEV + '</a>' + favChips(x.id) + '</div>';
    }).join('') + '</div>';
    var hh = exAll.filter(function (x) { return homeHidden(x.s.id); });
    if (hh.length) h += '<button type="button" class="hiddenlink" id="hidLink">nicht auf der Startseite (' + hh.length + ')</button><div class="hiddenlist" id="hidList" hidden>' +
      hh.map(function (x) { return '<div class="hidrow"><i class="sw" style="background:var(--c-' + x.s.id + ')"></i><span>' + esc(x.s.name) + '</span><button type="button" data-show="' + x.s.id + '">Einblenden</button></div>'; }).join('') + '</div>';
    if (last) {
      h += '<a class="next" href="' + esc(last.h) + '"><div class="nt"><span class="k">Als Nächstes</span><b>' + esc(last.t) + '</b><small>' + esc(last.sub) + '</small></div>' +
        '<span class="arr">' + ic('arrow') + '</span></a>';
    }
    var kwn = kwList().length; if (kwn) h += kwRowHTML('#/begriffe', kwn, '', 1);
    h += todayHTML();
    view.innerHTML = h;
    wireLongPress(view, function (el) { lpMenu(el.dataset.lp, el.dataset.k, homeView); });
    var hl = $('#hidLink'); if (hl) hl.onclick = function () { var l = $('#hidList'); l.hidden = !l.hidden; };
    $$('[data-show]').forEach(function (b) { b.onclick = function () { setHomeHidden(b.dataset.show, false); homeView(); toast('„' + subj(b.dataset.show).name + '“ wieder auf der Startseite'); }; });
  }
  function faecherView() {
    var vis = C.subjects.filter(function (s) { return !isHidden(s.id); }), hid = C.subjects.filter(function (s) { return isHidden(s.id); });
    var h = '<h1>Fächer</h1><p class="sub">' + esc(appName()) + '</p>' +
      '<a class="fakesearch" href="#/suche"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>Begriff oder Satz suchen …</a><div class="grid fach">';
    vis.forEach(function (s) {
      var st = subjStats(s);
      h += '<div class="tilewrap" data-sid="' + s.id + '"><div class="hidehint">Ausblenden</div><a class="tile s-' + s.id + tintCls(tintOf(s.id)) + '" data-lp="subj" data-k="' + s.id + '" href="#/f/' + s.id + '">' + (st.placeholder ? '<span class="badge">Gerüst</span>' : '') +
        '<div><h2 class="name">' + esc(s.name) + '</h2><p class="desc">' + esc(s.desc) + '</p></div>' +
        '<div class="foot"><span>' + esc(st.txt) + '</span><div class="bar"><div style="width:' + st.pct + '%"></div></div><span class="go">Öffnen</span></div></a>' +
        '<button type="button" class="tilemenu" aria-label="Mehr zu ' + esc(s.name) + '">' + ic('more') + '</button></div>';
    });
    h += '</div>';
    if (OWN_ON && (ownCount() || DB.custom.folders.length)) h += '<a class="mixtile" href="#/neu"><span><b>Eigene Karten</b><small>' + ownCount() + (ownCount() === 1 ? ' Karte' : ' Karten') + ' in ' + DB.custom.folders.length + (DB.custom.folders.length === 1 ? ' Ordner' : ' Ordnern') + '</small></span><span class="go">Öffnen</span></a>';
    if (eligible().length >= 2) h += '<a class="mixtile" href="#/mix"><span><b>Gemischt üben</b><small>Fächer kombinieren, Karten und Tests gemischt</small></span><span class="go">Öffnen</span></a>';
    if (!vis.length) h += '<p class="note" style="text-align:center;padding:26px 10px">Alle Themen sind ausgeblendet.</p>';
    if (hid.length) {
      h += '<button type="button" class="hiddenlink" id="hidLink">versteckte Themen (' + hid.length + ')</button><div class="hiddenlist" id="hidList" hidden>' +
        hid.map(function (s) { return '<div class="hidrow"><i class="sw" style="background:var(--c-' + s.id + ')"></i><span>' + esc(s.name) + '</span><button type="button" data-show="' + s.id + '">Einblenden</button></div>'; }).join('') + '</div>';
    }
    view.innerHTML = h;
    wireHome(!!hid.length);
    wireLongPress(view, function (el) { lpMenu(el.dataset.lp, el.dataset.k, faecherView); });
  }
  function hideSubject(sid) {
    setHidden(sid, true); faecherView();
    toast('„' + subj(sid).name + '“ ausgeblendet', 'Rückgängig', function () { setHidden(sid, false); if (parseHash().parts[0] === 'faecher') faecherView(); });
  }
  function wireHome(hasHidden) {
    var openMenu = null;
    function closeMenu() { if (openMenu) { openMenu.remove(); openMenu = null; } }
    $$('.tilewrap').forEach(function (w) {
      var tile = $('.tile', w), sid = w.dataset.sid, x0 = 0, y0 = 0, dx = 0, mode = '', moved = false;
      $('.tilemenu', w).onclick = function (ev) {
        ev.preventDefault(); ev.stopPropagation(); var had = openMenu && openMenu.parentNode === w; closeMenu(); if (had) return;
        var m = document.createElement('div'); m.className = 'tilepop';
        m.innerHTML = '<button type="button">Ausblenden</button>'; w.appendChild(m); openMenu = m;
        $('button', m).onclick = function () { closeMenu(); hideSubject(sid); };
      };
      tile.addEventListener('touchstart', function (e) { var t = e.touches[0]; x0 = t.clientX; y0 = t.clientY; dx = 0; mode = ''; moved = false; tile.style.transition = 'none'; }, { passive: true });
      tile.addEventListener('touchmove', function (e) {
        var t = e.touches[0], mx = t.clientX - x0, my = t.clientY - y0;
        if (!mode) { if (Math.abs(mx) > 10 && Math.abs(mx) > Math.abs(my) * 1.4) mode = 'h'; else if (Math.abs(my) > 10) mode = 'v'; }
        if (mode !== 'h') return;
        moved = true; dx = Math.min(0, mx); tile.style.transform = 'translateX(' + dx + 'px)'; w.classList.toggle('armed', dx < -90);
        if (e.cancelable) e.preventDefault();
      }, { passive: false });
      function end() {
        tile.style.transition = ''; var go = mode === 'h' && dx < -90;
        if (go) { tile.style.transform = 'translateX(-110%)'; setTimeout(function () { hideSubject(sid); }, 160); }
        else { tile.style.transform = ''; w.classList.remove('armed'); }
        if (moved) setTimeout(function () { moved = false; }, 50);
      }
      tile.addEventListener('touchend', end); tile.addEventListener('touchcancel', end);
      tile.addEventListener('click', function (e) { if (moved) { e.preventDefault(); e.stopPropagation(); } }, true);
    });
    var onDoc = function (e) { if (openMenu && !e.target.closest('.tilepop, .tilemenu')) closeMenu(); };
    document.addEventListener('click', onDoc, true); cleanups.push(function () { document.removeEventListener('click', onDoc, true); });
    if (hasHidden) {
      $('#hidLink').onclick = function () { var l = $('#hidList'); l.hidden = !l.hidden; };
      $$('[data-show]').forEach(function (b) { b.onclick = function () { var sid = b.dataset.show; setHidden(sid, false); faecherView(); toast('„' + subj(sid).name + '“ wieder eingeblendet'); }; });
    }
  }
  // ====================================================================== Gemischt
  function mixShuffle(list, even) {
    if (!even) return shuffle(list);
    var g = {}, keys = [], out = [], more = true;
    list.forEach(function (x) { var k = x._s || ''; if (!g[k]) { g[k] = []; keys.push(k); } g[k].push(x); });
    keys = shuffle(keys); keys.forEach(function (k) { g[k] = shuffle(g[k]); });
    while (more) { more = false; keys.forEach(function (k) { if (g[k].length) { out.push(g[k].shift()); more = true; } }); }
    return out;
  }
  function subjContent(sx) {
    var cards = 0, items = 0;
    sx.chapters.forEach(function (ch) { if (ch.placeholder) return; if (ch.cards) cards += ch.cards.length; if (ch.items) items += ch.items.length; });
    return { cards: cards, items: items };
  }
  function eligible() { return C.subjects.filter(function (x) { var c = subjContent(x); return !isHidden(x.id) && (c.cards || c.items); }); }
  function mixSelected() { var el = eligible(), sel = DB.settings.mixSubs; return el.filter(function (x) { return !sel || sel.indexOf(x.id) >= 0; }); }
  function mixView(part) {
    var sel = mixSelected(), even = DB.settings.mixMode === 'even', cards = [], items = [], seen = {};
    sel.forEach(function (sx) {
      sx.chapters.forEach(function (ch) {
        if (ch.placeholder) return;
        if (ch.cards) ch.cards.forEach(function (c) { if (seen[c.id]) return; seen[c.id] = 1; cards.push(Object.assign({}, c, { _s: sx.id })); });
        if (ch.items) ch.items.forEach(function (it) { if (seen[it.id]) return; seen[it.id] = 1; items.push(Object.assign({}, it, { _s: sx.id })); });
      });
    });
    if (part === 'karten' || part === 'tests') {
      if ((part === 'karten' && !cards.length) || (part === 'tests' && !items.length)) { location.hash = '#/mix'; return; }
      var S = { id: 'mix', mix: true, name: 'Gemischt', href: '#/mix', desc: '', chapters: [] };
      view.className = 's-mix';
      var sub = sel.map(function (x) { return x.name; }).join(' · ');
      if (part === 'karten') cardsView(S, { id: 'mix', kind: 'cards', title: 'Gemischt: Karteikarten', sub: sub, cards: mixShuffle(cards, even) }, {});
      else testsView(S, { id: 'mix', kind: 'tests', title: 'Gemischt: Tests', sub: sub, items: items }, {});
      return;
    }
    var el = eligible();
    var h = '<div class="nav">' + backLink('#/faecher', 'Fächer') + '</div><h1>Gemischt üben</h1><p class="sub">Wähle die Fächer, die gemischt werden sollen.</p><div class="group" style="padding:4px 16px">' +
      el.map(function (sx) {
        var c = subjContent(sx), on = sel.indexOf(sx) >= 0;
        return '<label class="mixrow"><input type="checkbox" data-s="' + sx.id + '"' + (on ? ' checked' : '') + '><i class="sw" style="background:var(--c-' + sx.id + ')"></i><span class="nm">' + esc(sx.name) + '</span><span class="ct">' +
          [c.cards ? c.cards + ' Karten' : '', c.items ? c.items + ' Fragen' : ''].filter(Boolean).join(' · ') + '</span></label>';
      }).join('') + '</div>' +
      '<div class="chips"><span class="lbl">Mischung</span><button class="chip' + (even ? ' on' : '') + '" data-mm="even">Gleichmäßig</button><button class="chip' + (!even ? ' on' : '') + '" data-mm="rand">Nach Menge</button></div>' +
      '<p class="note" style="margin:0 0 14px">' + (even ? 'Jedes Fach kommt abwechselnd dran, auch wenn eines viel mehr Material hat.' : 'Alles wird zufällig gemischt, große Fächer kommen öfter dran.') + '</p>' +
      '<div class="row"><button class="primary" id="mxC"' + (cards.length ? '' : ' disabled') + '>Karteikarten (' + cards.length + ')</button><button class="primary" id="mxT"' + (items.length ? '' : ' disabled') + '>Tests (' + items.length + ')</button></div>' +
      (sel.length ? '' : '<p class="note" style="text-align:center;margin-top:12px">Wähle mindestens ein Fach.</p>');
    view.innerHTML = h;
    $$('.mixrow input').forEach(function (b) {
      b.onchange = function () {
        var ids = $$('.mixrow input').filter(function (x) { return x.checked; }).map(function (x) { return x.dataset.s; });
        DB.settings.mixSubs = ids.length === el.length ? null : ids; save(); mixView();
      };
    });
    $$('[data-mm]').forEach(function (b) { b.onclick = function () { DB.settings.mixMode = b.dataset.mm === 'even' ? 'even' : 'rand'; save(); mixView(); }; });
    $('#mxC').onclick = function () { location.hash = '#/mix/karten'; };
    $('#mxT').onclick = function () { location.hash = '#/mix/tests'; };
  }
  function chapTile(s, ch) {
    var r = progOf([ch], false), pct = r.pct, parts = [progTxt(r)], desc;
    if (ch.kind === 'schema') desc = 'Fahrplan mit Mustersätzen, Aufgaben zum Aufdecken';
    else if (ch.cards && ch.items) desc = 'Karteikarten, Multiple Choice, Richtig/Falsch, Lückentext, Zeit-Simulation';
    else if (ch.cards) desc = 'Karteikarten';
    else { var b2 = tests(s.id, ch.id).best.exam; if (b2 !== undefined) parts.push('Klausur ' + b2 + ' %'); desc = 'Tests: Multiple Choice, Lückentext, Richtig/Falsch, Zeit-Simulation'; }
    var ck = s.id + '/' + ch.id;
    return '<a class="tile s-' + s.id + tintCls(tintOf(s.id, ch.group, ch.id)) + '"' + (ch.placeholder ? '' : ' data-lp="sec" data-k="' + ck + '"') + ' href="#/f/' + s.id + '/' + ch.id + '">' + (ch.placeholder ? '<span class="badge">Gerüst</span>' : '') +
      '<div><h2 class="name">' + (isFav(ck) ? '<span class="favst" aria-label="Favorit">' + STAR + '</span>' : '') + esc(ch.title) + '</h2><p class="desc">' + esc(desc) + '</p>' + (ch.note ? '<p class="cnote">' + esc(ch.note) + '</p>' : '') + '</div>' +
      '<div class="foot"><span>' + esc(parts.join(' · ')) + '</span><div class="bar"><div style="width:' + pct + '%"></div></div><span class="go">Öffnen</span></div></a>';
  }
  function fachView(sid, gid) {
    var s = subj(sid); if (!s) return homeView();
    var grp = gid ? (s.groups || []).filter(function (g) { return g.id === gid; })[0] : null;
    if (gid && !grp) { location.hash = '#/f/' + sid; return; }
    var only = grp && s.chapters.filter(function (c) { return c.group === gid; });
    if (only && only.length === 1) { location.replace('#/f/' + sid + '/' + only[0].id); return; }
    var h = '<div class="nav">' + backLink(grp ? '#/f/' + sid : '#/faecher', grp ? s.name : 'Fächer') + '</div><h1>' + esc(grp ? grp.name : s.name) + '</h1><p class="sub">' + esc(grp ? s.name : s.desc) + '</p><div class="grid">';
    if (sid === 'psy' && !grp) h = h.replace(/<div class="grid">$/, '<p class="disclaimer">Alle Inhalte dieser App wurden nicht von der Dozentin bzw. dem Dozenten überprüft und sind ohne jede Gewähr zu verwenden. Es können sich Fehler eingeschlichen haben, und die Klausur kann andere Inhalte abfragen.</p><div class="grid">');
    if (s.groups && !grp) {
      s.groups.forEach(function (g) {
        var chs = s.chapters.filter(function (c) { return c.group === g.id; }), gp = progOf(chs, true);
        var txt = !chs.length ? 'Inhalte folgen' : progTxt(gp);
        var one = chs.length === 1 ? chs[0].id : null, gk = one ? sid + '/' + one : sid + '/u/' + g.id; // ein Kapitel = Kachel steht für das Kapitel
        h += '<a class="tile s-' + sid + tintCls(tintOf(sid, g.id, one)) + '"' + (chs.length ? ' data-lp="sec" data-k="' + gk + '"' : '') + ' href="#/f/' + sid + (chs.length === 1 ? '/' + chs[0].id : '/u/' + g.id) + '">' + (chs.length ? '' : '<span class="badge">Folgt</span>') +
          '<div><h2 class="name">' + (isFav(gk) ? '<span class="favst" aria-label="Favorit">' + STAR + '</span>' : '') + esc(g.name) + '</h2><p class="desc">' + esc(g.desc) + '</p></div>' +
          '<div class="foot"><span>' + esc(txt) + '</span><div class="bar"><div style="width:' + gp.pct + '%"></div></div><span class="go">Öffnen</span></div></a>';
      });
    } else {
      var list = grp ? s.chapters.filter(function (c) { return c.group === gid; }) : s.chapters;
      list.forEach(function (ch) { h += chapTile(s, ch); });
      if (!list.length) h += '<div class="note" style="text-align:center;padding:18px 6px">Inhalte folgen.</div>';
    }
    var kwn = !grp ? kwList(sid).length : 0;
    view.innerHTML = h + '</div>' + (kwn ? kwRowHTML('#/begriffe?s=' + sid, kwn) : '');
    wireLongPress(view, function (el) { lpMenu(el.dataset.lp, el.dataset.k, function () { fachView(sid, gid); }); });
  }
  function chapterView(sid, cid, q) {
    if (sid === 'psy' && cid === 'tp') { location.replace('#/f/psy/u/pers'); return; }
    if (cid === 'allg' && subj(sid)) { // v48: „Allgemein“ ist jetzt eine Gruppe mit Unterbereichen – alte Links weiterleiten
      var t = q.c || q.q, hit = t && subj(sid).chapters.filter(function (c) { return c.group === 'allg' && (c.cards || []).concat(c.items || []).some(function (x) { return x.id === t; }); })[0];
      location.replace('#/f/' + sid + '/' + (hit ? hit.id + (q.c ? '?c=' : '?q=') + encodeURIComponent(t) : 'u/allg')); return;
    }
    var s = subj(sid), ch = chap(sid, cid); if (!s || !ch) return homeView();
    view.className = 's-' + sid;
    var grp = ch.group && (s.groups || []).filter(function (g) { return g.id === ch.group; })[0];
    if (grp && s.chapters.filter(function (c) { return c.group === grp.id; }).length > 1) s = Object.assign({}, s, { href: '#/f/' + sid + '/u/' + grp.id, name: grp.name });
    if (ch.kind === 'schema') { schemaView(s, ch, q); return; }
    if (ch.cards && ch.items) {
      if (q.c || q.mode === 'cards' || q.read) cardsView(Object.assign({}, s, { href: '#/f/' + sid + '/' + cid, name: ch.title.split(' · ')[0] }), Object.assign({}, ch, { kind: 'cards' }), q);
      else testsView(s, ch, q);
    } else if (ch.kind === 'cards') cardsView(s, ch, q); else testsView(s, ch, q);
  }

  // ====================================================================== Rechenschemata (v64): Überblick (aufklappbar) + Aufgaben zum Aufdecken
  var RS_MARK = [['Nicht gewusst', 0], ['Teilweise', 0.5], ['Gewusst', 1]];
  function schemaView(s, ch, q) {
    var T = tests(s.id, ch.id), STEP = {}; ch.steps.forEach(function (x) { STEP[x.n] = x; });
    var TASK = {}; ch.tasks.forEach(function (t) { TASK[t.id] = t; });
    var back = backHref('#/f/' + s.id), backName = fromSearch() ? 'Suche' : s.name;
    function rsData() { return T.rs && typeof T.rs === 'object' ? T.rs : (T.rs = {}); }
    function stepLabel(n) { return 'Schritt ' + n + ' · ' + STEP[n].t; }
    // Schwache Schritte: letzte Bewertung je Aufgabe, „nicht gewusst“ zählt 1, „teilweise“ ½
    function weak() {
      var w = {}, d = rsData();
      Object.keys(d).forEach(function (id) { var r = d[id]; if (!TASK[id] || !r || !r.m) return; TASK[id].steps.forEach(function (p, i) { var v = r.m[i]; if (v === 0) w[p.n] = (w[p.n] || 0) + 1; else if (v === 0.5) w[p.n] = (w[p.n] || 0) + 0.5; }); });
      return Object.keys(w).map(Number).filter(function (n) { return w[n] > 0; }).sort(function (a, b) { return w[b] - w[a] || a - b; }).map(function (n) { return { n: n, v: w[n] }; });
    }
    function overview(tab) {
      setImm(false);
      var h = '<div class="nav">' + backLink(back, backName) + '</div><h1 style="font-size:1.55rem">' + esc(ch.title) + '</h1><p class="sub">' + esc(ch.sub) + '</p>';
      h += '<div class="chips rstabs"><button class="chip' + (tab === 'u' ? ' on' : '') + '" data-tab="u">Überblick</button><button class="chip' + (tab === 'a' ? ' on' : '') + '" data-tab="a">Aufgaben (' + ch.tasks.length + ')</button></div>';
      if (tab === 'u') {
        var ex = TASK[ch.example];
        h += '<div class="group rsgroup">' + ch.steps.map(function (x) {
          var bsp = ex && ex.steps.filter(function (p) { return p.n === x.n; })[0];
          return '<details class="faq rsstep" data-n="' + x.n + '"' + (String(q.st) === String(x.n) ? ' open' : '') + '><summary><span class="rsn">' + x.n + '</span><span class="rsh"><b>' + esc(x.t) + '</b><small>' + x.goal + '</small></span><svg class="chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></summary><div class="fa">' +
            '<div class="rs-satz"><div class="rs-lbl">Mustersatz · auswendig</div>' + x.satz + '</div>' +
            '<div class="tip warn rs-fall"><div class="rs-lbl">Achtung</div>' + x.fall + '</div>' +
            (bsp ? '<details class="rs-bsp"><summary>Beispiel (' + esc(ex.src.split(' (')[0]) + ')</summary><div class="serif rs-body">' + bsp.h + '</div></details>' : '') + '</div></details>';
        }).join('') + '</div>';
        h += '<div class="group rsgroup">' + ch.extra.map(function (x) {
          return '<details class="faq rsx"><summary><b>' + esc(x.t) + '</b><svg class="chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></summary><div class="fa">' + x.h + '</div></details>';
        }).join('') + '</div>';
        h += '<div class="row"><button class="primary" id="rsGo">Aufgaben üben</button></div>';
      } else {
        var mode = DB.settings.rsMode === 'k' ? 'k' : 's', ls = learnState(), d = rsData(), wk = weak();
        h += '<div class="chips"><span class="lbl">Ablauf</span><button class="chip' + (mode === 's' ? ' on' : '') + '" data-rm="s">Mit Schritten</button><button class="chip' + (mode === 'k' ? ' on' : '') + '" data-rm="k">Wie in der Klausur</button></div>';
        h += '<p class="note" style="margin:0 0 14px">' + (mode === 's' ? 'Du siehst vorher, welcher Schritt dran ist. Rechne auf Papier, dann aufdecken.' : 'Nur die Aufgabe steht da. Rechne auf Papier und decke die Lösung Schritt für Schritt auf.') + '</p>';
        if (wk.length) h += '<div class="banner"><b>Zuletzt schwach:</b> ' + wk.slice(0, 3).map(function (w) { return 'Schritt ' + w.n + ' (' + esc(STEP[w.n].t) + ')'; }).join(', ') + '</div>';
        h += '<div class="modes">' + ch.tasks.map(function (t) {
          var r = d[t.id], x = ls[t.id], st = !x ? 'Noch nicht geübt' : x.s === 1 ? 'Zuletzt alles gewusst' : 'Zuletzt ' + Math.round(x.s * 100) + ' %';
          var dots = r && r.m ? '<span class="rsdots">' + r.m.map(function (v) { return '<i class="v' + String(v).replace('.', '') + '"></i>'; }).join('') + '</span>' : '';
          return '<button class="mode rstask" data-t="' + t.id + '"><span><span class="t">' + esc(t.src.split(' (')[0]) + '</span><br><span class="d">' + esc(t.src.indexOf(' (') > 0 ? t.src.slice(t.src.indexOf(' (') + 2, -1) : '') + '</span></span><span class="r">' + esc(st) + dots + '</span></button>';
        }).join('') + '</div>';
      }
      view.innerHTML = h;
      $$('[data-tab]').forEach(function (b) { b.onclick = function () { overview(b.dataset.tab); }; });
      $$('[data-rm]').forEach(function (b) { b.onclick = function () { DB.settings.rsMode = b.dataset.rm; save(); overview('a'); }; });
      $$('.rstask').forEach(function (b) { b.onclick = function () { runTask(TASK[b.dataset.t]); }; });
      var g = $('#rsGo'); if (g) g.onclick = function () { overview('a'); window.scrollTo(0, 0); };
      if (q.st) { var o = $('.rsstep[open]'); if (o) setTimeout(function () { o.scrollIntoView({ block: 'start' }); }, 30); q.st = null; }
    }
    function runTask(t) {
      var mode = DB.settings.rsMode === 'k' ? 'k' : 's', marks = [], pos = 0, shown = false, N = t.steps.length;
      setImm(true); window.scrollTo(0, 0);
      function draw() {
        var h = lhead('rsX', null, t.src.split(' (')[0], mode === 'k' ? 'Wie in der Klausur' : 'Mit Schritten', Math.min(pos + 1, N) + '/' + N, pos / N);
        h += '<div class="card rsq"><div class="meta"><span class="side">Aufgabe</span><span>' + esc(t.src.indexOf(' (') > 0 ? t.src.slice(t.src.indexOf(' (') + 2, -1) : '') + '</span></div><div class="serif rs-body">' + t.q + '</div></div>';
        t.steps.forEach(function (p, i) {
          if (i > pos || (i === pos && !shown)) return;
          var m = marks[i];
          h += '<div class="rsdone' + (i === pos ? ' cur' : '') + '"><div class="rs-lbl"><span>' + esc(stepLabel(p.n)) + '</span>' + (m !== undefined ? '<span class="rsm v' + String(m).replace('.', '') + '">' + RS_MARK.filter(function (x) { return x[1] === m; })[0][0] + '</span>' : '') + '</div><div class="serif rs-body">' + p.h + '</div></div>';
        });
        if (pos < N && !shown) {
          var p = t.steps[pos];
          h += '<div class="rsnext">' + (mode === 's' ? '<div class="rs-lbl"><span>' + esc(stepLabel(p.n)) + '</span></div><div class="rsgoal">' + STEP[p.n].goal + '</div><p class="note">Schreib den Schritt auf Papier, mit Satz.</p>' : '<p class="note">Rechne weiter auf Papier und decke dann den nächsten Schritt auf.</p>') +
            '<div class="row"><button class="primary" id="rsShow">' + (mode === 's' ? 'Aufdecken' : 'Nächsten Schritt aufdecken') + '</button></div></div>';
        } else if (pos < N) {
          h += '<div class="rsrate">' + RS_MARK.map(function (x, i) { return '<button class="btn' + (i === 2 ? ' known' : '') + '" data-v="' + x[1] + '">' + x[0] + '</button>'; }).join('') + '</div>';
        } else {
          var sc = marks.reduce(function (a, b) { return a + b; }, 0) / N, all = marks.every(function (v) { return v === 1; });
          var bad = t.steps.map(function (p, i) { return marks[i] < 1 ? 'Schritt ' + p.n : ''; }).filter(Boolean).filter(function (x, i, a) { return a.indexOf(x) === i; });
          h += '<div class="card rsend"><h2>' + (all ? 'Alles gewusst' : Math.round(sc * 100) + ' % gewusst') + '</h2><p>' + (all ? 'Die Aufgabe zählt für deinen Lernstand als richtig.' : 'Nochmal ansehen: ' + esc(bad.join(', ')) + '. Im Überblick stehen Mustersatz und Fallen dazu.') + '</p></div>' +
            '<div class="row"><button class="ghost" id="rsAgain">Nochmal</button><button class="primary" id="rsBack">Zur Übersicht</button></div>';
        }
        view.innerHTML = h;
        $('#rsX').onclick = function () { overview('a'); };
        var b = $('#rsShow'); if (b) b.onclick = function () { shown = true; draw(); var c = $('.rsdone.cur'); if (c) c.scrollIntoView({ block: 'start', behavior: 'smooth' }); };
        $$('.rsrate button').forEach(function (x) { x.onclick = function () {
          marks[pos] = parseFloat(x.dataset.v); pos++; shown = false;
          if (pos === N) finish();
          draw(); var n = $('.rsnext, .rsend'); if (n) n.scrollIntoView({ block: 'center', behavior: 'smooth' });
        }; });
        var a = $('#rsAgain'); if (a) a.onclick = function () { runTask(t); };
        var bk = $('#rsBack'); if (bk) bk.onclick = function () { overview('a'); window.scrollTo(0, 0); };
      }
      function finish() {
        var sc = marks.reduce(function (a, b) { return a + b; }, 0) / N;
        logAns(s.id, t.id, sc); rsData()[t.id] = { m: marks.slice(), ts: Date.now() }; T.ts = Date.now(); save();
      }
      draw();
    }
    view.className = 's-' + s.id;
    if (q.t && TASK[q.t]) runTask(TASK[q.t]); else overview('u');
  }

  // ====================================================================== Lernmodus-Kopf (v44): ✕ links, Titel mitte, Zähler rechts, Leiste darunter
  function lhead(closeId, href, title, sub, cnt, frac) {
    return '<div class="lhead">' + (href ? '<a class="rbtn" id="' + closeId + '" href="' + href + '" aria-label="Schließen">' + ic('x') + '</a>' : '<button type="button" class="rbtn" id="' + closeId + '" aria-label="Schließen">' + ic('x') + '</button>') +
      '<div class="lt"><b>' + esc(title) + '</b>' + (sub ? '<span>' + esc(sub) + '</span>' : '') + '</div>' +
      '<div class="cnt" aria-label="' + esc(cnt.replace('/', ' von ')) + '">' + esc(cnt) + '</div></div>' +
      '<div class="ltrack" aria-hidden="true"><div style="width:' + Math.round(Math.max(0, Math.min(1, frac)) * 100) + '%"></div></div>';
  }

  // ====================================================================== Karteikarten
  function cardsView(s, ch, q) {
    var cards = ch.cards, byId = {}; cards.forEach(function (c) { byId[c.id] = c; });
    var st = DB.settings, noRed = s.own || !cards.some(function (c) { return c.red; }), filter = (q.c || noRed || s.due) ? 'all' : st.cardFilter;
    var order = cards.map(function (c) { return c.id; }); if (st.cardOrder === 'shuffle' && !s.mix) order = shuffle(order);
    var deck = [], pos = 0, flipped = false, confirmReset = false, reading = q.read === '1', rpos = 0;
    var terms = (q.hl || '').split(/\s+/).filter(function (t) { return t.length > 1; });

    function build(keep) {
      var cur = deck[pos];
      deck = order.filter(function (id) { var c = byId[id]; return filter === 'red' ? c.red : filter === 'again' ? DB.progress[id] === 'again' : true; });
      pos = keep && deck.indexOf(cur) >= 0 ? deck.indexOf(cur) : 0; flipped = false;
    }
    function readDraw() {
      var list = order.map(function (id) { return byId[id]; }), total = list.length;
      rpos = Math.max(0, Math.min(rpos, total - 1));
      setImm(true);
      var h = lhead('rEnd', '', ch.title, 'Lesen · ohne Wertung', total ? (rpos + 1) + '/' + total : '0', total ? (rpos + 1) / total : 0);
      if (!total) h += '<div class="empty">Keine Karten vorhanden.</div>';
      else {
        var c = list[rpos];
        h +=
          '<div class="card">' + (c.red ? '<span class="reddot"></span>' : '') + '<div class="meta"><span>' + esc(c.src) + '</span><span class="side">Frage</span></div>' +
          '<div class="face">' + c.q + '</div></div>' +
          '<div class="card" style="margin-top:10px"><div class="meta"><span></span><span class="side" style="color:var(--green)">Antwort</span></div><div class="face">' + c.a + '</div></div>' +
          '<div class="row"><button class="ghost" id="rPrev"' + (rpos === 0 ? ' disabled' : '') + '>' + ic('left') + 'Zurück</button><button class="ghost" id="rNext"' + (rpos === total - 1 ? ' disabled' : '') + '>Weiter' + ic('right') + '</button></div>';
      }
      h += '<div class="tools"><button id="rShuf">Mischen</button><button id="rOrd">Skript-Reihenfolge</button></div><p class="foot-note kbd">Pfeiltasten zum Blättern</p>';
      view.innerHTML = h;
      $('#rEnd').onclick = function () { reading = false; draw(); window.scrollTo(0, 0); };
      var rp = $('#rPrev'), rn = $('#rNext');
      if (rp) rp.onclick = function () { rpos--; readDraw(); window.scrollTo(0, 0); };
      if (rn) rn.onclick = function () { rpos++; readDraw(); window.scrollTo(0, 0); };
      $('#rShuf').onclick = function () { order = shuffle(cards.map(function (c) { return c.id; })); rpos = 0; readDraw(); };
      $('#rOrd').onclick = function () { order = cards.map(function (c) { return c.id; }); rpos = 0; readDraw(); };
    }
    function draw() {
      if (reading) return readDraw();
      var total = deck.length, nRed = cards.filter(function (c) { return c.red; }).length;
      var nAgain = cards.filter(function (c) { return DB.progress[c.id] === 'again'; }).length;
      var known = deck.filter(function (id) { return DB.progress[id] === 'known'; }).length;
      setImm(true);
      var h = lhead('bClose', backHref(s.href || '#/f/' + s.id), ch.title, s.mix ? (ch.sub || '') : (subj(s.id) ? subj(s.id).name : s.name), total ? (pos + 1) + '/' + total : '0', total ? known / total : 0) +
        (ch.note ? '<p class="cnote hub">' + esc(ch.note) + '</p>' : '') +
        '<div class="seg" id="seg">' + (noRed ? '' : '<button data-f="red" class="' + (filter === 'red' ? 'on' : '') + '"><span class="dot"></span>Rot markiert (' + nRed + ')</button>') +
        '<button data-f="all" class="' + (filter === 'all' ? 'on' : '') + '">Alle (' + cards.length + ')</button>' +
        '<button data-f="again" class="' + (filter === 'again' ? 'on' : '') + '">Nochmal (' + nAgain + ')</button></div>' +
        '<div class="status"><span>' + (total ? known + ' von ' + total + ' gewusst' : '') + '</span><button type="button" class="linkbtn" id="bRead" style="display:inline-flex;align-items:center;gap:6px;min-height:36px">' + ic('book') + 'Lesen</button></div>';
      if (!total) {
        h += '<div class="empty">' + (filter === 'again' ? 'Keine Karten im Nochmal-Stapel. Stark!' : 'Keine Karten in dieser Auswahl.') + '</div>';
      } else {
        var c = byId[deck[pos]], mark = DB.progress[c.id] === 'known' ? ' · gewusst' : DB.progress[c.id] === 'again' ? ' · nochmal' : '';
        h += '<div class="card flip ' + (flipped ? 'back' : 'front') + '" id="card" role="button" tabindex="0" aria-label="' + (flipped ? 'Zur Frage umdrehen' : 'Karte umdrehen') + '">' + (c.red ? '<span class="reddot" title="Rot markiert"></span>' : '') +
          '<div class="meta"><span>' + esc(c.src) + mark + '</span><span class="side">' + (flipped ? 'Antwort' : 'Frage') + '</span></div>' +
          '<div class="face">' + (flipped ? c.a : c.q) + '</div>' + (flipped ? '' : '<div class="hint">Antippen zum Umdrehen</div>') + '</div>';
        if (flipped) h += '<div class="rate"><button class="btn again" id="bAgain">' + ic('x') + 'Nochmal</button><button class="btn known" id="bKnown">' + ic('check') + 'Gewusst</button></div>';
        h += '<div class="small-nav"><button type="button" id="bPrev"' + (pos === 0 ? ' disabled' : '') + '>' + ic('left') + 'Zurück</button><button type="button" id="bNext"' + (pos === total - 1 ? ' disabled' : '') + '>Weiter' + ic('right') + '</button></div>';
        if (!s.mix && !s.due && !s.own) {
          var hp = parseHash().parts.join('/');
          setLast({ h: '#/' + hp + '?mode=cards&at=' + encodeURIComponent(c.id), t: ch.title, sub: (subj(s.id) ? subj(s.id).name + ' · ' : '') + 'bei Karte ' + (pos + 1) + ' von ' + total + ' aufgehört' });
        }
      }
      h += '<div class="tools"><button id="bShuf">Mischen</button><button id="bOrd">Skript-Reihenfolge</button><button id="bReset">' + (confirmReset ? 'Wirklich zurücksetzen?' : 'Fortschritt zurücksetzen') + '</button></div>' +
        '<p class="foot-note kbd">Karte antippen oder Leertaste zum Umdrehen · Pfeiltasten zum Blättern</p>';
      view.innerHTML = h;
      if (terms.length && total) highlight($('.face', view), terms);
      $$('#seg button').forEach(function (b) { b.onclick = function () { filter = b.dataset.f; build(false); draw(); }; });
      $('#bRead').onclick = function () { rpos = 0; reading = true; draw(); window.scrollTo(0, 0); };
      var card = $('#card'); if (card) card.onclick = flip;
      var bp = $('#bPrev'); if (bp) bp.onclick = function () { go(-1); };
      var bn = $('#bNext'); if (bn) bn.onclick = function () { go(1); };
      var ba = $('#bAgain'); if (ba) ba.onclick = function () { rate('again'); };
      var bk = $('#bKnown'); if (bk) bk.onclick = function () { rate('known'); };
      $('#bShuf').onclick = function () { order = shuffle(cards.map(function (c) { return c.id; })); build(false); draw(); };
      $('#bOrd').onclick = function () { order = cards.map(function (c) { return c.id; }); build(false); draw(); };
      $('#bReset').onclick = function () {
        if (!confirmReset) { confirmReset = true; draw(); return; }
        cards.forEach(function (c) { delete DB.progress[c.id]; ptouch(c.id); }); save(); confirmReset = false; build(false); draw();
      };
    }
    function flip() { if (!deck.length) return; flipped = !flipped; draw(); }
    function go(d) { var np = pos + d; if (np < 0 || np >= deck.length) return; pos = np; flipped = false; draw(); window.scrollTo(0, 0); }
    function rate(val) {
      var id = deck[pos]; DB.progress[id] = val; ptouch(id); logAns(byId[id]._s || s.id, id, val === 'known' ? 1 : 0); save();
      if (filter === 'again' && val === 'known') { deck.splice(pos, 1); if (pos >= deck.length) pos = Math.max(0, deck.length - 1); flipped = false; draw(); return; }
      if (pos < deck.length - 1) pos++;
      flipped = false; draw(); window.scrollTo(0, 0);
    }
    function onKey(e) {
      if (/INPUT|TEXTAREA/.test((e.target || {}).tagName || '')) return;
      if (reading) { if (e.key === 'ArrowRight' && rpos < order.length - 1) { rpos++; readDraw(); } else if (e.key === 'ArrowLeft' && rpos > 0) { rpos--; readDraw(); } return; }
      if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); flip(); }
      else if (e.key === 'ArrowRight') go(1); else if (e.key === 'ArrowLeft') go(-1);
    }
    document.addEventListener('keydown', onKey); onLeave(function () { document.removeEventListener('keydown', onKey); });

    build(false);
    if (reading) { readDraw(); return; }
    if (q.at && byId[q.at] && !q.c) {
      if (deck.indexOf(q.at) < 0) { filter = 'all'; build(false); }
      pos = Math.max(0, deck.indexOf(q.at));
    }
    if (q.c && byId[q.c]) {
      pos = Math.max(0, deck.indexOf(q.c)); flipped = true;
      if (terms.length) {
        var c0 = byId[q.c], inT = function (html) { var t = nrm(textOf(html)); return terms.some(function (x) { return t.indexOf(nrm(x)) >= 0; }); };
        if (inT(c0.q) && !inT(c0.a)) flipped = false;
      }
    }
    draw();
  }

  // ====================================================================== Tests
  var TYPES = { mc: 'Multiple Choice', tf: 'Richtig / Falsch', gap: 'Lückentext' };
  var MODES = [
    { id: 'mc', name: 'Multiple Choice', desc: 'Vier Antworten, eine stimmt', ico: 'mc' },
    { id: 'tf', name: 'Richtig / Falsch', desc: 'Schnelle Aussagen mit Erklärung', ico: 'tf' },
    { id: 'gap', name: 'Lückentext', desc: 'Begriffe selbst eintippen', ico: 'gap' },
    { id: 'exam', name: 'Zeit-Simulation', desc: 'Mini-Klausur mit Timer und Note', ico: 'clock' }
  ];
  function gapParts(it) {
    var parts = [], re = /\{\{(.*?)\}\}/g, last = 0, m;
    while ((m = re.exec(it.text))) { parts.push({ t: it.text.slice(last, m.index) }); parts.push({ g: m[1].split('|') }); last = re.lastIndex; }
    parts.push({ t: it.text.slice(last) }); return parts;
  }
  function gapHTML(it, values) {
    var k = 0;
    return gapParts(it).map(function (p) {
      if (p.t !== undefined) return p.t;
      var w = Math.max.apply(null, p.g.map(function (a) { return a.length; })), v = values && values[k] ? values[k] : '';
      return '<input class="gap" data-k="' + (k++) + '" value="' + esc(v) + '" size="' + Math.min(Math.max(w, 6), 22) + '" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" aria-label="Lücke">';
    }).join('');
  }
  function gapSolution(it) { return gapParts(it).map(function (p) { return p.t !== undefined ? p.t : '<b>' + esc(p.g[0]) + '</b>'; }).join(''); }
  function plainHTML(it) {
    if (it.type === 'mc') return it.q; if (it.type === 'tf') return it.statement;
    return gapParts(it).map(function (p) { return p.t !== undefined ? p.t : '…'; }).join('');
  }
  // ---- Echtes Multiple Choice (Psycho 2): 4 Optionen, 1–4 richtig, je Option ±1, mindestens 0 → 0/2/4 Punkte
  function corrSet(it) { return Array.isArray(it.correct) ? it.correct : [it.correct]; }
  function isMulti(it, sid) { return it.type === 'mc' && (it._s || sid) === 'psy'; }
  function mcPoints(it, sel) {
    var c = corrSet(it), p = 0; sel = sel || [];
    it.options.forEach(function (_, i) { p += (sel.indexOf(i) >= 0) === (c.indexOf(i) >= 0) ? 1 : -1; });
    return Math.max(0, p);
  }
  function mcMarked(it, sel, order) {
    var c = corrSet(it); order = order || it.options.map(function (_, i) { return i; });
    return '<div class="opts">' + order.map(function (oi) {
      var on = !!sel && sel.indexOf(oi) >= 0, r = c.indexOf(oi) >= 0, cls, lab;
      if (!sel) { cls = r ? 'ok' : 'okn'; lab = r ? 'richtig' : ''; }
      else if (on && r) { cls = 'ok'; lab = 'Richtig angekreuzt'; }
      else if (!on && !r) { cls = 'okn'; lab = 'Richtig weggelassen'; }
      else if (on) { cls = 'bad'; lab = 'Falsch angekreuzt'; }
      else { cls = 'miss'; lab = 'Vergessen · wäre richtig'; }
      return '<div class="opt mopt ' + cls + '"><span class="box">' + (on || (!sel && r) ? ic('check') : '') + '</span><span>' + it.options[oi] + (lab ? '<small class="mlab">' + lab + '</small>' : '') + '</span></div>';
    }).join('') + '</div>';
  }
  // Auswertung getrennt nach Art, z. B. „MC 22/32 Punkte · R/F 8/10 · Lücke 2,5/4“
  function breakdown(rows) {
    var g = {}, L = { mcp: 'MC', mc: 'MC', tf: 'R/F', gap: 'Lücke' };
    rows.forEach(function (r) {
      var k = r.p !== undefined ? 'mcp' : r.it.type, x = g[k] = g[k] || { a: 0, m: 0 };
      x.a += r.p !== undefined ? r.p : r.s; x.m += r.p !== undefined ? r.it.options.length : 1;
    });
    if (g.mcp && g.mc) L.mc = 'Single Choice';
    return ['mcp', 'mc', 'tf', 'gap'].filter(function (k) { return g[k]; }).map(function (k) { return L[k] + ' ' + fmt(g[k].a) + '/' + g[k].m + (k === 'mcp' ? ' Punkte' : ''); }).join(' · ');
  }
  // ---- Frage melden: geht über die Feedback-Warteschlange ins Blatt „Feedback“ (Seite = Fach + Fragen-ID)
  var REP_WHY = ['Antwort falsch', 'Mehrere Antworten passen', 'Unklar formuliert', 'Erklärung fehlt oder falsch', 'Tippfehler', 'Sonstiges'];
  function reportQ(it, sid, btn) {
    if (!it) return;
    var fach = it._s || sid, why = '';
    openTile('Frage melden',
      '<p class="note" style="margin:0 0 10px">Was stimmt nicht? Die Nummer der Frage wird mitgeschickt.</p>' +
      '<div class="chips" id="repWhy">' + REP_WHY.map(function (w) { return '<button type="button" class="chip" data-w="' + w + '">' + w + '</button>'; }).join('') + '</div>' +
      '<textarea id="repText" class="fbtext" maxlength="500" placeholder="Kommentar (optional)" aria-label="Kommentar"></textarea>' +
      '<p class="note" style="margin:0">Bitte keine persönlichen Daten hineinschreiben.</p>',
      '<div class="row"><button type="button" class="ghost pvok">Abbrechen</button><button type="button" class="primary" id="repGo" disabled>Senden</button></div>');
    var go = $('#repGo'), ta = $('#repText');
    function upd() { go.disabled = !why && !ta.value.trim(); }
    $$('#repWhy .chip').forEach(function (b) {
      b.onclick = function () { why = why === b.dataset.w ? '' : b.dataset.w; $$('#repWhy .chip').forEach(function (x) { x.classList.toggle('on', x.dataset.w === why); }); upd(); };
    });
    ta.addEventListener('input', upd);
    go.onclick = function () {
      var c = ta.value.trim().slice(0, 500);
      if (!why && !c) return;
      fbQueue(fbQueue().concat([{ text: 'Frage gemeldet · ' + (why || 'Kommentar') + (c ? ': ' + c : ''), ts: Date.now(), seite: ('Frage ' + fach + ' · ' + it.id).slice(0, 80) }]));
      closeTile();
      if (btn) { btn.textContent = 'Gemeldet ✓'; btn.disabled = true; }
      if (navigator.onLine === false) { toast('Gespeichert · wird gesendet, sobald du online bist'); return; }
      fbFlush(function (ok) { toast(ok ? 'Danke, Frage gemeldet' : 'Gerade keine Verbindung · wird später gesendet'); });
    };
  }
  function grade(it, ans) {
    if (it.type === 'mc') return Array.isArray(ans) ? mcPoints(it, ans) / it.options.length : ans === it.correct ? 1 : 0;
    if (it.type === 'tf') return ans === it.answer ? 1 : 0;
    var parts = gapParts(it).filter(function (p) { return p.g; }), ok = 0;
    if (!parts.length) return 0;
    parts.forEach(function (p, k) { var v = norm((ans && ans[k]) || ''); if (v && p.g.some(function (a) { return norm(a) === v; })) ok++; });
    return ok / parts.length;
  }
  function solutionHTML(it, multi, sel, order) {
    var s = it.type === 'mc' && multi ? mcMarked(it, sel, order) + '<div class="tip"><b>' + (sel ? mcPoints(it, sel) + ' / ' + it.options.length + ' Punkte' : 'Nicht beantwortet · 0 Punkte') + '</b></div>' :
      it.type === 'mc' ? '<div class="tip"><b>Richtig:</b> ' + corrSet(it).map(function (i) { return it.options[i]; }).join(' · ') + '</div>' :
      it.type === 'tf' ? '<div class="tip"><b>' + (it.answer ? 'Richtig' : 'Falsch') + '.</b></div>' : '<div class="tip">' + gapSolution(it) + '</div>';
    if (it.expl) s += '<div class="tip' + (it.warn ? ' warn' : '') + '">' + it.expl + '</div>';
    return s;
  }
  function noteFor(p) {
    var t = [[95, '1,0'], [90, '1,3'], [85, '1,7'], [80, '2,0'], [75, '2,3'], [70, '2,7'], [65, '3,0'], [60, '3,3'], [55, '3,7'], [50, '4,0']];
    for (var i = 0; i < t.length; i++) if (p >= t[i][0]) return t[i][1];
    return '5,0';
  }

  function testsView(s, ch, q) {
    var ITEMS = ch.items, BYID = {}; ITEMS.forEach(function (i) { BYID[i.id] = i; });
    var T = tests(s.id, ch.id), st = DB.settings;
    var sh = s.mix ? function (l) { return mixShuffle(l, st.mixMode === 'even'); } : shuffle;
    function pool(type) { return ITEMS.filter(function (i) { return i.type === type; }); }
    function nav(extra) { return '<div class="nav">' + backLink(backHref(s.href || '#/f/' + s.id), fromSearch() ? 'Suche' : s.name) + (extra || '') + '</div>'; }
    function prep(id) { var it = BYID[id]; return { it: it, order: it.type === 'mc' ? shuffle(it.options.map(function (_, i) { return i; })) : null, multi: isMulti(it, s.id) }; }
    function finishLog(r) {
      logAns(r.it._s || s.id, r.it.id, r.s, r.p); T.ts = Date.now();
      var ix = T.wrong.indexOf(r.it.id);
      if (r.s === 1 && ix >= 0) T.wrong.splice(ix, 1);
      if (r.s < 1 && ix < 0) T.wrong.push(r.it.id);
    }

    function hub() {
      setImm(false);
      var counts = { mc: pool('mc').length, tf: pool('tf').length, gap: pool('gap').length }, total = ITEMS.length;
      var h = nav() + '<h1 style="font-size:1.55rem">' + esc(ch.title) + '</h1><p class="sub">' + esc(ch.sub || '') + '</p>' + (ch.note ? '<p class="cnote hub">' + esc(ch.note) + '</p>' : '');
      if (ch.placeholder) h += '<div class="banner"><b>Gerüst:</b> Das sind nur Beispielfragen, damit du die Test-Funktionen ausprobieren kannst. Die echten Inhalte folgen.</div>';
      h += '<div class="chips"><span class="lbl">Fragen pro Runde</span>' + [5, 10, 0].map(function (n) { return '<button class="chip' + (st.testN === n ? ' on' : '') + '" data-n="' + n + '">' + (n || 'Alle') + '</button>'; }).join('') + '</div>';
      var cardsMode = '';
      if (ch.cards) {
        var kn = ch.cards.filter(function (c) { return DB.progress[c.id] === 'known'; }).length;
        cardsMode = '<button class="mode" data-m="cards"><span class="ico">' + ic('cards') + '</span><span><span class="t">Karteikarten</span><br><span class="d">Umdrehen, gewusst oder nochmal</span></span><span class="r">' + ch.cards.length + ' Karten' + (kn ? '<b>' + kn + ' gewusst</b>' : '') + '</span></button>';
      }
      h += '<div class="modes">' + cardsMode + MODES.map(function (m) {
        var c = m.id === 'exam' ? total : counts[m.id], b = T.best[m.id];
        return '<button class="mode" data-m="' + m.id + '"' + (c ? '' : ' disabled') + '><span class="ico">' + ic(m.ico) + '</span><span><span class="t">' + m.name + '</span><br><span class="d">' + (m.id === 'mc' && s.id === 'psy' ? 'Vier Antworten, 1 bis 4 richtig' : m.desc) + '</span></span>' +
          '<span class="r">' + c + ' Fragen' + (b !== undefined ? '<b>Bestwert ' + b + ' %</b>' : '') + '</span></button>';
      }).join('') + '</div>';
      if (ch.rel) h += '<a class="mode rsrel" href="' + ch.rel.href + '"><span class="ico">' + ic('book') + '</span><span><span class="t">' + esc(ch.rel.t) + '</span><br><span class="d">' + esc(ch.rel.d) + '</span></span>' + CHEV + '</a>';
      h += '<div class="row" style="margin-top:14px">' + (ch.cards ? '<button class="ghost" id="readC">' + ic('book') + 'Karten lesen</button>' : '') + '<button class="ghost" id="readQ">' + ic('book') + 'Fragen lesen</button></div>';
      if (st.mMosaic && !s.mix) h += mosaicHTML(ITEMS);
      var wr = T.wrong.filter(function (id) { return BYID[id]; });
      if (wr.length) h += '<div class="row" style="margin-top:14px"><button class="ghost" id="wrong">Falsche Fragen wiederholen (' + wr.length + ')</button></div>';
      h += '<div class="tools"><button id="reset">Fortschritt zurücksetzen</button></div>';
      view.innerHTML = h;
      $$('.chip').forEach(function (b) { b.onclick = function () { st.testN = parseInt(b.dataset.n, 10); save(); hub(); }; });
      $$('.mode').forEach(function (b) { b.onclick = function () { start(b.dataset.m); }; });
      $('#readQ').onclick = function () { readItems(0); };
      if (st.mMosaic && !s.mix) wireMosaic(ITEMS, function (id) { run([prep(id)], 'wrong', 'Einzelfrage'); });
      var rc = $('#readC'); if (rc) rc.onclick = function () { location.hash = '#/f/' + s.id + '/' + ch.id + '?read=1'; };
      var wb = $('#wrong'); if (wb) wb.onclick = function () { run(shuffle(wr).map(prep), 'wrong', 'Falsche Fragen'); };
      $('#reset').onclick = function () {
        var b = $('#reset');
        if (b.dataset.sure) { T.best = {}; T.wrong = []; T.ts = Date.now(); save(); hub(); } else { b.textContent = 'Wirklich zurücksetzen?'; b.dataset.sure = 1; }
      };
    }
    function readItems(k) {
      var list = ITEMS, total = list.length; k = Math.max(0, Math.min(k, total - 1));
      var it = list[k], qh, ah;
      if (it.type === 'mc') { qh = it.q; ah = corrSet(it).map(function (i) { return it.options[i]; }).join('<br>'); }
      else if (it.type === 'tf') { qh = it.statement; ah = '<b>' + (it.answer ? 'Richtig' : 'Falsch') + '</b>'; }
      else { qh = plainHTML(it); ah = gapSolution(it); }
      var h = nav('<button id="rEnd">Fertig</button>') + '<h1 style="font-size:1.4rem">' + esc(ch.title) + '</h1><p class="sub" style="margin-bottom:0">Lesen · ohne Wertung</p>' +
        '<div class="status"><span>' + TYPES[it.type] + ' · ' + (k + 1) + ' / ' + total + '</span><span>' + esc(it.src || '') + '</span></div>' +
        '<div class="pbar"><div style="width:' + ((k + 1) / total * 100) + '%"></div></div>' +
        '<div class="card"><div class="meta"><span></span><span class="side">Frage</span></div><div class="face">' + qh + '</div></div>' +
        '<div class="card" style="margin-top:10px"><div class="meta"><span></span><span class="side" style="color:var(--green)">Antwort</span></div><div class="face">' + ah + '</div>' + (it.expl ? '<div class="tip' + (it.warn ? ' warn' : '') + '">' + it.expl + '</div>' : '') + '</div>' +
        '<div class="row"><button class="ghost" id="rPrev"' + (k === 0 ? ' disabled' : '') + '>' + ic('left') + 'Zurück</button><button class="ghost" id="rNext"' + (k === total - 1 ? ' disabled' : '') + '>Weiter' + ic('right') + '</button></div>';
      view.innerHTML = h; window.scrollTo(0, 0);
      $('#rEnd').onclick = hub;
      $('#rPrev').onclick = function () { readItems(k - 1); }; $('#rNext').onclick = function () { readItems(k + 1); };
    }
    function start(mode) {
      if (mode === 'cards') { location.hash = '#/f/' + s.id + '/' + ch.id + '?mode=cards'; return; }
      if (mode === 'exam') return examSetup();
      var ids = sh(pool(mode)).map(function (i) { return i.id; }); if (st.testN) ids = ids.slice(0, st.testN);
      run(ids.map(prep), mode, TYPES[mode]);
    }
    function questionBody(p, values) {
      var it = p.it;
      if (it.type === 'mc' && p.multi) return '<div class="qtext">' + it.q + '</div><div class="mhint">1 bis 4 Antworten sind richtig</div><div class="opts">' + p.order.map(function (oi) { var on = values && values.indexOf(oi) >= 0; return '<button class="opt mopt' + (on ? ' sel' : '') + '" data-o="' + oi + '" aria-pressed="' + on + '"><span class="box">' + (on ? '✓' : '') + '</span><span>' + it.options[oi] + '</span></button>'; }).join('') + '</div>';
      if (it.type === 'mc') return '<div class="qtext">' + it.q + '</div><div class="opts">' + p.order.map(function (oi, k) { return '<button class="opt" data-o="' + oi + '"><span class="k">' + 'ABCD'.charAt(k) + '</span><span>' + it.options[oi] + '</span></button>'; }).join('') + '</div>';
      if (it.type === 'tf') return '<div class="qtext">' + it.statement + '</div><div class="tfrow"><button class="opt" data-v="1">Richtig</button><button class="opt" data-v="0">Falsch</button></div>';
      return '<div class="qtext gaptext">' + gapHTML(it, values) + '</div>';
    }

    function run(queue, mode, title) {
      var i = 0, results = [], skipped = 0;
      if (!queue.length) { view.innerHTML = nav() + '<div class="empty">Keine Fragen in dieser Auswahl.</div>'; return; }
      setImm(true);
      var fachName = subj(s.id) ? subj(s.id).name : s.name;
      function show() {
        if (i >= queue.length) return finish();
        var p = queue[i], it = p.it, done = false, isTF = it.type === 'tf';
        var where = s.mix ? (subj(it._s) ? subj(it._s).name : '') : fachName + ' · ' + ch.title.split(' · ')[0];
        var h = lhead('quit', '', isTF ? 'Richtig oder falsch?' : title, where, (i + 1) + '/' + queue.length, i / queue.length);
        if (isTF) {
          var len = textOf(it.statement).length, sz = len > 150 ? ' l' : len > 70 ? ' m' : '';
          h += '<div class="card rfcard"><div class="chips2">' + (s.mix && subj(it._s) ? '<span class="tchip acc">' + esc(subj(it._s).name) + '</span>' : '<span class="tchip acc">' + esc(ch.title.split(' · ')[0]) + '</span>') +
            (it.src ? '<span class="tchip">' + esc(it.src) + '</span>' : '') + '</div><div class="stmt' + sz + '"><div>' + it.statement + '</div></div><div id="fb"></div></div>' +
            '<div class="rfbtns" id="tfrow"><button class="yes" data-v="1">' + ic('check') + 'Richtig</button><button class="no" data-v="0">' + ic('x') + 'Falsch</button></div>' +
            '<button type="button" class="skip" id="skip">Überspringen</button>';
        } else h += '<div class="card">' + (it.src ? '<div class="meta"><span>' + esc(it.src) + '</span></div>' : '') + questionBody(p) + '<div id="fb"></div></div>';
        if (!s.mix && !s.due) setLast({ h: '#/f/' + s.id + '/' + ch.id, t: ch.title, sub: fachName + ' · ' + title + ', bei Frage ' + (i + 1) + ' von ' + queue.length + ' aufgehört' });
        if (it.type === 'gap') h += '<div class="row" id="gaprow"><button class="ghost" id="reveal">Lösung zeigen</button><button class="primary" id="check">Prüfen</button></div>';
        if (p.multi) h += '<div class="row" id="mcrow"><button class="primary" id="mcheck" disabled>Prüfen</button></div>';
        view.innerHTML = h; window.scrollTo(0, 0);
        kwAttach($('.card', view), it, it._s || s.id);
        $('#quit').onclick = hub;
        function answered(score, pts) {
          if (done) return; done = true; results.push({ it: it, s: score, p: pts });
          var sym = score === 1 ? ic('check') : score > 0 ? ic('half') : ic('x');
          var head = pts !== undefined ? pts + ' / ' + it.options.length + ' Punkte' : score === 1 ? 'Richtig' : score > 0 ? 'Teilweise richtig' : 'Nicht ganz';
          if (isTF) { var sk = $('#skip'); if (sk) sk.remove(); }
          $('#fb').innerHTML = '<div class="fb ' + (score === 1 ? 'ok' : score > 0 && pts !== undefined ? 'mid' : 'bad') + '" role="status">' + sym + head + '</div>' +
            (isTF ? '<div class="tip"><b>' + (it.answer ? 'Die Aussage ist richtig.' : 'Die Aussage ist falsch.') + '</b></div>' : '') +
            (it.expl ? '<div class="tip' + (it.warn ? ' warn' : '') + '">' + it.expl + '</div>' : '') +
            '<div class="row"><button class="primary" id="next">' + (i === queue.length - 1 ? 'Ergebnis' : 'Weiter') + ic('right') + '</button></div>' +
            '<div class="tools"><button id="rep">Frage melden</button></div>';
          $('#next').onclick = function () { i++; show(); };
          $('#rep').onclick = function () { reportQ(it, s.id, $('#rep')); };
        }
        if (p.multi) {
          var sel = [], mb = $('#mcheck');
          $$('.opt').forEach(function (b) {
            b.onclick = function () {
              var o = parseInt(b.dataset.o, 10), ix = sel.indexOf(o);
              if (ix >= 0) sel.splice(ix, 1); else sel.push(o);
              var on = ix < 0; b.classList.toggle('sel', on); b.setAttribute('aria-pressed', on); $('.box', b).innerHTML = on ? ic('check') : '';
              mb.disabled = !sel.length;
            };
          });
          mb.onclick = function () {
            if (!sel.length) return;
            var pts = mcPoints(it, sel);
            $('.opts', view).outerHTML = mcMarked(it, sel, p.order); $('#mcrow').remove();
            answered(pts / it.options.length, pts);
          };
        } else if (it.type === 'mc') {
          $$('.opt').forEach(function (b) {
            b.onclick = function () {
              var o = parseInt(b.dataset.o, 10);
              $$('.opt').forEach(function (x) { x.disabled = true; if (parseInt(x.dataset.o, 10) === it.correct) x.classList.add('ok'); });
              if (o !== it.correct) b.classList.add('bad'); answered(grade(it, o));
            };
          });
        } else if (isTF) {
          $$('#tfrow button').forEach(function (b) {
            b.onclick = function () {
              var v = b.dataset.v === '1';
              $$('#tfrow button').forEach(function (x) { x.disabled = true; }); b.classList.add('pick');
              answered(grade(it, v));
              var fb = $('#fb'); if (fb) fb.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
            };
          });
          $('#skip').onclick = function () { skipped++; i++; show(); };
        } else {
          var inputs = $$('input.gap'), parts = gapParts(it).filter(function (z) { return z.g; });
          if (inputs[0]) inputs[0].focus({ preventScroll: true });
          var check = function (reveal) {
            if (done) return;
            var vals = inputs.map(function (x) { return x.value; }), sc = reveal ? 0 : grade(it, vals);
            inputs.forEach(function (x, k) {
              var ok = !reveal && parts[k].g.some(function (a) { return norm(a) === norm(x.value); });
              x.classList.add(ok ? 'ok' : 'bad'); x.readOnly = true;
              if (!ok) x.insertAdjacentHTML('afterend', '<span class="sol">→ ' + esc(parts[k].g[0]) + '</span>');
            });
            $('#gaprow').remove(); answered(sc);
          };
          $('#check').onclick = function () { check(false); };
          $('#reveal').onclick = function () { check(true); };
          inputs.forEach(function (x, k) { x.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); if (k < inputs.length - 1) inputs[k + 1].focus(); else check(false); } }); });
        }
      }
      function finish() {
        setImm(false);
        if (!results.length) return hub();
        var pts = results.reduce(function (a, r) { return a + r.s; }, 0), pct = Math.round(pts / results.length * 100);
        results.forEach(finishLog);
        if (mode !== 'wrong' && (T.best[mode] === undefined || pct > T.best[mode])) T.best[mode] = pct; T.ts = Date.now();
        save(); badgeCheck();
        var bad = results.filter(function (r) { return r.s < 1; }), hasP = results.some(function (r) { return r.p !== undefined; });
        var h = nav() + '<div class="card"><div class="score"><div class="big">' + pct + ' %</div><div class="note">' + (hasP ? breakdown(results) : fmt(pts) + ' von ' + results.length + ' richtig') + (skipped ? ' · ' + skipped + ' übersprungen' : '') + ' · ' + title + '</div></div></div>';
        if (bad.length) {
          h += '<div class="list">' + bad.map(function (r) { return '<details class="it"><summary><span class="st ' + (r.s > 0 ? 'mid" aria-label="teilweise">' + ic('half') : 'bad" aria-label="falsch">' + ic('x')) + '</span><span>' + plainHTML(r.it) + '</span></summary><div class="body">' + solutionHTML(r.it, r.p !== undefined) + '</div></details>'; }).join('') + '</div>' +
            '<div class="row" style="margin-top:14px"><button class="ghost" id="againWrong">Falsche wiederholen</button><button class="primary" id="again">Nochmal</button></div>';
        } else h += '<div class="tip" style="margin-top:12px">Alles richtig. Stark!</div><div class="row"><button class="primary" id="again">Nochmal</button></div>';
        h += '<div class="tools"><button id="menu">Zum Menü</button></div>';
        view.innerHTML = h; window.scrollTo(0, 0);
        $('#menu').onclick = hub; $('#again').onclick = function () { mode === 'wrong' ? hub() : start(mode); };
        var aw = $('#againWrong'); if (aw) aw.onclick = function () { run(shuffle(bad.map(function (r) { return r.it.id; })).map(prep), 'wrong', 'Falsche Fragen'); };
      }
      show();
    }

    function examSetup() {
      setImm(false);
      var maxN = ITEMS.length, counts = [8, 12, 16].filter(function (n) { return n <= maxN; }); if (!counts.length) counts = [maxN];
      if (counts.indexOf(st.examN) < 0) st.examN = counts[counts.length - 1];
      view.innerHTML = nav() + '<h1 style="font-size:1.55rem">Zeit-Simulation</h1><p class="sub">Mini-Klausur mit gemischten Fragen. Ergebnis, Punkte und Note gibt es erst am Ende.</p>' +
        '<div class="chips"><span class="lbl">Zeit</span>' + [10, 20, 30].map(function (m) { return '<button class="chip' + (st.examMin === m ? ' on' : '') + '" data-min="' + m + '">' + m + ' Min</button>'; }).join('') + '</div>' +
        '<div class="chips"><span class="lbl">Fragen</span>' + counts.map(function (n) { return '<button class="chip' + (st.examN === n ? ' on' : '') + '" data-exn="' + n + '">' + n + '</button>'; }).join('') + '</div>' +
        '<div class="row"><button class="primary" id="go">Klausur starten</button></div>';
      $$('[data-min]').forEach(function (b) { b.onclick = function () { st.examMin = parseInt(b.dataset.min, 10); save(); examSetup(); }; });
      $$('[data-exn]').forEach(function (b) { b.onclick = function () { st.examN = parseInt(b.dataset.exn, 10); save(); examSetup(); }; });
      $('#go').onclick = function () { save(); exam(st.examMin, st.examN); };
    }
    function exam(minutes, n) {
      var qs = { mc: sh(pool('mc')), tf: sh(pool('tf')), gap: sh(pool('gap')) }, order = ['mc', 'tf', 'gap'], queue = [], k = 0, guard = 0;
      while (queue.length < n && guard++ < 500) { var t = order[k++ % 3]; if (qs[t].length) queue.push(qs[t].shift()); }
      queue = queue.map(function (it) { return prep(it.id); });
      var ans = queue.map(function () { return null; }), cur = 0, end = Date.now() + minutes * 60000, timer = null, finished = false;
      setImm(true);
      onLeave(function () { clearInterval(timer); });
      function stash() { if (queue[cur].it.type === 'gap') ans[cur] = $$('input.gap').map(function (x) { return x.value; }); }
      function clockText() { var left = Math.max(0, Math.round((end - Date.now()) / 1000)); return { txt: Math.floor(left / 60) + ':' + ('0' + (left % 60)).slice(-2), left: left }; }
      function answeredAt(i) { var a = ans[i]; if (a === null || a === undefined) return false; if (queue[i].multi) return a.length > 0; return Array.isArray(a) ? a.some(function (v) { return v.trim(); }) : true; }
      function show() {
        var p = queue[cur], it = p.it, c = clockText();
        view.innerHTML = '<div class="nav"><span class="clock' + (c.left < 60 ? ' low' : '') + '">' + ic('clock') + '<span id="clock">' + c.txt + '</span></span><button id="submit">Abgeben</button></div>' +
          '<div class="dots">' + queue.map(function (_, i) { return '<button data-i="' + i + '" class="' + (i === cur ? 'cur ' : '') + (answeredAt(i) ? 'done' : '') + '">' + (i + 1) + '</button>'; }).join('') + '</div>' +
          '<div class="meta"><span>Frage ' + (cur + 1) + ' / ' + queue.length + '</span><span>' + TYPES[it.type] + '</span></div><div class="card">' + questionBody(p, Array.isArray(ans[cur]) ? ans[cur] : null) + '</div>' +
          '<div class="row"><button class="ghost" id="prev"' + (cur === 0 ? ' disabled' : '') + '>' + ic('left') + 'Zurück</button><button class="ghost" id="nxt"' + (cur === queue.length - 1 ? ' disabled' : '') + '>Weiter' + ic('right') + '</button></div>';
        if (p.multi) $$('.opt').forEach(function (b) { b.onclick = function () { var o = parseInt(b.dataset.o, 10), a = ans[cur] || [], ix = a.indexOf(o); if (ix >= 0) a.splice(ix, 1); else a.push(o); ans[cur] = a; show(); }; });
        else if (it.type === 'mc') $$('.opt').forEach(function (b) { if (ans[cur] === parseInt(b.dataset.o, 10)) b.classList.add('sel'); b.onclick = function () { ans[cur] = parseInt(b.dataset.o, 10); show(); }; });
        else if (it.type === 'tf') $$('.opt').forEach(function (b) { if (ans[cur] === (b.dataset.v === '1')) b.classList.add('sel'); b.onclick = function () { ans[cur] = b.dataset.v === '1'; show(); }; });
        else $$('input.gap').forEach(function (x, kk, all) {
          x.addEventListener('input', stash);
          x.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); if (kk < all.length - 1) all[kk + 1].focus(); else x.blur(); } });
        });
        $$('.dots button').forEach(function (b) { b.onclick = function () { stash(); cur = parseInt(b.dataset.i, 10); show(); }; });
        $('#prev').onclick = function () { stash(); cur--; show(); }; $('#nxt').onclick = function () { stash(); cur++; show(); };
        $('#submit').onclick = function () {
          var b = $('#submit');
          if (b.dataset.sure) { stash(); finish(); }
          else { var open = ans.filter(function (_, i) { return !answeredAt(i); }).length; b.textContent = open ? open + ' offen · wirklich?' : 'Wirklich abgeben?'; b.dataset.sure = 1; }
        };
      }
      function tick() {
        var c = clockText(), el = $('#clock');
        if (el) { el.textContent = c.txt; el.parentNode.classList.toggle('low', c.left < 60); }
        if (c.left <= 0 && !finished) { stash(); finish(true); }
      }
      function finish(timeout) {
        if (finished) return; finished = true; clearInterval(timer); setImm(false);
        var pts = 0, rows = queue.map(function (p, i) {
          if (p.multi) { var a = ans[i] && ans[i].length ? ans[i] : null, mp = a ? mcPoints(p.it, a) : 0; pts += mp / p.it.options.length; return { it: p.it, s: mp / p.it.options.length, p: mp, a: a, o: p.order }; }
          var sc = grade(p.it, ans[i]); pts += sc; return { it: p.it, s: sc };
        });
        var pct = Math.round(pts / queue.length * 100), hasP = rows.some(function (r) { return r.p !== undefined; });
        rows.forEach(finishLog);
        if (T.best.exam === undefined || pct > T.best.exam) T.best.exam = pct;
        save(); badgeCheck();
        var used = Math.round((Date.now() - (end - minutes * 60000)) / 1000);
        view.innerHTML = nav() + '<div class="card"><div class="score"><div class="big">' + (hasP ? pct + ' %' : fmt(pts) + ' / ' + queue.length) + '</div><div class="note">' + (hasP ? breakdown(rows) : pct + ' %') + ' · Note ' + noteFor(pct) + ' (Richtwert)' +
          (timeout ? ' · Zeit abgelaufen' : ' · ' + Math.floor(used / 60) + ':' + ('0' + used % 60).slice(-2) + ' Min benötigt') + '</div></div></div><div class="list">' +
          rows.map(function (r) {
            var cls = r.s === 1 ? 'ok' : r.s > 0 ? 'mid' : 'bad', sym = r.s === 1 ? ic('check') : r.s > 0 ? ic('half') : ic('x');
            return '<details class="it"><summary><span class="st ' + cls + '">' + sym + '</span><span>' + plainHTML(r.it) + '</span></summary><div class="body">' + solutionHTML(r.it, r.p !== undefined, r.a, r.o) + '<div class="tools"><button data-rep="' + r.it.id + '">Frage melden</button></div></div></details>';
          }).join('') + '</div><div class="row" style="margin-top:14px"><button class="ghost" id="menu">Zum Menü</button><button class="primary" id="again">Neue Klausur</button></div>';
        window.scrollTo(0, 0); $('#menu').onclick = hub; $('#again').onclick = examSetup;
        $$('[data-rep]').forEach(function (b) { b.onclick = function () { reportQ(BYID[b.dataset.rep], s.id, b); }; });
      }
      show(); timer = setInterval(tick, 500);
    }

    function single(id, terms) {
      var it = BYID[id]; if (!it) return hub();
      view.innerHTML = nav('<button id="all">Alle Tests</button>') +
        '<div class="meta"><span>' + esc(ch.title) + ' · ' + TYPES[it.type] + '</span><span>' + esc(it.src || '') + '</span></div>' +
        '<div class="card"><div class="qtext">' + (it.type === 'gap' ? gapSolution(it) : plainHTML(it)) + '</div>' +
        (it.type === 'mc' ? '<div class="opts">' + it.options.map(function (o, i) { return '<div class="opt' + (corrSet(it).indexOf(i) >= 0 ? ' ok' : '') + '"><span class="k">' + 'ABCD'.charAt(i) + '</span><span>' + o + '</span></div>'; }).join('') + '</div>' : '') +
        (it.type === 'tf' ? '<div class="tip"><b>' + (it.answer ? 'Richtig' : 'Falsch') + '.</b></div>' : '') + (it.expl ? '<div class="tip' + (it.warn ? ' warn' : '') + '">' + it.expl + '</div>' : '') + '</div>';
      $('#all').onclick = hub; highlight($('.card', view), terms);
    }
    if (q.q) single(q.q, (q.hl || '').split(/\s+/)); else hub();
  }

  // ====================================================================== Suche
  var SEARCH = C.search; SEARCH.forEach(function (e) { e._h = nrm(e.title + ' ' + e.kw); e._t = nrm(e.text); });
  function mapNorm(s) { var out = '', map = []; for (var i = 0; i < s.length; i++) { var c = nrm(s[i]); for (var j = 0; j < c.length; j++) { out += c[j]; map.push(i); } } return { t: out, m: map }; }
  function snippet(text, toks) {
    var mn = mapNorm(text), pos = -1;
    toks.forEach(function (t) { var p = mn.t.indexOf(t); if (p >= 0 && (pos < 0 || p < pos)) pos = p; });
    var start = 0, end = Math.min(text.length, 170);
    if (pos >= 0) { var o = mn.m[pos]; start = Math.max(0, o - 55); end = Math.min(text.length, o + 115); var sp = text.lastIndexOf(' ', start + 12); if (start > 0 && sp > 0 && sp < o) start = sp + 1; }
    var ranges = [];
    toks.forEach(function (t) { var from = 0, p; while ((p = mn.t.indexOf(t, from)) >= 0) { var a = mn.m[p], b = mn.m[p + t.length - 1] + 1; if (a >= start && b <= end) ranges.push([a, b]); from = p + t.length; } });
    ranges.sort(function (x, y) { return x[0] - y[0]; });
    var html = '', cur = start;
    ranges.forEach(function (r) { if (r[0] < cur) return; html += esc(text.slice(cur, r[0])) + '<mark>' + esc(text.slice(r[0], r[1])) + '</mark>'; cur = r[1]; });
    return (start > 0 ? '… ' : '') + html + esc(text.slice(cur, end)) + (end < text.length ? ' …' : '');
  }
  // Wortschatz für Vorschläge: Schlagwörter aus dem Suchindex (Anzeigeform + Häufigkeit)
  var VOCAB = (function () {
    var m = {};
    SEARCH.forEach(function (e) {
      var seen = {};
      (e.kw || '').split(/\s+/).forEach(function (w) {
        w = w.replace(/^[^\wäöüÄÖÜß]+|[^\wäöüÄÖÜß]+$/g, ''); var k = nrm(w);
        if (k.length < 4 || /^[\d.^]+$/.test(k) || seen[k]) return; seen[k] = 1;
        if (!m[k]) m[k] = { k: k, w: w, n: 0, s: {} }; m[k].n++; m[k].s[e.s] = (m[k].s[e.s] || 0) + 1;
        if (/^[A-ZÄÖÜ]/.test(w) && !/^[A-ZÄÖÜ]/.test(m[k].w)) m[k].w = w;
      });
    });
    return Object.keys(m).map(function (k) { return m[k]; }).sort(function (a, b) { return b.n - a.n || (a.k < b.k ? -1 : 1); });
  })();
  function lev(a, b) {
    if (Math.abs(a.length - b.length) > 2) return 9;
    var prev = [], cur, i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur = [i];
      for (j = 1; j <= b.length; j++) cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      prev = cur;
    }
    return prev[b.length];
  }
  function popular(per) {
    var out = [], seen = {};
    C.subjects.forEach(function (sj) {
      if (isHidden(sj.id)) return;
      VOCAB.filter(function (v) { return v.s[sj.id]; }).sort(function (a, b) { return b.s[sj.id] - a.s[sj.id] || (a.k < b.k ? -1 : 1); }).slice(0, per)
        .forEach(function (v) { if (!seen[v.k]) { seen[v.k] = 1; out.push(v.w); } });
    });
    return out;
  }
  function prefixSug(tok) { return VOCAB.filter(function (v) { return v.k !== tok && v.k.indexOf(tok) === 0; }).slice(0, 6); }
  function fuzzySug(tok) {
    if (tok.length < 4) return [];
    var maxd = tok.length >= 8 ? 2 : 1;
    return VOCAB.map(function (v) { return { v: v, d: Math.min(lev(tok, v.k), lev(tok, v.k.slice(0, tok.length))) }; })
      .filter(function (x) { return x.d <= maxd && x.v.k !== tok; })
      .sort(function (a, b) { return a.d - b.d || b.v.n - a.v.n; }).slice(0, 4).map(function (x) { return x.v; });
  }
  function remember(q) {
    q = (q || '').trim(); if (nrm(q).length < 3) return;
    DB.recent = DB.recent.filter(function (r) { return nrm(r) !== nrm(q); }); DB.recent.unshift(q); DB.recent = DB.recent.slice(0, 8); save();
  }
  function chips(list, cls) { return '<div class="sugrow">' + list.map(function (w) { return '<button class="sugchip' + (cls ? ' ' + cls : '') + '" data-w="' + esc(w) + '">' + esc(w) + '</button>'; }).join('') + '</div>'; }

  // ====================================================================== Begriffe (v59): Wörter in Fragen antippen, Erklärung aus Karteikarten, Liste „Meine Begriffe“
  var KW_IC = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h10M4 11h7M4 16h5"/><circle cx="16.5" cy="14.5" r="3.5"/><path d="M19 17l2.5 2.5"/></svg>';
  function kwTxt(h) { return textOf(String(h || '').replace(/<annotation[\s\S]*?<\/annotation>/g, '')); }
  function kwKey(sid, t) { return sid + ':' + norm(t); }
  function kwStem(t) { t = norm(t); return t.length >= 6 ? t.replace(/(en|er|es|n|s|e)$/, '') : t; }
  function kwList(sid) {
    return Object.keys(DB.terms).map(function (k) { return DB.terms[k]; })
      .filter(function (x) { return x && !x.d && x.t && (!sid || x.s === sid) && subj(x.s) && !isHidden(x.s); })
      .sort(function (a, b) { return b.ts - a.ts; });
  }
  function kwHas(sid, t) { var x = DB.terms[kwKey(sid, t)]; return !!(x && !x.d); }
  function kwSet(sid, t, on, ctx) {
    var k = kwKey(sid, t), old = DB.terms[k] || {};
    DB.terms[k] = on ? { t: t, s: sid, q: (ctx && ctx.q) || old.q || '', src: (ctx && ctx.src) || old.src || '', m: old.m || 0, ts: Date.now() } : Object.assign(old, { d: 1, ts: Date.now() });
    var keys = Object.keys(DB.terms); if (keys.length > 800) keys.filter(function (x) { return DB.terms[x].d; }).sort(function (a, b) { return DB.terms[a].ts - DB.terms[b].ts; }).slice(0, keys.length - 800).forEach(function (x) { delete DB.terms[x]; });
    save();
  }
  function kwMergeTerms(a, b) {
    var bt = b && b.terms; if (!bt || typeof bt !== 'object') return;
    Object.keys(bt).forEach(function (k) { var y = bt[k], x = a.terms[k]; if (y && typeof y.t === 'string' && (!x || (y.ts || 0) > (x.ts || 0))) a.terms[k] = y; });
  }
  // v61: Wörter statt zusammengeklebter Buchstaben vergleichen, Füllwörter ignorieren, nur das aktuelle Fach
  var KW_STOP = {};
  ('der die das den dem des ein eine einer eines einem einen kein keine keiner keines keinem keinen zum zur vom im ins am ans beim ' +
   'von mit fuer auf aus an in bei bis durch ueber unter nach vor zu um ohne gegen seit zwischen hinter neben waehrend wegen pro je ' +
   'und oder aber sondern denn doch wenn dann falls dass weil da als wie ob so sowie bzw bzgl etc usw ca dh zb sog ' +
   'ist sind war waren sei seien wird werden wurde wurden worden hat haben hatte hatten gilt gelten gibt heisst nennt nennen ' +
   'kann koennen konnte muss muessen soll sollen darf duerfen will mag ' +
   'nicht nur auch noch schon sehr mehr weniger immer nie oft hier dort dabei damit dazu also alle allen aller alles jede jeder jedes jeden jedem ' +
   'man es er sie wir ihr ich du sich sein seine seiner seinen seinem ihre ihrer ihren ihrem ihm ihn uns euch dies diese dieser dieses diesen diesem ' +
   'welche welcher welches welchen welchem was wer wo wann warum wieso ja nein gleich genau etwa eher bzw').split(' ').forEach(function (w) { KW_STOP[w] = 1; });
  function kwToks(s) { return String(s || '').toLowerCase().replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss').normalize('NFD').replace(/[̀-ͯ]/g, '').split(/[^a-z0-9]+/).filter(Boolean); }
  // inhaltstragende Wortstämme eines Begriffs (leer = nur Füllwörter)
  function kwCore(t) { return kwToks(t).filter(function (w) { return w.length >= 3 && !KW_STOP[w] && !/^\d+$/.test(w); }).map(kwStem); }
  function kwHit(st, toks) { for (var i = 0; i < toks.length; i++) { var w = toks[i]; if (st.length >= 5 ? w.indexOf(st) >= 0 : w.indexOf(st) === 0) return true; } return false; }
  function kwGapFill(h) { return String(h || '').replace(/\{\{([^}]*)\}\}/g, function (_, x) { return '<b>' + x.split('|')[0] + '</b>'; }); }
  var KW_CARDS = null;
  function kwCards() {
    if (KW_CARDS) return KW_CARDS;
    var kws = {}, ikw = {}, seen = {}; KW_CARDS = [];
    SEARCH.forEach(function (e) { var m = /[?&]c=([^&]+)/.exec(e.route || ''); if (m) kws[m[1]] = e.kw || ''; m = /[?&]q=([^&]+)/.exec(e.route || ''); if (m) ikw[e.s + '|' + m[1]] = e.kw || ''; });
    function add(s, ch, c, q, a, kw, test) {
      var key = s.id + '|' + c.id; if (seen[key]) return; seen[key] = 1;
      var bold = '', bs = []; String(q).replace(/<b>([\s\S]*?)<\/b>/g, function (_, x) { bold += ' ' + x; bs.push(kwCore(kwTxt(x)).join(' ')); });
      KW_CARDS.push({ c: { id: c.id, q: q, a: a, src: c.src }, s: s.id, ch: ch, test: test, bs: bs, b: kwToks(kwTxt(bold)), f: kwToks(kwTxt(q)), k: kwToks(kw), a: kwToks(kwTxt(a)) });
    }
    C.subjects.forEach(function (s) {
      s.chapters.forEach(function (ch) {
        if (ch.placeholder) return;
        (ch.cards || []).forEach(function (c) { add(s, ch, c, c.q, c.a, kws[c.id] || '', 0); });
        // Ersatz aus den Tests (nur wenn keine Karte passt): Lösung + Erklärung als Antwortseite
        (ch.items || []).forEach(function (it) {
          var q = '', a = '', ex = it.expl ? '<p>' + it.expl + '</p>' : '';
          if (it.type === 'gap') { q = kwGapFill(it.text); a = ex; }
          else if (it.type === 'tf') { q = it.statement; a = '<p><b>' + (it.answer ? 'Richtig.' : 'Falsch.') + '</b></p>' + ex; }
          else if (it.type === 'mc' && it.options) {
            var ok = Array.isArray(it.correct) ? it.options.filter(function (o, n) { return it.correct.indexOf(n) >= 0; }) : [it.options[it.correct]];
            q = it.q; a = '<p><b>Lösung:</b> ' + ok.join(' · ') + '</p>' + ex;
          } else return;
          add(s, ch, it, q, a, ikw[s.id + '|' + it.id] || '', it.type === 'gap' ? 3 : it.type === 'mc' ? 2 : 1);
        });
      });
    });
    return KW_CARDS;
  }
  function kwFind(t, sid, skip) {
    var core = kwCore(t); if (!core.length) return [];
    var whole = core.join(' '), res = [];
    kwCards().forEach(function (x) {
      if (x.s !== sid || isHidden(x.s) || (skip && x.c.id === skip)) return;
      var sc = 0, front = 0;
      for (var i = 0; i < core.length; i++) {
        var st = core[i], v = (kwHit(st, x.b) ? 6 : 0) + (kwHit(st, x.f) ? 4 : 0) + (kwHit(st, x.k) ? 2 : 0), w = kwHit(st, x.a) ? 1 : 0;
        if (!v && !w) return; // jedes Wort des Begriffs muss vorkommen
        if (v) front++; sc += v + w;
      }
      if (x.bs.indexOf(whole) >= 0) sc += 5;
      res.push({ x: x, sc: sc, front: front === core.length });
    });
    var fr = res.filter(function (r) { return r.front; });
    if (fr.length) res = fr; else res = res.filter(function (r) { return core.every(function (st) { return st.length >= 5; }); });
    // Karteikarten haben Vorrang, Testfragen nur als Ersatz
    var cards = res.filter(function (r) { return !r.x.test; });
    if (cards.length) res = cards;
    res.sort(function (p, q) { return q.sc - p.sc || (q.x.test || 0) - (p.x.test || 0) || (p.x.f.length - q.x.f.length); });
    return res.slice(0, 4).map(function (r) { return r.x; });
  }
  function kwCardHTML(x, noQ) {
    var sn = subj(x.s) ? subj(x.s).name : '';
    return '<div class="kwcard"><div class="kwsrc">' + esc(sn + (x.c.src ? ' · ' + x.c.src : '') + (x.test ? ' · aus den Tests' : '')) + '</div>' + (noQ ? '' : '<div class="face kwq">' + x.c.q + '</div>') + '<div class="face kwa">' + x.c.a + '</div></div>';
  }
  // Fenster zu einem Begriff: passende Karte(n), „Auf die Liste“, „Erklärung fehlt“ (geht als Feedback raus)
  function kwShow(t, sid, ctx) {
    ctx = ctx || {};
    var found = kwFind(t, sid, ctx.list ? null : ctx.q), h = '';
    if (found.length) {
      h += kwCardHTML(found[0]);
      if (found.length > 1) h += '<p class="kwmore">Weitere Karten</p>' + found.slice(1).map(function (x) {
        return '<details class="faq"><summary><div class="face kwsum">' + x.c.q + '</div><svg class="chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></summary><div class="fa">' + kwCardHTML(x, 1) + '</div></details>';
      }).join('');
    } else h += '<p class="kwnone">Zu diesem Begriff gibt es noch keine Karte.</p>';
    h += '<div class="kwfoot">' + (ctx.list ? '<a class="linkbtn" href="#/suche?q=' + encodeURIComponent(t) + '">In der Suche öffnen</a>' : '') +
      '<button type="button" class="linkbtn" id="kwMiss">' + (found.length ? 'Passt nicht? Erklärung fehlt melden' : 'Erklärung fehlt melden') + '</button></div>';
    var on = kwHas(sid, t);
    openTile('„' + t + '“', h, '<div class="row"><button type="button" class="ghost pvok">Schließen</button><button type="button" class="' + (on ? 'ghost' : 'primary') + '" id="kwAdd">' + (on ? 'Entfernen' : 'Merken') + '</button></div>');
    $('#kwAdd').onclick = function () {
      var now = !kwHas(sid, t); kwSet(sid, t, now, ctx); closeTile();
      toast(now ? 'Auf deiner Liste „Meine Begriffe“' : 'Von der Liste genommen');
      if (ctx.done) ctx.done();
    };
    $('#kwMiss').onclick = function () {
      var b = this;
      fbQueue(fbQueue().concat([{ text: 'Erklärung fehlt · „' + t.slice(0, 80) + '“', ts: Date.now(), seite: ('Begriff ' + sid + ' · ' + (ctx.q || 'Liste')).slice(0, 80) }]));
      var x = DB.terms[kwKey(sid, t)]; if (x && !x.d) { x.m = 1; save(); }
      b.textContent = 'Gemeldet ✓'; b.disabled = true;
      if (navigator.onLine === false) { toast('Gespeichert · wird gesendet, sobald du online bist'); return; }
      fbFlush(function (ok) { toast(ok ? 'Danke, wir ergänzen die Erklärung' : 'Gerade keine Verbindung · wird später gesendet'); });
    };
  }
  // Wörter einer Frage antippbar machen (Formeln, Eingabefelder und Knöpfe der App bleiben außen vor)
  var KW_SKIP = 'math, .katex, input, textarea, svg, script, style, .kwbtn, .kwbar, .tchip, .meta, .k, .box';
  var KW_RE = /[\p{L}\p{N}][\p{L}\p{N}\-]*/gu, kwBlk = 0;
  function kwWrap(root) {
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), list = [], n;
    while ((n = w.nextNode())) { var pe = n.parentElement; if (!pe || pe.closest(KW_SKIP) || pe.classList.contains('kw') || !/[\p{L}\p{N}]/u.test(n.nodeValue)) continue; list.push(n); }
    list.forEach(function (n) {
      var blk = n.parentElement.closest('p, li, td, th, button, .tip, .face, .qtext, .stmt, div') || root;
      if (!blk.dataset.kwb) { blk.dataset.kwb = ++kwBlk; blk.dataset.kwn = 0; }
      var frag = document.createDocumentFragment(), s = n.nodeValue, last = 0, m; KW_RE.lastIndex = 0;
      while ((m = KW_RE.exec(s))) {
        if (m.index > last) frag.appendChild(document.createTextNode(s.slice(last, m.index)));
        var sp = document.createElement('span'); sp.className = 'kw'; sp.textContent = m[0]; sp.dataset.b = blk.dataset.kwb; sp.dataset.i = blk.dataset.kwn = +blk.dataset.kwn + 1;
        frag.appendChild(sp); last = m.index + m[0].length;
      }
      if (last < s.length) frag.appendChild(document.createTextNode(s.slice(last)));
      n.replaceWith(frag);
    });
  }
  function kwUnwrap(root) {
    $$('.kw', root).forEach(function (sp) { sp.replaceWith(document.createTextNode(sp.textContent)); });
    $$('[data-kwb]', root).forEach(function (b) { delete b.dataset.kwb; delete b.dataset.kwn; b.normalize(); });
    root.normalize();
  }
  // Knopf oben rechts in der Fragekarte; an = Wörter antippen, mehrere nebeneinander ergeben einen Begriff
  function kwAttach(card, it, sid) {
    if (!card) return;
    card.classList.add('haskw');
    var btn = document.createElement('button'); btn.type = 'button'; btn.className = 'kwbtn'; btn.setAttribute('aria-label', 'Begriff nachschlagen'); btn.setAttribute('aria-pressed', 'false'); btn.innerHTML = KW_IC;
    card.appendChild(btn);
    var on = false, sel = [], bar = null, mo = null;
    function phrase() {
      if (!sel.length) return '';
      var r = document.createRange(); r.setStartBefore(sel[0]); r.setEndAfter(sel[sel.length - 1]);
      return r.toString().replace(/\s+/g, ' ').trim().slice(0, 80);
    }
    function paint() {
      $$('.kw.sel', card).forEach(function (x) { x.classList.remove('sel'); });
      sel.forEach(function (x) { x.classList.add('sel'); });
      var t = phrase(), core = t ? kwCore(t).length : 0;
      bar.innerHTML = t && !core ? '<div class="kwt"><b>„' + esc(t) + '“</b><small>Allgemeines Wort · tippe den Fachbegriff daneben an</small></div><div class="kwacts"><button type="button" class="ghost" id="kwOff">Fertig</button></div>'
        : t ? '<div class="kwt"><b>„' + esc(t) + '“</b><small>' + (kwHas(sid, t) ? 'Auf deiner Liste' : 'Weitere Wörter daneben antippen für längere Begriffe') + '</small></div>' +
        '<div class="kwacts"><button type="button" class="ghost" id="kwListB">' + (kwHas(sid, t) ? 'Gemerkt ✓' : 'Merken') + '</button><button type="button" class="primary" id="kwExpl">Erklärung</button></div>'
        : '<div class="kwt"><b>Begriff antippen</b><small>Zum Nachschlagen oder Merken</small></div><div class="kwacts"><button type="button" class="ghost" id="kwOff">Fertig</button></div>';
      var o = $('#kwOff', bar); if (o) o.onclick = function () { set(false); };
      var l = $('#kwListB', bar); if (l) l.onclick = function () { var now = !kwHas(sid, t); kwSet(sid, t, now, { q: it.id, src: it.src }); toast(now ? 'Auf deiner Liste „Meine Begriffe“' : 'Von der Liste genommen'); paint(); };
      var e = $('#kwExpl', bar); if (e) e.onclick = function () { kwShow(t, sid, { q: it.id, src: it.src, done: paint }); };
    }
    function onTap(ev) {
      if (!on) return;
      var w = ev.target.closest && ev.target.closest('.kw');
      if (w && card.contains(w)) {
        ev.preventDefault(); ev.stopPropagation();
        var i = sel.indexOf(w), b = w.dataset.b, n = +w.dataset.i;
        if (i === 0 || (i > 0 && i === sel.length - 1)) sel.splice(i, 1);
        else if (i > 0) sel = [w];
        else if (sel.length && sel[0].dataset.b === b && n === +sel[0].dataset.i - 1) sel.unshift(w);
        else if (sel.length && sel[0].dataset.b === b && n === +sel[sel.length - 1].dataset.i + 1) sel.push(w);
        else sel = [w];
        paint(); return;
      }
      // im Begriffe-Modus nicht versehentlich antworten oder umdrehen
      if (ev.target.closest('.opt, .rfbtns button, #card, .stmt') && !ev.target.closest('.kwbtn')) { ev.preventDefault(); ev.stopPropagation(); }
    }
    function set(v) {
      on = v; sel = []; btn.classList.toggle('on', on); btn.setAttribute('aria-pressed', on ? 'true' : 'false'); card.classList.toggle('kwon', on);
      if (on) {
        kwWrap(card);
        bar = document.createElement('div'); bar.className = 'kwbar'; bar.setAttribute('role', 'region'); bar.setAttribute('aria-label', 'Begriff'); document.body.appendChild(bar); paint();
        mo = new MutationObserver(function () { mo.disconnect(); kwWrap(card); mo.observe(card, { childList: true, subtree: true }); }); mo.observe(card, { childList: true, subtree: true });
        document.addEventListener('click', onTap, true);
      } else {
        if (mo) mo.disconnect(); mo = null;
        if (bar) bar.remove(); bar = null;
        document.removeEventListener('click', onTap, true);
        kwUnwrap(card);
      }
    }
    btn.onclick = function (e) { e.stopPropagation(); set(!on); };
    onLeave(function () { if (on) set(false); });
  }
  // ====================================================================== Abkürzungen erklären (v63)
  // Gepunktet unterstrichen; Antippen zeigt oben die Langform. In Antwortknöpfen per langem Drücken.
  var AB_MATH = { 'DGL': 'Differentialgleichung', 'AWP': 'Anfangswertproblem', 'ZWS': 'Zwischenwertsatz', 'o. E.': 'ohne Einschränkung' };
  var AB_PSY = {
    'SV': 'Sprachverständnis', 'VRV': 'Visuell-räumliche Verarbeitung', 'FS': 'Fluides Schlussfolgern', 'AGD': 'Arbeitsgedächtnis', 'VG': 'Verarbeitungsgeschwindigkeit',
    'BZF': 'Buchstaben-Zahlen-Folgen', 'GF': 'Gemeinsamkeiten finden', 'KTT': 'Klassische Testtheorie', 'KT': 'Konzentrationstest', 'MT': 'Mosaik-Test',
    'IQ': 'Intelligenzquotient', 'SD': 'Standardabweichung', 'M': 'Mittelwert', 'PR': 'Prozentrang', 'KI': 'Konfidenzintervall', 'WP': 'Wertpunkte',
    'ADHS': 'Aufmerksamkeitsdefizit-/Hyperaktivitätsstörung', 'WISC': 'Wechsler Intelligence Scale for Children', 'HAWIK': 'Hamburg-Wechsler-Intelligenztest für Kinder',
    'PISA': 'Programme for International Student Assessment', 'TIMSS': 'Trends in International Mathematics and Science Study', 'IGLU': 'Internationale Grundschul-Lese-Untersuchung', 'VERA': 'Vergleichsarbeiten',
    'EPQ': 'Eysenck Personality Questionnaire', 'LPA': 'Lehrer-Persönlichkeits-Adjektivskalen', 'CHC': 'Cattell-Horn-Carroll-Modell',
    'EZ': 'eineiige Zwillinge', 'ZZ': 'zweieiige Zwillinge', 'LG': 'leibliche Geschwister', 'AG': 'Adoptivgeschwister', 'SA': 'starke Ablehnung', 'SZ': 'starke Zustimmung',
    'UCS': 'unkonditionierter Stimulus', 'UCR': 'unkonditionierte Reaktion', 'NS': 'neutraler Stimulus', 'CS': 'konditionierter Stimulus', 'CR': 'konditionierte Reaktion',
    'PEN': 'Psychotizismus, Extraversion, Neurotizismus', 'OCEAN': 'Offenheit, Gewissenhaftigkeit, Extraversion, Verträglichkeit, Neurotizismus',
    'NEO-FFI': 'NEO-Fünf-Faktoren-Inventar', '16PF': '16-Persönlichkeits-Faktoren-Test', 'MMPI': 'Minnesota Multiphasic Personality Inventory', 'TAT': 'Thematischer Apperzeptionstest',
    'EEG': 'Elektroenzephalografie', 'PET': 'Positronen-Emissions-Tomografie', 'DNA': 'Desoxyribonukleinsäure', 'DRK': 'Deutsches Rotes Kreuz'
  };
  var AB_ONLYEQ = { 'M': 1 };   // nur vor „=“ (M = 100), sonst zu mehrdeutig
  var AB_ALL = Object.assign({}, AB_MATH, AB_PSY); delete AB_ALL.M;
  var abRes = {};
  function abDict(sid) {
    var k = sid === 'psy' ? 'psy' : sid ? 'math' : 'all';
    if (!abRes[k]) {
      var d = k === 'psy' ? AB_PSY : k === 'math' ? AB_MATH : AB_ALL;
      var keys = Object.keys(d).sort(function (a, b) { return b.length - a.length; }).map(function (s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/ /g, '\\s?'); });
      abRes[k] = { d: d, re: new RegExp('(^|[^\\p{L}\\p{N}])(' + keys.join('|') + ')(?![\\p{L}\\p{N}])', 'gu') };
    }
    return abRes[k];
  }
  function abKey(d, s) { if (d[s]) return s; var t = s.replace(/\s+/g, ' '); if (d[t]) return t; t = s.replace(/\s+/g, ''); return Object.keys(d).filter(function (k) { return k.replace(/ /g, '') === t; })[0]; }
  var AB_SKIP = 'math, .katex, input, textarea, svg, script, style, a, button:not(.opt), .ab, .kwon, .meta, .tchip, .k, .kwbar, .abtip, .srcl';
  function abWrap(root, R) {
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), list = [], n;
    while ((n = w.nextNode())) { var pe = n.parentElement; if (!pe || pe.closest(AB_SKIP)) continue; R.re.lastIndex = 0; if (R.re.test(n.nodeValue)) list.push(n); }
    list.forEach(function (n) {
      var s = n.nodeValue, last = 0, m, frag = document.createDocumentFragment(), hit = false; R.re.lastIndex = 0;
      while ((m = R.re.exec(s))) {
        var st = m.index + m[1].length, k = abKey(R.d, m[2]);
        if (!k || (AB_ONLYEQ[k] && !/^\s*=/.test(s.slice(st + m[2].length)))) continue;
        if (st > last) frag.appendChild(document.createTextNode(s.slice(last, st)));
        var sp = document.createElement('span'); sp.className = 'ab'; sp.textContent = m[2]; sp.dataset.ab = k; sp.title = R.d[k];
        frag.appendChild(sp); last = st + m[2].length; hit = true;
      }
      if (!hit) return;
      if (last < s.length) frag.appendChild(document.createTextNode(s.slice(last)));
      n.replaceWith(frag);
    });
  }
  var abTip = null, abTm = 0, abCur = null;
  function abHide() { clearTimeout(abTm); if (abTip) abTip.remove(); abTip = null; if (abCur) abCur.classList.remove('on'); abCur = null; }
  function abShow(el) {
    var k = el.dataset.ab, l = el.title || AB_ALL[k] || AB_PSY[k]; if (!l) return;
    abHide(); abCur = el; el.classList.add('on');
    abTip = document.createElement('div'); abTip.className = 'abtip'; abTip.setAttribute('role', 'status');
    abTip.innerHTML = '<b>' + esc(k) + '</b> = ' + esc(l);
    abTip.onclick = abHide; document.body.appendChild(abTip);
    abTm = setTimeout(abHide, 5000);
  }
  function abScope() {
    var r = parseHash(), p = r.parts;
    if (p[0] === 'f' && p[1] && p[2] && p[2] !== 'u') return p[1];
    if (/^(mix|faellig|suche)$/.test(p[0] || '')) return '';
    if (p[0] === 'begriffe') return r.q.s || '';
    return null;
  }
  var abQ = 0, abMo = new MutationObserver(function () { if (!abQ) abQ = requestAnimationFrame(abRun); });
  function abRun() {
    abQ = 0;
    var sid = abScope(), roots = $$('.pvcard');
    if (sid !== null) roots.unshift(view);
    if (roots.length) { var R = abDict(sid || ''); abMo.disconnect(); roots.forEach(function (r) { abWrap(r, R); }); }
    abMo.observe(document.body, { childList: true, subtree: true });
  }
  abMo.observe(document.body, { childList: true, subtree: true });
  window.addEventListener('hashchange', abHide);
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('.ab');
    if (abLp) { abLp = false; if (a) { e.preventDefault(); e.stopPropagation(); return; } }
    if (!a) { if (abTip && !e.target.closest('.abtip')) abHide(); return; }
    if (a.closest('.kwon') || a.closest('button.opt')) return;   // Begriffe-Modus bzw. Antwortknopf: normal weiter
    e.preventDefault(); e.stopPropagation(); abShow(a);
  }, true);
  // langes Drücken (480 ms) bzw. Rechtsklick auf Abkürzungen in Antwortknöpfen
  var abLp = false, abLpT = 0, abX = 0, abY = 0;
  document.addEventListener('touchstart', function (e) {
    var a = e.target.closest && e.target.closest('button.opt .ab'); clearTimeout(abLpT); if (!a || a.closest('.kwon')) return;
    var t = e.touches[0]; abX = t.clientX; abY = t.clientY;
    abLpT = setTimeout(function () { abLp = true; if (navigator.vibrate) try { navigator.vibrate(12); } catch (x) {} abShow(a); }, 480);
  }, { passive: true });
  document.addEventListener('touchmove', function (e) { var t = e.touches[0]; if (Math.abs(t.clientX - abX) > 10 || Math.abs(t.clientY - abY) > 10) clearTimeout(abLpT); }, { passive: true });
  document.addEventListener('touchend', function () { clearTimeout(abLpT); }, { passive: true });
  document.addEventListener('contextmenu', function (e) { var a = e.target.closest && e.target.closest('button.opt .ab'); if (!a || a.closest('.kwon')) return; e.preventDefault(); abShow(a); });

  function kwRowHTML(href, n, sub, acc) {
    return '<a class="kwrow' + (acc ? ' acc' : '') + '" href="' + href + '"><span class="kwi">' + KW_IC + '</span><span class="kwrt"><b>Meine Begriffe</b><small>' + n + (n === 1 ? ' Begriff' : ' Begriffe') + ' zum Nachlernen' + (sub ? ' · ' + esc(sub) : '') + '</small></span>' + CHEV + '</a>';
  }
  function kwView(sid) {
    var s = sid && subj(sid); if (sid && !s) sid = '';
    var list = kwList(sid);
    var h = '<div class="nav">' + backLink(sid ? '#/f/' + sid : '#/', sid ? s.name : 'Start') + '</div><h1>Meine Begriffe</h1><p class="sub">' + esc(sid ? s.name : 'Alle Fächer') + '</p>';
    if (!list.length) h += '<div class="empty kwempty">Noch keine Begriffe. Tippe in einer Frage oben rechts auf <span class="kwi sm">' + KW_IC + '</span> und dann auf ein Wort, das du nicht kennst.</div>';
    else {
      h += '<p class="note" style="margin:0 0 12px">Antippen zeigt die Erklärung. Haken setzen, wenn du den Begriff kannst.</p><div class="group kwlist">';
      list.forEach(function (x, n) {
        h += '<div class="kwitem"><button type="button" class="kwopen" data-n="' + n + '"><b>' + esc(x.t) + '</b><small>' + esc((sid ? '' : subj(x.s).name + (x.src ? ' · ' : '')) + (x.src || '')) + (x.m ? ' · Erklärung gemeldet' : '') + '</small></button>' +
          '<button type="button" class="kwdone" data-n="' + n + '" aria-label="Gelernt, von der Liste nehmen">' + ic('check') + '</button></div>';
      });
      h += '</div>';
    }
    view.innerHTML = h;
    $$('.kwopen').forEach(function (b) { b.onclick = function () { var x = list[+b.dataset.n]; kwShow(x.t, x.s, { list: 1, q: x.q, src: x.src, done: function () { kwView(sid); } }); }; });
    $$('.kwdone').forEach(function (b) {
      b.onclick = function () {
        var x = list[+b.dataset.n]; kwSet(x.s, x.t, false); kwView(sid);
        toast('„' + x.t + '“ gelernt', 'Rückgängig', function () { kwSet(x.s, x.t, true, { q: x.q, src: x.src }); kwView(sid); });
      };
    });
  }
  function searchView(q0) {
    var filter = 'all';
    view.innerHTML = '<h1>Suche</h1><div class="searchbox" id="sbox"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>' +
      '<input id="q" type="search" placeholder="Begriff oder Satz suchen …" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="search" aria-label="Suche">' +
      '<button class="clear" id="clear" aria-label="Suche löschen">' + ic('x') + '</button></div><div id="res"></div>';
    var input = $('#q'), box = $('#sbox'); input.value = q0;
    function setLast(word, replaceAll) {
      var parts = input.value.replace(/\s+$/, '').split(/\s+/); if (replaceAll) parts = [word]; else parts[parts.length - 1] = word;
      input.value = parts.join(' ') + (replaceAll ? '' : ' '); render(); input.focus();
    }
    function render() {
      var q = input.value.trim(); box.classList.toggle('has', input.value.length > 0);
      lastQ = q || ''; try { history.replaceState(null, '', q ? '#/suche?q=' + encodeURIComponent(q) : '#/suche'); } catch (e) {}
      var res = $('#res');
      if (!q) {
        var h = '';
        if (DB.recent.length) h += '<div class="sughead"><span>Zuletzt gesucht</span><button id="clrRecent">Löschen</button></div>' + chips(DB.recent);
        h += '<div class="sughead"><span>Häufige Begriffe</span></div>' + chips(popular(5));
        res.innerHTML = h + '<p class="note" style="text-align:center;padding:22px 10px 0">Suche in allen Fächern: Definitionen, Sätze, Schlagwörter.</p>';
        wire(); return;
      }
      var toks = nrm(q).split(/\s+/).filter(Boolean), list = [];
      SEARCH.forEach(function (e, n) {
        if (isHidden(e.s)) return;
        var score = 0;
        for (var i = 0; i < toks.length; i++) { var inH = e._h.indexOf(toks[i]) >= 0, inT = e._t.indexOf(toks[i]) >= 0; if (!inH && !inT) return; score += (inH ? 3 : 0) + (inT ? 1 : 0); }
        list.push({ e: e, score: score, n: n });
      });
      list.sort(function (a, b) { return b.score - a.score || a.n - b.n; });
      // geteilte Einträge (Allgemein in mehreren Fächern) unter „Alle“ nur einmal
      var uniq = {}, listAll = list.filter(function (x) { var u = x.e.u; if (!u) return true; if (uniq[u]) return false; uniq[u] = 1; return true; });
      // Vorschläge: Wortende ergänzen, sonst Tippfehler korrigieren
      var sug = '', last = toks[toks.length - 1], typing = !/\s$/.test(input.value);
      var ps = typing && last.length >= 2 ? prefixSug(last) : [];
      if (ps.length) sug = chips(ps.map(function (v) { return v.w; }), '');
      else if (!list.length) {
        var bad = toks.filter(function (t) { return !SEARCH.some(function (e) { return e._h.indexOf(t) >= 0 || e._t.indexOf(t) >= 0; }); }), fz = bad.length ? fuzzySug(bad[bad.length - 1]) : [];
        if (fz.length) { sug = '<p class="sugnote">Meintest du:</p>' + chips(fz.map(function (v) { return v.w; }), 'ai'); sug = sug.replace(/class="sugchip ai"/g, 'class="sugchip ai" data-fix="' + esc(bad[bad.length - 1]) + '"'); }
      }
      var counts = { all: listAll.length }; list.forEach(function (x) { counts[x.e.s] = (counts[x.e.s] || 0) + 1; });
      var subs = C.subjects.filter(function (s) { return !isHidden(s.id) && SEARCH.some(function (e) { return e.s === s.id; }); });
      var f = '<div class="filters"><button data-f="all" class="' + (filter === 'all' ? 'on' : '') + '">Alle (' + counts.all + ')</button>' + subs.map(function (s) {
        return '<button data-f="' + s.id + '" class="' + (filter === s.id ? 'on' : '') + '"><span class="sw" style="background:var(--c-' + s.id + ')"></span>' + esc(s.name) + ' (' + (counts[s.id] || 0) + ')</button>';
      }).join('') + '</div>';
      var shown = filter === 'all' ? listAll : list.filter(function (x) { return x.e.s === filter; });
      var hl = encodeURIComponent(q);
      res.innerHTML = sug + f + (shown.length ? '<div class="count">' + shown.length + ' Treffer</div>' + shown.slice(0, 40).map(function (x) {
        var e = x.e, sj = subj(e.s), sep = e.route.indexOf('?') >= 0 ? '&' : '?';
        return '<a class="hit" style="--hc:var(--c-' + e.s + ')" href="#' + e.route + sep + 'hl=' + hl + '"><div class="top"><span class="subj">' + esc(sj.name) + '</span><span class="ttl">' + esc(e.title) + '</span><span class="typ">' + esc(e.label) + '</span></div><div class="snip">' + snippet(e.text, toks) + '</div></a>';
      }).join('') : '<div class="none">Keine Treffer für „' + esc(q) + '“.</div>');
      $$('.filters button', res).forEach(function (b) { b.onclick = function () { filter = b.dataset.f; render(); }; });
      $$('.hit', res).forEach(function (a) { a.addEventListener('click', function () { remember(q); }); });
      wire();
    }
    function wire() {
      $$('.sugchip', $('#res')).forEach(function (b) {
        b.onclick = function () {
          var w = b.dataset.w;
          if (b.dataset.fix) { var re = new RegExp(b.dataset.fix.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i'); var cur = input.value; var nv = cur.replace(new RegExp('\\S*$'), w); input.value = nv; render(); input.focus(); return; }
          var inRecent = DB.recent.indexOf(w) >= 0 && !input.value.trim(); setLast(w, !input.value.trim() || inRecent);
        };
      });
      var cr = $('#clrRecent'); if (cr) cr.onclick = function () { DB.recent = []; save(); render(); };
    }
    input.addEventListener('input', render);
    input.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); remember(input.value); input.blur(); } });
    $('#clear').onclick = function () { input.value = ''; render(); input.focus(); };
    render();
    if (!q0) setTimeout(function () { try { input.focus(); } catch (e) {} }, 50);
  }

  // ====================================================================== Verlauf
  var vRange = 'w', vSel = null;
  function allSubj() { return C.subjects.concat(OWN_ON && DB.log.some(function (e) { return e[1] === 'own'; }) ? [{ id: 'own', name: 'Eigene Karten' }] : []); }
  function verlaufView() {
    var now = new Date(), i, MON = ['Jan.', 'Feb.', 'März', 'Apr.', 'Mai', 'Juni', 'Juli', 'Aug.', 'Sept.', 'Okt.', 'Nov.', 'Dez.'];
    var WD = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'], WDL = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
    var today0 = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    // Einträge pro Tag: { fach: {n, s} }
    var map = {};
    DB.log.forEach(function (e) {
      var d = dayKey(e[0]), m = map[d] = map[d] || {}, f = m[e[1]] = m[e[1]] || { n: 0, s: 0, k: 0, p: 0, pm: 0 }; f.n++;
      if (typeof e[4] === 'number') { f.p += e[4]; f.pm += 4; } else { f.k++; f.s += (typeof e[3] === 'number' ? e[3] : 0); }
    });
    function dayData(d) { return map[dayKey(d.getTime())] || {}; }
    function total(c) { return Object.keys(c).reduce(function (a, k) { return a + c[k].n; }, 0); }
    function merge(list) { var r = {}; list.forEach(function (c) { Object.keys(c).forEach(function (k) { var f = r[k] = r[k] || { n: 0, s: 0, k: 0, p: 0, pm: 0 }; f.n += c[k].n; f.s += c[k].s; f.k += c[k].k; f.p += c[k].p; f.pm += c[k].pm; }); }); return r; }
    function dmy(d) { return d.getDate() + '. ' + MON[d.getMonth()]; }
    function build() {
      var out = [], d, c;
      if (vRange === 'j') {
        var dow = (today0.getDay() + 6) % 7, mon = new Date(today0.getFullYear(), today0.getMonth(), today0.getDate() - dow);
        for (i = 11; i >= 0; i--) {
          var st = new Date(mon.getFullYear(), mon.getMonth(), mon.getDate() - i * 7), en = new Date(st.getFullYear(), st.getMonth(), st.getDate() + 6), ds = [];
          for (var k = 0; k < 7; k++) ds.push(dayData(new Date(st.getFullYear(), st.getMonth(), st.getDate() + k)));
          out.push({ key: dayKey(st.getTime()), c: merge(ds), lab: i === 0 ? 'Jetzt' : (st.getDate() + '.' + (st.getMonth() + 1) + '.'), title: dmy(st) + ' – ' + dmy(en), sub: 'Woche', days: 7 });
        }
      } else {
        var N = vRange === 'm' ? 30 : 7;
        for (i = N - 1; i >= 0; i--) {
          d = new Date(today0.getFullYear(), today0.getMonth(), today0.getDate() - i); c = dayData(d);
          out.push({ key: dayKey(d.getTime()), c: c, lab: N > 7 ? ((d.getDate() % 5 === 0 && i > 1) ? String(d.getDate()) : '') : (i === 0 ? 'Heute' : WD[d.getDay()]), title: WDL[d.getDay()] + ', ' + dmy(d) + (i === 0 ? ' (heute)' : ''), sub: 'Tag', days: 1 });
        }
      }
      return out;
    }
    function streakOf() {
      var n = 0; for (i = 0; i < 400; i++) { var t = total(dayData(new Date(today0.getFullYear(), today0.getMonth(), today0.getDate() - i))); if (t > 0) n++; else if (i === 0) continue; else break; } return n;
    }
    function render() {
      var bs = build(), max = Math.max.apply(null, bs.map(function (x) { return total(x.c); }).concat([1]));
      var tod = total(dayData(today0)), wk = 0; for (i = 0; i < 7; i++) wk += total(dayData(new Date(today0.getFullYear(), today0.getMonth(), today0.getDate() - i)));
      var rng = bs.reduce(function (a, x) { return a + total(x.c); }, 0), days = vRange === 'w' ? 7 : vRange === 'm' ? 30 : 84;
      var sel = bs.filter(function (x) { return x.key === vSel; })[0];
      var subLine = { w: 'Beantwortete Fragen und Karten der letzten 7 Tage', m: 'Beantwortete Fragen und Karten der letzten 30 Tage', j: 'Beantwortete Fragen und Karten der letzten 12 Wochen' }[vRange];
      var h = '<h1>Verlauf</h1><p class="sub">' + subLine + '</p>' +
        '<div class="stats"><div class="stat"><b>' + tod + '</b><span>heute</span></div><div class="stat"><b>' + wk + '</b><span>7 Tage</span></div><div class="stat"><b>' + (DB.settings.mChain ? chainOf() : streakOf()) + '</b><span>' + (DB.settings.mChain ? 'Lerntage-Kette' : 'Tage in Folge') + '</span></div></div>' +
        '<div class="seg" id="vseg"><button data-r="w" class="' + (vRange === 'w' ? 'on' : '') + '">Woche</button><button data-r="m" class="' + (vRange === 'm' ? 'on' : '') + '">Monat</button><button data-r="j" class="' + (vRange === 'j' ? 'on' : '') + '">12 Wochen</button></div>';
      if (!DB.log.length) h += '<div class="note" style="text-align:center;padding:10px 6px 20px">Hier erscheint dein Verlauf, sobald du Karten oder Fragen beantwortest.</div>';
      h += '<div class="group" style="padding:12px 14px"><div class="chart' + (vRange === 'm' ? ' dense' : '') + '">' + bs.map(function (x) {
        var t = total(x.c), hh = Math.round(t / max * 108);
        var stack = allSubj().map(function (s) { var n = x.c[s.id] ? x.c[s.id].n : 0; return n ? '<i style="height:' + Math.max(3, Math.round(n / t * hh)) + 'px;background:var(--c-' + s.id + ')"></i>' : ''; }).join('');
        return '<button type="button" class="day' + (x.key === vSel ? ' sel' : '') + '" data-k="' + x.key + '" aria-label="' + esc(x.title) + ': ' + t + '"><div class="n">' + (vRange === 'm' ? '' : (t || '')) + '</div><div class="stack">' + stack + '</div><div class="lab">' + x.lab + '</div></button>';
      }).join('') + '</div><div class="legend">' + allSubj().map(function (s) { return '<span><i class="sw" style="background:var(--c-' + s.id + ')"></i>' + esc(s.name) + '</span>'; }).join('') + '</div></div>';
      if (sel) {
        var t2 = total(sel.c);
        h += '<div class="group daydet"><div class="dhead"><b>' + esc(sel.title) + '</b><span>' + (t2 ? t2 + (t2 === 1 ? ' Antwort' : ' Antworten') : 'nichts gelernt') + '</span></div>' +
          allSubj().filter(function (s) { return sel.c[s.id]; }).map(function (s) {
            var f = sel.c[s.id], parts = [];
            if (f.k) parts.push(Math.round(f.s / f.k * 100) + ' % gewusst/richtig');
            if (f.pm) parts.push('MC ' + f.p + '/' + f.pm + ' Punkte');
            return '<div class="drow"><i class="sw" style="background:var(--c-' + s.id + ')"></i><span class="nm">' + esc(s.name) + '</span><span class="ct">' + f.n + ' · ' + parts.join(' · ') + '</span></div>';
          }).join('') + '</div>';
      } else if (DB.log.length) h += '<p class="note" style="text-align:center">Tippe einen Balken an für Details.</p>';
      h += badgesHTML();
      h += '<p class="note" style="text-align:center">Gezählt wird jede beantwortete Karte und Testfrage. Im Zeitraum: ' + rng + ' in ' + days + ' Tagen.</p>';
      view.innerHTML = h;
      $$('#vseg button').forEach(function (b) { b.onclick = function () { vRange = b.dataset.r; vSel = null; render(); }; });
      $$('.chart .day').forEach(function (b) { b.onclick = function () { vSel = (vSel === b.dataset.k) ? null : b.dataset.k; render(); }; });
    }
    vSel = null; render();
  }

  // ====================================================================== Neu: eigene Ordner und Karten
  var GREEK = { alpha: 'α', beta: 'β', gamma: 'γ', delta: 'δ', epsilon: 'ε', varepsilon: 'ε', theta: 'θ', lambda: 'λ', mu: 'μ', pi: 'π', rho: 'ρ', sigma: 'σ', tau: 'τ', phi: 'φ', chi: 'χ', psi: 'ψ', omega: 'ω', eta: 'η', Delta: 'Δ', Sigma: 'Σ', Omega: 'Ω', Pi: 'Π', Phi: 'Φ', Gamma: 'Γ',
    infty: '∞', cdot: '·', times: '×', pm: '±', leq: '≤', le: '≤', geq: '≥', ge: '≥', neq: '≠', ne: '≠', approx: '≈', to: '→', rightarrow: '→', Rightarrow: '⇒', Leftrightarrow: '⇔', in: '∈', notin: '∉', subset: '⊂', subseteq: '⊆', cup: '∪', cap: '∩', emptyset: '∅',
    forall: '∀', exists: '∃', neg: '¬', land: '∧', lor: '∨', partial: '∂', sum: '∑', prod: '∏', int: '∫', mathbb: '' };
  var BIGOPS = { sum: 1, prod: 1, int: 1 };
  // Kleiner TeX-Teil (Hoch, Tief, Bruch, Wurzel, griechische Buchstaben) -> MathML
  function texToMathML(src) {
    var p = 0, n = src.length;
    function ws() { while (p < n && /\s/.test(src[p])) p++; }
    function group() { ws(); if (src[p] === '{') { p++; var r = seq('}'); if (src[p] === '}') p++; return '<mrow>' + r + '</mrow>'; } return atom(); }
    function atom() {
      ws(); if (p >= n) return '<mrow></mrow>'; var c = src[p];
      if (c === '{') return group();
      if (c === '\\') {
        p++; var m = /^[A-Za-z]+/.exec(src.slice(p)); if (!m) { var ch = src[p++] || ''; return '<mo>' + esc(ch) + '</mo>'; }
        var cmd = m[0]; p += cmd.length;
        if (cmd === 'frac') { var a = group(), b = group(); return '<mfrac>' + a + b + '</mfrac>'; }
        if (cmd === 'sqrt') { return '<msqrt>' + group() + '</msqrt>'; }
        if (cmd === 'mathbb') { ws(); var L = src[p] === '{' ? (function () { p++; var e = src.indexOf('}', p); if (e < 0) e = n; var t = src.slice(p, e); p = Math.min(e + 1, n); return t; })() : (src[p++] || ''); var M = { N: 'ℕ', Z: 'ℤ', Q: 'ℚ', R: 'ℝ', C: 'ℂ' }; return '<mi>' + (M[L] || esc(L)) + '</mi>'; }
        if (cmd === 'lim') return '<mi>lim</mi>';
        if (GREEK[cmd] !== undefined) { return BIGOPS[cmd] ? '<mo largeop="true">' + GREEK[cmd] + '</mo>' : (/[a-zΑ-ω]/.test(GREEK[cmd]) && !/[∞]/.test(GREEK[cmd]) ? '<mi>' + GREEK[cmd] + '</mi>' : '<mo>' + GREEK[cmd] + '</mo>'); }
        return '<mtext>\\' + esc(cmd) + '</mtext>';
      }
      if (/[0-9.]/.test(c)) { var d = /^[0-9]*\.?[0-9]+|^[0-9]+/.exec(src.slice(p)); var t = d ? d[0] : c; p += t.length; return '<mn>' + t + '</mn>'; }
      if (/[A-Za-zÄÖÜäöüß]/.test(c)) { p++; return '<mi>' + esc(c) + '</mi>'; }
      p++; return '<mo>' + esc(c) + '</mo>';
    }
    function seq(stop) {
      var out = '';
      while (p < n && src[p] !== stop) {
        ws(); if (p >= n || src[p] === stop) break;
        var base = atom(), sub = null, sup = null;
        for (;;) { ws(); if (src[p] === '^' && sup === null) { p++; sup = group(); } else if (src[p] === '_' && sub === null) { p++; sub = group(); } else break; }
        out += sub !== null && sup !== null ? '<msubsup>' + base + sub + sup + '</msubsup>' : sup !== null ? '<msup>' + base + sup + '</msup>' : sub !== null ? '<msub>' + base + sub + '</msub>' : base;
      }
      return out;
    }
    return '<math>' + seq(null) + '</math>';
  }
  // Text mit $…$ -> HTML (Zeilenumbrüche bleiben erhalten)
  function rich(text) {
    return String(text || '').split(/(\$[^$]+\$)/).map(function (part) {
      if (part.length > 2 && part[0] === '$' && part[part.length - 1] === '$') return texToMathML(part.slice(1, -1));
      return esc(part).replace(/\n/g, '<br>');
    }).join('');
  }
  var TILES = [
    { id: 'gr', name: 'Griechisch', t: ['α', 'β', 'γ', 'δ', 'ε', 'θ', 'λ', 'μ', 'π', 'ρ', 'σ', 'τ', 'φ', 'χ', 'ω', 'Δ', 'Σ', 'Ω'] },
    { id: 'lo', name: 'Logik', t: ['∀', '∃', '¬', '∧', '∨', '⇒', '⇔', '→', '∴', '≡'] },
    { id: 'me', name: 'Mengen', t: ['∈', '∉', '⊂', '⊆', '∪', '∩', '∅', '∖', 'ℕ', 'ℤ', 'ℚ', 'ℝ', 'ℂ'] },
    { id: 'an', name: 'Analysis', t: ['∞', '∑', '∏', '∫', '∂', '≤', '≥', '≠', '≈', '±', '√', '·', '×', '|x|', 'lim'] },
    { id: 'hb', name: 'Hoch/Tief/Bruch', t: [{ l: 'x²', v: '$x^{|}$' }, { l: 'xₙ', v: '$x_{|}$' }, { l: 'a⁄b', v: '$\\frac{|}{}$' }, { l: '√x', v: '$\\sqrt{|}$' }, { l: 'xₙ²', v: '$x_{|}^{}$' }, { l: '$…$', v: '$|$' }] },
    { id: 'ps', name: 'Psycho 2', t: ['χ²', 'η²', 'ρ', 'r', 'σ', 'μ', 'M', 'SD', 'α', 'β', 'p', 'n', '≤', '≥', '≠', '±', '≈', 'Σ'] }
  ];
  function ownFolder(id) { return DB.custom.folders.filter(function (f) { return f.id === id; })[0]; }
  function newId(pre) { return pre + '-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 5); }
  function ownCards(f) { return f.cards.map(function (c) { return { id: c.id, q: rich(c.q), a: rich(c.a), red: false, src: f.name, _s: 'own' }; }); }
  function neuView(fid, sub) {
    if (fid) {
      var f = ownFolder(fid); if (!f) { location.hash = '#/neu'; return; }
      if (sub === 'ueben') {
        if (!f.cards.length) { location.hash = '#/neu/' + fid; return; }
        view.className = 's-own';
        return cardsView({ id: 'own', own: true, name: f.name, href: '#/neu/' + fid, desc: '', chapters: [] }, { id: fid, kind: 'cards', title: f.name, sub: 'Eigene Karten', cards: ownCards(f) }, {});
      }
      return folderView(f);
    }
    var h = '<h1>Neu</h1><p class="sub">Eigene Karten und Ordner</p>';
    if (DB.custom.folders.length) {
      h += '<div class="grid">' + DB.custom.folders.map(function (f) {
        var k = f.cards.filter(function (c) { return DB.progress[c.id] === 'known'; }).length;
        return '<a class="tile s-own" href="#/neu/' + f.id + '"><div><h2 class="name">' + esc(f.name) + '</h2><p class="desc">Eigene Karten</p></div><div class="foot"><span>' + (f.cards.length ? (k ? k + ' von ' + f.cards.length + ' gewusst' : f.cards.length + ' Karten') : 'Noch leer') +
          '</span><div class="bar"><div style="width:' + (f.cards.length ? k / f.cards.length * 100 : 0) + '%"></div></div><span class="go">Öffnen</span></div></a>';
      }).join('') + '</div>';
    } else h += '<div class="note" style="text-align:center;padding:8px 6px 18px">Noch keine eigenen Ordner. Lege einen an und schreib deine Karten selbst, mit Symbolen und Formeln.</div>';
    h += backupHint();
    h += '<div class="group" style="padding:14px 16px;margin-top:16px"><b>Neuer Ordner</b><div class="newrow"><input class="txt wide" id="fname" type="text" maxlength="40" placeholder="Name, z. B. Analysis Formeln" autocomplete="off"><button class="actbtn" id="fadd">Anlegen</button></div></div>';
    view.innerHTML = h; bindBackupHint();
    function add() {
      var name = $('#fname').value.trim().replace(/\s+/g, ' '); if (!name) { toast('Bitte einen Namen eingeben'); return; }
      var f = { id: newId('o'), name: name, cards: [] }; DB.custom.folders.push(f); ownTouch(); save(); location.hash = '#/neu/' + f.id;
    }
    $('#fadd').onclick = add; $('#fname').addEventListener('keydown', function (e) { if (e.key === 'Enter') add(); });
  }
  function folderView(f) {
    var editId = null, cat = 'gr', last = 'q', importOpen = false;
    function draw() {
      var ed = editId ? f.cards.filter(function (c) { return c.id === editId; })[0] : null;
      var tiles = TILES.filter(function (t) { return t.id === cat; })[0];
      var h = '<div class="nav">' + backLink('#/neu', 'Eigene Karten') + '</div><h1 style="font-size:1.55rem">' + esc(f.name) + '</h1><p class="sub">' + f.cards.length + (f.cards.length === 1 ? ' Karte' : ' Karten') + '</p>';
      if (f.cards.length) h += '<div class="row"><button class="primary" id="learn">Üben (' + f.cards.length + ')</button></div>';
      h += '<div class="group ed" style="padding:14px 16px;margin-top:14px"><b>' + (ed ? 'Karte bearbeiten' : 'Neue Karte') + '</b>' +
        '<label class="edl">Frage</label><textarea class="edt" id="qIn" rows="3" placeholder="Frage …">' + esc(ed ? ed.q : '') + '</textarea>' +
        '<label class="edl">Antwort</label><textarea class="edt" id="aIn" rows="3" placeholder="Antwort …">' + esc(ed ? ed.a : '') + '</textarea>' +
        '<div class="chips tilecats">' + TILES.map(function (t) { return '<button type="button" class="chip' + (t.id === cat ? ' on' : '') + '" data-cat="' + t.id + '">' + t.name + '</button>'; }).join('') + '</div>' +
        '<div class="tilegrid">' + tiles.t.map(function (x, i) { var l = typeof x === 'string' ? x : x.l; return '<button type="button" class="symtile" data-i="' + i + '">' + esc(l) + '</button>'; }).join('') + '</div>' +
        '<div class="prev"><span class="edl">Vorschau</span><div class="pv" id="pvQ"></div><div class="pv a" id="pvA"></div></div>' +
        '<p class="note" style="margin:8px 0 0">Formeln zwischen $ … $ schreiben, z. B. <code>$x^{2}$</code>, <code>$a_{n}$</code>, <code>$\\frac{a}{b}$</code>, <code>$\\sqrt{x}$</code>.</p>' +
        '<div class="row" style="margin-top:12px">' + (ed ? '<button class="ghost" id="ecancel">Abbrechen</button>' : '') + '<button class="primary" id="esave">' + (ed ? 'Speichern' : 'Karte hinzufügen') + '</button></div></div>';
      if (f.cards.length) {
        h += '<div class="group" style="padding:2px 16px;margin-top:14px">' + f.cards.map(function (c, i) {
          return '<div class="ownrow"><div class="ot"><span class="oq">' + rich(c.q) + '</span></div><span class="oa">' + (DB.progress[c.id] === 'known' ? '✓' : '') + '</span>' +
            '<button class="actbtn" data-edit="' + c.id + '">Bearbeiten</button><button class="actbtn danger" data-del="' + c.id + '">Löschen</button></div>';
        }).join('') + '</div>';
      }
      h += backupHint();
      h += '<div class="tools"><button id="imp">' + (importOpen ? 'Einfügen schließen' : 'Mehrere Karten einfügen') + '</button><button id="fren">Ordner umbenennen</button><button id="fdel">Ordner löschen</button></div>';
      if (importOpen) h += '<div class="group" style="padding:12px 16px"><b>Mehrere Karten einfügen</b><p class="note" style="margin:4px 0 0">Eine Karte pro Zeile: <code>Frage ; Antwort</code></p><textarea class="imp" id="impTx" placeholder="Was ist 2+2 ; 4"></textarea><div id="impInfo" class="note"></div><div class="row"><button class="primary" id="impGo">Importieren</button></div></div>';
      var scr = window.scrollY, hadFocus = document.activeElement && document.activeElement.id;
      view.innerHTML = h; window.scrollTo(0, scr); bindBackupHint();
      var q = $('#qIn'), a = $('#aIn');
      function prev() { $('#pvQ').innerHTML = q.value.trim() ? '<b>F:</b> ' + rich(q.value) : ''; $('#pvA').innerHTML = a.value.trim() ? '<b>A:</b> ' + rich(a.value) : ''; }
      q.addEventListener('focus', function () { last = 'q'; }); a.addEventListener('focus', function () { last = 'a'; });
      q.addEventListener('input', prev); a.addEventListener('input', prev); prev();
      $$('[data-cat]').forEach(function (b) { b.onclick = function () { var sq = q.value, sa = a.value; cat = b.dataset.cat; draft = { q: sq, a: sa }; draw(); }; });
      $$('.symtile').forEach(function (b) {
        b.onmousedown = function (e) { e.preventDefault(); };
        b.onclick = function () {
          var x = tiles.t[+b.dataset.i], v = typeof x === 'string' ? x : x.v, el = last === 'a' ? a : q, caret = v.indexOf('|');
          if (caret >= 0) v = v.replace('|', ''); else caret = v.length;
          var s0 = el.selectionStart === undefined ? el.value.length : el.selectionStart, s1 = el.selectionEnd === undefined ? s0 : el.selectionEnd;
          el.value = el.value.slice(0, s0) + v + el.value.slice(s1); el.focus(); var pos = s0 + caret; el.setSelectionRange(pos, pos); prev();
        };
      });
      if (draft && !ed) { q.value = draft.q; a.value = draft.a; prev(); } else if (draft && ed) { q.value = draft.q; a.value = draft.a; prev(); }
      draft = null;
      var ls = $('#learn'); if (ls) ls.onclick = function () { location.hash = '#/neu/' + f.id + '/ueben'; };
      $('#esave').onclick = function () {
        var qv = q.value.trim(), av = a.value.trim(); if (!qv || !av) { toast('Frage und Antwort ausfüllen'); return; }
        if (ed) { ed.q = qv; ed.a = av; toast('Gespeichert'); } else f.cards.push({ id: newId('oc'), q: qv, a: av, ts: Date.now() });
        editId = null; ownTouch(); save(); draw(); if (!ed) { window.scrollTo(0, scr); $('#qIn').focus({ preventScroll: true }); ownFirstTip(); }
      };
      var ec = $('#ecancel'); if (ec) ec.onclick = function () { editId = null; draw(); };
      $$('[data-edit]').forEach(function (b) { b.onclick = function () { editId = b.dataset.edit; draw(); window.scrollTo(0, 0); }; });
      $$('[data-del]').forEach(function (b) {
        b.onclick = function () {
          if (!b.dataset.sure) { b.dataset.sure = 1; b.textContent = 'Wirklich?'; setTimeout(function () { if (b.isConnected) { b.textContent = 'Löschen'; delete b.dataset.sure; } }, 3000); return; }
          var id = b.dataset.del; f.cards = f.cards.filter(function (c) { return c.id !== id; }); delete DB.progress[id]; ownTouch(); save(); draw();
        };
      });
      $('#imp').onclick = function () { importOpen = !importOpen; draw(); };
      $('#fren').onclick = function () { var n = prompt('Neuer Name für den Ordner', f.name); if (n && n.trim()) { f.name = n.trim().slice(0, 40); ownTouch(); save(); draw(); } };
      $('#fdel').onclick = function () {
        var b = $('#fdel'); if (!b.dataset.sure) { b.dataset.sure = 1; b.textContent = 'Wirklich löschen?'; return; }
        DB.custom.folders = DB.custom.folders.filter(function (x) { return x.id !== f.id; }); f.cards.forEach(function (c) { delete DB.progress[c.id]; }); ownTouch(); save(); location.hash = '#/neu'; toast('Ordner gelöscht');
      };
      if (importOpen) {
        var tx = $('#impTx');
        function parse() { return tx.value.split('\n').map(function (l) { var i = l.indexOf(';'); return i < 0 ? null : { q: l.slice(0, i).trim(), a: l.slice(i + 1).trim() }; }).filter(function (c) { return c && c.q && c.a; }); }
        tx.addEventListener('input', function () { var n = parse().length; $('#impInfo').textContent = n ? n + ' Karten erkannt' : ''; });
        $('#impGo').onclick = function () {
          var list = parse(); if (!list.length) { toast('Keine Karten erkannt. Format: Frage ; Antwort'); return; }
          list.forEach(function (c) { f.cards.push({ id: newId('oc'), q: c.q, a: c.a, ts: Date.now() }); }); ownTouch(); save(); importOpen = false; draw(); toast(list.length + ' Karten hinzugefügt'); ownFirstTip();
        };
      }
    }
    var draft = null;
    draw();
  }

  // ====================================================================== Einstellungen
  function segHTML(key, opts, val) {
    return '<div class="seg small" data-k="' + key + '">' + opts.map(function (o) { return '<button data-v="' + o[0] + '" class="' + (String(val) === String(o[0]) ? 'on' : '') + '">' + o[1] + '</button>'; }).join('') + '</div>';
  }
  function exportText() {
    var d = JSON.parse(JSON.stringify(DB)); d.settings.ownDirty = 0; d.settings.lastBackup = Date.now();
    return JSON.stringify({ app: 'lernkiste', v: 1, exported: new Date().toISOString(), data: d });
  }
  function shareFile() {
    var txt = exportText(), name = 'lernkiste-backup-' + dayKey(Date.now()) + '.json', blob = new Blob([txt], { type: 'application/json' }), file = null;
    try { file = new File([blob], name, { type: 'application/json' }); } catch (e) {}
    if (file && navigator.canShare && navigator.canShare({ files: [file] })) navigator.share({ files: [file], title: 'Lernkiste Backup' }).then(backupMarked, function () {});
    else { var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name; document.body.appendChild(a); a.click(); setTimeout(function () { a.remove(); URL.revokeObjectURL(a.href); }, 1000); backupMarked(); toast('Backup gespeichert'); }
  }
  function copyText() {
    var txt = exportText();
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(function () { backupMarked(); toast('Backup kopiert'); }, function () { toast('Kopieren nicht möglich'); });
    else { var ta = document.createElement('textarea'); ta.value = txt; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); backupMarked(); toast('Backup kopiert'); } catch (e) { toast('Kopieren nicht möglich'); } ta.remove(); }
  }
  function mergeInto(a, b) {
    Object.assign(a.progress, b.progress || {});
    Object.keys(b.badges || {}).forEach(function (k) { if (!a.badges[k] || b.badges[k] < a.badges[k]) a.badges[k] = b.badges[k]; });
    Object.keys(b.tests || {}).forEach(function (k) {
      var x = a.tests[k] = a.tests[k] || { best: {}, wrong: [] }, y = b.tests[k]; x.best = x.best || {}; x.wrong = x.wrong || [];
      Object.keys(y.best || {}).forEach(function (m) { if (x.best[m] === undefined || y.best[m] > x.best[m]) x.best[m] = y.best[m]; });
      (y.wrong || []).forEach(function (id) { if (x.wrong.indexOf(id) < 0) x.wrong.push(id); });
      if (y.rs && (!x.rs || (y.ts || 0) > (x.ts || 0))) x.rs = y.rs;
    });
    var seen = {}; a.log.forEach(function (e) { seen[e[0] + '|' + e[2]] = 1; });
    (b.log || []).forEach(function (e) { if (!seen[e[0] + '|' + e[2]]) a.log.push(e); });
    a.log.sort(function (p, q) { return p[0] - q[0]; });
    (b.recent || []).forEach(function (r) { if (a.recent.indexOf(r) < 0) a.recent.push(r); }); a.recent = a.recent.slice(0, 8);
    (b.hidden || []).forEach(function (id) { if (a.hidden.indexOf(id) < 0) a.hidden.push(id); });
    (b.custom && b.custom.folders || []).forEach(function (bf) {
      var af = a.custom.folders.filter(function (x) { return x.id === bf.id; })[0];
      if (!af) { a.custom.folders.push(bf); return; }
      bf.cards.forEach(function (c) { if (!af.cards.some(function (x) { return x.id === c.id; })) af.cards.push(c); });
    });
    kwMergeTerms(a, b);
    if (b.settings) a.settings = Object.assign(a.settings, b.settings);
  }
  // Fremde Backups säubern: Namen, IDs, Einstellungen ohne HTML-Zeichen; Kartentexte werden beim Anzeigen ohnehin maskiert (rich).
  function cleanImport(o, qa) {
    if (typeof o === 'string') return qa ? o.slice(0, 5000) : o.replace(/[<>"'`]/g, '').slice(0, 300);
    if (typeof o === 'number') return isFinite(o) ? o : 0;
    if (typeof o === 'boolean' || o === null) return o;
    if (Array.isArray(o)) return o.slice(0, 50000).map(function (x) { return cleanImport(x, qa); });
    if (typeof o === 'object') { var r = {}; Object.keys(o).forEach(function (k) { if (k === '__proto__' || k === 'constructor' || k === 'prototype') return; r[k.replace(/[<>"'`]/g, '')] = cleanImport(o[k], k === 'q' || k === 'a'); }); return r; }
    return null;
  }
  // ====================================================================== Sync (v49): Sync-Code ohne Konto, Supabase-Tabelle lernkiste_sync
  var SB_URL = 'https://qbdpzamygonpruaafcrt.supabase.co', SB_KEY = 'sb_publishable_A7zukzk82Suux8jteQvLGA_WmXnZb14', SYNC_KEY = 'lernkiste-sync';
  // bleibt auf dem Gerät: Name (personenbezogen), Statistik-Zustimmung, Backup-Merker
  var SYNC_LOCAL = { st65: 1, obDone: 1, name: 1, stats: 1, statsAsked: 1, lastBackup: 1, ownDirty: 1, ownTip: 1, nagDay: 1, ui44: 1 };
  var SYNC_ABC = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';
  var syncApplying = false, syncBusy = false, syncAgain = false, syncTimer = 0, syncErr = false;
  function syncCfg() { var o = rd(SYNC_KEY); return o && typeof o.code === 'string' && o.code.length === 20 ? o : null; }
  function syncSetCfg(o) { try { if (o) localStorage.setItem(SYNC_KEY, JSON.stringify(o)); else localStorage.removeItem(SYNC_KEY); } catch (e) {} }
  function syncNewCode() { var b = new Uint8Array(20), c = ''; crypto.getRandomValues(b); for (var i = 0; i < 20; i++) c += SYNC_ABC[b[i] % SYNC_ABC.length]; return c; }
  function syncFmt(c) { return c.replace(/(.{4})(?=.)/g, '$1-'); }
  function syncNorm(t) { return String(t || '').toUpperCase().replace(/[^A-Z0-9]/g, ''); }
  function sbRpc(fn, body) {
    return fetch(SB_URL + '/rest/v1/rpc/' + fn, { method: 'POST', headers: { apikey: SB_KEY, 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
      .then(function (r) { if (!r.ok) throw new Error('http ' + r.status); return r.text(); })
      .then(function (t) { return t ? JSON.parse(t) : null; });
  }
  function syncMark() {
    var c = syncCfg(); if (!c) return;
    if (!c.dirty) { c.dirty = Date.now(); syncSetCfg(c); }
    clearTimeout(syncTimer); syncTimer = setTimeout(syncNow, 15000);
  }
  function syncPayload() {
    var o = {}; Object.keys(DB).forEach(function (k) { if (k !== 'custom' && k !== 'recent') o[k] = DB[k]; });
    var st = {}; Object.keys(DB.settings).forEach(function (k) { if (!SYNC_LOCAL[k]) st[k] = DB.settings[k]; }); o.settings = st;
    return o;
  }
  // Abgleich: pro Karte gewinnt die neuere Bewertung, pro Test der neuere Stand, Verlauf wird vereinigt. Zurücksetzen/Löschen gilt überall.
  function syncMerge(a, raw) {
    var b = normalizeDB(cleanImport(raw)), R = Math.max(a.resetAt || 0, b.resetAt || 0), L = Math.max(a.logClr || 0, b.logClr || 0);
    var at = a.ptime = a.ptime || {}, bt = b.ptime || {}, ids = {};
    [a.progress, at, b.progress, bt].forEach(function (o) { Object.keys(o).forEach(function (k) { ids[k] = 1; }); });
    Object.keys(ids).forEach(function (id) {
      var ta = at[id] || 0, tb = bt[id] || 0, v = tb > ta ? b.progress[id] : ta > tb ? a.progress[id] : (a.progress[id] || b.progress[id]), t = Math.max(ta, tb);
      if (R && t < R) { v = undefined; t = 0; }
      if (v === 'known' || v === 'again') a.progress[id] = v; else delete a.progress[id];
      if (t) at[id] = t; else delete at[id];
    });
    var tk = {}; Object.keys(a.tests).concat(Object.keys(b.tests)).forEach(function (k) { tk[k] = 1; });
    Object.keys(tk).forEach(function (k) {
      var x = a.tests[k], y = b.tests[k];
      if (y && (!x || (y.ts || 0) > (x.ts || 0))) a.tests[k] = x = { best: y.best || {}, wrong: (y.wrong || []).slice(), ts: y.ts || 0, moved: y.moved, saved: y.saved, rs: y.rs };
      else if (x && y && !x.ts && !y.ts) {
        x.best = x.best || {}; x.wrong = x.wrong || [];
        Object.keys(y.best || {}).forEach(function (m) { if (x.best[m] === undefined || y.best[m] > x.best[m]) x.best[m] = y.best[m]; });
        (y.wrong || []).forEach(function (w) { if (x.wrong.indexOf(w) < 0) x.wrong.push(w); });
      }
      if (R && (x.ts || 0) < R && !x.moved) delete a.tests[k];
    });
    var seen = {}, log = [];
    a.log.concat(b.log).forEach(function (e) { if (!Array.isArray(e) || e[0] < L) return; var key = e[0] + '|' + e[2]; if (seen[key]) return; seen[key] = 1; log.push(e); });
    log.sort(function (p, q) { return p[0] - q[0]; }); if (log.length > 20000) log.splice(0, log.length - 20000); a.log = log;
    Object.keys(b.badges).forEach(function (k) { if (!a.badges[k] || b.badges[k] < a.badges[k]) a.badges[k] = b.badges[k]; });
    if ((b.hiddenTs || 0) > (a.hiddenTs || 0)) { a.hidden = b.hidden.slice(); a.hiddenTs = b.hiddenTs; }
    if (raw.settings && (raw.settings._ts || 0) > (a.settings._ts || 0)) Object.keys(raw.settings).forEach(function (k) { if (!SYNC_LOCAL[k] && DEFAULTS.hasOwnProperty(k) || k === '_ts') a.settings[k] = b.settings[k]; });
    kwMergeTerms(a, b);
    if (R) a.resetAt = R; if (L) a.logClr = L;
  }
  function syncNow() {
    var c = syncCfg(); clearTimeout(syncTimer);
    if (!c || navigator.onLine === false) return Promise.resolve(false);
    if (syncBusy) { syncAgain = true; return Promise.resolve(false); }
    syncBusy = true;
    var stamp = c.dirty || 0, changed = false;
    return sbRpc('lk_get', { p_code: c.code }).then(function (r) {
      var remote = r && r.data;
      if (remote && typeof remote === 'object' && !Array.isArray(remote)) {
        var before = JSON.stringify(DB); syncMerge(DB, remote); changed = JSON.stringify(DB) !== before;
        if (changed) { syncApplying = true; save(); syncApplying = false; }
      }
      if (remote && !stamp) return null;
      return sbRpc('lk_put', { p_code: c.code, p_data: syncPayload() });
    }).then(function () {
      var n = syncCfg(); if (n && n.code === c.code) { if ((n.dirty || 0) === stamp) n.dirty = 0; n.last = Date.now(); syncSetCfg(n); }
      syncErr = false; if (changed) syncRefresh(); else syncStatusUI(); return true;
    }).catch(function () { syncErr = true; syncStatusUI(); return false; })
      .then(function (ok) { syncBusy = false; if (syncAgain) { syncAgain = false; setTimeout(syncNow, 500); } return ok; });
  }
  function syncRefresh() {
    if (document.body.classList.contains('immersive') || tileEl) return;
    var a = document.activeElement; if (a && (a.tagName === 'INPUT' || a.tagName === 'TEXTAREA')) { syncStatusUI(); return; }
    var y = window.scrollY; route(); window.scrollTo(0, y);
  }
  function syncWhen(t) {
    if (!t) return 'Noch nicht abgeglichen';
    var d = new Date(t), hm = d.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' });
    return 'Zuletzt abgeglichen ' + (dayKey(t) === dayKey(Date.now()) ? 'heute, ' + hm : d.toLocaleDateString('de-DE') + ', ' + hm);
  }
  function syncStatusText() { var c = syncCfg(); if (!c) return ''; return syncErr ? 'Gerade keine Verbindung · wird später erneut versucht' : syncWhen(c.last); }
  function syncStatusUI() { var e = $('#syncStat'); if (e) e.textContent = syncStatusText(); }
  var openSec = {};
  var SETIC = {
    learn: '<svg viewBox="0 0 24 24"><rect x="3" y="7" width="14" height="13" rx="2"/><path d="M7 4h12a2 2 0 0 1 2 2v11"/></svg>',
    motiv: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
    data: '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg>',
    fb: '<svg viewBox="0 0 24 24"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>',
    help: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.1 9a3 3 0 0 1 5.8 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>'
  };
  // v60: App teilen – QR-Code (qr.svg, offline im Cache), Link kopieren, Teilen-Menü des Systems
  var SHARE_URL = 'https://konstismile.github.io/Diff-1-Lernkarten/';
  var SHARE_TXT = 'Lernkiste: Karteikarten und Klausurfragen für Diff 1, Querschnitt und Psycho 2. Kostenlos, offline, ohne Konto.';
  function shareApp() {
    var canShare = !!navigator.share;
    openTile('App teilen',
      '<div class="qrbox"><img src="qr.svg" alt="QR-Code zur Lernkiste" width="220" height="220"></div>' +
      '<p class="sharelead">Lass den Code abfotografieren oder schick den Link.</p>' +
      '<div class="sharelink" id="shLink">' + esc(SHARE_URL.replace(/^https:\/\//, '').replace(/\/$/, '')) + '</div>',
      '<div class="row"><button type="button" class="ghost" id="shCopy">Link kopieren</button>' + (canShare ? '<button type="button" class="primary" id="shGo">Teilen …</button>' : '<button type="button" class="primary pvok">Fertig</button>') + '</div>');
    $('#shCopy').onclick = function () {
      var b = this;
      function ok() { b.textContent = 'Kopiert ✓'; }
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(SHARE_URL).then(ok, function () { toast('Kopieren nicht möglich'); });
      else toast('Kopieren nicht möglich');
    };
    var g = $('#shGo'); if (g) g.onclick = function () { navigator.share({ title: 'Lernkiste', text: SHARE_TXT, url: SHARE_URL }).catch(function () {}); };
  }
  // v58: Hilfe / häufige Fragen in den Einstellungen (aufklappbar, eine Frage pro <details>)
  function faqHTML() {
    var Q = function (q, a) { return '<details class="faq"><summary>' + q + '<svg class="chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></summary><div class="fa">' + a + '</div></details>'; };
    var P = 'Einstellungen → Daten und App';
    return Q('Wie bekomme ich die App aufs Handy?',
        '<p><b>iPhone</b></p><ol><li>Öffne die Seite in <b>Safari</b>.</li><li>Tippe auf <b>Teilen</b> (Quadrat mit Pfeil). Siehst du es nicht, tippe zuerst auf die drei Punkte.</li><li>Wähle <b>Zum Home-Bildschirm</b>.</li><li>Tippe auf <b>Hinzufügen</b>.</li></ol>' +
        '<p><b>Android</b></p><ol><li>Öffne die Seite in <b>Chrome</b>.</li><li>Tippe oben rechts auf <b>⋮</b>.</li><li>Wähle <b>App installieren</b> oder <b>Zum Startbildschirm hinzufügen</b>.</li><li>Bestätige.</li></ol>' +
        '<p class="note">iPhone: Die App auf dem Home-Bildschirm hat einen eigenen Speicher, getrennt von Safari. Hast du vorher in Safari gelernt, übertrage den Stand per Sync oder Backup (siehe unten).</p>') +
      Q('Funktioniert die App ohne Internet?',
        '<p>Ja. Nach dem ersten Öffnen mit Internet kannst du ohne Netz lernen. Nur Sync und Updates brauchen eine Verbindung. Feedback und gemeldete Fragen werden gesendet, sobald du wieder online bist.</p>') +
      Q('Wo ist mein Lernstand gespeichert?',
        '<p>Nur auf diesem Gerät, in dieser App bzw. diesem Browser. Er geht verloren, wenn du die App vom Home-Bildschirm löschst oder im Browser die Website-Daten löschst. Im privaten Modus wird nichts dauerhaft gespeichert.</p>' +
        '<p>Sichern kannst du ihn mit dem Sync oder einem Backup.</p>') +
      Q('Wie verbinde ich zwei Geräte?',
        '<ol><li>Auf dem ersten Gerät: ' + P + ' → <b>Code erzeugen</b>.</li><li>Mit <b>Kopieren</b> den Code übernehmen und dir selbst schicken oder abschreiben.</li><li>Auf dem zweiten Gerät: ' + P + ' → <b>Code eingeben</b>, Code einfügen, <b>Verbinden</b>.</li><li>Fertig. Beide gleichen sich ab jetzt von selbst ab. Mit <b>Jetzt abgleichen</b> geht es sofort.</li></ol>' +
        '<p class="note">Der Lernstand beider Geräte wird zusammengeführt. Bei jeder Karte und Frage zählt die neueste Antwort. Dein Name wird nicht übertragen. Gib den Code nur auf deinen eigenen Geräten ein.</p>') +
      Q('Wie mache ich ein Backup?',
        '<ol><li>' + P + ' → Backup speichern → <b>Datei</b>.</li><li>Auf dem iPhone z. B. <b>In Dateien sichern</b> wählen.</li></ol>' +
        '<p>Oder mit <b>Backup als Text kopieren</b> den Stand kopieren und z. B. in einer Notiz einfügen.</p>') +
      Q('Wie spiele ich ein Backup ein?',
        '<ol><li>' + P + ' → Backup einspielen → <b>Datei</b> oder <b>Text</b>.</li><li>Datei wählen oder den kopierten Text einfügen und <b>Prüfen</b>.</li><li><b>Zusammenführen</b> behält deinen jetzigen Stand und ergänzt ihn. <b>Ersetzen</b> überschreibt ihn mit dem Backup.</li></ol>') +
      Q('Wie bekomme ich Updates?',
        '<p>Von selbst: Gibt es eine neue Version, erscheint <b>Update bereit</b>. Tippe auf <b>Jetzt neu laden</b>. Dein Lernstand bleibt erhalten.</p>' +
        '<p>Selbst nachsehen: ' + P + ' → <b>Nach Update suchen</b>.</p>') +
      Q('Wie teile ich die App?',
        '<p>Einstellungen → <b>App teilen</b>. Dort lässt du den QR-Code abfotografieren, kopierst den Link oder verschickst ihn mit <b>Teilen</b>. Dein Lernstand wird dabei nicht mitgeschickt.</p>') +
      Q('Wie merke ich mir Begriffe, die ich nicht kenne?',
        '<ol><li>Tippe in einer Frage oben rechts auf <span class="kwi sm">' + KW_IC + '</span>.</li><li>Tippe das Wort an. Für längere Begriffe tippst du die Wörter daneben dazu.</li><li><b>Erklärung</b> zeigt die passende Karteikarte aus diesem Fach. Gibt es noch keine, siehst du eine passende Testfrage mit Lösung. <b>Merken</b> setzt den Begriff auf deine Liste.</li></ol>' +
        '<p>Die Liste <b>Meine Begriffe</b> findest du auf der Startseite und im jeweiligen Fach. Gibt es keine passende Erklärung, tippe auf <b>Erklärung fehlt melden</b>, dann ergänzen wir sie.</p>') +
      Q('Was sind Rechenschemata?',
        '<p>Ein Fahrplan für einen Aufgabentyp, z. B. lineare DGL 1. Ordnung (Querschnitt → Rechenschemata). Unter <b>Überblick</b> stehen die Schritte; antippen zeigt den Mustersatz zum Auswendiglernen, typische Fehler und ein Beispiel.</p><p>Unter <b>Aufgaben</b> rechnest du auf Papier und deckst Schritt für Schritt auf. Nach jedem Schritt bewertest du dich selbst. „Mit Schritten“ zeigt vorher, welcher Schritt dran ist, „Wie in der Klausur“ nicht.</p>') +
      Q('Was bedeuten Abkürzungen wie DGL oder AWP?',
        '<p>Gepunktet unterstrichene Abkürzungen kannst du antippen. Oben erscheint dann kurz die Langform, z. B. <b>AWP = Anfangswertproblem</b>. In Antwortknöpfen hältst du die Abkürzung gedrückt, damit du nicht aus Versehen antwortest.</p>') +
      Q('Wie lege ich Favoriten an oder ändere Farben?',
        '<p>Halte eine Kachel gedrückt. Bei Unterbereichen und Kapiteln (unter <b>Fächer</b>) kannst du <b>Favorisieren</b>, dann erscheinen sie auf der Startseite als Knopf unter ihrem Fach. Mit <b>Farbe</b> gibst du der Kachel eine eigene Farbe. Die Farbe eines Fachs gilt auch für seine Unterbereiche, außer du stellst sie dort extra ein.</p>' +
        '<p>Eine Klausur auf der Startseite gedrückt halten → <b>Ausblenden</b>: nur auf der Startseite oder auch bei den Fächern. Zurückholen kannst du sie unter der Liste mit <b>nicht auf der Startseite</b>. Favoriten-Knopf gedrückt halten nimmt ihn wieder heraus.</p>') +
      Q('Ich habe einen Fehler in einer Frage gefunden.',
        '<p>Beantworte die Frage und tippe darunter auf <b>Frage melden</b>. Für alles andere gibt es unten das <b>Feedback</b>.</p>') +
      Q('Was zeigt der Balken beim Lernstand?',
        '<p>Den Anteil der Fragen, die du zuletzt ganz richtig beantwortet hast. Hat ein Kapitel keine Fragen, zählen die Karten mit „Gewusst“.</p>');
  }
  function settingsView() {
    function syncHTML() {
      var c = syncCfg();
      if (!c) return '<div class="setrow"><div class="l"><b>Sync einrichten</b><small>Erzeugt einen Code. Gib ihn auf deinem anderen Gerät ein, dann gleichen beide ihren Lernstand ab.</small></div><button class="actbtn" id="sNew">Code erzeugen</button></div>' +
        '<div class="setrow"><div class="l"><b>Code eingeben</b><small>Du hast schon einen Code von einem anderen Gerät</small></div><button class="actbtn" id="sJoin">Eingeben</button></div><div id="sbox"></div>';
      return '<div class="setrow"><div class="l"><b>Dein Sync-Code</b><small class="synccode">' + esc(syncFmt(c.code)) + '</small></div><button class="actbtn" id="sCopy">Kopieren</button></div>' +
        '<div class="setrow"><div class="l"><b>Status</b><small id="syncStat">' + esc(syncStatusText()) + '</small></div><button class="actbtn" id="sNow">Jetzt abgleichen</button></div>' +
        '<p class="note" style="margin:4px 0 8px">Wer den Code kennt, sieht deinen Lernstand. Gib ihn nur auf deinen eigenen Geräten ein.</p>' +
        '<div class="setrow"><div class="l"><b>Sync beenden</b><small>Nur auf diesem Gerät. Der Lernstand hier bleibt.</small></div><button class="actbtn" id="sEnd">Beenden</button></div>' +
        '<div class="setrow"><div class="l"><b>Online-Kopie löschen</b><small>Löscht den Stand auf dem Server und beendet den Sync hier. Andere Geräte laden ihn beim nächsten Abgleich wieder hoch, bis du dort auch beendest.</small></div><button class="actbtn danger" id="sDel">Löschen</button></div>';
    }
    var st = DB.settings, sc = syncCfg();
    var motOn = ['mDue', 'mGoal', 'mChain', 'mCount', 'mMosaic', 'mBadges'].filter(function (k) { return st[k]; }).length;
    function sec(id, icon, title, sum, body) {
      return '<div class="group sec" data-sec="' + id + '"><button type="button" class="shead"><span class="sico">' + SETIC[icon] + '</span>' +
        '<span class="stx"><b>' + title + '</b><small>' + esc(sum) + '</small></span><svg class="chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></button><div class="gbody">' + body + '</div></div>';
    }
    var sub = function (t) { return '<h4 class="subh">' + t + '</h4>'; };
    var h = '<h1>Einstellungen</h1><p class="sub" style="margin-bottom:12px">' + esc(appName()) + '</p>' +
      '<div class="group top">' +
      '<div class="setrow"><div class="l"><b>Dein Name</b><small>Für den Titel, z. B. „Annas Lernkiste“</small></div>' +
      '<input class="txt" id="uname" type="text" maxlength="20" value="' + esc(st.name || '') + '" placeholder="Name" autocomplete="off" autocapitalize="words" spellcheck="false" aria-label="Dein Name"></div>' +
      '<div class="setrow"><div class="l"><b>Design</b></div>' + segHTML('theme', [['light', 'Hell'], ['dark', 'Dunkel'], ['auto', 'System']], st.theme) + '</div>' +
      '<div class="setrow"><div class="l"><b>Schriftgröße</b></div>' + segHTML('font', [[0.9, 'Klein'], [1, 'Mittel'], [1.15, 'Groß']], st.font) + '</div>' + '</div>' +
      '<div class="group"><div class="setrow tap" id="appShareRow" role="button" tabindex="0"><div class="l"><b>App teilen</b><small>QR-Code oder Link für Kommilitonen</small></div><button class="actbtn" id="bAppShare" type="button">Teilen</button></div></div>' +
      sec('lernen', 'learn', 'Lernen', (st.testN ? st.testN : 'Alle') + ' Fragen pro Runde · Klausur ' + st.examMin + ' Min.',
        sub('Karteikarten') +
        '<div class="setrow"><div class="l"><b>Standard-Filter</b><small>Welche Karten zuerst erscheinen</small></div>' + segHTML('cardFilter', [['red', 'Rot markiert'], ['all', 'Alle']], st.cardFilter) + '</div>' +
      '<div class="setrow"><div class="l"><b>Reihenfolge</b></div>' + segHTML('cardOrder', [['script', 'Skript'], ['shuffle', 'Gemischt']], st.cardOrder) + '</div>' +
        sub('Tests') +
        '<div class="setrow"><div class="l"><b>Fragen pro Runde</b></div>' + segHTML('testN', [[5, '5'], [10, '10'], [0, 'Alle']], st.testN) + '</div>' +
      '<div class="setrow"><div class="l"><b>Klausur: Minuten</b></div>' + segHTML('examMin', [[10, '10'], [20, '20'], [30, '30']], st.examMin) + '</div>' +
      '<div class="setrow"><div class="l"><b>Klausur: Fragen</b></div>' + segHTML('examN', [[8, '8'], [12, '12'], [16, '16']], st.examN) + '</div>') +
      sec('motiv', 'motiv', 'Motivation', motOn ? motOn + ' von 6 an' : 'Alles aus',
        '<div class="setrow"><div class="l"><b>Heute fällig</b><small>Wiederholung nach 1, 3, 7 und 14 Tagen</small></div>' + segHTML('mDue', [[0, 'Aus'], [1, 'An']], st.mDue) + '</div>' +
      '<div class="setrow"><div class="l"><b>Tagesziel</b><small>Antworten pro Tag</small></div>' + segHTML('mGoal', [[0, 'Aus'], [10, '10'], [20, '20'], [30, '30'], [50, '50']], st.mGoal) + '</div>' +
      '<div class="setrow"><div class="l"><b>Lerntage-Kette</b><small>Ein Pausetag pro Woche reißt sie nicht</small></div>' + segHTML('mChain', [[0, 'Aus'], [1, 'An']], st.mChain) + '</div>' +
      '<div class="setrow"><div class="l"><b>Klausur-Countdown</b></div>' + segHTML('mCount', [[0, 'Aus'], [1, 'An']], st.mCount) + '</div>' +
      '<div class="setrow"><div class="l"><b>Fragen-Übersicht</b><small>Mosaik im Kapitel</small></div>' + segHTML('mMosaic', [[0, 'Aus'], [1, 'An']], st.mMosaic) + '</div>' +
      '<div class="setrow"><div class="l"><b>Abzeichen</b><small>Im Verlauf</small></div>' + segHTML('mBadges', [[0, 'Aus'], [1, 'An']], st.mBadges) + '</div>') +
      sec('daten', 'data', 'Daten und App', (sc ? 'Sync an' : 'Sync aus') + ' · Backup · Version',
        sub('Geräte synchronisieren') + syncHTML() +
        sub('Backup') +
        '<div class="setrow"><div class="l"><b>Backup speichern</b><small>Lernstand, Verlauf, eigene Karten und Einstellungen als Datei</small></div><button class="actbtn" id="bShare">Datei</button></div>' +
      '<div class="setrow"><div class="l"><b>Backup als Text kopieren</b><small>Zum Einfügen auf einem anderen Gerät</small></div><button class="actbtn" id="bCopy">Kopieren</button></div>' +
      '<div class="setrow"><div class="l"><b>Backup einspielen</b><small>Aus Datei oder eingefügtem Text</small></div><span style="display:flex;gap:6px"><button class="actbtn" id="bFile">Datei</button><button class="actbtn" id="bPaste">Text</button></span></div>' +
      '<div id="impbox"></div><input type="file" id="file" accept=".json,application/json,text/plain" style="display:none">' +
        sub('App') +
        '<div class="setrow"><div class="l"><b>Version</b><small>' + esc(C.version) + '</small></div><button class="actbtn" id="bUpd">Nach Update suchen</button></div>' +
      '<div class="setrow"><div class="l"><b>Offline</b><small>Nach dem ersten Öffnen mit Internet funktioniert die App ohne Netz.</small></div></div>' +
      '<div class="setrow"><div class="l"><b>Anonyme Nutzungsstatistik</b><small>Ohne personenbezogene Daten: zählt nur App-Starts und geöffnete Fächer. Kein Name, keine IP-Adresse, keine Geräte-ID, kein Lernstand. Niemand ist daran erkennbar, auch nicht für mich.</small></div>' + segHTML('stats', [[0, 'Aus'], [1, 'An']], st.stats ? 1 : 0) + '</div>' +
      '<div class="setrow tap" id="privRow" role="button" tabindex="0"><div class="l"><b>Datenschutz</b><small>Was die App speichert und sendet</small></div><button class="actbtn" id="bPriv" type="button">Lesen</button></div>' +
        sub('Zurücksetzen') +
        '<div class="setrow"><div class="l"><b>Verlauf löschen</b></div><button class="actbtn danger" id="bLog">Löschen</button></div>' +
      '<div class="setrow"><div class="l"><b>Lernstand zurücksetzen</b><small>Alle Fächer, Einstellungen bleiben</small></div><button class="actbtn danger" id="bProg">Zurücksetzen</button></div>') +
      sec('hilfe', 'help', 'Hilfe', 'Installieren, Sync, Backup', faqHTML()) +
      sec('fb', 'fb', 'Feedback', 'Anonym, ohne Namen',
        '<div class="fbbox"><div class="l"><small>Schreib, was dir fehlt, was nicht klappt oder besser sein könnte. Anonym, ohne Namen. Bitte keine persönlichen Daten hineinschreiben.</small></div>' +
      '<textarea id="fbText" class="fbtext" maxlength="' + FB_MAX + '" placeholder="Deine Nachricht …" aria-label="Feedback"></textarea>' +
      '<input type="text" id="fbWeb" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">' +
      '<div class="fbrow"><small id="fbInfo" class="fbinfo">' + fbInfo() + '</small><button class="actbtn" id="fbSend" disabled>Senden</button></div></div>') +
      '<p class="note" style="text-align:center">' + (syncCfg() ? 'Dein Lernstand wird über deinen Sync-Code mit deinen anderen Geräten abgeglichen.' : 'Dein Lernstand liegt nur auf diesem Gerät. Mit dem Backup oder dem Sync sicherst du ihn.') + '</p>';
    view.innerHTML = h;
    $$('#view .sec').forEach(function (g) {
      var id = g.dataset.sec, btn = $('.shead', g);
      function set(on) { g.classList.toggle('open', on); btn.setAttribute('aria-expanded', on ? 'true' : 'false'); openSec[id] = on; }
      btn.onclick = function () { set(!g.classList.contains('open')); };
      set(openSec[id] === undefined ? id === 'fb' : !!openSec[id]);
    });
    $$('.seg[data-k] button').forEach(function (b) {
      b.onclick = function () {
        var k = b.parentNode.dataset.k, v = b.dataset.v; DB.settings[k] = isNaN(v) ? v : +v; DB.settings._ts = Date.now(); save(); applyPrefs(); if (k === 'stats' && !DB.settings.stats) statForget();
        var y = window.scrollY; settingsView(); window.scrollTo(0, y);
      };
    });
    $('#uname').addEventListener('input', function () {
      DB.settings.name = this.value.slice(0, 20); save(); document.title = appName(); $('#view .sub').textContent = appName();
    });
    $('#bShare').onclick = shareFile; $('#bCopy').onclick = copyText;
    $('#privRow').onclick = function () { openTile('Datenschutz', privacyHTML()); };
    $('#appShareRow').onclick = shareApp;
    $('#appShareRow').onkeydown = function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); shareApp(); } };
    $('#privRow').onkeydown = function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); this.onclick(); } };
    var fbT = $('#fbText'), fbB = $('#fbSend');
    fbT.addEventListener('input', function () { fbB.disabled = !fbT.value.trim(); $('#fbInfo').textContent = fbT.value.length > FB_MAX - 200 ? (FB_MAX - fbT.value.length) + ' Zeichen übrig' : fbInfo(); });
    fbB.onclick = function () {
      var text = fbT.value.trim().slice(0, FB_MAX); if (!text) return;
      if ($('#fbWeb').value) { fbT.value = ''; fbB.disabled = true; toast('Danke für dein Feedback!'); return; }
      fbQueue(fbQueue().concat([{ text: text, ts: Date.now() }]));
      fbT.value = ''; fbB.disabled = true;
      if (navigator.onLine === false) { toast('Gespeichert · wird gesendet, sobald du online bist'); $('#fbInfo').textContent = fbInfo(); return; }
      fbB.textContent = 'Sende …';
      fbFlush(function (ok) {
        if (!fbB.isConnected) return;
        fbB.textContent = 'Senden'; $('#fbInfo').textContent = fbInfo();
        toast(ok ? 'Danke für dein Feedback!' : 'Gerade keine Verbindung · wird später gesendet');
      });
    };
    function importFrom(text) {
      var o; try { o = JSON.parse(text); } catch (e) { toast('Das ist keine gültige Backup-Datei'); return; }
      if (!o || o.app !== 'lernkiste' || !o.data) { toast('Das ist kein Lernkiste-Backup'); return; }
      if (typeof o.data !== 'object' || Array.isArray(o.data)) { toast('Das ist kein Lernkiste-Backup'); return; }
      var d = normalizeDB(cleanImport(o.data)), n = Object.keys(d.progress).length, l = d.log.length;
      $('#impbox').innerHTML = '<div class="tip" style="margin:8px 0">Backup gefunden: ' + n + ' bewertete Karten, ' + l + ' Verlaufseinträge.</div>' +
        '<div class="row" style="margin:0 0 10px"><button class="ghost" id="iMerge">Zusammenführen</button><button class="ghost" id="iRepl">Ersetzen</button><button class="ghost" id="iCancel">Abbrechen</button></div>';
      $('#iMerge').onclick = function () { mergeInto(DB, d); save(); applyPrefs(); toast('Backup zusammengeführt'); settingsView(); };
      $('#iRepl').onclick = function () { DB = d; save(); applyPrefs(); toast('Backup eingespielt'); settingsView(); };
      $('#iCancel').onclick = function () { $('#impbox').innerHTML = ''; };
    }
    $('#bFile').onclick = function () { $('#file').click(); };
    $('#file').onchange = function () { var f = this.files[0]; if (!f) return; var r = new FileReader(); r.onload = function () { importFrom(String(r.result)); }; r.readAsText(f); this.value = ''; };
    $('#bPaste').onclick = function () {
      $('#impbox').innerHTML = '<textarea class="imp" id="impText" placeholder="Backup-Text hier einfügen"></textarea><div class="row" style="margin:0 0 10px"><button class="ghost" id="impGo">Prüfen</button></div>';
      $('#impGo').onclick = function () { importFrom($('#impText').value.trim()); };
    };
    function twoStep(id, label, fn) {
      var b = $(id); b.onclick = function () { if (b.dataset.sure) fn(); else { b.dataset.sure = 1; b.textContent = 'Wirklich?'; setTimeout(function () { if (b.isConnected) { b.textContent = label; delete b.dataset.sure; } }, 3000); } };
    }
    twoStep('#bLog', 'Löschen', function () { DB.log = []; DB.logClr = Date.now(); save(); toast('Verlauf gelöscht'); settingsView(); });
    twoStep('#bProg', 'Zurücksetzen', function () { DB.progress = {}; DB.tests = {}; DB.ptime = {}; DB.resetAt = Date.now(); save(); toast('Lernstand zurückgesetzt'); settingsView(); });
    function rerender() { var y = window.scrollY; settingsView(); window.scrollTo(0, y); }
    if ($('#sNew')) {
      $('#sNew').onclick = function () {
        if (navigator.onLine === false) { toast('Dafür brauchst du Internet'); return; }
        syncSetCfg({ code: syncNewCode(), dirty: Date.now(), last: 0 }); syncErr = false;
        toast('Code erzeugt · wird hochgeladen …'); rerender();
        syncNow().then(function (ok) { toast(ok ? 'Sync eingerichtet' : 'Hochladen hat nicht geklappt · wird später erneut versucht'); });
      };
      $('#sJoin').onclick = function () {
        $('#sbox').innerHTML = '<input class="txt synin" id="sIn" type="text" maxlength="30" placeholder="XXXX-XXXX-XXXX-XXXX-XXXX" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-label="Sync-Code">' +
          '<div class="row" style="margin:8px 0 10px"><button class="ghost" id="sGo">Verbinden</button><button class="ghost" id="sCancel">Abbrechen</button></div>';
        $('#sIn').focus();
        $('#sCancel').onclick = function () { $('#sbox').innerHTML = ''; };
        $('#sGo').onclick = function () {
          var code = syncNorm($('#sIn').value), b = $('#sGo');
          if (code.length !== 20) { toast('Der Code hat 20 Zeichen'); return; }
          if (navigator.onLine === false) { toast('Dafür brauchst du Internet'); return; }
          b.disabled = true; b.textContent = 'Prüfe …';
          sbRpc('lk_get', { p_code: code }).then(function (r) {
            if (!r || !r.data) { toast('Code nicht gefunden · bitte prüfen'); b.disabled = false; b.textContent = 'Verbinden'; return; }
            syncSetCfg({ code: code, dirty: Date.now(), last: 0 }); syncErr = false;
            return syncNow().then(function (ok) { toast(ok ? 'Verbunden · Lernstand zusammengeführt' : 'Verbunden · Abgleich folgt'); if ($('#sNow') || $('#sJoin')) rerender(); });
          }).catch(function () { toast('Keine Verbindung'); if (b.isConnected) { b.disabled = false; b.textContent = 'Verbinden'; } });
        };
      };
    } else {
      $('#sCopy').onclick = function () {
        var t = syncFmt(syncCfg().code);
        (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { toast('Code kopiert'); }, function () { toast(t); });
      };
      $('#sNow').onclick = function () {
        var b = $('#sNow'); b.disabled = true; b.textContent = 'Gleiche ab …';
        syncNow().then(function (ok) { toast(ok ? 'Abgeglichen' : 'Gerade keine Verbindung'); if (b.isConnected) { b.disabled = false; b.textContent = 'Jetzt abgleichen'; } });
      };
      twoStep('#sEnd', 'Beenden', function () { syncSetCfg(null); syncErr = false; toast('Sync beendet'); rerender(); });
      twoStep('#sDel', 'Löschen', function () {
        var c = syncCfg(); if (!c) return;
        sbRpc('lk_delete', { p_code: c.code }).then(function () { syncSetCfg(null); toast('Online-Kopie gelöscht · Sync beendet'); rerender(); }, function () { toast('Keine Verbindung · nichts gelöscht'); });
      });
    }
    $('#bUpd').onclick = function () {
      if (!('serviceWorker' in navigator)) { toast('Offline-Modus nicht verfügbar'); return; }
      navigator.serviceWorker.getRegistration().then(function (r) {
        if (!r) { toast('Offline-Modus ist nicht aktiv'); return; }
        toast('Suche nach Update …');
        return r.update().then(function () { setTimeout(function () { location.reload(); }, 1600); });
      }).catch(function () { toast('Keine Verbindung'); });
    };
  }

  // ====================================================================== Start
  applyPrefs();
  var off = document.createElement('div'); off.className = 'offline'; off.setAttribute('role', 'status');
  off.innerHTML = '<svg viewBox="0 0 24 24"><path d="M2 8.8a15 15 0 0 1 4-2.4M22 8.8a15 15 0 0 0-9.5-3.7M5 12.9a10 10 0 0 1 3.3-2M19 12.9a10 10 0 0 0-4.5-2.6M8.5 16.4a5 5 0 0 1 7 0M12 20h.01M3 3l18 18"/></svg>Offline';
  document.body.appendChild(off);
  function netState() { off.classList.toggle('on', navigator.onLine === false); }
  window.addEventListener('online', function () { netState(); toast('Wieder online'); fbFlush(); syncNow(); });
  setTimeout(syncNow, 1500);
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'visible') syncNow(); else { var c = syncCfg(); if (c && c.dirty) syncNow(); } });
  setTimeout(function () { fbFlush(); }, 3000);
  window.addEventListener('offline', netState);
  netState();
  window.addEventListener('hashchange', route);
  route();
  statPing('start');
  document.addEventListener('visibilitychange', statVisible);
  // ---- Automatische Update-Prüfung (höchstens alle 20 Stunden) und Hinweis, nie mitten im Test
  var updReady = false, updDismissed = false, bar = document.createElement('div');
  // v51: groß und mittig, damit niemand das Update verpasst; nie mitten im Lernmodus
  bar.className = 'updbar'; bar.setAttribute('role', 'dialog'); bar.setAttribute('aria-modal', 'true'); bar.setAttribute('aria-label', 'Update bereit');
  bar.innerHTML = '<div class="updcard"><div class="obico ok">' + ic('arrow') + '</div><h2>Update bereit</h2><p>Eine neue Version der Lernkiste ist da. Dein Lernstand bleibt erhalten.</p>' +
    '<button type="button" class="primary obbig" id="updGo">Jetzt neu laden</button><button type="button" class="oblink" id="updX">Später</button></div>';
  document.body.appendChild(bar);
  $('#updGo').onclick = function () { location.reload(); };
  $('#updX').onclick = function () { updDismissed = true; updUI(); };
  function updUI() { if (!bar) return; bar.classList.toggle('on', updReady && !updDismissed && !document.body.classList.contains('immersive')); }
  function checkUpdate() {
    if (!('serviceWorker' in navigator) || navigator.onLine === false) return;
    var last = 0; try { last = +localStorage.getItem('lernkiste-upd') || 0; } catch (e) {}
    if (Date.now() - last < 20 * 3600 * 1000) return;
    navigator.serviceWorker.getRegistration().then(function (r) {
      if (!r) return;
      try { localStorage.setItem('lernkiste-upd', String(Date.now())); } catch (e) {}
      return r.update();
    }).catch(function () {});
  }
  if ('serviceWorker' in navigator) {
    var hadController = !!navigator.serviceWorker.controller;
    navigator.serviceWorker.addEventListener('controllerchange', function () { if (hadController) { updReady = true; updDismissed = false; updUI(); } });
    window.addEventListener('load', function () { navigator.serviceWorker.register('sw.js').then(checkUpdate).catch(function () {}); });
    document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'visible') checkUpdate(); });
  }
})();
