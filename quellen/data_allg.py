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

    C('sin-cos-werte', QD, 'Kap. 5, Bem. 5.9 (3b); Kap. 10, Bsp. 10.4 (4), 10.10 (2); Lösung Bl. 2, A7',
      r"Wie lauten \(\sin\) und \(\cos\) an den Stellen \(0,\ \frac\pi6,\ \frac\pi4,\ \frac\pi3,\ \frac\pi2,\ \pi,\ \frac{3\pi}2,\ 2\pi\)?",
      r'''<table><tr><th>\(x\)</th><th>\(\sin x\)</th><th>\(\cos x\)</th></tr>
<tr><td>\(0\)</td><td>\(0\)</td><td>\(1\)</td></tr>
<tr><td>\(\frac\pi6\)</td><td>\(\frac12\)</td><td>\(\frac12\sqrt3\)</td></tr>
<tr><td>\(\frac\pi4\)</td><td>\(\frac12\sqrt2\)</td><td>\(\frac12\sqrt2\)</td></tr>
<tr><td>\(\frac\pi3\)</td><td>\(\frac12\sqrt3\)</td><td>\(\frac12\)</td></tr>
<tr><td>\(\frac\pi2\)</td><td>\(1\)</td><td>\(0\)</td></tr>
<tr><td>\(\pi\)</td><td>\(0\)</td><td>\(-1\)</td></tr>
<tr><td>\(\frac{3\pi}2\)</td><td>\(-1\)</td><td>\(0\)</td></tr>
<tr><td>\(2\pi\)</td><td>\(0\)</td><td>\(1\)</td></tr></table>
<p>\(\frac12\sqrt2=\frac1{\sqrt2}\). Die Werte bei \(\frac\pi3\) folgen aus denen bei \(\frac\pi6\) mit \(\sin(\frac\pi2-x)=\cos x\) und \(\cos(\frac\pi2-x)=\sin x\).</p>
<div class="tip"><b>Merkhilfe am Einheitskreis:</b> Der Punkt zum Winkel \(\varphi\) ist \((\cos\varphi,\sin\varphi)\), z. B. \(\varphi=\frac\pi6\): \((\frac12\sqrt3,\frac12)\); \(\varphi=\frac\pi4\): \((\frac1{\sqrt2},\frac1{\sqrt2})\).</div>''',
      'Sinus Cosinus Werte Tabelle pi/6 pi/4 pi/3 Wurzel 3 Wurzel 2 Einheitskreis spezielle Werte'),

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

assert len({c['key'] for c in CARDS}) == len(CARDS)
assert len({i['id'] for i in ITEMS}) == len(ITEMS)
for x in CARDS + ITEMS:
    assert x['subj'] and set(x['subj']) <= {'quer', 'diff1'}, x
