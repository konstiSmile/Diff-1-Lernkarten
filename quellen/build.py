import re, json, os, shutil, importlib, datetime
from bs4 import BeautifulSoup
import tex

OUT = os.environ.get('LERNKISTE_OUT', '/home/claude/out2')
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
VERSION = datetime.date.today().isoformat() + '.1'
NAME = 'Konstis Lernkiste'

# ---------------------------------------------------------------- Diff 1 Karten (feste IDs)
CARD_IDS = ['reelle-zahlen', 'archimedes', 'vollstaendigkeit', 'folge', 'monotonie', 'beschraenktheit', 'monoton-beschr',
            'grenzwert', 'eindeutigkeit', 'konvergenz', 'konv-beschr', 'ungleichung', 'schrankenlemma', '1-durch-nk',
            'aequivalenzen', 'betrag', 'grenzwertsaetze', 'best-divergent', 'kehrwerte']
DIFF_KW = [
    'Körper angeordnet Archimedisch vollständig reelle Zahlen Eigenschaften', 'Archimedes archimedisch Axiom',
    'Supremum Infimum obere Schranke kleinste Schranke Vollständigkeit', 'Folge Folgenglied Index Abbildung',
    'Monotonie monoton wachsend fallend streng', 'beschränkt Schranke obere untere Beschränktheit', 'monotone Folge beschränkt',
    'Grenzwert Limes Epsilon Umgebung Konvergenz Quantoren Definition', 'Eindeutigkeit Grenzwert eindeutig',
    'konvergent divergent Nullfolge Konvergenz', 'konvergent beschränkt Kontraposition', 'Ungleichung Grenzübergang kleiner gleich',
    'Schrankenlemma Sandwich Einschnürungssatz Einschließungssatz', 'Nullfolge Schrankenlemma Potenz',
    'Äquivalenz Grenzwert Nullfolge Betrag', 'Betrag umgekehrte Dreiecksungleichung',
    'Grenzwertsätze Summe Produkt Quotient Rechenregeln', 'bestimmt divergent uneigentlich konvergent unendlich', 'Kehrwert Nullfolge unendlich']

src = open('quelle.html', encoding='utf-8').read()
soup = BeautifulSoup(src, 'html.parser')
raw = soup.select('#data .c')
assert len(raw) == len(CARD_IDS) == len(DIFF_KW), (len(raw), len(CARD_IDS))
cards, search = [], []
for i, c in enumerate(raw):
    cid = 'diff1-k1-' + CARD_IDS[i]
    q = c.select_one('.q').decode_contents(); a = c.select_one('.a').decode_contents()
    red = c['data-red'] == '1'
    cards.append(dict(id=cid, red=red, src=c['data-src'], q=tex.convert(q), a=tex.convert(a)))
    search.append(dict(s='diff1', title=c['data-src'], label='Karteikarte · Kap. 1' + (' · rot markiert' if red else ''),
                       route=f'/f/diff1/k1?c={cid}', kw=DIFF_KW[i], text=tex.plain(q) + ' — ' + tex.plain(a)))

TYPES = {'mc': 'Multiple Choice', 'tf': 'Richtig/Falsch', 'gap': 'Lückentext'}
def test_text(it):
    if it['type'] == 'mc': t = it['q'] + ' ' + ' / '.join(it['options'])
    elif it['type'] == 'tf': t = it['statement'] + (' Richtig.' if it['answer'] else ' Falsch.')
    else: t = re.sub(r'\{\{(.*?)\}\}', lambda m: m.group(1).replace('|', '/'), it['text'])
    return tex.plain(t + ' ' + it.get('expl', ''))
def conv_item(it):
    it = dict(it)
    for k in ('q', 'statement', 'text', 'expl'):
        if k in it: it[k] = tex.convert(it[k])
    if 'options' in it: it['options'] = [tex.convert(o) for o in it['options']]
    it.pop('kw', None); it.pop('placeholder', None)
    if not it.get('warn'): it.pop('warn', None)
    return it
def tests_chapter(modname, sid, cid, title, sub, placeholder):
    m = importlib.import_module(modname)
    if not placeholder:
        for it in m.ITEMS:
            search.append(dict(s=sid, title=it['src'], label=TYPES[it['type']], route=f"/f/{sid}/{cid}?q={it['id']}", kw=it.get('kw', ''), text=test_text(it)))
    return dict(id=cid, title=title, sub=sub, kind='tests', placeholder=placeholder, items=[conv_item(i) for i in m.ITEMS])

