import re, html, subprocess

_cache = {}

def tex2mml(tex, display=False):
    key = (tex, display)
    if key in _cache:
        return _cache[key]
    md = ('$$%s$$' if display else '$%s$') % tex
    out = subprocess.run(['pandoc', '-f', 'markdown', '-t', 'html', '--mathml'],
                         input=md, capture_output=True, text=True, check=True).stdout
    m = re.search(r'<math.*?</math>', out, re.S)
    if not m:
        raise SystemExit('Konvertierung fehlgeschlagen: ' + tex)
    _cache[key] = m.group(0)
    return _cache[key]

def convert(s):
    """\\( \\) und \\[ \\] in HTML-Text durch MathML ersetzen."""
    def repl(m):
        display = m.group(1) == '['
        mml = tex2mml(html.unescape(m.group(2)), display)
        return '<div class="dm">%s</div>' % mml if display else mml
    return re.sub(r'\\([\[(])(.*?)\\[\])]', repl, s, flags=re.S)

MAP = [(r'\\(?:begin|end)\{[^}]*\}', ' '), (r'\\mathbb\s*R', 'ℝ'), (r'\\mathbb\s*N', 'ℕ'), (r'\\mathbb\s*Z', 'ℤ'), (r'\\mathbb\s*Q', 'ℚ'),
       (r'\\varepsilon', 'ε'), (r'\\epsilon', 'ε'), (r'\\delta', 'δ'), (r'\\varphi', 'φ'), (r'\\infty', '∞'), (r'\\leq?\b', '≤'), (r'\\geq?\b', '≥'),
       (r'\\neq', '≠'), (r'\\to\b', '→'), (r'\\iff', '⇔'), (r'\\Rightarrow', '⇒'), (r'\\forall', '∀'), (r'\\exists', '∃'),
       (r'\\in\b', '∈'), (r'\\subseteq', '⊆'), (r'\\cdot', '·'), (r'\\pm', '±'), (r'\\sqrt', '√'), (r'\\partial', '∂'),
       (r'\\nabla', '∇'), (r'\\operatorname\{([^}]*)\}', r'\1 '), (r'\^2', '²'), (r'\^3', '³'), (r'_', ''), (r'\\lim\b', 'lim'), (r'\\max', 'max'), (r'\\min', 'min'),
       (r'\\sup', 'sup'), (r'\\inf', 'inf'), (r'\\pi', 'π'), (r'\\mid', '|'), (r'\\emptyset', '∅'), (r'\\setminus', '∖')]

def tex_to_text(tex):
    t = tex
    for pat, rep in MAP:
        t = re.sub(pat, rep, t)
    t = re.sub(r'\\(?:frac|tfrac|dfrac)\s*\{([^{}]*)\}\s*\{([^{}]*)\}', r'(\1)/(\2)', t)
    t = re.sub(r'\\[a-zA-Z]+', ' ', t)
    t = re.sub(r'[{}\\]', '', t)
    return re.sub(r'\s+', ' ', t).strip()

def plain(s):
    """HTML mit TeX -> Klartext fuer die Suche."""
    s = re.sub(r'\\([\[(])(.*?)\\[\])]', lambda m: tex_to_text(html.unescape(m.group(2))), s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()
