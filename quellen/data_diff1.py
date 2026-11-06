# Diff 1 · Kapitel 1 – Folgen und Grenzwerte: Testfragen (MC, Richtig/Falsch, Lückentext)
# Formeln als TeX in \( \); Lücken als {{Antwort|Alternative}} (kein "}}" direkt nach TeX-Klammern!).
# Jede Frage muss ohne weiteren Kontext verständlich sein. IDs nie ändern, nur anhängen.
ITEMS = []

def mc(id, q, options, correct, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, type='mc', q=q, options=options, correct=correct, expl=expl, src=src, kw=kw, warn=warn))

def tf(id, statement, answer, expl, src, kw, warn=False):
    ITEMS.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=src, kw=kw, warn=warn))

def gap(id, text, expl, src, kw):
    ITEMS.append(dict(id=id, type='gap', text=text, expl=expl, src=src, kw=kw))

# ------------------------------------------------------------ Multiple Choice
mc('d1-mc-01', r'Welche Beschreibung trifft auf \((\mathbb R,+,\cdot,<)\) zu?',
   ['vollständiger, archimedisch angeordneter Körper', 'endlicher, archimedisch angeordneter Körper', 'vollständiger Körper ohne Anordnung', 'angeordneter Körper, der nicht vollständig ist'], 0,
   r'\(\mathbb R\) ist ein Körper, angeordnet, archimedisch <b>und</b> vollständig. \(\mathbb Q\) wäre angeordnet und archimedisch, aber nicht vollständig.',
   'Bem. 1.0.1', 'reelle Zahlen Körper angeordnet vollständig archimedisch')
mc('d1-mc-02', r'Wie lautet das <b>Archimedische Axiom</b>?',
   [r'\(\forall x,y\in\mathbb R^+\ \exists n\in\mathbb N:\ n\cdot x>y\)', r'\(\exists x,y\in\mathbb R^+\ \forall n\in\mathbb N:\ n\cdot x>y\)', r'\(\forall x\in\mathbb R^+\ \exists n\in\mathbb N:\ n<x\)', r'\(\forall x,y\in\mathbb R^+\ \exists n\in\mathbb N:\ n+x>y\)'], 0,
   r'Oft genug aufaddiert, überholt \(x\) jedes \(y\). Folgerung: Zu jedem \(\varepsilon>0\) gibt es \(n\) mit \(\frac1n<\varepsilon\).',
   'Bem. 1.0.1 (3)', 'Archimedes archimedisches Axiom')
mc('d1-mc-03', r'Was bedeutet „\(\mathbb R\) ist <b>vollständig</b>“?',
   [r'Jede nichtleere, nach oben beschränkte Teilmenge von \(\mathbb R\) hat ein Supremum in \(\mathbb R\)', 'Jede Folge reeller Zahlen ist konvergent', 'Jede Teilmenge von ℝ besitzt ein Maximum', r'Zwischen je zwei reellen Zahlen liegt eine rationale Zahl'], 0,
   r'Entsprechend hat jede nichtleere, nach unten beschränkte Teilmenge ein Infimum in \(\mathbb R\).',
   'Bem. 1.0.1 (4)', 'Vollständigkeit Supremum Infimum')
mc('d1-mc-04', r'Welche Teilmenge von \(\mathbb Q\) hat in \(\mathbb Q\) <b>kein</b> Supremum?',
   [r'\(\{q\in\mathbb Q: q^2<2\}\)', r'\(\{q\in\mathbb Q: 0<q<1\}\)', r'\(\{\frac1n: n\in\mathbb N\}\)', r'\(\{q\in\mathbb Q: q\le5\}\)'], 0,
   r'Das Supremum wäre \(\sqrt2\notin\mathbb Q\). Deshalb ist \(\mathbb Q\) nicht vollständig.',
   'Bem. 1.0.1 (4)', 'Q nicht vollständig Wurzel 2 Supremum Gegenbeispiel')
mc('d1-mc-05', r'Was ist eine <b>Folge</b> reeller Zahlen?',
   [r'Eine Abbildung \(f:\mathbb N\to\mathbb R\)', r'Eine Abbildung \(f:\mathbb R\to\mathbb N\)', 'Eine Menge reeller Zahlen', 'Eine unendliche Summe reeller Zahlen'], 0,
   r'\(a_n=f(n)\) ist das \(n\)-te Folgeglied, \(n\) der Index.', 'Def. 1.0.1', 'Folge Abbildung Folgeglied Index')
