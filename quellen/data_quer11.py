# Querschnitt · Kapitel 11 – Gewöhnliche Differentialgleichungen erster Ordnung (Teil IV, S. 360–382)
# Quelle: querschnitt-kapitel11.pdf. Nur Inhalte aus dem Skript.
# Formeln als TeX in \( \) bzw. \[ \]; Lücken als {{Antwort|Alternative}}. IDs/Keys nie ändern, nur anhängen.
# Jede Frage muss ohne Skript verständlich sein.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

CARDS = [
    C('modell', 'Bem. 11.1 a)–c)',
      r"Natürliches Wachstum: Welche Größen betrachtet man, welche <b>Modellannahme</b> trifft man und auf welche <b>Differentialgleichung</b> führt sie?",
      r'''<p>Eine Größe \(u\) wird in einem Zeitintervall \(I\subseteq\mathbb R\) beobachtet (z. B. Wachstum einer Bakterienpopulation, Zerfall einer radioaktiven Substanz). Für \(t\in I\) beschreibt</p>
<ul><li>\(u(t)\) den <b>momentanen Wert</b> (etwa Anzahl oder Masse der zum Zeitpunkt \(t\) vorhandenen Bakterien oder Atome),</li>
<li>\(u'(t)\) die <b>momentane Änderungsrate</b> (\(u'(t)\ge0\) beim Bakterienwachstum, \(u'(t)\le0\) beim radioaktiven Zerfall).</li></ul>
<p>Der Zusammenhang zwischen \(t\), \(u(t)\) und \(u'(t)\) hängt vom gewählten Modell ab. <b>Modellannahme „natürliches Wachstum“:</b> \(u(t)\) und \(u'(t)\) sind unabhängig von \(t\) direkt proportional, d. h. es gibt \(\alpha\in\mathbb R\) mit</p>
\[u'(t)=\alpha\cdot u(t)\quad\text{für alle } t\in I.\]
<p><b>Gesucht:</b> eine differenzierbare Funktion \(u:I\to\mathbb R\) auf dem Definitions<i>intervall</i> \(I\subseteq\mathbb R\) mit Wertebereich \(W_u\subseteq\mathbb R^+\), die diese Beziehung zwischen \(u\) und \(u'\) erfüllt, also eine Lösung der Differentialgleichung erster Ordnung</p>
\[u'=\alpha\cdot u\quad\text{mit } t\in I \text{ und } u>0.\]''',
      'natürliches Wachstum Modell Bakterien radioaktiver Zerfall Änderungsrate proportional Wachstumskonstante'),

    C('wachstum-loesungen', 'Bem. 11.1 d)–e)',
      r"Welche Funktionen lösen \(u'=\alpha\cdot u\) mit \(u>0\)? Wie legt ein <b>Anfangswert</b> \(u_0=u(t_0)\) die Lösung fest?",
      r'''<p>Alle Funktionen \(u_c:I\to\mathbb R,\ u_c(t)=c\cdot e^{\alpha t}\) mit \(c>0\), denn für alle \(t\in I\) ist</p>
\[\begin{aligned}u_c'(t)&=c\cdot\left(e^{\alpha t}\cdot\alpha\right)\\ &=\alpha\cdot\left(c\cdot e^{\alpha t}\right)=\alpha\cdot u_c(t).\end{aligned}\]
<p>Die DGL beschreibt nur den <b>grundsätzlichen</b> zeitlichen Verlauf einer Größe mit natürlichem Wachstum (Wachstumskonstante \(\alpha\)) und hat <b>unendlich viele Lösungen</b>. Die Gesamtheit der \(u_c\) mit \(c>0\) sind <b>alle</b> Lösungen von \(u'=\alpha\cdot u\) mit \(u>0\) (wird im Skript gezeigt).</p>
<p><b>Anfangswert:</b> Für den genauen Verlauf muss \(u_0=u(t_0)\) zu einem Zeitpunkt \(t_0\in I\) bekannt sein. Dann ist \(u_0=c\cdot e^{\alpha t_0}\), also \(c=u_0\cdot e^{-\alpha t_0}\), und</p>
\[\begin{aligned}u(t)&=c\cdot e^{\alpha t}=u_0\cdot e^{-\alpha t_0}\cdot e^{\alpha t}\\ &=u_0\cdot e^{\alpha(t-t_0)}\end{aligned}\]<p>für alle \(t\in I\).</p>''',
      'Exponentialfunktion Lösung Anfangswert unendlich viele Lösungen Wachstumskonstante'),

    C('def-dgl', 'Def. 11.2 (1), (2)',
      r"Was ist eine <b>gewöhnliche Differentialgleichung erster Ordnung</b> (explizite Form), und wann heißt \(\varphi\) eine <b>Lösung</b>?",
      r'''<p>Sei \(\emptyset\ne U\subseteq\mathbb R^2\) mit \((x_0,y_0)\in U\) und \(f:U\to\mathbb R\) eine Funktion.</p>
<ol><li>Man bezeichnet \(y'=f(x,y)\) für \((x,y)\in U\) als (gewöhnliche) <b>Differentialgleichung erster Ordnung (in expliziter Form)</b>.</li>
<li>Eine <b>differenzierbare</b> Funktion \(\varphi:D_\varphi\to\mathbb R\) auf dem <b>Definitionsintervall</b> \(D_\varphi\subseteq\mathbb R\) heißt <b>Lösung</b> von \(y'=f(x,y)\), wenn für alle \(x\in D_\varphi\) gilt:</li></ol>
\[(x,\varphi(x))\in U\]<p>mit</p>\[\varphi'(x)=f(x,\varphi(x)).\]
<div class="tip"><b>Zwei Bedingungen:</b> Der Graph liegt in \(U\), und die Gleichung ist an jeder Stelle erfüllt. \(D_\varphi\) muss ein Intervall sein.</div>''',
      'Differentialgleichung erster Ordnung explizit Lösung Definition Definitionsintervall'),

    C('def-maximal', 'Def. 11.2 (3), (4)',
      r"Wann heißt eine Lösung von \(y'=f(x,y)\) <b>maximal</b>? Was ist die <b>allgemeine Lösung</b>?",
      r'''<ul><li><b>Maximal:</b> Eine Lösung \(\varphi:D_\varphi\to\mathbb R\) heißt maximal, wenn es keine <i>echte</i> Fortsetzung \(\widetilde\varphi:D_{\widetilde\varphi}\to\mathbb R\) von \(\varphi\) gibt, die ebenfalls eine Lösung von \(y'=f(x,y)\) ist.</li>
<li><b>Allgemeine Lösung:</b> die <b>Menge aller maximalen Lösungen</b> \(\varphi:D_\varphi\to\mathbb R\) von \(y'=f(x,y)\).</li></ul>''',
      'maximale Lösung Fortsetzung allgemeine Lösung Menge'),

    C('def-awp', 'Def. 11.2 (5)',
      r"Was ist eine Lösung des <b>Anfangswertproblems</b> \(y'=f(x,y)\) mit \(y(x_0)=y_0\)?",
      r'''<p>Eine <b>maximale</b> Lösung \(\varphi:D_\varphi\to\mathbb R\) der Differentialgleichung \(y'=f(x,y)\) mit \(\varphi(x_0)=y_0\).</p>
<p>Andere Bezeichnung: <b>Anfangswertaufgabe</b>.</p>
<div class="tip"><b>Merke:</b> Die Lösung eines Anfangswertproblems ist nach Definition immer eine <i>maximale</i> Lösung.</div>''',
      'Anfangswertproblem Anfangswertaufgabe AWP Anfangsbedingung'),

    C('bsp-wachstum', 'Bsp. 11.3',
      r"Beispiel \((*)\ y'=\alpha\cdot y\) mit \(x\in I\) und \(y>0\): Was sind \(U\) und \(f\), die Lösungen, die maximalen Lösungen, die allgemeine Lösung und die Lösung des Anfangswertproblems?",
      r'''<ol><li>\(U=I\times\mathbb R^+\) mit \(f:U\to\mathbb R,\ f(x,y)=\alpha\cdot y\).</li>
<li>Für jedes \(c\in\mathbb R^+\) ist \(\varphi_c:I\to\mathbb R,\ \varphi_c(x)=c\cdot e^{\alpha x}\) eine Lösung, denn \((x,\varphi_c(x))\in I\times\mathbb R^+=U\) und \(\varphi_c'(x)=\alpha\cdot\varphi_c(x)=f(x,\varphi_c(x))\) für alle \(x\in I\); der Graph \(G_{\varphi_c}\) verläuft komplett in \(U\).</li>
<li>Das Definitionsintervall \(I\) lässt sich (im Rahmen von \(U\)) nicht weiter vergrößern; damit ist \(\varphi_c\) schon <b>maximal</b>.</li>
<li>Die Gesamtheit aller \(\varphi_c\) mit \(c\in\mathbb R^+\) ist die <b>allgemeine Lösung</b>.</li>
<li>Für \((x_0,y_0)\in U\) ist \(\varphi:I\to\mathbb R,\ \varphi(x)=y_0\cdot e^{\alpha(x-x_0)}\) die Lösung des AWP \(y'=\alpha\cdot y\) mit \(y(x_0)=y_0\).</li></ol>''',
      'Beispiel Wachstum maximale Lösung allgemeine Lösung Anfangswertproblem Exponentialfunktion'),

    C('def-linear', 'Def. 11.4',
      r"Was ist eine <b>lineare Differentialgleichung erster Ordnung</b>? Wann heißt sie <b>homogen</b>, wann <b>inhomogen</b>?",
      r'''<p>Sei \(\emptyset\ne I\subseteq\mathbb R\) ein Intervall und \(a:I\to\mathbb R\), \(b:I\to\mathbb R\) zwei <b>stetige</b> Funktionen. Dann heißt</p>
\[y'=a(x)\cdot y+b(x)\]
<p>eine <b>lineare DGL erster Ordnung</b>; es ist also \(U=I\times\mathbb R\) und \(f:U\to\mathbb R,\ f(x,y)=a(x)\cdot y+b(x)\).</p>
<ul><li><b>Homogen</b>, wenn \(b\) die Nullfunktion ist: \(y'=a(x)\cdot y\) bzw. \(y'-a(x)\cdot y=0\).</li>
<li>Andernfalls <b>inhomogen</b>: \(y'=a(x)\cdot y+b(x)\) bzw. \(y'-a(x)\cdot y=b(x)\).</li></ul>''',
      'lineare Differentialgleichung homogen inhomogen Nullfunktion stetig'),

    C('satz-homogen', 'Satz 11.5 (1)',
      r"Wie lautet die allgemeine Lösung der <b>homogenen</b> linearen DGL \(y'=a(x)\cdot y\)? (mit Voraussetzungen)",
      r'''<p><b>Voraussetzungen:</b> \(\emptyset\ne I\subseteq\mathbb R\) Intervall, \(a,b:I\to\mathbb R\) stetig, \(A:I\to\mathbb R\) eine <b>Stammfunktion von \(a\)</b>.</p>
<p>Dann besteht die allgemeine Lösung von \((\mathrm D_0)\ y'=a(x)\cdot y\) <b>genau</b> aus den Funktionen</p>
\[\varphi_c:I\to\mathbb R,\quad\varphi_c(x)=c\cdot e^{A(x)},\quad c\in\mathbb R.\]
<div class="tip">Hier ist \(c\in\mathbb R\) beliebig (auch \(c=0\) oder negativ). Im Wachstumsbeispiel \(y'=\alpha y\) mit \(y>0\) war dagegen nur \(c\in\mathbb R^+\) zugelassen.</div>''',
      'homogene lineare Differentialgleichung allgemeine Lösung Stammfunktion Exponentialfunktion'),

    C('satz-inhomogen', 'Satz 11.5 (2)',
      r"Wie erhält man die allgemeine Lösung der <b>inhomogenen</b> linearen DGL \(y'=a(x)\cdot y+b(x)\), wenn man <b>eine</b> Lösung \(\varphi_p\) kennt?",
      r'''<p>(\(I\) Intervall, \(a,b\) stetig, \(A\) Stammfunktion von \(a\).) Ist \(\varphi_p:I\to\mathbb R\) eine Lösung von \((\mathrm D)\ y'=a(x)\cdot y+b(x)\), so besteht die allgemeine Lösung von \((\mathrm D)\) <b>genau</b> aus den Funktionen</p>
\[\varphi_p+\varphi_c:I\to\mathbb R,\]\[x\mapsto\varphi_p(x)+c\cdot e^{A(x)},\quad c\in\mathbb R.\]
<div class="tip"><b>Merke:</b> allgemeine Lösung (inhomogen) = <b>partikuläre</b> Lösung + allgemeine Lösung der zugehörigen <b>homogenen</b> DGL.</div>''',
      'inhomogene lineare Differentialgleichung partikuläre Lösung allgemeine Lösung Superposition'),

    C('satz-variation', 'Satz 11.5 (3)',
      r"Welche Form hat <b>jede maximale Lösung</b> der inhomogenen linearen DGL \(y'=a(x)\cdot y+b(x)\)? (Variation der Konstanten)",
      r'''<p>Jede maximale Lösung von \((\mathrm D)\) hat die Form</p>
\[\varphi:I\to\mathbb R,\quad\varphi(x)=u(x)\cdot e^{A(x)},\]
<p>wobei \(u:I\to\mathbb R\) eine Stammfunktion zu</p>
\[u':I\to\mathbb R,\quad u'(x)=b(x)\,e^{-A(x)}\]
<p>ist (\(A\) Stammfunktion von \(a\)).</p>
<div class="tip">Im Skript heißt dieser Ansatz <b>Variation der Konstanten</b>: Die Konstante \(c\) in \(c\cdot e^{A(x)}\) wird durch eine differenzierbare Funktion \(u(x)\) ersetzt. Maximale Lösungen sind auf ganz \(I\) definiert.</div>''',
      'Variation der Konstanten maximale Lösung Stammfunktion inhomogen'),

    C('beweis-linear', 'Beweis zu Satz 11.5',
      r"Beweisidee: Warum ist \(\varphi=u\cdot e^{A}\) genau dann Lösung von \(y'=a(x)y+b(x)\), wenn \(u'=b\,e^{-A}\)? Wie folgen daraus die Aussagen über die homogene und die inhomogene Gleichung?",
      r'''<p>Jede differenzierbare \(\varphi:I\to\mathbb R\) lässt sich mit einer differenzierbaren Funktion \(u\) schreiben als</p>
\[\begin{aligned}&\varphi(x)=u(x)\cdot e^{A(x)}\\ \iff\ &\varphi(x)\cdot e^{-A(x)}=u(x).\end{aligned}\]
<p>Produktregel und \(A'=a\) (alles an der Stelle \(x\)):</p>
\[\begin{aligned}\varphi'&=u'e^{A}+u\,e^{A}A'\\ &=u'e^{A}+a\,u\,e^{A}\end{aligned}\]
<p>\(\varphi\) ist also genau dann Lösung, wenn</p>
\[u'e^{A}+a\,u\,e^{A}=a\cdot u\,e^{A}+b,\]
<p>d. h. \(u'(x)\,e^{A(x)}=b(x)\) bzw. \(u'(x)=b(x)\,e^{-A(x)}\). Das zeigt (3).</p>
<ul><li><b>Homogen</b> (\(b=0\)): \(u'=0\), also \(u(x)=c\) konstant ⇒ \(\varphi_c(x)=c\cdot e^{A(x)}\) ist die allgemeine Lösung.</li>
<li><b>Inhomogen:</b> Für ein konkretes \(u\) mit \(u'=b\,e^{-A}\) ist \(\varphi_p=u\cdot e^{A}\) eine <b>partikuläre</b> Lösung, und die allgemeine Lösung (\(c\in\mathbb R\)) ist</li></ul>
\[\begin{aligned}\varphi(x)&=(u(x)+c)\,e^{A(x)}\\ &=\underbrace{u(x)e^{A(x)}}_{=\varphi_p(x)}+\underbrace{c\,e^{A(x)}}_{=\varphi_c(x)}.\end{aligned}\]''',
      'Beweis Produktregel Variation der Konstanten partikuläre Lösung'),

    C('vorgehen-linear', 'Bsp. 11.6 · Vorgehen',
      r"Wie geht man bei einer <b>linearen DGL</b> \(y'=a(x)y+b(x)\) mit Anfangswert \(y(x_0)=y_0\) vor (wie in den Beispielen des Skripts)?",
      r'''<ol><li>\(a(x)\) und \(b(x)\) ablesen (stetig).</li>
<li>Stammfunktion \(A\) von \(a\) bestimmen ⇒ homogene Lösungen \(\varphi_c(x)=c\cdot e^{A(x)}\).</li>
<li>Partikuläre Lösung \(\varphi_p\) finden:
<ul><li>gelingt es (z. B. durch Raten), ist \(\varphi_p+\varphi_c\) die allgemeine Lösung;</li>
<li>sonst <b>Variation der Konstanten</b>: \(\varphi(x)=u(x)\,e^{A(x)}\) einsetzen ⇒ \(u'(x)=b(x)\,e^{-A(x)}\), integrieren. Mit „\(+c\)“ beim Integrieren erhält man gleich die allgemeine Lösung.</li></ul></li>
<li>Die freie Konstante \(c\) mit dem Anfangswert \(y(x_0)=y_0\) bestimmen.</li></ol>''',
      'Vorgehen Rezept lineare Differentialgleichung Variation der Konstanten partikuläre Lösung Anfangswert'),

    C('bsp-4xy', 'Bsp. 11.6 1a) (F01 II 6)',
      r"Wie lautet die allgemeine Lösung von \(y'=4xy\)? Wie sehen die Graphen aus?",
      r'''<p>Homogene lineare DGL mit \(a:\mathbb R\to\mathbb R,\ a(x)=4x\). Stammfunktion: \(A(x)=2x^2\). Allgemeine Lösung:</p>
\[\varphi_c(x)=c\cdot e^{A(x)}=c\cdot e^{2x^2}\]<p>mit \(\varphi_c:\mathbb R\to\mathbb R\), \(c\in\mathbb R\).</p>
<p><b>Skizze</b> (im Skript für \(c\in\{0,\pm\frac12,\pm1\}\)): Graphen symmetrisch zur \(y\)-Achse mit \(\varphi_c(0)=c\); für \(c>0\) oberhalb der \(x\)-Achse, nach oben steil ansteigend; \(c=0\) ist die \(x\)-Achse; für \(c<0\) gespiegelt unterhalb der \(x\)-Achse.</p>''',
      'Beispiel homogen 4xy Skizze Graphen Staatsexamen'),

    C('bsp-4xy-awp', 'Bsp. 11.6 1b)',
      r"Bestimme die maximale Lösung von \(y'=4xy+(1-x)\,e^{4x}\) mit \(y(1)=0\).",
      r'''<p>Inhomogene lineare DGL mit \(a(x)=4x\), \(b(x)=(1-x)\,e^{4x}\); homogene Lösungen \(c\cdot e^{2x^2}\).</p>
<p><b>Weg 1 – partikuläre Lösung raten:</b> \(\varphi_p(x)=\frac14e^{4x}\), denn \(\varphi_p'(x)=e^{4x}=4x\cdot\varphi_p(x)+(1-x)e^{4x}\) (da \(4x\cdot\frac14e^{4x}=x\,e^{4x}\)). Allgemeine Lösung: \(\varphi(x)=\frac14e^{4x}+c\cdot e^{2x^2}\), \(c\in\mathbb R\).</p>
<p><b>Weg 2 – Variation der Konstanten:</b> \(\varphi(x)=u(x)\,e^{2x^2}\) ⇒ \(u'(x)\,e^{2x^2}=(1-x)\,e^{4x}\) ⇒</p>
\[\begin{aligned}u'(x)&=(1-x)\,e^{4x-2x^2}\\ &=\tfrac14\,e^{4x-2x^2}(4-4x)\end{aligned}\]<p>⇒ \(u(x)=\frac14e^{4x-2x^2}+c\),</p>
<p>also \(\varphi(x)=\frac14e^{4x}+c\cdot e^{2x^2}\).</p>
<p><b>Anfangswert:</b> \(\frac14e^4+c\cdot e^2=0\iff c=-\frac14e^2\). Ergebnis:</p>
\[\varphi:\mathbb R\to\mathbb R,\quad\varphi(x)=\tfrac14e^{4x}-\tfrac14e^{2x^2+2}.\]''',
      'Beispiel inhomogen Anfangswertaufgabe partikuläre Lösung Variation der Konstanten'),

    C('bsp-arctan', 'Bsp. 11.6 2 (H07 III 3)',
      r"Bestimme die Lösung von \(y'=\frac{x}{1+x^2}\cdot y+\frac{1}{\sqrt{1+x^2}}\) mit \(y(0)=0\).",
      r'''<p>Inhomogene lineare DGL mit \(a(x)=\frac{x}{1+x^2}=\frac12\cdot\frac{2x}{1+x^2}\), \(b(x)=\frac1{\sqrt{1+x^2}}\). Stammfunktion \(A(x)=\frac12\ln(1+x^2)\), also homogene Lösungen</p>
\[\begin{aligned}\varphi_c(x)&=c\cdot e^{\frac12\ln(1+x^2)}\\ &=c\cdot\left(e^{\ln(1+x^2)}\right)^{\frac12}\\ &=c\cdot\sqrt{1+x^2}\end{aligned}\]<p>mit \(c\in\mathbb R\).</p>
<p><b>Variation der Konstanten:</b> \(\varphi(x)=u(x)\sqrt{1+x^2}\), \(\varphi'(x)=u'(x)\sqrt{1+x^2}+u(x)\frac{x}{\sqrt{1+x^2}}\). Einsetzen ⇒ \(u'(x)\sqrt{1+x^2}=\frac1{\sqrt{1+x^2}}\), also \(u'(x)=\frac1{1+x^2}\).</p>
<ul><li>Partikulär: \(u=\arctan\) ⇒ \(\varphi_p(x)=\arctan(x)\sqrt{1+x^2}\); allgemein \(\varphi_p+\varphi_c\).</li>
<li>Gleich allgemein: \(u(x)=\arctan(x)+c\) ⇒ \(\varphi(x)=(\arctan(x)+c)\sqrt{1+x^2}\).</li></ul>
<p>Anfangswert: wegen \(\arctan 0=0\) und \(\sqrt{1+0^2}=1\) gilt \(\varphi(0)=0\iff c=0\). Maximale Lösung:</p>
\[\varphi(x)=\arctan(x)\cdot\sqrt{1+x^2}\]<p>für \(x\in\mathbb R\).</p>''',
      'Beispiel arctan Wurzel Logarithmus Variation der Konstanten Staatsexamen'),

    C('def-getrennt', 'Def. 11.7',
      r"Was ist eine <b>Differentialgleichung mit getrennten Variablen</b>?",
      r'''<p>Seien \(\emptyset\ne I\subseteq\mathbb R\) und \(\emptyset\ne J\subseteq\mathbb R\) zwei Intervalle und \(h:I\to\mathbb R\), \(g:J\to\mathbb R\) zwei <b>stetige</b> Funktionen. Dann heißt</p>
\[y'=h(x)\cdot g(y)\quad\text{für } x\in I \text{ und } y\in J\]
<p>eine DGL mit getrennten Variablen; es ist also \(U=I\times J\subseteq\mathbb R^2\) und \(f:U\to\mathbb R,\ f(x,y)=h(x)\cdot g(y)\).</p>''',
      'getrennte Variablen Trennung der Variablen Definition'),

    C('spezialfaelle', 'Def. 11.7 (1)–(3)',
      r"Welche drei <b>Spezialfälle</b> der DGL mit getrennten Variablen \(y'=h(x)\cdot g(y)\) gibt es? Was ist eine <b>autonome</b> DGL?",
      r'''<ol><li>\(J=\mathbb R\) (also \(U=I\times\mathbb R\)) und \(g(y)=1\): \(y'=h(x)\) für \(x\in I\). Die allgemeine Lösung ist die Menge \(\int h(x)\,dx\) <b>aller Stammfunktionen</b> von \(h\).</li>
<li>\(J=\mathbb R\) und \(g(y)=y\): \(y'=h(x)\cdot y\) für \(x\in I\), also eine <b>homogene lineare</b> DGL.</li>
<li>\(I=\mathbb R\) (also \(U=\mathbb R\times J\)) und \(h(x)=1\): \(y'=g(y)\) für \(y\in J\); diese heißt <b>autonome</b> Differentialgleichung.</li></ol>''',
      'Spezialfall autonome Differentialgleichung Stammfunktion homogen linear'),

    C('bsp-wurzel-xy', 'Bsp. 11.8 (H04 II 6)',
      r"Bestimme die maximale Lösung von \(y'=(xy)^{\frac12}\) für \(x>0,\ y>0\) mit \(y(1)=1\).",
      r'''<p>Wegen \((xy)^{\frac12}=x^{\frac12}\cdot y^{\frac12}\) für \(x,y\in\mathbb R^+\): getrennte Variablen mit \(h:\mathbb R^+\to\mathbb R,\ h(x)=x^{\frac12}\) und \(g:\mathbb R^+\to\mathbb R,\ g(y)=y^{\frac12}\).</p>
<p>Da \(g(y)\ne0\) für alle \(y\in\mathbb R^+\): \(y^{-\frac12}y'=x^{\frac12}\). Integration nach \(x\) mit Substitutionsregel (\(y'=\frac{dy}{dx}\), \(y'\,dx=dy\)):</p>
\[\int y^{-\frac12}\,dy=\int x^{\frac12}\,dx\ \Rightarrow\ 2y^{\frac12}=\tfrac23x^{\frac32}+c.\]
<p>\(y(1)=1\iff2=\frac23+c\iff c=\frac43\). Also</p>
\[\varphi:\mathbb R^+\to\mathbb R,\quad\varphi(x)=\left(\tfrac13x^{\frac32}+\tfrac23\right)^2.\]''',
      'Beispiel getrennte Variablen Substitutionsregel Wurzel Staatsexamen'),

    C('satz-trennung', 'Satz 11.9',
      r"<b>Trennung der Variablen</b> (g nullstellenfrei): Was sagt der Satz über \(y'=h(x)\,g(y)\), \(y(x_0)=y_0\), und wie berechnet man die Lösung?",
      r'''<p><b>Voraussetzungen:</b> \(\emptyset\ne I,J\subseteq\mathbb R\) <b>offene</b> Intervalle, \((x_0,y_0)\in I\times J\), \(h:I\to\mathbb R\) und \(g:J\to\mathbb R\) stetig, \(g\) <b>nullstellenfrei</b>.</p>
<p><b>Aussage:</b> Das AWP hat eine <b>eindeutig bestimmte maximale Lösung</b> \(\varphi:D_\varphi\to\mathbb R\).</p>
<p><b>Berechnung:</b> \(H\) Stammfunktion von \(h\), \(Q\) Stammfunktion von \(\frac1g\). Ansatz „Trennung der Variablen“:</p>
\[\int\frac{1}{g(y)}\,dy=\int h(x)\,dx,\]<p>also \(Q(y)=H(x)+c\).</p>
<p>\(c\) an \(y(x_0)=y_0\) anpassen, dann nach \(y\) auflösen. Das geht immer, da \(Q'(y)=\frac1{g(y)}\ne0\) auf dem Intervall \(J\) ⇒ \(Q\) <b>streng monoton</b>, also umkehrbar:</p>
\[\varphi(x)=Q^{-1}\bigl(H(x)+c_0\bigr)\]<p>(\(c_0\): die angepasste Konstante).</p>
<div class="tip warn">Das maximale Definitionsintervall \(D_\varphi\) kann <b>echt in \(I\) enthalten</b> sein.</div>''',
      'Trennung der Variablen nullstellenfrei eindeutig maximale Lösung Stammfunktion streng monoton umkehrbar'),

    C('bsp-2xy2', 'Bsp. 11.10 (F08 I 6)',
      r"Löse \(y'=2xy^2\) mit \(y(1)=a\) für \(a=\frac12\) und \(a=-\frac12\) und bestimme jeweils das maximale Definitionsintervall.",
      r'''<p>Getrennte Variablen: \(h(x)=2x\), \(g(y)=y^2\) (beide auf \(\mathbb R\)). \(g\) hat die Nullstelle \(y=0\) ⇒ \(\psi(x)=0\) ist eine maximale Lösung. Getrennt betrachtet auf \(U_1=\mathbb R\times\mathbb R^+\) und \(U_2=\mathbb R\times\mathbb R^-\) (dort \(g\) nullstellenfrei):</p>
\[\int\frac1{y^2}\,dy=\int2x\,dx\ \Rightarrow\ -\frac1y=x^2+c.\]
<ul><li>\(a=\frac12\): \(-2=1+c\iff c=-3\), \(y=\frac1{3-x^2}\). Von \(]-\infty,-\sqrt3[\), \(]-\sqrt3,\sqrt3[\), \(]\sqrt3,+\infty[\) wählt man das Intervall mit \(x_0=1\): \(\varphi_1:]-\sqrt3,\sqrt3[\,\to\mathbb R\), \(\varphi_1(x)=\frac1{3-x^2}\). Verläuft in \(U_1\); wegen \(\lim_{x\to\pm\sqrt3}\varphi_1(x)=+\infty\) nicht fortsetzbar ⇒ maximal.</li>
<li>\(a=-\frac12\): \(2=1+c\iff c=1\), \(\varphi_2:\mathbb R\to\mathbb R\), \(\varphi_2(x)=-\frac1{x^2+1}\). Verläuft in \(U_2\); wegen \(D_{\varphi_2}=\mathbb R\) maximal.</li></ul>''',
      'Beispiel getrennte Variablen maximales Definitionsintervall Polstelle Halbebene Staatsexamen'),

    C('satz-trennung-c1', 'Satz 11.11',
      r"Was gilt für \(y'=h(x)\,g(y)\), \(y(x_0)=y_0\), wenn \(g\) <b>stetig differenzierbar</b> ist (\(g\) darf Nullstellen haben)?",
      r'''<p><b>Voraussetzungen:</b> \(\emptyset\ne I,J\subseteq\mathbb R\) offene Intervalle, \((x_0,y_0)\in I\times J\), \(h:I\to\mathbb R\), \(g:J\to\mathbb R\) stetig, \(g\) zusätzlich <b>stetig differenzierbar</b>.</p>
<p><b>Aussage:</b> Das AWP hat eine <b>eindeutig bestimmte maximale Lösung</b> \(\varphi:D_\varphi\to\mathbb R\).</p>
<ul><li>Für \(g(y_0)=0\): die <b>konstante</b> Funktion \(\varphi:I\to\mathbb R,\ \varphi(x)=y_0\).</li>
<li>Für \(g(y_0)\ne0\): wieder Trennung der Variablen: in \(\int\frac{dy}{g(y)}=\int h(x)\,dx+c\) die Konstante an \(y(x_0)=y_0\) anpassen und nach \(y\) auflösen; \(D_\varphi\) kann echt in \(I\) enthalten sein.</li></ul>''',
      'stetig differenzierbar eindeutig konstante Lösung Nullstelle Trennung der Variablen'),

    C('bsp-autonom', 'Bsp. 11.12 1 (H98 III 5)',
      r"Bestimme die allgemeine Lösung von \(y'+(y+3)(y+2)=0\): konstante Lösungen, Lage der übrigen Lösungen, Formeln.",
      r'''<p>Autonome DGL \(y'=g(y)\) mit \(g(y)=-(y+3)(y+2)\), stetig differenzierbar ⇒ durch jeden Punkt \((x_0,y_0)\in\mathbb R^2\) genau eine maximale Lösung.</p>
<ul><li><b>Konstante Lösungen</b> = Nullstellen von \(g\): \(\psi_1(x)=-3\), \(\psi_2(x)=-2\).</li>
<li>Kein anderer Graph hat einen Punkt mit \(G_{\psi_1}\) oder \(G_{\psi_2}\) gemeinsam (sonst gäbe es durch diesen Punkt mehr als eine maximale Lösung). Jede andere Lösung verläuft also ganz in \(y<-3\), in \(-3<y<-2\) oder in \(-2<y\); dort ist \(g(y)\ne0\).</li></ul>
<p>\(\frac1{g(y)}=\frac{-1}{(y+3)(y+2)}=\frac1{y+3}-\frac1{y+2}\) ⇒ \(\ln|y+3|-\ln|y+2|=x+c\) ⇒ \(\left|\frac{y+3}{y+2}\right|=e^{x+c}\).</p>
<ul><li>\(-3<y<-2\) (Quotient \(<0\)): \(\varphi_c:\mathbb R\to\mathbb R,\ \varphi_c(x)=-\frac{2e^{x+c}+3}{1+e^{x+c}}\).</li>
<li>\(y<-3\) oder \(-2<y\) (Quotient \(>0\)): \(\varphi_c(x)=\frac{2e^{x+c}-3}{1-e^{x+c}}\); wegen \(1-e^{x+c}=0\iff x=-c\) ist \(D_{\varphi_c}=]-\infty,-c[\) oder \(]-c,+\infty[\).</li></ul>''',
      'autonome Differentialgleichung konstante Lösungen Nullstellen Partialbruch Logarithmus Staatsexamen'),

    C('bsp-wurzel-y', 'Bsp. 11.12 2 (H07 I 6)',
      r"Das AWP \(y'=\sqrt y\), \(y(0)=0\) auf \([0,+\infty[\): Warum gibt es <b>mehrere</b> Lösungen? Nenne sie.",
      r'''<p>Autonome DGL mit \(g:[0,+\infty[\,\to\mathbb R,\ g(y)=\sqrt y\), stetig, aber in der Nullstelle \(y=0\) <b>nicht differenzierbar</b>.</p>
<ul><li>Die Nullfunktion \(\psi(x)=0\) ist eine Lösung.</li>
<li>Auf dem offenen 1. Quadranten \(U=\mathbb R^+\times\mathbb R^+\) (\(y>0\)) ist \(g\) nullstellenfrei ⇒ eindeutige maximale Lösung durch jeden Punkt von \(U\): \(\int y^{-\frac12}dy=\int1\,dx\) ⇒ \(2\sqrt y=x+c\) ⇒ \(y=\left(\frac{x+c}2\right)^2\) für \(x>-c\).</li>
<li>\(c=0\): \(\varphi_0(x)=\left(\frac x2\right)^2\) auf \(]0,+\infty[\) lässt sich zu \(\varphi:[0,+\infty[\,\to\mathbb R,\ \varphi(x)=\left(\frac x2\right)^2\) fortsetzen; wegen \(\varphi'(x)=\frac x2=\sqrt{\varphi(x)}\) für \(x\ge0\) und \(\varphi(0)=0\) eine <b>zweite</b> Lösung.</li>
<li>Sogar <b>unendlich viele</b>: für jedes \(c<0\) ist \(\varphi_c(x)=\left(\frac{x+c}2\right)^2\) für \(x>-c\) und \(\varphi_c(x)=0\) für \(0\le x\le-c\) eine maximale Lösung.</li></ul>
<div class="tip warn">Die Voraussetzung „\(g\) stetig differenzierbar“ ist hier verletzt – und die Lösung ist nicht eindeutig.</div>''',
      'Wurzel nicht eindeutig unendlich viele Lösungen nicht differenzierbar Nullfunktion Staatsexamen'),

    C('peano', 'Satz 11.13 (1)',
      r"Was besagt der <b>Existenzsatz von Peano</b>?",
      r'''<p>Sei \(\emptyset\ne U\subseteq\mathbb R^2\) eine <b>offene</b> Teilmenge mit \((x_0,y_0)\in U\) und \(f:U\to\mathbb R\) eine Funktion.</p>
<p>Ist \(f\) <b>stetig</b>, so existiert <b>(mindestens) eine</b> maximale Lösung \(\varphi:D_\varphi\to\mathbb R\) des Anfangswertproblems \(y'=f(x,y)\) mit \(y(x_0)=y_0\).</p>
<p>(Giuseppe Peano, 1858–1922; verallgemeinert die Sätze zur Trennung der Variablen.)</p>''',
      'Peano Existenzsatz Existenz stetig mindestens eine Lösung'),

    C('eindeutigkeit', 'Satz 11.13 (2)',
      r"Was besagt der <b>Eindeutigkeitssatz</b> für \(y'=f(x,y)\), \(y(x_0)=y_0\)?",
      r'''<p>(\(\emptyset\ne U\subseteq\mathbb R^2\) offen, \((x_0,y_0)\in U\), \(f:U\to\mathbb R\) stetig.) Ist \(f\) <b>darüber hinaus bezüglich \(y\) partiell differenzierbar</b> und die partielle Ableitung \(\partial_yf:U\to\mathbb R\) <b>stetig</b>, so ist die maximale Lösung \(\varphi:D_\varphi\to\mathbb R\) aus dem Existenzsatz von Peano sogar <b>eindeutig bestimmt</b>.</p>
<div class="tip">Vergleiche \(y'=\sqrt y\), \(y(0)=0\): Dort ist \(g(y)=\sqrt y\) in \(0\) nicht differenzierbar, und es gibt unendlich viele Lösungen.</div>''',
      'Eindeutigkeitssatz eindeutig partiell differenzierbar stetige partielle Ableitung'),

    C('vergleich', 'Sätze 11.5, 11.9, 11.11, 11.13',
      r"<b>Überblick:</b> Welche Voraussetzungen liefern Existenz bzw. Eindeutigkeit der maximalen Lösung eines AWP?",
      r'''<ul><li><b>Linear</b> \(y'=a(x)y+b(x)\), \(a,b\) stetig auf \(I\): allgemeine Lösung explizit (\(\varphi_p+c\,e^{A}\)); maximale Lösungen auf ganz \(I\).</li>
<li><b>Getrennte Variablen</b>, \(I,J\) offen, \(h,g\) stetig, \(g\) <b>nullstellenfrei</b>: eindeutige maximale Lösung, \(\varphi=Q^{-1}(H+c_0)\).</li>
<li><b>Getrennte Variablen</b>, \(g\) <b>stetig differenzierbar</b>: eindeutige maximale Lösung; bei \(g(y_0)=0\) konstant \(y_0\).</li>
<li><b>Allgemein</b> \(y'=f(x,y)\), \(U\) offen: \(f\) stetig ⇒ mindestens eine (Peano); zusätzlich \(\partial_yf\) existiert und stetig ⇒ eindeutig.</li></ul>''',
      'Überblick Vergleich Existenz Eindeutigkeit Voraussetzungen'),
]

