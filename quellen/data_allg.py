# Allgemein (Mathe) – gemeinsamer Pool für Querschnitt und Diff 1
# Jede Karte/Frage hat subj: Liste aus 'quer' und/oder 'diff1'. Gleiche ID in beiden Fächern → Lernstand zählt einmal.
# Quellen: Skript Kap. 4–6, 9, 10 sowie Übungsblätter/Lösungen Querschnitt (Blatt 1–5, Lösungen 1–4).
# Formeln als TeX in \( \) bzw. \[ \]; Lücken als {{Antwort|Alternative}}, nie Zahlen/Formeln als Lückenantwort.
# IDs/Keys nie ändern, nur anhängen. Jede Frage muss ohne Skript verständlich sein.

Q = ['quer']
D = ['diff1']
QD = ['quer', 'diff1']

def H(t):
    return '<p><i>Hinweis (nicht im Skript): ' + t + '</i></p>'

def C(key, subj, src, q, a, kw=''):
    return dict(key=key, subj=subj, src=src, q=q, a=a, kw=kw)

# ------------------------------------------------ Zeichnungen (inline SVG, Farben über app.css .fig)
from math import pi, sin, cos, tan, radians
_PI = {0: '0', 1: 'π/6', 2: 'π/4', 3: 'π/3', 4: 'π/2'}
def _lab(k, n):  # Winkel k·π/n als Text
    from fractions import Fraction
    f = Fraction(k, n)
    if f == 0: return '0'
    a, b = f.numerator, f.denominator
    z = ('−' if a < 0 else '') + ('' if abs(a) == 1 else str(abs(a))) + 'π'
    return z if b == 1 else z + '/' + str(b)
STD = sorted({(k, 6) for k in range(12)} | {(k, 4) for k in range(8)}, key=lambda t: t[0] / t[1])
STD = [t for i, t in enumerate(STD) if all(abs(t[0] / t[1] - u[0] / u[1]) > 1e-9 for u in STD[:i])]

def graph(funcs, x0=-pi/2, x1=2*pi, mark=None, ymax=1.35, W=330, H=None, legend=True, label='Graph'):
    """funcs: Liste (name, klasse); name in sin/cos/tan. mark: (x, y) Punkt."""
    L, R, T = 16, 10, 8
    B = 40 if legend else 24
    H = H or (150 + B)
    sx = (W - L - R) / (x1 - x0); sy = (H - T - B) / (2 * ymax)
    X = lambda x: L + (x - x0) * sx; Y = lambda y: T + (ymax - y) * sy
    o = []
    for v in (1, -1):
        o.append(f'<line class="gd" x1="{X(x0):.1f}" y1="{Y(v):.1f}" x2="{X(x1):.1f}" y2="{Y(v):.1f}"/>')
    o.append(f'<line class="ax" x1="{X(x0):.1f}" y1="{Y(0):.1f}" x2="{X(x1)+4:.1f}" y2="{Y(0):.1f}"/>')
    if x0 <= 0 <= x1:
        o.append(f'<line class="ax" x1="{X(0):.1f}" y1="{Y(ymax):.1f}" x2="{X(0):.1f}" y2="{Y(-ymax):.1f}"/>')
        for v, t in ((1, '1'), (-1, '−1')):
            o.append(f'<text x="{X(0)-4:.1f}" y="{Y(v)-3:.1f}" text-anchor="end">{t}</text>')
    k = round(x0 / (pi / 2))
    while k * pi / 2 <= x1 + 1e-9:
        x = k * pi / 2
        if abs(x) > 1e-9:
            o.append(f'<line class="ax" x1="{X(x):.1f}" y1="{Y(0)-3:.1f}" x2="{X(x):.1f}" y2="{Y(0)+3:.1f}"/>')
            o.append(f'<text x="{X(x):.1f}" y="{Y(-ymax)+15:.1f}" text-anchor="middle">{_lab(k, 2)}</text>')
        k += 1
    F = {'sin': sin, 'cos': cos, 'tan': tan}
    for name, cls in funcs:
        f = F[name]; segs, cur = [], []
        n = 400
        for i in range(n + 1):
            x = x0 + (x1 - x0) * i / n
            if name == 'tan' and abs(cos(x)) < 1e-3: 
                if cur: segs.append(cur); cur = []
                continue
            y = f(x)
            if abs(y) > ymax:
                if cur: cur.append((x, max(-ymax, min(ymax, y)))); segs.append(cur); cur = []
                continue
            cur.append((x, y))
        if cur: segs.append(cur)
        for sg in segs:
            if len(sg) > 1:
                o.append(f'<polyline class="{cls}" points="' + ' '.join(f'{X(a):.1f},{Y(b):.1f}' for a, b in sg) + '"/>')
        if name == 'tan':
            for kk in range(-3, 6):
                xp = pi / 2 + kk * pi
                if x0 < xp < x1: o.append(f'<line class="gd" x1="{X(xp):.1f}" y1="{Y(ymax):.1f}" x2="{X(xp):.1f}" y2="{Y(-ymax):.1f}"/>')
    if legend:
        for i, (name, cls) in enumerate(funcs):
            lx = W / 2 - 40 * (len(funcs) - 1) + 80 * i
            o.append(f'<line class="{cls}" x1="{lx-26:.1f}" y1="{H-9}" x2="{lx-8:.1f}" y2="{H-9}"/><text class="t-{name}" x="{lx-4:.1f}" y="{H-5}">{name}</text>')
    if mark:
        mx, my = mark
        o.append(f'<line class="gd" x1="{X(mx):.1f}" y1="{Y(0):.1f}" x2="{X(mx):.1f}" y2="{Y(my):.1f}"/>')
        o.append(f'<circle class="pm" cx="{X(mx):.1f}" cy="{Y(my):.1f}" r="5"/>')
    return f'<div class="fig"><svg viewBox="0 0 {W} {H}" role="img" aria-label="{label}">' + ''.join(o) + '</svg></div>'

def kreis(mark=None, alle=False, labels=False, extra=(), W=300, label='Einheitskreis'):
    """mark: (k, n) für Winkel k·π/n; alle: Punkte aller Standardwinkel; labels: Winkel beschriften."""
    c, Rr = W / 2, 105
    P = lambda a, r=Rr: (c + r * cos(a), c - r * sin(a))
    o = [f'<line class="ax" x1="{c-Rr-18}" y1="{c}" x2="{c+Rr+18}" y2="{c}"/>', f'<line class="ax" x1="{c}" y1="{c+Rr+18}" x2="{c}" y2="{c-Rr-18}"/>',
         f'<circle class="ax" cx="{c}" cy="{c}" r="{Rr}"/>',
         f'<text x="{c+Rr-4}" y="{c+15}" text-anchor="end">1</text>', f'<text x="{c-Rr+4}" y="{c+15}">−1</text>',
         f'<text x="{c+5}" y="{c-Rr+15}">1</text>', f'<text x="{c+5}" y="{c+Rr-6}">−1</text>']
    if alle:
        for k, n in STD:
            x, y = P(k * pi / n); o.append(f'<circle class="pt" cx="{x:.1f}" cy="{y:.1f}" r="3"/>')
            if labels:
                lx, ly = P(k * pi / n, Rr + 20)
                o.append(f'<text x="{lx:.1f}" y="{ly+4:.1f}" text-anchor="middle" style="font-size:11px">{_lab(k, n)}</text>')
    for (k, n) in list(extra) + ([mark] if mark else []):
        a = k * pi / n; x, y = P(a); isM = (k, n) == mark
        if isM:
            o.append(f'<line class="gd" x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{c}"/>')
            o.append(f'<line class="gd" x1="{x:.1f}" y1="{y:.1f}" x2="{c}" y2="{y:.1f}"/>')
            o.append(f'<line class="ray" x1="{c}" y1="{c}" x2="{x:.1f}" y2="{y:.1f}"/>')
            r0 = 24; large = 1 if a > pi else 0; ex, ey = P(a, r0)
            o.append(f'<path class="ray" d="M{c+r0},{c} A{r0},{r0} 0 {large} 0 {ex:.1f},{ey:.1f}"/>')
        o.append(f'<circle class="{"pm" if isM else "pt"}" cx="{x:.1f}" cy="{y:.1f}" r="{6 if isM else 4}"/>')
    return f'<div class="fig"><svg viewBox="0 0 {W} {W}" role="img" aria-label="{label}">' + ''.join(o) + '</svg></div>'