mc('d1-mc-06', r'Eine Folge \((a_n)\) heißt <b>monoton fallend</b>, wenn …',
   [r'\(a_n\ge a_{n+1}\) für alle \(n\)', r'\(a_n\le a_{n+1}\) für alle \(n\)', r'\(a_n>a_{n+1}\) für alle \(n\)', r'\(a_n\ge a_1\) für alle \(n\)'], 0,
   r'Mit „\(>\)“ statt „\(\ge\)“ ist sie <i>streng</i> monoton fallend.', 'Def. 1.0.2', 'Monotonie monoton fallend')
mc('d1-mc-07', r'Was weiß man über eine <b>monoton wachsende</b> Folge \((a_n)\) sofort?',
   [r'Sie ist nach unten beschränkt (\(a_n\ge a_1\))', r'Sie ist nach oben beschränkt', 'Sie ist beschränkt', 'Sie ist konvergent'], 0,
   r'Untere Schranke ist \(a_1\). Für „beschränkt“ fehlt noch die obere Schranke.', 'Bem. 1.0.4', 'monoton wachsend nach unten beschränkt')
mc('d1-mc-08', r'Wie lautet die Definition „\((a_n)\) ist <b>beschränkt</b>“ mit dem Betrag?',
   [r'\(\exists N\in\mathbb R_0^+\ \forall n:\ |a_n|\le N\)', r'\(\forall n\ \exists N\in\mathbb R_0^+:\ |a_n|\le N\)', r'\(\exists N\ \exists n:\ |a_n|\le N\)', r'\(\forall N\ \exists n:\ |a_n|>N\)'], 0,
   r'Eine <b>feste</b> Schranke \(N\) für alle \(n\). Bei \(\forall n\ \exists N\) wäre jede Folge „beschränkt“ (wähle \(N=|a_n|\)).',
   'Bem. 1.0.3', 'Beschränktheit Betrag Quantoren', warn=True)
mc('d1-mc-09', r'Wie lautet die Definition „\(a\) ist <b>Grenzwert</b> von \((a_n)\)“?',
   [r'\(\forall\varepsilon>0\ \exists n_0\ \forall n\ge n_0:\ |a_n-a|<\varepsilon\)', r'\(\forall\varepsilon>0\ \forall n_0\ \exists n\ge n_0:\ |a_n-a|<\varepsilon\)', r'\(\exists n_0\ \forall\varepsilon>0\ \forall n\ge n_0:\ |a_n-a|<\varepsilon\)', r'\(\forall\varepsilon>0\ \exists n_0\ \forall n\ge n_0:\ |a_n-a|>\varepsilon\)'], 0,
   r'Die zweite Variante beschreibt nur, dass unendlich viele Glieder nahe \(a\) liegen (Häufungspunkt). Bei der dritten müsste \(n_0\) für alle \(\varepsilon\) gleich sein.',
   'Def. 1.0.4', 'Grenzwert Definition Quantoren Epsilon', warn=True)
mc('d1-mc-10', r'Was bedeutet „<b>fast alle</b> Folgeglieder liegen in der \(\varepsilon\)-Umgebung von \(a\)“?',
   ['Alle bis auf endlich viele', 'Mehr als die Hälfte', 'Unendlich viele', 'Alle bis auf ein einziges'], 0,
   r'Genau das besagt die Grenzwertdefinition: Ab \(n_0\) liegen alle Glieder in der Umgebung, davor höchstens endlich viele nicht.',
   'Bem. 1.0.5', 'fast alle Folgeglieder Umgebung')
mc('d1-mc-11', r'Beweis der Eindeutigkeit des Grenzwerts: Angenommen \(a_n\to a\) und \(a_n\to b\) mit \(a\neq b\). Welches \(\varepsilon\) wählt man?',
   [r'\(\varepsilon=\frac{|a-b|}{2}\)', r'\(\varepsilon=|a-b|\)', r'\(\varepsilon=2|a-b|\)', r'\(\varepsilon=\frac1n\)'], 0,
   r'Dann sind die beiden \(\varepsilon\)-Umgebungen disjunkt, aber fast alle \(a_n\) müssten in beiden liegen. Widerspruch.',
   'Satz 1.0.1', 'Eindeutigkeit Grenzwert Beweis epsilon')