# ---------------------------------------------------------------- Tests
ITEMS = []

def mc(id, q, options, correct, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, type='mc', q=q, options=options, correct=correct, expl=expl, src=src, kw=kw, warn=warn))

def tf(id, statement, answer, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=src, kw=kw, warn=warn))

def gap(id, text, expl, src, kw):
    ITEMS.append(dict(id=id, type='gap', text=text, expl=expl, src=src, kw=kw))

# ------------------------------------------------------------ Multiple Choice
mc('q11-mc-01', r"Welche Differentialgleichung beschreibt die Modellannahme „<b>natürliches Wachstum</b>“ (\(u(t)\) und \(u'(t)\) direkt proportional)?",
   [r"\(u'(t)=\alpha\cdot u(t)\)", r"\(u(t)=\alpha\cdot u'(t)+t\)", r"\(u'(t)=\alpha+u(t)\)", r"\(u''(t)=\alpha\cdot u(t)\)"], 0,
   r"Es gibt eine Proportionalitätskonstante \(\alpha\in\mathbb R\) mit \(u'(t)=\alpha\cdot u(t)\) für alle \(t\in I\).", 'Bem. 11.1 b)', 'natürliches Wachstum Modell proportional')
mc('q11-mc-02', r"Welche Funktion löst \(u'=\alpha\cdot u\) mit dem Anfangswert \(u(t_0)=u_0\)?",
   [r"\(u(t)=u_0\cdot e^{\alpha(t-t_0)}\)", r"\(u(t)=u_0\cdot e^{\alpha t}\)", r"\(u(t)=u_0\cdot e^{\alpha(t_0-t)}\)", r"\(u(t)=u_0+e^{\alpha(t-t_0)}\)"], 0,
   r"Aus \(u_0=c\cdot e^{\alpha t_0}\) folgt \(c=u_0\cdot e^{-\alpha t_0}\), also \(u(t)=u_0\cdot e^{\alpha(t-t_0)}\).", 'Bem. 11.1 e)', 'Anfangswert Exponentialfunktion')
