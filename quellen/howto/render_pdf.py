from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page()
    pg.goto('file:///home/claude/build/howto1.html'); pg.wait_for_timeout(500)
    # Überlauf je Seite prüfen
    print(pg.evaluate("""() => [...document.querySelectorAll('.page')].map(p => { const f=p.querySelector('.foot').getBoundingClientRect().top; const last=[...p.children].filter(c=>!c.classList.contains('foot')).pop().getBoundingClientRect().bottom; return {gap: Math.round(f-last)}; })"""))
    pg.pdf(path='/home/claude/out/Karteikarten_HowTo_1Seite.pdf', prefer_css_page_size=True, print_background=True)
    b.close()
