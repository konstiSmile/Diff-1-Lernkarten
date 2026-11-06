(function () {
  'use strict';
  var C = window.CONTENT;
  var KEY = 'lernkiste-v1';
  var DEFAULTS = { theme: 'dark', font: 1, cardFilter: 'red', name: '', cardOrder: 'script', testN: 10, examMin: 20, examN: 12 };

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
    var t = document.createElement('div'); t.className = 'toast'; t.appendChild(document.createTextNode(msg));
    if (actionLabel) {
      var b = document.createElement('button'); b.type = 'button'; b.className = 'toastact'; b.textContent = actionLabel;
      b.onclick = function () { t.remove(); action(); }; t.appendChild(b);
    }
    document.body.appendChild(t);
    setTimeout(function () { t.remove(); }, actionLabel ? 6000 : 2600);
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
    d.v = 1; d.recent = d.recent || []; d.progress = d.progress || {}; d.tests = d.tests || {}; d.log = d.log || []; d.hidden = d.hidden || [];
    d.settings = Object.assign({}, DEFAULTS, d.settings || {});
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
    if (fresh) { migrate(d); try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) {} }
    return d;
  })();
  function save() {
    if (DB.log.length > 20000) DB.log.splice(0, DB.log.length - 20000);
    try { localStorage.setItem(KEY, JSON.stringify(DB)); } catch (e) {}
  }
  function logAns(fach, id, score) { DB.log.push([Date.now(), fach, id, Math.round(score * 100) / 100]); }
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
    else if (p[0] === 'neu') { tab = 'neu'; neuView(); }
    else if (p[0] === 'einstellungen') { tab = 'set'; settingsView(); }
    else if (p[0] === 'f' && p[1] && !p[2]) fachView(p[1]);
    else if (p[0] === 'f' && p[1] && p[2]) chapterView(p[1], p[2], r.q);
    else homeView();
    setTab(tab);
    if (!(p[0] === 'f' && p[2] && r.q.c)) window.scrollTo(0, 0);
  }

  // ====================================================================== Start / Fach
  function subjStats(s) {
    var known = 0, total = 0, items = 0, best = null, allPlaceholder = true;
    s.chapters.forEach(function (ch) {
      if (!ch.placeholder) allPlaceholder = false;
      if (ch.kind === 'cards') { total += ch.cards.length; ch.cards.forEach(function (c) { if (DB.progress[c.id] === 'known') known++; }); }
      else { items += ch.items.length; var b = tests(s.id, ch.id).best.exam; if (b !== undefined && (best === null || b > best)) best = b; }
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
      '<a class="fakesearch" href="#/suche"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>Begriff oder Satz suchen …</a><div class="grid fach">';
    vis.forEach(function (s) {
      var st = subjStats(s);
      h += '<div class="tilewrap" data-sid="' + s.id + '"><div class="hidehint">Ausblenden</div><a class="tile s-' + s.id + '" href="#/f/' + s.id + '">' + (st.placeholder ? '<span class="badge">Gerüst</span>' : '') +
        '<div><h2 class="name">' + esc(s.name) + '</h2><p class="desc">' + esc(s.desc) + '</p></div>' +
        '<div class="foot"><span>' + esc(st.txt) + '</span><div class="bar"><div style="width:' + st.pct + '%"></div></div><span class="go">Öffnen ›</span></div></a>' +
        '<button type="button" class="tilemenu" aria-label="Mehr zu ' + esc(s.name) + '">⋯</button></div>';
    });
    h += '</div>';
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
  function fachView(sid) {
    var s = subj(sid); if (!s) return homeView();
    var h = '<div class="nav"><a href="#/">‹ Start</a></div><h1>' + esc(s.name) + '</h1><p class="sub">' + esc(s.desc) + '</p><div class="grid">';
    s.chapters.forEach(function (ch) {
      var txt, pct = 0;
      if (ch.kind === 'cards') { var k = ch.cards.filter(function (c) { return DB.progress[c.id] === 'known'; }).length; txt = k ? k + ' von ' + ch.cards.length + ' gewusst' : ch.cards.length + ' Karten'; pct = k / ch.cards.length * 100; }
      else { var b = tests(sid, ch.id).best.exam; txt = ch.items.length + ' Fragen' + (b !== undefined ? ' · Klausur ' + b + ' %' : ''); pct = b || 0; }
      h += '<a class="tile s-' + sid + '" href="#/f/' + sid + '/' + ch.id + '">' + (ch.placeholder ? '<span class="badge">Gerüst</span>' : '') +
        '<div><h2 class="name">' + esc(ch.title) + '</h2><p class="desc">' + esc(ch.kind === 'cards' ? 'Karteikarten' : 'Tests: Multiple Choice, Lückentext, Richtig/Falsch, Zeit-Simulation') + '</p></div>' +
        '<div class="foot"><span>' + esc(txt) + '</span><div class="bar"><div style="width:' + pct + '%"></div></div><span class="go">Öffnen ›</span></div></a>';
    });
    view.innerHTML = h + '</div>';
  }
  function chapterView(sid, cid, q) {
    var s = subj(sid), ch = chap(sid, cid); if (!s || !ch) return homeView();
    view.className = 's-' + sid;
    if (ch.kind === 'cards') cardsView(s, ch, q); else testsView(s, ch, q);
  }

  // ====================================================================== Karteikarten
  function cardsView(s, ch, q) {
    var cards = ch.cards, byId = {}; cards.forEach(function (c) { byId[c.id] = c; });
    var st = DB.settings, filter = q.c ? 'all' : st.cardFilter;
    var order = cards.map(function (c) { return c.id; }); if (st.cardOrder === 'shuffle') order = shuffle(order);
    var deck = [], pos = 0, flipped = false, confirmReset = false;
    var terms = (q.hl || '').split(/\s+/).filter(function (t) { return t.length > 1; });

    function build(keep) {
      var cur = deck[pos];
      deck = order.filter(function (id) { var c = byId[id]; return filter === 'red' ? c.red : filter === 'again' ? DB.progress[id] === 'again' : true; });
      pos = keep && deck.indexOf(cur) >= 0 ? deck.indexOf(cur) : 0; flipped = false;
    }
    function draw() {
      var total = deck.length, nRed = cards.filter(function (c) { return c.red; }).length;
      var nAgain = cards.filter(function (c) { return DB.progress[c.id] === 'again'; }).length;
      var known = deck.filter(function (id) { return DB.progress[id] === 'known'; }).length;
      var h = '<div class="nav"><a href="#/f/' + s.id + '">‹ ' + esc(s.name) + '</a></div>' +
        '<h1 style="font-size:1.5rem">' + esc(ch.title) + '</h1><p class="sub" style="margin-bottom:0">' + esc(ch.sub || '') + '</p>' +
        '<div class="seg" id="seg"><button data-f="red" class="' + (filter === 'red' ? 'on' : '') + '"><span class="dot"></span>Rot markiert (' + nRed + ')</button>' +
        '<button data-f="all" class="' + (filter === 'all' ? 'on' : '') + '">Alle (' + cards.length + ')</button>' +
        '<button data-f="again" class="' + (filter === 'again' ? 'on' : '') + '">Nochmal (' + nAgain + ')</button></div>' +
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
      var id = deck[pos]; DB.progress[id] = val; logAns(s.id, id, val === 'known' ? 1 : 0); save();
      if (filter === 'again' && val === 'known') { deck.splice(pos, 1); if (pos >= deck.length) pos = Math.max(0, deck.length - 1); flipped = false; draw(); return; }
      if (pos < deck.length - 1) pos++;
      flipped = false; draw(); window.scrollTo(0, 0);
    }
    function onKey(e) {
      if (/INPUT|TEXTAREA/.test((e.target || {}).tagName || '')) return;
      if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); flip(); }
      else if (e.key === 'ArrowRight') go(1); else if (e.key === 'ArrowLeft') go(-1);
    }
    document.addEventListener('keydown', onKey); onLeave(function () { document.removeEventListener('keydown', onKey); });

    build(false);
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
  function grade(it, ans) {
    if (it.type === 'mc') return ans === it.correct ? 1 : 0;
    if (it.type === 'tf') return ans === it.answer ? 1 : 0;
    var parts = gapParts(it).filter(function (p) { return p.g; }), ok = 0;
    if (!parts.length) return 0;
    parts.forEach(function (p, k) { var v = norm((ans && ans[k]) || ''); if (v && p.g.some(function (a) { return norm(a) === v; })) ok++; });
    return ok / parts.length;
  }
  function solutionHTML(it) {
    var s = it.type === 'mc' ? '<div class="tip"><b>Richtig:</b> ' + it.options[it.correct] + '</div>' :
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
    function pool(type) { return ITEMS.filter(function (i) { return i.type === type; }); }
    function nav(extra) { return '<div class="nav"><a href="#/f/' + s.id + '">‹ ' + esc(s.name) + '</a>' + (extra || '') + '</div>'; }
    function prep(id) { var it = BYID[id]; return { it: it, order: it.type === 'mc' ? shuffle(it.options.map(function (_, i) { return i; })) : null }; }
    function finishLog(r) {
      logAns(s.id, r.it.id, r.s);
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
      h += '<div class="modes">' + MODES.map(function (m) {
        var c = m.id === 'exam' ? total : counts[m.id], b = T.best[m.id];
        return '<button class="mode" data-m="' + m.id + '"' + (c ? '' : ' disabled') + '><span class="ico">' + m.ico + '</span><span><span class="t">' + m.name + '</span><br><span class="d">' + m.desc + '</span></span>' +
          '<span class="r">' + c + ' Fragen' + (b !== undefined ? '<b>Bestwert ' + b + ' %</b>' : '') + '</span></button>';
      }).join('') + '</div>';
      var wr = T.wrong.filter(function (id) { return BYID[id]; });
      if (wr.length) h += '<div class="row" style="margin-top:14px"><button class="ghost" id="wrong">Falsche Fragen wiederholen (' + wr.length + ')</button></div>';
      h += '<div class="tools"><button id="reset">Fortschritt zurücksetzen</button></div>';
      view.innerHTML = h;
      $$('.chip').forEach(function (b) { b.onclick = function () { st.testN = parseInt(b.dataset.n, 10); save(); hub(); }; });
      $$('.mode').forEach(function (b) { b.onclick = function () { start(b.dataset.m); }; });
      var wb = $('#wrong'); if (wb) wb.onclick = function () { run(shuffle(wr).map(prep), 'wrong', 'Falsche Fragen'); };
      $('#reset').onclick = function () {
        var b = $('#reset');
        if (b.dataset.sure) { T.best = {}; T.wrong = []; save(); hub(); } else { b.textContent = 'Wirklich zurücksetzen?'; b.dataset.sure = 1; }
      };
    }
    function start(mode) {
      if (mode === 'exam') return examSetup();
      var ids = shuffle(pool(mode)).map(function (i) { return i.id; }); if (st.testN) ids = ids.slice(0, st.testN);
      run(ids.map(prep), mode, TYPES[mode]);
    }
    function questionBody(p, values) {
      var it = p.it;
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
        view.innerHTML = h; window.scrollTo(0, 0);
        $('#quit').onclick = hub;
        function answered(score) {
          if (done) return; done = true; results.push({ it: it, s: score });
          $('#fb').innerHTML = '<div class="fb ' + (score === 1 ? 'ok' : 'bad') + '">' + (score === 1 ? '✓ Richtig' : score > 0 ? '◐ Teilweise richtig' : '✗ Nicht ganz') + '</div>' +
            (it.expl ? '<div class="tip' + (it.warn ? ' warn' : '') + '">' + it.expl + '</div>' : '') +
            '<div class="row"><button class="primary" id="next">' + (i === queue.length - 1 ? 'Ergebnis ›' : 'Weiter ›') + '</button></div>';
          $('#next').onclick = function () { i++; show(); };
        }
        if (it.type === 'mc') {
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
        save();
        var bad = results.filter(function (r) { return r.s < 1; });
        var h = nav() + '<div class="card"><div class="score"><div class="big">' + pct + ' %</div><div class="note">' + fmt(pts) + ' von ' + queue.length + ' richtig · ' + title + '</div></div></div>';
        if (bad.length) {
          h += '<div class="list">' + bad.map(function (r) { return '<details class="it"><summary><span class="st bad">✗</span><span>' + plainHTML(r.it) + '</span></summary><div class="body">' + solutionHTML(r.it) + '</div></details>'; }).join('') + '</div>' +
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
      var qs = { mc: shuffle(pool('mc')), tf: shuffle(pool('tf')), gap: shuffle(pool('gap')) }, order = ['mc', 'tf', 'gap'], queue = [], k = 0, guard = 0;
      while (queue.length < n && guard++ < 500) { var t = order[k++ % 3]; if (qs[t].length) queue.push(qs[t].shift()); }
      queue = queue.map(function (it) { return prep(it.id); });
      var ans = queue.map(function () { return null; }), cur = 0, end = Date.now() + minutes * 60000, timer = null, finished = false;
      setImm(true);
      onLeave(function () { clearInterval(timer); });
      function stash() { if (queue[cur].it.type === 'gap') ans[cur] = $$('input.gap').map(function (x) { return x.value; }); }
      function clockText() { var left = Math.max(0, Math.round((end - Date.now()) / 1000)); return { txt: Math.floor(left / 60) + ':' + ('0' + (left % 60)).slice(-2), left: left }; }
      function answeredAt(i) { var a = ans[i]; if (a === null || a === undefined) return false; return Array.isArray(a) ? a.some(function (v) { return v.trim(); }) : true; }
      function show() {
        var p = queue[cur], it = p.it, c = clockText();
        view.innerHTML = '<div class="nav"><span class="clock' + (c.left < 60 ? ' low' : '') + '" id="clock">⏱ ' + c.txt + '</span><button id="submit">Abgeben</button></div>' +
          '<div class="dots">' + queue.map(function (_, i) { return '<button data-i="' + i + '" class="' + (i === cur ? 'cur ' : '') + (answeredAt(i) ? 'done' : '') + '">' + (i + 1) + '</button>'; }).join('') + '</div>' +
          '<div class="meta"><span>Frage ' + (cur + 1) + ' / ' + queue.length + '</span><span>' + TYPES[it.type] + '</span></div><div class="card">' + questionBody(p, Array.isArray(ans[cur]) ? ans[cur] : null) + '</div>' +
          '<div class="row"><button class="ghost" id="prev"' + (cur === 0 ? ' disabled' : '') + '>‹ Zurück</button><button class="ghost" id="nxt"' + (cur === queue.length - 1 ? ' disabled' : '') + '>Weiter ›</button></div>';
        if (it.type === 'mc') $$('.opt').forEach(function (b) { if (ans[cur] === parseInt(b.dataset.o, 10)) b.classList.add('sel'); b.onclick = function () { ans[cur] = parseInt(b.dataset.o, 10); show(); }; });
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
        var pts = 0, rows = queue.map(function (p, i) { var sc = grade(p.it, ans[i]); pts += sc; return { it: p.it, s: sc }; });
        var pct = Math.round(pts / queue.length * 100);
        rows.forEach(finishLog);
        if (T.best.exam === undefined || pct > T.best.exam) T.best.exam = pct;
        save();
        var used = Math.round((Date.now() - (end - minutes * 60000)) / 1000);
        view.innerHTML = nav() + '<div class="card"><div class="score"><div class="big">' + fmt(pts) + ' / ' + queue.length + '</div><div class="note">' + pct + ' % · Note ' + noteFor(pct) + ' (Richtwert)' +
          (timeout ? ' · Zeit abgelaufen' : ' · ' + Math.floor(used / 60) + ':' + ('0' + used % 60).slice(-2) + ' Min benötigt') + '</div></div></div><div class="list">' +
          rows.map(function (r) {
            var cls = r.s === 1 ? 'ok' : r.s > 0 ? 'mid' : 'bad', sym = r.s === 1 ? '✓' : r.s > 0 ? '◐' : '✗';
            return '<details class="it"><summary><span class="st ' + cls + '">' + sym + '</span><span>' + plainHTML(r.it) + '</span></summary><div class="body">' + solutionHTML(r.it) + '</div></details>';
          }).join('') + '</div><div class="row" style="margin-top:14px"><button class="ghost" id="menu">Zum Menü</button><button class="primary" id="again">Neue Klausur</button></div>';
        window.scrollTo(0, 0); $('#menu').onclick = hub; $('#again').onclick = examSetup;
      }
      show(); timer = setInterval(tick, 500);
    }

    function single(id, terms) {
      var it = BYID[id]; if (!it) return hub();
      view.innerHTML = nav('<button id="all">Alle Tests</button>') +
        '<div class="meta"><span>' + esc(ch.title) + ' · ' + TYPES[it.type] + '</span><span>' + esc(it.src || '') + '</span></div>' +
        '<div class="card"><div class="qtext">' + (it.type === 'gap' ? gapSolution(it) : plainHTML(it)) + '</div>' +
        (it.type === 'mc' ? '<div class="opts">' + it.options.map(function (o, i) { return '<div class="opt' + (i === it.correct ? ' ok' : '') + '"><span class="k">' + 'ABCD'.charAt(i) + '</span><span>' + o + '</span></div>'; }).join('') + '</div>' : '') +
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
  function verlaufView() {
    var now = new Date(), i, MON = ['Jan.', 'Feb.', 'März', 'Apr.', 'Mai', 'Juni', 'Juli', 'Aug.', 'Sept.', 'Okt.', 'Nov.', 'Dez.'];
    var WD = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'], WDL = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
    var today0 = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    // Einträge pro Tag: { fach: {n, s} }
    var map = {};
    DB.log.forEach(function (e) { var d = dayKey(e[0]), m = map[d] = map[d] || {}, f = m[e[1]] = m[e[1]] || { n: 0, s: 0 }; f.n++; f.s += (typeof e[3] === 'number' ? e[3] : 0); });
    function dayData(d) { return map[dayKey(d.getTime())] || {}; }
    function total(c) { return Object.keys(c).reduce(function (a, k) { return a + c[k].n; }, 0); }
    function merge(list) { var r = {}; list.forEach(function (c) { Object.keys(c).forEach(function (k) { var f = r[k] = r[k] || { n: 0, s: 0 }; f.n += c[k].n; f.s += c[k].s; }); }); return r; }
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
        '<div class="stats"><div class="stat"><b>' + tod + '</b><span>heute</span></div><div class="stat"><b>' + wk + '</b><span>7 Tage</span></div><div class="stat"><b>' + streakOf() + '</b><span>Tage in Folge</span></div></div>' +
        '<div class="seg" id="vseg"><button data-r="w" class="' + (vRange === 'w' ? 'on' : '') + '">Woche</button><button data-r="m" class="' + (vRange === 'm' ? 'on' : '') + '">Monat</button><button data-r="j" class="' + (vRange === 'j' ? 'on' : '') + '">12 Wochen</button></div>';
      if (!DB.log.length) h += '<div class="note" style="text-align:center;padding:10px 6px 20px">Hier erscheint dein Verlauf, sobald du Karten oder Fragen beantwortest.</div>';
      h += '<div class="group" style="padding:12px 14px"><div class="chart' + (vRange === 'm' ? ' dense' : '') + '">' + bs.map(function (x) {
        var t = total(x.c), hh = Math.round(t / max * 108);
        var stack = C.subjects.map(function (s) { var n = x.c[s.id] ? x.c[s.id].n : 0; return n ? '<i style="height:' + Math.max(3, Math.round(n / t * hh)) + 'px;background:var(--c-' + s.id + ')"></i>' : ''; }).join('');
        return '<button type="button" class="day' + (x.key === vSel ? ' sel' : '') + '" data-k="' + x.key + '" aria-label="' + esc(x.title) + ': ' + t + '"><div class="n">' + (vRange === 'm' ? '' : (t || '')) + '</div><div class="stack">' + stack + '</div><div class="lab">' + x.lab + '</div></button>';
      }).join('') + '</div><div class="legend">' + C.subjects.map(function (s) { return '<span><i class="sw" style="background:var(--c-' + s.id + ')"></i>' + esc(s.name) + '</span>'; }).join('') + '</div></div>';
      if (sel) {
        var t2 = total(sel.c);
        h += '<div class="group daydet"><div class="dhead"><b>' + esc(sel.title) + '</b><span>' + (t2 ? t2 + (t2 === 1 ? ' Antwort' : ' Antworten') : 'nichts gelernt') + '</span></div>' +
          C.subjects.filter(function (s) { return sel.c[s.id]; }).map(function (s) {
            var f = sel.c[s.id], pct = Math.round(f.s / f.n * 100);
            return '<div class="drow"><i class="sw" style="background:var(--c-' + s.id + ')"></i><span class="nm">' + esc(s.name) + '</span><span class="ct">' + f.n + ' · ' + pct + ' % gewusst/richtig</span></div>';
          }).join('') + '</div>';
      } else if (DB.log.length) h += '<p class="note" style="text-align:center">Tippe einen Balken an für Details.</p>';
      h += '<p class="note" style="text-align:center">Gezählt wird jede beantwortete Karte und Testfrage. Im Zeitraum: ' + rng + ' in ' + days + ' Tagen.</p>';
      view.innerHTML = h;
      $$('#vseg button').forEach(function (b) { b.onclick = function () { vRange = b.dataset.r; vSel = null; render(); }; });
      $$('.chart .day').forEach(function (b) { b.onclick = function () { vSel = (vSel === b.dataset.k) ? null : b.dataset.k; render(); }; });
    }
    vSel = null; render();
  }

  function neuView() {
    view.innerHTML = '<h1>Neu</h1><p class="sub">Eigene Karten und Ordner</p><div class="group" style="padding:16px"><b>Kommt als Nächstes.</b>' +
      '<p class="note" style="margin:6px 0 0">Hier legst du bald eigene Karten und Ordner an, mit Symbol-Kacheln für Formeln. Bis dahin kannst du in den Einstellungen dein Backup sichern.</p></div>';
  }

  // ====================================================================== Einstellungen
  function segHTML(key, opts, val) {
    return '<div class="seg small" data-k="' + key + '">' + opts.map(function (o) { return '<button data-v="' + o[0] + '" class="' + (String(val) === String(o[0]) ? 'on' : '') + '">' + o[1] + '</button>'; }).join('') + '</div>';
  }
  function exportText() { return JSON.stringify({ app: 'lernkiste', v: 1, exported: new Date().toISOString(), data: DB }); }
  function shareFile() {
    var txt = exportText(), name = 'lernkiste-backup-' + dayKey(Date.now()) + '.json', blob = new Blob([txt], { type: 'application/json' }), file = null;
    try { file = new File([blob], name, { type: 'application/json' }); } catch (e) {}
    if (file && navigator.canShare && navigator.canShare({ files: [file] })) navigator.share({ files: [file], title: 'Lernkiste Backup' }).catch(function () {});
    else { var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name; document.body.appendChild(a); a.click(); setTimeout(function () { a.remove(); URL.revokeObjectURL(a.href); }, 1000); toast('Backup gespeichert'); }
  }
  function copyText() {
    var txt = exportText();
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(function () { toast('Backup kopiert'); }, function () { toast('Kopieren nicht möglich'); });
    else { var ta = document.createElement('textarea'); ta.value = txt; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); toast('Backup kopiert'); } catch (e) { toast('Kopieren nicht möglich'); } ta.remove(); }
  }
  function mergeInto(a, b) {
    Object.assign(a.progress, b.progress || {});
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
      '<div class="group"><h3>Daten und Backup</h3>' +
      '<div class="setrow"><div class="l"><b>Backup speichern</b><small>Lernstand, Verlauf und Einstellungen als Datei</small></div><button class="actbtn" id="bShare">Datei</button></div>' +
      '<div class="setrow"><div class="l"><b>Backup als Text kopieren</b><small>Zum Einfügen auf einem anderen Gerät</small></div><button class="actbtn" id="bCopy">Kopieren</button></div>' +
      '<div class="setrow"><div class="l"><b>Backup einspielen</b><small>Aus Datei oder eingefügtem Text</small></div><span style="display:flex;gap:6px"><button class="actbtn" id="bFile">Datei</button><button class="actbtn" id="bPaste">Text</button></span></div>' +
      '<div id="impbox"></div><input type="file" id="file" accept=".json,application/json,text/plain" style="display:none">' +
      '<div class="setrow"><div class="l"><b>Verlauf löschen</b></div><button class="actbtn danger" id="bLog">Löschen</button></div>' +
      '<div class="setrow"><div class="l"><b>Lernstand zurücksetzen</b><small>Alle Fächer, Einstellungen bleiben</small></div><button class="actbtn danger" id="bProg">Zurücksetzen</button></div></div>' +
      '<div class="group"><h3>Feedback</h3>' +
      '<div class="setrow soon"><div class="l"><b>Feedback / Ideen senden</b><small>Schreib uns, was dir fehlt oder besser sein könnte.</small></div><span class="soonbadge">Kommt bald</span></div></div>' +
      '<div class="group"><h3>App</h3>' +
      '<div class="setrow"><div class="l"><b>Version</b><small>' + esc(C.version) + '</small></div><button class="actbtn" id="bUpd">Nach Update suchen</button></div>' +
      '<div class="setrow"><div class="l"><b>Offline</b><small>Nach dem ersten Öffnen mit Internet funktioniert die App ohne Netz.</small></div></div></div>' +
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
        var k = b.parentNode.dataset.k, v = b.dataset.v; DB.settings[k] = isNaN(v) ? v : +v; save(); applyPrefs();
        var y = window.scrollY; settingsView(); window.scrollTo(0, y);
      };
    });
    $('#uname').addEventListener('input', function () {
      DB.settings.name = this.value.slice(0, 20); save(); document.title = appName(); $('#view .sub').textContent = appName();
    });
    $('#bShare').onclick = shareFile; $('#bCopy').onclick = copyText;
    function importFrom(text) {
      var o; try { o = JSON.parse(text); } catch (e) { toast('Das ist keine gültige Backup-Datei'); return; }
      if (!o || o.app !== 'lernkiste' || !o.data) { toast('Das ist kein Lernkiste-Backup'); return; }
      var d = normalizeDB(o.data), n = Object.keys(d.progress).length, l = d.log.length;
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
  window.addEventListener('online', function () { netState(); toast('Wieder online'); });
  window.addEventListener('offline', netState);
  netState();
  window.addEventListener('hashchange', route);
  route();
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