mc('q11-mc-03', r"Wann heißt eine differenzierbare Funktion \(\varphi:D_\varphi\to\mathbb R\) auf einem Intervall \(D_\varphi\) eine <b>Lösung</b> von \(y'=f(x,y)\), \((x,y)\in U\)?",
   [r"Wenn \((x,\varphi(x))\in U\) und \(\varphi'(x)=f(x,\varphi(x))\) für alle \(x\in D_\varphi\)",
    r"Wenn \(\varphi'(x)=f(x,\varphi(x))\) für mindestens ein \(x\in D_\varphi\)",
    r"Wenn \(\varphi(x)=f(x,\varphi'(x))\) für alle \(x\in D_\varphi\)",
    r"Wenn \((x,\varphi'(x))\in U\) für alle \(x\in D_\varphi\)"], 0,
   r"Beide Bedingungen müssen für <b>alle</b> \(x\in D_\varphi\) gelten: Graph in \(U\) und Gleichung erfüllt.", 'Def. 11.2 (2)', 'Lösung Definition')
mc('q11-mc-04', r"Was ist die <b>allgemeine Lösung</b> einer Differentialgleichung \(y'=f(x,y)\)?",
   ['Die Menge aller maximalen Lösungen', 'Eine beliebige Lösung', 'Die Lösung mit dem größten Definitionsintervall', r"Die Menge aller auf ganz \(\mathbb R\) definierten Lösungen"], 0,
   r"Eine Lösung ist maximal, wenn es keine echte Fortsetzung gibt, die ebenfalls Lösung ist.", 'Def. 11.2 (4)', 'allgemeine Lösung maximal')
