# Querschnitt · Rechenschemata (v64)
# Rechenschema „Lineare DGL 1. Ordnung – Variation der Konstanten“.
# Quellen: Zusatzmaterial Tutorium 6, Tutorium 6 (A. 21–24) mit Bearbeitungsvorschlag, Mitschrift des Nutzers.
# Blatt 6 (Übungen) bewusst nicht enthalten (Abgabe des Nutzers).
# Formeln als TeX in \( \) bzw. \[ \]. Platzhalter: <span class="ph">⟨…⟩</span> im Text, \langle\dots\rangle in Formeln.
# Aufgaben-IDs nie ändern, nur anhängen.

PH = lambda t='…': '<span class="ph">⟨' + t + '⟩</span>'

TITLE = 'Lineare DGL 1. Ordnung'
SUB = 'Variation der Konstanten · Fahrplan und Aufgaben zum Aufdecken'

STEPS = [
  dict(n=1, t='Gegeben: Normalform, a, b und Intervall',
       goal=r"DGL auf die Form \(y'=a(x)\cdot y+b(x)\) bringen, \(a\), \(b\) und \(I\) festhalten",
       satz=r'''<p><i>Falls nötig, zuerst umformen:</i> Für alle \(x\in\) ''' + PH('Intervall') + ' gilt ' + PH('Teiler') + r''' \(\neq0\) und damit</p>
\[\begin{aligned}&\langle\text{gegebene DGL}\rangle\\&\iff y'(x)=\langle a(x)\rangle\cdot y(x)\\&\qquad+\langle b(x)\rangle;\end{aligned}\]
<p>folglich ist …</p>
<p>Gegeben ist die inhomogene lineare DGL 1. Ordnung</p>
\[y'=a(x)\cdot y+b(x)\qquad(\ast)\]
<p>mit den stetigen Funktionen</p>
\[a:I\to\mathbb R,\quad a(x)=\langle\dots\rangle\]
<p>und</p>
\[b:I\to\mathbb R,\quad b(x)=\langle\dots\rangle.\]
<p><i>Beim AWP:</i> Wegen der Anfangsbedingung \(y(x_0)=y_0\) wählen wir</p>
\[I=\langle\dots\rangle\]
<p>als maximales Definitionsintervall.</p>
<p><i>Intervall vorgegeben:</i> Das Definitionsintervall \(I\) ist gegeben als ''' + PH('x > 0') + r' bzw. \(I=\langle\dots\rangle\).</p>',
       fall=r'''<p><b>Vor dem Teilen begründen</b>, dass der Teiler nicht 0 ist, z. B. \(\cos(x)>0\) auf \(\left]-\frac{\pi}{2},\frac{\pi}{2}\right[\) oder \(x>0\).</p>
<p><b>Vorzeichen beim Umstellen</b> prüfen: \(x\,y'+3y-5x^2=0\iff y'=-\frac{3}{x}\,y+5x\).</p>
<p><b>Intervall finden:</b> das größte Intervall, auf dem \(a\) und \(b\) stetig sind (Nenner, \(\ln\), \(\tan\)) und das die Anfangsstelle \(x_0\) enthält. Beispiel: \(a(x)=\frac1x\), \(y(-1)=2\) ergibt \(I=\left]-\infty,0\right[\).</p>
<p><b>Parameter vor \(y'\)?</b> Er kann 0 sein: Fallunterscheidung.</p>'''),
  dict(n=2, t='Homogene DGL und Stammfunktion',
       goal=r'Zugehörige homogene DGL notieren und eine Stammfunktion \(A\) von \(a\) angeben',
       satz=r'''<p>Die zugehörige homogene DGL lautet</p>
\[y'=a(x)\cdot y.\qquad(\ast_0)\]
<p>Eine Stammfunktion von \(a:I\to\mathbb R\) ist</p>
\[A:I\to\mathbb R,\quad A(x)=\langle\dots\rangle.\]''',
       fall=r'''<p><b>Betrag auflösen</b> mit dem Vorzeichen auf \(I\) und das dazuschreiben: \(A(x)=\ln(|x-2|)\overset{x<2}{=}\ln(2-x)\), denn für \(x<2\) ist \(|x-2|=-(x-2)=2-x\).</p>
<p><b>Häufige Stammfunktionen:</b></p>
\[\begin{aligned}\int\tfrac{1}{x-k}\,dx&=\ln|x-k|\\\int\tan x\,dx&=-\ln|\cos x|\\\int\ln x\,dx&=x\ln x-x\\\int\tfrac{2x}{1+x^2}\,dx&=\ln(1+x^2)\end{aligned}\]'''),
  dict(n=3, t='Allgemeine Lösung der homogenen DGL',
       goal=r'\(\varphi_c(x)=c\cdot e^{A(x)}\) hinschreiben und vereinfachen',
       satz=r'''<p>Die allgemeine Lösung von \((\ast_0)\) ist damit die Gesamtheit aller</p>
\[\begin{aligned}&\varphi_c:I\to\mathbb R,\\&\varphi_c(x)=c\cdot e^{A(x)}=\langle\dots\rangle,\\&c\in\mathbb R.\end{aligned}\]''',
       fall=r'''<p><b>\(e^{A(x)}\) immer vereinfachen:</b></p>
\[\begin{aligned}e^{\ln(2-x)}&=2-x\\e^{-3\ln x}&=x^{-3}\\e^{-2\ln\cos x}&=(\cos x)^{-2}\\e^{x\ln x-x}&=\left(\tfrac{x}{e}\right)^x\end{aligned}\]
<p>Das „\(c\in\mathbb R\)“ nicht vergessen.</p>'''),
  dict(n=4, t='Partikuläre Lösung (Variation der Konstanten)',
       goal=r'Mit \(\varphi_p(x)=u(x)\cdot e^{A(x)}\) ein \(u\) bestimmen, sodass \(\varphi_p\) die DGL löst',
       satz=r'''<p>Um eine partikuläre Lösung von \((\ast)\) zu finden, wählen wir den Ansatz der Variation der Konstanten</p>
\[\begin{aligned}&\varphi_p:I\to\mathbb R,\\&\varphi_p(x)=u(x)\cdot e^{A(x)}=\langle\dots\rangle,\end{aligned}\]
<p>mit einer differenzierbaren Funktion \(u:I\to\mathbb R\). Für alle \(x\in I\) gilt: \(\varphi_p\) ist eine Lösung von \((\ast)\)</p>
\[\begin{aligned}&\iff\varphi_p'(x)=a(x)\cdot\varphi_p(x)\\&\qquad+b(x)\\&\iff\langle\dots\rangle\\&\iff u'(x)=\langle\dots\rangle.\end{aligned}\]
<p>Für alle \(x\in I\) können wir also</p>
\[u(x)=\langle\dots\rangle\]
<p>wählen, und eine partikuläre Lösung von \((\ast)\) ist damit</p>
\[\varphi_p:I\to\mathbb R,\quad\varphi_p(x)=\langle\dots\rangle.\]''',
       fall=r'''<p><b>Kontrolle:</b> Die Terme mit \(u(x)\) müssen sich wegkürzen, übrig bleibt immer \(u'(x)=b(x)\cdot e^{-A(x)}\). Bleibt \(u(x)\) stehen, liegt ein Rechenfehler vor (meist Produktregel oder \(A\)).</p>
<p><b>„\(\iff\)“ ist Pflicht</b>, „\(\Rightarrow\)“ reicht nicht (Punktabzug).</p>
<p><b>Probe:</b> \(\varphi_p\) in \((\ast)\) einsetzen, die Gleichung muss stimmen.</p>
<p>Beim Integrieren von \(u'\) oft partielle Integration, z. B. \(\int x\cos x\,dx=x\sin x+\cos x\).</p>
<p><b>Parameter in \(u'\)?</b> Prüfen, ob die Stammfunktion für alle Werte gleich ist. Typisch \(u'(x)=e^{mx}\): für \(m\neq0\) und \(m=0\) verschieden, also Fallunterscheidung.</p>'''),
  dict(n=5, t='Allgemeine Lösung',
       goal=r'Nach dem Satz \(\varphi=\varphi_c+\varphi_p\) zusammensetzen',
       satz=r'''<p>Nach dem Satz über die allgemeine Lösung (allgemeine Lösung von \((\ast)\) = allgemeine Lösung von \((\ast_0)\) + eine partikuläre Lösung von \((\ast)\)) ist die allgemeine Lösung von \((\ast)\) letztlich die Gesamtheit aller</p>
\[\begin{aligned}&\varphi:I\to\mathbb R,\\&\varphi(x)=\varphi_c(x)+\varphi_p(x)=\langle\dots\rangle,\\&c\in\mathbb R.\end{aligned}\]''',
       fall=r'''<p><b>Kurzweg</b> (Musterlösung Tut. 21): \(u\) gleich mit Konstante integrieren, \(u(x)=\ldots+c\) mit \(c\in\mathbb R\). Dann ist \(\varphi(x)=u(x)\cdot e^{A(x)}\) sofort die allgemeine Lösung.</p>
<p>Ist nur die allgemeine Lösung gefragt: weiter mit Schritt 7.</p>'''),
  dict(n=6, t='Beim AWP: Konstante bestimmen',
       goal=r'\(c\) aus der Anfangsbedingung ausrechnen',
       satz=r'''<p>Aus der Anfangsbedingung \(y(x_0)=y_0\) folgt nun</p>
\[y_0=\varphi(x_0)\iff\ldots\iff c=\langle\dots\rangle.\]''',
       fall=r'<p><b>Probe:</b> \(\varphi(x_0)\) mit dem gefundenen \(c\) ausrechnen, es muss \(y_0\) herauskommen.</p>'),
  dict(n=7, t='Antwortsatz',
       goal='Zurück zur ursprünglichen Frage und genau sie beantworten',
       satz=r'''<p><i>Maximale Lösung des AWP:</i> Die maximale Lösung des gestellten Anfangswertproblems ist damit</p>
\[\varphi:I\to\mathbb R,\quad\varphi(x)=\langle\dots\rangle.\]
<p><i>Allgemeine Lösung:</i> Die allgemeine Lösung der gegebenen DGL ist damit die Gesamtheit der Funktionen</p>
\[\varphi:I\to\mathbb R,\quad\varphi(x)=\langle\dots\rangle,\]<p>\(c\in\mathbb R\).</p>
<p><i>Weitergehende Frage:</i> Für die Lösung \(\varphi\) gilt also \(\varphi(\mathbb R)=\langle\dots\rangle\). Bzw.: Genau für ''' + PH('Parameter') + ' ∈ ' + PH('Menge') + ' besitzt das AWP eine Lösung mit ' + PH('gefragter Eigenschaft') + '.</p>',
       fall=r'''<p>Die Aufgabenstellung noch einmal lesen: <b>Was war ursprünglich gefragt?</b> Ergebnis immer mit Name, Definitionsbereich und Vorschrift und mit dem konkreten \(I\).</p>
<p>Bei Zusatzfragen ist \(\varphi\) erst das Werkzeug:</p>
<p><b>Wertemenge \(\varphi(\mathbb R)\):</b> Monotonie (Vorzeichen von \(\varphi'\)) und Grenzwerte an den Rändern von \(I\), dann mit dem Zwischenwertsatz begründen.</p>
<p><b>„Für welche Parameter …“:</b> jeden Fall einzeln prüfen und am Ende alle Fälle in <i>einem</i> Antwortsatz zusammenführen.</p>'''),
]

