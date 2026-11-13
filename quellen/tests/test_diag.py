# Psycho 2 · Diagnostik Teil 1 (v24): Hub, alle Formate, Suche, Tabelle, Überlauf
from playwright.sync_api import sync_playwright
errs=[]; B='http://localhost:8765/index.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    ovf=lambda t: errs.append(f'OVF {t}') if pg.evaluate("document.documentElement.scrollWidth")>390 else None
    pg.goto(B+'#/f/psy'); pg.wait_for_selector('.tile'); print('gruppen:', [t.replace('\n',' | ') for t in pg.locator('.tile').all_inner_texts()]); ovf('fach')
    pg.goto(B+'#/f/psy/u/diag'); pg.reload(); pg.wait_for_selector('.tile'); print('diag:', [t.replace('\n',' | ') for t in pg.locator('.tile').all_inner_texts()]); ovf('gruppe')
    pg.goto(B+'#/f/psy/d1'); pg.reload(); pg.wait_for_selector('.mode'); ovf('hub')
    print('hub', pg.inner_text('h1'), [pg.inner_text(f'.mode >> nth={i}').replace('\n',' ') for i in range(pg.locator('.mode').count())])
    pg.screenshot(path='/tmp/diag_hub.png')
    for i in range(1,5):
        pg.goto(B+'#/f/psy/d1'); pg.reload(); pg.wait_for_selector('.mode'); pg.click(f'.mode >> nth={i}'); pg.wait_for_timeout(400); ovf(f'modus {i}')
        print(' modus',i, pg.inner_text('#view')[:70].replace('\n',' '))
    pg.goto(B+'#/f/psy/d1?c=psy-diag-d1-anna'); pg.reload(); pg.wait_for_selector('#card'); pg.click('#card'); pg.wait_for_timeout(500); ovf('anna'); pg.screenshot(path='/tmp/diag_anna.png')
    pg.goto(B+'#/f/psy/d1'); pg.reload(); pg.wait_for_selector('#readQ'); pg.click('#readQ'); pg.wait_for_selector('#rNext'); ovf('readQ')
    for q in ('Event Sampling','Beobachterdrift','Formenwaage'):
        pg.goto(B+'#/suche?q='+q); pg.reload(); pg.wait_for_selector('.hit'); print('suche',q, len(pg.locator('.hit').all()))
    b.close()
print('errs',errs)