mc('q11-mc-05', r"Was ist nach Definition eine Lösung des <b>Anfangswertproblems</b> \(y'=f(x,y)\), \(y(x_0)=y_0\)?",
   [r"Eine maximale Lösung \(\varphi\) mit \(\varphi(x_0)=y_0\)", r"Irgendeine Lösung \(\varphi\) mit \(\varphi(x_0)=y_0\)", r"Eine auf ganz \(\mathbb R\) definierte Lösung", r"Jede Lösung, deren Graph durch \((y_0,x_0)\) geht"], 0,
   'Auch „Anfangswertaufgabe“ genannt. Die Lösung muss maximal sein.', 'Def. 11.2 (5)', 'Anfangswertproblem maximal')
mc('q11-mc-06', r"Wann heißt die lineare DGL \(y'=a(x)\cdot y+b(x)\) (\(a,b\) stetig) <b>homogen</b>?",
   [r"Wenn \(b\) die Nullfunktion ist", r"Wenn \(a\) die Nullfunktion ist", r"Wenn \(a\) konstant ist", r"Wenn \(a=b\) ist"], 0,
   r"Dann \(y'=a(x)\cdot y\) bzw. \(y'-a(x)\cdot y=0\); sonst inhomogen.", 'Def. 11.4', 'homogen inhomogen Nullfunktion')
