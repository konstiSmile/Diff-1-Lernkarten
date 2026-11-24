# Diff 1 · Kapitel 2 – Vollständigkeit und Konvergenz (Kurzskript Reichert, S. 8–12)
# Quelle: „2. Vollständigkeit und Konvergenz.pdf“ (ohne rote Markierungen). Nur Inhalte aus dem Skript;
# eigene Ergänzungen sind in den Karten als „Ergänzung“ gekennzeichnet.
# Formeln als TeX in \( \) bzw. \[ \]; Lücken als {{Antwort|Alternative}}. Keys/IDs nie ändern, nur anhängen.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

CARDS = [
    C('hs-monoton', 'Satz 2.0.1',
      r"Wie lautet der <b>Hauptsatz über monotone Folgen</b>?",
      r"""<p><b>1) Monoton wachsende</b> Folge \((a_n)_{n\in\mathbb N}\) reeller Zahlen:</p>
<ul><li>beschränkt ⇒ konvergent gegen \(\sup\{a_n\mid n\in\mathbb N\}\),</li>
<li>unbeschränkt ⇒ bestimmt divergent gegen \(+\infty\).</li></ul>
<p><b>2) Monoton fallende</b> Folge \((a_n)_{n\in\mathbb N}\) reeller Zahlen:</p>
<ul><li>beschränkt ⇒ konvergent gegen \(\inf\{a_n\mid n\in\mathbb N\}\),</li>
<li>unbeschränkt ⇒ bestimmt divergent gegen \(-\infty\).</li></ul>""",
      'Hauptsatz monotone Folgen monoton wachsend fallend beschränkt Supremum Infimum bestimmt divergent'),

    C('bem-vollst-beweis', 'Bem. 2.0.1',
      r"Welche Eigenschaft von \(\mathbb R\) benutzt der Beweis des <b>Hauptsatzes über monotone Folgen</b>?",
      r"""<p>Die <b>Vollständigkeit</b> von \(\mathbb R\): Teilmengen \(M\) von \(\mathbb R\) besitzen ein Supremum und ein Infimum in \(\mathbb R\).</p>
<p>Im Beweis ist \(M=\{a_n\mid n\in\mathbb N\}\subseteq\mathbb R\), und es gilt \(\sup M\in\mathbb R\), \(\inf M\in\mathbb R\).</p>
<div class="tip"><b>Genau genommen</b> (so in Bem. 2.0.10): jede <b>nicht-leere, beschränkte</b> Teilmenge hat Supremum und Infimum. Im Satz ist \(M\) nicht leer, und im Fall „beschränkt“ wird das Supremum bzw. Infimum gebraucht.</div>""",
      'Vollständigkeit Supremum Infimum Beweis monotone Folgen'),

    C('intervallschachtelung', 'Def. 2.0.1',
      r"Was ist eine <b>Intervallschachtelung</b>?",
      r"""<p>Für \(n\in\mathbb N\) und \(a_n,b_n\in\mathbb R\) mit \(a_n\le b_n\) ist \([a_n,b_n]\subseteq\mathbb R\) ein <b>reelles Intervall</b>. Die Folge \(([a_n,b_n])_{n\in\mathbb N}\) heißt <b>Intervallschachtelung</b>, wenn gilt:</p>
<ol><li>\((a_n)_{n\in\mathbb N}\) (untere Grenzen) ist <b>monoton wachsend</b>,</li>
<li>\((b_n)_{n\in\mathbb N}\) (obere Grenzen) ist <b>monoton fallend</b>,</li>
<li>\((b_n-a_n)_{n\in\mathbb N}\) (Intervalllängen) ist eine <b>Nullfolge</b>.</li></ol>""",
      'Intervallschachtelung Intervall monoton wachsend fallend Nullfolge Intervalllänge'),

    C('schachtelung-teilmenge', 'Bem. 2.0.2 (1)',
      r"Wie liegen bei einer Intervallschachtelung \(([a_n,b_n])_{n\in\mathbb N}\) aufeinanderfolgende Intervalle zueinander?",
      r"""<p>Für alle \(n\in\mathbb N\) gilt</p>
\[a_n\le a_{n+1}\le b_{n+1}\le b_n\]
<p>und somit</p>
\[[a_{n+1},b_{n+1}]\subseteq[a_n,b_n].\]
<p>Jedes „nächsthöhere“ Intervall ist also <b>Teilmenge des vorherigen</b>.</p>""",
      'Intervallschachtelung Teilmenge geschachtelt'),

    C('hoechstens-eine', 'Bem. 2.0.2 (2)',
      r"Warum liegt in allen Intervallen einer Intervallschachtelung <b>höchstens eine</b> reelle Zahl? (Begründung)",
      r"""<p>Seien \(r,r'\in\mathbb R\) mit \(r\in\bigcap_{n\in\mathbb N}[a_n,b_n]\) und \(r'\in\bigcap_{n\in\mathbb N}[a_n,b_n]\). Dann gilt für alle \(n\in\mathbb N\):</p>
\[a_n\le r\le b_n\quad\text{und}\quad a_n\le r'\le b_n,\]
<p>also \(|r-r'|\le b_n-a_n\), wobei \(b_n-a_n\to0\) für \(n\to\infty\) (Bedingung 3: die Intervalllängen bilden eine Nullfolge).</p>
<p>Mit dem <b>Schrankenlemma</b> folgt \(|r-r'|\to0\), also \(r=r'\).</p>""",
      'höchstens eine Zahl Schrankenlemma Intervallschachtelung Durchschnitt Eindeutigkeit'),

    C('cantor-dedekind', 'Satz 2.0.2',
      r"Was besagt der Satz über <b>Cantor-Dedekind-Schnitte</b>?",
      r"""<p>Zu jeder Intervallschachtelung \(([a_n,b_n])_{n\in\mathbb N}\) in \(\mathbb R\) existiert <b>genau eine</b> reelle Zahl \(r\in\mathbb R\) mit</p>
\[r\in\bigcap_{n\in\mathbb N}[a_n,b_n].\]""",
      'Cantor Dedekind Schnitte Intervallschachtelung genau eine reelle Zahl'),

    C('grenzwerte-schachtelung', 'Bem. 2.0.3',
      r"Wie hängt die durch eine Intervallschachtelung definierte Zahl \(r\) mit den Folgen \((a_n)\) und \((b_n)\) zusammen? Warum?",
      r"""<p>\(r\) ergibt sich als <b>Grenzwert</b>:</p>
\[\lim_{n\to\infty}a_n=r=\lim_{n\to\infty}b_n.\]
<p><b>Begründung:</b> Nach Definition ist \(r\in\bigcap_{n\in\mathbb N}[a_n,b_n]\), also \(a_n\le r\le b_n\) für alle \(n\in\mathbb N\), und \(b_n-a_n\to0\). Im Grenzwert folgt \(\lim a_n=r=\lim b_n\).</p>
<p>So kann man wichtige reelle Zahlen definieren, z. B. \(\sqrt x\) (Heron-Verfahren) und die Eulersche Zahl \(e\).</p>""",
      'Cantor Dedekind Grenzwert Intervallschachtelung Definition reeller Zahlen'),

    C('heron', 'Bem. 2.0.3 (1)',
      r"Wie definiert man die <b>Quadratwurzel</b> \(\sqrt x\) für \(x\in\mathbb R^+\) als Grenzwert? Wie heißt das Verfahren?",
      r"""<p>Als Limes der rekursiv definierten Folge</p>
\[b_{n+1}=\frac12\left(b_n+\frac{x}{b_n}\right)\]
<p>für beliebigen Startwert \(b_0>0\).</p>
<p>Dieser Algorithmus heißt <b>Heron-Verfahren</b> zur Bestimmung von \(\sqrt x\).</p>""",
      'Heron Verfahren Quadratwurzel rekursiv Startwert Wurzel'),

    C('euler', 'Bem. 2.0.3 (2)',
      r"Wie ist die <b>Eulersche Zahl</b> \(e\) als Grenzwert definiert, und wie \(e^z\) für \(z\in\mathbb Z\)?",
      r"""\[e=\lim_{n\to\infty}\left(1+\frac1n\right)^n.\]
<p>In Verallgemeinerung dazu definiert man \(e^z\) für eine ganze Zahl \(z\in\mathbb Z\) als</p>
\[e^z=\lim_{n\to\infty}\left(1+\frac zn\right)^n.\]""",
      'Eulersche Zahl e Grenzwert Exponential ganze Zahl'),

    C('wurzel-grenzwerte', 'Bem. 2.0.4',
      r"Welche Grenzwerte von <b>\(n\)-ten Wurzeln</b> kann man ebenfalls mit Intervallschachtelung betrachten?",
      r"""<p>Für gegebenes \(x\in\mathbb R^+\):</p>
\[\lim_{n\to\infty}\sqrt[n]{x}=1\]
<p>und insbesondere</p>
\[\lim_{n\to\infty}\sqrt[n]{n}=1.\]""",
      'n-te Wurzel Grenzwert 1 Intervallschachtelung'),

    C('teilfolge', 'Def. 2.0.2, Bsp. 2.0.3',
      r"Was ist eine <b>Teilfolge</b>? Nenne Beispiele.",
      r"""<p>Sei \((a_n)_{n\in\mathbb N}\) eine Folge reeller Zahlen. Ist \((n_k)_{k\in\mathbb N}\) eine <b>streng monoton wachsende</b> Folge von Indizes, so heißt \((a_{n_k})_{k\in\mathbb N}\) eine <b>Teilfolge</b> von \((a_n)_{n\in\mathbb N}\).</p>
<p><b>Beispiele:</b> \((a_{2k-1})_{k\in\mathbb N}\), \((a_{2k})_{k\in\mathbb N}\), \((a_{k^2})_{k\in\mathbb N}\). Auch \((a_k)_{k\in\mathbb N}\) ist selbst eine Teilfolge von \((a_n)_{n\in\mathbb N}\).</p>""",
      'Teilfolge Indizes streng monoton wachsend Beispiele'),

    C('haeufungspunkt', 'Def. 2.0.3',
      r"Wann heißt \(h\in\mathbb R\) ein <b>Häufungspunkt</b> der Folge \((a_n)_{n\in\mathbb N}\)?",
      r"""<p>Wenn es eine Teilfolge \((a_{n_k})_{k\in\mathbb N}\) gibt mit</p>
\[\lim_{k\to\infty}a_{n_k}=h.\]
<div class="tip">Im Skript steht unter dem Limes „\(n\to\infty\)“; gemeint ist der Grenzübergang der Teilfolge, also \(k\to\infty\).</div>""",
      'Häufungspunkt Teilfolge Grenzwert Definition'),

    C('hp-konvergent', 'Bem. 2.0.5',
      r"Was gilt für Häufungspunkte einer <b>konvergenten</b> Folge? Was folgt aus <b>mehr als einem</b> Häufungspunkt?",
      r"""<ol><li>Ist \((a_n)_{n\in\mathbb N}\) konvergent gegen \(a\), so ist \(a\) der <b>einzige</b> Häufungspunkt. Jede Teilfolge \((a_{n_k})_{k\in\mathbb N}\) konvergiert dann gegen \(a\).</li>
<li>Hat \((a_n)_{n\in\mathbb N}\) <b>mehr als einen</b> Häufungspunkt, so ist sie nicht konvergent, sondern <b>divergent</b>.</li></ol>""",
      'Häufungspunkt konvergent einziger divergent mehrere'),

    C('hp-epsilon', 'Satz 2.0.3, Bem. 2.0.6',
      r"Wie lässt sich ein Häufungspunkt mit <b>\(\varepsilon\)-Umgebungen</b> beschreiben? Was ist der Unterschied zum Grenzwert?",
      r"""<p>\(h\in\mathbb R\) ist <b>genau dann</b> ein Häufungspunkt von \((a_n)_{n\in\mathbb N}\), wenn für jedes \(\varepsilon>0\) <b>unendlich viele</b> Folgeglieder \(a_n\) in der \(\varepsilon\)-Umgebung \(]h-\varepsilon,h+\varepsilon[\) um \(h\) liegen.</p>
<div class="tip warn"><b>Unterschied zum Grenzwert:</b> Beim Häufungspunkt dürfen auch <b>unendlich viele</b> Folgeglieder <b>außerhalb</b> der \(\varepsilon\)-Umgebung liegen.</div>""",
      'Häufungspunkt Epsilon Umgebung unendlich viele Folgeglieder außerhalb'),

    C('gw-vs-hp', 'Bem. 2.0.7',
      r"Grenzwert und Häufungspunkt: Welche drei Aussagen sind jeweils <b>äquivalent</b>?",
      r"""<p><b>1. Grenzwert</b> (\((a_n)\) reelle Folge, \(a\in\mathbb R\)):</p>
<ul><li>\(a\) ist der Grenzwert von \((a_n)_{n\in\mathbb N}\).</li>
<li><b>Jede</b> Teilfolge konvergiert gegen \(a\).</li>
<li>In jeder \(\varepsilon\)-Umgebung von \(a\) liegen <b>fast alle</b> (alle bis auf endlich viele) Folgeglieder.</li></ul>
<p><b>2. Häufungspunkt</b> (\(h\in\mathbb R\)):</p>
<ul><li>\(h\) ist ein Häufungspunkt von \((a_n)_{n\in\mathbb N}\).</li>
<li><b>Es gibt eine</b> Teilfolge, die gegen \(h\) konvergiert.</li>
<li>In jeder \(\varepsilon\)-Umgebung von \(h\) liegen <b>unendlich viele</b> Folgeglieder.</li></ul>""",
      'Grenzwert Häufungspunkt Unterschied äquivalent fast alle unendlich viele jede Teilfolge'),

    C('bolzano', 'Satz 2.0.4',
      r"Was besagt der Satz von <b>Bolzano-Weierstraß</b>?",
      r"""<p>Jede <b>beschränkte</b> Folge reeller Zahlen besitzt <b>mindestens einen Häufungspunkt</b>.</p>
<div class="tip">Laut Bem. 2.0.9 verwendet er, dass eine Intervallschachtelung eindeutig ein Element \(r\in\mathbb R\) definiert.</div>""",
      'Bolzano Weierstraß beschränkt Häufungspunkt'),

    C('cauchy', 'Def. 2.0.4, Bem. 2.0.8',
      r"Wann heißt eine Folge \((a_n)_{n\in\mathbb N}\) reeller Zahlen <b>Cauchy-Folge</b>? Was bedeutet das anschaulich?",
      r"""\[\forall\varepsilon>0\ \exists n_0\in\mathbb N\ \forall n,m\ge n_0:\ |a_n-a_m|<\varepsilon.\]
<p><b>Anschaulich:</b> Ab einem bestimmten Index \(n_0\) sind je zwei Folgeglieder \(a_n\) und \(a_m\) weniger als \(\varepsilon\) voneinander entfernt.</p>""",
      'Cauchy-Folge Cauchy Definition Epsilon Quantoren'),

    C('hs-konvergent', 'Satz 2.0.5',
      r"Wie lautet der <b>Hauptsatz über konvergente Folgen</b>?",
      r"""<p>Für eine Folge \((a_n)_{n\in\mathbb N}\) reeller Zahlen sind <b>äquivalent</b>:</p>
<ol><li>\((a_n)_{n\in\mathbb N}\) ist <b>konvergent</b>.</li>
<li>\((a_n)_{n\in\mathbb N}\) ist eine <b>Cauchy-Folge</b>.</li>
<li>\((a_n)_{n\in\mathbb N}\) ist <b>beschränkt</b> und besitzt <b>genau einen</b> Häufungspunkt.</li></ol>""",
      'Hauptsatz konvergente Folgen Cauchy-Folge beschränkt genau ein Häufungspunkt äquivalent'),

    C('beweis-koerper', 'Bem. 2.0.9',
      r"Welche Beweisrichtungen des Hauptsatzes über konvergente Folgen gelten auch in anderen Körpern (z. B. \(\mathbb Q\)), welche nur in \(\mathbb R\)? Warum?",
      r"""<ul><li><b>1) ⇒ 2)</b> (konvergent ⇒ Cauchy) benutzt nicht, dass es eine Folge in \(\mathbb R\) ist; gilt also auch in anderen Körpern, z. B. in \(\mathbb Q\).</li>
<li><b>2) ⇒ 1)</b> (Cauchy ⇒ konvergent; geführt über 2) ⇒ 3) und 3) ⇒ 1)) gilt <b>nur in \(\mathbb R\)</b>: Er benutzt Bolzano-Weierstraß, und dieser verwendet, dass eine Intervallschachtelung eindeutig ein Element \(r\in\mathbb R\) definiert.</li></ul>
<p><b>Kurz:</b> Jede konvergente Folge in einem Körper \(K\) ist eine Cauchy-Folge in \(K\), aber nicht unbedingt umgekehrt. In \(\mathbb R\) gilt die Umkehrung, in \(\mathbb Q\) nicht.</p>""",
      'Beweis Cauchy konvergent Körper Q Bolzano-Weierstraß Umkehrung'),

    C('vollstaendigkeit', 'Def. 2.0.5',
      r"Wann heißt ein archimedisch angeordneter Körper \((K,+,\cdot,<)\) <b>vollständig</b>?",
      r"""<p>Wenn <b>jede Cauchy-Folge in \(K\)</b> einen <b>Grenzwert in \(K\)</b> besitzt.</p>""",
      'Vollständigkeit vollständig Körper Cauchy-Folge Grenzwert Definition'),

    C('vollst-aequivalent', 'Bem. 2.0.10',
      r"Welche <b>drei äquivalenten Formulierungen</b> der Vollständigkeit eines archimedisch angeordneten Körpers \(K\) gibt es?",
      r"""<ol><li>Jede <b>Cauchy-Folge</b> in \(K\) besitzt einen Grenzwert in \(K\).</li>
<li>Jede <b>Intervallschachtelung</b> \(([a_n,b_n])\) von Intervallen in \(K\) definiert genau ein Element \(r\in K\) mit \(r\in\bigcap_{n\in\mathbb N}[a_n,b_n]\).</li>
<li>Jede <b>nicht-leere beschränkte Teilmenge</b> \(M\) von \(K\) besitzt ein Supremum \(\sup M\) in \(K\) und ein Infimum \(\inf M\) in \(K\).</li></ol>""",
      'Vollständigkeit äquivalent Cauchy Intervallschachtelung Supremum Infimum'),

    C('r-vollstaendig', 'Bsp. 2.0.7',
      r"Ist \((\mathbb R,+,\cdot,<)\) vollständig? Was folgt daraus?",
      r"""<p>Ja: Der archimedisch angeordnete Körper der reellen Zahlen ist <b>vollständig</b>. Dadurch sind die reellen Zahlen <b>eindeutig charakterisiert</b>.</p>""",
      'reelle Zahlen vollständig eindeutig charakterisiert'),

    C('q-nicht', 'Bsp. 2.0.8',
      r"Warum ist \((\mathbb Q,+,\cdot,<)\) <b>nicht vollständig</b>? (Beispiel)",
      r"""<p>\(\mathbb Q\) ist ein archimedisch angeordneter Körper, aber nicht vollständig. Betrachte die rekursiv definierte Folge</p>
\[b_{n+1}=\frac12\left(b_n+\frac2{b_n}\right)\]
<p>mit Startwert \(b_0>0\). Sie konvergiert gegen \(\sqrt2\), ist also eine <b>Cauchy-Folge in \(\mathbb Q\)</b>, aber \(\sqrt2\notin\mathbb Q\).</p>
<div class="tip">Das ist das Heron-Verfahren für \(x=2\). <b>Ergänzung (nicht im Skript):</b> Damit alle Glieder in \(\mathbb Q\) liegen, wählt man einen rationalen Startwert.</div>""",
      'Q nicht vollständig Wurzel 2 Heron Cauchy-Folge Gegenbeispiel'),
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
mc('d2-mc-01', r"Wogegen konvergiert eine <b>monoton wachsende, beschränkte</b> Folge \((a_n)\) reeller Zahlen?",
   [r"Gegen \(\sup\{a_n\mid n\in\mathbb N\}\)", r"Gegen \(\inf\{a_n\mid n\in\mathbb N\}\)", r"Gegen \(a_1\)", "Sie muss nicht konvergieren"], 0,
   r"Hauptsatz über monotone Folgen. Monoton fallend und beschränkt: Grenzwert \(\inf\{a_n\}\).", 'Satz 2.0.1', 'Hauptsatz monotone Folgen Supremum')
mc('d2-mc-02', r"Was gilt für eine <b>monoton fallende, unbeschränkte</b> Folge reeller Zahlen?",
   [r"Sie divergiert bestimmt gegen \(-\infty\)", r"Sie divergiert bestimmt gegen \(+\infty\)", r"Sie konvergiert gegen ihr Infimum", "Sie hat zwei Häufungspunkte"], 0,
   r"Monoton wachsend und unbeschränkt: bestimmt divergent gegen \(+\infty\).", 'Satz 2.0.1 (2)', 'monoton fallend unbeschränkt bestimmt divergent')
mc('d2-mc-03', r"Welche Bedingung gehört <b>nicht</b> zur Definition einer Intervallschachtelung \(([a_n,b_n])_{n\in\mathbb N}\)?",
   [r"\((a_n)\) und \((b_n)\) sind beide Nullfolgen", r"\((a_n)\) ist monoton wachsend", r"\((b_n)\) ist monoton fallend", r"\((b_n-a_n)\) ist eine Nullfolge"], 0,
   'Nur die Intervalllängen müssen eine Nullfolge bilden, nicht die Grenzen selbst.', 'Def. 2.0.1', 'Intervallschachtelung Bedingungen')
mc('d2-mc-04', r"Welche Ungleichungskette gilt bei einer Intervallschachtelung für alle \(n\in\mathbb N\)?",
   [r"\(a_n\le a_{n+1}\le b_{n+1}\le b_n\)", r"\(a_{n+1}\le a_n\le b_n\le b_{n+1}\)", r"\(a_n\le b_n\le a_{n+1}\le b_{n+1}\)", r"\(a_{n+1}\le b_{n+1}\le a_n\le b_n\)"], 0,
   r"Daraus folgt \([a_{n+1},b_{n+1}]\subseteq[a_n,b_n]\).", 'Bem. 2.0.2 (1)', 'Intervallschachtelung Ungleichung Teilmenge')
mc('d2-mc-05', r"Was besagt der Satz über <b>Cantor-Dedekind-Schnitte</b>?",
   ['Zu jeder Intervallschachtelung in ℝ gibt es genau eine reelle Zahl, die in allen Intervallen liegt',
    'Zu jeder Intervallschachtelung gibt es mindestens zwei reelle Zahlen in allen Intervallen',
    'Jede beschränkte Folge hat einen Häufungspunkt',
    'Jede Cauchy-Folge ist beschränkt'], 0,
   r"\(r\in\bigcap_{n\in\mathbb N}[a_n,b_n]\), und es gilt \(\lim a_n=r=\lim b_n\).", 'Satz 2.0.2', 'Cantor Dedekind')
mc('d2-mc-06', r"Mit welchem Hilfsmittel zeigt man, dass in allen Intervallen einer Intervallschachtelung <b>höchstens eine</b> Zahl liegt?",
   [r"Schrankenlemma, angewandt auf \(|r-r'|\le b_n-a_n\)", 'Satz von Bolzano-Weierstraß', 'Hauptsatz über monotone Folgen', 'Archimedisches Axiom allein'], 0,
   r"Da \(b_n-a_n\to0\), folgt \(|r-r'|\to0\), also \(r=r'\).", 'Bem. 2.0.2 (2)', 'Schrankenlemma höchstens eine')
mc('d2-mc-07', r"Welche Rekursion beschreibt das <b>Heron-Verfahren</b> zur Bestimmung von \(\sqrt x\) (\(x>0\), \(b_0>0\))?",
   [r"\(b_{n+1}=\frac12\left(b_n+\frac x{b_n}\right)\)", r"\(b_{n+1}=\frac12\left(b_n+x\,b_n\right)\)", r"\(b_{n+1}=\frac{b_n}2+\frac{b_n}x\)", r"\(b_{n+1}=\frac12\left(b_n-\frac x{b_n}\right)\)"], 0,
   r"Der Grenzwert ist \(\sqrt x\); der Startwert \(b_0>0\) ist beliebig.", 'Bem. 2.0.3 (1)', 'Heron Verfahren Wurzel')
mc('d2-mc-08', r"Wie ist \(e^z\) für \(z\in\mathbb Z\) im Skript als Grenzwert definiert?",
   [r"\(\lim_{n\to\infty}\left(1+\frac zn\right)^n\)", r"\(\lim_{n\to\infty}\left(1+\frac1n\right)^{z}\)", r"\(\lim_{n\to\infty}\left(z+\frac1n\right)^n\)", r"\(\lim_{n\to\infty}\left(1+\frac nz\right)^n\)"], 0,
   r"Für \(z=1\) erhält man \(e=\lim\left(1+\frac1n\right)^n\).", 'Bem. 2.0.3 (2)', 'Eulersche Zahl e hoch z')
mc('d2-mc-09', r"Welchen Grenzwert hat \(\sqrt[n]{n}\) für \(n\to\infty\)?",
   [r"\(1\)", r"\(0\)", r"\(e\)", r"\(+\infty\)"], 0,
   r"Ebenso \(\lim\sqrt[n]{x}=1\) für jedes \(x\in\mathbb R^+\).", 'Bem. 2.0.4', 'n-te Wurzel Grenzwert')
mc('d2-mc-10', r"Wann ist \((a_{n_k})_{k\in\mathbb N}\) eine <b>Teilfolge</b> von \((a_n)_{n\in\mathbb N}\)?",
   [r"Wenn \((n_k)_{k\in\mathbb N}\) eine streng monoton wachsende Folge von Indizes ist", r"Wenn \((n_k)\) eine beliebige Folge natürlicher Zahlen ist", r"Wenn \((n_k)\) monoton fallend ist", r"Wenn \((a_{n_k})\) konvergiert"], 0,
   r"Beispiele: \((a_{2k-1})\), \((a_{2k})\), \((a_{k^2})\), auch \((a_k)\) selbst.", 'Def. 2.0.2', 'Teilfolge Indizes')
mc('d2-mc-11', r"Welche der folgenden ist im Allgemeinen <b>keine</b> Teilfolge von \((a_n)_{n\in\mathbb N}\)?",
   [r"\((a_{1})_{k\in\mathbb N}\), also immer dasselbe Glied", r"\((a_{2k})_{k\in\mathbb N}\)", r"\((a_{k^2})_{k\in\mathbb N}\)", r"\((a_k)_{k\in\mathbb N}\)"], 0,
   r"Die Indexfolge muss streng monoton wachsend sein; die konstante Indexfolge \(n_k=1\) ist es nicht.", 'Def. 2.0.2, Bsp. 2.0.3', 'Teilfolge Beispiele streng monoton')
mc('d2-mc-12', r"Wann heißt \(h\in\mathbb R\) ein <b>Häufungspunkt</b> der Folge \((a_n)\)?",
   ['Wenn es eine Teilfolge gibt, die gegen h konvergiert', 'Wenn jede Teilfolge gegen h konvergiert', 'Wenn fast alle Folgeglieder gleich h sind', 'Wenn h das Supremum der Folgeglieder ist'], 0,
   'Konvergiert jede Teilfolge gegen h, ist h sogar der Grenzwert.', 'Def. 2.0.3', 'Häufungspunkt Definition Teilfolge')
mc('d2-mc-13', r"Wie viele Folgeglieder müssen bei einem <b>Häufungspunkt</b> \(h\) in jeder \(\varepsilon\)-Umgebung \(]h-\varepsilon,h+\varepsilon[\) liegen?",
   ['Unendlich viele', 'Fast alle (alle bis auf endlich viele)', 'Mindestens eines', 'Alle'], 0,
   r"„Fast alle“ ist die Bedingung für den <b>Grenzwert</b>. Beim Häufungspunkt dürfen auch unendlich viele außerhalb liegen.", 'Satz 2.0.3', 'Häufungspunkt Epsilon unendlich viele', warn=True)
mc('d2-mc-14', r"Eine Folge hat <b>mehr als einen</b> Häufungspunkt. Was folgt?",
   ['Sie ist divergent', 'Sie ist konvergent', 'Sie ist eine Cauchy-Folge', 'Sie ist unbeschränkt'], 0,
   'Eine konvergente Folge hat genau einen Häufungspunkt, ihren Grenzwert.', 'Bem. 2.0.5 (2)', 'mehrere Häufungspunkte divergent')
mc('d2-mc-15', r"Was besagt der Satz von <b>Bolzano-Weierstraß</b>?",
   ['Jede beschränkte Folge reeller Zahlen hat mindestens einen Häufungspunkt', 'Jede beschränkte Folge reeller Zahlen ist konvergent', 'Jede monotone Folge hat genau einen Häufungspunkt', 'Jede Folge reeller Zahlen hat einen Häufungspunkt'], 0,
   r"Beispiel einer beschränkten, nicht konvergenten Folge: \(((-1)^n)\) mit den Häufungspunkten \(1\) und \(-1\) (Ergänzung).", 'Satz 2.0.4', 'Bolzano Weierstraß')
mc('d2-mc-16', r"Wie lautet die Definition einer <b>Cauchy-Folge</b> \((a_n)\)?",
   [r"\(\forall\varepsilon>0\) \(\exists n_0\in\mathbb N\) \(\forall n,m\ge n_0:\) \(|a_n-a_m|<\varepsilon\)",
    r"\(\exists\varepsilon>0\) \(\forall n_0\in\mathbb N\) \(\exists n,m\ge n_0:\) \(|a_n-a_m|<\varepsilon\)",
    r"Nur \(\forall\varepsilon>0\) \(\exists n_0\in\mathbb N\) \(\forall n\ge n_0:\) \(|a_n-a_{n+1}|<\varepsilon\)",
    r"\(\forall n,m\in\mathbb N:\) \(|a_n-a_m|<1\)"], 0,
   r"Ab einem Index \(n_0\) liegen <b>je zwei</b> Folgeglieder weniger als \(\varepsilon\) auseinander.", 'Def. 2.0.4', 'Cauchy-Folge Quantoren')
mc('d2-mc-17', r"Welche Aussage ist nach dem <b>Hauptsatz über konvergente Folgen</b> <b>nicht</b> äquivalent zu „\((a_n)\) ist konvergent“?",
   [r"\((a_n)\) ist beschränkt", r"\((a_n)\) ist eine Cauchy-Folge", r"\((a_n)\) ist beschränkt und hat genau einen Häufungspunkt", r"Jede Teilfolge von \((a_n)\) konvergiert gegen denselben Grenzwert \(a\)"], 0,
   r"Beschränkt allein reicht nicht (z. B. \(((-1)^n)\), Ergänzung). Die letzte Option ist äquivalent nach Bem. 2.0.7.", 'Satz 2.0.5', 'Hauptsatz konvergente Folgen äquivalent')
mc('d2-mc-18', r"Welche Richtung des Hauptsatzes über konvergente Folgen gilt auch in \(\mathbb Q\)?",
   ['konvergent ⇒ Cauchy-Folge', 'Cauchy-Folge ⇒ konvergent', 'beschränkt mit genau einem Häufungspunkt ⇒ konvergent', 'Keine der Richtungen'], 0,
   'Cauchy ⇒ konvergent braucht Bolzano-Weierstraß und damit die Vollständigkeit von ℝ.', 'Bem. 2.0.9', 'Q Cauchy konvergent Körper')
mc('d2-mc-19', r"Wann heißt ein archimedisch angeordneter Körper \(K\) nach Definition <b>vollständig</b>?",
   [r"Wenn jede Cauchy-Folge in \(K\) einen Grenzwert in \(K\) hat", r"Wenn jede Folge in \(K\) konvergiert", r"Wenn jede Teilmenge von \(K\) ein Maximum hat", r"Wenn \(K\) unendlich viele Elemente hat"], 0,
   'Äquivalent: Intervallschachtelungen definieren genau ein Element; nicht-leere beschränkte Teilmengen haben Supremum und Infimum.', 'Def. 2.0.5', 'Vollständigkeit Definition')
mc('d2-mc-20', r"Mit welcher Folge zeigt das Skript, dass \(\mathbb Q\) <b>nicht vollständig</b> ist?",
   [r"\(b_{n+1}=\frac12\left(b_n+\frac2{b_n}\right)\), \(b_0>0\), mit Grenzwert \(\sqrt2\notin\mathbb Q\)", r"\(a_n=\frac1n\) mit Grenzwert \(0\)", r"\(a_n=(-1)^n\)", r"\(a_n=\left(1+\frac1n\right)^n\) mit Grenzwert \(1\)"], 0,
   r"Die Folge ist eine Cauchy-Folge in \(\mathbb Q\), ihr Grenzwert liegt aber nicht in \(\mathbb Q\).", 'Bsp. 2.0.8', 'Q nicht vollständig Wurzel 2')

# ------------------------------------------------------------ Richtig / Falsch
tf('d2-tf-01', r"Jede monoton wachsende Folge reeller Zahlen ist konvergent.", False,
   r"Nur wenn sie beschränkt ist; unbeschränkt divergiert sie bestimmt gegen \(+\infty\).", 'Satz 2.0.1', 'monoton wachsend konvergent beschränkt', warn=True)
tf('d2-tf-02', r"Der Beweis des Hauptsatzes über monotone Folgen benutzt die Vollständigkeit von \(\mathbb R\).", True,
   r"Er braucht \(\sup M\) bzw. \(\inf M\) in \(\mathbb R\) für \(M=\{a_n\mid n\in\mathbb N\}\).", 'Bem. 2.0.1', 'Vollständigkeit Beweis')
tf('d2-tf-03', r"Bei einer Intervallschachtelung ist jedes Intervall \([a_{n+1},b_{n+1}]\) eine Teilmenge von \([a_n,b_n]\).", True,
   r"Wegen \(a_n\le a_{n+1}\le b_{n+1}\le b_n\).", 'Bem. 2.0.2 (1)', 'Intervallschachtelung Teilmenge')
tf('d2-tf-04', r"Bei einer Intervallschachtelung müssen die unteren Grenzen \(a_n\) eine Nullfolge bilden.", False,
   r"Die <b>Intervalllängen</b> \(b_n-a_n\) bilden eine Nullfolge; \((a_n)\) ist monoton wachsend.", 'Def. 2.0.1', 'Intervallschachtelung Nullfolge')
tf('d2-tf-05', r"Die durch eine Intervallschachtelung definierte Zahl \(r\) ist der gemeinsame Grenzwert der unteren und der oberen Intervallgrenzen.", True,
   r"\(\lim a_n=r=\lim b_n\).", 'Bem. 2.0.3', 'Grenzwert Intervallschachtelung')
tf('d2-tf-06', r"Beim Heron-Verfahren zur Berechnung von \(\sqrt x\) muss der Startwert \(b_0\) bereits nahe bei \(\sqrt x\) liegen.", False,
   r"Laut Skript ist jeder Startwert \(b_0>0\) erlaubt.", 'Bem. 2.0.3 (1)', 'Heron Startwert')
tf('d2-tf-07', r"Für jedes \(x\in\mathbb R^+\) gilt \(\lim_{n\to\infty}\sqrt[n]{x}=1\).", True,
   r"Insbesondere auch \(\lim\sqrt[n]{n}=1\).", 'Bem. 2.0.4', 'n-te Wurzel')
tf('d2-tf-08', r"Die Folge \((a_k)_{k\in\mathbb N}\) ist selbst eine Teilfolge von \((a_n)_{n\in\mathbb N}\).", True,
   r"Die Indexfolge \(n_k=k\) ist streng monoton wachsend.", 'Bsp. 2.0.3', 'Teilfolge')
tf('d2-tf-09', r"Ist eine Folge konvergent gegen \(a\), so ist \(a\) ihr einziger Häufungspunkt.", True,
   'Jede Teilfolge konvergiert dann gegen a.', 'Bem. 2.0.5 (1)', 'konvergent einziger Häufungspunkt')
tf('d2-tf-10', r"Bei einem Häufungspunkt \(h\) liegen in jeder \(\varepsilon\)-Umgebung von \(h\) fast alle Folgeglieder.", False,
   r"Nur <b>unendlich viele</b>; außerhalb dürfen ebenfalls unendlich viele liegen. „Fast alle“ gilt beim Grenzwert.", 'Satz 2.0.3, Bem. 2.0.6', 'Häufungspunkt fast alle unendlich viele', warn=True)
tf('d2-tf-11', r"\(a\) ist genau dann Grenzwert von \((a_n)\), wenn jede Teilfolge von \((a_n)\) gegen \(a\) konvergiert.", True,
   'Beim Häufungspunkt genügt dagegen eine Teilfolge.', 'Bem. 2.0.7 (1)', 'Grenzwert Teilfolge äquivalent')
tf('d2-tf-12', r"Jede beschränkte Folge reeller Zahlen ist konvergent.", False,
   r"Bolzano-Weierstraß liefert nur mindestens einen <b>Häufungspunkt</b>. Konvergent ist sie erst mit genau einem Häufungspunkt.", 'Satz 2.0.4, Satz 2.0.5', 'beschränkt konvergent Bolzano', warn=True)
tf('d2-tf-13', r"Eine reelle Folge ist genau dann konvergent, wenn sie eine Cauchy-Folge ist.", True,
   'Hauptsatz über konvergente Folgen (in ℝ).', 'Satz 2.0.5', 'Cauchy konvergent äquivalent')
tf('d2-tf-14', r"Jede Cauchy-Folge in \(\mathbb Q\) hat einen Grenzwert in \(\mathbb Q\).", False,
   r"Gegenbeispiel: Heron-Folge für \(\sqrt2\); der Grenzwert \(\sqrt2\) liegt nicht in \(\mathbb Q\).", 'Bem. 2.0.9, Bsp. 2.0.8', 'Q Cauchy Grenzwert')
tf('d2-tf-15', r"Jede konvergente Folge in einem Körper \(K\) ist eine Cauchy-Folge in \(K\).", True,
   'Der Beweis von „konvergent ⇒ Cauchy“ benutzt nicht, dass es sich um ℝ handelt.', 'Bem. 2.0.9', 'konvergent Cauchy Körper')
tf('d2-tf-16', r"\(\mathbb Q\) ist ein archimedisch angeordneter Körper, aber nicht vollständig.", True,
   r"Die Heron-Folge für \(\sqrt2\) ist eine Cauchy-Folge in \(\mathbb Q\) ohne Grenzwert in \(\mathbb Q\).", 'Bsp. 2.0.8', 'Q nicht vollständig')
tf('d2-tf-17', r"Durch die Eigenschaft, ein vollständiger archimedisch angeordneter Körper zu sein, sind die reellen Zahlen eindeutig charakterisiert.", True,
   '', 'Bsp. 2.0.7', 'reelle Zahlen eindeutig charakterisiert')
tf('d2-tf-18', r"Zur Vollständigkeit gehört: Jede beliebige Teilmenge von \(K\) besitzt ein Supremum in \(K\).", False,
   r"Nur jede <b>nicht-leere, beschränkte</b> Teilmenge besitzt Supremum und Infimum in \(K\).", 'Bem. 2.0.10 (3)', 'Supremum nicht-leer beschränkt', warn=True)

# ------------------------------------------------------------ Lückentext
gap('d2-gap-01', r"Eine monoton wachsende, beschränkte Folge konvergiert gegen das {{Supremum|sup}} ihrer Folgeglieder, eine monoton fallende, beschränkte Folge gegen das {{Infimum|inf}}.",
    '', 'Satz 2.0.1', 'Supremum Infimum monoton')
gap('d2-gap-02', r"Bei einer Intervallschachtelung ist die Folge der unteren Grenzen monoton {{wachsend|steigend}}, die der oberen Grenzen monoton {{fallend}}, und die Intervalllängen bilden eine {{Nullfolge}}.",
    '', 'Def. 2.0.1', 'Intervallschachtelung')
gap('d2-gap-03', r"Nach dem Satz über die {{Cantor-Dedekind-Schnitte|Cantor-Dedekind|Cantor Dedekind Schnitte}} gibt es zu jeder Intervallschachtelung in ℝ genau eine reelle Zahl in allen Intervallen.",
    '', 'Satz 2.0.2', 'Cantor Dedekind')
gap('d2-gap-04', r"Die Folge \(b_{n+1}=\frac12\left(b_n+\frac x{b_n}\right)\) zur Berechnung von \(\sqrt x\) heißt {{Heron-Verfahren|Heron|Heronverfahren}}.",
    '', 'Bem. 2.0.3 (1)', 'Heron')
gap('d2-gap-05', r"Ist \((n_k)\) eine streng monoton wachsende Folge von Indizes, so heißt \((a_{n_k})\) eine {{Teilfolge}} von \((a_n)\).",
    '', 'Def. 2.0.2', 'Teilfolge')
gap('d2-gap-06', r"Konvergiert eine Teilfolge von \((a_n)\) gegen \(h\), so heißt \(h\) {{Häufungspunkt|Haeufungspunkt}} der Folge.",
    '', 'Def. 2.0.3', 'Häufungspunkt')
gap('d2-gap-07', r"Beim Grenzwert liegen in jeder ε-Umgebung {{fast alle}} Folgeglieder, beim Häufungspunkt {{unendlich viele}}.",
    'Fast alle = alle bis auf endlich viele.', 'Bem. 2.0.7', 'fast alle unendlich viele')
gap('d2-gap-08', r"Nach dem Satz von {{Bolzano-Weierstraß|Bolzano-Weierstrass|Bolzano Weierstraß}} besitzt jede beschränkte Folge reeller Zahlen mindestens einen Häufungspunkt.",
    '', 'Satz 2.0.4', 'Bolzano Weierstraß')
gap('d2-gap-09', r"Eine Folge, bei der ab einem Index \(n_0\) je zwei Folgeglieder weniger als ε voneinander entfernt sind, heißt {{Cauchy-Folge|Cauchyfolge|Cauchy Folge}}.",
    '', 'Def. 2.0.4, Bem. 2.0.8', 'Cauchy-Folge')
gap('d2-gap-10', r"Eine reelle Folge ist genau dann konvergent, wenn sie {{beschränkt}} ist und genau einen Häufungspunkt besitzt.",
    '', 'Satz 2.0.5', 'beschränkt Häufungspunkt')
gap('d2-gap-11', r"Ein archimedisch angeordneter Körper heißt {{vollständig}}, wenn jede Cauchy-Folge in ihm einen Grenzwert in ihm besitzt.",
    '', 'Def. 2.0.5', 'vollständig')
