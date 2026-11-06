# Querschnitt · Kapitel 10 – Grundlegende Eigenschaften von Funktionen mehrerer Veränderlicher
# Formeln als TeX in \( \); Lücken als {{Antwort|Alternative}}.
ITEMS = []

def mc(id, q, options, correct, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, type='mc', q=q, options=options, correct=correct, expl=expl, src=src, kw=kw, warn=warn))

def tf(id, statement, answer, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=src, kw=kw, warn=warn))

def gap(id, text, expl, src, kw):
    ITEMS.append(dict(id=id, type='gap', text=text, expl=expl, src=src, kw=kw))

# ------------------------------------------------------------ Multiple Choice
mc('q-mc-01', r'Was ist die <b>Niveaumenge</b> \(N_f(c)\) einer Funktion \(f:D\to\mathbb R\)?',
   [r'\(\{x\in D\mid f(x)=c\}\)', r'\(\{f(x)\mid x\in D\}\)', r'\(\{(x,f(x))\mid x\in D\}\)', r'\(\{x\in D\mid f(x)\ge c\}\)'], 0,
   r'Die Menge \(\{f(x)\mid x\in D\}\) ist die <b>Wertemenge</b> \(W_f\), die dritte ist der <b>Graph</b>. Für \(n=2\) heißt \(N_f(c)\) Höhenlinie.',
   'Def. 10.1 (4)', 'Niveaumenge Höhenlinie Niveaulinie Wertemenge Graph')

mc('q-mc-02', r'In welchem Raum liegt der Graph \(G_f\) einer Funktion \(f:D\to\mathbb R\) mit \(D\subseteq\mathbb R^n\)?',
   [r'\(\mathbb R^{n}\)', r'\(\mathbb R^{n+1}\)', r'\(\mathbb R^{n-1}\)', r'\(\mathbb R^{2n}\)'], 1,
   r'\(G_f=\{(x,y)\mid x\in D,\ y=f(x)\}\subseteq\mathbb R^{n+1}\). Für \(n=2\) ist das eine Fläche im \(\mathbb R^3\).',
   'Def. 10.1 (2)', 'Graph Fläche R^3')

mc('q-mc-03', r'Was ist die Höhenlinie von \(f(x_1,x_2)=x_1^2+x_2^2\) zum Niveau \(c=4\)?',
   [r'Kreis um \((0,0)\) mit Radius \(2\)', r'Kreis um \((0,0)\) mit Radius \(4\)', 'leere Menge', r'nur der Punkt \((0,0)\)'], 0,
   r'\(x_1^2+x_2^2=4\) ist der Kreis mit Radius \(\sqrt4=2\). Allgemein: \(c>0\) Kreis mit Radius \(\sqrt c\), \(c=0\) nur \(\{(0,0)\}\), \(c<0\) leer.',
   'Beispiel 10.2 (1)', 'Höhenlinie Kreis Paraboloid Niveau')

mc('q-mc-04', r'Wie lautet die Wertemenge von \(f(x_1,x_2)=x_1^2+x_2^2\) auf \(\mathbb R^2\)?',
   [r'\(\mathbb R_0^+=[0,\infty[\)', r'\(\mathbb R\)', r'\(]0,\infty[\)', r'\([1,\infty[\)'], 0,
   r'Die Wertemenge besteht aus allen \(c\) mit \(N_f(c)\neq\emptyset\), also \(c\ge0\). Der Wert \(0\) wird in \((0,0)\) angenommen.',
   'Beispiel 10.2 (1)', 'Wertemenge Wertebereich')

mc('q-mc-05', r'Was gilt für eine lokale Extremstelle \(a\) im <b>Innern</b> von \(D\), wenn \(f\) in \(a\) partiell differenzierbar ist?',
   [r'\(\operatorname{grad}f(a)=0\)', r'\(\operatorname{Hess}f(a)\) ist positiv definit', r'\(f(a)=0\)', r'\(\partial_1f(a)>0\)'], 0,
   r'Das ist die <b>notwendige</b> Bedingung 1. Ordnung (Satz 10.13). Sie ist nicht hinreichend: \(x_1^2-x_2^2\) hat in \((0,0)\) einen Sattelpunkt.',
   'Satz 10.13', 'notwendige Bedingung Gradient Null kritischer Punkt Extremstelle')