mc('q11-mc-07', r"\(A\) sei eine Stammfunktion der stetigen Funktion \(a\) auf dem Intervall \(I\). Was ist die allgemeine Lösung von \(y'=a(x)\cdot y\)?",
   [r"\(\varphi_c(x)=c\cdot e^{A(x)}\), \(c\in\mathbb R\)", r"\(\varphi_c(x)=c\cdot e^{a(x)}\), \(c\in\mathbb R\)", r"\(\varphi_c(x)=A(x)+c\), \(c\in\mathbb R\)", r"\(\varphi_c(x)=c\cdot e^{-A(x)}\), \(c\in\mathbb R\)"], 0,
   r"Im Exponenten steht die <b>Stammfunktion</b> \(A\), nicht \(a\) selbst.", 'Satz 11.5 (1)', 'homogen allgemeine Lösung Stammfunktion')
mc('q11-mc-08', r"\(\varphi_p\) sei eine Lösung der inhomogenen linearen DGL \(y'=a(x)y+b(x)\), \(A\) Stammfunktion von \(a\). Was ist die allgemeine Lösung?",
   [r"\(\varphi_p(x)+c\cdot e^{A(x)}\), \(c\in\mathbb R\)", r"\(c\cdot\varphi_p(x)\), \(c\in\mathbb R\)", r"\(\varphi_p(x)+c\), \(c\in\mathbb R\)", r"\(\varphi_p(x)\cdot e^{A(x)}+c\), \(c\in\mathbb R\)"], 0,
   'Partikuläre Lösung plus allgemeine Lösung der zugehörigen homogenen DGL.', 'Satz 11.5 (2)', 'inhomogen partikulär allgemeine Lösung')