CARDS = [
    # ------------------------------------------------ 1 Weierstraß, kompakt
    C('kompakt', Q, 'Kap. 9, Def. 9.17 (5)',
      r"Wann heißt eine Teilmenge \(X\subseteq\mathbb R^n\) <b>kompakt</b>? Nenne typische Beispiele und Gegenbeispiele.",
      r'''<p>\(X\) heißt <b>beschränkt</b>, wenn es ein \(r>0\) mit \(X\subseteq K_r(0)\) gibt, und <b>kompakt</b>, wenn \(X\) <b>beschränkt und abgeschlossen</b> ist.</p>
<p><b>Kompakt</b> sind z. B.</p>
<ul><li>in \(\mathbb R\): jedes abgeschlossene Intervall \([a,b]\) und endliche Vereinigungen davon, etwa \([0,1]\cup[2,3]\);</li>
<li>in \(\mathbb R^2\): jede abgeschlossene Kreisscheibe \(\{x\mid\|x-m\|\le r\}\), jede Kreislinie \(\{x\mid\|x-m\|=r\}\), jedes abgeschlossene Rechteck \([a_1,b_1]\times[a_2,b_2]\) und sein Rand.</li></ul>
<p><b>Nicht kompakt</b> sind z. B. die offene Kreisscheibe \(\{x\mid\|x-m\|<r\}\) (nicht abgeschlossen), \(\mathbb R^2\) selbst (nicht beschränkt) und die Intervalle \([a,b[\), \(]a,b[\), \([a,+\infty[\).</p>''',
      'kompakt beschränkt abgeschlossen Kreisscheibe Kreislinie Rechteck offen'),

    C('weierstrass', Q, 'Kap. 10, Bem. 10.9 (2); Kap. 4, Satz 4.14',
      r"Wie lautet der <b>Satz von Weierstraß</b> für Funktionen mehrerer Veränderlicher, und was ist der Spezialfall für \(f:[a,b]\to\mathbb R\)?",
      r'''<p>Für eine <b>stetige</b> Funktion \(f:D\to\mathbb R\) auf einer <b>kompakten</b> Definitionsmenge \(\emptyset\ne D\subseteq\mathbb R^n\) gilt:</p>
<ol><li>Die Wertemenge \(W_f\subseteq\mathbb R\) ist kompakt.</li>
<li>\(f\) nimmt <b>Maximum und Minimum</b> an, d. h. es gibt \(p,q\in D\) mit \(f(p)\le f(x)\le f(q)\) für alle \(x\in D\).</li>
<li>Ist \(D\) zusätzlich <b>zusammenhängend</b>, so gilt \(W_f=[f(p),f(q)]\).</li></ol>
<p><b>Spezialfall</b> (Satz 4.14): Eine stetige Funktion \(f:[a,b]\to\mathbb R\) ist beschränkt, nimmt Minimum und Maximum an, und es gilt \(W_f=[f(p),f(q)]\). Das Intervall \([a,b]\) ist kompakt und zusammenhängend.</p>''',
      'Weierstraß Satz kompakt stetig Maximum Minimum Wertemenge zusammenhängend'),

    C('weierstrass-anwenden', Q, 'Lösung Bl. 1, A2 und A4; Bl. 4, A13',
      r"Wie begründet man in einer Aufgabe, dass \(f\) auf \(D\) <b>globale Extremstellen</b> besitzt (z. B. \(f(x,y)=\cos(x)+\sin(y)\) auf \([-\pi,\pi]\times[0,\pi]\))?",
      r'''<p>Zwei Dinge zeigen, dann den Satz von Weierstraß zitieren:</p>
<ol><li><b>\(D\) ist kompakt:</b> \(D\) ist abgeschlossen und beschränkt (hier: abgeschlossenes Rechteck).</li>
<li><b>\(f\) ist stetig:</b> als Summe, Produkt oder Verkettung stetiger Funktionen (hier: Summe zweier trigonometrischer Funktionen).</li></ol>
<p>Nach dem <b>Satz von Weierstraß</b> gibt es dann (mindestens) eine globale Minimalstelle \((a,b)\) und eine globale Maximalstelle \((c,d)\) mit \(f(a,b)\le f(x,y)\le f(c,d)\) für alle \((x,y)\in D\).</p>
<p>Im Beispiel: \(f\le 1+1=2\) mit Gleichheit genau für \(x=0,\ y=\tfrac\pi2\); \(f\ge-1+0=-1\) mit Gleichheit in den Eckpunkten \((\pm\pi,0),(\pm\pi,\pi)\).</p>''',
      'Weierstraß anwenden Begründung globale Extremstellen kompakt stetig Aufgabe'),

    # ------------------------------------------------ 2 Polarkoordinaten
    C('polar-scheibe', Q, 'Kap. 10, Bsp. 10.4 (4); Lösung Bl. 1, A3',
      r"Wie beschreibt man die <b>abgeschlossene Kreisscheibe</b> \(\{(x,y)\mid x^2+y^2\le R^2\}\) in <b>Polarkoordinaten</b>?",
      r'''<p>Jeder Punkt \((x,y)\) der Kreisscheibe hat eine Darstellung</p>
\[x=r\cos(\varphi),\quad y=r\sin(\varphi)\]<p>mit \(r\in[0,R]\) und \(\varphi\in[0,2\pi]\).</p>
<p>Dabei ist \(r\) der Abstand vom Ursprung und \(\varphi\) der Winkel zur positiven \(x\)-Achse.</p>
<p><b>Beispiel</b> (Lösung Bl. 1, A3): \(M=\{x^2+y^2\le2\}\) hat Radius \(\sqrt2\), also \(r\in[0,\sqrt2]\), \(\varphi\in[0,2\pi]\). Oft zerfällt \(f\) dann in einen Faktor in \(\varphi\) und einen in \(r\), die man getrennt untersucht.</p>
<div class="tip"><b>Wichtig:</b> Für die <i>ganze Scheibe</i> läuft auch \(r\). Bei festem \(r\) erhält man nur die Kreislinie (eigene Karte).</div>''',
      'Polarkoordinaten Kreisscheibe Radius Winkel r phi Darstellung'),

    C('polar-linie', Q, 'Kap. 9, Bsp. 9.6 (2); Kap. 10, Bsp. 10.10 (2); Lösung Bl. 4, A14',
      r"Wie parametrisiert man die <b>Kreislinie</b> \(\{(x,y)\mid x^2+y^2=r^2\}\)? Was beschreibt \(\rho(\varphi)=(\sqrt2\cos\varphi,\ \sqrt2\sin\varphi)\), \(\varphi\in[0,2\pi]\)?",
      r'''<p>Bei <b>festem</b> Radius \(r>0\):</p>
\[\varphi\mapsto\bigl(r\cos(\varphi),\ r\sin(\varphi)\bigr)\]<p>mit \(\varphi\in[0,2\pi]\).</p>
<p>Für \(\varphi=0\) und \(\varphi=2\pi\) erhält man denselben Punkt \((r,0)\).</p>
<p>\(\rho(\varphi)=(\sqrt2\cos\varphi,\sqrt2\sin\varphi)\) beschreibt daher nur den <b>Rand</b> \(\{x^2+y^2=2\}\) der Kreisscheibe \(\{x^2+y^2\le2\}\), nicht die ganze Scheibe. Für die Scheibe braucht man \((r\cos\varphi,r\sin\varphi)\) mit \(r\in[0,\sqrt2]\).</p>
<p><b>Teilbögen</b> über den Winkelbereich: Viertelkreis im 1. Quadranten \(\varphi\in[0,\frac\pi2]\) (Lösung Bl. 4, A13); Teil von \(x^2+y^2=3\) mit \(x+y\ge0\): \(\varphi\in[-\frac\pi4,\frac{3\pi}4]\) (Lösung Bl. 1, A4).</p>''',
      'Kreislinie Parametrisierung Rand Kreisbogen Viertelkreis Polarkoordinaten fester Radius'),

    C('hilfsfunktion', Q, 'Kap. 10, Bsp. 10.10 (2); Lösung Bl. 2, A7a',
      r"Wie bestimmt man die globalen Extremstellen von \(f\) auf der <b>Einheitskreislinie</b> mit einer <b>Hilfsfunktion</b> \(h(\varphi)\)?",
      r'''<ol><li>Kreislinie ist kompakt, \(f\) stetig ⇒ nach <b>Weierstraß</b> existieren Maximum und Minimum.</li>
<li>Einsetzen: \(x=\cos\varphi\), \(y=\sin\varphi\), \(\varphi\in[0,2\pi]\), ergibt \(h(\varphi)=f(\cos\varphi,\sin\varphi)\).</li>
<li><b>Kandidaten</b> für Extremstellen von \(h\): die <b>Randpunkte</b> \(0\) und \(2\pi\) sowie die <b>Nullstellen von \(h'\)</b> in \(]0,2\pi[\).</li>
<li>Zugehörige Punkte \((x,y)\) bestimmen und eine <b>Wertetabelle</b> aufstellen.</li></ol>
<p><b>Beispiel</b> (Lösung Bl. 2, A7a): \(f(x,y)=2x^3-3y\), \(h(\varphi)=2\cos^3\varphi-3\sin\varphi\),</p>
\[h'(\varphi)=-3\cos\varphi\,\bigl(\sin(2\varphi)+1\bigr),\]
<p>Nullstellen \(\frac\pi2,\frac{3\pi}4,\frac{3\pi}2,\frac{7\pi}4\). Minimum \(-3\) in \((0,1)\), Maximum \(3\) in \((0,-1)\).</p>''',
      'Hilfsfunktion Kreislinie Extremstellen Polarkoordinaten Kandidaten Wertetabelle'),

    # ------------------------------------------------ 3 Strecken, Rand
    C('strecke', Q, 'Kap. 9, Def. 9.15 (2a), Bsp. 9.6 (1)',
      r"Wie parametrisiert man die <b>Verbindungsstrecke</b> zweier Punkte \(x,y\in\mathbb R^n\)?",
      r'''\[\{\,x+t\,(y-x)\mid t\in[0,1]\,\}.\]
<p>Für \(t=0\) ist man in \(x\), für \(t=1\) in \(y\). Lässt man \(t\) durch ganz \(\mathbb R\) laufen, erhält man die <b>Gerade</b> \(a+\mathbb R\cdot u\) mit Trägerpunkt \(a=x\) und Richtungsvektor \(u=y-x\) (Bsp. 9.6 (1)).</p>
<p><b>Beispiel:</b> Strecke von \((1,0)\) nach \((0,2)\): \((1,0)+t\,(-1,2)=(1-t,\,2t)\). Gleichwertig ist \((t,\,2-2t)\) mit \(t\in[0,1]\) (andere Durchlaufrichtung, Bsp. 10.10 (2b)).</p>''',
      'Strecke Verbindungsstrecke Parametrisierung Gerade konvex Richtungsvektor'),

    C('rand-polygon', Q, 'Lösung Bl. 2, A7b; Bl. 4, A15; Kap. 10, Bsp. 10.10 (2b)',
      r"Wie untersucht man \(f\) auf dem <b>Rand eines Dreiecks oder Rechtecks</b>?",
      r'''<p>Jede <b>Seite einzeln</b> als Strecke parametrisieren und die Hilfsfunktion \(h_i(t)=f(\text{Seite}(t))\) untersuchen. Kandidaten je Seite: die <b>Eckpunkte</b> und die Nullstellen von \(h_i'\) im Innern.</p>
<p><b>Dreieck</b> mit Ecken \((0,0),(1,0),(1,1)\) (Lösung Bl. 2, A7b):</p>
<ul><li>untere Kathete \((t,0)\), \(t\in[0,1]\),</li><li>rechte Kathete \((1,t)\), \(t\in[0,1]\),</li><li>Hypotenuse \((t,t)\), \(t\in[0,1]\).</li></ul>
<p><b>Rechteck</b> \([-1,1]\times[0,2\pi]\) (Lösung Bl. 4, A15): \((-1,t)\) und \((1,t)\) mit \(t\in[0,2\pi]\), \((t,0)\) und \((t,2\pi)\) mit \(t\in[-1,1]\).</p>
<p>Zum Schluss alle Kandidaten (Rand und Innere) in eine <b>Wertetabelle</b>.</p>''',
      'Rand Dreieck Rechteck Seiten parametrisieren Kathete Hypotenuse Hilfsfunktion Eckpunkte'),

    # ------------------------------------------------ 4 sin/cos
    C('sin-cos-eigenschaften', QD, 'Kap. 5, Satz 5.10, Bem. 5.9',
      r"Welche Eigenschaften haben \(\sin\) und \(\cos\) (Symmetrie, Periode, Nullstellen, Maximum/Minimum, Wertebereich)?",
      r'''<table><tr><th></th><th>\(\sin\)</th><th>\(\cos\)</th></tr>
<tr><td>Symmetrie</td><td>ungerade</td><td>gerade</td></tr>
<tr><td>Periode</td><td>\(2\pi\)</td><td>\(2\pi\)</td></tr>
<tr><td>Nullstellen</td><td>\(k\pi\), \(k\in\mathbb Z\)</td><td>\(k\pi+\frac\pi2\), \(k\in\mathbb Z\)</td></tr>
<tr><td>Max. 1 in</td><td>\(2k\pi+\frac\pi2\)</td><td>\(2k\pi\)</td></tr>
<tr><td>Min. −1 in</td><td>\(2k\pi-\frac\pi2\)</td><td>\((2k+1)\pi\)</td></tr>
<tr><td>Wertebereich</td><td>\([-1,1]\)</td><td>\([-1,1]\)</td></tr></table>
<p>Also \(\sin(-x)=-\sin x\) und \(\cos(-x)=\cos x\). Beide sind stetig, und für alle \(x\) gilt \(\sin^2(x)+\cos^2(x)=1\).</p>''',
      'Sinus Cosinus Eigenschaften gerade ungerade Periode periodisch Nullstellen Maximum Minimum Wertebereich'),

    C('sin-cos-werte', QD, 'Kap. 5, Bem. 5.9 (3b), Satz 5.11; Kap. 10, Bsp. 10.4 (4), 10.10 (2); Lösung Bl. 2, A7',
      r"Wie lauten \(\sin\) und \(\cos\) an den Stellen \(0,\ \frac\pi6,\ \frac\pi4,\ \frac\pi3,\ \frac\pi2,\ \pi,\ \frac{3\pi}2,\ 2\pi\)?",
      r'''<table><tr><th>\(x\)</th><th>Grad</th><th>\(\sin x\)</th><th>\(\cos x\)</th><th>\(\tan x\)</th></tr>
<tr><td>\(0\)</td><td>0°</td><td>\(0\)</td><td>\(1\)</td><td>\(0\)</td></tr>
<tr><td>\(\frac\pi6\)</td><td>30°</td><td>\(\frac12\)</td><td>\(\frac12\sqrt3\)</td><td>\(\frac13\sqrt3\)</td></tr>
<tr><td>\(\frac\pi4\)</td><td>45°</td><td>\(\frac12\sqrt2\)</td><td>\(\frac12\sqrt2\)</td><td>\(1\)</td></tr>
<tr><td>\(\frac\pi3\)</td><td>60°</td><td>\(\frac12\sqrt3\)</td><td>\(\frac12\)</td><td>\(\sqrt3\)</td></tr>
<tr><td>\(\frac\pi2\)</td><td>90°</td><td>\(1\)</td><td>\(0\)</td><td>–</td></tr>
<tr><td>\(\pi\)</td><td>180°</td><td>\(0\)</td><td>\(-1\)</td><td>\(0\)</td></tr>
<tr><td>\(\frac{3\pi}2\)</td><td>270°</td><td>\(-1\)</td><td>\(0\)</td><td>–</td></tr>
<tr><td>\(2\pi\)</td><td>360°</td><td>\(0\)</td><td>\(1\)</td><td>\(0\)</td></tr></table>
<p>„–“: \(\tan=\frac{\sin}{\cos}\) ist dort nicht definiert (Nullstellen von \(\cos\)). \(\frac12\sqrt2=\frac1{\sqrt2}\). Die Werte bei \(\frac\pi3\) folgen aus denen bei \(\frac\pi6\) mit \(\sin(\frac\pi2-x)=\cos x\) und \(\cos(\frac\pi2-x)=\sin x\).</p>'''
      + H(r'Merkregel für \(0,\frac\pi6,\frac\pi4,\frac\pi3,\frac\pi2\): \(\sin\) ist der Reihe nach \(\frac12\sqrt0,\ \frac12\sqrt1,\ \frac12\sqrt2,\ \frac12\sqrt3,\ \frac12\sqrt4\); \(\cos\) dieselben Werte rückwärts. Gradzahlen nur zur Orientierung, im Skript wird im Bogenmaß gerechnet.')
      + graph([('sin', 'k-sin'), ('cos', 'k-cos')], label='Graphen von sin und cos'),
      'Sinus Cosinus Tangens Werte Tabelle pi/6 pi/4 pi/3 Wurzel 3 Wurzel 2 spezielle Werte Grad Merkregel 30 45 60'),

    C('einheitskreis', QD, 'Kap. 9, Bsp. 9.6 (2); Kap. 10, Bsp. 10.4 (4), 10.10 (2); Kap. 5, Bem. 5.9',
      r"Wie liest man \(\sin\varphi\) und \(\cos\varphi\) am <b>Einheitskreis</b> ab, und wie erhält man die Werte in allen vier Quadranten?",
      kreis(alle=True, labels=True, label='Einheitskreis mit Standardwinkeln') +
      r'''<p>Zum Winkel \(\varphi\) gehört der Punkt \(\bigl(\cos\varphi,\ \sin\varphi\bigr)\): <b>\(x\)-Koordinate = Cosinus</b>, <b>\(y\)-Koordinate = Sinus</b>.</p>
<p>In den anderen Quadranten kommen dieselben Beträge wie im 1. Quadranten vor, nur die Vorzeichen wechseln:</p>
<table><tr><th>Quadrant</th><th>Winkel</th><th>\(\cos\)</th><th>\(\sin\)</th></tr>
<tr><td>1.</td><td>\(\varphi\)</td><td>+</td><td>+</td></tr>
<tr><td>2.</td><td>\(\pi-\varphi\)</td><td>−</td><td>+</td></tr>
<tr><td>3.</td><td>\(\pi+\varphi\)</td><td>−</td><td>−</td></tr>
<tr><td>4.</td><td>\(2\pi-\varphi\)</td><td>+</td><td>−</td></tr></table>
<p>Beispiele: \(\frac{2\pi}3=\pi-\frac\pi3\) ergibt \((-\frac12,\ \frac12\sqrt3)\); \(\frac{7\pi}6=\pi+\frac\pi6\) ergibt \((-\frac12\sqrt3,\ -\frac12)\); \(\frac{7\pi}4=2\pi-\frac\pi4\) ergibt \((\frac12\sqrt2,\ -\frac12\sqrt2)\).</p>'''
      + H(r'Die Vorzeichenregeln folgen aus Bem. 5.9: \(\sin(x+\pi)=-\sin x\), \(\cos(x+\pi)=-\cos x\), \(\sin(-x)=-\sin x\), \(\cos(-x)=\cos x\) und der \(2\pi\)-Periode.'),
      'Einheitskreis Quadrant Vorzeichen Koordinaten Standardwinkel 2pi/3 5pi/6 7pi/6 4pi/3 5pi/3 11pi/6 ablesen'),

    C('sin-cos-graph', QD, 'Kap. 5, Satz 5.10',
      r"Wie sehen die <b>Graphen</b> von \(\sin\) und \(\cos\) aus? Woran erkennt man, welcher welcher ist?",
      graph([('sin', 'k-sin'), ('cos', 'k-cos')], label='Graphen von sin und cos') +
      r'''<ul><li><b>\(\sin\)</b> geht durch den Ursprung (\(\sin 0=0\)), steigt bis \(1\) bei \(\frac\pi2\), Nullstellen bei \(0,\pi,2\pi\), Minimum \(-1\) bei \(\frac{3\pi}2\). Punktsymmetrisch zum Ursprung (ungerade).</li>
<li><b>\(\cos\)</b> beginnt bei \(1\) (\(\cos0=1\)), Nullstellen bei \(\frac\pi2\) und \(\frac{3\pi}2\), Minimum \(-1\) bei \(\pi\). Achsensymmetrisch zur \(y\)-Achse (gerade).</li>
<li>Der Cosinus ist der um \(\frac\pi2\) nach links verschobene Sinus: \(\cos x=\sin(x+\frac\pi2)\).</li></ul>'''
      + H(r'\(\cos x=\sin(x+\frac\pi2)\) folgt aus \(\sin(\frac\pi2-x)=\cos x\) und \(\cos(-x)=\cos x\).'),
      'Graph Sinus Cosinus Kurve Verlauf zeichnen erkennen Symmetrie'),

    C('tan', QD, 'Kap. 5, Satz 5.11; Kap. 6, Bsp. 6.6 (3)',
      r"Wie ist der <b>Tangens</b> definiert? Definitionsbereich, Periode, Nullstellen, Polstellen?",
      r'''\[\tan(x)=\frac{\sin(x)}{\cos(x)}\quad\text{für } x\ne k\pi+\tfrac\pi2\]
<ul><li>stetig, ungerade und <b>\(\pi\)-periodisch</b>,</li>
<li>Nullstellen \(k\pi\) (die von \(\sin\)),</li>
<li>nicht definiert bei \(k\pi+\frac\pi2\) (Nullstellen von \(\cos\)); dort \(\lim\tan(x)=\mp\infty\) von rechts bzw. links,</li>
<li>auf jedem Intervall \(]k\pi-\frac\pi2,\ k\pi+\frac\pi2[\) streng monoton wachsend, Wertebereich \(\mathbb R\),</li>
<li>Ableitung \(\tan'(x)=1+\tan^2(x)=\frac1{\cos^2(x)}\).</li></ul>'''
      + graph([('tan', 'k-tan')], ymax=3, label='Graph von tan'),
      'Tangens tan Definition Polstellen Periode Nullstellen Graph'),

    C('sin-cos-verschieben', QD, 'Kap. 5, Bem. 5.9 (1), (3b); Lösung Bl. 2, A7',
      r"Welche Verschiebungsformeln gelten für \(\sin\) und \(\cos\) (um \(\frac\pi2\), \(\pi\), \(2\pi\))? Welcher Punkt der Einheitskreislinie gehört zu \(\varphi=\frac{3\pi}4\) und \(\varphi=\frac{7\pi}4\)?",
      r'''<p>Für alle \(x\in\mathbb R\):</p>
\[\begin{aligned}\sin(\tfrac\pi2-x)&=\cos x\\ \cos(\tfrac\pi2-x)&=\sin x\\ \sin(x+\pi)&=-\sin x\\ \cos(x+\pi)&=-\cos x\\ \sin(x+2\pi)&=\sin x\\ \cos(x+2\pi)&=\cos x\end{aligned}\]
<p>Damit erhält man die Punkte (Lösung Bl. 2, A7a):</p>
<ul><li>\(\varphi=\frac{3\pi}4\): \((-\frac12\sqrt2,\ \frac12\sqrt2)\)</li>
<li>\(\varphi=\frac{5\pi}4\): \((-\frac1{\sqrt2},\ -\frac1{\sqrt2})\) (Bsp. 10.4 (4))</li>
<li>\(\varphi=\frac{7\pi}4\): \((\frac12\sqrt2,\ -\frac12\sqrt2)\)</li></ul>''',
      'Verschiebung Sinus Cosinus pi halbe Periode Einheitskreis 3pi/4 7pi/4 5pi/4'),

    # ------------------------------------------------ 5 Additionstheoreme
    C('additionstheoreme', QD, 'Kap. 5, Bem. 5.9 (2a, b)',
      r"Wie lauten die <b>Additionstheoreme</b> für \(\sin(x\pm y)\) und \(\cos(x\pm y)\)?",
      r'''\[\sin(x+y)=\sin x\cos y+\cos x\sin y\]
\[\sin(x-y)=\sin x\cos y-\cos x\sin y\]
\[\cos(x+y)=\cos x\cos y-\sin x\sin y\]
\[\cos(x-y)=\cos x\cos y+\sin x\sin y\]
<div class="tip"><b>Vorzeichen:</b> Beim Sinus bleibt das Vorzeichen, beim Cosinus dreht es sich um.</div>
<p><b>Anwendung</b> (Lösung Bl. 3, A9b): Für \(g=\sin(x_1+x_2)\cos(x_1-x_2)\) ergibt die Produktregel mit dem Additionstheorem</p>
\[\begin{aligned}\partial_1g&=\cos(x_1+x_2)\cos(x_1-x_2)\\ &\quad-\sin(x_1+x_2)\sin(x_1-x_2)\\ &=\cos\bigl((x_1+x_2)+(x_1-x_2)\bigr)\\ &=\cos(2x_1).\end{aligned}\]''',
      'Additionstheoreme Additionstheorem Sinus Cosinus Summe Differenz Winkel'),

    C('doppelwinkel', QD, 'Kap. 5, Bem. 5.9 (2c–e); Lösung Bl. 2, A7a; Bl. 4, A13',
      r"Welche Formeln folgen aus den Additionstheoremen für \(\sin(2x)\), \(\cos(2x)\), \(\sin^2(x)\) und \(\cos^2(x)\)?",
      r'''\[\sin^2(x)+\cos^2(x)=1\]
\[\begin{aligned}\sin(2x)&=2\sin(x)\cos(x)\\ \cos(2x)&=\cos^2(x)-\sin^2(x)\\ \sin^2(x)&=\tfrac12\bigl(1-\cos(2x)\bigr)\\ \cos^2(x)&=\tfrac12\bigl(1+\cos(2x)\bigr)\end{aligned}\]
<p><b>In den Übungen:</b></p>
<ul><li>\(2\sin\varphi\cos\varphi+1=\sin(2\varphi)+1\) (Lösung Bl. 2, A7a)</li>
<li>\(\cos\varphi\cdot\sin\varphi=\frac{\sin(2\varphi)}2\) (Lösung Bl. 4, A13)</li>
<li>\(\cos^2\varphi=1-\sin^2\varphi\) zum Vereinfachen (Lösung Bl. 1, A3)</li></ul>''',
      'Doppelwinkel sin 2x cos 2x sin quadrat cos quadrat trigonometrischer Pythagoras'),

    # ------------------------------------------------ 6 Ableitungen
    C('ableitungsregeln', QD, 'Kap. 6, Satz 6.5',
      r"Wie lauten <b>Produkt-, Quotienten- und Kettenregel</b>?",
      r'''<p>Für in \(a\) differenzierbare \(f,g\) und \(\lambda\in\mathbb R\):</p>
\[(f\pm g)'=f'\pm g',\qquad(\lambda f)'=\lambda f'\]
<p><b>Produktregel</b> (alles an der Stelle \(a\)):</p>\[(f\cdot g)'=f'\cdot g+f\cdot g'\]
<p><b>Quotientenregel</b> (für \(g(a)\ne0\)):</p>\[\left(\frac fg\right)'=\frac{f'\cdot g-f\cdot g'}{g^2}\]
<p><b>Kettenregel</b> (\(g\) in \(a\) und \(f\) in \(g(a)\) differenzierbar):</p>
\[(f\circ g)'(a)=f'\bigl(g(a)\bigr)\cdot g'(a)\]''',
      'Ableitungsregeln Produktregel Quotientenregel Kettenregel Ableitung Summe'),

    C('ableitungen-grund', QD, 'Kap. 6, Bsp. 6.3, 6.6 (3, 4), 6.8 (1, 2, 6)',
      r"Wie lauten die Ableitungen von \(\sin,\ \cos,\ \tan,\ e^x,\ e^{g(x)},\ \ln x,\ \ln|x|,\ \ln|g(x)|\) und \(x^r\)?",
      r'''<table><tr><th>Funktion</th><th>Ableitung</th></tr>
<tr><td>\(\sin x\)</td><td>\(\cos x\)</td></tr>
<tr><td>\(\cos x\)</td><td>\(-\sin x\)</td></tr>
<tr><td>\(\tan x\)</td><td>\(1+\tan^2 x=\frac1{\cos^2x}\)</td></tr>
<tr><td>\(e^x\)</td><td>\(e^x\)</td></tr>
<tr><td>\(e^{g(x)}\)</td><td>\(e^{g(x)}\cdot g'(x)\)</td></tr>
<tr><td>\(\ln x\) \((x>0)\)</td><td>\(\frac1x\)</td></tr>
<tr><td>\(\ln|x|\) \((x\ne0)\)</td><td>\(\frac1x\)</td></tr>
<tr><td>\(\ln|g(x)|\)</td><td>\(\frac{g'(x)}{g(x)}\)</td></tr>
<tr><td>\(x^r\) \((x>0,\ r\in\mathbb R)\)</td><td>\(r\,x^{r-1}\)</td></tr></table>
<p>Beispiele: \((e^{\lambda x})'=\lambda e^{\lambda x}\), \((e^{\sin x})'=e^{\sin x}\cos x\), \((e^{\sqrt x})'=e^{\sqrt x}\cdot\frac1{2\sqrt x}\).</p>''',
      'Ableitung sin cos tan exp ln Logarithmus Potenz Exponentialfunktion Grundableitungen'),

    C('allg-potenz', QD, 'Kap. 5, Def. 5.6 (2), Satz 5.7; Lösung Bl. 3, A9d',
      r"Wie ist die <b>allgemeine Potenz</b> \(a^x\) definiert, und wie leitet man eine Funktion wie \(k(x_1,x_2)=(x_1^2+1)^{-x_2}\) nach \(x_2\) ab?",
      r'''<p>Für \(a>0\) und \(x\in\mathbb R\):</p>
\[a^x=\exp\bigl(x\cdot\ln(a)\bigr).\]
<p>Es gelten die Potenzgesetze \(a^x a^y=a^{x+y}\), \(\frac{a^x}{a^y}=a^{x-y}\), \(a^xb^x=(ab)^x\), \((a^x)^y=a^{xy}\).</p>
<p><b>Steht die Variable im Exponenten,</b> schreibt man in eine e-Funktion um (Lösung Bl. 3, A9d):</p>
\[\begin{aligned}k(x_1,x_2)&=(x_1^2+1)^{-x_2}\\ &=e^{-x_2\ln(x_1^2+1)}\end{aligned}\]
\[\begin{aligned}\partial_2k&=e^{-x_2\ln(x_1^2+1)}\cdot\bigl(-\ln(x_1^2+1)\bigr)\\ &=-(x_1^2+1)^{-x_2}\ln(x_1^2+1).\end{aligned}\]
<p>Nach \(x_1\) (Variable nur in der Basis) geht auch die Potenzregel: \(\partial_1k=-x_2(x_1^2+1)^{-x_2-1}\cdot2x_1\).</p>'''
      + H(r"Allgemein folgt so \((a^x)'=\ln(a)\cdot a^x\)."),
      'allgemeine Potenz a hoch x exp ln Exponent Variable im Exponenten umschreiben Potenzgesetze'),

    # ------------------------------------------------ 7 de l'Hospital
    C('hospital', Q, 'Kap. 6, Satz 6.17, Bsp. 6.18; Lösung Bl. 3, A10a',
      r"Wie lautet die <b>Regel von de l’Hospital</b>, und worauf muss man bei der Anwendung achten?",
      r'''<p>Seien \(f,g:\,]a,b[\,\to\mathbb R\) differenzierbar mit \(g'(x)\ne0\), und es liege einer der Fälle vor:</p>
<ul><li>„\(\frac00\)“: \(\lim_{x\to a+}f(x)=0\) und \(\lim_{x\to a+}g(x)=0\), oder</li>
<li>„\(\frac{\pm\infty}{\pm\infty}\)“: \(\lim_{x\to a+}g(x)=\pm\infty\).</li></ul>
<p><b>Existiert</b> \(\lim_{x\to a+}\frac{f'(x)}{g'(x)}\) (eigentlich oder uneigentlich), so existiert auch \(\lim_{x\to a+}\frac{f(x)}{g(x)}\), und beide sind gleich. Analog für \(x\to b-\) und \(x\to\pm\infty\).</p>
<div class="tip"><b>Mehrfach anwenden:</b> Erst die Existenz des <i>letzten</i> Grenzwerts begründet alle Gleichheitszeichen davor. Vor jedem Schritt prüfen, ob wirklich „\(\frac00\)“ (bzw. „\(\frac\infty\infty\)“) vorliegt.</div>
<p><b>Beispiel</b> (Lösung Bl. 3, A10a, viermal angewendet): \(\displaystyle\lim_{r\to0}\frac{2-2\cos r-r^2}{r^4}=-\frac1{12}\).</p>''',
      'de l Hospital Hospital Grenzwert 0/0 unendlich Quotient Regel L H'),

    # ------------------------------------------------ 10 injektiv/surjektiv, ZWS
    C('nullstellensatz-zws', Q, 'Kap. 4, Satz 4.11, 4.13',
      r"Wie lauten der <b>Nullstellensatz</b> und der <b>Zwischenwertsatz</b>?",
      r'''<p><b>Nullstellensatz:</b> Ist \(f:[a,b]\to\mathbb R\) stetig mit \(f(a)\cdot f(b)<0\), so gibt es ein \(\xi\in\,]a,b[\) mit \(f(\xi)=0\).</p>
<p><b>Zwischenwertsatz:</b> Ist \(f:[a,b]\to\mathbb R\) stetig und \(c\) ein Wert zwischen \(f(a)\) und \(f(b)\), so gibt es ein \(\xi\in[a,b]\) mit \(f(\xi)=c\).</p>
<p>Beweisidee ZWS: Nullstellensatz auf \(g(x)=f(x)-c\) anwenden.</p>
<p><b>Im \(\mathbb R^n\)</b> (Bem. 10.9 (1)): Verbindet eine Kurve \(\varphi\) in \(D\) zwei Punkte \(p,q\) mit \(f(p)<0<f(q)\), so hat \(h=f\circ\varphi\) eine Nullstelle; also gibt es \(x_0\) auf der Kurve mit \(f(x_0)=0\).</p>''',
      'Nullstellensatz Zwischenwertsatz stetig Intervall Vorzeichenwechsel'),

    C('injektiv-surjektiv', Q, 'Kap. 4, Def. 4.16, Satz 4.17; Kap. 6, Bsp. 6.8 (5)',
      r"Wann heißt \(f:D_f\to\mathbb R\) <b>injektiv</b> bzw. <b>surjektiv</b>? Wie zeigt man beides für \(f(x)=x+\ln(x)\) auf \(\mathbb R^+\)?",
      r'''<p><b>Injektiv:</b> Für alle \(x_1,x_2\in D_f\) mit \(x_1\ne x_2\) gilt \(f(x_1)\ne f(x_2)\). Dann ist \(f\) umkehrbar.</p>
<p><b>Surjektiv:</b> \(W_f=\mathbb R\), d. h. zu jedem \(y\in\mathbb R\) gibt es ein \(x\) mit \(f(x)=y\).</p>
<p>Jede <b>streng monotone</b> Funktion ist injektiv (Satz 4.17).</p>
<p><b>Beispiel</b> \(f(x)=x+\ln x\):</p>
<ul><li>injektiv: Aus \(x_1<x_2\) folgt \(\ln x_1<\ln x_2\), also \(f(x_1)<f(x_2)\); \(f\) ist streng monoton wachsend;</li>
<li>surjektiv: \(\lim_{x\to0+}f(x)=-\infty\) und \(\lim_{x\to+\infty}f(x)=+\infty\); zu \(y\) gibt es also \(a,b\) mit \(f(a)\le y\le f(b)\), und der <b>Zwischenwertsatz</b> liefert \(\xi\in[a,b]\) mit \(f(\xi)=y\).</li></ul>''',
      'injektiv surjektiv bijektiv umkehrbar streng monoton Zwischenwertsatz Umkehrfunktion'),

    C('kreislinie-weder-noch', Q, 'Blatt 2, A8 und Lösung',
      r"Warum kann eine stetige Funktion \(f\) auf der Einheitskreislinie \(D\) weder <b>surjektiv</b> noch <b>injektiv</b> sein?",
      r'''<p><b>Nicht surjektiv:</b> \(D\) ist kompakt, also nimmt \(f\) nach <b>Weierstraß</b> Minimum und Maximum an: \(W_f\subseteq[f(p_1),f(p_2)]\subsetneq\mathbb R\).</p>
<p><b>Nicht injektiv:</b> Ist \(f(1,0)=f(-1,0)\), fertig. Sonst o. E. \(f(1,0)>f(-1,0)\); setze \(m\) als Mittelwert. Mit \(\varphi(t)=(\cos t,\sin t)\), \(t\in[0,2\pi]\), ist \(h=f\circ\varphi\) stetig mit</p>
\[\begin{aligned}h(0)=h(2\pi)&=f(1,0)>m,\\ h(\pi)&=f(-1,0)<m.\end{aligned}\]
<p>Der <b>Zwischenwertsatz</b> liefert \(\xi_1\in\,]0,\pi[\) und \(\xi_2\in\,]\pi,2\pi[\) mit \(h(\xi_1)=h(\xi_2)=m\): zwei verschiedene Punkte (oberhalb und unterhalb der \(x\)-Achse) mit gleichem Funktionswert.</p>''',
      'Kreislinie injektiv surjektiv Staatsexamen Zwischenwertsatz Weierstraß stetig'),

    # ------------------------------------------------ 11 Kandidaten
    C('kandidaten', Q, 'Kap. 10, Satz 10.13, Zusammenfassung 10.20; Lösung Bl. 4, A14',
      r"Welche Punkte sind <b>Kandidaten für Extremstellen</b> von \(f:D\to\mathbb R\), und wie geht man bei globalen Extremstellen vor?",
      r'''<p><b>Kandidaten</b> (Zusammenfassung 10.20):</p>
<ul><li>die <b>Randpunkte</b> von \(D\),</li>
<li>die Stellen, an denen \(f\) <b>nicht partiell differenzierbar</b> ist,</li>
<li>die <b>kritischen Stellen</b> im Innern: \(\operatorname{grad}f(a)=0\) (Satz 10.13).</li></ul>
<p><b>Vorgehen global:</b> \(f\) stetig, \(D\) kompakt ⇒ Weierstraß. Inneres: kritische Stellen; Rand: parametrisieren (Polarkoordinaten oder Strecken). Dann <b>Wertetabelle</b> aller Kandidaten.</p>
<p><b>Abkürzung</b> (Lösung Bl. 4, A14): Hat \(f\) <i>keine</i> kritischen Punkte, liegen die globalen Extremstellen auf dem Rand.</p>''',
      'Kandidaten Extremstellen Rand kritische Stellen Gradient nicht differenzierbar Wertetabelle Vorgehen'),
]