mc('d1-mc-12', r'Welche Folge ist <b>beschränkt, aber divergent</b>?',
   [r'\(a_n=(-1)^n\)', r'\(a_n=n\)', r'\(a_n=\frac1n\)', r'\(a_n=(-1)^n\,n\)'], 0,
   r'Es gilt \(|(-1)^n|\le1\), aber es gibt keinen Grenzwert. \(\frac1n\) konvergiert, die anderen beiden sind unbeschränkt.',
   'Satz 1.0.2', 'beschränkt divergent Gegenbeispiel')
mc('d1-mc-13', r'Es gelten \(a_n\to a\), \(b_n\to b\) und \(a_n<b_n\) für alle \(n\). Was folgt daraus für die Grenzwerte?',
   [r'\(a\le b\)', r'\(a<b\)', r'\(a\ge b\)', r'Es folgt keine Aussage'], 0,
   r'Strikte Ungleichungen werden beim Grenzübergang „weich“. Beispiel: \(0<\frac1n\), aber beide Grenzwerte sind \(0\).',
   'Satz 1.0.3 (1)', 'Ungleichung Grenzübergang kleiner gleich', warn=True)
mc('d1-mc-14', r'Es gilt \(a_n\le c_n\le b_n\) für alle \(n\), und \(a_n\to a\) sowie \(b_n\to a\) (derselbe Grenzwert). Was folgt?',
   [r'\((c_n)\) konvergiert gegen \(a\)', r'\((c_n)\) ist beschränkt, kann aber divergent sein', r'\((c_n)\) konvergiert gegen \(0\)', 'Es folgt nichts über \((c_n)\)'], 0,
   r'Das ist das Schrankenlemma (Sandwich-Lemma, Einschnürungssatz). Die Konvergenz von \((c_n)\) wird gefolgert, nicht vorausgesetzt.',
   'Satz 1.0.3 (2)', 'Schrankenlemma Sandwich Einschnürungssatz')
mc('d1-mc-15', r'Es gelten \(a_n\to a\) und \(b_n\to b\). Welche Zusatzbedingung braucht man für \(\lim\frac{a_n}{b_n}=\frac ab\)?',
   [r'\(b\neq0\)', r'\(a\neq0\)', r'\(b_n>0\) für alle \(n\)', r'Beide Folgen sind monoton'], 0,
   r'Mit \(b\neq0\) ist \(b_n\neq0\) ab einem \(n_0\), und der Quotient konvergiert gegen \(\frac ab\).',
   'Satz 1.0.4', 'Grenzwertsätze Quotient Voraussetzung')
mc('d1-mc-16', r'Wie lautet \(\displaystyle\lim_{n\to\infty}\frac{n^2+1}{2n^2-3}\)?',
   [r'\(\frac12\)', r'\(0\)', r'\(1\)', 'Die Folge divergiert'], 0,
   r'Durch \(n^2\) kürzen: \(\frac{1+1/n^2}{2-3/n^2}\to\frac12\), mit den Grenzwertsätzen und \(\frac1{n^2}\to0\).',
   'Satz 1.0.4', 'Grenzwertsätze Quotient Kürzen')
mc('d1-mc-17', r'Was gilt für die Folge \(a_n=(-1)^n\,n\)?',
   [r'unbeschränkt und divergent, aber nicht bestimmt divergent', r'bestimmt divergent gegen \(+\infty\)', r'bestimmt divergent gegen \(-\infty\)', 'konvergent'], 0,
   r'Die Glieder wechseln das Vorzeichen, daher gibt es weder \(+\infty\) noch \(-\infty\) als bestimmten Grenzwert.',
   'Def. 1.0.6', 'bestimmt divergent unbeschränkt Vorzeichenwechsel')