mc('q11-mc-09', r"Beim Ansatz \(\varphi(x)=u(x)\cdot e^{A(x)}\) (Variation der Konstanten) für \(y'=a(x)y+b(x)\): Welche Bedingung muss \(u\) erfüllen?",
   [r"\(u'(x)=b(x)\,e^{-A(x)}\)", r"\(u'(x)=b(x)\,e^{A(x)}\)", r"\(u'(x)=a(x)\,e^{-A(x)}\)", r"\(u(x)=b(x)\,e^{-A(x)}\)"], 0,
   r"Einsetzen: \(u'e^{A}+a\,u\,e^{A}=a\,u\,e^{A}+b\), also \(u'e^{A}=b\).", 'Satz 11.5 (3)', 'Variation der Konstanten')
mc('q11-mc-10', r"Was ist die allgemeine Lösung von \(y'=4xy\)?",
   [r"\(c\cdot e^{2x^2}\), \(c\in\mathbb R\)", r"\(c\cdot e^{4x}\), \(c\in\mathbb R\)", r"\(c\cdot e^{x^2}\), \(c\in\mathbb R\)", r"\(2x^2+c\), \(c\in\mathbb R\)"], 0,
   r"\(a(x)=4x\) hat die Stammfunktion \(A(x)=2x^2\).", 'Bsp. 11.6 1a)', 'Beispiel homogen')
mc('q11-mc-11', r"Was ist die maximale Lösung von \(y'=4xy+(1-x)e^{4x}\) mit \(y(1)=0\)?",
   [r"\(\frac14e^{4x}-\frac14e^{2x^2+2}\)", r"\(\frac14e^{4x}+\frac14e^{2x^2+2}\)", r"\(\frac14e^{4x}-\frac14e^{2x^2}\)", r"\(e^{4x}-e^{2x^2+2}\)"], 0,
   r"Allgemein \(\frac14e^{4x}+c\,e^{2x^2}\); aus \(\frac14e^4+c\,e^2=0\) folgt \(c=-\frac14e^2\).", 'Bsp. 11.6 1b)', 'Beispiel inhomogen Anfangswert')
mc('q11-mc-12', r"Was ist die Lösung von \(y'=\frac{x}{1+x^2}\,y+\frac1{\sqrt{1+x^2}}\) mit \(y(0)=0\)?",
   [r"\(\arctan(x)\cdot\sqrt{1+x^2}\)", r"\(\frac{\arctan(x)}{\sqrt{1+x^2}}\)", r"\(\ln(1+x^2)\cdot\sqrt{1+x^2}\)", r"\(\sqrt{1+x^2}-1\)"], 0,
   r"Homogen: \(c\sqrt{1+x^2}\). Variation der Konstanten liefert \(u'=\frac1{1+x^2}\), also \(u=\arctan+c\); \(y(0)=0\) gibt \(c=0\).", 'Bsp. 11.6 2', 'Beispiel arctan')
mc('q11-mc-13', r"Welche Funktionen bilden die allgemeine Lösung von \(y'=\frac{x}{1+x^2}\cdot y\)?",
   [r"\(c\cdot\sqrt{1+x^2}\), \(c\in\mathbb R\)", r"\(c\cdot(1+x^2)\), \(c\in\mathbb R\)", r"\(\frac{c}{\sqrt{1+x^2}}\), \(c\in\mathbb R\)", r"\(c\cdot e^{x^2}\), \(c\in\mathbb R\)"], 0,
   r"\(A(x)=\frac12\ln(1+x^2)\), also \(e^{A(x)}=\left(e^{\ln(1+x^2)}\right)^{\frac12}=\sqrt{1+x^2}\).", 'Bsp. 11.6 2', 'Beispiel homogen Wurzel Logarithmus')
mc('q11-mc-14', r"Welche Differentialgleichung heißt <b>autonom</b>?",
   [r"\(y'=g(y)\)", r"\(y'=h(x)\)", r"\(y'=a(x)\cdot y\)", r"\(y'=a(x)\cdot y+b(x)\)"], 0,
   r"Spezialfall der DGL mit getrennten Variablen \(y'=h(x)g(y)\) mit \(I=\mathbb R\) und \(h(x)=1\).", 'Def. 11.7 (3)', 'autonom')
mc('q11-mc-15', r"Was ist die allgemeine Lösung von \(y'=h(x)\) (\(h\) stetig auf \(I\))?",
   [r"Die Menge \(\int h(x)\,dx\) aller Stammfunktionen von \(h\)", r"Die Funktion \(h'\)", r"Die Menge aller Funktionen \(c\cdot e^{h(x)}\)", r"Die Nullstellen von \(h\)"], 0,
   r"Spezialfall \(g(y)=1\) der DGL mit getrennten Variablen.", 'Def. 11.7 (1)', 'Stammfunktion Spezialfall')
