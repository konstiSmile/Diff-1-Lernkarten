# Eigene Karten: Backup-Tipp, Hinweis, Erinnerung nach 7 Tagen, Warnung bei Speicherfehler (v34)
from playwright.sync_api import sync_playwright
import subprocess, time, json
B = 'http://localhost:8765/'
srv = subprocess.Popen(['python3', '-m', 'http.server', '8765'], cwd='/home/claude/out2', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
def db(pg): return pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1'))")
def toast(pg): return pg.locator('.toast').inner_text() if pg.locator('.toast').count() else ''
try:
  with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    ctx = b.new_context(viewport={'width': 390, 'height': 780}, service_workers='block', accept_downloads=True)
    ctx.add_init_script("if(!localStorage.getItem('lernkiste-v1'))localStorage.setItem('lernkiste-v1',JSON.stringify({settings:{statsAsked:1}}))")
    pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(B + '#/neu'); pg.wait_for_selector('#fname')
    print('ohne karten kein hinweis:', pg.locator('.bkhint').count() == 0)
    pg.fill('#fname', 'Test'); pg.click('#fadd'); pg.wait_for_selector('#qIn')
    pg.fill('#qIn', 'F1'); pg.fill('#aIn', 'A1'); pg.click('#esave'); pg.wait_for_timeout(600)
    print('tipp nach erster karte:', 'nur auf diesem Gerät' in toast(pg))
    print('hinweis warn:', pg.locator('.bkhint.warn').count() == 1, '| ovf', pg.evaluate('document.documentElement.scrollWidth'))
    pg.locator('.bkhint').screenshot(path='/home/claude/bk.png')
    pg.evaluate("document.querySelectorAll('.toast').forEach(x=>x.remove())")
    pg.fill('#qIn', 'F2'); pg.fill('#aIn', 'A2'); pg.click('#esave'); pg.wait_for_timeout(500)
    print('tipp nur einmal:', 'nur auf diesem Gerät' not in toast(pg))
    with pg.expect_download() as dl: pg.click('#bkNow')
    data = json.loads(open(dl.value.path()).read())
    print('backup enthält karten:', len(data['data']['custom']['folders'][0]['cards']) == 2, '| im backup sauber:', data['data']['settings']['ownDirty'] == 0)
    d = db(pg); print('gesichert markiert:', d['settings']['ownDirty'] == 0 and d['settings']['lastBackup'] > 0)
    pg.goto(B + '#/neu'); pg.wait_for_selector('.bkhint'); print('alles gesichert:', pg.locator('.bkhint.warn').count() == 0, pg.locator('.bkhint b').inner_text())
    # Erinnerung nach 8 Tagen
    pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.settings.ownDirty=Date.now()-8*864e5;d.settings.nagDay='';localStorage.setItem('lernkiste-v1',JSON.stringify(d))")
    pg.goto(B); pg.reload(); pg.wait_for_timeout(3000); print('erinnerung:', toast(pg)[:60])
    pg.reload(); pg.wait_for_timeout(3000); print('nicht zweimal am tag:', 'nicht gesichert' not in toast(pg))
    # Bestandsnutzer: Karten, nie gesichert
    pg.evaluate("var d=JSON.parse(localStorage.getItem('lernkiste-v1'));d.settings.ownDirty=0;d.settings.lastBackup=0;d.settings.nagDay='';localStorage.setItem('lernkiste-v1',JSON.stringify(d))")
    pg.reload(); pg.wait_for_timeout(3000); d = db(pg)
    print('bestand: merker gesetzt, keine erinnerung:', d['settings']['ownDirty'] > 0, 'nicht gesichert' not in toast(pg))
    pg.goto(B + '#/neu'); pg.wait_for_selector('.bkhint'); print('bestand: warn', pg.locator('.bkhint.warn').count() == 1)
    # Speicherfehler
    pg.evaluate("(()=>{Storage.prototype.setItem=function(){throw new Error('QuotaExceededError')};return 1})()")
    pg.click('.tile.s-own'); pg.wait_for_selector('#qIn'); pg.fill('#qIn', 'F3'); pg.fill('#aIn', 'A3'); pg.click('#esave'); pg.wait_for_timeout(300)
    print('warnung speicherfehler:', 'Speichern hat nicht geklappt' in toast(pg))
    pg.locator('.toast').screenshot(path='/home/claude/bk2.png')
    pg.evaluate("document.querySelectorAll('.toast').forEach(x=>x.remove())")
    pg.fill('#qIn', 'F4'); pg.fill('#aIn', 'A4'); pg.click('#esave'); pg.wait_for_timeout(300)
    print('nicht wiederholt:', 'Speichern hat nicht geklappt' not in toast(pg))
    print('errs', errs); b.close()
finally:
  srv.terminate()