import data_pers
def pers_cards(key, title, sub, num):
    out = []
    for c in data_pers.CARDS[key]:
        cid = f"psy-pers-{key}-{c['key']}"
        out.append(dict(id=cid, red=False, src=c['src'], q=tex.convert(c['q']), a=tex.convert(c['a'])))
        search.append(dict(s='psy', title=c['src'], label=f'Karteikarte · Kap. {num}', route=f'/f/psy/{key}?c={cid}', kw=c['kw'], text=tex.plain(c['q']) + ' — ' + tex.plain(c['a'])))
    return dict(id=key, group='pers', title=title, sub=sub, kind='cards', placeholder=False, cards=out)
pers_tests = tests_chapter('data_pers', 'psy', 'tp', 'Tests · Kapitel 1 und 2', 'Multiple Choice, Richtig/Falsch, Lückentext, Zeit-Simulation', False)
pers_tests['group'] = 'pers'

CONTENT = dict(name=NAME, version=VERSION, subjects=[
    dict(id='diff1', name='Diff 1', desc='Differential- und Integralrechnung 1', chapters=[
        dict(id='k1', title='Kapitel 1 · Folgen und Grenzwerte', sub='Karteikarten aus dem Skript', kind='cards', placeholder=False, cards=cards),
        tests_chapter('data_diff1', 'diff1', 'tk1', 'Tests · Kapitel 1', 'Multiple Choice, Richtig/Falsch, Lückentext, Zeit-Simulation', False)]),
    dict(id='quer', name='Querschnitt', desc='Funktionen mehrerer Veränderlicher und mehr', chapters=[
        tests_chapter('data_querschnitt', 'quer', 'k10', 'Kapitel 10 · Funktionen mehrerer Veränderlicher', 'Tests zum Skript', False)]),
    dict(id='psy', name='Psycho 2', desc='Persönlichkeit, Entwicklung, Diagnostik', groups=[
        dict(id='pers', name='Persönlichkeitspsychologie', desc='Eigenschaften, Methoden, Theorien'),
        dict(id='entw', name='Entwicklungspsychologie', desc='Kommt später'),
        dict(id='diag', name='Diagnostische Psychologie', desc='Kommt später')], chapters=[
        pers_cards('k1', 'Kapitel 1 · Einführung und Eigenschaften', 'Karteikarten: Definition, Traits, Konstrukte', 1),
        pers_cards('k2', 'Kapitel 2 · Methoden', 'Karteikarten: Forschungsansätze, Korrelation, Faktorenanalyse', 2),
        pers_tests]),
], search=search)
js = 'window.CONTENT = ' + json.dumps(CONTENT, ensure_ascii=False).replace('</', '<\\/') + ';\n'
assert 'http' not in re.sub(r'xmlns=\\"http://www.w3.org/1998/Math/MathML\\"', '', js), 'externe Verweise'
assert '\\\\(' not in js
open(f'{OUT}/content.js', 'w', encoding='utf-8').write(js)
print('content.js', len(js) // 1024, 'KB', len(search), 'Suchtreffer-Einträge')

# ---------------------------------------------------------------- Shell
shutil.copy('app.css', f'{OUT}/app.css'); shutil.copy('app.js', f'{OUT}/app.js')
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(f'''<!DOCTYPE html>
<html lang="de" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{NAME}</title>
<meta name="theme-color" content="#1b1a18">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="apple-mobile-web-app-title" content="Lernkiste">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="stylesheet" href="app.css">
<script>try{{var s=JSON.parse(localStorage.getItem('lernkiste-v1')||'null'),t=s&&s.settings&&s.settings.theme;if(t==='auto')t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
</head>
<body>
<main id="app"><div id="view"></div></main>
<div id="tabbar" class="tabbar"></div>
<noscript><p style="padding:20px">Diese App braucht JavaScript.</p></noscript>
<script src="content.js"></script>
<script src="app.js"></script>
</body>
</html>
''')

# ---------------------------------------------------------------- Weiterleitungen alter Seiten
ORDER = ['diff1-k1-' + x for x in CARD_IDS]
def stub(fn, route, extra=''):
    open(f'{OUT}/{fn}', 'w', encoding='utf-8').write(f'''<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>{NAME}</title>
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#1b1a18">
<script>
var ids={json.dumps(ORDER)},h=location.hash.replace(/^#/,''),p={{}};h.split('&').forEach(function(x){{var k=x.split('=');if(k[0])p[k[0]]=k[1]||''}});
var r='{route}',q=[];{extra}
location.replace('index.html#'+r+(q.length?'?'+q.join('&'):''));
</script></head><body style="background:#1b1a18;color:#eee;font-family:sans-serif;padding:20px"><a href="index.html" style="color:#8fb6dc">Weiter zu {NAME}</a></body></html>
''')
stub('diff1.html', '/f/diff1/k1', "if(p.k!==undefined&&ids[+p.k]){q.push('c='+ids[+p.k]);if(p.hl)q.push('hl='+p.hl)}")
stub('querschnitt.html', '/f/quer/k10', "if(p.q){q.push('q='+p.q);if(p.hl)q.push('hl='+p.hl)}")
stub('psycho2.html', '/f/psy', "if(p.q){q.push('q='+p.q);if(p.hl)q.push('hl='+p.hl)}")

# ---------------------------------------------------------------- Manifest, Icons, Service Worker
open(f'{OUT}/manifest.webmanifest', 'w', encoding='utf-8').write(json.dumps(dict(
    name=NAME, short_name='Lernkiste', description='Karteikarten und Tests fürs Studium', lang='de', start_url='./', scope='./',
    display='standalone', background_color='#1b1a18', theme_color='#1b1a18',
    icons=[dict(src='icon-192.png', sizes='192x192', type='image/png'), dict(src='icon-512.png', sizes='512x512', type='image/png')]),
    ensure_ascii=False, indent=2) + '\n')

from PIL import Image, ImageDraw, ImageFont
def icon(size, path):
    S = size * 4; im = Image.new('RGB', (S, S), '#1b1a18'); d = ImageDraw.Draw(im)
    m = int(S * .17); r = int(S * .09)
    d.rounded_rectangle([m, int(S * .22), S - m, int(S * .78)], r, fill='#f1ece3')
    d.rounded_rectangle([m, int(S * .22), S - m, int(S * .78)], r, outline='#d9a86c', width=int(S * .018))
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', int(S * .38))
    bb = d.textbbox((0, 0), 'K', font=f); w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((S - w) / 2 - bb[0], S * .5 - h / 2 - bb[1]), 'K', font=f, fill='#1b1a18')
    cx, cy, rr = S - m - int(S * .075), int(S * .22) + int(S * .075), int(S * .035)
    d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill='#d9524a')
    im.resize((size, size), Image.LANCZOS).save(path)
