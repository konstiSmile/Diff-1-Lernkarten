from playwright.sync_api import sync_playwright
errs=[]
B='http://localhost:8765/index.html'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':390,'height':780},service_workers='block')
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    def ovf(t):
        w=pg.evaluate("document.documentElement.scrollWidth")
        if w>390: errs.append(f'OVF {t} {w}')
        # Elemente in Karten/Fragen, die breiter als ihr Container sind (ohne scrollbare .dm)
        bad=pg.evaluate("""()=>{const out=[];document.querySelectorAll('#view math').forEach(m=>{if(m.closest('.dm'))return;const r=m.getBoundingClientRect();if(r.right>392)out.push(m.textContent.slice(0,40))});return out}""")
        if bad: errs.append(f'MATH {t} {bad}')
    pg.goto(B+'#/f/quer'); pg.reload(); pg.wait_for_selector('.tile')
    print('quer:', [t.replace('\n',' | ') for t in pg.locator('.tile').all_inner_texts()]); pg.screenshot(path='/tmp/q_fach.png')
    pg.goto(B+'#/f/quer/u/dgl'); pg.reload(); pg.wait_for_selector('.tile'); print('dgl:', [t.replace('\n',' | ') for t in pg.locator('.tile').all_inner_texts()])
    pg.goto(B+'#/f/quer/u/mv'); pg.reload(); pg.wait_for_selector('.tile'); print('mv:', [t.replace('\n',' | ') for t in pg.locator('.tile').all_inner_texts()])
    pg.goto(B+'#/f/quer/k10'); pg.reload(); pg.wait_for_selector('.mode'); print('k10 back:', pg.get_attribute('.nav a','href'))
    pg.goto(B+'#/f/quer/k11'); pg.reload(); pg.wait_for_selector('.mode'); print('hub:', pg.inner_text('h1'), pg.get_attribute('.nav a','href'), [pg.inner_text(f'.mode >> nth={i}').replace('\n',' ') for i in range(5)])
    pg.click('.mode >> nth=0'); pg.wait_for_selector('#bRead'); pg.click('#bRead'); pg.wait_for_selector('#rNext')
    for i in range(26):
        ovf(f'card{i+1}')
        if i in (0,10,21): pg.screenshot(path=f'/tmp/q_card{i+1}.png', full_page=True)
        if i<25: pg.click('#rNext')
    print('ende:', pg.inner_text('.status').replace('\n',' '))
    pg.goto(B+'#/f/quer/k11'); pg.reload(); pg.wait_for_selector('#readQ'); pg.click('#readQ'); pg.wait_for_selector('#rNext')
    n=0
    while True:
        ovf('q'+str(n)); n+=1
        if pg.is_disabled('#rNext'): break
        pg.click('#rNext')
    print('fragen gelesen', n)
    pg.goto(B+'#/f/quer/k11'); pg.reload(); pg.wait_for_selector('.mode'); pg.click('.mode >> nth=1'); pg.wait_for_selector('.opt'); ovf('mc'); pg.click('.opt >> nth=0'); pg.wait_for_selector('#next'); pg.screenshot(path='/tmp/q_mc.png')
    pg.goto(B+'#/suche?q=Peano'); pg.reload(); pg.wait_for_timeout(500); print('suche Peano:', pg.inner_text('#view')[:200].replace('\n',' | '))
    pg.goto(B+'#/mix'); pg.reload(); pg.wait_for_selector('.mixrow'); print('mix:', pg.inner_text('#view')[:200].replace('\n',' '))
    b.close()
print('errs',errs)