ITEMS = []

def mc(id, subj, q, options, correct, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, subj=subj, type='mc', q=q, options=options, correct=correct, expl=expl, src=src, kw=kw, warn=warn))

def tf(id, subj, statement, answer, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, subj=subj, type='tf', statement=statement, answer=answer, expl=expl, src=src, kw=kw, warn=warn))

def gap(id, subj, text, expl, src, kw):
    ITEMS.append(dict(id=id, subj=subj, type='gap', text=text, expl=expl, src=src, kw=kw))

# ------------------------------------------------------------ Multiple Choice
mc('allg-mc-01', Q, r'Welche der folgenden Mengen ist <b>nicht</b> kompakt?',
   [r'die offene Einheitskreisscheibe \(\{x^2+y^2<1\}\)', r'die Einheitskreislinie \(\{x^2+y^2=1\}\)', r'das Rechteck \([-1,1]\times[0,2\pi]\)', r'der Viertelkreis \(\{x^2+y^2\le1,\ x\ge0,\ y\ge0\}\)'], 0,
   r'Die offene Kreisscheibe ist beschränkt, aber nicht abgeschlossen (ihr Rand gehört nicht dazu). Kreislinie, abgeschlossenes Rechteck und abgeschlossener Viertelkreis sind beschränkt und abgeschlossen.',
   'Def. 9.17 (5); Lösung Bl. 4, A13, A15', 'kompakt offen Kreisscheibe Beispiele')
mc('allg-mc-02', Q, r'Warum besitzt \(f(x,y)=\cos(x)+\sin(y)\) auf \(D=[-\pi,\pi]\times[0,\pi]\) globale Extremstellen?',
   [r'\(D\) ist kompakt und \(f\) stetig, also greift der Satz von Weierstraß', r'\(f\) ist periodisch', r'\(D\) ist offen und \(f\) differenzierbar', r'\(f\) hat keine kritischen Stellen'], 0,
   r'\(D\) ist ein abgeschlossenes Rechteck, also kompakt; \(f\) ist als Summe zweier trigonometrischer Funktionen stetig. Maximum \(2\) in \((0,\frac\pi2)\), Minimum \(-1\) in den Ecken.',
   'Lösung Bl. 1, A2', 'Weierstraß Begründung kompakt stetig')
mc('allg-mc-03', Q, r'Wie beschreibt man die <b>ganze</b> Kreisscheibe \(M=\{x^2+y^2\le2\}\) in Polarkoordinaten?',
   [r'\((r\cos\varphi,\ r\sin\varphi)\) mit \(r\in[0,\sqrt2]\), \(\varphi\in[0,2\pi]\)', r'\((\sqrt2\cos\varphi,\ \sqrt2\sin\varphi)\) mit \(\varphi\in[0,2\pi]\)', r'\((r\cos\varphi,\ r\sin\varphi)\) mit \(r\in[0,2]\), \(\varphi\in[0,2\pi]\)', r'\((r\cos\varphi,\ r\sin\varphi)\) mit \(r\in[0,\sqrt2]\), \(\varphi\in[0,\pi]\)'], 0,
   r'Der Radius ist \(\sqrt2\), und für die ganze Scheibe muss auch \(r\) laufen. Mit festem \(r=\sqrt2\) erhält man nur den Rand; \(\varphi\in[0,\pi]\) ergibt nur die obere Hälfte.',
   'Bsp. 10.4 (4); Lösung Bl. 1, A3', 'Polarkoordinaten Kreisscheibe Radius', warn=True)
mc('allg-mc-04', Q, r'Was beschreibt \(\rho(\varphi)=(\sqrt2\cos\varphi,\ \sqrt2\sin\varphi)\) mit \(\varphi\in[0,2\pi]\)?',
   [r'die Kreislinie um \((0,0)\) mit Radius \(\sqrt2\)', r'die Kreisscheibe um \((0,0)\) mit Radius \(\sqrt2\)', r'die Kreislinie um \((0,0)\) mit Radius \(2\)', r'einen Halbkreis mit Radius \(\sqrt2\)'], 0,
   r'Bei festem Radius entsteht nur die Kreislinie \(x^2+y^2=2\), also der Rand der Scheibe \(\{x^2+y^2\le2\}\).',
   'Bsp. 9.6 (2); Lösung Bl. 4, A14', 'Kreislinie Rand Parametrisierung Radius', warn=True)
mc('allg-mc-05', Q, r'Welcher Winkelbereich beschreibt den Viertelkreisbogen \(\{x^2+y^2=1,\ x\ge0,\ y\ge0\}\) mit \(x=\cos\varphi\), \(y=\sin\varphi\)?',
   [r'\(\varphi\in[0,\frac\pi2]\)', r'\(\varphi\in[0,\pi]\)', r'\(\varphi\in[\frac\pi2,\pi]\)', r'\(\varphi\in[-\frac\pi2,0]\)'], 0,
   r'Im 1. Quadranten sind \(\cos\varphi\ge0\) und \(\sin\varphi\ge0\), also \(\varphi\) zwischen \(0\) und \(\frac\pi2\).',
   'Lösung Bl. 4, A13', 'Viertelkreis Winkelbereich Polarkoordinaten Quadrant')
mc('allg-mc-06', Q, r'Welcher Winkelbereich gehört zum Teil der Kreislinie \(x^2+y^2=3\) mit \(x+y\ge0\)?',
   [r'\(\varphi\in[-\frac\pi4,\frac{3\pi}4]\)', r'\(\varphi\in[0,\pi]\)', r'\(\varphi\in[\frac\pi4,\frac{5\pi}4]\)', r'\(\varphi\in[-\frac\pi2,\frac\pi2]\)'], 0,
   r'\(x+y\ge0\) heißt: auf oder oberhalb der Geraden \(y=-x\). Diese trifft den Kreis bei \(\varphi=-\frac\pi4\) und \(\varphi=\frac{3\pi}4\).',
   'Lösung Bl. 1, A4c', 'Kreisbogen Winkelbereich Winkelhalbierende Polarkoordinaten')
mc('allg-mc-07', Q, r'Wie parametrisiert man die Strecke von \((1,0)\) nach \((0,2)\)?',
   [r'\((t,\ 2-2t)\) mit \(t\in[0,1]\)', r'\((t,\ 2t)\) mit \(t\in[0,1]\)', r'\((t,\ 2-t)\) mit \(t\in[0,1]\)', r'\((2-2t,\ t)\) mit \(t\in[0,1]\)'], 0,
   r'Probe: \(t=0\) ergibt \((0,2)\), \(t=1\) ergibt \((1,0)\), dazwischen linear. Die anderen Kurven treffen nicht beide Endpunkte.',
   'Bsp. 10.10 (2b); Def. 9.15 (2a)', 'Strecke Hypotenuse Parametrisierung Dreieck')
mc('allg-mc-08', Q, r'Welche Menge ist die <b>Verbindungsstrecke</b> von \(x\) nach \(y\) im \(\mathbb R^n\)?',
   [r'\(\{x+t(y-x)\mid t\in[0,1]\}\)', r'\(\{x+t(y-x)\mid t\in\mathbb R\}\)', r'\(\{x+ty\mid t\in[0,1]\}\)', r'\(\{t(x+y)\mid t\in[0,1]\}\)'], 0,
   r'Für \(t=0\) erhält man \(x\), für \(t=1\) erhält man \(y\). Mit \(t\in\mathbb R\) wäre es die ganze Gerade.',
   'Def. 9.15 (2a)', 'Verbindungsstrecke Strecke Gerade konvex')
mc('allg-mc-09', Q, r'Eine differenzierbare Hilfsfunktion \(h:[0,2\pi]\to\mathbb R\) soll global maximiert werden. Welche Stellen muss man prüfen?',
   [r"die Randpunkte \(0\) und \(2\pi\) sowie die Nullstellen von \(h'\) in \(]0,2\pi[\)", r"nur die Nullstellen von \(h'\)", r'nur die Randpunkte \(0\) und \(2\pi\)', r'die Nullstellen von \(h\)'], 0,
   r'Auf einem abgeschlossenen Intervall können Extrema auch am Rand liegen. Im Innern kommen bei Differenzierbarkeit nur Nullstellen der Ableitung in Frage.',
   'Bsp. 10.10 (2); Lösung Bl. 2, A7a', 'Hilfsfunktion Randpunkte Ableitung Nullstellen Kandidaten')