icon(180, f'{OUT}/apple-touch-icon.png'); icon(192, f'{OUT}/icon-192.png'); icon(512, f'{OUT}/icon-512.png')

FILES = ['./', 'index.html', 'app.css', 'app.js', 'content.js', 'diff1.html', 'querschnitt.html', 'psycho2.html',
         'manifest.webmanifest', 'apple-touch-icon.png', 'icon-192.png', 'icon-512.png']
open(f'{OUT}/sw.js', 'w', encoding='utf-8').write(f'''// Offline-Speicher für {NAME}.
// Bei jeder Änderung an Inhalten oder Code die Versionsnummer erhöhen (v8 -> v9 ...).
const CACHE = 'lernkiste-v17';
const FILES = {json.dumps(FILES)};

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES.map(f => new Request(f, {{ cache: 'reload' }})))).then(() => self.skipWaiting()));
}});

self.addEventListener('activate', e => {{
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
}});

// Erst aus dem Speicher antworten (sofort, auch offline), im Hintergrund aktualisieren.
self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.open(CACHE).then(cache =>
      cache.match(e.request, {{ ignoreSearch: true }}).then(cached => {{
        const fresh = fetch(e.request)
          .then(res => {{ if (res && res.ok) cache.put(e.request, res.clone()); return res; }})
          .catch(() => cached);
        return cached || fresh;
      }})
    )
  );
}});
''')
print('fertig', os.listdir(OUT))