EXTRA = [
  dict(t='Fallunterscheidungen', h=r'''<p>Sobald ein <b>Parameter</b> vorkommt (\(k\), \(a\), \(b\), …), an diesen Stellen prüfen, ob eine Rechnung nur für manche Werte gilt:</p>
<ul>
<li><b>Teilen</b> durch einen Ausdruck mit Parameter (Normalform, Auflösen nach \(c\)): Ist er 0, eigener Fall.</li>
<li><b>Integrieren von \(e^{mx}\):</b> für \(m\neq0\) ist \(\int e^{mx}\,dx=\frac1m e^{mx}\), für \(m=0\) ist \(\int1\,dx=x\).</li>
<li><b>Integrieren von \(x^m\):</b> für \(m\neq-1\) ist es \(\frac{x^{m+1}}{m+1}\), für \(m=-1\) ist es \(\ln|x|\).</li>
<li><b>Betrag auflösen:</b> Das Vorzeichen hängt vom Intervall bzw. von der Anfangsstelle ab.</li>
<li><b>Grenzwerte, Beschränktheit:</b> \(e^{mx}\) für \(x\to\infty\): für \(m<0\) gegen 0, für \(m=0\) gleich 1, für \(m>0\) gegen \(\infty\).</li>
</ul>
<div class="rs-satz"><div class="rs-lbl">Mustersatz</div>
<p>Für alle \(x\in I\) gilt also \(u'(x)=\langle\dots\rangle\). Zur Bestimmung von \(u\) unterscheiden wir zwei Fälle.</p>
<p><b>1. Fall:</b> ''' + PH('Parameter') + ' ≠ ' + PH('Wert') + '. Dann können wir \\(u(x)=\\langle\\dots\\rangle\\) wählen, und …</p>' + r'''
<p><b>2. Fall:</b> ''' + PH('Parameter') + ' = ' + PH('Wert') + '. Dann ist \\(u\'(x)=\\langle\\dots\\rangle\\), und wir können \\(u(x)=\\langle\\dots\\rangle\\) wählen, und …</p></div>' + r'''
<p>Ohne Fallunterscheidung steht im ersten Fall für den Sonderwert eine Division durch 0. Das ist der typische Punktabzug. Ausgerechnet in der Aufgabe „Eigenes Beispiel mit Parameter“.</p>'''),
  dict(t='Sonderfälle', h=r'''<p><b>Homogene DGL (\(b=0\)), Tut. 22:</b> Schritt 4 und 5 entfallen, \(c\) direkt aus der Anfangsbedingung bestimmen.</p>
<div class="rs-satz"><div class="rs-lbl">Mustersatz</div><p>Bei der gegebenen DGL \(y'=a(x)\cdot y\) handelt es sich um die homogene lineare DGL 1. Ordnung mit der stetigen Koeffizientenfunktion \(a:I\to\mathbb R\); damit ist die Gesamtheit der Funktionen \(\varphi_c:I\to\mathbb R\), \(\varphi_c(x)=c\cdot e^{A(x)}=\langle\dots\rangle\), mit \(c\in\mathbb R\) die allgemeine Lösung von \((\ast_0)\).</p></div>
<p><b>\(a\) und \(b\) konstant, Tut. 24:</b> Eine partikuläre Lösung lässt sich raten, oft eine Konstante. Bei \(y'=y+1\) zum Beispiel \(\varphi_p(x)=-1\).</p>
<div class="rs-satz"><div class="rs-lbl">Mustersatz</div><p>Ferner ist offensichtlich die konstante Funktion \(\varphi_p:\mathbb R\to\mathbb R\), \(\varphi_p(x)=\langle\dots\rangle\), eine partikuläre Lösung von \((\ast)\).</p></div>
<p><b>Gestaffeltes System, Tut. 24:</b> Die Gleichung mit nur einer Unbekannten zuerst lösen (mit Anfangswert), das Ergebnis in die andere einsetzen, die dann wieder eine lineare DGL 1. Ordnung ist. Am Ende beide als Vektor angeben: \(\psi:\mathbb R\to\mathbb R^2\).</p>'''),
  dict(t='Formale Regeln', h=r'''<ul>
<li>Funktionen immer mit <b>Name, Definitionsbereich und Vorschrift</b>. Falsch: „\(y=e^x\)“. Richtig: \(y_1:\mathbb R\to\mathbb R\), \(y_1(x)=e^x\).</li>
<li><b>Jeden Schritt als Satz ausschreiben</b>, denn die Sätze sind die Erklärung und zählen.</li>
<li>Umformungsketten mit <b>„\(\iff\)“</b>, nicht mit „\(\Rightarrow\)“.</li>
<li>„für alle \(x\in I\)“ und „\(c\in\mathbb R\)“ dazuschreiben.</li>
<li>\((\ast)\) und \((\ast_0)\) als Namen vergeben und darauf verweisen.</li>
</ul>'''),
]