mc('allg-mc-10', Q, r"Für \(h(\varphi)=2\cos^3\varphi-3\sin\varphi\) ist \(h'(\varphi)=-3\cos\varphi\,(\sin(2\varphi)+1)\). Welche Nullstellen hat \(h'\) in \([0,2\pi]\)?",
   [r'\(\frac\pi2,\ \frac{3\pi}4,\ \frac{3\pi}2,\ \frac{7\pi}4\)', r'\(\frac\pi2,\ \frac{3\pi}2\)', r'\(\frac\pi4,\ \frac\pi2,\ \frac{5\pi}4,\ \frac{3\pi}2\)', r'\(0,\ \pi,\ 2\pi\)'], 0,
   r'\(\cos\varphi=0\) bei \(\frac\pi2,\frac{3\pi}2\). \(\sin(2\varphi)=-1\) heißt \(2\varphi\in\{\frac{3\pi}2,\frac{7\pi}2\}\), also \(\varphi\in\{\frac{3\pi}4,\frac{7\pi}4\}\).',
   'Lösung Bl. 2, A7a', 'Nullstellen Ableitung sin 2phi Hilfsfunktion Kreislinie')
mc('allg-mc-11', QD, r'Welchen Wert hat \(\sin(\frac\pi6)\)?',
   [r'\(\frac12\)', r'\(\frac12\sqrt3\)', r'\(\frac12\sqrt2\)', r'\(1\)'], 0,
   r'Zum Winkel \(\frac\pi6\) gehört auf der Einheitskreislinie der Punkt \((\frac12\sqrt3,\frac12)\); die \(y\)-Koordinate ist der Sinus.',
   'Bsp. 10.10 (2)', 'sin pi/6 Wert spezielle Werte')
mc('allg-mc-12', QD, r'Welchen Wert hat \(\sin(\frac\pi3)\)?',
   [r'\(\frac12\sqrt3\)', r'\(\frac13\sqrt3\)', r'\(\frac12\)', r'\(\frac12\sqrt2\)'], 0,
   r'Mit \(\sin(\frac\pi2-x)=\cos x\) gilt \(\sin(\frac\pi3)=\sin(\frac\pi2-\frac\pi6)\), und das ist \(\cos(\frac\pi6)=\frac12\sqrt3\).',
   'Bem. 5.9 (3b), Bsp. 10.10 (2)', 'sin pi/3 Wert spezielle Werte', warn=True)
mc('allg-mc-13', QD, r'Welchen Wert hat \(\cos(\frac\pi3)\)?',
   [r'\(\frac12\)', r'\(\frac12\sqrt3\)', r'\(\frac12\sqrt2\)', r'\(0\)'], 0,
   r'Mit \(\cos(\frac\pi2-x)=\sin x\) gilt \(\cos(\frac\pi3)=\cos(\frac\pi2-\frac\pi6)\), und das ist \(\sin(\frac\pi6)=\frac12\).',
   'Bem. 5.9 (3b)', 'cos pi/3 Wert spezielle Werte')
mc('allg-mc-14', QD, r'Welcher Punkt der Einheitskreislinie gehört zu \(\varphi=\frac{3\pi}4\)?',
   [r'\((-\frac12\sqrt2,\ \frac12\sqrt2)\)', r'\((\frac12\sqrt2,\ -\frac12\sqrt2)\)', r'\((-\frac12\sqrt2,\ -\frac12\sqrt2)\)', r'\((-\frac12,\ \frac12\sqrt3)\)'], 0,
   r'\(\frac{3\pi}4\) liegt im 2. Quadranten: \(\cos<0\), \(\sin>0\), beide mit Betrag \(\frac12\sqrt2\). Der Punkt \((\frac12\sqrt2,-\frac12\sqrt2)\) gehört zu \(\frac{7\pi}4\).',
   'Lösung Bl. 2, A7a', 'Einheitskreis 3pi/4 Punkt Quadrant')
mc('allg-mc-15', QD, r'Wo liegen die Nullstellen von \(\cos\)?',
   [r'bei \(k\pi+\frac\pi2\), \(k\in\mathbb Z\)', r'bei \(k\pi\), \(k\in\mathbb Z\)', r'bei \(2k\pi\), \(k\in\mathbb Z\)', r'bei \(\frac{k\pi}2\), \(k\in\mathbb Z\)'], 0,
   r'Die Nullstellen \(k\pi\) gehören zum Sinus. \(\cos\) hat bei \(2k\pi\) sein Maximum \(1\).',
   'Satz 5.10 (2)', 'Nullstellen Cosinus')
mc('allg-mc-16', QD, r'Was ist \(\sin(2x)\)?',
   [r'\(2\sin(x)\cos(x)\)', r'\(\cos^2(x)-\sin^2(x)\)', r'\(2\sin(x)\)', r'\(\sin^2(x)+\cos^2(x)\)'], 0,
   r'Folgt aus \(\sin(x+y)=\sin x\cos y+\cos x\sin y\) mit \(y=x\). \(\cos^2-\sin^2\) ist \(\cos(2x)\).',
   'Bem. 5.9 (2d)', 'sin 2x Doppelwinkel')
mc('allg-mc-17', QD, r'Was ist \(\cos(2x)\)?',
   [r'\(\cos^2(x)-\sin^2(x)\)', r'\(2\sin(x)\cos(x)\)', r'\(\cos^2(x)+\sin^2(x)\)', r'\(2\cos(x)\)'], 0,
   r'Aus \(\cos(x+y)=\cos x\cos y-\sin x\sin y\) mit \(y=x\). \(\cos^2+\sin^2\) ist immer \(1\).',
   'Bem. 5.9 (2d)', 'cos 2x Doppelwinkel')
mc('allg-mc-18', QD, r'Wie lautet das Additionstheorem für \(\sin(x+y)\)?',
   [r'\(\sin x\cos y+\cos x\sin y\)', r'\(\sin x\cos y-\cos x\sin y\)', r'\(\cos x\cos y-\sin x\sin y\)', r'\(\sin x\sin y+\cos x\cos y\)'], 0,
   r'Mit Minuszeichen erhält man \(\sin(x-y)\); \(\cos x\cos y-\sin x\sin y\) ist \(\cos(x+y)\).',
   'Bem. 5.9 (2a)', 'Additionstheorem sin Summe')
mc('allg-mc-19', QD, r'Wie lautet das Additionstheorem für \(\cos(x-y)\)?',
   [r'\(\cos x\cos y+\sin x\sin y\)', r'\(\cos x\cos y-\sin x\sin y\)', r'\(\sin x\cos y-\cos x\sin y\)', r'\(\cos x\sin y+\sin x\cos y\)'], 0,
   r'Beim Cosinus dreht sich das Vorzeichen um: bei \(x-y\) steht ein Plus.',
   'Bem. 5.9 (2b)', 'Additionstheorem cos Differenz')
mc('allg-mc-20', QD, r'Womit lässt sich \(\cos\varphi\cdot\sin\varphi\) ersetzen?',
   [r'\(\frac12\sin(2\varphi)\)', r'\(\sin(2\varphi)\)', r'\(\frac12\cos(2\varphi)\)', r'\(2\sin(2\varphi)\)'], 0,
   r'Wegen \(\sin(2\varphi)=2\sin\varphi\cos\varphi\). So wird z. B. \(\sin(\cos\varphi\sin\varphi)=\sin(\frac{\sin(2\varphi)}2)\).',
   'Bem. 5.9 (2d); Lösung Bl. 4, A13', 'sin cos Produkt Doppelwinkel umformen')
mc('allg-mc-21', QD, r'Was ist \(\sin^2(x)\)?',
   [r'\(\frac12(1-\cos(2x))\)', r'\(\frac12(1+\cos(2x))\)', r'\(1-\cos(2x)\)', r'\(\frac12\sin(2x)\)'], 0,
   r'Mit Plus erhält man \(\cos^2(x)=\frac12(1+\cos(2x))\).',
   'Bem. 5.9 (2e)', 'sin quadrat cos 2x')
mc('allg-mc-22', QD, r'Wie lautet die <b>Quotientenregel</b>?',
   [r"\(\bigl(\frac fg\bigr)'=\frac{f'g-fg'}{g^2}\)", r"\(\bigl(\frac fg\bigr)'=\frac{fg'-f'g}{g^2}\)", r"\(\bigl(\frac fg\bigr)'=\frac{f'}{g'}\)", r"\(\bigl(\frac fg\bigr)'=\frac{f'g+fg'}{g^2}\)"], 0,
   r"Im Zähler zuerst \(f'g\), dann minus \(fg'\); Nenner \(g^2\), Voraussetzung \(g\ne0\).",
   'Satz 6.5 (1)', 'Quotientenregel Ableitung')
mc('allg-mc-23', QD, r'Wie lautet die <b>Kettenregel</b>?',
   [r"\((f\circ g)'(a)=f'(g(a))\cdot g'(a)\)", r"\((f\circ g)'(a)=f'(a)\cdot g'(a)\)", r"\((f\circ g)'(a)=f'(g'(a))\)", r"\((f\circ g)'(a)=f(g'(a))\cdot g'(a)\)"], 0,
   r'Äußere Ableitung an der inneren Stelle mal innere Ableitung.',
   'Satz 6.5 (2)', 'Kettenregel Ableitung Verkettung')
mc('allg-mc-24', QD, r'Was ist die Ableitung von \(e^{\sin(x)}\)?',
   [r'\(e^{\sin(x)}\cdot\cos(x)\)', r'\(e^{\cos(x)}\)', r'\(e^{\sin(x)}\)', r'\(\cos(x)\cdot e^{x}\)'], 0,
   r"Kettenregel: \((e^{g(x)})'=e^{g(x)}\cdot g'(x)\) mit \(g=\sin\).",
   'Bsp. 6.6 (4b)', 'Ableitung e hoch sin Kettenregel')
mc('allg-mc-25', QD, r'Was ist die Ableitung von \(\ln|x|\) für \(x\ne0\)?',
   [r'\(\frac1x\)', r'\(\frac1{|x|}\)', r'\(-\frac1x\)', r'\(\ln(x)\)'], 0,
   r"Für \(x<0\) ist \((\ln(-x))'=\frac1{-x}\cdot(-1)=\frac1x\). Allgemein \((\ln|g|)'=\frac{g'}g\).",
   'Bsp. 6.8 (2)', 'Ableitung ln Betrag Logarithmus', warn=True)
mc('allg-mc-26', QD, r'Wie ist \(a^x\) für \(a>0\) definiert?',
   [r'\(\exp(x\cdot\ln a)\)', r'\(\exp(a\cdot\ln x)\)', r'\(x\cdot\ln a\)', r'\(\ln(a)^x\)'], 0,
   r'Allgemeine Potenz (Def. 5.6). Damit lässt sich jede Potenz mit variablem Exponenten als e-Funktion schreiben.',
   'Def. 5.6 (2)', 'allgemeine Potenz Definition exp ln')
mc('allg-mc-27', QD, r'Was ist \(\partial_{x_2}\) von \(k(x_1,x_2)=(x_1^2+1)^{-x_2}\)?',
   [r'\(-(x_1^2+1)^{-x_2}\cdot\ln(x_1^2+1)\)', r'\(-x_2\,(x_1^2+1)^{-x_2-1}\)', r'\(-2x_1x_2\,(x_1^2+1)^{-x_2-1}\)', r'\((x_1^2+1)^{-x_2}\)'], 0,
   r'Umschreiben: \(k=e^{-x_2\ln(x_1^2+1)}\), Kettenregel nach \(x_2\). Die Potenzregel gilt nur für die Basis; \(-2x_1x_2(x_1^2+1)^{-x_2-1}\) ist \(\partial_{x_1}k\).',
   'Lösung Bl. 3, A9d', 'Variable im Exponenten partielle Ableitung exp ln', warn=True)
mc('allg-mc-28', Q, r"Unter welcher Voraussetzung darf man \(\lim\frac{f}{g}=\lim\frac{f'}{g'}\) (de l’Hospital) schreiben?",
   [r"Fall „\(\frac00\)“ oder \(g\to\pm\infty\), \(g'\ne0\), und \(\lim\frac{f'}{g'}\) existiert", r'immer, wenn \(\lim\frac fg\) existiert', r'nur im Fall „\(\frac00\)“, sonst nie', r'wenn \(f\) und \(g\) stetig sind'], 0,
   r'Entscheidend ist die Existenz des Grenzwerts der Ableitungen; daraus folgt die Existenz von \(\lim\frac fg\), nicht umgekehrt.',
   'Satz 6.17', 'de l Hospital Voraussetzungen')
mc('allg-mc-29', Q, r'Was ergibt \(\displaystyle\lim_{r\to0}\frac{2-2\cos r-r^2}{r^4}\)?',
   [r'\(-\frac1{12}\)', r'\(\frac1{12}\)', r'\(0\)', r'\(-\frac1{24}\)'], 0,
   r'Viermal de l’Hospital, jedes Mal „\(\frac00\)“. Nacheinander entstehen \(\frac{2\sin r-2r}{4r^3}\), \(\frac{2\cos r-2}{12r^2}\), \(\frac{-2\sin r}{24r}\) und \(\frac{-2\cos r}{24}\), was gegen \(-\frac1{12}\) geht.',
   'Lösung Bl. 3, A10a', 'de l Hospital Grenzwert cos mehrfach')
mc('allg-mc-30', Q, r'Was ergibt \(\displaystyle\lim_{x\to+\infty}\frac{\ln x}{\sqrt x}\)?',
   [r'\(0\)', r'\(1\)', r'\(+\infty\)', r'\(\frac12\)'], 0,
   r'Fall „\(\frac\infty\infty\)“: \(\frac{1/x}{1/(2\sqrt x)}=\frac2{\sqrt x}\to0\).',
   'Bsp. 6.18 (1)', 'de l Hospital ln Wurzel unendlich')
mc('allg-mc-31', Q, r'Wann heißt \(f:D_f\to\mathbb R\) <b>injektiv</b>?',
   [r'wenn aus \(x_1\ne x_2\) stets \(f(x_1)\ne f(x_2)\) folgt', r'wenn es zu jedem \(y\in\mathbb R\) ein \(x\) mit \(f(x)=y\) gibt', r'wenn \(f\) stetig ist', r'wenn \(f(x_1)=f(x_2)\) für alle \(x_1,x_2\) gilt'], 0,
   r'Verschiedene Stellen haben verschiedene Werte. Die zweite Aussage beschreibt Surjektivität (\(W_f=\mathbb R\)).',
   'Def. 4.16 (1)', 'injektiv Definition umkehrbar')
mc('allg-mc-32', Q, r'Warum ist eine stetige Funktion auf der Einheitskreislinie <b>nicht surjektiv</b>?',
   [r'Nach Weierstraß nimmt sie Minimum und Maximum an, also \(W_f\subseteq[\min,\max]\subsetneq\mathbb R\)', r'weil die Kreislinie nicht zusammenhängend ist', r'weil jede stetige Funktion beschränkt ist', r'nach dem Zwischenwertsatz'], 0,
   r'Die Kreislinie ist kompakt. Der Zwischenwertsatz wird für die Nicht-Injektivität gebraucht. Nicht jede stetige Funktion ist beschränkt (z. B. auf \(\mathbb R\)).',
   'Lösung Bl. 2, A8', 'surjektiv Kreislinie Weierstraß')
mc('allg-mc-33', Q, r'Wie zeigt man, dass \(f(x)=x+\ln x\) auf \(\mathbb R^+\) <b>surjektiv</b> ist?',
   [r'Grenzwerte \(-\infty\) für \(x\to0+\) und \(+\infty\) für \(x\to+\infty\), dann Zwischenwertsatz', r'über die strenge Monotonie', r'über den Satz von Weierstraß', r"über \(f'(x)>0\)"], 0,
   r"Strenge Monotonie (bzw. \(f'>0\)) liefert nur Injektivität. Für jeden Wert \(y\) gibt es \(a,b\) mit \(f(a)\le y\le f(b)\), und der Zwischenwertsatz liefert \(\xi\) mit \(f(\xi)=y\).",
   'Bsp. 6.8 (5)', 'surjektiv Zwischenwertsatz Grenzwert bijektiv')
mc('allg-mc-34', Q, r'\(f(x,y)=(x+y)e^{xy}\) hat keine kritischen Punkte. Wo liegen seine globalen Extremstellen auf \(K=\{x^2+y^2\le2\}\)?',
   [r'auf dem Rand \(x^2+y^2=2\)', r'im Ursprung', r'es gibt keine', r'im Innern von \(K\)'], 0,
   r'\(K\) ist kompakt und \(f\) stetig, also gibt es Extremstellen (Weierstraß). Im Innern müssten es kritische Punkte sein, also liegen sie auf dem Rand: Maximum \(2e\) in \((1,1)\), Minimum \(-2e\) in \((-1,-1)\).',
   'Lösung Bl. 4, A14', 'keine kritischen Punkte Rand Extremstellen')

# ------------------------------------------------------------ Richtig / Falsch
tf('allg-tf-01', Q, r'Jede abgeschlossene Teilmenge des \(\mathbb R^n\) ist kompakt.', False,
   r'Kompakt heißt abgeschlossen <b>und</b> beschränkt. \(\mathbb R^2\) ist abgeschlossen, aber nicht beschränkt.', 'Def. 9.17 (5); Bsp. 10.10 (3)', 'kompakt abgeschlossen beschränkt')
tf('allg-tf-02', Q, r'Die Menge \([0,1]\cup[2,3]\subseteq\mathbb R\) ist kompakt.', True,
   r'Endliche Vereinigungen abgeschlossener Intervalle sind kompakt.', 'Def. 9.17 (5)', 'kompakt Intervall Vereinigung')
tf('allg-tf-03', Q, r'Der Rand eines abgeschlossenen Rechtecks \([a_1,b_1]\times[a_2,b_2]\) ist kompakt.', True,
   r'Im Skript ausdrücklich genannt: Rechtecksfläche und ihr Rand sind kompakt.', 'Def. 9.17 (5)', 'kompakt Rand Rechteck')
tf('allg-tf-04', Q, r'Für eine stetige Funktion auf einer nichtleeren kompakten Menge ist auch die Wertemenge kompakt.', True,
   r'Satz von Weierstraß, Teil a).', 'Bem. 10.9 (2a)', 'Weierstraß Wertemenge kompakt')
