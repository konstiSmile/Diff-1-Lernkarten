import re, json, sys, importlib, shutil, os
from bs4 import BeautifulSoup
import tex

OUT = '/home/claude/out'
os.makedirs(OUT, exist_ok=True)

HEAD_TAGS = '''
<meta name="theme-color" content="#f6f3ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1b1a18" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Karteikarten">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" type="image/png" href="icon-192.png">'''
SW_REG = "<script>if ('serviceWorker' in navigator) { window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {})); }</script>\n"

# ---------------------------------------------------------------- Diff1 (Karteikarten)
src = open('quelle.html', encoding='utf-8').read()
head, body = src.split('<body', 1)
body = tex.convert(body)
out = head + '<body' + body
out = re.sub(r'<script>\s*window\.MathJax.*?</script>\s*', '', out, flags=re.S)
out = re.sub(r'<script src="https://cdnjs[^>]*></script>\s*', '', out)
out = re.sub(r'<link[^>]*fonts\.g[^>]*>\s*', '', out)
out = out.replace('<body class="loading">', '<body>')
out = re.sub(r"\s*// MathJax typesets.*?8000\);", '', out, flags=re.S)
old = '.face mjx-container[display="true"] { overflow-x: auto; overflow-y: hidden; padding: 2px 0; margin: .5em 0 !important; }'
assert old in out
out = out.replace(old,
    '.face .dm { overflow-x: auto; overflow-y: hidden; padding: 2px 0; margin: .5em 0; }\n'
    '  .face math { font-family: "STIX Two Math", "Cambria Math", "Latin Modern Math", math, serif; font-size: 1.05em; }\n'
    '  .face math[display="block"] { display: block math; }')