# Aufgaben: steps = Liste (n, html); n = Nummer des Fahrplan-Schritts
def T(id, src, q, steps, kw=''):
    return dict(id=id, src=src, q=q, steps=[dict(n=n, h=h) for n, h in steps], kw=kw)

TASKS = [
  T('rs-dgl1-t21', 'Tutorium 6 · A. 21 (Staatsexamen Frühjahr 2005)',
    r"<p>Man bestimme die maximale Lösung des Anfangswertproblems</p>\[y'=\frac{1}{x-2}\,y+x^2-2x\]<p>für \(x<2\) mit \(y(1)=\frac32\).</p>",
    [(1, r'''<p>Gegeben ist die inhomogene lineare DGL 1. Ordnung</p>\[y'=a(x)\cdot y+b(x)\qquad(\ast)\]<p>mit den stetigen Funktionen</p>\[a:I\to\mathbb R,\quad a(x)=\frac{1}{x-2}\]<p>und</p>\[b:I\to\mathbb R,\quad b(x)=x^2-2x=x(x-2).\]<p>Mit \(x<2\) aus der Angabe wählen wir</p>\[I=\left]-\infty,2\right[\]<p>als maximales Definitionsintervall.</p>'''),
     (2, r'''<p>Die zugehörige homogene DGL lautet</p>\[y'=a(x)\cdot y.\qquad(\ast_0)\]<p>Eine Stammfunktion von \(a:I\to\mathbb R\) ist</p>\[\begin{aligned}&A:I\to\mathbb R,\\&A(x)=\ln(|x-2|)\overset{x<2}{=}\ln(2-x).\end{aligned}\]'''),
     (3, r'''<p>Die allgemeine Lösung von \((\ast_0)\) ist damit die Gesamtheit aller</p>\[\begin{aligned}&\varphi_c:I\to\mathbb R,\\&\varphi_c(x)=c\cdot e^{\ln(2-x)}=c\cdot(2-x),\\&c\in\mathbb R.\end{aligned}\]'''),
     (4, r'''<p>Um eine partikuläre Lösung von \((\ast)\) zu finden, wählen wir den Ansatz der Variation der Konstanten</p>\[\varphi_p:I\to\mathbb R,\quad\varphi_p(x)=u(x)\cdot(2-x),\]<p>mit einer differenzierbaren Funktion \(u:I\to\mathbb R\). Für alle \(x\in I\) gilt: \(\varphi_p\) ist eine Lösung von \((\ast)\)</p>
\[\begin{aligned}&\iff\varphi_p'(x)=\tfrac{1}{x-2}\cdot\varphi_p(x)\\&\qquad\quad+x^2-2x\\&\iff u'(x)(2-x)-u(x)\\&\qquad=\tfrac{1}{x-2}\,u(x)(2-x)\\&\qquad\quad+x^2-2x\\&\iff u'(x)(2-x)-u(x)\\&\qquad=-u(x)+x^2-2x\\&\iff u'(x)=\frac{x(x-2)}{-(x-2)}=-x.\end{aligned}\]
<p>Für alle \(x\in I\) können wir also \(u(x)=-\tfrac12x^2\) wählen, und eine partikuläre Lösung von \((\ast)\) ist damit</p>\[\varphi_p:I\to\mathbb R,\quad\varphi_p(x)=-\tfrac12x^2(2-x).\]'''),
     (5, r'''<p>Nach dem Satz über die allgemeine Lösung ist die allgemeine Lösung von \((\ast)\) letztlich die Gesamtheit aller</p>\[\begin{aligned}&\varphi:I\to\mathbb R,\\&\varphi(x)=c\,(2-x)-\tfrac12x^2(2-x),\\&c\in\mathbb R.\end{aligned}\]'''),
     (6, r'''<p>Aus der Anfangsbedingung \(y(1)=\frac32\) folgt nun</p>\[\tfrac32=c\cdot1-\tfrac12\cdot1\iff c=2.\]'''),
     (7, r'''<p>Die maximale Lösung des gestellten Anfangswertproblems ist damit</p>\[\varphi:I\to\mathbb R,\quad\varphi(x)=\left(2-\tfrac12x^2\right)(2-x),\]<p>also \(\varphi(x)=4-2x-x^2+\frac12x^3\).</p>''')],
    'Variation der Konstanten Anfangswertproblem maximale Lösung'),

  T('rs-dgl1-zus', 'Zusatzmaterial Tutorium 6 · Beispiel',
    r"<p>Bestimmen Sie die maximale Lösung des Anfangswertproblems</p>\[y'=\frac1x\cdot y+2x\quad\text{mit }y(-1)=2.\]",
    [(1, r'''<p>Gegeben ist die inhomogene lineare DGL 1. Ordnung</p>\[y'=a(x)\cdot y+b(x)\qquad(\ast)\]<p>mit den stetigen Funktionen</p>\[a:I\to\mathbb R,\quad a(x)=\frac1x\]<p>und</p>\[b:I\to\mathbb R,\quad b(x)=2x.\]<p>Wegen der Anfangsbedingung \(y(-1)=2\) wählen wir</p>\[I=\left]-\infty,0\right[\]<p>als maximales Definitionsintervall.</p>'''),
     (2, r'''<p>Die zugehörige homogene DGL lautet</p>\[y'=a(x)\cdot y.\qquad(\ast_0)\]<p>Eine Stammfunktion von \(a:I\to\mathbb R\) ist</p>\[\begin{aligned}&A:I\to\mathbb R,\\&A(x)=\ln(|x|)\overset{x<0}{=}\ln(-x).\end{aligned}\]'''),
     (3, r'''<p>Die allgemeine Lösung von \((\ast_0)\) ist damit die Gesamtheit aller</p>\[\begin{aligned}&\varphi_c:I\to\mathbb R,\\&\varphi_c(x)=c\cdot e^{\ln(-x)}=c\cdot(-x),\\&c\in\mathbb R.\end{aligned}\]'''),
     (4, r'''<p>Um eine partikuläre Lösung von \((\ast)\) zu finden, wählen wir den Ansatz der Variation der Konstanten</p>\[\varphi_p:I\to\mathbb R,\quad\varphi_p(x)=u(x)\cdot(-x),\]<p>mit einer differenzierbaren Funktion \(u:I\to\mathbb R\). Für alle \(x\in I\) gilt: \(\varphi_p\) ist eine Lösung von \((\ast)\)</p>
\[\begin{aligned}&\iff\varphi_p'(x)=\tfrac1x\cdot\varphi_p(x)+2x\\&\iff u'(x)(-x)+u(x)(-1)\\&\qquad=\tfrac1x\,u(x)(-x)+2x\\&\iff u'(x)(-x)-u(x)\\&\qquad=-u(x)+2x\\&\iff u'(x)=-2.\end{aligned}\]
<p>Für alle \(x\in I\) können wir also \(u(x)=-2x\) wählen, und eine partikuläre Lösung von \((\ast)\) ist damit</p>\[\begin{aligned}&\varphi_p:I\to\mathbb R,\\&\varphi_p(x)=-2x\cdot(-x)=2x^2.\end{aligned}\]'''),
     (5, r'''<p>Nach dem Satz über die allgemeine Lösung ist die allgemeine Lösung von \((\ast)\) letztlich die Gesamtheit aller</p>\[\varphi:I\to\mathbb R,\quad\varphi(x)=-c\,x+2x^2,\]<p>\(c\in\mathbb R\).</p>'''),
     (6, r'''<p>Aus der Anfangsbedingung \(y(-1)=2\) folgt nun</p>\[\begin{aligned}&2=-c\cdot(-1)+2\cdot(-1)^2\\&\iff2=c+2\iff c=0.\end{aligned}\]'''),
     (7, r'''<p>Die maximale Lösung des gestellten Anfangswertproblems ist damit</p>\[\varphi:I\to\mathbb R,\quad\varphi(x)=2x^2.\]''')],
    'Variation der Konstanten Anfangswertproblem Betrag'),

  T('rs-dgl1-t22', 'Tutorium 6 · A. 22 (Staatsexamen Herbst 2007)',
    r'''<p>Gegeben sei die Funktion \(a:\left]-1,1\right[\to\mathbb R\),</p>\[a(x)=\frac{1-x}{(1+x)(1+x^2)}.\]
<p>a) Man bestätige, dass \(a(x)=\frac{1}{1+x}-\frac{x}{1+x^2}\) für alle \(x\in\left]-1,1\right[\) gilt, und bestimme damit eine Stammfunktion \(A\) von \(a\).</p>
<p>b) Man löse das Anfangswertproblem \(y'=a(x)\,y\) mit \(y(0)=1\).</p>''',
    [(1, r'''<p>Bei der gegebenen DGL</p>\[y'=a(x)\cdot y\qquad(\ast_0)\]<p>handelt es sich um die <b>homogene</b> lineare DGL 1. Ordnung mit der stetigen Koeffizientenfunktion \(a:I\to\mathbb R\) auf dem gegebenen Intervall \(I=\left]-1,1\right[\). Schritt 4 und 5 entfallen.</p>'''),
     (2, r'''<p>a) Für alle \(x\in I\) gilt</p>\[\begin{aligned}&\frac{1}{1+x}-\frac{x}{1+x^2}\\&=\frac{(1+x^2)-x(1+x)}{(1+x)(1+x^2)}\\&=\frac{1-x}{(1+x)(1+x^2)}=a(x),\end{aligned}\]<p>und wegen \(a(x)=\frac{1}{1+x}-\frac12\cdot\frac{2x}{1+x^2}\) ist</p>\[\begin{aligned}&A:I\to\mathbb R,\\&A(x)=\ln(1+x)-\tfrac12\ln(1+x^2)\\&\qquad=\ln\left(\frac{1+x}{\sqrt{1+x^2}}\right)\end{aligned}\]<p>eine Stammfunktion von \(a\).</p>'''),
     (3, r'''<p>b) Damit ist die Gesamtheit der Funktionen</p>\[\begin{aligned}&\varphi_c:I\to\mathbb R,\\&\varphi_c(x)=c\cdot e^{A(x)}=c\cdot\frac{1+x}{\sqrt{1+x^2}},\\&c\in\mathbb R,\end{aligned}\]<p>die allgemeine Lösung von \((\ast_0)\).</p>'''),
     (6, r'''<p>Aus der Anfangsbedingung \(y(0)=1\) folgt nun</p>\[1=c\cdot\frac{1+0}{\sqrt{1+0^2}}\iff c=1.\]'''),
     (7, r'''<p>Die Lösung des gegebenen Anfangswertproblems ist damit</p>\[\varphi:I\to\mathbb R,\quad\varphi(x)=\frac{1+x}{\sqrt{1+x^2}}.\]''')],
    'homogen Partialbruch Stammfunktion Anfangswertproblem'),

  T('rs-dgl1-t23', 'Tutorium 6 · A. 23 (Staatsexamen Frühjahr 2015)',
    r"<p>Man bestimme für \(x\in\left]-\frac\pi2,\frac\pi2\right[\) die allgemeine Lösung der Differentialgleichung</p>\[y'\cdot\cos(x)-2y\cdot\sin(x)=x.\]",
    [(1, r'''<p>Für alle \(x\in\left]-\frac\pi2,\frac\pi2\right[\) gilt \(\cos(x)>0\) und damit</p>\[\begin{aligned}&y'(x)\cos(x)-2y(x)\sin(x)=x\\&\iff y'(x)=\frac{2\sin(x)}{\cos(x)}\cdot y(x)+\frac{x}{\cos(x)};\end{aligned}\]<p>folglich ist die inhomogene lineare DGL 1. Ordnung</p>\[y'=a(x)\cdot y+b(x)\qquad(\ast)\]<p>mit den stetigen Funktionen</p>\[a:I\to\mathbb R,\quad a(x)=\frac{2\sin(x)}{\cos(x)}\]<p>und</p>\[b:I\to\mathbb R,\quad b(x)=\frac{x}{\cos(x)}\]<p>auf dem gegebenen Intervall \(I=\left]-\frac\pi2,\frac\pi2\right[\) zu betrachten.</p>'''),
     (2, r'''<p>Die zugehörige homogene DGL lautet</p>\[y'=a(x)\cdot y.\qquad(\ast_0)\]<p>Eine Stammfunktion von \(a:I\to\mathbb R\) ist</p>\[\begin{aligned}&A:I\to\mathbb R,\\&A(x)=-2\ln(|\cos(x)|)\\&\qquad\overset{\cos(x)>0}{=}-2\ln(\cos(x)).\end{aligned}\]'''),
     (3, r'''<p>Die allgemeine Lösung von \((\ast_0)\) ist damit die Gesamtheit aller</p>\[\begin{aligned}&\varphi_c:I\to\mathbb R,\\&\varphi_c(x)=c\cdot e^{-2\ln(\cos(x))}\\&\qquad=c\cdot(\cos(x))^{-2},\quad c\in\mathbb R.\end{aligned}\]'''),
     (4, r'''<p>Um eine partikuläre Lösung von \((\ast)\) zu finden, wählen wir den Ansatz der Variation der Konstanten</p>\[\begin{aligned}&\varphi_p:I\to\mathbb R,\\&\varphi_p(x)=u(x)\cdot(\cos(x))^{-2},\end{aligned}\]<p>mit einer differenzierbaren Funktion \(u:I\to\mathbb R\). Wegen</p>\[\begin{aligned}\varphi_p'(x)&=u'(x)(\cos x)^{-2}\\&\quad+u(x)\cdot2(\cos x)^{-3}\sin x\end{aligned}\]<p>gilt für alle \(x\in I\): \(\varphi_p\) ist eine Lösung von \((\ast)\)</p>
\[\begin{aligned}&\iff u'(x)(\cos x)^{-2}\\&\qquad+2u(x)(\cos x)^{-3}\sin x\\&\qquad=\tfrac{2\sin x}{\cos x}\,u(x)(\cos x)^{-2}\\&\qquad\quad+\tfrac{x}{\cos x}\\&\iff u'(x)(\cos x)^{-2}=\tfrac{x}{\cos x}\\&\iff u'(x)=x\cos(x).\end{aligned}\]
<p>Mit partieller Integration ist</p>\[\begin{aligned}&\int x\cos(x)\,dx\\&=x\sin(x)-\int\sin(x)\,dx\\&=x\sin(x)+\cos(x)+C.\end{aligned}\]<p>Für alle \(x\in I\) können wir also \(u(x)=x\sin(x)+\cos(x)\) wählen, und eine partikuläre Lösung von \((\ast)\) ist damit</p>\[\begin{aligned}&\varphi_p:I\to\mathbb R,\\&\varphi_p(x)=\frac{x\sin(x)+\cos(x)}{\cos^2(x)}.\end{aligned}\]'''),
     (5, r'''<p>Nach dem Satz über die allgemeine Lösung ist die allgemeine Lösung von \((\ast)\) letztlich die Gesamtheit aller</p>\[\begin{aligned}&\varphi:I\to\mathbb R,\\&\varphi(x)=\frac{x\sin(x)+\cos(x)+c}{\cos^2(x)},\\&c\in\mathbb R.\end{aligned}\]<p>Kein Anfangswert gegeben, Schritt 6 entfällt.</p>'''),
     (7, r'''<p>Die allgemeine Lösung der gegebenen DGL ist damit die Gesamtheit der Funktionen</p>\[\begin{aligned}&\varphi:\left]-\tfrac\pi2,\tfrac\pi2\right[\to\mathbb R,\\&\varphi(x)=\frac{x\sin(x)+\cos(x)+c}{\cos^2(x)},\\&c\in\mathbb R.\end{aligned}\]''')],
    'Normalform umformen cos tan partielle Integration allgemeine Lösung'),

  T('rs-dgl1-t24', 'Tutorium 6 · A. 24 (Staatsexamen Herbst 2005)',
    r"<p>Man bestimme die Lösung der Anfangswertaufgabe</p>\[y_1'=y_1+y_2,\qquad y_2'=y_2+1\]<p>mit \(y_1(0)=y_2(0)=1\).</p>",
    [(1, r'''<p>Zu betrachten ist das System (I) \(y_1'=y_1+y_2\), (II) \(y_2'=y_2+1\) mit \(y_1(0)=1\) und \(y_2(0)=1\). Gestaffelt: Zuerst (II) lösen, denn dort kommt nur \(y_2\) vor.</p>
<p>(II) ist die inhomogene lineare DGL 1. Ordnung \(y_2'=a(x)\,y_2+b_2(x)\) mit den konstanten Funktionen</p>\[a:\mathbb R\to\mathbb R,\ a(x)=1,\]<p>und</p>\[b_2:\mathbb R\to\mathbb R,\ b_2(x)=1.\]'''),
     (2, r'''<p>Da \(A:\mathbb R\to\mathbb R,\ A(x)=x\) eine Stammfunktion von \(a\) ist, …</p>'''),
     (3, r'''<p>… stellt die Gesamtheit der Funktionen \(\varphi_c:\mathbb R\to\mathbb R,\ \varphi_c(x)=c\,e^{x}\), mit \(c\in\mathbb R\) die allgemeine Lösung der zugehörigen homogenen DGL \(y_2'=y_2\) dar.</p>'''),
     (4, r'''<p>Ferner ist offensichtlich die konstante Funktion \(\varphi_p:\mathbb R\to\mathbb R,\ \varphi_p(x)=-1\), eine partikuläre Lösung von (II) (geraten, \(a\) und \(b_2\) konstant).</p>'''),
     (5, r'''<p>Damit ist die Gesamtheit der Funktionen \(\psi_2:\mathbb R\to\mathbb R,\ \psi_2(x)=c\,e^x-1\), mit \(c\in\mathbb R\) die allgemeine Lösung von (II).</p>'''),
     (6, r'''<p>Wegen \(\psi_2(0)=1\iff c\,e^0-1=1\iff c=2\) erhalten wir</p>\[\psi_2:\mathbb R\to\mathbb R,\quad\psi_2(x)=2e^x-1.\]'''),
     (4, r'''<p><b>Jetzt (I):</b> Eingesetzt ist (I) die inhomogene lineare DGL \(y_1'=a(x)\,y_1+b_1(x)\) mit \(a(x)=1\) und \(b_1(x)=2e^x-1\). Homogen wie oben \(c\,e^x\). Ansatz der Variation der Konstanten \(\psi_1(x)=u(x)\,e^x\) mit differenzierbarem \(u:\mathbb R\to\mathbb R\). Für alle \(x\in\mathbb R\) gilt: \(\psi_1\) ist eine Lösung von (I)</p>
\[\begin{aligned}&\iff u'(x)e^x+u(x)e^x\\&\qquad=u(x)e^x+2e^x-1\\&\iff u'(x)=(2e^x-1)\,e^{-x}\\&\qquad\quad=2-e^{-x}.\end{aligned}\]
<p>Also \(u(x)=2x+e^{-x}+d\) mit \(d\in\mathbb R\) und damit</p>\[\begin{aligned}\psi_1(x)&=\left(2x+e^{-x}+d\right)e^x\\&=(2x+d)\,e^x+1.\end{aligned}\]'''),
     (6, r'''<p>Wegen \(\psi_1(0)=1\iff(2\cdot0+d)\,e^0+1=1\iff d=0\) erhalten wir</p>\[\psi_1:\mathbb R\to\mathbb R,\quad\psi_1(x)=2x\,e^x+1.\]'''),
     (7, r'''<p>Zusammenfassend ist die Lösung der Anfangswertaufgabe</p>\[\psi:\mathbb R\to\mathbb R^2,\]\[\psi(x)=\begin{pmatrix}\psi_1(x)\\\psi_2(x)\end{pmatrix}=\begin{pmatrix}2x\,e^x+1\\2e^x-1\end{pmatrix}.\]''')],
    'System gestaffelt partikuläre Lösung raten konstant'),

  T('rs-dgl1-k', 'Eigenes Beispiel mit Parameter (Fallunterscheidung)',
    r"<p>Man bestimme für \(k\in\mathbb R\) die Lösung des Anfangswertproblems</p>\[y'=y+e^{kx}\quad\text{mit }y(0)=1.\]",
    [(1, r'''<p>Gegeben ist die inhomogene lineare DGL 1. Ordnung \(y'=a(x)\cdot y+b(x)\) \((\ast)\) mit den stetigen Funktionen</p>\[a:\mathbb R\to\mathbb R,\ a(x)=1,\]<p>und</p>\[b:\mathbb R\to\mathbb R,\ b(x)=e^{kx},\]<p>also \(I=\mathbb R\).</p>'''),
     (2, r'''<p>Die zugehörige homogene DGL lautet \(y'=y\) \((\ast_0)\). Eine Stammfunktion von \(a\) ist \(A:\mathbb R\to\mathbb R,\ A(x)=x\).</p>'''),
     (3, r'''<p>Die allgemeine Lösung von \((\ast_0)\) ist damit die Gesamtheit aller \(\varphi_c:\mathbb R\to\mathbb R,\ \varphi_c(x)=c\,e^x\), \(c\in\mathbb R\).</p>'''),
     (4, r'''<p>Ansatz der Variation der Konstanten \(\varphi_p(x)=u(x)\,e^x\) mit differenzierbarem \(u:\mathbb R\to\mathbb R\). Für alle \(x\in\mathbb R\) gilt: \(\varphi_p\) ist eine Lösung von \((\ast)\)</p>
\[\begin{aligned}&\iff u'(x)e^x+u(x)e^x\\&\qquad=u(x)e^x+e^{kx}\\&\iff u'(x)=e^{(k-1)x}.\end{aligned}\]
<p>Zur Bestimmung von \(u\) unterscheiden wir zwei Fälle.</p>
<p><b>1. Fall: \(k\neq1\).</b> Dann können wir \(u(x)=\frac{1}{k-1}e^{(k-1)x}\) wählen, also \(\varphi_p(x)=\frac{1}{k-1}e^{kx}\).</p>
<p><b>2. Fall: \(k=1\).</b> Dann ist \(u'(x)=1\), und wir können \(u(x)=x\) wählen, also \(\varphi_p(x)=x\,e^x\).</p>'''),
     (5, r'''<p>Nach dem Satz über die allgemeine Lösung ist die allgemeine Lösung von \((\ast)\) die Gesamtheit aller \(\varphi:\mathbb R\to\mathbb R\) mit</p>\[\varphi(x)=c\,e^x+\tfrac{1}{k-1}e^{kx}\quad(k\neq1)\]<p>bzw.</p>\[\varphi(x)=c\,e^x+x\,e^x\quad(k=1),\]<p>jeweils \(c\in\mathbb R\).</p>'''),
     (6, r'''<p>Aus der Anfangsbedingung \(y(0)=1\) folgt</p><p>für \(k\neq1\): \(1=c+\frac{1}{k-1}\iff c=\frac{k-2}{k-1}\),</p><p>für \(k=1\): \(1=c\).</p>'''),
     (7, r'''<p>Die Lösung des Anfangswertproblems ist damit \(\varphi:\mathbb R\to\mathbb R\) mit</p>\[\varphi(x)=\tfrac{k-2}{k-1}\,e^{x}+\tfrac{1}{k-1}\,e^{kx}\quad\text{für }k\neq1\]<p>und</p>\[\varphi(x)=(1+x)\,e^{x}\quad\text{für }k=1.\]''')],
    'Fallunterscheidung Parameter Sonderfall Division durch Null'),
]
assert len({t['id'] for t in TASKS}) == len(TASKS)