tf('allg-tf-05', Q, r'Ist \(D\) kompakt und zusammenhängend und \(f\) stetig, so ist \(W_f\) ein abgeschlossenes Intervall.', True,
   r'Dann gilt \(W_f=[f(p),f(q)]\) mit Minimal- und Maximalstelle \(p,q\).', 'Bem. 10.9 (2c)', 'Weierstraß zusammenhängend Wertebereich Intervall')
tf('allg-tf-06', Q, r'\((r\cos\varphi,\ r\sin\varphi)\) mit <b>festem</b> \(r>0\) und \(\varphi\in[0,2\pi]\) beschreibt eine Kreisscheibe.', False,
   r'Bei festem \(r\) erhält man nur die Kreislinie. Für die Scheibe muss auch \(r\in[0,R]\) laufen.', 'Bsp. 9.6 (2), 10.4 (4)', 'Polarkoordinaten Kreislinie Kreisscheibe', warn=True)
tf('allg-tf-07', QD, r'Die Sinusfunktion ist gerade.', False,
   r'\(\sin(-x)=-\sin(x)\): Sinus ist ungerade, Cosinus ist gerade.', 'Bem. 5.9 (1)', 'Sinus ungerade gerade Symmetrie')
tf('allg-tf-08', QD, r'Für alle \(x\in\mathbb R\) gilt \(\sin^2(x)+\cos^2(x)=1\).', True,
   r'Folgt aus den Additionstheoremen. Im Einheitskreis: \((\cos\varphi,\sin\varphi)\) hat Abstand \(1\) vom Ursprung.', 'Bem. 5.9 (2c)', 'trigonometrischer Pythagoras sin cos quadrat')
tf('allg-tf-09', QD, r'Sinus und Cosinus sind \(\pi\)-periodisch.', False,
   r'Sie sind \(2\pi\)-periodisch; es gilt \(\sin(x+\pi)=-\sin(x)\). \(\pi\)-periodisch sind Tangens und Cotangens.', 'Satz 5.10, 5.11', 'Periode periodisch Sinus Cosinus Tangens')
tf('allg-tf-10', QD, r'Für alle \(x\) gilt \(\sin(\frac\pi2-x)=\cos(x)\).', True,
   r'Ebenso \(\cos(\frac\pi2-x)=\sin(x)\). Damit folgen z. B. die Werte bei \(\frac\pi3\) aus denen bei \(\frac\pi6\).', 'Bem. 5.9 (3b)', 'Verschiebung pi halbe sin cos')
tf('allg-tf-11', QD, r'Für alle \(x\) gilt \(\cos(x+\pi)=\cos(x)\).', False,
   r'Richtig ist \(\cos(x+\pi)=-\cos(x)\). Erst nach \(2\pi\) wiederholen sich die Werte.', 'Bem. 5.9 (3b)', 'Verschiebung pi cos Vorzeichen')
tf('allg-tf-12', QD, r'Der Wertebereich von \(\sin\) ist \([-1,1]\).', True,
   r'Maximum \(1\) in \(2k\pi+\frac\pi2\), Minimum \(-1\) in \(2k\pi-\frac\pi2\).', 'Satz 5.10 (1)', 'Wertebereich Sinus')
tf('allg-tf-13', QD, r'Jede stetige Funktion ist differenzierbar.', False,
   r'Gegenbeispiel: \(|x|\) ist überall stetig, aber in \(0\) nicht differenzierbar. Umgekehrt ist jede differenzierbare Funktion stetig.', 'Satz 6.4 (1)', 'stetig differenzierbar Betrag Gegenbeispiel')
tf('allg-tf-14', QD, r'Die Ableitung von \(\tan(x)\) ist \(1+\tan^2(x)\).', True,
   r'Quotientenregel: \(\frac{\cos^2x+\sin^2x}{\cos^2x}=1+\tan^2x=\frac1{\cos^2x}\).', 'Bsp. 6.6 (3)', 'Ableitung Tangens Quotientenregel')
tf('allg-tf-15', Q, r"Existiert \(\lim\frac{f}{g}\), so existiert nach de l’Hospital auch \(\lim\frac{f'}{g'}\).", False,
   r"Die Regel geht nur in die andere Richtung: Aus der Existenz von \(\lim\frac{f'}{g'}\) folgt die von \(\lim\frac fg\).", 'Satz 6.17', 'de l Hospital Richtung Existenz', warn=True)
tf('allg-tf-16', Q, r'Jede streng monotone Funktion ist injektiv.', True,
   r'Aus \(x_1<x_2\) folgt \(f(x_1)<f(x_2)\) (bzw. \(>\)), also \(f(x_1)\ne f(x_2)\). Die Umkehrfunktion ist ebenfalls streng monoton.', 'Satz 4.17', 'streng monoton injektiv Umkehrfunktion')
tf('allg-tf-17', Q, r'Es gibt eine stetige injektive Funktion auf der Einheitskreislinie mit Werten in \(\mathbb R\).', False,
   r'Mit dem Zwischenwertsatz findet man oberhalb und unterhalb der \(x\)-Achse je einen Punkt mit demselben Wert (Staatsexamen F14).', 'Lösung Bl. 2, A8', 'Kreislinie injektiv stetig Zwischenwertsatz')
tf('allg-tf-18', Q, r'Hat eine partiell differenzierbare Funktion keine kritischen Punkte, so liegen ihre globalen Extremstellen auf einer kompakten Menge auf dem Rand.', True,
   r'Innere Extremstellen müssten kritische Punkte sein (Satz 10.13); nach Weierstraß gibt es aber Extremstellen.', 'Lösung Bl. 4, A14b', 'kritische Punkte Rand Extremstellen')
tf('allg-tf-19', QD, r'Die Ableitung von \(\ln|x|\) ist \(\frac1{|x|}\).', False,
   r'Richtig ist \(\frac1x\) für alle \(x\ne0\), auch für negative \(x\).', 'Bsp. 6.8 (2)', 'Ableitung ln Betrag', warn=True)

# ------------------------------------------------------------ Lückentext (nur Wörter als Antwort)
gap('allg-gap-01', Q, r'Eine Teilmenge des \(\mathbb R^n\) heißt kompakt, wenn sie {{beschränkt}} und {{abgeschlossen}} ist.',
    r'Beispiele: abgeschlossene Kreisscheibe, Kreislinie, abgeschlossenes Rechteck.', 'Def. 9.17 (5)', 'kompakt beschränkt abgeschlossen')
gap('allg-gap-02', Q, r'Bei festem Radius beschreibt \((r\cos\varphi,\ r\sin\varphi)\) mit \(\varphi\in[0,2\pi]\) eine {{Kreislinie|Kreis|Kreisrand}}; lässt man auch den Radius laufen, eine {{Kreisscheibe}}.',
    r'Für die Scheibe: \(r\in[0,R]\), \(\varphi\in[0,2\pi]\).', 'Bsp. 9.6 (2), 10.4 (4)', 'Polarkoordinaten Kreislinie Kreisscheibe')
gap('allg-gap-03', Q, r'Den Rand eines Dreiecks untersucht man, indem man jede {{Seite|Dreiecksseite|Strecke|Kante}} einzeln parametrisiert und die zugehörige {{Hilfsfunktion}} untersucht.',
    r'Kandidaten je Seite: Eckpunkte und Nullstellen der Ableitung im Innern.', 'Lösung Bl. 2, A7b', 'Rand Dreieck Seiten Hilfsfunktion')
gap('allg-gap-04', Q, r'Bei einer differenzierbaren Hilfsfunktion auf einem abgeschlossenen Intervall prüft man die Nullstellen der Ableitung und die {{Randpunkte|Intervallgrenzen|Ränder}}; zum Vergleich stellt man eine {{Wertetabelle}} auf.',
    r'Extrema können auch an den Intervallgrenzen liegen.', 'Bsp. 10.10 (2)', 'Hilfsfunktion Randpunkte Wertetabelle')
gap('allg-gap-05', QD, r'Die Sinusfunktion ist {{ungerade}}, die Cosinusfunktion ist {{gerade}}.',
    r'\(\sin(-x)=-\sin x\), \(\cos(-x)=\cos x\).', 'Bem. 5.9 (1)', 'Sinus Cosinus gerade ungerade')
gap('allg-gap-06', QD, r'Die Formeln für \(\sin(x+y)\) und \(\cos(x+y)\) heißen {{Additionstheoreme|Additionstheorem}}.',
    r'\(\sin(x+y)=\sin x\cos y+\cos x\sin y\), \(\cos(x+y)=\cos x\cos y-\sin x\sin y\).', 'Bem. 5.9 (2)', 'Additionstheoreme Name')
gap('allg-gap-07', QD, r'Für die Ableitung eines Produkts verwendet man die {{Produktregel}}, für die Ableitung einer Verkettung die {{Kettenregel}}.',
    r"\((fg)'=f'g+fg'\), \((f\circ g)'=f'(g)\cdot g'\).", 'Satz 6.5', 'Produktregel Kettenregel')
gap('allg-gap-08', QD, r'Steht die Variable im Exponenten, schreibt man die Potenz zum Ableiten als {{Exponentialfunktion|e-Funktion|exp}} mit dem {{Logarithmus|natürlichen Logarithmus|ln}} im Exponenten.',
    r'\(a^x=\exp(x\ln a)\), dann Kettenregel.', 'Def. 5.6 (2); Lösung Bl. 3, A9d', 'allgemeine Potenz umschreiben exp ln')
gap('allg-gap-09', Q, r"Liegt beim Grenzwert eines Quotienten der Fall „\(\frac00\)“ vor, hilft oft die Regel von {{de l’Hospital|de l'Hospital|l’Hospital|l'Hospital|Hospital|de l Hospital}}.",
    r'Voraussetzung: Der Grenzwert der Ableitungsquotienten existiert.', 'Satz 6.17', 'de l Hospital Name')
gap('allg-gap-10', Q, r'Nach dem {{Zwischenwertsatz}} nimmt eine stetige Funktion auf \([a,b]\) jeden Wert zwischen \(f(a)\) und \(f(b)\) an.',
    r'Spezialfall Nullstellensatz: Vorzeichenwechsel ⇒ Nullstelle.', 'Satz 4.13', 'Zwischenwertsatz Name')
gap('allg-gap-11', Q, r'Eine Funktion, bei der verschiedene Stellen stets verschiedene Funktionswerte haben, heißt {{injektiv}}; gilt \(W_f=\mathbb R\), heißt sie {{surjektiv}}.',
    r'Injektive Funktionen sind umkehrbar.', 'Def. 4.16', 'injektiv surjektiv Begriffe')
gap('allg-gap-12', Q, r'Hat \(f\) keine {{kritischen Punkte|kritischen Stellen|kritische Punkte}} im Innern, liegen die globalen Extremstellen auf dem {{Rand}}.',
    r'Vorausgesetzt, \(f\) ist stetig, partiell differenzierbar und \(D\) kompakt.', 'Lösung Bl. 4, A14b', 'kritische Punkte Rand')

# ------------------------------------------------------------ Einheitskreis und Graphen (mit Zeichnung)
def _pt(k, n):
    return r'\(\left(%s,\ %s\right)\)' % (_val('cos', k, n), _val('sin', k, n))
def _val(f, k, n):
    from fractions import Fraction
    a = Fraction(k, n) % 2  # in Vielfachen von pi
    base = {Fraction(0): (0, 1), Fraction(1, 6): (r'\frac12', r'\frac12\sqrt3'), Fraction(1, 4): (r'\frac12\sqrt2', r'\frac12\sqrt2'),
            Fraction(1, 3): (r'\frac12\sqrt3', r'\frac12'), Fraction(1, 2): (1, 0)}
    # Referenzwinkel und Vorzeichen
    if a <= Fraction(1, 2): r, sc, ss = a, 1, 1
    elif a <= 1: r, sc, ss = 1 - a, -1, 1
    elif a <= Fraction(3, 2): r, sc, ss = a - 1, -1, -1
    else: r, sc, ss = 2 - a, 1, -1
    sv, cv = base[r]
    v, sg = (sv, ss) if f == 'sin' else (cv, sc)
    if v == 0: return '0'
    v = str(v)
    return ('-' if sg < 0 else '') + v

KQ = [((2, 3), 'zweiten'), ((5, 6), 'zweiten'), ((5, 4), 'dritten'), ((4, 3), 'dritten'), ((7, 6), 'dritten'), ((5, 3), 'vierten'), ((11, 6), 'vierten')]
def _neg(v): return v[1:] if v.startswith('-') else ('0' if v == '0' else '-' + v)
def _fr(k, n):  # Winkel als TeX-Bruch
    a = _lab(k, n).replace('π', r'\pi').split('/')
    return a[0] if len(a) == 1 else r'\frac{%s}{%s}' % (a[0], a[1])
def _ref(k, n):  # Referenzwinkel im 1. Quadranten
    from fractions import Fraction
    a = Fraction(k, n) % 1
    a = min(a, 1 - a)
    return _fr(a.numerator, a.denominator)
for i, ((k, n), qd) in enumerate(KQ):
    c_, s_ = _val('cos', k, n), _val('sin', k, n)
    P2 = lambda x, y: r'\(\left(%s,\ %s\right)\)' % (x, y)
    other = {(2, 3): (3, 4), (5, 6): (2, 3), (5, 4): (4, 3), (4, 3): (5, 4), (7, 6): (5, 4), (5, 3): (7, 4), (11, 6): (7, 4)}[(k, n)]
    opts = []
    for o in (P2(c_, s_), P2(s_, c_), P2(_neg(c_), s_), P2(c_, _neg(s_)), _pt(*other)):
        if o not in opts: opts.append(o)
    opts = opts[:4]; assert len(opts) == 4
    mc('allg-mc-%02d' % (35 + i), QD, r'Am Einheitskreis ist der Punkt zum Winkel \(\varphi=%s\) markiert. Welche Koordinaten hat er?' % _fr(k, n) + kreis(mark=(k, n), label='Einheitskreis, Punkt markiert'),
       opts, 0,
       r'Der Punkt ist \((\cos\varphi,\ \sin\varphi)\) und liegt im %s Quadranten: Beträge wie beim Referenzwinkel \(%s\), Vorzeichen nach Quadrant.' % (qd, _ref(k, n)),
       'Bem. 5.9; Einheitskreis', 'Einheitskreis Koordinaten ' + _lab(k, n) + ' Quadrant')

# Winkel ablesen
for i, ((k, n), wrong) in enumerate([((3, 4), [(2, 3), (5, 6), (5, 4)]), ((5, 3), [(11, 6), (4, 3), (7, 4)]), ((7, 6), [(5, 6), (4, 3), (11, 6)])]):
    fr = lambda kk, nn: r'\(%s\)' % _fr(kk, nn)
    mc('allg-mc-%02d' % (42 + i), QD, r'Der markierte Punkt hat die Koordinaten %s. Zu welchem Winkel \(\varphi\in[0,2\pi[\) gehört er?' % _pt(k, n) + kreis(mark=(k, n), label='Einheitskreis, Punkt markiert'),
       [fr(k, n)] + [fr(*w) for w in wrong], 0,
       r'Am Vorzeichen der Koordinaten liest man den Quadranten ab, an den Beträgen den Referenzwinkel. Probe: \(\cos\varphi\) und \(\sin\varphi\) ergeben genau die Koordinaten.',
       'Bem. 5.9; Einheitskreis', 'Winkel ablesen Einheitskreis Koordinaten')

# Werte in anderen Quadranten
for i, (f, k, n) in enumerate([('sin', 5, 6), ('cos', 2, 3), ('sin', 4, 3), ('cos', 7, 4), ('sin', 11, 6), ('cos', 5, 4), ('sin', 3, 2)]):
    r = _val(f, k, n)
    pool = ['0', '1', '-1', r'\frac12', r'-\frac12', r'\frac12\sqrt2', r'-\frac12\sqrt2', r'\frac12\sqrt3', r'-\frac12\sqrt3']
    neg = r[1:] if r.startswith('-') else ('-' + r if r != '0' else '1')
    other = _val('cos' if f == 'sin' else 'sin', k, n)
    cand = [r, neg, other] + [p for p in pool if p not in (r, neg, other)]
    opts = []
    for c in cand:
        if c not in opts: opts.append(c)
    opts = opts[:4]
    mc('allg-mc-%02d' % (45 + i), QD, r'Welchen Wert hat \(\%s\!\left(%s\right)\)?' % (f, _fr(k, n)),
       [r'\(%s\)' % o for o in opts], 0,
       r'Am Einheitskreis gehört zum Winkel \(%s\) der Punkt %s; \(\cos\) ist die \(x\)-, \(\sin\) die \(y\)-Koordinate.' % (_fr(k, n), _pt(k, n)),
       'Bem. 5.9; Einheitskreis', '%s Wert %s Einheitskreis' % (f, _lab(k, n)))

# Graphen erkennen
_opts4 = [r'\(\cos x\)', r'\(\sin x\)', r'\(-\cos x\)', r'\(-\sin x\)']
mc('allg-mc-52', QD, r'Welche Funktion ist hier auf \([-\frac\pi2,\,2\pi]\) dargestellt?' + graph([('cos', 'k-q')], legend=False, label='Graph einer Funktion'),
   _opts4, 0,
   r'Der Graph beginnt bei \(x=0\) mit dem Wert \(1\), hat Nullstellen bei \(\pm\frac\pi2\) und \(\frac{3\pi}2\) und das Minimum \(-1\) bei \(\pi\): das ist \(\cos\).',
   'Satz 5.10', 'Graph erkennen Cosinus Kurve')
mc('allg-mc-53', QD, r'Welche Funktion ist hier auf \([-\frac\pi2,\,2\pi]\) dargestellt?' + graph([('sin', 'k-q')], legend=False, label='Graph einer Funktion'),
   [_opts4[1], _opts4[0], _opts4[3], _opts4[2]], 0,
   r'Der Graph geht durch den Ursprung und steigt dort, Maximum \(1\) bei \(\frac\pi2\), Minimum \(-1\) bei \(\frac{3\pi}2\): das ist \(\sin\).',
   'Satz 5.10', 'Graph erkennen Sinus Kurve')