mc('q-mc-06', r'Wie lautet der Gradient von \(f(x_1,x_2)=2x_1x_2\)?',
   [r'\((2x_2,\ 2x_1)\)', r'\((2x_1,\ 2x_2)\)', r'\((x_2,\ x_1)\)', r'\((2,\ 2)\)'], 0,
   r'\(\partial_1f=2x_2\) (nach \(x_1\) ableiten, \(x_2\) festhalten) und \(\partial_2f=2x_1\).',
   'Beispiel 10.12 (2)', 'Gradient partielle Ableitung')

mc('q-mc-07', r'Wie lautet die Hessematrix von \(f(x_1,x_2)=x_1^2+x_2^2\)?',
   [r'\(\begin{pmatrix}2&0\\0&2\end{pmatrix}\)', r'\(\begin{pmatrix}2x_1&0\\0&2x_2\end{pmatrix}\)', r'\(\begin{pmatrix}0&2\\2&0\end{pmatrix}\)', r'\(\begin{pmatrix}1&1\\1&1\end{pmatrix}\)'], 0,
   r'\(\partial_1\partial_1f=2\), \(\partial_2\partial_2f=2\), gemischte Ableitungen \(0\). Die Matrix ist positiv definit.',
   'Beispiel 10.16 (1)', 'Hessematrix zweite Ableitungen')

mc('q-mc-08', r'Eine symmetrische \(2\times2\)-Matrix hat \(\det(A)<0\). Was folgt?',
   ['positiv definit', 'negativ definit', 'indefinit', 'semidefinit, aber nicht definit'], 2,
   r'\(\det<0\) heißt: ein positiver und ein negativer Eigenwert, also <b>indefinit</b>. Bei \(\det>0\) entscheidet die Spur: \(>0\) positiv definit, \(<0\) negativ definit.',
   'Bem. 10.17 (2)', 'definit indefinit Determinante Spur Eigenwerte')

mc('q-mc-09', r'Am kritischen Punkt \(a\) gilt \(\operatorname{Hess}f(a)=\begin{pmatrix}2&1\\1&2\end{pmatrix}\). Was ist \(a\)?',
   ['isolierte lokale Minimalstelle', 'isolierte lokale Maximalstelle', 'Sattelpunkt', 'keine Aussage möglich'], 0,
   r'\(\det=3>0\) und Spur \(=4>0\), also positiv definit. Nach Satz 10.18 a) ist \(a\) eine isolierte lokale Minimalstelle.',
   'Satz 10.18, Beispiel 10.19 (4)', 'Hessematrix positiv definit Minimum Determinante Spur')

mc('q-mc-10', r'An einem kritischen Punkt gilt \(\det(\operatorname{Hess}f(a))=0\). Was folgt aus Satz 10.18?',
   [r'keine Aussage, man muss die Funktionswerte in Umgebungen untersuchen', r'\(a\) ist ein Sattelpunkt', r'\(a\) ist eine lokale Minimalstelle', r'\(a\) ist eine lokale Maximalstelle'], 0,
   r'Die Hessematrix ist dann semidefinit, Satz 10.18 greift nicht. Beispiel 10.19 (5): bei \(2x^2+2y^2-4xy-x^4-y^4\) liefern \(f(t,t)<0\) und \(f(t,-t)>0\), also kein Extremum in \((0,0)\).',
   'Beispiel 10.19 (5)', 'Hessematrix Determinante null semidefinit keine Aussage', warn=True)

