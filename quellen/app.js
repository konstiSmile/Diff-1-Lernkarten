(function () {
  'use strict';
  var C = window.CONTENT;
  var KEY = 'lernkiste-v1';
  // Feedback: Google-Apps-Script-Web-App, schreibt in eine private Google-Tabelle
  var FB_URL = 'https://script.google.com/macros/s/AKfycbz4r4-dfoJQUeoy8WQayF3W7S6ddmKt8bujKiew7bUV5JmCUVMop5dhP5pDgDmMZtMm/exec';
  var FB_MAX = 2000, FB_Q = 'lernkiste-fbq', DEV_KEY = 'lernkiste-dev';
  var DEFAULTS = { theme: 'dark', font: 1, cardFilter: 'red', name: '', cardOrder: 'script', testN: 10, examMin: 20, examN: 12, mixMode: 'even', mixSubs: null, stats: 0, statsAsked: 0, lastBackup: 0, ownDirty: 0, ownTip: 0, nagDay: '', mDue: 1, mGoal: 30, mChain: 1, mCount: 1, mMosaic: 1, mBadges: 1 };

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
  // ---- Anonyme Nutzungsstatistik (nur mit Einwilligung, Standard aus): keine Geräte-ID, nichts auf dem Gerät gespeichert
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
      '<div class="pvhead"><b>' + esc(title) + '</b><button type="button" class="pvx" aria-label="Schließen">✕</button></div>' +
      '<div class="pvbody">' + html + '</div>' +
      (foot || '<button type="button" class="actbtn pvok">Schließen</button>') + '</div>';
    w.onclick = function (e) { if (e.target === w || e.target.closest('.pvx, .pvok')) closeTile(); };
    tileKey = function (e) { if (e.key === 'Escape') closeTile(); };
    document.addEventListener('keydown', tileKey);
    document.body.appendChild(w); document.body.classList.add('pvopen'); tileEl = w;
    cleanups.push(closeTile);
    $('.pvx', w).focus();
  }
  // ---- Einmalige Frage nach der Nutzungsstatistik (Einwilligung); ohne Antwort beim nächsten Start erneut
  var statAskedNow = false;
  function statAsk() {
    if (statAskedNow || DB.settings.statsAsked) return;
    if (DB.settings.stats) { DB.settings.statsAsked = Date.now(); save(); return; }
    setTimeout(function () {
      if (statAskedNow || DB.settings.statsAsked || tileEl || document.body.classList.contains('immersive')) return;
      statAskedNow = true;
      openTile('Kurze Frage', '<p>Darf die Lernkiste <b>anonym zählen</b>, wie oft sie geöffnet wird und welche Fächer genutzt werden? Das hilft, die App zu verbessern.</p>' +
        '<div class="pvkey"><b>Ich kann damit niemanden zuordnen</b><p>Es werden keine personenbezogenen Daten erhoben. Ich sehe nur Zahlen wie „heute 12 App-Starts, 5-mal Psycho 2“ – nicht, wer die App geöffnet hat, mit welchem Gerät oder von wo. Auch zwei Einträge kann ich nicht derselben Person zuordnen.</p></div>' +
        '<p>Gesendet werden nur „App-Start“ oder das geöffnete Fach und die App-Version. Kein Name, keine E-Mail, keine IP-Adresse, keine Geräte-ID, kein Standort, kein Lernstand.</p>' +
        '<p class="note">Du kannst das jederzeit ändern: Einstellungen → App. Dort steht auch alles zum Datenschutz.</p>',
        '<div class="row"><button type="button" class="ghost" id="stNo">Nein</button><button type="button" class="primary" id="stYes">Ja, gern</button></div>');
      function answer(on) {
        DB.settings.stats = on ? 1 : 0; DB.settings.statsAsked = Date.now(); save(); closeTile(); if (!on) statForget();
        if (on) { statPing('start'); var r = parseHash().parts; if (r[0] === 'f' && r[1]) statFach(r[1]); }
        toast(on ? 'Danke!' : 'Okay, es wird nichts gezählt');
      }
      $('#stYes').onclick = function () { answer(true); };
      $('#stNo').onclick = function () { answer(false); };
    }, 1500);
  }
  function privacyHTML() {
    return '<div class="pvkey"><b>Das Wichtigste zuerst</b><p>Ich erhebe keine personenbezogenen Daten. Ich bekomme weder deinen Namen noch deine E-Mail-Adresse, IP-Adresse, eine Geräte-Kennung oder deinen Lernstand. Ich sehe nur Zahlen wie „heute 12 App-Starts, 5-mal Psycho 2“. Ich kann nicht erkennen, wer die App nutzt, mit welchem Gerät oder von wo, und bei der Statistik auch nicht, ob zwei Einträge von derselben Person stammen.</p></div>' +
      '<p><b>Kurz gesagt:</b> Dein Lernstand bleibt auf deinem Gerät. Die App sendet nur etwas, wenn du Feedback schickst, eine Frage meldest oder die Nutzungsstatistik einschaltest.</p>' +
      '<h4>Auf deinem Gerät</h4>' +
      '<p>Lernstand, Verlauf, eigene Karten und Einstellungen (auch dein Name) liegen nur im Speicher deines Browsers. Sie verlassen das Gerät nicht, außer du speicherst selbst ein Backup. Damit die App offline läuft, speichert der Browser außerdem die App-Dateien.</p>' +
      '<h4>Beim Laden der App</h4>' +
      '<p>Die App liegt bei GitHub Pages (GitHub, USA). Wie jeder Webserver verarbeitet GitHub dabei technisch deine IP-Adresse. Die App lädt keine Werbung, keine Tracker und nichts von fremden Seiten.</p>' +
      '<h4>Feedback und „Frage melden“ (nur wenn du sendest)</h4>' +
      '<p>Gesendet werden dein Text (beim Melden: Grund, Kommentar, Fach und Nummer der Frage), die App-Version und eine zufällige Kennung gegen Spam. Diese Kennung wird beim ersten Feedback auf dem Gerät gespeichert und sagt nichts über dich. Kein Name. Ziel ist eine private Google-Tabelle über Google Apps Script (Google, Server auch in den USA). Google verarbeitet dabei technisch deine IP-Adresse, in der Tabelle landet sie nicht. Schreib bitte keine persönlichen Daten in den Text.</p>' +
      '<h4>Nutzungsstatistik (nur wenn eingeschaltet)</h4>' +
      '<p><b>Die Statistik ist vollständig anonym.</b> Sie zählt nur, <i>wie oft</i> die App und die Fächer geöffnet werden, nicht <i>wer</i> sie öffnet. Kein Eintrag enthält etwas, das auf dich oder dein Gerät schließen lässt.</p>' +
      '<p>Nur mit deiner Zustimmung: Die App fragt einmal, und du kannst es jederzeit ändern. Wenn sie an ist, meldet die App beim Öffnen und beim ersten Öffnen eines Fachs: „App-Start“ oder „Fach geöffnet“, welches Fach und die App-Version. Beim Öffnen kommt dazu nur, ob es der erste Start heute, in dieser Woche oder überhaupt auf diesem Gerät ist (ja/nein). So lässt sich zählen, wie viele Geräte die App nutzen, ohne sie zu unterscheiden. Dafür merkt sich die App auf deinem Gerät das Datum der letzten Meldung; das wird nicht gesendet und beim Ausschalten gelöscht. Den Zeitpunkt notiert die Tabelle. Nicht gesendet werden: Name, E-Mail, IP-Adresse, Geräte-ID, Gerätetyp, Standort, Antworten oder Lernstände. Ziel ist dieselbe private Google-Tabelle wie beim Feedback. Ausschalten geht jederzeit hier in den Einstellungen und wirkt sofort.</p>' +
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
    d.v = 1; d.recent = d.recent || []; d.progress = d.progress || {}; d.tests = d.tests || {}; d.log = d.log || []; d.hidden = d.hidden || []; d.custom = d.custom || {}; d.custom.folders = d.custom.folders || []; d.badges = (d.badges && typeof d.badges === 'object' && !Array.isArray(d.badges)) ? d.badges : {};
    d.settings = Object.assign({}, DEFAULTS, d.settings || {});
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
    if (fresh || moved) { if (moved) d.tests['psy/tp'].saved = 1; try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) {} }
    return d;
  })();
  function save() {
    if (DB.log.length > 20000) DB.log.splice(0, DB.log.length - 20000);
    try { localStorage.setItem(KEY, JSON.stringify(DB)); saveWarned = false; }
    catch (e) {
      if (saveWarned) return; saveWarned = true;
      setTimeout(function () { toast('Achtung: Speichern hat nicht geklappt (Speicher voll oder gesperrt). Bitte mach ein Backup.', 'Backup', shareFile); }, 50);
    }
  }
  var saveWarned = false;
  // ---- Eigene Karten: Merker für Änderungen seit dem letzten Backup und Erinnerung
  function ownTouch() { if (!DB.settings.ownDirty) DB.settings.ownDirty = Date.now(); }
  function ownCount() { return DB.custom.folders.reduce(function (n, f) { return n + f.cards.length; }, 0); }
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
  function logAns(fach, id, score, pts) { var e = [Date.now(), fach, id, Math.round(score * 100) / 100]; if (typeof pts === 'number') e.push(pts); DB.log.push(e); }
  function tests(sid, cid) { var k = sid + '/' + cid, t = DB.tests[k] = DB.tests[k] || {}; t.best = t.best || {}; t.wrong = t.wrong || []; return t; }

  var mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  function applyPrefs() {
    var t = DB.settings.theme; if (t === 'auto') t = (mq && mq.matches) ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', t);
    document.documentElement.style.fontSize = (15 * DB.settings.font) + 'px';
    document.title = appName();
    var m = $('meta[name="theme-color"]'); if (m) m.setAttribute('content', t === 'dark' ? '#1b1a18' : '#f6f3ee');
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
    { id: 'start', href: '#/', label: 'Start', svg: '<path d="M3 11l9-8 9 8v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>' },
    { id: 'suche', href: '#/suche', label: 'Suche', svg: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>' },
    { id: 'neu', href: '#/neu', label: 'Neu', plus: true, svg: '<path d="M12 5v14M5 12h14"/>' },
    { id: 'verlauf', href: '#/verlauf', label: 'Verlauf', svg: '<path d="M5 20V10M12 20V4M19 20v-7"/>' },
    { id: 'set', href: '#/einstellungen', label: 'Einstellungen', svg: '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>' }
  ];
  $('#tabbar').innerHTML = '<nav>' + TABS.map(function (t) {
    return '<a class="tab' + (t.plus ? ' plus' : '') + '" data-t="' + t.id + '" href="' + t.href + '">' +
      (t.plus ? '<span class="pl"><svg viewBox="0 0 24 24">' + t.svg + '</svg></span>' : '<svg viewBox="0 0 24 24">' + t.svg + '</svg>') +
      '<span class="t">' + t.label + '</span></a>';
  }).join('') + '</nav>';
  function setTab(id) { $$('.tab').forEach(function (a) { a.classList.toggle('on', a.dataset.t === id); }); }

  function route() {
    cleanups.splice(0).forEach(function (f) { try { f(); } catch (e) {} });
    setImm(false); view.className = ''; view.removeAttribute('style');
    var r = parseHash(), p = r.parts, tab = 'start';
    if (!p.length) homeView();
    else if (p[0] === 'suche') { tab = 'suche'; searchView(r.q.q || ''); }
    else if (p[0] === 'verlauf') { tab = 'verlauf'; verlaufView(); }
    else if (p[0] === 'neu') { tab = 'neu'; neuView(p[1], p[2]); }
    else if (p[0] === 'einstellungen') { tab = 'set'; settingsView(); }
    else if (p[0] === 'mix') mixView(p[1]);
    else if (p[0] === 'faellig') dueView(p[1]);
    else if (p[0] === 'f' && p[1] && p[2] === 'u' && p[3]) fachView(p[1], p[3]);
    else if (p[0] === 'f' && p[1] && !p[2]) fachView(p[1]);
    else if (p[0] === 'f' && p[1] && p[2]) chapterView(p[1], p[2], r.q);
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
    var ls = learnState(), today = dayNum(Date.now()), cards = [], items = [];
    C.subjects.forEach(function (sx) {
      if (isHidden(sx.id)) return;
      sx.chapters.forEach(function (ch) {
        if (ch.placeholder) return;
        (ch.cards || []).forEach(function (c) { if (isDue(ls[c.id], today)) cards.push(Object.assign({}, c, { _s: sx.id })); });
        (ch.items || []).forEach(function (it) { if (isDue(ls[it.id], today)) items.push(Object.assign({}, it, { _s: sx.id })); });
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
    if (st.mDue) {
      var d = dueLists(), any = d.cards.length + d.items.length;
      rows.push('<div class="tdrow" id="tdDue"><div class="tdtxt"><b>Heute fällig</b><small>' + (any ? 'Geübtes wiederholen' : 'Nichts fällig') + '</small></div>' +
        (d.cards.length ? '<a class="actbtn" href="#/faellig/karten">Karten ' + d.cards.length + '</a>' : '') +
        (d.items.length ? '<a class="actbtn" href="#/faellig/tests">Fragen ' + d.items.length + '</a>' : '') + '</div>');
    }
    if (st.mCount) {
      var cs = examDays();
      if (cs.length) rows.push('<div class="tdcount" id="tdCount">' + cs.map(function (x) {
        return '<span><i class="sw" style="background:var(--c-' + x.s.id + ')"></i>' + esc(x.s.name) + ' ' + (x.d === 0 ? 'heute' : x.d === 1 ? 'morgen' : 'in ' + x.d + ' Tagen') + '</span>';
      }).join('') + '</div>');
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
    var known = 0, total = 0, items = 0, best = null, allPlaceholder = true;
    s.chapters.forEach(function (ch) {
      if (!ch.placeholder) allPlaceholder = false;
      if (ch.cards) { total += ch.cards.length; ch.cards.forEach(function (c) { if (DB.progress[c.id] === 'known') known++; }); }
      if (ch.items) { items += ch.items.length; var b = tests(s.id, ch.id).best.exam; if (b !== undefined && (best === null || b > best)) best = b; }
    });
    var txt, pct = 0;
    if (total) { txt = known ? known + ' von ' + total + ' gewusst' : total + ' Karten'; pct = known / total * 100; }
    else if (best !== null) { txt = 'Klausur-Bestwert ' + best + ' %'; pct = best; }
    else txt = allPlaceholder ? 'Inhalte folgen' : items + ' Fragen';
    return { txt: txt, pct: pct, placeholder: allPlaceholder };
  }
  function homeView() {
    var vis = C.subjects.filter(function (s) { return !isHidden(s.id); }), hid = C.subjects.filter(function (s) { return isHidden(s.id); });
    var h = '<h1>' + esc(appName()) + '</h1><p class="sub">Fach auswählen</p>' +
      '<a class="fakesearch" href="#/suche"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>Begriff oder Satz suchen …</a>' + todayHTML() + '<div class="grid fach">';
    vis.forEach(function (s) {
      var st = subjStats(s);
      h += '<div class="tilewrap" data-sid="' + s.id + '"><div class="hidehint">Ausblenden</div><a class="tile s-' + s.id + '" href="#/f/' + s.id + '">' + (st.placeholder ? '<span class="badge">Gerüst</span>' : '') +
        '<div><h2 class="name">' + esc(s.name) + '</h2><p class="desc">' + esc(s.desc) + '</p></div>' +
        '<div class="foot"><span>' + esc(st.txt) + '</span><div class="bar"><div style="width:' + st.pct + '%"></div></div><span class="go">Öffnen ›</span></div></a>' +
        '<button type="button" class="tilemenu" aria-label="Mehr zu ' + esc(s.name) + '">⋯</button></div>';
    });
    h += '</div>';
    if (eligible().length >= 2) h += '<a class="mixtile" href="#/mix"><span><b>Gemischt üben</b><small>Fächer kombinieren, Karten und Tests gemischt</small></span><span class="go">Öffnen ›</span></a>';
    if (!vis.length) h += '<p class="note" style="text-align:center;padding:26px 10px">Alle Themen sind ausgeblendet.</p>';
    if (hid.length) {
      h += '<button type="button" class="hiddenlink" id="hidLink">versteckte Themen (' + hid.length + ')</button><div class="hiddenlist" id="hidList" hidden>' +
        hid.map(function (s) { return '<div class="hidrow"><i class="sw" style="background:var(--c-' + s.id + ')"></i><span>' + esc(s.name) + '</span><button type="button" data-show="' + s.id + '">Einblenden</button></div>'; }).join('') + '</div>';
    }
    view.innerHTML = h;
    wireHome(!!hid.length);
  }
  function hideSubject(sid) {
    setHidden(sid, true); homeView();
    toast('„' + subj(sid).name + '“ ausgeblendet', 'Rückgängig', function () { setHidden(sid, false); if (!parseHash().parts.length) homeView(); });
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
      $$('[data-show]').forEach(function (b) { b.onclick = function () { var sid = b.dataset.show; setHidden(sid, false); homeView(); toast('„' + subj(sid).name + '“ wieder eingeblendet'); }; });
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
    var sel = mixSelected(), even = DB.settings.mixMode === 'even', cards = [], items = [];
    sel.forEach(function (sx) {
      sx.chapters.forEach(function (ch) {
        if (ch.placeholder) return;
        if (ch.cards) ch.cards.forEach(function (c) { cards.push(Object.assign({}, c, { _s: sx.id })); });
        if (ch.items) ch.items.forEach(function (it) { items.push(Object.assign({}, it, { _s: sx.id })); });
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
    var h = '<div class="nav"><a href="#/">‹ Start</a></div><h1>Gemischt üben</h1><p class="sub">Wähle die Fächer, die gemischt werden sollen.</p><div class="group" style="padding:4px 16px">' +
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
    var parts = [], pct = 0, k = 0, desc;
    if (ch.cards) { k = ch.cards.filter(function (c) { return DB.progress[c.id] === 'known'; }).length; pct = k / ch.cards.length * 100; }
    if (ch.items) { var b = tests(s.id, ch.id).best.exam; if (b !== undefined) pct = Math.max(pct, b); }
    if (ch.cards && ch.items) { parts.push(ch.items.length + ' Fragen', ch.cards.length + ' Karten'); desc = 'Karteikarten, Multiple Choice, Richtig/Falsch, Lückentext, Zeit-Simulation'; }
    else if (ch.cards) { parts.push(k ? k + ' von ' + ch.cards.length + ' gewusst' : ch.cards.length + ' Karten'); desc = 'Karteikarten'; }
    else { var b2 = tests(s.id, ch.id).best.exam; parts.push(ch.items.length + ' Fragen' + (b2 !== undefined ? ' · Klausur ' + b2 + ' %' : '')); desc = 'Tests: Multiple Choice, Lückentext, Richtig/Falsch, Zeit-Simulation'; }
    return '<a class="tile s-' + s.id + '" href="#/f/' + s.id + '/' + ch.id + '">' + (ch.placeholder ? '<span class="badge">Gerüst</span>' : '') +
      '<div><h2 class="name">' + esc(ch.title) + '</h2><p class="desc">' + esc(desc) + '</p></div>' +
      '<div class="foot"><span>' + esc(parts.join(' · ')) + '</span><div class="bar"><div style="width:' + pct + '%"></div></div><span class="go">Öffnen ›</span></div></a>';
  }
  function fachView(sid, gid) {
    var s = subj(sid); if (!s) return homeView();
    var grp = gid ? (s.groups || []).filter(function (g) { return g.id === gid; })[0] : null;
    if (gid && !grp) { location.hash = '#/f/' + sid; return; }
    var h = '<div class="nav"><a href="#/' + (grp ? 'f/' + sid : '') + '">‹ ' + esc(grp ? s.name : 'Start') + '</a></div><h1>' + esc(grp ? grp.name : s.name) + '</h1><p class="sub">' + esc(grp ? s.name : s.desc) + '</p><div class="grid">';
    if (sid === 'psy' && !grp) h = h.replace(/<div class="grid">$/, '<p class="disclaimer">Alle Inhalte dieser App wurden nicht von der Dozentin bzw. dem Dozenten überprüft und sind ohne jede Gewähr zu verwenden. Es können sich Fehler eingeschlichen haben, und die Klausur kann andere Inhalte abfragen.</p><div class="grid">');
    if (s.groups && !grp) {
      s.groups.forEach(function (g) {
        var chs = s.chapters.filter(function (c) { return c.group === g.id; }), cards = 0, items = 0, known = 0;
        chs.forEach(function (c) { if (c.cards) { cards += c.cards.length; c.cards.forEach(function (x) { if (DB.progress[x.id] === 'known') known++; }); } if (c.items) items += c.items.length; });
        var txt = !chs.length ? 'Inhalte folgen' : [chs.length + (chs.length === 1 ? ' Kapitel' : ' Kapitel'), cards ? cards + ' Karten' : '', items ? items + ' Fragen' : ''].filter(Boolean).join(' · ');
        h += '<a class="tile s-' + sid + '" href="#/f/' + sid + '/u/' + g.id + '">' + (chs.length ? '' : '<span class="badge">Folgt</span>') +
          '<div><h2 class="name">' + esc(g.name) + '</h2><p class="desc">' + esc(g.desc) + '</p></div>' +
          '<div class="foot"><span>' + esc(txt) + '</span><div class="bar"><div style="width:' + (cards ? known / cards * 100 : 0) + '%"></div></div><span class="go">Öffnen ›</span></div></a>';
      });
    } else {
      var list = grp ? s.chapters.filter(function (c) { return c.group === gid; }) : s.chapters;
      list.forEach(function (ch) { h += chapTile(s, ch); });
      if (!list.length) h += '<div class="note" style="text-align:center;padding:18px 6px">Inhalte folgen.</div>';
    }
    view.innerHTML = h + '</div>';
  }
  function chapterView(sid, cid, q) {
    if (sid === 'psy' && cid === 'tp') { location.replace('#/f/psy/u/pers'); return; }
    var s = subj(sid), ch = chap(sid, cid); if (!s || !ch) return homeView();
    view.className = 's-' + sid;
    var grp = ch.group && (s.groups || []).filter(function (g) { return g.id === ch.group; })[0];
    if (grp) s = Object.assign({}, s, { href: '#/f/' + sid + '/u/' + grp.id, name: grp.name });
    if (ch.cards && ch.items) {
      if (q.c || q.mode === 'cards' || q.read) cardsView(Object.assign({}, s, { href: '#/f/' + sid + '/' + cid, name: ch.title.split(' · ')[0] }), Object.assign({}, ch, { kind: 'cards' }), q);
      else testsView(s, ch, q);
    } else if (ch.kind === 'cards') cardsView(s, ch, q); else testsView(s, ch, q);
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
      var h = '<div class="nav"><a href="' + (s.href || '#/f/' + s.id) + '">‹ ' + esc(s.name) + '</a><button id="rEnd">Fertig</button></div>' +
        '<h1 style="font-size:1.5rem">' + esc(ch.title) + '</h1><p class="sub" style="margin-bottom:0">Lesen · ohne Wertung</p>';
      if (!total) h += '<div class="empty">Keine Karten vorhanden.</div>';
      else {
        var c = list[rpos];
        h += '<div class="status"><span>Karte ' + (rpos + 1) + ' / ' + total + '</span><span>nichts wird gewertet</span></div>' +
          '<div class="pbar"><div style="width:' + ((rpos + 1) / total * 100) + '%"></div></div>' +
          '<div class="card">' + (c.red ? '<span class="reddot"></span>' : '') + '<div class="meta"><span>' + esc(c.src) + '</span><span class="side">Frage</span></div>' +
          '<div class="face">' + c.q + '</div></div>' +
          '<div class="card" style="margin-top:10px"><div class="meta"><span></span><span class="side" style="color:var(--green)">Antwort</span></div><div class="face">' + c.a + '</div></div>' +
          '<div class="row"><button class="ghost" id="rPrev"' + (rpos === 0 ? ' disabled' : '') + '>← Zurück</button><button class="ghost" id="rNext"' + (rpos === total - 1 ? ' disabled' : '') + '>Weiter →</button></div>';
      }
      h += '<div class="tools"><button id="rShuf">Mischen</button><button id="rOrd">Skript-Reihenfolge</button></div><p class="foot-note">Pfeiltasten zum Blättern</p>';
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
      var h = '<div class="nav"><a href="' + (s.href || '#/f/' + s.id) + '">‹ ' + esc(s.name) + '</a></div>' +
        '<h1 style="font-size:1.5rem">' + esc(ch.title) + '</h1><p class="sub" style="margin-bottom:0">' + esc(ch.sub || '') + '</p>' +
        '<div class="seg" id="seg">' + (noRed ? '' : '<button data-f="red" class="' + (filter === 'red' ? 'on' : '') + '"><span class="dot"></span>Rot markiert (' + nRed + ')</button>') +
        '<button data-f="all" class="' + (filter === 'all' ? 'on' : '') + '">Alle (' + cards.length + ')</button>' +
        '<button data-f="again" class="' + (filter === 'again' ? 'on' : '') + '">Nochmal (' + nAgain + ')</button></div>' +
        '<div class="row" style="margin:10px 0 0"><button class="ghost" id="bRead">📖 Karten lesen · ohne Wertung</button></div>' +
        '<div class="status"><span>' + (total ? 'Karte ' + (pos + 1) + ' / ' + total : '') + '</span><span>' + (total ? '✓ ' + known + ' von ' + total + ' gewusst' : '') + '</span></div>' +
        '<div class="pbar"><div style="width:' + (total ? known / total * 100 : 0) + '%"></div></div>';
      if (!total) {
        h += '<div class="empty">' + (filter === 'again' ? 'Keine Karten im Nochmal-Stapel. Stark!' : 'Keine Karten in dieser Auswahl.') + '</div>';
      } else {
        var c = byId[deck[pos]], mark = DB.progress[c.id] === 'known' ? ' · ✓' : DB.progress[c.id] === 'again' ? ' · ✗' : '';
        h += '<div class="card flip ' + (flipped ? 'back' : 'front') + '" id="card">' + (c.red ? '<span class="reddot"></span>' : '') +
          '<div class="meta"><span>' + esc(c.src) + mark + '</span><span class="side">' + (flipped ? 'Antwort' : 'Frage') + '</span></div>' +
          '<div class="face">' + (flipped ? c.a : c.q) + '</div>' + (flipped ? '' : '<div class="hint">Antippen zum Umdrehen</div>') + '</div>';
        if (flipped) h += '<div class="row"><button class="btn again" id="bAgain">✗ Nochmal</button><button class="btn known" id="bKnown">✓ Gewusst</button></div>';
        h += '<div class="row"><button class="ghost" id="bPrev"' + (pos === 0 ? ' disabled' : '') + '>← Zurück</button><button class="ghost" id="bFlip">' + (flipped ? 'Zur Frage' : 'Umdrehen') +
          '</button><button class="ghost" id="bNext"' + (pos === total - 1 ? ' disabled' : '') + '>Weiter →</button></div>';
      }
      h += '<div class="tools"><button id="bShuf">Mischen</button><button id="bOrd">Skript-Reihenfolge</button><button id="bReset">' + (confirmReset ? 'Wirklich zurücksetzen?' : 'Fortschritt zurücksetzen') + '</button></div>' +
        '<p class="foot-note">Karte antippen oder Leertaste zum Umdrehen · Pfeiltasten zum Blättern</p>';
      view.innerHTML = h;
      if (terms.length && total) highlight($('.face', view), terms);
      $$('#seg button').forEach(function (b) { b.onclick = function () { filter = b.dataset.f; build(false); draw(); }; });
      $('#bRead').onclick = function () { rpos = 0; reading = true; draw(); window.scrollTo(0, 0); };
      var card = $('#card'); if (card) card.onclick = flip;
      var bf = $('#bFlip'); if (bf) bf.onclick = flip;
      var bp = $('#bPrev'); if (bp) bp.onclick = function () { go(-1); };
      var bn = $('#bNext'); if (bn) bn.onclick = function () { go(1); };
      var ba = $('#bAgain'); if (ba) ba.onclick = function () { rate('again'); };
      var bk = $('#bKnown'); if (bk) bk.onclick = function () { rate('known'); };
      $('#bShuf').onclick = function () { order = shuffle(cards.map(function (c) { return c.id; })); build(false); draw(); };
      $('#bOrd').onclick = function () { order = cards.map(function (c) { return c.id; }); build(false); draw(); };
      $('#bReset').onclick = function () {
        if (!confirmReset) { confirmReset = true; draw(); return; }
        cards.forEach(function (c) { delete DB.progress[c.id]; }); save(); confirmReset = false; build(false); draw();
      };
    }
    function flip() { if (!deck.length) return; flipped = !flipped; draw(); }
    function go(d) { var np = pos + d; if (np < 0 || np >= deck.length) return; pos = np; flipped = false; draw(); window.scrollTo(0, 0); }
    function rate(val) {
      var id = deck[pos]; DB.progress[id] = val; logAns(byId[id]._s || s.id, id, val === 'known' ? 1 : 0); save();
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
    { id: 'mc', name: 'Multiple Choice', desc: 'Vier Antworten, eine stimmt', ico: '◉' },
    { id: 'tf', name: 'Richtig / Falsch', desc: 'Schnelle Aussagen mit Erklärung', ico: '±' },
    { id: 'gap', name: 'Lückentext', desc: 'Begriffe selbst eintippen', ico: '▭' },
    { id: 'exam', name: 'Zeit-Simulation', desc: 'Mini-Klausur mit Timer und Note', ico: '⏱' }
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
      return '<div class="opt mopt ' + cls + '"><span class="box">' + (on || (!sel && r) ? '✓' : '') + '</span><span>' + it.options[oi] + (lab ? '<small class="mlab">' + lab + '</small>' : '') + '</span></div>';
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
    function nav(extra) { return '<div class="nav"><a href="' + (s.href || '#/f/' + s.id) + '">‹ ' + esc(s.name) + '</a>' + (extra || '') + '</div>'; }
    function prep(id) { var it = BYID[id]; return { it: it, order: it.type === 'mc' ? shuffle(it.options.map(function (_, i) { return i; })) : null, multi: isMulti(it, s.id) }; }
    function finishLog(r) {
      logAns(r.it._s || s.id, r.it.id, r.s, r.p);
      var ix = T.wrong.indexOf(r.it.id);
      if (r.s === 1 && ix >= 0) T.wrong.splice(ix, 1);
      if (r.s < 1 && ix < 0) T.wrong.push(r.it.id);
    }

    function hub() {
      setImm(false);
      var counts = { mc: pool('mc').length, tf: pool('tf').length, gap: pool('gap').length }, total = ITEMS.length;
      var h = nav() + '<h1 style="font-size:1.55rem">' + esc(ch.title) + '</h1><p class="sub">' + esc(ch.sub || '') + '</p>';
      if (ch.placeholder) h += '<div class="banner"><b>Gerüst:</b> Das sind nur Beispielfragen, damit du die Test-Funktionen ausprobieren kannst. Die echten Inhalte folgen.</div>';
      h += '<div class="chips"><span class="lbl">Fragen pro Runde</span>' + [5, 10, 0].map(function (n) { return '<button class="chip' + (st.testN === n ? ' on' : '') + '" data-n="' + n + '">' + (n || 'Alle') + '</button>'; }).join('') + '</div>';
      var cardsMode = '';
      if (ch.cards) {
        var kn = ch.cards.filter(function (c) { return DB.progress[c.id] === 'known'; }).length;
        cardsMode = '<button class="mode" data-m="cards"><span class="ico">▤</span><span><span class="t">Karteikarten</span><br><span class="d">Umdrehen, gewusst oder nochmal</span></span><span class="r">' + ch.cards.length + ' Karten' + (kn ? '<b>' + kn + ' gewusst</b>' : '') + '</span></button>';
      }
      h += '<div class="modes">' + cardsMode + MODES.map(function (m) {
        var c = m.id === 'exam' ? total : counts[m.id], b = T.best[m.id];
        return '<button class="mode" data-m="' + m.id + '"' + (c ? '' : ' disabled') + '><span class="ico">' + m.ico + '</span><span><span class="t">' + m.name + '</span><br><span class="d">' + (m.id === 'mc' && s.id === 'psy' ? 'Vier Antworten, 1 bis 4 richtig' : m.desc) + '</span></span>' +
          '<span class="r">' + c + ' Fragen' + (b !== undefined ? '<b>Bestwert ' + b + ' %</b>' : '') + '</span></button>';
      }).join('') + '</div>';
      h += '<div class="row" style="margin-top:14px">' + (ch.cards ? '<button class="ghost" id="readC">📖 Karten lesen</button>' : '') + '<button class="ghost" id="readQ">📖 Fragen lesen</button></div>';
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
        if (b.dataset.sure) { T.best = {}; T.wrong = []; save(); hub(); } else { b.textContent = 'Wirklich zurücksetzen?'; b.dataset.sure = 1; }
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
        '<div class="row"><button class="ghost" id="rPrev"' + (k === 0 ? ' disabled' : '') + '>← Zurück</button><button class="ghost" id="rNext"' + (k === total - 1 ? ' disabled' : '') + '>Weiter →</button></div>';
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
      var i = 0, results = [];
      if (!queue.length) { view.innerHTML = nav() + '<div class="empty">Keine Fragen in dieser Auswahl.</div>'; return; }
      setImm(true);
      function show() {
        if (i >= queue.length) return finish();
        var p = queue[i], it = p.it, done = false;
        var h = nav('<button id="quit">Beenden</button>') +
          '<div class="meta"><span>' + title + ' · ' + (i + 1) + ' / ' + queue.length + '</span><span>' + esc(it.src || '') + '</span></div>' +
          '<div class="pbar"><div style="width:' + (i / queue.length * 100) + '%"></div></div><div class="card">' + questionBody(p) + '<div id="fb"></div></div>';
        if (it.type === 'gap') h += '<div class="row" id="gaprow"><button class="ghost" id="reveal">Lösung zeigen</button><button class="primary" id="check">Prüfen</button></div>';
        if (p.multi) h += '<div class="row" id="mcrow"><button class="primary" id="mcheck" disabled>Prüfen</button></div>';
        view.innerHTML = h; window.scrollTo(0, 0);
        $('#quit').onclick = hub;
        function answered(score, pts) {
          if (done) return; done = true; results.push({ it: it, s: score, p: pts });
          var head = pts !== undefined ? (pts === it.options.length ? '✓ ' : pts > 0 ? '◐ ' : '✗ ') + pts + ' / ' + it.options.length + ' Punkte' : score === 1 ? '✓ Richtig' : score > 0 ? '◐ Teilweise richtig' : '✗ Nicht ganz';
          $('#fb').innerHTML = '<div class="fb ' + (score === 1 ? 'ok' : score > 0 && pts !== undefined ? 'mid' : 'bad') + '">' + head + '</div>' +
            (it.expl ? '<div class="tip' + (it.warn ? ' warn' : '') + '">' + it.expl + '</div>' : '') +
            '<div class="row"><button class="primary" id="next">' + (i === queue.length - 1 ? 'Ergebnis ›' : 'Weiter ›') + '</button></div>' +
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
              var on = ix < 0; b.classList.toggle('sel', on); b.setAttribute('aria-pressed', on); $('.box', b).textContent = on ? '✓' : '';
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
        } else if (it.type === 'tf') {
          $$('.opt').forEach(function (b) {
            b.onclick = function () {
              var v = b.dataset.v === '1';
              $$('.opt').forEach(function (x) { x.disabled = true; if ((x.dataset.v === '1') === it.answer) x.classList.add('ok'); });
              if (v !== it.answer) b.classList.add('bad'); answered(grade(it, v));
            };
          });
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
        var pts = results.reduce(function (a, r) { return a + r.s; }, 0), pct = Math.round(pts / queue.length * 100);
        results.forEach(finishLog);
        if (mode !== 'wrong' && (T.best[mode] === undefined || pct > T.best[mode])) T.best[mode] = pct;
        save(); badgeCheck();
        var bad = results.filter(function (r) { return r.s < 1; }), hasP = results.some(function (r) { return r.p !== undefined; });
        var h = nav() + '<div class="card"><div class="score"><div class="big">' + pct + ' %</div><div class="note">' + (hasP ? breakdown(results) : fmt(pts) + ' von ' + queue.length + ' richtig') + ' · ' + title + '</div></div></div>';
        if (bad.length) {
          h += '<div class="list">' + bad.map(function (r) { return '<details class="it"><summary><span class="st ' + (r.s > 0 ? 'mid">◐' : 'bad">✗') + '</span><span>' + plainHTML(r.it) + '</span></summary><div class="body">' + solutionHTML(r.it, r.p !== undefined) + '</div></details>'; }).join('') + '</div>' +
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
        view.innerHTML = '<div class="nav"><span class="clock' + (c.left < 60 ? ' low' : '') + '" id="clock">⏱ ' + c.txt + '</span><button id="submit">Abgeben</button></div>' +
          '<div class="dots">' + queue.map(function (_, i) { return '<button data-i="' + i + '" class="' + (i === cur ? 'cur ' : '') + (answeredAt(i) ? 'done' : '') + '">' + (i + 1) + '</button>'; }).join('') + '</div>' +
          '<div class="meta"><span>Frage ' + (cur + 1) + ' / ' + queue.length + '</span><span>' + TYPES[it.type] + '</span></div><div class="card">' + questionBody(p, Array.isArray(ans[cur]) ? ans[cur] : null) + '</div>' +
          '<div class="row"><button class="ghost" id="prev"' + (cur === 0 ? ' disabled' : '') + '>‹ Zurück</button><button class="ghost" id="nxt"' + (cur === queue.length - 1 ? ' disabled' : '') + '>Weiter ›</button></div>';
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
        if (el) { el.textContent = '⏱ ' + c.txt; el.classList.toggle('low', c.left < 60); }
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
            var cls = r.s === 1 ? 'ok' : r.s > 0 ? 'mid' : 'bad', sym = r.s === 1 ? '✓' : r.s > 0 ? '◐' : '✗';
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

  function searchView(q0) {
    var filter = 'all';
    view.innerHTML = '<h1>Suche</h1><div class="searchbox" id="sbox"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>' +
      '<input id="q" type="search" placeholder="Begriff oder Satz suchen …" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="search" aria-label="Suche">' +
      '<button class="clear" id="clear" aria-label="Suche löschen">✕</button></div><div id="res"></div>';
    var input = $('#q'), box = $('#sbox'); input.value = q0;
    function setLast(word, replaceAll) {
      var parts = input.value.replace(/\s+$/, '').split(/\s+/); if (replaceAll) parts = [word]; else parts[parts.length - 1] = word;
      input.value = parts.join(' ') + (replaceAll ? '' : ' '); render(); input.focus();
    }
    function render() {
      var q = input.value.trim(); box.classList.toggle('has', input.value.length > 0);
      try { history.replaceState(null, '', q ? '#/suche?q=' + encodeURIComponent(q) : '#/suche'); } catch (e) {}
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
      // Vorschläge: Wortende ergänzen, sonst Tippfehler korrigieren
      var sug = '', last = toks[toks.length - 1], typing = !/\s$/.test(input.value);
      var ps = typing && last.length >= 2 ? prefixSug(last) : [];
      if (ps.length) sug = chips(ps.map(function (v) { return v.w; }), '');
      else if (!list.length) {
        var bad = toks.filter(function (t) { return !SEARCH.some(function (e) { return e._h.indexOf(t) >= 0 || e._t.indexOf(t) >= 0; }); }), fz = bad.length ? fuzzySug(bad[bad.length - 1]) : [];
        if (fz.length) { sug = '<p class="sugnote">Meintest du:</p>' + chips(fz.map(function (v) { return v.w; }), 'ai'); sug = sug.replace(/class="sugchip ai"/g, 'class="sugchip ai" data-fix="' + esc(bad[bad.length - 1]) + '"'); }
      }
      var counts = { all: list.length }; list.forEach(function (x) { counts[x.e.s] = (counts[x.e.s] || 0) + 1; });
      var subs = C.subjects.filter(function (s) { return !isHidden(s.id) && SEARCH.some(function (e) { return e.s === s.id; }); });
      var f = '<div class="filters"><button data-f="all" class="' + (filter === 'all' ? 'on' : '') + '">Alle (' + counts.all + ')</button>' + subs.map(function (s) {
        return '<button data-f="' + s.id + '" class="' + (filter === s.id ? 'on' : '') + '"><span class="sw" style="background:var(--c-' + s.id + ')"></span>' + esc(s.name) + ' (' + (counts[s.id] || 0) + ')</button>';
      }).join('') + '</div>';
      var shown = list.filter(function (x) { return filter === 'all' || x.e.s === filter; });
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
  function allSubj() { return C.subjects.concat(DB.log.some(function (e) { return e[1] === 'own'; }) ? [{ id: 'own', name: 'Eigene Karten' }] : []); }
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
          '</span><div class="bar"><div style="width:' + (f.cards.length ? k / f.cards.length * 100 : 0) + '%"></div></div><span class="go">Öffnen ›</span></div></a>';
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
      var h = '<div class="nav"><a href="#/neu">‹ Neu</a></div><h1 style="font-size:1.55rem">' + esc(f.name) + '</h1><p class="sub">' + f.cards.length + (f.cards.length === 1 ? ' Karte' : ' Karten') + '</p>';
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
    if (b.settings) a.settings = Object.assign(a.settings, b.settings);
  }
  var openSec = {};
  function settingsView() {
    var st = DB.settings;
    var h = '<h1>Einstellungen</h1><p class="sub" style="margin-bottom:12px">' + esc(appName()) + '</p>' +
      '<div class="group"><h3>Persönlich</h3>' +
      '<div class="setrow"><div class="l"><b>Dein Name</b><small>Aus „Konstis Lernkiste“ wird z. B. „Annas Lernkiste“. Leer lassen für den Standardnamen.</small></div>' +
      '<input class="txt" id="uname" type="text" maxlength="20" value="' + esc(st.name || '') + '" placeholder="Name" autocomplete="off" autocapitalize="words" spellcheck="false" aria-label="Dein Name"></div></div>' +
      '<div class="group"><h3>Darstellung</h3>' +
      '<div class="setrow"><div class="l"><b>Design</b></div>' + segHTML('theme', [['dark', 'Dunkel'], ['light', 'Hell'], ['auto', 'System']], st.theme) + '</div>' +
      '<div class="setrow"><div class="l"><b>Schriftgröße</b></div>' + segHTML('font', [[0.9, 'Klein'], [1, 'Mittel'], [1.15, 'Groß']], st.font) + '</div></div>' +
      '<div class="group"><h3>Karteikarten</h3>' +
      '<div class="setrow"><div class="l"><b>Standard-Filter</b><small>Welche Karten zuerst erscheinen</small></div>' + segHTML('cardFilter', [['red', 'Rot markiert'], ['all', 'Alle']], st.cardFilter) + '</div>' +
      '<div class="setrow"><div class="l"><b>Reihenfolge</b></div>' + segHTML('cardOrder', [['script', 'Skript'], ['shuffle', 'Gemischt']], st.cardOrder) + '</div></div>' +
      '<div class="group"><h3>Tests</h3>' +
      '<div class="setrow"><div class="l"><b>Fragen pro Runde</b></div>' + segHTML('testN', [[5, '5'], [10, '10'], [0, 'Alle']], st.testN) + '</div>' +
      '<div class="setrow"><div class="l"><b>Klausur: Minuten</b></div>' + segHTML('examMin', [[10, '10'], [20, '20'], [30, '30']], st.examMin) + '</div>' +
      '<div class="setrow"><div class="l"><b>Klausur: Fragen</b></div>' + segHTML('examN', [[8, '8'], [12, '12'], [16, '16']], st.examN) + '</div></div>' +
      '<div class="group"><h3>Motivation</h3>' +
      '<div class="setrow"><div class="l"><b>Heute fällig</b><small>Wiederholung nach 1, 3, 7 und 14 Tagen</small></div>' + segHTML('mDue', [[0, 'Aus'], [1, 'An']], st.mDue) + '</div>' +
      '<div class="setrow"><div class="l"><b>Tagesziel</b><small>Antworten pro Tag</small></div>' + segHTML('mGoal', [[0, 'Aus'], [10, '10'], [20, '20'], [30, '30'], [50, '50']], st.mGoal) + '</div>' +
      '<div class="setrow"><div class="l"><b>Lerntage-Kette</b><small>Ein Pausetag pro Woche reißt sie nicht</small></div>' + segHTML('mChain', [[0, 'Aus'], [1, 'An']], st.mChain) + '</div>' +
      '<div class="setrow"><div class="l"><b>Klausur-Countdown</b></div>' + segHTML('mCount', [[0, 'Aus'], [1, 'An']], st.mCount) + '</div>' +
      '<div class="setrow"><div class="l"><b>Fragen-Übersicht</b><small>Mosaik im Kapitel</small></div>' + segHTML('mMosaic', [[0, 'Aus'], [1, 'An']], st.mMosaic) + '</div>' +
      '<div class="setrow"><div class="l"><b>Abzeichen</b><small>Im Verlauf</small></div>' + segHTML('mBadges', [[0, 'Aus'], [1, 'An']], st.mBadges) + '</div></div>' +
      '<div class="group"><h3>Daten und Backup</h3>' +
      '<div class="setrow"><div class="l"><b>Backup speichern</b><small>Lernstand, Verlauf, eigene Karten und Einstellungen als Datei</small></div><button class="actbtn" id="bShare">Datei</button></div>' +
      '<div class="setrow"><div class="l"><b>Backup als Text kopieren</b><small>Zum Einfügen auf einem anderen Gerät</small></div><button class="actbtn" id="bCopy">Kopieren</button></div>' +
      '<div class="setrow"><div class="l"><b>Backup einspielen</b><small>Aus Datei oder eingefügtem Text</small></div><span style="display:flex;gap:6px"><button class="actbtn" id="bFile">Datei</button><button class="actbtn" id="bPaste">Text</button></span></div>' +
      '<div id="impbox"></div><input type="file" id="file" accept=".json,application/json,text/plain" style="display:none">' +
      '<div class="setrow"><div class="l"><b>Verlauf löschen</b></div><button class="actbtn danger" id="bLog">Löschen</button></div>' +
      '<div class="setrow"><div class="l"><b>Lernstand zurücksetzen</b><small>Alle Fächer, Einstellungen bleiben</small></div><button class="actbtn danger" id="bProg">Zurücksetzen</button></div></div>' +
      '<div class="group"><h3>Feedback</h3>' +
      '<div class="fbbox"><div class="l"><b>Feedback / Ideen senden</b><small>Schreib, was dir fehlt, was nicht klappt oder besser sein könnte. Anonym, ohne Namen. Bitte keine persönlichen Daten hineinschreiben.</small></div>' +
      '<textarea id="fbText" class="fbtext" maxlength="' + FB_MAX + '" placeholder="Deine Nachricht …" aria-label="Feedback"></textarea>' +
      '<input type="text" id="fbWeb" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">' +
      '<div class="fbrow"><small id="fbInfo" class="fbinfo">' + fbInfo() + '</small><button class="actbtn" id="fbSend" disabled>Senden</button></div></div></div>' +
      '<div class="group"><h3>App</h3>' +
      '<div class="setrow"><div class="l"><b>Version</b><small>' + esc(C.version) + '</small></div><button class="actbtn" id="bUpd">Nach Update suchen</button></div>' +
      '<div class="setrow"><div class="l"><b>Offline</b><small>Nach dem ersten Öffnen mit Internet funktioniert die App ohne Netz.</small></div></div>' +
      '<div class="setrow"><div class="l"><b>Anonyme Nutzungsstatistik</b><small>Ohne personenbezogene Daten: zählt nur App-Starts und geöffnete Fächer. Kein Name, keine IP-Adresse, keine Geräte-ID, kein Lernstand. Niemand ist daran erkennbar, auch nicht für mich.</small></div>' + segHTML('stats', [[0, 'Aus'], [1, 'An']], st.stats ? 1 : 0) + '</div>' +
      '<div class="setrow tap" id="privRow" role="button" tabindex="0"><div class="l"><b>Datenschutz</b><small>Was die App speichert und sendet</small></div><button class="actbtn" id="bPriv" type="button">Lesen</button></div></div>' +
      '<p class="note" style="text-align:center">Dein Lernstand liegt nur auf diesem Gerät. Mit dem Backup sicherst du ihn.</p>';
    view.innerHTML = h;
    $$('#view .group').forEach(function (g) {
      var t = $('h3', g); if (!t || t.textContent === 'Persönlich') return;
      var name = t.textContent, body = document.createElement('div'), btn = document.createElement('button');
      body.className = 'gbody'; while (t.nextSibling) body.appendChild(t.nextSibling); g.appendChild(body);
      btn.type = 'button'; btn.className = 'ghead'; btn.innerHTML = '<span>' + esc(name) + '</span><svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>';
      function set(on) { g.classList.toggle('open', on); btn.setAttribute('aria-expanded', on ? 'true' : 'false'); openSec[name] = on; }
      btn.onclick = function () { set(!g.classList.contains('open')); };
      t.replaceWith(btn); set(!!openSec[name]);
    });
    $$('.seg[data-k] button').forEach(function (b) {
      b.onclick = function () {
        var k = b.parentNode.dataset.k, v = b.dataset.v; DB.settings[k] = isNaN(v) ? v : +v; save(); applyPrefs(); if (k === 'stats' && !DB.settings.stats) statForget();
        var y = window.scrollY; settingsView(); window.scrollTo(0, y);
      };
    });
    $('#uname').addEventListener('input', function () {
      DB.settings.name = this.value.slice(0, 20); save(); document.title = appName(); $('#view .sub').textContent = appName();
    });
    $('#bShare').onclick = shareFile; $('#bCopy').onclick = copyText;
    $('#privRow').onclick = function () { openTile('Datenschutz', privacyHTML()); };
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
    // Fremde Backups säubern: Namen, IDs, Einstellungen ohne HTML-Zeichen; Kartentexte werden beim Anzeigen ohnehin maskiert (rich).
    function cleanImport(o, qa) {
      if (typeof o === 'string') return qa ? o.slice(0, 5000) : o.replace(/[<>"'`]/g, '').slice(0, 300);
      if (typeof o === 'number') return isFinite(o) ? o : 0;
      if (typeof o === 'boolean' || o === null) return o;
      if (Array.isArray(o)) return o.slice(0, 50000).map(function (x) { return cleanImport(x, qa); });
      if (typeof o === 'object') { var r = {}; Object.keys(o).forEach(function (k) { if (k === '__proto__' || k === 'constructor' || k === 'prototype') return; r[k.replace(/[<>"'`]/g, '')] = cleanImport(o[k], k === 'q' || k === 'a'); }); return r; }
      return null;
    }
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
    twoStep('#bLog', 'Löschen', function () { DB.log = []; save(); toast('Verlauf gelöscht'); settingsView(); });
    twoStep('#bProg', 'Zurücksetzen', function () { DB.progress = {}; DB.tests = {}; save(); toast('Lernstand zurückgesetzt'); settingsView(); });
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
  window.addEventListener('online', function () { netState(); toast('Wieder online'); fbFlush(); });
  setTimeout(function () { fbFlush(); }, 3000);
  window.addEventListener('offline', netState);
  netState();
  window.addEventListener('hashchange', route);
  route();
  statPing('start');
  document.addEventListener('visibilitychange', statVisible);
  // ---- Automatische Update-Prüfung (höchstens alle 20 Stunden) und Hinweis, nie mitten im Test
  var updReady = false, updDismissed = false, bar = document.createElement('div');
  bar.className = 'updbar'; bar.setAttribute('role', 'status');
  bar.innerHTML = '<span>Update bereit</span><button id="updGo">Neu laden</button><button class="x" id="updX" aria-label="Später">✕</button>';
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