mc('allg-mc-54', QD, r'Abgebildet ist \(\cos\) auf \([0,2\pi]\). Wo liegen seine Nullstellen in diesem Bereich?' + graph([('cos', 'k-cos')], x0=0, legend=False, label='Graph von cos'),
   [r'\(\frac\pi2\) und \(\frac{3\pi}2\)', r'\(0\), \(\pi\) und \(2\pi\)', r'\(\pi\)', r'\(\frac\pi4\) und \(\frac{5\pi}4\)'], 0,
   r'Nullstellen von \(\cos\): \(k\pi+\frac\pi2\). \(0,\pi,2\pi\) sind die Nullstellen von \(\sin\).',
   'Satz 5.10 (2)', 'Nullstellen Cosinus Graph')
mc('allg-mc-55', QD, r'Abgebildet ist \(\sin\). An welcher Stelle liegt der markierte Punkt (Minimum)?' + graph([('sin', 'k-sin')], x0=0, mark=(3 * pi / 2, -1), legend=False, label='Graph von sin mit markiertem Minimum'),
   [r'\(x=\frac{3\pi}2\)', r'\(x=\pi\)', r'\(x=\frac{5\pi}4\)', r'\(x=2\pi\)'], 0,
   r'\(\sin\) hat das Minimum \(-1\) bei \(2k\pi-\frac\pi2\), im Bereich \([0,2\pi]\) also bei \(\frac{3\pi}2\).',
   'Satz 5.10 (1)', 'Minimum Sinus Graph')
mc('allg-mc-56', QD, r'Abgebildet ist \(\cos\). Welchen Wert hat die Funktion am markierten Punkt bei \(x=\frac\pi3\)?' + graph([('cos', 'k-cos')], x0=0, mark=(pi / 3, 0.5), legend=False, label='Graph von cos mit markiertem Punkt'),
   [r'\(\frac12\)', r'\(\frac12\sqrt3\)', r'\(\frac12\sqrt2\)', r'\(\frac13\)'], 0,
   r'\(\cos(\frac\pi3)=\frac12\); der Punkt liegt genau auf halber Höhe zwischen \(0\) und \(1\).',
   'Bem. 5.9 (3b)', 'cos pi/3 Graph Wert')

tf('allg-tf-20', QD, r'Die abgebildete Funktion ist ungerade.' + graph([('cos', 'k-q')], legend=False, label='Graph einer Funktion'), False,
   r'Abgebildet ist \(\cos\). Der Graph ist achsensymmetrisch zur \(y\)-Achse, also ist die Funktion <b>gerade</b>: \(\cos(-x)=\cos x\).',
   'Bem. 5.9 (1)', 'gerade ungerade Graph Cosinus Symmetrie')
tf('allg-tf-21', QD, r'Der abgebildete Graph ist punktsymmetrisch zum Ursprung.' + graph([('sin', 'k-q')], legend=False, label='Graph einer Funktion'), True,
   r'Abgebildet ist \(\sin\); wegen \(\sin(-x)=-\sin x\) ist der Graph punktsymmetrisch zum Ursprung.',
   'Bem. 5.9 (1)', 'punktsymmetrisch Sinus Graph ungerade')
tf('allg-tf-22', QD, r'Die beiden markierten Punkte zu \(\varphi=\frac\pi6\) und \(\varphi=\frac{5\pi}6\) haben denselben Sinuswert.' + kreis(extra=[(1, 6), (5, 6)], label='Einheitskreis mit zwei Punkten'), True,
   r'Sie liegen spiegelbildlich zur \(y\)-Achse, also gleiche \(y\)-Koordinate \(\frac12\); die \(x\)-Koordinaten \(\pm\frac12\sqrt3\) unterscheiden sich im Vorzeichen.',
   'Bem. 5.9; Einheitskreis', 'Einheitskreis Symmetrie Sinus gleich pi minus phi')
tf('allg-tf-23', QD, r'Für jeden Winkel \(\varphi\) im dritten Quadranten sind \(\sin\varphi\) und \(\cos\varphi\) beide negativ.', True,
   r'Im dritten Quadranten (\(\pi<\varphi<\frac{3\pi}2\)) liegt der Punkt \((\cos\varphi,\sin\varphi)\) links unten.',
   'Einheitskreis', 'Quadrant Vorzeichen negativ')
gap('allg-gap-13', QD, r'Am Einheitskreis ist die \(x\)-Koordinate des Punktes zum Winkel \(\varphi\) der {{Cosinus|cos|Kosinus}} von \(\varphi\), die \(y\)-Koordinate der {{Sinus|sin}}.',
    r'Punkt \((\cos\varphi,\ \sin\varphi)\).', 'Bsp. 9.6 (2), 10.4 (4)', 'Einheitskreis Koordinaten Sinus Cosinus')
gap('allg-gap-14', QD, r'Der Graph des Cosinus ist {{achsensymmetrisch|spiegelsymmetrisch|symmetrisch}} zur \(y\)-Achse, der Graph des Sinus ist {{punktsymmetrisch}} zum Ursprung.',
    r'\(\cos\) ist gerade, \(\sin\) ist ungerade.', 'Bem. 5.9 (1)', 'Symmetrie Graph Sinus Cosinus')

# ============================================================ Diff 1: Punkte 12–24 (Übungs-Know-how, v47)
# Quellen: Kurzskript Diff 1 (Kap. 1–2), Übungsblätter Diff 1 (Bl. 1–6) mit Lösungen 1–3; für 15/24 auch Kap. 1 und 3 (Vorjahr).
# Grunddefinitionen (Grenzwert, Hauptsatz monotone Folgen, e, Beschränktheit) stehen schon in Diff 1 Kap. 1/2 – hier nur Techniken.

CARDS += [
    # ------------------------------------------------ 12 Vollständige Induktion
    C('induktion', D, 'Diff 1, Lösung Bl. 1, A1, A3',
      r"Wie ist ein Beweis durch <b>vollständige Induktion</b> aufgebaut?",
      r'''<ol><li><b>Induktionsanfang:</b> Aussage für den kleinsten Index prüfen (z. B. \(n=0\) oder \(n=1\)).</li>
<li><b>Induktionsvoraussetzung:</b> Die Aussage gelte für ein \(n\).</li>
<li><b>Induktionsschluss</b> „\(n\to n+1\)“: Aus der Voraussetzung die Aussage für \(n+1\) folgern.</li></ol>
<p><b>Beispiel</b> (Lösung Bl. 1, A1): \(a_0=3\), \(a_{n+1}=\frac{a_n^2+4}{2a_n}\). Behauptung \(a_n\ge2\).</p>
<p>Anfang: \(a_0=3\ge2\). Schluss: Aus \(a_n\ge2\) folgt \(a_n>0\) und</p>
\[\begin{aligned}a_{n+1}-2&=\dfrac{a_n^2-4a_n+4}{2a_n}\\&=\dfrac{(a_n-2)^2}{2a_n}\ge0.\end{aligned}\]''',
      'vollständige Induktion Induktionsanfang Induktionsvoraussetzung Induktionsschluss Beweis rekursiv'),

    C('induktion-produkt', D, 'Diff 1, Lösung Bl. 2, A3',
      r"Wie führt man bei einem <b>Produkt</b> oder einer <b>Summe</b> den Induktionsschluss von \(n\) auf \(n+1\) durch?",
      r'''<p>Den <b>letzten Faktor</b> (bzw. Summanden) abspalten, dann die Induktionsvoraussetzung einsetzen und vereinfachen.</p>
<p><b>Beispiel</b> (Lösung Bl. 2, A3): Behauptung \(\prod_{k=2}^{n}\bigl(1-\frac{2}{k(k+1)}\bigr)=\frac13\bigl(1+\frac2n\bigr)\).</p>
<p>Abspalten: Produkt bis \(n+1\) = (Produkt bis \(n\)) \(\cdot\bigl(1-\frac{2}{(n+1)(n+2)}\bigr)\).</p>
<p>Voraussetzung einsetzen und vereinfachen:</p>
\[\begin{aligned}&\tfrac13\bigl(1+\tfrac2n\bigr)\bigl(1-\tfrac{2}{(n+1)(n+2)}\bigr)\\&=\tfrac13\bigl(1+\tfrac{2}{n+1}\bigr).\end{aligned}\]
<p>Danach: \(x_n\to\frac13(1+0)=\frac13\).</p>''',
      'Induktion Produkt Summe letzter Faktor abspalten Induktionsschluss'),

    # ------------------------------------------------ 13 Ungleichungen
    C('ungleichungen', D, 'Diff 1, Lösung Bl. 1, A3; Lösung Bl. 2, A1; Lösung Bl. 3, A4',
      r"Welche Regeln gelten beim <b>Rechnen mit Ungleichungen</b>?",
      r'''<ul><li><b>Addition</b> einer Zahl: Zeichen bleibt.</li>
<li><b>Multiplikation</b> mit einer <b>positiven</b> Zahl: Zeichen bleibt; mit einer <b>negativen</b> Zahl: Zeichen <b>dreht sich um</b>.</li>
<li><b>Wurzel</b> ziehen bei \(0\le x\le y\): \(\sqrt x\le\sqrt y\).</li>
<li><b>Quadrieren</b> nur bei positiven Zahlen: \(0<x<y\Rightarrow x^2<y^2\).</li>
<li><b>Kehrwert</b> bei positiven Zahlen dreht um: \(n+2<n+3\Rightarrow\frac3{n+2}>\frac3{n+3}\).</li></ul>
<p><b>Beispiel</b> (Lösung Bl. 1, A3a), Schluss von \(1\le a_n\le5\) auf \(a_{n+1}=5-\sqrt{11-2a_n}\):</p>
\[\begin{aligned}&1\le a_n\le5\\&\Rightarrow-2\ge-2a_n\ge-10\\&\Rightarrow9\ge11-2a_n\ge1\\&\Rightarrow3\ge\sqrt{11-2a_n}\ge1\\&\Rightarrow-3\le-\sqrt{11-2a_n}\le-1\\&\Rightarrow2\le a_{n+1}\le4.\end{aligned}\]''',
      'Ungleichungen Rechenregeln negativ umdrehen Wurzel Quadrieren Kehrwert monoton Abschätzung'),

    # ------------------------------------------------ 14 epsilon-n0
    C('epsilon-n0', D, 'Diff 1, Lösung Bl. 1, A2; Lösung Bl. 2, A2',
      r"Wie zeigt man Konvergenz <b>direkt mit der Definition</b> (\(\varepsilon\)-\(n_0\)-Nachweis)?",
      r'''<ol><li>\(|x_n-a|\) auf einen Bruch bringen und vereinfachen.</li>
<li>Nach oben abschätzen bis \(\le\frac Cn\): <b>Zähler vergrößern, Nenner verkleinern</b> (Nenner bleibt positiv).</li>
<li>\(n_0>\frac C\varepsilon\) wählen; so ein \(n_0\) gibt es nach dem <b>Archimedischen Axiom</b>.</li>
<li>Für \(n\ge n_0\): \(|x_n-a|\le\frac Cn\le\frac C{n_0}<\varepsilon\).</li></ol>
<p>Die Wahl von \(n_0\) ergibt sich erst aus der Abschätzung; im Aufschrieb steht sie trotzdem am Anfang.</p>
<p><b>Beispiel</b> (Lösung Bl. 1, A2): \(x_n=\frac{6n+1}{2n-1}\), \(a=3\):</p>
\[\begin{aligned}|x_n-3|&=\dfrac{4}{2n-1}\le\dfrac{4}{2n-n}\\&=\dfrac4n\le\dfrac4{n_0}<\varepsilon\end{aligned}\]
<p>mit \(n_0>\frac4\varepsilon\).</p>''',
      'epsilon n0 Nachweis Definition Konvergenz Abschätzung Archimedisches Axiom Zähler Nenner'),

    # ------------------------------------------------ 15 Dreiecksungleichung (beide Fächer)
    C('dreiecksungleichung', QD, 'Kap. 1, Bem. 1.1 d), e); Diff 1 Kurzskript, Bem. 1.0.8; Diff 1, Lösung Bl. 1, A4; Lösung Bl. 2, A1',
      r"Wie lauten die <b>Dreiecksungleichung</b> und die <b>umgekehrte</b> Dreiecksungleichung, und wofür braucht man sie?",
      r'''<p>Für alle \(x,y\in\mathbb R\):</p>
\[|x+y|\le|x|+|y|,\]\[\bigl||x|-|y|\bigr|\le|x\pm y|.\]
<p><b>Beschränktheit</b> zeigen (Lösung Bl. 2, A1):</p>
\[\left|1+\tfrac{(-1)^n}{n}+\tfrac1{n^2}\right|\le1+\tfrac1n+\tfrac1{n^2}\le3.\]
<p><b>Summen</b> beschränkter Folgen (Lösung Bl. 1, A4a): \(|x_n+y_n|\le|x_n|+|y_n|\le C_1+C_2\).</p>
<p><b>Betrag einer Folge</b> (Kurzskript Bem. 1.0.8): Aus \(0\le\bigl||a_n|-|a|\bigr|\le|a_n-a|\) folgt \(a_n\to a\Rightarrow|a_n|\to|a|\). Die Umkehrung gilt nur für \(a=0\); Gegenbeispiel \(a_n=(-1)^n\).</p>''',
      'Dreiecksungleichung umgekehrte Betrag Abschätzung beschränkt Summe'),

    # ------------------------------------------------ 16 Höchste Potenz ausklammern
    C('hoechste-potenz', D, 'Diff 1, Lösung Bl. 2, A1; Lösung Bl. 3, A1a; Kurzskript Satz 1.0.4',
      r"Wie bestimmt man den Grenzwert eines <b>Bruchs aus Polynomen in \(n\)</b>?",
      r'''<ol><li>In Zähler und Nenner die <b>höchste Potenz</b> von \(n\) ausklammern und kürzen.</li>
<li>\(\frac1{n^k}\to0\) und die <b>Grenzwertsätze</b> anwenden (Grenzwert des Nenners \(\neq0\)).</li></ol>
<p><b>Beispiel</b> (Lösung Bl. 2, A1): \(\frac{2n+1}{n+2}=\frac{2+\frac1n}{1+\frac2n}\to\frac{2+0}{1+0}=2\).</p>
<p><b>Beispiel</b> (Lösung Bl. 3, A1a): ausmultipliziert</p>
\[\frac{(2n^2+3)^3}{(3n^3+2)^2}=\frac{8+\frac{36}{n^2}+\frac{54}{n^4}+\frac{27}{n^6}}{9+\frac{12}{n^3}+\frac4{n^6}}\to\frac89.\]''' + H(r'Ohne Ausmultiplizieren geht es schneller: \((2n^2+3)^3=n^6\bigl(2+\frac3{n^2}\bigr)^3\) und \((3n^3+2)^2=n^6\bigl(3+\frac2{n^3}\bigr)^2\), also Grenzwert \(\frac{2^3}{3^2}=\frac89\).'),
      'höchste Potenz ausklammern Grenzwertsätze Polynom Bruch Grenzwert berechnen'),

    # ------------------------------------------------ 18 (1+1/n)^n
    C('euler-anwenden', D, 'Diff 1, Lösung Bl. 3, A1b; Kurzskript Bem. 2.0.3',
      r"Wie nutzt man \(\bigl(1+\frac1n\bigr)^n\to e\) beim Berechnen von Grenzwerten?",
      r'''<p>Den Ausdruck so umformen, dass \(\bigl(1+\frac1n\bigr)^n\) als <b>Faktor</b> auftaucht; den Rest mit den Grenzwertsätzen behandeln. Nützlich: \(\frac{(n+1)^n}{n^n}=\bigl(\frac{n+1}n\bigr)^n=\bigl(1+\frac1n\bigr)^n\) und \(n^{n+1}=n\cdot n^n\).</p>
<p><b>Beispiel</b> (Lösung Bl. 3, A1b):</p>
\[\begin{aligned}y_n&=\frac{(2n^2+1)(n+1)^n}{(3n+1)\,n^{n+1}}\\&=\frac{2+\frac1{n^2}}{3+\frac1n}\cdot\left(1+\frac1n\right)^n\to\frac23\,e.\end{aligned}\]
<p>Die Folge \(\bigl(1+\frac1n\bigr)^n\) ist monoton wachsend und nach oben beschränkt.</p>''',
      'Eulersche Zahl e Grenzwert umformen Faktor (1+1/n)^n Produkt'),

    # ------------------------------------------------ 19 Rekursive Folgen
    C('rekursiv-grenzwert', D, 'Diff 1, Lösung Bl. 1, A3; Lösung Bl. 3, A3; Kurzskript Satz 1.0.3, 2.0.1',
      r"Wie zeigt man, dass eine <b>rekursive Folge</b> konvergiert, und wie bestimmt man ihren Grenzwert?",
      r'''<ol><li><b>Monotonie</b> und <b>Beschränktheit</b> zeigen (meist mit Induktion).</li>
<li>Hauptsatz über monotone Folgen ⇒ \((a_n)\) konvergiert gegen ein \(a\).</li>
<li>Schranken übertragen sich: \(1\le a_n\le5\Rightarrow1\le a\le5\).</li>
<li>In der Rekursion \(n\to\infty\): \(a=\lim a_{n+1}=f(a)\). Gleichung lösen.</li>
<li>Die Lösung wählen, die zu den <b>Schranken</b> passt.</li></ol>
<p><b>Beispiel</b> (Lösung Bl. 3, A3): \(a_1=\frac72\), \(a_{n+1}=5-\sqrt{11-2a_n}\), monoton fallend, \(a_n\in[1,5]\):</p>
\[\begin{aligned}&a=5-\sqrt{11-2a}\\&\Rightarrow a^2-8a+14=0\\&\Rightarrow a=4\pm\sqrt2.\end{aligned}\]
<p>Da \(4+\sqrt2>5\), ist \(a=4-\sqrt2\approx2{,}59\).</p>''',
      'rekursive Folge Grenzwert Fixpunkt monoton beschränkt konvergent Gleichung Lösung wählen'),

    C('rekursiv-divergenz', D, 'Diff 1, Lösung Bl. 3, A4',
      r"Was folgt, wenn <b>keine Lösung</b> der Grenzwertgleichung \(a=f(a)\) zu den Schranken der rekursiven Folge passt?",
      r'''<p>Dann kann die Folge <b>nicht konvergieren</b> (Widerspruchsbeweis).</p>
<p><b>Beispiel</b> (Lösung Bl. 3, A4): \(x_0=4\), \(x_{n+1}=\frac14x_n^2+\frac34\). Mit Induktion: \(0<x_n<x_{n+1}\), also \(x_n\ge x_0=4\).</p>
<p>Annahme \(x_n\to a\). Dann \(a\ge4\) und \(a=\frac14a^2+\frac34\), also \(a^2-4a+3=(a-1)(a-3)=0\), d. h. \(a=1\) oder \(a=3\). Widerspruch zu \(a\ge4\) ⇒ \((x_n)\) divergiert.</p>''',
      'rekursive Folge divergent Widerspruch Grenzwertgleichung keine passende Lösung Startwert'),

    # ------------------------------------------------ 21 Monotonie nachweisen
    C('monotonie-nachweis', D, 'Diff 1, Lösung Bl. 1, A1, A3b; Lösung Bl. 2, A1',
      r"Wie weist man die <b>Monotonie</b> einer Folge nach?",
      r'''<ul><li><b>Differenz:</b> \(a_{n+1}-a_n\le0\) ⇒ monoton fallend (\(\ge0\) ⇒ wachsend).</li>
<li><b>Quotient</b>, nur wenn alle \(a_n>0\): \(\frac{a_{n+1}}{a_n}\le1\) ⇒ monoton fallend (\(\ge1\) ⇒ wachsend).</li>
<li><b>Umformen:</b> \(a_n=\frac{2n+1}{n+2}=2-\frac3{n+2}\) ist streng monoton wachsend.</li>
<li>Bei rekursiven Folgen oft mit <b>Induktion</b>: \(a_n\ge a_{n+1}\Rightarrow a_{n+1}\ge a_{n+2}\).</li>
<li><b>Nicht monoton:</b> drei Glieder genügen, z. B. \(b_1=1<\frac74=b_2\) und \(b_2>\frac79=b_3\).</li></ul>
<p><b>Beispiel</b> (Lösung Bl. 1, A1) mit \(a_n\ge2\):</p>
\[a_{n+1}-a_n=\frac{4-a_n^2}{2a_n}\le0,\]\[\frac{a_{n+1}}{a_n}=\frac12+\frac2{a_n^2}\le1.\]''',
      'Monotonie nachweisen Differenz Quotient monoton wachsend fallend Induktion nicht monoton'),

    # ------------------------------------------------ 23 Beschränktheit
    C('beschraenktheit-zeigen', D, 'Diff 1, Lösung Bl. 2, A1; Kurzskript Satz 1.0.2, Bem. 1.0.4',
      r"Auf welchen Wegen zeigt man, dass eine Folge <b>beschränkt</b> ist?",
      r'''<ul><li><b>Direkt abschätzen</b>, z. B. \(0\le\frac{2n+1}{n+2}\le\frac{2n+2}{n+1}=2\), oder mit der Dreiecksungleichung.</li>
<li>Über <b>Konvergenz</b>: Konvergiert die Folge, ist sie beschränkt (Satz 1.0.2). Etwa \(\frac{2n+1}{n+2}\to2\), also beschränkt.</li>
<li>Über <b>Monotonie</b>: Monoton wachsend ⇒ \(a_1\) ist untere Schranke; monoton fallend ⇒ \(a_1\) ist obere Schranke.</li></ul>
<p>Umgekehrt: Ist eine Folge <b>unbeschränkt</b>, so ist sie divergent.</p>''',
      'beschränkt zeigen Beschränktheit Schranke konvergent abschätzen monoton'),

    # ------------------------------------------------ 24 Reihen (beide Fächer)
    C('geometrische-summe', QD, 'Diff 1, Bl. 4 (Hinweis zu A1); Kap. 3, Satz 3.4 (2)',
      r"Wie lauten die <b>geometrische Summenformel</b> und das Konvergenzverhalten der <b>geometrischen Reihe</b>?",
      r'''<p>Für \(q\in\mathbb R\), \(q\neq1\):</p>
\[\sum_{i=0}^{n}q^i=\frac{1-q^{n+1}}{1-q}.\]
<p>Die geometrische Reihe \(\sum_{n=0}^\infty q^n\) konvergiert <b>genau dann</b>, wenn \(|q|<1\); dann gilt</p>
\[\sum_{n=0}^{\infty}q^n=\frac1{1-q}.\]
<p>Grund: \(q^{n+1}\to0\) für \(|q|<1\). Für \(|q|\ge1\) ist \((q^n)\) keine Nullfolge.</p>''',
      'geometrische Summe Summenformel geometrische Reihe q Konvergenz Reihenwert'),

    C('teleskopsumme', QD, 'Kap. 3, Bem. 3.1, Bsp. 3.3 (3); Diff 1, Bl. 5 (Hinweis zu A2)',
      r"Was ist eine <b>Teleskopsumme</b>, und wie hilft sie bei Reihen?",
      r'''<p>In einer Summe aus Differenzen heben sich alle inneren Glieder auf:</p>
\[\begin{aligned}&(x_n-x_{n-1})+(x_{n-1}-x_{n-2})\\&+\dots+(x_{m+1}-x_m)\\&=x_n-x_m.\end{aligned}\]
<p>So lassen sich Partialsummen oft direkt ausrechnen. Mit der Dreiecksungleichung folgt außerdem (Bl. 5, Hinweis zu A2):</p>
\[\begin{aligned}|x_n-x_m|&\le|x_n-x_{n-1}|\\&+\dots+|x_{m+1}-x_m|.\end{aligned}\]
<p><b>Beispiel</b> (Kap. 3, Bem. 3.1): \(\sum_{k=1}^{n}\frac1{k(k+1)}=\frac n{n+1}\to1\), also \(\sum_{n=1}^\infty\frac1{n(n+1)}=1\).</p>''' + H(r'Mit \(\frac1{k(k+1)}=\frac1k-\frac1{k+1}\) ist das eine Teleskopsumme: \(s_n=1-\frac1{n+1}\). Im Skript wird die Formel per Induktion gezeigt.'),
      'Teleskopsumme Partialsumme Differenzen heben sich auf Reihe 1/(n(n+1))'),

    C('harmonische-reihe', QD, 'Kap. 3, Satz 3.4 (1), Bsp. 3.7 (2), (3), Bem. 3.10; Diff 1, Bl. 5, A2',
      r"Was gilt für die <b>harmonische Reihe</b> \(\sum\frac1n\), und was hat das mit Nullfolgen zu tun?",
      r'''<ul><li>\(\sum_{n=1}^\infty\frac1n\) <b>divergiert</b>, obwohl \(\frac1n\to0\).</li>
<li>Allgemein: Ist \(\sum a_n\) konvergent, so ist \((a_n)\) eine Nullfolge. Die <b>Umkehrung gilt nicht</b> – die harmonische Reihe ist das Gegenbeispiel.</li>
<li>Ist \((a_n)\) keine Nullfolge, divergiert \(\sum a_n\).</li>
<li>\(\sum_{n=1}^\infty\frac1{n^p}\) mit \(p\ge2\) <b>konvergiert</b>.</li>
<li>Die alternierende harmonische Reihe \(\sum\frac{(-1)^{n-1}}n\) <b>konvergiert</b>.</li></ul>''',
      'harmonische Reihe divergent Nullfolge notwendig Umkehrung 1/n 1/n^2 alternierend'),
]