mc('q-mc-11', r'Welche Voraussetzungen hat der <b>Satz von Weierstraß</b> für Funktionen mehrerer Veränderlicher?',
   [r'\(f\) stetig und \(D\neq\emptyset\) kompakt', r'\(f\) differenzierbar und \(D\) offen', r'\(f\) stetig und \(D\) zusammenhängend', r'\(f\) beschränkt und \(D\) abgeschlossen'], 0,
   r'Dann nimmt \(f\) Maximum und Minimum an, und \(W_f\) ist kompakt. Ist \(D\) zusätzlich zusammenhängend, gilt \(W_f=[f(p),f(q)]\).',
   'Bem. 10.9 (2)', 'Weierstraß Satz kompakt stetig Maximum Minimum')

mc('q-mc-12', r'Was bedeutet „kompakt“ für Teilmengen des \(\mathbb R^n\)?',
   ['beschränkt und abgeschlossen', 'offen und beschränkt', 'nur abgeschlossen', 'zusammenhängend'], 0,
   r'Beispiele: abgeschlossene Kreisscheibe, Einheitskreislinie, abgeschlossenes Quadrat. Die <i>offene</i> Kreisscheibe ist nicht kompakt, dort kann das Minimum fehlen.',
   'Kap. 9 / Bem. 10.9', 'kompakt beschränkt abgeschlossen Heine Borel')

mc('q-mc-13', r'Sei \(f(x_1,x_2)=\dfrac{2x_1x_2}{x_1^2+x_2^2}\) für \((x_1,x_2)\neq(0,0)\) und \(f(0,0)=0\). Welche Aussage stimmt?',
   [r'\(f\) ist in \((0,0)\) stetig', r'\(f\) ist in \((0,0)\) unstetig, aber partiell differenzierbar', r'\(f\) ist in \((0,0)\) nicht partiell differenzierbar', r'\(f\) ist stetig partiell differenzierbar'], 1,
   r'Längs der Achsen ist \(f=0\), also \(\partial_1f(0,0)=\partial_2f(0,0)=0\). Längs \((t,t)\) ist \(f=1\ne0\): unstetig. Partiell differenzierbar heißt also <b>nicht</b> stetig.',
   'Beispiel 10.8 (3), 10.12 (6)', 'unstetig partiell differenzierbar Winkelhalbierende Gegenbeispiel', warn=True)

mc('q-mc-14', r'Für \(f(x_1,x_2)=\dfrac{x_1^2x_2}{x_1^4+x_2^2}\), \(f(0,0)=0\): Längs welcher Kurve zeigt man die Unstetigkeit in \(0\)?',
   ['längs jeder Geraden durch den Ursprung', 'längs der Koordinatenachsen', r'längs der Parabel \(x_2=x_1^2\)', 'längs der Kreislinie um den Ursprung'], 2,
   r'Auf jeder Geraden \(f\to0\), aber \(f(t,t^2)=\frac{t^4}{2t^4}=\frac12\ne0\). Geraden reichen für Stetigkeit nicht, es muss <i>jede</i> Folge \(a_k\to0\) klappen.',
   'Beispiel 10.8 (5)', 'Unstetigkeit Parabel Geraden Folgenkriterium', warn=True)

mc('q-mc-15', r'Welche Kandidaten für Extremstellen von \(f:D\to\mathbb R\) muss man betrachten?',
   [r'Randpunkte, Stellen ohne partielle Differenzierbarkeit, kritische Stellen im Innern', r'nur die kritischen Stellen', r'nur die Randpunkte', r'nur die Eckpunkte von \(D\)'], 0,
   r'Das ist die Zusammenfassung 10.20. Beispiele: \(\sqrt{x_1^2+x_2^2}\) hat sein Minimum in \((0,0)\), wo \(f\) nicht partiell differenzierbar ist; \(x_1^2-x_2^2\) auf dem Quadrat hat Extrema am Rand.',
   'Zusammenfassung 10.20, Bsp. 10.14 (2)', 'Kandidaten Extremstellen Rand kritische Punkte')