mc('d1-mc-18', r'Für \(a_n\neq0\) gilt \(\lim a_n=0\iff\) …',
   [r'\(\lim\frac1{|a_n|}=+\infty\)', r'\(\lim\frac1{a_n}=+\infty\)', r'\(\lim\frac1{a_n}=0\)', r'\(\lim|a_n|=+\infty\)'], 0,
   r'Der Betrag ist nötig: \(a_n=\frac{(-1)^n}{n}\to0\), aber \(\frac1{a_n}=(-1)^nn\) ist nicht bestimmt divergent.',
   'Bem. 1.0.9', 'Kehrwert Nullfolge unendlich Betrag', warn=True)
mc('d1-mc-19', r'Für welchen Grenzwert \(a\) folgt aus \(\lim|a_n|=|a|\) auch \(\lim a_n=a\)?',
   [r'Für \(a=0\)', r'Für \(a=1\)', 'Für jedes \\(a\\)', 'Für keines'], 0,
   r'Für \(a=0\) sind \(|a_n|\to0\) und \(a_n\to0\) gleichwertig. Sonst falsch: \(a_n=(-1)^n\) hat \(|a_n|\to1\), ist aber divergent.',
   'Bem. 1.0.8 (2)', 'Betrag Grenzwert Umkehrung')
mc('d1-mc-20', r'Welche Aussage über Konvergenz und Beschränktheit ist richtig?',
   ['Jede konvergente Folge ist beschränkt', 'Jede beschränkte Folge ist konvergent', 'Jede unbeschränkte Folge ist konvergent', 'Jede divergente Folge ist unbeschränkt'], 0,
   r'Gleichwertig (Kontraposition): Jede unbeschränkte Folge ist divergent. Die Umkehrung „beschränkt ⇒ konvergent“ ist falsch.',
   'Satz 1.0.2', 'konvergent beschränkt Kontraposition')

# ------------------------------------------------------------ Richtig / Falsch
tf('d1-tf-01', r'Der Grenzwert einer konvergenten Folge reeller Zahlen ist eindeutig.', True,
   r'Zwei verschiedene Grenzwerte \(a\neq b\) führen zum Widerspruch.', 'Satz 1.0.1', 'Eindeutigkeit Grenzwert')
tf('d1-tf-02', r'Jede beschränkte Folge reeller Zahlen ist konvergent.', False,
   r'Gegenbeispiel: \(a_n=(-1)^n\) ist beschränkt, aber divergent.', 'Satz 1.0.2', 'beschränkt konvergent Gegenbeispiel', warn=True)
tf('d1-tf-03', r'Jede streng monoton wachsende Folge ist auch monoton wachsend.', True,
   r'Aus \(a_n<a_{n+1}\) folgt \(a_n\le a_{n+1}\).', 'Def. 1.0.2', 'streng monoton wachsend')
tf('d1-tf-04', r'Eine monoton fallende Folge ist stets nach oben beschränkt.', True,
   r'Es gilt \(a_n\le a_1\) für alle \(n\), also ist \(a_1\) obere Schranke.', 'Bem. 1.0.4', 'monoton fallend nach oben beschränkt')
tf('d1-tf-05', r'Eine monoton fallende Folge ist stets beschränkt.', False,
   r'Nach oben ja (\(a_n\le a_1\)), aber nach unten nicht unbedingt: \(a_n=-n\) ist monoton fallend und unbeschränkt.', 'Bem. 1.0.4', 'monoton fallend beschränkt Gegenbeispiel', warn=True)
tf('d1-tf-06', r'Aus \(a_n\to a\), \(b_n\to b\) und \(a_n<b_n\) für alle \(n\) folgt \(a<b\).', False,
   r'Nur \(a\le b\) folgt. Gegenbeispiel: \(a_n=0<\frac1n=b_n\), beide Grenzwerte sind \(0\).', 'Bem. 1.0.6', 'Ungleichung Grenzübergang strikt', warn=True)
tf('d1-tf-07', r'In \(\mathbb Q\) besitzt jede nichtleere, nach oben beschränkte Teilmenge ein Supremum in \(\mathbb Q\).', False,
   r'Gegenbeispiel: \(\{q\in\mathbb Q: q^2<2\}\) hat kein Supremum in \(\mathbb Q\). \(\mathbb Q\) ist nicht vollständig.', 'Bem. 1.0.1 (4)', 'Q vollständig Supremum')
