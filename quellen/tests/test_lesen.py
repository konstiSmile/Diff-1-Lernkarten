from playwright.sync_api import sync_playwright
errs=[]
B='http://localhost:8765/index.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    ovf=lambda t: errs.append(f'OVF {t}') if pg.evaluate("document.documentElement.scrollWidth")>390 else None
    pg.goto(B+'#/f/diff1'); pg.reload(); pg.wait_for_selector('.tile')
    print('diff1 chapters', [t.split('\n')[0] for t in pg.locator('.tile').all_inner_texts()])
    pg.goto(B+'#/f/diff1/k1'); pg.reload(); pg.wait_for_selector('#bRead')
    before=pg.evaluate("localStorage.getItem('lernkiste-v1')")
    pg.click('#bRead'); pg.wait_for_selector('#rNext'); print('lesen:', pg.inner_text('.status').replace('\n',' '), '| has Antwort:', 'ANTWORT' in pg.inner_text('#view')); ovf('read1'); pg.screenshot(path='/tmp/read1.png', full_page=True)
    for _ in range(18): pg.click('#rNext')
    print('ende:', pg.inner_text('.status').replace('\n',' '), 'next disabled', pg.is_disabled('#rNext')); ovf('read19')
    pg.click('#rEnd'); pg.wait_for_selector('#card'); print('zurück in Üben:', pg.inner_text('.status').replace('\n',' '))
    print('DB unverändert:', before==pg.evaluate("localStorage.getItem('lernkiste-v1')") or 'prüfen')
    pg.goto(B+'#/f/diff1/tk1'); pg.reload(); pg.wait_for_selector('.mode'); print('tests:', pg.inner_text('h1'), [pg.inner_text(f'.mode >> nth={i}').replace('\n',' ') for i in range(4)])
    pg.click('.mode >> nth=0'); pg.wait_for_selector('.opt'); ovf('mc'); pg.click('.opt >> nth=0'); pg.screenshot(path='/tmp/d1mc.png')
    pg.goto(B+'#/f/diff1/tk1'); pg.reload(); pg.wait_for_selector('#readQ'); pg.click('#readQ'); pg.wait_for_selector('#rNext'); print('fragen lesen:', pg.inner_text('.meta').replace('\n',' ')); ovf('readQ'); pg.screenshot(path='/tmp/d1read_q.png', full_page=True)
    for _ in range(25): pg.click('#rNext')
    print(pg.inner_text('.meta').replace('\n',' ')); ovf('readQ2'); pg.screenshot(path='/tmp/d1read_q2.png', full_page=True)
    for _ in range(21): pg.click('#rNext')
    print(pg.inner_text('.meta').replace('\n',' ')); ovf('readQ3'); pg.screenshot(path='/tmp/d1read_q3.png', full_page=True)
    pg.goto(B+'#/f/diff1/tk1'); pg.reload(); pg.wait_for_selector('.mode'); pg.click('.mode >> nth=3'); pg.wait_for_selector('.chip'); print('exam setup:', pg.inner_text('#view')[:120].replace('\n',' '))
    pg.goto(B+'#/f/psy/k1'); pg.reload(); pg.wait_for_selector('#bRead'); pg.click('#bRead'); pg.wait_for_selector('#rNext'); print('psy lesen ok', pg.inner_text('.status').replace('\n',' '))
    pg.goto(B+'#/mix'); pg.reload(); pg.wait_for_selector('.mixrow'); print('mix:', pg.inner_text('.row').replace('\n',' '))
    b.close()
print('errs',errs)