mc('q-mc-16', r'Was sagt der <b>Satz von Schwarz</b>?',
   [r'Bei zweimal stetig partiell differenzierbarem \(f\) gilt \(\partial_i\partial_jf=\partial_j\partial_if\)', r'Jede partiell differenzierbare Funktion ist stetig', r'Der Gradient verschwindet an jeder Extremstelle', r'Die Hessematrix ist stets positiv definit'], 0,
   r'Die Hessematrix ist dann symmetrisch: „Auf die Differentiationsreihenfolge kommt es nicht an.“ Ohne stetige zweite Ableitungen kann das scheitern.',
   'Bem. 10.17 (1)', 'Schwarz Symmetrie Hessematrix Differentiationsreihenfolge')

mc('q-mc-17', r'Sei \(g=\operatorname{grad}f(a)\), \(H=\operatorname{Hess}f(a)\) und \(h=x-a\). Wie lautet die <b>quadratische Approximation</b> von \(f\) in \(a\)?',
   [r'\(f(a)+g\cdot h+\tfrac12\,h^{\top}H\,h\)',
    r'\(f(a)+g\cdot h+h^{\top}H\,h\)',
    r'\(f(a)+\tfrac12\,H\cdot h\)',
    r'\(f(a)+g^2\cdot h^2\)'], 0,
   r'Wie das Taylorpolynom 2. Grades in einer Veränderlichen: der Faktor \(\frac12\) gehört vor den Hesse-Term. Am kritischen Punkt (\(g=0\)) fällt der lineare Term weg.',
   'Bem. 10.17 (1b)', 'Taylor quadratische Approximation lineare Approximation Hessematrix')

# ------------------------------------------------------------ Richtig / Falsch
tf('q-tf-01', r'Jede stetige Funktion auf einer nichtleeren kompakten Menge \(D\subseteq\mathbb R^n\) nimmt Maximum und Minimum an.', True,
   r'Das ist der Satz von Weierstraß (Bem. 10.9).', 'Bem. 10.9 (2)', 'Weierstraß kompakt Maximum Minimum')
tf('q-tf-02', r'Ist \(f\) in \(a\) partiell differenzierbar, dann ist \(f\) in \(a\) auch stetig.', False,
   r'Gegenbeispiel: \(f=\frac{2x_1x_2}{x_1^2+x_2^2}\), \(f(0,0)=0\). Überall partiell differenzierbar, in \((0,0)\) unstetig. Erst <i>stetig</i> partiell differenzierbar liefert Stetigkeit.',
   'Beispiel 10.12 (6)', 'partiell differenzierbar stetig Gegenbeispiel', warn=True)
tf('q-tf-03', r'Ist \(f\) stetig partiell differenzierbar, so ist \(f\) stetig.', True,
   r'Satz 10.15 1b). Stetige partielle Ableitungen sind also stärker als bloße Existenz der partiellen Ableitungen.', 'Def. 10.15 (1b)', 'stetig partiell differenzierbar')
tf('q-tf-04', r'Aus \(\operatorname{grad}f(a)=0\) folgt, dass \(a\) eine lokale Extremstelle ist.', False,
   r'Die Bedingung ist nur notwendig. Für \(f=x_1^2-x_2^2\) ist \(\operatorname{grad}f(0,0)=0\), aber \((0,0)\) ist ein Sattelpunkt.',
   'Beispiel 10.14 (1b)', 'Sattelpunkt kritischer Punkt hinreichend notwendig', warn=True)
tf('q-tf-05', r'Die Funktion \(f(x_1,x_2)=\sqrt{x_1^2+x_2^2}\) ist in \((0,0)\) partiell differenzierbar.', False,
   r'Auf den Achsen ist \(f=|x_1|\) bzw. \(|x_2|\), und der Betrag ist in \(0\) nicht differenzierbar. Trotzdem ist \((0,0)\) eine Minimalstelle.',
   'Beispiel 10.12 (5)', 'Betragsfunktion Kegel nicht differenzierbar')