tf('d1-tf-08', r'Die Folge \(a_n=n\) ist divergent, obwohl sie „gegen \(+\infty\)“ strebt.', True,
   r'\(+\infty\) ist keine reelle Zahl, also kein Grenzwert im Sinne der Definition. Man sagt: bestimmt divergent.', 'Def. 1.0.5', 'divergent bestimmt divergent unendlich')
tf('d1-tf-09', r'Die Folge \(a_n=(-1)^n\,n\) ist bestimmt divergent.', False,
   r'Sie ist unbeschränkt und divergent, aber springt zwischen positiv und negativ; weder \(+\infty\) noch \(-\infty\) passt.', 'Def. 1.0.6', 'bestimmt divergent Vorzeichenwechsel')
tf('d1-tf-10', r'Aus \(\lim|a_n|=1\) folgt \(\lim a_n=1\).', False,
   r'Gegenbeispiel \(a_n=(-1)^n\): \(|a_n|\to1\), aber \((a_n)\) divergiert. Aus \(a_n\to a\) folgt dagegen \(|a_n|\to|a|\).', 'Bem. 1.0.8 (2)', 'Betrag Grenzwert Umkehrung', warn=True)
tf('d1-tf-11', r'Für jedes feste \(k\in\mathbb N\) ist \(\left(\frac1{n^k}\right)_n\) eine Nullfolge.', True,
   r'Schrankenlemma: \(0\le\frac1{n^k}\le\frac1n\to0\).', 'Bem. 1.0.7', 'Nullfolge Potenz Schrankenlemma')
tf('d1-tf-12', r'Die Summe zweier divergenter Folgen ist stets divergent.', False,
   r'Gegenbeispiel: \(a_n=n\) und \(b_n=-n\) sind divergent, aber \(a_n+b_n=0\) konvergiert. Die Grenzwertsätze setzen <b>konvergente</b> Folgen voraus.', 'Satz 1.0.4', 'Grenzwertsätze Summe divergent Voraussetzung', warn=True)
tf('d1-tf-13', r'In der Grenzwertdefinition darf der Index \(n_0\) von \(\varepsilon\) abhängen.', True,
   r'Die Reihenfolge der Quantoren \(\forall\varepsilon\ \exists n_0\) erlaubt das ausdrücklich. Je kleiner \(\varepsilon\), desto größer wird \(n_0\) meist.', 'Def. 1.0.4', 'Grenzwert Quantoren n0 Epsilon')
tf('d1-tf-14', r'Das Schrankenlemma setzt voraus, dass die eingeschlossene Folge \((c_n)\) konvergiert.', False,
   r'Vorausgesetzt werden nur \(a_n\le c_n\le b_n\) und gleiche Grenzwerte von \((a_n)\), \((b_n)\). Die Konvergenz von \((c_n)\) folgt.', 'Satz 1.0.3 (2)', 'Schrankenlemma Voraussetzung Sandwich')
tf('d1-tf-15', r'Ist eine Folge unbeschränkt, so ist sie divergent.', True,
   r'Kontraposition von „konvergent ⇒ beschränkt“.', 'Satz 1.0.2', 'unbeschränkt divergent Kontraposition')
tf('d1-tf-16', r'Aus \(\lim|b_n|=+\infty\) folgt \(\lim\frac1{b_n}=0\) (für \(b_n\neq0\)).', True,
   r'Wird \(|b_n|\) beliebig groß, wird \(\frac1{|b_n|}\) beliebig klein.', 'Bem. 1.0.9', 'Kehrwert Nullfolge unendlich')
tf('d1-tf-17', r'Zu jedem \(\varepsilon>0\) gibt es ein \(n\in\mathbb N\) mit \(\frac1n<\varepsilon\).', True,
   r'Folgt aus dem Archimedischen Axiom: wähle \(n>\frac1\varepsilon\).', 'Bem. 1.0.1 (3)', 'Archimedes Epsilon 1/n')
tf('d1-tf-18', r'Aus \(a_n\to a\) folgt \(\lim(a_n-a)=0\), und umgekehrt.', True,
   r'In der Definition kommt ohnehin nur \(|a_n-a|\) vor.', 'Bem. 1.0.8 (1)', 'Äquivalenz Grenzwert Nullfolge')

