# Echtes MC für Psycho 2 (0/2/4 Punkte), getrennte Auswertung, Verlauf mit Punkten, „Frage melden“ (v35)
# Aufruf: python3 test_mc_echt.py [URL]  (Ausgabeordner per http.server auf 8765)
import sys, json
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/'
SHOT = sys.argv[2] if len(sys.argv) > 2 else None
# Testdaten: in Psycho Kap. 1 nur eine MC-Frage (zwei richtige Optionen), eine R/F- und eine Lückenfrage
PATCH = """
(function(){var c;Object.defineProperty(window,'CONTENT',{configurable:true,get:function(){return c},set:function(v){
  var p=v.subjects.filter(function(s){return s.id==='psy'})[0], k=p.chapters.filter(function(x){return x.id==='k1'})[0];
  var mc=k.items.filter(function(i){return i.id==='pp-mc-01'})[0]; mc.correct=[0,1];
  var tf=k.items.filter(function(i){return i.type==='tf'})[0], gp=k.items.filter(function(i){return i.type==='gap'})[0];
  k.items=[mc,tf,gp]; c=v;}});})();
if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1,testN:0}}));
"""
posts = []

def ok(cond, msg):
    print(('OK   ' if cond else 'FAIL ') + msg)
    if not cond: ok.fail = True