tf('q-tf-06', r'Der Punkt \((0,0)\) ist eine lokale Extremstelle von \(f(x_1,x_2)=x_1^2-x_2^2\) auf \(\mathbb R^2\).', False,
   r'In jeder Umgebung gibt es Werte \(>0\) (auf der \(x_1\)-Achse) und \(<0\) (auf der \(x_2\)-Achse). Sattelpunkt.',
   'Beispiel 10.4 (2)', 'Sattelpunkt hyperbolisches Paraboloid')
tf('q-tf-07', r'Die Niveaumenge von \(f=x_1^2+x_2^2\) zum Niveau \(c<0\) ist leer.', True,
   r'Eine Summe von Quadraten ist nie negativ.', 'Beispiel 10.2 (1)', 'Niveaumenge leer Höhenlinie')
tf('q-tf-08', r'Strebt \(f(x)\to f(0)\) längs jeder Geraden durch \(0\), so ist \(f\) in \(0\) stetig.', False,
   r'Beispiel 10.8 (5): \(\frac{x_1^2x_2}{x_1^4+x_2^2}\) strebt längs jeder Geraden gegen \(0\), aber längs der Parabel \(x_2=x_1^2\) gegen \(\frac12\).',
   'Beispiel 10.8 (5)', 'Stetigkeit Geraden Parabel Gegenbeispiel', warn=True)
tf('q-tf-09', r'Für zweimal stetig partiell differenzierbares \(f\) ist die Hessematrix symmetrisch.', True,
   r'Satz von Schwarz: \(\partial_i\partial_jf=\partial_j\partial_if\).', 'Bem. 10.17 (1a)', 'Schwarz symmetrisch Hessematrix')
tf('q-tf-10', r'Ist \(a\) kritischer Punkt und \(\operatorname{Hess}f(a)\) indefinit, so ist \(a\) keine lokale Extremstelle.', True,
   r'Satz 10.18 c). Für \(n=2\) ist \(a\) ein Sattelpunkt.', 'Satz 10.18 c)', 'indefinit Sattelpunkt Hessematrix')
tf('q-tf-11', r'Gilt \(\det(\operatorname{Hess}f(a))=0\) an einem kritischen Punkt, so ist \(a\) ein Sattelpunkt.', False,
   r'Dann macht Satz 10.18 keine Aussage. Es kann Minimum, Maximum oder Sattelpunkt sein (z. B. \(x^4\) oder \(-x^4\) mit \(\det=0\)).',
   'Beispiel 10.19 (5)', 'Determinante null keine Aussage', warn=True)
tf('q-tf-12', r'Der Gradient \(\operatorname{grad}f(a)\) einer Funktion \(f:D\to\mathbb R\) ist eine reelle Zahl.', False,
   r'Der Gradient ist ein <b>Vektor</b> im \(\mathbb R^n\): \((\partial_1f(a),\dots,\partial_nf(a))\).', 'Def. 10.11 (2)', 'Gradient Vektor Nabla')
tf('q-tf-13', r'Eine symmetrische \(2\times2\)-Matrix mit \(\det>0\) und \(\operatorname{Spur}<0\) ist negativ definit.', True,
   r'Beide Eigenwerte haben gleiches Vorzeichen (\(\det>0\)) und die Summe ist negativ, also sind beide negativ.', 'Bem. 10.17 (2)', 'negativ definit Determinante Spur')
tf('q-tf-14', r'Die Wertemenge von \(f(x_1,x_2)=x_2^2-x_1\) ist ganz \(\mathbb R\).', True,
   r'Zu jedem \(c\) ist \(N_f(c)\) eine Parabel \(x_1=x_2^2-c\), also nichtleer.', 'Beispiel 10.2 (3)', 'Wertemenge Parabel Höhenlinie')
tf('q-tf-15', r'Jede lokale Maximalstelle ist auch eine globale Maximalstelle.', False,
   r'Lokal heißt nur: größter Wert in einer Umgebung. Global verlangt \(f(x)\le f(a)\) für <i>alle</i> \(x\in D\), also \(f(a)=\max W_f\).',
   'Def. 10.3', 'lokal global Maximalstelle')