mc('q11-mc-16', r"Trennung der Variablen bei \(y'=h(x)g(y)\) mit nullstellenfreiem \(g\): Warum lässt sich \(Q(y)=H(x)+c\) (\(Q\) Stammfunktion von \(\frac1g\)) immer nach \(y\) auflösen?",
   [r"Weil \(Q'=\frac1g\ne0\) auf einem Intervall, also \(Q\) streng monoton und damit umkehrbar ist", r"Weil \(H\) streng monoton ist", r"Weil \(c\) beliebig gewählt werden kann", r"Weil \(g\) differenzierbar ist"], 0,
   r"Dann \(\varphi(x)=Q^{-1}(H(x)+c_0)\).", 'Satz 11.9', 'Trennung der Variablen umkehrbar streng monoton')
mc('q11-mc-17', r"Was ist das maximale Definitionsintervall der Lösung von \(y'=2xy^2\) mit \(y(1)=\frac12\)?",
   [r"\(]-\sqrt3,\sqrt3[\)", r"\(\mathbb R\)", r"\(]\sqrt3,+\infty[\)", r"\(]0,\sqrt3[\)"], 0,
   r"Lösung \(\varphi_1(x)=\frac1{3-x^2}\); das Intervall muss \(x_0=1\) enthalten, an \(\pm\sqrt3\) geht \(\varphi_1\) gegen \(+\infty\).", 'Bsp. 11.10', 'maximales Definitionsintervall', warn=True)
mc('q11-mc-18', r"Was ist die Lösung von \(y'=2xy^2\) mit \(y(1)=-\frac12\)?",
   [r"\(-\frac1{x^2+1}\) auf \(\mathbb R\)", r"\(\frac1{3-x^2}\) auf \(]-\sqrt3,\sqrt3[\)", r"\(\frac1{x^2+1}\) auf \(\mathbb R\)", r"\(-\frac1{x^2-1}\) auf \(]-1,1[\)"], 0,
   r"Aus \(-\frac1y=x^2+c\) und \(2=1+c\) folgt \(c=1\); die Lösung liegt in der unteren Halbebene.", 'Bsp. 11.10', 'Beispiel getrennte Variablen')
mc('q11-mc-19', r"Was ist die maximale Lösung von \(y'=(xy)^{\frac12}\) (\(x,y>0\)) mit \(y(1)=1\)?",
   [r"\(\left(\frac13x^{\frac32}+\frac23\right)^2\)", r"\(\left(\frac23x^{\frac32}+\frac13\right)^2\)", r"\(\frac13x^{\frac32}+\frac23\)", r"\(\frac14\left(x^{\frac32}+1\right)^2\)"], 0,
   r"\(2y^{\frac12}=\frac23x^{\frac32}+c\) mit \(c=\frac43\).", 'Bsp. 11.8', 'Beispiel getrennte Variablen Wurzel')
mc('q11-mc-20', r"Welche konstanten Lösungen hat \(y'+(y+3)(y+2)=0\)?",
   [r"\(y=-3\) und \(y=-2\)", r"\(y=3\) und \(y=2\)", r"nur \(y=-3\)", 'keine'], 0,
   r"Konstante Lösungen einer autonomen DGL \(y'=g(y)\) sind genau die Nullstellen von \(g(y)=-(y+3)(y+2)\).", 'Bsp. 11.12 1', 'konstante Lösungen Nullstellen autonom')
mc('q11-mc-21', r"Was garantiert der <b>Existenzsatz von Peano</b> für \(y'=f(x,y)\), \(y(x_0)=y_0\) (\(U\) offen), wenn \(f\) stetig ist?",
   ['Mindestens eine maximale Lösung', 'Genau eine maximale Lösung', 'Eine auf ganz ℝ definierte Lösung', 'Nichts ohne Differenzierbarkeit von f'], 0,
   r"Eindeutigkeit braucht zusätzlich: \(\partial_yf\) existiert und ist stetig.", 'Satz 11.13 (1)', 'Peano Existenz')
mc('q11-mc-22', r"Welche zusätzliche Voraussetzung (neben der Stetigkeit von \(f\)) liefert die <b>Eindeutigkeit</b> der maximalen Lösung von \(y'=f(x,y)\), \(y(x_0)=y_0\)?",
   [r"\(f\) ist bezüglich \(y\) partiell differenzierbar und \(\partial_yf\) ist stetig", r"\(f\) ist bezüglich \(x\) partiell differenzierbar", r"\(f\) ist beschränkt", r"\(f\) ist nullstellenfrei"], 0,
   'Eindeutigkeitssatz.', 'Satz 11.13 (2)', 'Eindeutigkeitssatz partielle Ableitung')
mc('q11-mc-23', r"Wie viele Lösungen \(y:[0,+\infty[\,\to\mathbb R\) hat das AWP \(y'=\sqrt y\), \(y(0)=0\)?",
   ['Unendlich viele', 'Genau eine', 'Genau zwei', 'Keine'], 0,
   r"Z. B. \(\psi=0\), \(\left(\frac x2\right)^2\) und für jedes \(c<0\) die Funktion, die bis \(-c\) null ist und danach \(\left(\frac{x+c}2\right)^2\).", 'Bsp. 11.12 2', 'nicht eindeutig unendlich viele Lösungen')
mc('q11-mc-24', r"\(g\) sei stetig differenzierbar und \(g(y_0)=0\). Was ist die Lösung des AWP \(y'=h(x)\,g(y)\), \(y(x_0)=y_0\)?",
   [r"Die konstante Funktion \(\varphi(x)=y_0\) auf \(I\)", r"Die Nullfunktion", r"\(\varphi(x)=Q^{-1}(H(x)+c_0)\)", 'Es gibt keine Lösung'], 0,
   'Für g(y₀) ≠ 0 nimmt man dagegen die Trennung der Variablen.', 'Satz 11.11', 'konstante Lösung stetig differenzierbar')

# ------------------------------------------------------------ Richtig / Falsch
tf('q11-tf-01', r"Die Differentialgleichung \(u'=\alpha\cdot u\) hat genau eine Lösung.", False,
   r"Sie hat unendlich viele Lösungen \(c\cdot e^{\alpha t}\); erst ein Anfangswert legt die Lösung fest.", 'Bem. 11.1 d)', 'unendlich viele Lösungen')
tf('q11-tf-02', r"Eine Lösung von \(y'=f(x,y)\) ist nach Definition auf einem <b>Intervall</b> definiert.", True,
   r"\(\varphi:D_\varphi\to\mathbb R\) auf dem Definitionsintervall \(D_\varphi\subseteq\mathbb R\).", 'Def. 11.2 (2)', 'Definitionsintervall')
tf('q11-tf-03', r"Eine Lösung heißt maximal, wenn sie auf ganz \(\mathbb R\) definiert ist.", False,
   r"Maximal heißt: keine echte Fortsetzung ist ebenfalls Lösung. Z. B. ist \(\frac1{3-x^2}\) auf \(]-\sqrt3,\sqrt3[\) maximal.", 'Def. 11.2 (3)', 'maximal', warn=True)
tf('q11-tf-04', r"Die Lösung eines Anfangswertproblems ist nach Definition immer eine maximale Lösung.", True,
   r"Def.: maximale Lösung \(\varphi\) mit \(\varphi(x_0)=y_0\).", 'Def. 11.2 (5)', 'Anfangswertproblem maximal')
tf('q11-tf-05', r"Für \(y'=\alpha\cdot y\) mit \(y>0\) (also \(U=I\times\mathbb R^+\)) ist \(c\cdot e^{\alpha x}\) für <b>jedes</b> \(c\in\mathbb R\) eine Lösung.", False,
   r"Nur für \(c\in\mathbb R^+\): Der Graph muss in \(U\) liegen.", 'Bsp. 11.3', 'Wachstum Lösung c positiv', warn=True)
tf('q11-tf-06', r"\(y'-a(x)\cdot y=0\) mit stetigem \(a\) ist eine homogene lineare Differentialgleichung.", True,
   r"Das ist \(y'=a(x)\cdot y\), also \(b\) = Nullfunktion.", 'Def. 11.4', 'homogen')
tf('q11-tf-07', r"In der allgemeinen Lösung \(c\cdot e^{A(x)}\) der homogenen linearen DGL \(y'=a(x)y\) darf \(c\) jede reelle Zahl sein, auch \(0\).", True,
   r"\(c\in\mathbb R\); für \(c=0\) erhält man die Nullfunktion.", 'Satz 11.5 (1)', 'homogen Konstante')
tf('q11-tf-08', r"Die allgemeine Lösung der inhomogenen linearen DGL ist die Summe einer partikulären Lösung und der allgemeinen Lösung der zugehörigen homogenen DGL.", True,
   r"\(\varphi_p+\varphi_c\) mit \(\varphi_c(x)=c\cdot e^{A(x)}\), \(c\in\mathbb R\).", 'Satz 11.5 (2)', 'partikulär homogen')
