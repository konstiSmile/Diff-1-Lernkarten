# Motivation (v36): Heute fällig, Tagesziel-Ring, Lerntage-Kette, Klausur-Countdown, Einstellungen „Motivation“
# Aufruf: python3 test_motivation.py [URL] [Screenshot]
import sys, datetime
from playwright.sync_api import sync_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8765/'
SHOT = sys.argv[2] if len(sys.argv) > 2 else None
# Verlauf vorbelegen (Tage relativ zu heute, Mittag):
#  Karte diff1-k1-reelle-zahlen: vor 3 Tagen gewusst → Serie 1, Abstand 1 Tag → fällig
#  Frage pp-tf-01: vor 3 Tagen richtig, gestern falsch → fällig
#  Frage pp-mc-01: vor 1 Tag 4 Punkte, davor an 2 Tagen 4 Punkte → gemeistert, Abstand 7 → nicht fällig
#  Lerntage: -1, -3, -4, -5 (Lücke bei -2 = Pausetag) → Kette 4
SEED = """
(function(){if(sessionStorage.seeded)return;sessionStorage.seeded=1;
var D=function(k){var d=new Date();d.setHours(12,0,0,0);d.setDate(d.getDate()-k);return d.getTime();};
var log=[[D(5),'psy','pp-mc-01',1,4],[D(4),'psy','pp-mc-01',1,4],[D(3),'diff1','diff1-k1-reelle-zahlen',1],[D(1),'psy','pp-mc-01',1,4]];
log.splice(3,0,[D(3)+1000,'psy','pp-tf-01',1]);
log.push([D(1)+1,'psy','pp-tf-01',0]);
log.sort(function(a,b){return a[0]-b[0]});
localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1},log:log}));})();
"""

def ok(cond, msg):
    print(('OK   ' if cond else 'FAIL ') + msg)
    if not cond: ok.fail = True
ok.fail = False

today = datetime.date.today()
def days(s): return (datetime.date.fromisoformat(s) - today).days

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block')
    ctx.add_init_script(SEED)
    pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    def openMot():
        if not pg.locator('.group.open .ghead:has-text("Motivation")').count(): pg.click('.ghead:has-text("Motivation")')
    def go(h):
        pg.goto(URL + '#/leer'); pg.wait_for_timeout(100); pg.goto(URL + h); pg.wait_for_timeout(250)

    go('#/')
    ok(pg.inner_text('#tdGoal b') == 'Heute 0 von 30', 'Tagesziel: ' + pg.inner_text('#tdGoal b'))
    ok('Lerntage in Folge: 4' in pg.inner_text('#tdGoal'), 'Kette mit Pausetag: ' + pg.inner_text('#tdGoal small'))
    due = pg.inner_text('.hello')
    ok('1 Karte und 1 Frage warten' in due, 'Heute fällig: ' + due.replace('\n', ' | '))
    cd = ' · '.join(x.replace('\n', ' ') for x in pg.locator('.exrow').all_inner_texts())
    exp = 'Psycho 2 in %d Tagen' % days('2027-01-29')
    ok(cd.startswith('29 Jan Psycho 2') and ('in %d Tagen' % days('2027-01-29')) in cd and ('in %d Tagen' % days('2027-02-19')) in cd, 'Countdown: ' + cd.replace('\n', ' · '))
    ok(pg.evaluate('document.documentElement.scrollWidth') <= 390, 'Startseite ohne Überlauf')
    if SHOT: pg.screenshot(path=SHOT)

    # Fällige Fragen üben
    go('#/faellig/tests'); pg.wait_for_selector('.mode')
    ok('Heute fällig: Fragen' in pg.inner_text('h1'), 'Fällig-Hub')
    pg.click('.mode[data-m=tf]'); pg.wait_for_selector('#tfrow button'); pg.click('#tfrow button >> nth=0'); pg.click('#next'); pg.wait_for_selector('.score')
    go('#/')
    ok('Heute 1 von 30' in pg.inner_text('#tdGoal b') and 'Frage' not in pg.inner_text('.hello span'), 'Nach Üben: Ziel 1, Frage nicht mehr fällig')
    ok('Lerntage in Folge: 5' in pg.inner_text('#tdGoal'), 'Kette zählt heute mit')

    # Fällige Karten: Filter „Alle“, auch bei rot markierten Karten
    pg.click('#goLearn'); pg.wait_for_selector('#card')
    ok(pg.inner_text('.cnt') == '1/1', 'Fällige Karte sichtbar')
    pg.click('#card'); pg.click('#bKnown')
    go('#/')
    ok('nichts fällig' in pg.inner_text('.hello span'), 'Nichts mehr fällig')

    # Verlauf zeigt Kette
    go('#/verlauf'); ok('Lerntage-Kette' in pg.inner_text('.stats'), 'Verlauf: Lerntage-Kette')

    # Einstellungen
    go('#/einstellungen'); openMot()
    ok(pg.evaluate('document.documentElement.scrollWidth') <= 390, 'Einstellungen ohne Überlauf')
    pg.click('.seg[data-k=mGoal] button[data-v="0"]'); pg.click('.seg[data-k=mDue] button[data-v="0"]')
    go('#/')
    ok(pg.locator('.ring').count() == 0 and 'wartet' not in pg.inner_text('.hello span') and 'warten' not in pg.inner_text('.hello span') and 'Antworten' in pg.inner_text('#tdGoal b'), 'Ziel und Fällig abschaltbar')
    go('#/einstellungen'); openMot()
    pg.click('.seg[data-k=mChain] button[data-v="0"]'); pg.click('.seg[data-k=mCount] button[data-v="0"]')
    go('#/'); ok(pg.locator('.today').count() == 0, 'Alles aus → kein Kasten')
    go('#/einstellungen'); openMot(); pg.click('.seg[data-k=mCount] button[data-v="1"]')
    # versteckte Fächer fallen aus dem Countdown
    pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.hidden=['psy'];localStorage.setItem('lernkiste-v1',JSON.stringify(d))")
    pg.reload(); go('#/')
    ok('Psycho' not in pg.inner_text('.exams'), 'Verstecktes Fach nicht in den Klausurzeilen')
    ok(not errs, 'keine JS-Fehler ' + str(errs))
    b.close()
print('FERTIG', 'mit Fehlern' if ok.fail else 'alles ok')
sys.exit(1 if ok.fail else 0)