tf('q-tf-16', r'Die Bedingung \(\operatorname{grad}f(a)=0\) für Extremstellen gilt auch für Extremstellen \(a\) auf dem Rand von \(D\).', False,
   r'Der Satz gilt nur für <b>innere</b> Punkte. Am Rand kann ein Extremum mit \(\operatorname{grad}f\neq0\) auftreten, z. B. die Ecken von \([-1,1]^2\) bei \(x_1^2+x_2^2\).',
   'Satz 10.13, Beispiel 10.14 (2)', 'Rand innere Punkte Extremstelle', warn=True)
tf('q-tf-17', r'Der Quotient \(\frac fg\) zweier in \(b\) stetiger Funktionen ist stets in \(b\) stetig.', False,
   r'Man braucht \(g(b)\neq0\). Summe, Differenz und Produkt sind immer stetig.', 'Satz 10.7 (1)', 'Stetigkeit Quotient Rechenregeln')
tf('q-tf-18', r'Für \(n=2\) ist der Graph einer Funktion \(f:D\to\mathbb R\) eine Fläche im \(\mathbb R^3\).', True,
   r'\(G_f\subseteq\mathbb R^{n+1}=\mathbb R^3\). Beispiel: \(x_1^2+x_2^2\) liefert ein Rotationsparaboloid.', 'Def. 10.1 (2)', 'Graph Fläche Paraboloid')

# ------------------------------------------------------------ Lückentext
gap('q-gap-01', r'Eine Abbildung \(f:D\to\mathbb R^m\) mit \(D\subseteq\mathbb R^n\) heißt Funktion in \(n\) {{Veränderlichen|Variablen|Veränderlichen}}; die \(f_1,\dots,f_m\) heißen {{Koordinatenfunktionen|Komponenten|Komponentenfunktionen}}.',
    r'Jedes \(f(x)\in\mathbb R^m\) hat \(m\) Komponenten.', 'Def. 10.1 (1)', 'Funktion mehrerer Veränderlicher Koordinatenfunktionen Komponenten')
gap('q-gap-02', r'Die Menge \(N_f(c)=\{x\in D\mid f(x)=c\}\) heißt {{Niveaumenge}}; für \(n=2\) nennt man sie auch {{Höhenlinie|Niveaulinie|Höhenlinien}}.',
    r'Sie entspricht dem Schnitt des Graphen mit der Ebene in Höhe \(c\).', 'Def. 10.1 (4b)', 'Niveaumenge Höhenlinie')
gap('q-gap-03', r'Die Menge \(W_f=\{f(x)\mid x\in D\}\) heißt {{Wertemenge|Wertebereich|Bild}} von \(f\).',
    r'Es gilt \(c\in W_f\iff N_f(c)\neq\emptyset\).', 'Def. 10.1 (4a)', 'Wertemenge Wertebereich Bild')
gap('q-gap-04', r'Der Vektor \((\partial_1f(a),\dots,\partial_nf(a))\) heißt der {{Gradient}} von \(f\) in \(a\); man schreibt auch {{Nabla}} \(f\).',
    r'Schreibweisen: \(\operatorname{grad}f(a)\) oder \(\nabla f(a)\).', 'Def. 10.11 (2)', 'Gradient Nabla')
gap('q-gap-05', r'Ist \(a\) ein innerer Punkt und lokale Extremstelle von \(f\) und ist \(f\) in \(a\) partiell differenzierbar, so gilt \(\operatorname{grad}f(a)=\){{0|Nullvektor|00}}.',
    r'Beweisidee: Auf jeder Koordinatengeraden ist \(a_i\) eine Extremstelle einer Funktion einer Veränderlichen.', 'Satz 10.13', 'Gradient Null Extremstelle notwendige Bedingung')