tf('q11-tf-09', r"Jede maximale Lösung der linearen DGL \(y'=a(x)y+b(x)\) mit stetigen \(a,b\) auf dem Intervall \(I\) ist auf ganz \(I\) definiert.", True,
   r"Sie hat die Form \(\varphi:I\to\mathbb R,\ \varphi(x)=u(x)e^{A(x)}\).", 'Satz 11.5 (3)', 'linear Definitionsbereich')
tf('q11-tf-10', r"Bei der Variation der Konstanten ersetzt man die Konstante \(c\) in \(c\cdot e^{A(x)}\) durch eine differenzierbare Funktion \(u(x)\).", True,
   r"Ansatz \(\varphi(x)=u(x)\cdot e^{A(x)}\), dann \(u'(x)=b(x)e^{-A(x)}\).", 'Satz 11.5 / Bsp. 11.6', 'Variation der Konstanten')
tf('q11-tf-11', r"Die homogene lineare DGL \(y'=h(x)\cdot y\) ist ein Spezialfall einer DGL mit getrennten Variablen.", True,
   r"Mit \(g(y)=y\) und \(J=\mathbb R\).", 'Def. 11.7 (2)', 'Spezialfall getrennte Variablen')
tf('q11-tf-12', r"Bei der DGL mit getrennten Variablen \(y'=h(x)g(y)\) mit nullstellenfreiem \(g\) kann das maximale Definitionsintervall der Lösung echt kleiner als \(I\) sein.", True,
   r"Beispiel: \(y'=2xy^2\), \(y(1)=\frac12\) mit \(I=\mathbb R\), aber Lösung nur auf \(]-\sqrt3,\sqrt3[\).", 'Satz 11.9', 'Definitionsintervall echt enthalten')
tf('q11-tf-13', r"Die maximale Lösung von \(y'=2xy^2\) mit \(y(1)=\frac12\) ist auf ganz \(\mathbb R\) definiert.", False,
   r"\(\varphi_1(x)=\frac1{3-x^2}\) nur auf \(]-\sqrt3,\sqrt3[\).", 'Bsp. 11.10', 'Definitionsintervall')
tf('q11-tf-14', r"Die Nullfunktion \(\psi(x)=0\) ist eine maximale Lösung von \(y'=2xy^2\).", True,
   r"\(g(y)=y^2\) hat die Nullstelle \(y=0\).", 'Bsp. 11.10', 'konstante Lösung Nullstelle')
tf('q11-tf-15', r"Bei \(y'+(y+3)(y+2)=0\) kann der Graph einer nicht konstanten Lösung die Gerade \(y=-2\) schneiden.", False,
   'Sonst gäbe es durch den Schnittpunkt mehr als eine maximale Lösung (g ist stetig differenzierbar).', 'Bsp. 11.12 1', 'konstante Lösung schneiden Eindeutigkeit')
tf('q11-tf-16', r"Bei \(y'+(y+3)(y+2)=0\) sind die Lösungen mit \(-3<y<-2\) auf ganz \(\mathbb R\) definiert.", True,
   r"\(\varphi_c(x)=-\frac{2e^{x+c}+3}{1+e^{x+c}}\) auf \(\mathbb R\); die anderen nur auf \(]-\infty,-c[\) oder \(]-c,+\infty[\).", 'Bsp. 11.12 1', 'autonom Definitionsbereich')
tf('q11-tf-17', r"Das AWP \(y'=\sqrt y\), \(y(0)=0\) hat auf \([0,+\infty[\) genau eine Lösung.", False,
   r"Unendlich viele, z. B. \(0\) und \(\left(\frac x2\right)^2\). \(g(y)=\sqrt y\) ist in \(0\) nicht differenzierbar.", 'Bsp. 11.12 2', 'nicht eindeutig', warn=True)
tf('q11-tf-18', r"Nach dem Existenzsatz von Peano ist bei stetigem \(f\) die maximale Lösung des AWP bereits eindeutig.", False,
   r"Peano liefert nur <b>mindestens eine</b>; eindeutig erst, wenn zusätzlich \(\partial_yf\) existiert und stetig ist.", 'Satz 11.13', 'Peano Eindeutigkeit', warn=True)
tf('q11-tf-19', r"Im Existenz- und Eindeutigkeitssatz für \(y'=f(x,y)\) wird \(U\subseteq\mathbb R^2\) als <b>offene</b> Teilmenge vorausgesetzt.", True,
   r"\(\emptyset\ne U\subseteq\mathbb R^2\) offen mit \((x_0,y_0)\in U\).", 'Satz 11.13', 'offen Voraussetzung')
tf('q11-tf-20', r"Ist \(g\) stetig differenzierbar und \(g(y_0)=0\), so ist die Lösung des AWP \(y'=h(x)g(y)\), \(y(x_0)=y_0\) die konstante Funktion \(\varphi(x)=y_0\).", True,
   r"Auf ganz \(I\) definiert.", 'Satz 11.11', 'konstante Lösung')

# ------------------------------------------------------------ Lückentext
gap('q11-gap-01', r"Eine Lösung, zu der es keine echte Fortsetzung gibt, die ebenfalls Lösung ist, heißt {{maximal|maximale}}.",
    r"Die Menge aller dieser Lösungen ist die allgemeine Lösung.", 'Def. 11.2 (3)', 'maximal')
gap('q11-gap-02', r"Die Menge aller maximalen Lösungen einer Differentialgleichung heißt {{allgemeine}} Lösung.",
    '', 'Def. 11.2 (4)', 'allgemeine Lösung')
gap('q11-gap-03', r"Eine maximale Lösung \(\varphi\) mit \(\varphi(x_0)=y_0\) heißt Lösung des {{Anfangswertproblems|Anfangswertproblem|AWP}} bzw. der {{Anfangswertaufgabe}}.",
    '', 'Def. 11.2 (5)', 'Anfangswertproblem Anfangswertaufgabe')
gap('q11-gap-04', r"Die lineare DGL \(y'=a(x)y+b(x)\) heißt {{homogen}}, wenn \(b\) die Nullfunktion ist, und sonst {{inhomogen}}.",
    '', 'Def. 11.4', 'homogen inhomogen')
gap('q11-gap-05', r"Eine einzelne Lösung \(\varphi_p\) der inhomogenen linearen DGL heißt {{partikuläre|partikulär}} Lösung.",
    r"Allgemeine Lösung: \(\varphi_p+c\cdot e^{A(x)}\).", 'Satz 11.5 / Beweis', 'partikulär')
gap('q11-gap-06', r"Den Ansatz \(\varphi(x)=u(x)\cdot e^{A(x)}\) mit differenzierbarem \(u\) nennt man {{Variation der Konstanten}}.",
    r"Er führt auf \(u'(x)=b(x)\,e^{-A(x)}\).", 'Bsp. 11.6', 'Variation der Konstanten')
gap('q11-gap-07', r"Eine DGL der Form \(y'=h(x)\cdot g(y)\) mit stetigen \(h,g\) heißt Differentialgleichung mit {{getrennten Variablen|getrennten}}.",
    '', 'Def. 11.7', 'getrennte Variablen')
gap('q11-gap-08', r"Eine DGL der Form \(y'=g(y)\) heißt {{autonom|autonome}} Differentialgleichung.",
    r"Spezialfall von \(y'=h(x)g(y)\) mit \(h(x)=1\).", 'Def. 11.7 (3)', 'autonom')
gap('q11-gap-09', r"Die konstanten Lösungen einer autonomen DGL \(y'=g(y)\) entsprechen genau den {{Nullstellen}} von \(g\).",
    '', 'Bsp. 11.12 1', 'konstante Lösungen Nullstellen')
gap('q11-gap-10', r"Ist \(f\) stetig, so existiert nach dem Existenzsatz von {{Peano}} mindestens eine maximale Lösung des Anfangswertproblems.",
    'Giuseppe Peano (1858–1922).', 'Satz 11.13 (1)', 'Peano')
gap('q11-gap-11', r"Bei der Trennung der Variablen hat \(Q'=\frac1g\) keine Nullstelle; daher ist \(Q\) streng {{monoton}} und damit {{umkehrbar|invertierbar}}.",
    r"Dann \(\varphi(x)=Q^{-1}(H(x)+c_0)\).", 'Satz 11.9', 'streng monoton umkehrbar')