# ------------------------------------------------------------ Lückentext
gap('d1-gap-01', r'\(\mathbb R\) ist ein {{vollständiger}}, {{archimedisch|archimedisch angeordneter}} angeordneter Körper.',
    r'Vier Eigenschaften: Körper, angeordnet, Archimedisches Axiom, vollständig.', 'Bem. 1.0.1', 'reelle Zahlen Körper vollständig archimedisch')
gap('d1-gap-02', r'Die kleinste obere Schranke einer Menge heißt {{Supremum}}, die größte untere Schranke {{Infimum}}.',
    r'In \(\mathbb R\) existieren beide für nichtleere beschränkte Mengen.', 'Bem. 1.0.1 (4)', 'Supremum Infimum')
gap('d1-gap-03', r'Bei einer Folge heißt \(a_n=f(n)\) das \(n\)-te {{Folgeglied|Folgenglied|Glied}} und \(n\) der {{Index}}.',
    r'Eine Folge ist eine Abbildung \(f:\mathbb N\to\mathbb R\).', 'Def. 1.0.1', 'Folge Folgeglied Index')
gap('d1-gap-04', r'Gilt \(a_n\le a_{n+1}\) für alle \(n\), heißt die Folge monoton {{wachsend|steigend}}; gilt sogar \(a_n<a_{n+1}\), heißt sie {{streng}} monoton wachsend.',
    r'Jede streng monotone Folge ist auch monoton.', 'Def. 1.0.2', 'monoton wachsend streng')
gap('d1-gap-05', r'Konvergiert \((a_n)\) gegen \(a\), so liegen in jeder \(\varepsilon\)-Umgebung von \(a\) {{fast}} alle Folgeglieder, also alle bis auf {{endlich}} viele.',
    r'Das ist die anschauliche Form der Grenzwertdefinition.', 'Bem. 1.0.5', 'fast alle endlich Umgebung Grenzwert')
gap('d1-gap-06', r'Eine Folge, die gegen \(0\) konvergiert, heißt {{Nullfolge}}; besitzt sie keinen reellen Grenzwert, heißt sie {{divergent}}.',
    r'\(a_n=n\) ist divergent, obwohl sie bestimmt gegen \(+\infty\) strebt.', 'Def. 1.0.5', 'Nullfolge divergent konvergent')
gap('d1-gap-07', r'Jede konvergente Folge ist {{beschränkt}}. Die Umkehrung gilt nicht: \(a_n=(-1)^n\) ist beschränkt, aber {{divergent}}.',
    r'Beweisidee: Mit \(\varepsilon=1\) gilt ab \(n_0\) die Abschätzung \(|a_n|\le|a|+1\).', 'Satz 1.0.2', 'konvergent beschränkt divergent')
gap('d1-gap-08', r'Gilt \(a_n\le c_n\le b_n\) und haben \((a_n)\) und \((b_n)\) denselben Grenzwert, so konvergiert \((c_n)\) nach dem {{Schrankenlemma|Sandwich-Lemma|Sandwichlemma|Einschnürungssatz|Einschließungssatz}} gegen diesen Grenzwert.',
    r'Anwendung: \(0\le|c_n|\le b_n\) mit \(b_n\to0\) liefert \(c_n\to0\).', 'Satz 1.0.3 (2)', 'Schrankenlemma Sandwich Einschnürungssatz')
gap('d1-gap-09', r'Die Folge \(a_n=n\) ist {{bestimmt}} divergent gegen \(+\infty\); man sagt auch {{uneigentlich}} konvergent.',
    r'Sie hat keinen <i>reellen</i> Grenzwert und ist deshalb im engeren Sinn divergent.', 'Def. 1.0.6', 'bestimmt divergent uneigentlich konvergent')
gap('d1-gap-10', r'Zu jedem \(\varepsilon>0\) gibt es nach dem {{Archimedischen|archimedischen|Archimedes}} Axiom ein \(n\in\mathbb N\) mit \(\frac1n<\varepsilon\).',
    r'Das braucht man ständig bei Grenzwertbeweisen.', 'Bem. 1.0.1 (3)', 'Archimedes Epsilon')
