# Psycho 2: Kapitel 1 und 2 mit Karten und allen Testformaten (v22)
from playwright.sync_api import sync_playwright
errs=[]; B='http://localhost:8765/index.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    ovf=lambda t: errs.append(f'OVF {t}') if pg.evaluate("document.documentElement.scrollWidth")>390 else None
    # alter Stand mit Test-Kapitel tp
    pg.goto(B); pg.evaluate("localStorage.setItem('lernkiste-v1', JSON.stringify({v:1,tests:{'psy/tp':{best:{exam:70},wrong:['pp-mc-01','pp-tf-08','pp-gap-06']}}}))")
    pg.goto(B+'#/f/psy/u/pers'); pg.reload(); pg.wait_for_selector('.tile')
    print('kapitel:', [t.replace('\n',' | ') for t in pg.locator('.tile').all_inner_texts()]); ovf('gruppe')
    t=pg.evaluate("JSON.parse(localStorage.getItem('lernkiste-v1')).tests"); print('migriert:', {k:v.get('wrong') for k,v in t.items()})
    pg.goto(B+'#/f/psy/tp'); pg.wait_for_timeout(300); print('tp ->', pg.url.split('#')[1])
    for k in ('k1','k2'):
        pg.goto(B+'#/f/psy/'+k); pg.reload(); pg.wait_for_selector('.mode'); ovf('hub '+k)
        print(k, pg.inner_text('h1'), [pg.inner_text(f'.mode >> nth={i}').replace('\n',' ') for i in range(pg.locator('.mode').count())])
        if k=='k1': pg.screenshot(path='/tmp/psy_hub.png')
        pg.click('.mode >> nth=1'); pg.wait_for_selector('.opt'); ovf('mc '+k); pg.click('.opt >> nth=0')
        pg.goto(B+'#/f/psy/'+k); pg.reload(); pg.wait_for_selector('#readQ'); pg.click('#readQ'); pg.wait_for_selector('#rNext'); print(' fragen lesen:', pg.inner_text('.meta').replace('\n',' ')[:60]); ovf('readQ '+k)
        pg.goto(B+'#/f/psy/'+k+'?mode=cards'); pg.reload(); pg.wait_for_selector('#card'); print(' karten:', pg.inner_text('.status').replace('\n',' ')[:60])
    pg.goto(B+'#/suche?q=Komparationsforschung'); pg.reload(); pg.wait_for_selector('.hit'); print('suche:', [h.split('\n')[0] for h in pg.locator('.hit').all_inner_texts()][:5])
    pg.goto(B+'#/mix'); pg.reload(); pg.wait_for_selector('.mixrow'); print('mix:', pg.inner_text('.row').replace('\n',' ')[:150])
    b.close()
print('errs',errs)