ok.fail = False

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block')
    ctx.add_init_script(PATCH)
    def grab(route):
        posts.append(route.request.post_data); route.fulfill(status=200, body='ok')
    ctx.route('https://script.google.com/**', grab)
    pg = ctx.new_page()
    def hub(f):
        pg.goto(URL + '#/'); pg.wait_for_timeout(150); pg.goto(URL + '#/f/' + f + '/k1'); pg.wait_for_selector('.mode')
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))

    # --- Übungsrunde: nur Option 0 → 1 richtig angekreuzt, 1 vergessen, 2 richtig weggelassen → 2 Punkte
    hub('psy')
    ok('1 bis 4 richtig' in pg.inner_text('.modes'), 'Hub-Text für Psycho-MC')
    pg.click('.mode[data-m=mc]'); pg.wait_for_selector('.mopt')
    ok(pg.is_visible('.mhint'), 'Hinweis „1 bis 4 Antworten“ sichtbar')
    ok(pg.is_disabled('#mcheck'), 'Prüfen gesperrt ohne Kreuz')
    pg.click('.mopt[data-o="0"]'); pg.click('.mopt[data-o="2"]'); pg.click('.mopt[data-o="2"]')
    ok(pg.get_attribute('.mopt[data-o="0"]', 'aria-pressed') == 'true' and pg.get_attribute('.mopt[data-o="2"]', 'aria-pressed') == 'false', 'An- und Abwählen')
    pg.click('#mcheck')
    ok('2 / 4 Punkte' in pg.inner_text('.fb'), '2 Punkte bei einer vergessenen')
    ok(pg.locator('.mopt.ok').count() == 1 and pg.locator('.mopt.miss').count() == 1 and pg.locator('.mopt.okn').count() == 2, 'Markierung je Option')
    ok(pg.evaluate('document.documentElement.scrollWidth') <= 390, 'kein Überlauf (Markierung)')
    if SHOT: pg.screenshot(path=SHOT, full_page=True)

    # Frage melden
    pg.click('#rep'); pg.wait_for_selector('#repGo')
    ok(pg.is_disabled('#repGo'), 'Senden gesperrt ohne Grund')
    pg.click('#repWhy .chip[data-w="Unklar formuliert"]'); pg.fill('#repText', 'Testkommentar')
    pg.click('#repGo'); pg.wait_for_timeout(600)
    body = json.loads(posts[-1]) if posts else {}
    ok(body.get('typ') == 'feedback' and body.get('seite') == 'Frage psy · pp-mc-01', 'Meldung: Seite = Fach + ID')
    ok(body.get('text') == 'Frage gemeldet · Unklar formuliert: Testkommentar', 'Meldung: Text')
    ok(pg.inner_text('#rep') == 'Gemeldet ✓' and pg.is_disabled('#rep'), 'Knopf zeigt „Gemeldet“')

    pg.click('#next'); pg.wait_for_selector('.score')
    note = pg.inner_text('.score .note')
    ok('MC 2/4 Punkte' in note, 'Ergebnis in Punkten: ' + note)
    # R/F und Lücke: Melden-Knopf
    hub('psy'); pg.click('.mode[data-m=tf]')
    pg.wait_for_selector('.tfrow .opt'); pg.click('.tfrow .opt >> nth=0')
    ok(pg.is_visible('#rep'), 'Melden auch bei R/F')
    hub('psy'); pg.click('.mode[data-m=gap]')
    pg.wait_for_selector('#reveal'); pg.click('#reveal')
    ok(pg.is_visible('#rep'), 'Melden auch bei Lücke')
    log = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).log")
    mc = [e for e in log if e[2] == 'pp-mc-01']
    ok(mc and len(mc[-1]) == 5 and mc[-1][4] == 2 and mc[-1][3] == 0.5, 'Verlauf: Punkte als 5. Feld')
    ok(all(len(e) == 4 for e in log if e[2] != 'pp-mc-01'), 'Verlauf: R/F und Lücke ohne Punkte')
    wrong = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).tests['psy/k1'].wrong")
    ok('pp-mc-01' in wrong, '2 Punkte zählen nicht als gekonnt')

    # --- volle Punkte
    hub('psy'); pg.click('.mode[data-m=mc]'); pg.wait_for_selector('.mopt')
    pg.click('.mopt[data-o="0"]'); pg.click('.mopt[data-o="1"]'); pg.click('#mcheck')
    ok('4 / 4 Punkte' in pg.inner_text('.fb') and 'ok' in pg.get_attribute('.fb', 'class'), '4 Punkte bei allen richtigen')
    pg.click('#next'); pg.wait_for_selector('.score')
    wrong = pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).tests['psy/k1'].wrong")
    ok('pp-mc-01' not in wrong, '4 Punkte = gekonnt')

    # --- falsch angekreuzt: Option 2 + 3 → 0 Punkte
    hub('psy'); pg.click('.mode[data-m=mc]'); pg.wait_for_selector('.mopt')
    pg.click('.mopt[data-o="2"]'); pg.click('.mopt[data-o="3"]'); pg.click('#mcheck')
    ok('0 / 4 Punkte' in pg.inner_text('.fb'), '0 Punkte (nie negativ)')

    # --- Zeit-Simulation
    hub('psy'); pg.click('.mode[data-m=exam]'); pg.click('#go')
    pg.wait_for_selector('.dots')
    ok(pg.is_visible('.mhint'), 'Zeitmodus: Hinweis bei MC')
    pg.click('.mopt[data-o="0"]'); pg.click('.mopt[data-o="1"]')
    ok(pg.locator('.mopt.sel').count() == 2 and 'done' in pg.get_attribute('.dots button >> nth=0', 'class'), 'Zeitmodus: Mehrfachauswahl gemerkt')
    pg.click('#nxt'); pg.click('#prev')
    ok(pg.locator('.mopt.sel').count() == 2, 'Zeitmodus: Auswahl bleibt beim Blättern')
    pg.click('#submit'); pg.click('#submit'); pg.wait_for_selector('.score')
    note = pg.inner_text('.score .note')
    ok('MC 4/4 Punkte' in note and 'R/F 0/1' in note and 'Lücke 0/1' in note and 'Note' in note, 'Zeitmodus getrennt: ' + note)
    ok(pg.locator('details.it [data-rep]').count() == 3, 'Zeitmodus: Melden in jeder Lösung')
    pg.click('details.it >> nth=0'); ok(pg.locator('details.it >> nth=0').locator('.mopt.ok').count() == 2, 'Zeitmodus: markierte Optionen in der Lösung')

    # --- Verlauf
    pg.goto(URL + '#/verlauf'); pg.wait_for_selector('.chart .day'); pg.click('.chart .day >> nth=-1')
    t = pg.inner_text('.daydet')
    ok('Punkte' in t and 'MC' in t, 'Verlauf-Details mit Punkten: ' + t.replace('\n', ' | '))

    # --- Mathe bleibt Single Choice
    hub('diff1')
    ok('eine stimmt' in pg.inner_text('.modes'), 'Diff 1: alter Hub-Text')
    pg.click('.mode[data-m=mc]'); pg.wait_for_selector('.opt')
    ok(pg.locator('.mopt').count() == 0 and pg.locator('.mhint').count() == 0, 'Diff 1: keine Kästchen')
    pg.click('.opt >> nth=0'); pg.wait_for_selector('.fb')
    ok(('Richtig' in pg.inner_text('.fb') or 'Nicht ganz' in pg.inner_text('.fb')) and pg.is_visible('#rep'), 'Diff 1: Sofortwertung + Melden')

    ok(not errs, 'keine JS-Fehler ' + str(errs))
    b.close()
print('FERTIG', 'mit Fehlern' if ok.fail else 'alles ok')
sys.exit(1 if ok.fail else 0)