# ------------------------------------------------------------ Diff 1 Punkte 12–24: Multiple Choice
mc('allg-mc-57', D, r'Was zeigt man bei einer vollständigen Induktion im <b>Induktionsschluss</b> „\(n\to n+1\)“?',
   [r'Gilt die Aussage für ein \(n\), so gilt sie auch für \(n+1\)', r'Die Aussage gilt für den kleinsten Index', r'Gilt die Aussage für \(n+1\), so gilt sie auch für \(n\)', r'Die Aussage gilt für unendlich viele \(n\)'], 0,
   r'Der Anfang sichert den kleinsten Index, der Schluss überträgt die Aussage von \(n\) auf \(n+1\). Zusammen folgt sie für alle \(n\).',
   'Diff 1, Lösung Bl. 1, A1', 'Induktion Induktionsschluss')
mc('allg-mc-58', D, r'Für \(a_0=3\), \(a_{n+1}=\frac{a_n^2+4}{2a_n}\) soll \(a_{n+1}\ge2\) aus \(a_n\ge2\) folgen. Welche Umformung trägt den Beweis?',
   [r'\(a_{n+1}-2=\frac{(a_n-2)^2}{2a_n}\)', r'\(a_{n+1}-2=\frac{a_n^2-4}{2a_n}\)', r'\(a_{n+1}-2=\frac{4-a_n^2}{2a_n}\)', r'\(a_{n+1}-2=\frac{a_n-2}{2}\)'], 0,
   r'\(\frac{a_n^2+4}{2a_n}-2=\frac{a_n^2-4a_n+4}{2a_n}=\frac{(a_n-2)^2}{2a_n}\ge0\), da \(a_n>0\). \(\frac{4-a_n^2}{2a_n}\) ist dagegen \(a_{n+1}-a_n\) (Monotonie).',
   'Diff 1, Lösung Bl. 1, A1', 'Induktion rekursiv Umformung binomisch')
mc('allg-mc-59', D, r'Behauptung: \(\prod_{k=2}^{n}\bigl(1-\frac{2}{k(k+1)}\bigr)=\frac13\bigl(1+\frac2n\bigr)\). Wie beginnt man den Induktionsschluss?',
   [r'Den letzten Faktor abspalten und für das restliche Produkt die Induktionsvoraussetzung einsetzen', r'Alle Faktoren ausmultiplizieren', r'Den Grenzwert \(n\to\infty\) bilden', r'\(n=2\) einsetzen'], 0,
   r'\(\prod_{k=2}^{n+1}=\bigl(\prod_{k=2}^{n}\bigr)\cdot\bigl(1-\frac2{(n+1)(n+2)}\bigr)\); das Produkt bis \(n\) ersetzt man durch \(\frac13(1+\frac2n)\).',
   'Diff 1, Lösung Bl. 2, A3', 'Induktion Produkt letzter Faktor')
mc('allg-mc-60', D, r'Es gilt \(1\le a_n\le5\). Was folgt nach Multiplikation mit \(-2\)?',
   [r'\(-2\ge-2a_n\ge-10\)', r'\(-2\le-2a_n\le-10\)', r'\(2\le-2a_n\le10\)', r'\(-10\ge-2a_n\ge-2\)'], 0,
   r'Multiplikation mit einer negativen Zahl dreht beide Ungleichheitszeichen um.',
   'Diff 1, Lösung Bl. 1, A3a', 'Ungleichung negativ multiplizieren umdrehen', warn=True)
mc('allg-mc-61', D, r'Unter welcher Voraussetzung folgt aus \(x<y\) sicher \(x^2<y^2\)?',
   [r'\(0<x<y\)', r'immer', r'\(x<y<0\)', r'\(x<0<y\)'], 0,
   r'Quadrieren ist nur für positive Zahlen monoton. Gegenbeispiel: \(-3<1\), aber \(9>1\).',
   'Diff 1, Lösung Bl. 3, A4', 'Ungleichung quadrieren positiv')
mc('allg-mc-62', D, r'Es ist \(n+2<n+3\). Was folgt für \(\frac3{n+2}\) und \(\frac3{n+3}\)?',
   [r'\(\frac3{n+2}>\frac3{n+3}\)', r'\(\frac3{n+2}<\frac3{n+3}\)', r'\(\frac3{n+2}=\frac3{n+3}\)', r'Man kann sie nicht vergleichen'], 0,
   r'Größerer positiver Nenner ⇒ kleinerer Bruch. Daraus folgt, dass \(a_n=2-\frac3{n+2}\) streng monoton wächst.',
   'Diff 1, Lösung Bl. 2, A1', 'Ungleichung Kehrwert Nenner Bruch')
mc('allg-mc-63', D, r'Für \(x_n=\frac{6n+1}{2n-1}\) ist \(|x_n-3|=\frac4{2n-1}\). Welche Abschätzung ist richtig und führt zum Ziel?',
   [r'\(\frac4{2n-1}\le\frac4{2n-n}=\frac4n\)', r'\(\frac4{2n-1}\le\frac4{2n}\)', r'\(\frac4{2n-1}\le\frac4{2n+1}\)', r'\(\frac4{2n-1}=\frac4n\)'], 0,
   r'Wegen \(1\le n\) ist \(2n-1\ge2n-n=n\); kleinerer Nenner ⇒ größerer Bruch. \(\frac4{2n}\) und \(\frac4{2n+1}\) sind dagegen kleiner als \(\frac4{2n-1}\).',
   'Diff 1, Lösung Bl. 1, A2', 'epsilon n0 Abschätzung Nenner verkleinern', warn=True)
mc('allg-mc-64', D, r'Es ist gezeigt: \(|x_n-a|\le\frac4n\) für alle \(n\). Wie wählt man \(n_0\) zu gegebenem \(\varepsilon>0\)?',
   [r'\(n_0>\frac4\varepsilon\)', r'\(n_0>\frac\varepsilon4\)', r'\(n_0>4\varepsilon\)', r'\(n_0=4\)'], 0,
   r'Dann gilt für \(n\ge n_0\): \(\frac4n\le\frac4{n_0}<\varepsilon\). Ein solches \(n_0\) gibt es nach dem Archimedischen Axiom.',
   'Diff 1, Lösung Bl. 1, A2', 'epsilon n0 wählen Archimedes')
mc('allg-mc-65', D, r'Man will einen Bruch mit positivem Nenner für einen \(\varepsilon\)-\(n_0\)-Nachweis <b>nach oben</b> abschätzen. Was ist erlaubt?',
   [r'Zähler vergrößern und Nenner verkleinern (Nenner bleibt positiv)', r'Zähler verkleinern und Nenner vergrößern', r'Zähler und Nenner beide vergrößern', r'Zähler und Nenner beide verkleinern'], 0,
   r'Beides macht den Bruch größer, z. B. \(\frac{3(n-1)}{n^2+n-1}\le\frac{3n}{n^2+n-n}=\frac3n\) (Lösung Bl. 2, A2).',
   'Diff 1, Lösung Bl. 2, A2', 'Abschätzung Zähler vergrößern Nenner verkleinern')
mc('allg-mc-66', QD, r'Welche Ungleichung ist die <b>umgekehrte</b> Dreiecksungleichung?',
   [r'\(\bigl||x|-|y|\bigr|\le|x-y|\)', r'\(|x+y|\le|x|+|y|\)', r'\(|x-y|\le\bigl||x|-|y|\bigr|\)', r'\(|x\cdot y|\le|x|+|y|\)'], 0,
   r'Sie gilt für alle reellen \(x,y\), auch mit \(|x+y|\) rechts. \(|x+y|\le|x|+|y|\) ist die gewöhnliche Dreiecksungleichung.',
   'Kap. 1, Bem. 1.1 e); Diff 1 Kurzskript, Bem. 1.0.8', 'umgekehrte Dreiecksungleichung Betrag')
mc('allg-mc-67', D, r'Wie zeigt man mit der Dreiecksungleichung, dass \(b_n=1+\frac{(-1)^n}n+\frac1{n^2}\) beschränkt ist?',
   [r'\(|b_n|\le1+\frac1n+\frac1{n^2}\le3\)', r'\(|b_n|=1+\frac1n+\frac1{n^2}\)', r'\(|b_n|\le\frac1n\)', r'\(|b_n|\le1\)'], 0,
   r'\(\bigl|\frac{(-1)^n}n\bigr|=\frac1n\le1\) und \(\frac1{n^2}\le1\). Gleichheit gilt nicht immer: Für ungerades \(n\) ist der mittlere Summand negativ.',
   'Diff 1, Lösung Bl. 2, A1', 'Dreiecksungleichung beschränkt Abschätzung')
mc('allg-mc-68', D, r'Wie lautet \(\displaystyle\lim_{n\to\infty}\frac{(2n^2+3)^3}{(3n^3+2)^2}\)?',
   [r'\(\frac89\)', r'\(\frac23\)', r'\(\frac49\)', r'\(0\)'], 0,
   r'Zähler und Nenner haben die höchste Potenz \(n^6\); nach Ausklammern bleibt \(\frac{2^3}{3^2}=\frac89\).',
   'Diff 1, Lösung Bl. 3, A1a', 'höchste Potenz ausklammern Grenzwert Bruch')
mc('allg-mc-69', D, r'Wie geht man bei \(\displaystyle\lim_{n\to\infty}\frac{2n+1}{n+2}\) vor?',
   [r'\(n\) in Zähler und Nenner ausklammern: \(\frac{2+\frac1n}{1+\frac2n}\to2\)', r'Zähler und Nenner gehen gegen \(\infty\), also ist der Grenzwert \(1\)', r'Nur den Zähler durch \(n\) teilen: \(2+\frac1n\to2\)', r'Der Grenzwert existiert nicht, weil der Zähler unbeschränkt ist'], 0,
   r'„\(\frac\infty\infty\)“ ist kein Ergebnis. Erst nach dem Ausklammern sind Zähler und Nenner konvergent mit Nennergrenzwert \(\neq0\), dann greifen die Grenzwertsätze.',
   'Diff 1, Lösung Bl. 2, A1', 'höchste Potenz ausklammern Grenzwertsätze unendlich durch unendlich', warn=True)
mc('allg-mc-70', D, r'Wogegen konvergiert \(y_n=\frac{2+\frac1{n^2}}{3+\frac1n}\cdot\bigl(1+\frac1n\bigr)^n\)?',
   [r'\(\frac23\,e\)', r'\(\frac23\)', r'\(e\)', r'\(\frac32\,e\)'], 0,
   r'Erster Faktor \(\to\frac23\), zweiter \(\to e\); Produkt konvergenter Folgen.',
   'Diff 1, Lösung Bl. 3, A1b', 'Eulersche Zahl e Produkt Grenzwert')
mc('allg-mc-71', D, r'Womit stimmt \(\frac{(n+1)^n}{n^n}\) überein?',
   [r'\(\bigl(1+\frac1n\bigr)^n\)', r'\(1+\frac1n\)', r'\(\bigl(1+\frac1n\bigr)^{n+1}\)', r'\(n+1\)'], 0,
   r'\(\frac{(n+1)^n}{n^n}=\bigl(\frac{n+1}n\bigr)^n=\bigl(1+\frac1n\bigr)^n\to e\).',
   'Diff 1, Lösung Bl. 3, A1b', 'Eulersche Zahl umformen Potenz')
mc('allg-mc-72', D, r'\(a_1=\frac72\), \(a_{n+1}=5-\sqrt{11-2a_n}\) konvergiert, und \(a_n\in[1,5]\). Aus \(a=5-\sqrt{11-2a}\) folgt \(a=4\pm\sqrt2\). Welcher ist der Grenzwert?',
   [r'\(4-\sqrt2\), weil \(4+\sqrt2>5\)', r'\(4+\sqrt2\), weil die Folge fällt', r'beide', r'keiner, die Folge divergiert'], 0,
   r'Der Grenzwert liegt wie alle Folgeglieder in \([1,5]\). \(4+\sqrt2\approx5{,}41\) liegt außerhalb.',
   'Diff 1, Lösung Bl. 3, A3', 'rekursive Folge Grenzwert Lösung wählen Schranken')