out = out.replace('</title>', '</title>' + HEAD_TAGS, 1)
out = out.replace('</body>', SW_REG + '</body>')
assert 'http' not in re.sub(r'xmlns="http://www.w3.org/1998/Math/MathML"', '', out), 'externe Verweise in diff1'
assert '\\(' not in out and '\\[' not in out
open(f'{OUT}/diff1.html', 'w', encoding='utf-8').write(out)
print('diff1.html', out.count('<math'), 'Formeln', len(out) // 1024, 'KB')

# ---------------------------------------------------------------- Suchindex
DIFF_KW = [
    'Körper angeordnet Archimedisch vollständig reelle Zahlen Eigenschaften',
    'Archimedes archimedisch Axiom',
    'Supremum Infimum obere Schranke kleinste Schranke Vollständigkeit',
    'Folge Folgenglied Index Abbildung',
    'Monotonie monoton wachsend fallend streng',
    'beschränkt Schranke obere untere Beschränktheit',
    'monotone Folge beschränkt',
    'Grenzwert Limes Epsilon Umgebung Konvergenz Quantoren Definition',
    'Eindeutigkeit Grenzwert eindeutig',
    'konvergent divergent Nullfolge Konvergenz',
    'konvergent beschränkt Kontraposition',
    'Ungleichung Grenzübergang kleiner gleich',
    'Schrankenlemma Sandwich Einschnürungssatz Einschließungssatz',
    'Nullfolge Schrankenlemma Potenz',
    'Äquivalenz Grenzwert Nullfolge Betrag',
    'Betrag umgekehrte Dreiecksungleichung',
    'Grenzwertsätze Summe Produkt Quotient Rechenregeln',
    'bestimmt divergent uneigentlich konvergent unendlich',
    'Kehrwert Nullfolge unendlich',
]
index = []
soup = BeautifulSoup(src, 'html.parser')
for i, c in enumerate(soup.select('#data .c')):
    q = c.select_one('.q').decode_contents()
    a = c.select_one('.a').decode_contents()
    index.append(dict(s='diff1', title=c['data-src'], label='Karteikarte · Kap. 1' + (' · rot markiert' if c['data-red'] == '1' else ''),
                      url=f'diff1.html#k={i}', kw=DIFF_KW[i], text=tex.plain(q) + ' — ' + tex.plain(a)))

TYPES = {'mc': 'Multiple Choice', 'tf': 'Richtig/Falsch', 'gap': 'Lückentext'}

def test_text(it):
    if it['type'] == 'mc':
        t = it['q'] + ' ' + ' / '.join(it['options'])
    elif it['type'] == 'tf':
        t = it['statement'] + (' Richtig.' if it['answer'] else ' Falsch.')
    else:
        t = re.sub(r'\{\{(.*?)\}\}', lambda m: m.group(1).replace('|', '/'), it['text'])
    return tex.plain(t + ' ' + it.get('expl', ''))

# ---------------------------------------------------------------- Testseiten
tpl = open('test_template.html', encoding='utf-8').read()

def conv_item(it):
    it = dict(it)
    for k in ('q', 'statement', 'text', 'expl'):
        if k in it:
            it[k] = tex.convert(it[k])
    if 'options' in it:
        it['options'] = [tex.convert(o) for o in it['options']]
    it.pop('kw', None); it.pop('placeholder', None)
    return it

def build_tests(modname, filename, qkey):
    m = importlib.import_module(modname)
    D = dict(m.DATA)
    items = [conv_item(i) for i in m.ITEMS]
    D['items'] = items
    js = json.dumps(D, ensure_ascii=False).replace('</', '<\\/')
    page = tpl.replace('__DATA__', js).replace('__TITLE__', D['title'] + ' – Karteikarten').replace('__ACCENT__', D['accent'])
    assert 'http' not in re.sub(r'xmlns=\\"http://www.w3.org/1998/Math/MathML\\"', '', page), 'externe Verweise in ' + filename
    open(f'{OUT}/{filename}', 'w', encoding='utf-8').write(page)
    print(filename, len(items), 'Fragen', len(page) // 1024, 'KB')
    if not D['placeholder']:
        for it in m.ITEMS:
            index.append(dict(s=qkey, title=it['src'], label=TYPES[it['type']], url=f"{filename}#q={it['id']}",
                              kw=it.get('kw', ''), text=test_text(it)))
    return len(items)

nq = build_tests('data_querschnitt', 'querschnitt.html', 'quer')
build_tests('data_psycho2', 'psycho2.html', 'psy')

# ---------------------------------------------------------------- Startseite
idx = open('index_template.html', encoding='utf-8').read()
js = json.dumps(index, ensure_ascii=False).replace('</', '<\\/')
idx = idx.replace('__INDEX__', js).replace('__QN__', str(nq))
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(idx)
print('index.html', len(index), 'Suchtreffer-Einträge', len(idx) // 1024, 'KB')

# ---------------------------------------------------------------- sw + manifest
open(f'{OUT}/sw.js', 'w', encoding='utf-8').write('''// Offline-Speicher für die Karteikarten.
// Bei jeder Änderung an Karten oder Tests die Versionsnummer erhöhen (v3 -> v4 ...).
const CACHE = 'karteikarten-v3';
const FILES = ['./', 'index.html', 'diff1.html', 'querschnitt.html', 'psycho2.html', 'manifest.webmanifest', 'apple-touch-icon.png', 'icon-192.png', 'icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Erst aus dem Speicher antworten (sofort, auch offline), im Hintergrund aktualisieren.
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.open(CACHE).then(cache =>
      cache.match(e.request, { ignoreSearch: true }).then(cached => {
        const fresh = fetch(e.request)
          .then(res => { if (res && res.ok) cache.put(e.request, res.clone()); return res; })
          .catch(() => cached);
        return cached || fresh;
      })
    )
  );
});
''')
shutil.copy('/home/claude/out/manifest.webmanifest', '/tmp/manifest.bak') if os.path.exists('/home/claude/out/manifest.webmanifest') else None