gap('q-gap-06', r'Die Nullstellen des Gradienten heißen {{kritische Punkte|kritische Stellen|stationäre Punkte|kritischer Punkt}}.',
    r'Sie sind nur <i>Kandidaten</i> für lokale Extremstellen im Innern von \(D\).', 'Beispiel 10.14 (1)', 'kritische Punkte stationäre Punkte')
gap('q-gap-07', r'Die Matrix \((\partial_i\partial_jf(a))_{i,j}\) heißt {{Hessematrix|Hesse-Matrix|Hesse}} von \(f\) in \(a\).',
    r'Benannt nach Otto Hesse. Sie ist nach dem Satz von Schwarz symmetrisch, wenn \(f\) zweimal stetig partiell differenzierbar ist.', 'Def. 10.15 (2b)', 'Hessematrix Hesse')
gap('q-gap-08', r'Bei zweimal stetig partiell differenzierbaren Funktionen kommt es nach dem Satz von {{Schwarz}} nicht auf die {{Differentiationsreihenfolge|Reihenfolge}} an.',
    r'Folge: \(\partial_i\partial_jf=\partial_j\partial_if\).', 'Bem. 10.17 (1a)', 'Schwarz Reihenfolge Hessematrix symmetrisch')
gap('q-gap-09', r'Nach dem Satz von {{Weierstraß|Weierstrass}} nimmt eine stetige Funktion auf einer nichtleeren {{kompakten|kompakt}} Menge Maximum und Minimum an.',
    r'Kompakt \(=\) beschränkt und abgeschlossen.', 'Bem. 10.9 (2)', 'Weierstraß kompakt')
gap('q-gap-10', r'Eine symmetrische \(2\times2\)-Matrix mit \(\det<0\) ist {{indefinit}}; mit \(\det>0\) und \(\operatorname{Spur}>0\) ist sie {{positiv definit}}.',
    r'Mit \(\det>0\) und \(\operatorname{Spur}<0\) ist sie negativ definit.', 'Bem. 10.17 (2)', 'definit indefinit Determinante Spur')
gap('q-gap-11', r'Ist \(\operatorname{Hess}f(a)\) am kritischen Punkt positiv definit, so ist \(a\) eine isolierte lokale {{Minimalstelle|Minimum}}; ist sie negativ definit, eine isolierte lokale {{Maximalstelle|Maximum}}.',
    r'Satz 10.18 a) und b).', 'Satz 10.18', 'Hessematrix positiv definit negativ definit Minimalstelle Maximalstelle')
gap('q-gap-12', r'Ist \(\operatorname{Hess}f(a)\) indefinit und \(n=2\), so liegt ein {{Sattelpunkt}} vor, insbesondere keine lokale {{Extremstelle|Extremum}}.',
    r'Satz 10.18 c). Beispiel: \(x_1^2-x_2^2\) in \((0,0)\).', 'Satz 10.18 c)', 'Sattelpunkt indefinit')
gap('q-gap-13', r'Kandidaten für Extremstellen sind die {{Randpunkte}} von \(D\), die Stellen ohne partielle Differenzierbarkeit und die {{kritischen Stellen|kritischen Punkte}} im Innern.',
    r'Danach vergleicht man die Funktionswerte in einer Wertetabelle.', 'Zusammenfassung 10.20', 'Kandidaten Extremstellen Rand kritische')
gap('q-gap-14', r'Für \(n=2\) ist der Graph von \(f\) eine {{Fläche}} im \(\mathbb R^3\); \(x_1^2+x_2^2\) liefert ein Rotations{{paraboloid}}.',
    r'\(G_f\subseteq\mathbb R^{n+1}\).', 'Def. 10.1 (2), Beispiel 10.2 (1)', 'Graph Fläche Paraboloid')

DATA = dict(
    subject='Querschnitt', key='quer-k10', title='Querschnitt · Kapitel 10',
    sub='Funktionen mehrerer Veränderlicher: Tests zum Skript', accent='#d9a86c', placeholder=False, items=ITEMS,
)