mc('allg-mc-73', D, r'\(x_0=4\), \(x_{n+1}=\frac14x_n^2+\frac34\) ist wachsend mit \(x_n\ge4\). Die Gleichung \(a=\frac14a^2+\frac34\) hat die Lösungen \(1\) und \(3\). Was folgt?',
   [r'Die Folge divergiert, denn ein Grenzwert müsste \(\ge4\) sein', r'Die Folge konvergiert gegen \(3\)', r'Die Folge konvergiert gegen \(1\)', r'Die Folge konvergiert gegen \(4\)'], 0,
   r'Widerspruchsbeweis: Angenommen \(x_n\to a\). Dann \(a\ge4\) und \(a\in\{1,3\}\) – unmöglich.',
   'Diff 1, Lösung Bl. 3, A4', 'rekursive Folge divergent Widerspruch', warn=True)
mc('allg-mc-74', D, r'Wann darf man aus \(\frac{a_{n+1}}{a_n}\le1\) für alle \(n\) schließen, dass \((a_n)\) monoton fallend ist?',
   [r'Wenn alle \(a_n>0\) sind', r'Immer', r'Wenn alle \(a_n<0\) sind', r'Wenn \((a_n)\) beschränkt ist'], 0,
   r'Nur bei positiven Gliedern darf man mit \(a_n\) multiplizieren, ohne dass sich das Zeichen dreht: \(a_{n+1}\le a_n\).',
   'Diff 1, Lösung Bl. 1, A1', 'Monotonie Quotient positiv')
mc('allg-mc-75', D, r'Es ist \(a_n=\frac{2n+1}{n+2}=2-\frac3{n+2}\). Welches Monotonieverhalten hat \((a_n)\)?',
   [r'streng monoton wachsend', r'streng monoton fallend', r'nicht monoton', r'konstant'], 0,
   r'\(\frac3{n+2}\) wird kleiner, also wird \(2-\frac3{n+2}\) größer.',
   'Diff 1, Lösung Bl. 2, A1', 'Monotonie umformen wachsend')
mc('allg-mc-76', D, r'Für \(b_n=1+\frac{(-1)^n}n+\frac1{n^2}\) ist \(b_1=1\), \(b_2=\frac74\), \(b_3=\frac79\). Was folgt?',
   [r'\((b_n)\) ist weder monoton wachsend noch monoton fallend', r'\((b_n)\) ist monoton wachsend', r'\((b_n)\) ist monoton fallend', r'Ohne alle Glieder lässt sich nichts sagen'], 0,
   r'\(b_1<b_2\) schließt „fallend“ aus, \(b_2>b_3\) schließt „wachsend“ aus. Für „nicht monoton“ genügen solche Gegenbeispiele.',
   'Diff 1, Lösung Bl. 2, A1', 'nicht monoton Gegenbeispiel Folgeglieder')
mc('allg-mc-77', D, r'Wie lässt sich die Beschränktheit von \(a_n=\frac{2n+1}{n+2}\) <b>ohne</b> direkte Abschätzung begründen?',
   [r'\(a_n\to2\); konvergente Folgen sind beschränkt', r'\((a_n)\) ist monoton wachsend, also beschränkt', r'Zähler und Nenner sind beschränkt', r'\(a_1=1\) ist eine obere Schranke'], 0,
   r'Konvergent ⇒ beschränkt. Monoton wachsend liefert nur die untere Schranke \(a_1\); Zähler und Nenner sind unbeschränkt.',
   'Diff 1, Lösung Bl. 2, A1', 'beschränkt konvergent Begründung')
mc('allg-mc-78', QD, r'Wie lautet die geometrische Summenformel \(\sum_{i=0}^{n}q^i\) für \(q\neq1\)?',
   [r'\(\frac{1-q^{n+1}}{1-q}\)', r'\(\frac{1-q^{n}}{1-q}\)', r'\(\frac1{1-q}\)', r'\(\frac{q^{n+1}-1}{1-q}\)'], 0,
   r'Die Summe hat \(n+1\) Glieder, daher der Exponent \(n+1\). \(\frac1{1-q}\) ist der Wert der unendlichen Reihe für \(|q|<1\).',
   'Diff 1, Bl. 4 (Hinweis zu A1)', 'geometrische Summenformel', warn=True)
mc('allg-mc-79', QD, r'Für welche \(q\in\mathbb R\) konvergiert die geometrische Reihe \(\sum_{n=0}^\infty q^n\)?',
   [r'genau für \(|q|<1\)', r'genau für \(q<1\)', r'genau für \(|q|\le1\)', r'für alle \(q\neq1\)'], 0,
   r'Für \(|q|\ge1\) ist \((q^n)\) keine Nullfolge, die Reihe divergiert. Zum Beispiel divergiert sie für \(q=-1\) und \(q=-2\).',
   'Kap. 3, Satz 3.4 (2)', 'geometrische Reihe Konvergenz q')
mc('allg-mc-80', QD, r'Welchen Wert hat \(\sum_{n=0}^\infty\bigl(\frac12\bigr)^n\)?',
   [r'\(2\)', r'\(1\)', r'\(\frac12\)', r'Die Reihe divergiert'], 0,
   r'Geometrische Reihe mit \(q=\frac12\): \(\frac1{1-\frac12}=2\).',
   'Kap. 3, Satz 3.4 (2)', 'geometrische Reihe Reihenwert')
mc('allg-mc-81', QD, r'Was gilt für die harmonische Reihe \(\sum_{n=1}^\infty\frac1n\)?',
   [r'Sie divergiert, obwohl \(\frac1n\) eine Nullfolge ist', r'Sie konvergiert, weil \(\frac1n\) eine Nullfolge ist', r'Sie konvergiert gegen \(1\)', r'Sie divergiert, weil \(\frac1n\) keine Nullfolge ist'], 0,
   r'„Nullfolge“ ist nur notwendig, nicht hinreichend für die Konvergenz einer Reihe.',
   'Kap. 3, Satz 3.4 (1c), Bsp. 3.7 (2)', 'harmonische Reihe divergent Nullfolge', warn=True)
mc('allg-mc-82', QD, r'Welchen Wert hat \(\sum_{n=1}^\infty\frac1{n(n+1)}\)?',
   [r'\(1\)', r'\(\frac12\)', r'\(2\)', r'Die Reihe divergiert'], 0,
   r'Die Partialsummen sind \(s_n=\frac n{n+1}\to1\).',
   'Kap. 3, Bem. 3.1', 'Reihe Teleskopsumme Partialsumme Wert')
mc('allg-mc-83', QD, r'Was ergibt die Teleskopsumme \(\sum_{k=m}^{n-1}(x_{k+1}-x_k)\)?',
   [r'\(x_n-x_m\)', r'\(x_m-x_n\)', r'\(x_{n-1}-x_m\)', r'\(0\)'], 0,
   r'Alle inneren Glieder heben sich weg; übrig bleiben nur \(x_n\) und \(-x_m\).',
   'Kap. 3, Bsp. 3.3 (3b); Diff 1, Bl. 5 (Hinweis zu A2)', 'Teleskopsumme Differenzen')

# ------------------------------------------------------------ Diff 1 Punkte 12–24: Richtig / Falsch
tf('allg-tf-24', D, r'Im Induktionsschluss darf man die Induktionsvoraussetzung (Aussage für \(n\)) benutzen.', True,
   r'Genau das ist der Kern: Man folgert die Aussage für \(n+1\) aus der für \(n\).', 'Diff 1, Lösung Bl. 1, A1', 'Induktion Voraussetzung')
tf('allg-tf-25', D, r'Für einen Induktionsbeweis genügt der Induktionsschluss; den Induktionsanfang kann man weglassen.', False,
   r'Ohne Anfang fehlt der Startpunkt der Kette; der Schluss allein beweist nichts.', 'Diff 1, Lösung Bl. 1, A1', 'Induktion Anfang nötig')
tf('allg-tf-26', D, r'Multipliziert man beide Seiten einer Ungleichung mit einer negativen Zahl, dreht sich das Ungleichheitszeichen um.', True,
   r'Beispiel: \(1\le a_n\le5\Rightarrow-2\ge-2a_n\ge-10\).', 'Diff 1, Lösung Bl. 1, A3', 'Ungleichung negativ umdrehen')
tf('allg-tf-27', D, r'Aus \(a<b\) folgt stets \(a^2<b^2\).', False,
   r'Gegenbeispiel: \(-3<1\), aber \(9>1\). Quadrieren ist nur für \(0<a<b\) erlaubt.', 'Diff 1, Lösung Bl. 3, A4', 'Ungleichung quadrieren', warn=True)
tf('allg-tf-28', D, r'Aus \(0<x<y\) folgt \(\frac1x>\frac1y\).', True,
   r'Bei positiven Zahlen dreht der Kehrwert die Ungleichung um.', 'Diff 1, Lösung Bl. 2, A1', 'Ungleichung Kehrwert')
tf('allg-tf-29', QD, r'Für alle \(x,y\in\mathbb R\) gilt \(|x+y|\le|x|+|y|\).', True,
   r'Dreiecksungleichung.', 'Kap. 1, Bem. 1.1 d)', 'Dreiecksungleichung')
tf('allg-tf-30', QD, r'Für alle \(x,y\in\mathbb R\) gilt \(\bigl||x|-|y|\bigr|\le|x-y|\).', True,
   r'Umgekehrte Dreiecksungleichung; damit folgt etwa aus \(a_n\to a\) auch \(|a_n|\to|a|\).', 'Kap. 1, Bem. 1.1 e); Diff 1 Kurzskript, Bem. 1.0.8', 'umgekehrte Dreiecksungleichung')
tf('allg-tf-31', D, r'Jede Lösung der Gleichung \(a=f(a)\) ist Grenzwert der rekursiven Folge \(a_{n+1}=f(a_n)\).', False,
   r'Man muss die Lösung wählen, die zu den Schranken passt (Lösung Bl. 3, A3: nur \(4-\sqrt2\)); passt keine, divergiert die Folge (A4).', 'Diff 1, Lösung Bl. 3, A3, A4', 'rekursive Folge Fixpunkt Lösung wählen', warn=True)
tf('allg-tf-32', D, r'Gilt \(1\le a_n\le5\) für alle \(n\) und \(a_n\to a\), dann ist auch \(1\le a\le5\).', True,
   r'Nicht-strikte Ungleichungen übertragen sich auf den Grenzwert (Satz 1.0.3).', 'Diff 1 Kurzskript, Satz 1.0.3; Lösung Bl. 3, A3', 'Schranken Grenzwert übertragen')
tf('allg-tf-33', D, r'Ist \(a_{n+1}-a_n\ge0\) für alle \(n\), so ist \((a_n)\) monoton wachsend.', True,
   r'Das ist genau \(a_n\le a_{n+1}\).', 'Diff 1, Lösung Bl. 1, A1', 'Monotonie Differenz')
tf('allg-tf-34', D, r'Aus \(\frac{a_{n+1}}{a_n}\le1\) für alle \(n\) folgt stets \(a_{n+1}\le a_n\).', False,
   r'Nur für positive Glieder. Gegenbeispiel: \(a_n=-2\), \(a_{n+1}=-1\): Quotient \(\frac12\le1\), aber \(a_{n+1}>a_n\).', 'Diff 1, Lösung Bl. 1, A1', 'Monotonie Quotient positiv', warn=True)
tf('allg-tf-35', D, r'Die Folge \(\bigl(1+\frac1n\bigr)^n\) ist monoton wachsend und nach oben beschränkt.', True,
   r'Daher konvergiert sie; ihr Grenzwert ist \(e\).', 'Diff 1, Lösung Bl. 3, A1b', 'Eulersche Zahl monoton beschränkt')
tf('allg-tf-36', D, r'Bei \(\frac{2n+1}{n+2}\) gehen Zähler und Nenner gegen \(\infty\), also ist der Grenzwert \(1\).', False,
   r'„\(\frac\infty\infty\)“ ist kein Ergebnis. Nach Ausklammern: \(\frac{2+\frac1n}{1+\frac2n}\to2\).', 'Diff 1, Lösung Bl. 2, A1', 'Grenzwert Bruch unendlich ausklammern', warn=True)
tf('allg-tf-37', QD, r'Ist die Reihe \(\sum a_n\) konvergent, so ist \((a_n)\) eine Nullfolge.', True,
   r'Notwendige Bedingung für die Konvergenz einer Reihe.', 'Kap. 3, Satz 3.4 (1a)', 'Reihe Nullfolge notwendig')
tf('allg-tf-38', QD, r'Ist \((a_n)\) eine Nullfolge, so konvergiert die Reihe \(\sum a_n\).', False,
   r'Gegenbeispiel: die harmonische Reihe \(\sum\frac1n\) divergiert.', 'Kap. 3, Satz 3.4 (1c), Bsp. 3.7 (2)', 'Reihe Nullfolge nicht hinreichend harmonisch', warn=True)
tf('allg-tf-39', QD, r'Die Reihe \(\sum_{n=1}^\infty\frac1{n^2}\) konvergiert.', True,
   r'\(\sum\frac1{n^p}\) konvergiert für \(p\ge2\); nur für \(p=1\) (harmonische Reihe) divergiert sie.', 'Kap. 3, Bsp. 3.7 (3)', 'Reihe 1/n^2 konvergent')
tf('allg-tf-40', QD, r'Die geometrische Reihe \(\sum_{n=0}^\infty(-1)^n\) konvergiert.', False,
   r'Konvergenz nur für \(|q|<1\); hier ist \(|q|=1\), und \((-1)^n\) ist keine Nullfolge.', 'Kap. 3, Satz 3.4 (2)', 'geometrische Reihe q=-1 divergent')

# ------------------------------------------------------------ Diff 1 Punkte 12–24: Lückentext
gap('allg-gap-15', D, r'Ein Induktionsbeweis besteht aus dem {{Induktionsanfang}} und dem {{Induktionsschluss|Induktionsschritt}}.',
    r'Anfang: kleinster Index; Schluss: von \(n\) auf \(n+1\).', 'Diff 1, Lösung Bl. 1, A1', 'Induktion Anfang Schluss')
gap('allg-gap-16', D, r'Multipliziert man eine Ungleichung mit einer negativen Zahl, {{dreht|kehrt}} sich das Ungleichheitszeichen um.',
    r'\(1\le a_n\le5\Rightarrow-2\ge-2a_n\ge-10\).', 'Diff 1, Lösung Bl. 1, A3', 'Ungleichung negativ umdrehen')
gap('allg-gap-17', D, r'Um einen Bruch nach oben abzuschätzen, {{vergrößert|vergroessert}} man den Zähler und {{verkleinert}} den Nenner.',
    r'Beispiel: \(\frac4{2n-1}\le\frac4{2n-n}=\frac4n\).', 'Diff 1, Lösung Bl. 1, A2', 'Abschätzung Zähler Nenner')
gap('allg-gap-18', QD, r'Die Ungleichung \(|x+y|\le|x|+|y|\) heißt {{Dreiecksungleichung}}.',
    r'Umgekehrt: \(\bigl||x|-|y|\bigr|\le|x\pm y|\).', 'Kap. 1, Bem. 1.1 d)', 'Dreiecksungleichung Name')
gap('allg-gap-19', D, r'Bei Brüchen aus Polynomen in \(n\) klammert man in Zähler und Nenner die {{höchste|hoechste|größte}} Potenz von \(n\) aus und wendet dann die {{Grenzwertsätze|Grenzwertsatz|Rechenregeln}} an.',
    r'Beispiel: \(\frac{2n+1}{n+2}=\frac{2+\frac1n}{1+\frac2n}\to2\).', 'Diff 1, Lösung Bl. 2, A1', 'höchste Potenz ausklammern Grenzwertsätze')
gap('allg-gap-20', D, r'Für die Monotonie untersucht man die {{Differenz}} zweier aufeinanderfolgender Glieder oder, bei positiven Gliedern, ihren {{Quotienten|Quotient}}.',
    r'\(a_{n+1}-a_n\le0\) bzw. \(\frac{a_{n+1}}{a_n}\le1\) ⇒ monoton fallend.', 'Diff 1, Lösung Bl. 1, A1', 'Monotonie Differenz Quotient')
gap('allg-gap-21', D, r'Den Grenzwert einer rekursiven Folge erhält man, indem man ihn in die {{Rekursion|Rekursionsvorschrift|Rekursionsformel}} einsetzt; von den Lösungen wählt man die, die zu den {{Schranken|Schranke}} der Folge passt.',
    r'Beispiel: \(a=4\pm\sqrt2\) mit \(a\in[1,5]\) ⇒ \(a=4-\sqrt2\).', 'Diff 1, Lösung Bl. 3, A3', 'rekursive Folge Grenzwert Schranken')
gap('allg-gap-22', QD, r'Die Reihe \(\sum\frac1n\) heißt {{harmonische|harmonisch}} Reihe; sie ist {{divergent|divergiert}}.',
    r'Obwohl \(\frac1n\to0\).', 'Kap. 3, Bsp. 3.7 (2)', 'harmonische Reihe divergent')
gap('allg-gap-23', QD, r'Eine Reihe ist die Folge ihrer {{Partialsummen|Teilsummen|Partialsumme}}.',
    r'\(s_n=a_1+\dots+a_n\); konvergiert \((s_n)\), heißt der Grenzwert Summe der Reihe.', 'Kap. 3, Def. 3.2', 'Reihe Partialsummen')
gap('allg-gap-24', QD, r'Heben sich in einer Summe aus Differenzen alle inneren Glieder auf, spricht man von einer {{Teleskopsumme}}.',
    r'\((x_n-x_{n-1})+\dots+(x_{m+1}-x_m)=x_n-x_m\).', 'Kap. 3, Bsp. 3.3 (3b); Diff 1, Bl. 5 (Hinweis zu A2)', 'Teleskopsumme Name')


assert len({c['key'] for c in CARDS}) == len(CARDS)
assert len({i['id'] for i in ITEMS}) == len(ITEMS)
for x in CARDS + ITEMS:
    assert x['subj'] and set(x['subj']) <= {'quer', 'diff1'}, x
