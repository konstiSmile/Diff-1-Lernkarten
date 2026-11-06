# Psycho 2 · Persönlichkeitspsychologie (Vorlesung Barchfeld, LMU) · Kapitel 1 und 2
# Quelle: Zusammenfassung_PersPsych_Teil1-5.md (Teil 1 und Teil 2). Nur Inhalte aus den Folien.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

# ---------------------------------------------------------------- Kapitel 1: Einführung, Definitionen, Eigenschaften
CARDS_K1 = [
    C('was-ist', 'Teil 1 · Einführung', 'Was ist <b>Persönlichkeitspsychologie</b>?',
      'Ein <b>Teilgebiet der Psychologie</b>. Sie beschäftigt sich mit den <b>Bedingungen der individuellen Besonderheiten von Menschen</b> (also den Unterschieden zwischen Menschen).',
      'Persönlichkeitspsychologie Teilgebiet individuelle Besonderheiten Unterschiede'),
    C('fragen', 'Teil 1 · Einführung', 'Nach welchen <b>fünf Dingen</b> fragt die Persönlichkeitspsychologie?',
      '<ol><li>Beschaffenheit der Merkmale, in denen sich Menschen unterscheiden</li><li>Ausmaß der Unterschiede</li><li>Abhängigkeit der Merkmale voneinander</li><li>Ursachen der Unterschiede</li><li>Beeinflussbarkeit der Merkmale (Training, Umweltveränderungen, Medikamente …)</li></ol>',
      'Fragen Beschaffenheit Ausmaß Abhängigkeit Ursachen Beeinflussbarkeit'),
    C('definition', 'Teil 1 · Definition', 'Wie lautet die <b>Arbeitsdefinition</b> der Persönlichkeitspsychologie (Asendorpf, 2004)?',
      'Die <b>empirische</b> Wissenschaft von den <b>überdauernden, nichtpathologischen, verhaltensrelevanten</b> individuellen Besonderheiten von Menschen <b>innerhalb einer bestimmten Population</b>.',
      'Definition Asendorpf empirisch überdauernd nichtpathologisch verhaltensrelevant Population'),
    C('definition-begriffe', 'Teil 1 · Definition', 'Was bedeuten die Begriffe der Definition: <b>empirisch, überdauernd, nicht-pathologisch, verhaltensrelevant, Population</b>?',
      '<ul><li><b>Empirisch:</b> genügt wissenschaftlichen Kriterien</li><li><b>Überdauernd:</b> mittel- und langfristige Phänomene</li><li><b>Nicht-pathologisch:</b> gesunde Personen werden untersucht</li><li><b>Verhaltensrelevant:</b> Merkmale, die Verhalten steuern</li><li><b>Population:</b> Bevölkerungsgruppen</li></ul>',
      'empirisch überdauernd nichtpathologisch verhaltensrelevant Population gesund'),
    C('alltag', 'Teil 1 · Alltagspsychologie', 'Wozu dient die <b>Alltagspsychologie</b>?',
      'Menschen anhand von Merkmalen <b>beschreiben</b>, ihr Verhalten <b>erklären</b> und ihr Verhalten <b>vorhersagen</b>. Die Persönlichkeitspsychologie fragt dann, welche Merkmale konkret gemeint sind.',
      'Alltagspsychologie beschreiben erklären vorhersagen'),
    C('merkmale', 'Teil 1 · Alltagspsychologie', 'Welche Merkmale untersucht die Persönlichkeitspsychologie nach der Folie (Beispiele)?',
      'Z. B. eifersüchtig, intelligent, konservativ, gewissenhaft, ängstlich, mutig, hilfsbereit, aggressiv, engstirnig, cholerisch, extravertiert <b>sowie rein körperliche Merkmale</b> (mittelgroß, schlank, sommersprossig, braunäugig, blond).',
      'Merkmale Beispiele körperlich Eigenschaften'),
    C('eigenschaft', 'Teil 1 · Eigenschaften', 'Wie heißen Merkmale, die <b>Verhalten steuern oder beeinflussen</b>?',
      '<b>Eigenschaften = Dispositionen = Traits.</b>',
      'Eigenschaft Disposition Trait Verhalten steuern'),
    C('disposition', 'Teil 1 · Eigenschaften', 'Wie definiert Asendorpf (2004, S. 4) eine <b>Disposition</b>?',
      'Ein Merkmal einer Person mit <b>mittelfristiger zeitlicher Stabilität</b>: es überdauert <b>zumindest Wochen oder Monate</b>. Es <b>disponiert</b> die Person, in bestimmten Situationen ein bestimmtes Verhalten zu zeigen.<br><br><i>Nicht</i> „lebenslang unveränderlich“.',
      'Disposition mittelfristig Stabilität Wochen Monate'),
    C('normalverteilung', 'Teil 1 · Eigenschaften', 'Welche zwei Merkmale haben Eigenschaften (Normalverteilung und …)?',
      '<ul><li><b>Normalverteilung</b> (Gauß): die meisten Personen liegen in der Mitte, z. B. bei Geselligkeit „mittel gesellig“.</li><li><b>Kontinuum:</b> Eigenschaften sind Dimensionen, keine Kategorien. Jede Person liegt irgendwo auf dem Kontinuum.</li></ul>',
      'Normalverteilung Kontinuum Dimension Geselligkeit'),
    C('trait', 'Teil 1 · State und Trait', 'Was ist ein <b>Trait</b> (Eigenschaft, Disposition)?',
      'Eine <b>relativ überdauernde Disposition</b>, die bestimmte Aspekte des Verhaltens einer Person in einer bestimmten Klasse von Situationen beschreiben und vorhersagen soll.<br><br>Beispiel: Bei <b>allen</b> Prüfungen die Nerven verlieren = <b>Prüfungsangst (Trait)</b>.',
      'Trait Eigenschaft überdauernd Prüfungsangst'),
    C('state', 'Teil 1 · State und Trait', 'Was ist ein <b>State</b>?',
      'Der <b>aktuelle Zustand</b> einer Person, der <b>über Situationen hinweg variiert</b>.<br><br>Beispiel: Sich für eine Prüfung nicht vorbereitet zu haben führt zu einem <b>Zustand der Besorgnis (State)</b>.',
      'State Zustand aktuell situationsabhängig Besorgnis'),
    C('state-trait', 'Teil 1 · State und Trait', '<b>State oder Trait?</b> Unterschied in einem Satz.',
      '<b>Trait:</b> überdauernd, über Situationen hinweg stabil.<br><b>State:</b> aktuell, situationsabhängig, variiert.',
      'State Trait Unterschied Vergleich'),
    C('lisa-anna', 'Teil 1 · State und Trait', 'Lisa reagiert in <b>allen 8</b> Situationen mit Angst, Anna je nach Situation unterschiedlich. Was folgt?',
      '<b>Lisa = Trait-Angst</b> (stabil über Situationen).<br><b>Anna = State-Angst</b> (situationsabhängig).<br><br>Über 6 Klausuren: Lisa durchgehend starke Prüfungsangst, Anna schwankt.',
      'Lisa Anna Trait-Angst State-Angst Situationen Klausur'),
    C('konstrukt', 'Teil 1 · Konstrukte', 'Was ist ein <b>Konstrukt</b>?',
      'Ein <b>nicht empirisch erkennbarer Sachverhalt</b> innerhalb einer Theorie: gedanklicher bzw. theoretischer Natur, <b>nicht direkt beobachtbar</b>. Dispositionen sind Konstrukte.',
      'Konstrukt nicht beobachtbar theoretisch Disposition'),
    C('latent', 'Teil 1 · Konstrukte', 'Was sind <b>latente Konstrukte</b> und was heißt <b>Operationalisierung</b>?',
      'Latente Konstrukte (latente Variablen) werden aus <b>anderen, messbaren Sachverhalten (Indikatoren)</b> <b>erschlossen</b>. Dieses Erschließen heißt <b>Operationalisierung</b>.',
      'latent Konstrukt Indikatoren Operationalisierung erschlossen'),
    C('oekonomie', 'Teil 1 · Konstrukte', 'Was bedeutet die <b>Ökonomie von Konstrukten</b> (Beispiel Ängstlichkeit)?',
      'Verschiedene Ereignisse (Klausur, Zahnarzt, Fallschirmspringen) führen zu denselben Beobachtungen: negative Kognition, körperliche Veränderungen (Schwitzen, Zittern, Röte/Blässe), Emotion Angst. <b>Ein Konstrukt</b> („Ängstlichkeit“) fasst viele Beobachtungen <b>sparsam</b> zusammen.',
      'Ökonomie Konstrukt Ängstlichkeit Beobachtungen'),
    C('verwechslung', 'Teil 1 · Verwechslungsgefahr', 'Welche vier <b>Verwechslungen</b> sind in Teil 1 klausurtypisch?',
      '<ul><li>Trait (überdauernd) ≠ State (aktuell)</li><li>„Nicht-pathologisch“ = gesunde Personen, nicht Störungen</li><li>Dispositionen sind Konstrukte: nur über Indikatoren erschlossen</li><li>Disposition = <b>mittelfristig</b> stabil (Wochen/Monate), nicht lebenslang</li></ul>',
      'Verwechslungsgefahr Trait State pathologisch Konstrukt'),
    C('klausur', 'Teil 1 · Organisatorisches', 'Was ist zur <b>Klausur Psychologie II</b> zu wissen?',
      'Termin <b>29.01.2027, 8–10 Uhr</b>. Format: <b>Multiple Choice</b>. Klausurrelevant sind <b>nur die Folien und die Vorlesung</b> (Skripten nicht autorisiert). <b>Kein Wiederholungstermin</b> im selben Semester.',
      'Klausur Termin Multiple Choice Folien Wiederholung'),
]

# ---------------------------------------------------------------- Kapitel 2: Methoden
CARDS_K2 = [
    C('nomo-ideo', 'Teil 2 · Forschungsansätze', '<b>Nomothetisch</b> vs. <b>ideografisch</b>: Was wird verglichen?',
      '<b>Nomothetisch:</b> <b>eine</b> Disposition an <b>vielen</b> Individuen (Durchschnittswerte, Zusammenhänge, Gruppenunterschiede).<br><b>Ideografisch:</b> <b>viele</b> Dispositionen an <b>einem</b> Individuum (Persönlichkeit eines Menschen erfassen).<br><br>Merkhilfe: <b>ideo</b>grafisch = das Individuum.',
      'nomothetisch ideografisch idiografisch Disposition Individuen'),
    C('nomo-beispiele', 'Teil 2 · Forschungsansätze', 'Welche Beispielfragen gehören zum <b>nomothetischen</b>, welche zum <b>ideografischen</b> Ansatz?',
      '<b>Nomothetisch:</b> Sind Frauen hilfsbereiter als Männer? Sind eifersüchtige Menschen weniger selbstbewusst? Sinkt die Intelligenz im Laufe des Lebens?<br><br><b>Ideografisch:</b> Ist Lisa intelligenter als Anna? Wer ist der/die motivierteste Schüler*in der Klasse?',
      'nomothetisch ideografisch Beispielfragen Lisa Anna Intelligenz'),
    C('variation-korrelation', 'Teil 2 · Forschungsansätze', 'Was sind <b>Variationsforschung</b> und <b>Korrelationsforschung</b>?',
      'Beides nomothetisch:<br><b>Variationsforschung:</b> <b>ein</b> Merkmal an <b>vielen</b> Individuen.<br><b>Korrelationsforschung:</b> <b>zwei oder mehr</b> Merkmale an <b>vielen</b> Individuen.',
      'Variationsforschung Korrelationsforschung Merkmal Individuen'),
    C('psychografie', 'Teil 2 · Forschungsansätze', 'Was sind <b>Psychografie</b> und <b>Komparationsforschung</b>?',
      'Beides ideografisch:<br><b>Psychografie:</b> <b>eine</b> Individualität, viele Merkmale.<br><b>Komparationsforschung:</b> <b>zwei oder mehr</b> Individualitäten, viele Merkmale.',
      'Psychografie Komparationsforschung Individualität Merkmale'),
    C('schule', 'Teil 2 · Forschungsansätze', 'Was heißt <b>ideografisch</b> und <b>nomothetisch</b> im Schulkontext?',
      '<b>Ideografisch:</b> Profil einer einzelnen Schülerin (z. B. Lisa) über viele Merkmale.<br><b>Nomothetisch:</b> Position aller Schüler der Klasse 4a auf einer Disposition im Vergleich zum <b>Klassenmittelwert</b>.',
      'Schule Profil Klassenmittelwert Klasse 4a Schüler'),
    C('korrelative', 'Teil 2 · Korrelation', 'Was ist <b>korrelative Forschung</b> und welcher Ansatz ist sie?',
      'Untersuchung <b>vieler Personen</b> = <b>nomothetische</b> Forschung. Ziel: <b>Beziehungen zwischen Variablen</b> erfassen (berechenbar).',
      'korrelative Forschung nomothetisch Beziehungen Variablen'),
    C('r-bereich', 'Teil 2 · Korrelation', 'Welchen Wertebereich hat der <b>Korrelationskoeffizient r</b>, und was bedeuten positiv/negativ?',
      'Zwischen <b>−1 und +1</b>.<br><b>Positiv</b> („je mehr, desto mehr“): z. B. je mehr Futter, desto dickere Kühe (r = .5).<br><b>Negativ</b> („je mehr, desto weniger“): z. B. je mehr Strecke mit dem Auto, desto weniger Sprit im Tank (r = −.5).',
      'Korrelationskoeffizient r positiv negativ Zusammenhang'),
    C('r-groesse', 'Teil 2 · Korrelation', 'Welche <b>Größenordnungen</b> von Korrelationen unterscheidet die Folie?',
      '<ul><li>bis <b>r = .3</b>: gering</li><li>ab ca. <b>r = .5</b>: hoch</li><li>ab ca. <b>r = .7–.8</b>: (sehr) hoch</li></ul>',
      'Korrelation Größenordnung gering hoch .3 .5 .7'),
    C('r-selten', 'Teil 2 · Korrelation', 'Warum sind <b>sehr hohe Korrelationen</b> in der Psychologie selten?',
      'Ein Phänomen wird selten nur von einem anderen Phänomen beeinflusst. Beispiel Intelligenz: Gene, Förderung, Bildungshintergrund der Eltern …',
      'Korrelation selten Intelligenz Einflüsse'),
    C('scatter', 'Teil 2 · Korrelation', 'Scatterplot-Beispiel Größe und Gewicht: Was gilt für <b>Marsmenschen</b> und <b>Aliens</b>?',
      '<b>Marsmenschen:</b> perfekte Korrelation (r = 1).<br><b>Aliens:</b> <b>keine Varianz</b> → keine Korrelation berechenbar.<br>(Hunde hoch, Pferde mittel, Vögel mittel <i>negativ</i>, Fische keine Korrelation.)',
      'Scatterplot Marsmenschen Aliens Varianz Hunde Pferde Vögel Fische'),
    C('r2', 'Teil 2 · Korrelation', 'Was gibt das <b>Bestimmtheitsmaß r²</b> an?',
      'Das Quadrat des Korrelationskoeffizienten: wie viel <b>Prozent der Varianz</b> der einen Variable durch die andere <b>erklärt</b> werden können.<br><br>r = .5 → r² = .25 → <b>25 %</b> (nicht 50 %).',
      'Bestimmtheitsmaß r² erklärte Varianz Prozent'),
    C('matheleistung', 'Teil 2 · Korrelation', 'Matheleistung: Welche <b>r</b> und welche erklärte Varianz haben Intelligenz, Motivation, Interesse, Fleiß, Gedächtnis?',
      '<ul><li>Intelligenz .5 → <b>25 %</b></li><li>Motivation .4 → <b>16 %</b></li><li>Interesse .4 → <b>16 %</b></li><li>Fleiß .3 → <b>9 %</b></li><li>Gedächtnis .2 → <b>4 %</b></li></ul>Der Rest bleibt unerklärt.',
      'Matheleistung Intelligenz Motivation Interesse Fleiß Gedächtnis Varianz'),
    C('kausal', 'Teil 2 · Korrelation', 'Warum erlaubt eine Korrelation <b>keine Kausalaussage</b>? (Drei Erklärungen)',
      'Bei einem Zusammenhang zwischen A (Note in Mathe) und B (Intelligenz):<ol><li>A bedingt B</li><li>B bedingt A</li><li>eine <b>dritte Variable C</b> (z. B. Übung) bedingt A und B</li></ol>',
      'Korrelation Kausalität Drittvariable Ursache'),
    C('schuhgroesse', 'Teil 2 · Korrelation', 'Was zeigt das Beispiel <b>Schuhgröße und Einkommen</b> (Konfundierung)?',
      'In einer Stichprobe von 107 Personen: <b>r = .39</b>. Grund: Männer tragen im Schnitt größere Schuhe und verdienen mehr. Nach Geschlecht getrennt <b>nicht signifikant</b> (Männer .11, Frauen −.18).<br>→ <b>Scheinkorrelation</b> durch die Drittvariable Geschlecht.',
      'Schuhgröße Einkommen Konfundierung Scheinkorrelation Geschlecht'),
    C('faktorenanalyse', 'Teil 2 · Faktorenanalyse', 'Was ist die <b>Faktorenanalyse</b> und was ist ihr Ziel?',
      'Sammelbegriff für komplexe <b>mathematische Verfahren</b>, mit denen <b>Korrelationsmuster analysiert</b> werden.<br>Ziel: <b>Reduktion</b> vieler Variablen auf eine <b>kleinere Zahl möglichst unabhängiger Dimensionen/Faktoren</b>.',
      'Faktorenanalyse Reduktion Faktoren Dimensionen Korrelationsmuster'),
    C('faktorladung', 'Teil 2 · Faktorenanalyse', 'Was ist eine <b>Faktorladung</b>?',
      'Die <b>Korrelation zwischen einer Variable (Item) und einem Faktor</b>. Je stärker sich die Ladung von null unterscheidet, desto höher lädt die Variable auf dem Faktor.<br><br><i>Nicht</i> Item↔Item.',
      'Faktorladung Item Faktor Korrelation'),
    C('fa-eigenschaften', 'Teil 2 · Faktorenanalyse', 'Welche <b>Eigenschaften</b> hat die Faktorenanalyse laut Folie?',
      '<ul><li>Die <b>Daten „sprechen“ für sich selbst</b>: kein explizites Modell vorab (das Modell ist das Ziel).</li><li>Zwei <b>Entscheidungen</b> des Forschers: Welches Item gehört zu welchem Faktor? Wie werden die Faktoren <b>benannt</b>?</li><li>Items desselben Faktors <b>hoch korreliert</b>, Faktoren untereinander <b>unkorreliert</b>.</li></ul>',
      'Faktorenanalyse Eigenschaften Modell Items unkorreliert benennen'),
    C('fa-ablauf', 'Teil 2 · Faktorenanalyse', 'Wie läuft die Faktorenanalyse am Beispiel „Fragebogen Zielverfolgung“ ab?',
      '<ol><li>Ausgangspunkt: <b>Korrelationstabelle</b> der 8 Items (A–H)</li><li>Ergebnis: <b>Faktorladungen</b> pro Item auf Faktor 1, 2, 3</li><li><b>Interpretation:</b> Welche Disposition steckt hinter jedem Faktor?</li></ol>Skala der Items: −2 (trifft gar nicht zu) bis +2 (trifft genau zu).',
      'Faktorenanalyse Ablauf Zielverfolgung Fragebogen Korrelationstabelle Interpretation'),
    C('fa-beispiel', 'Teil 2 · Faktorenanalyse', 'Zielverfolgung: Wie heißen die Faktoren und welche Items laden worauf?',
      '<b>Faktor 1 = Hartnäckigkeit</b> (A .57, C .76, H .69)<br><b>Faktor 2 = Flexibilität</b> (B .67, E .88, F .69)<br>Faktor 3 offen („????“), lädt G (.76)<br>D ist uneindeutig (.45 auf Faktor 1 und 2).',
      'Hartnäckigkeit Flexibilität Faktor Items Ladungen Zielverfolgung'),
    C('verwechslung2', 'Teil 2 · Verwechslungsgefahr', 'Welche Verwechslungen sind in Teil 2 klausurtypisch?',
      '<ul><li>Nomothetisch (viele Personen) ≠ ideografisch (eine Person)</li><li>Variation (1 Merkmal) ≠ Korrelation (≥ 2 Merkmale); Psychografie (1 Person) ≠ Komparation (≥ 2 Personen)</li><li>r ≠ r²: r = .5 heißt 25 %</li><li>Faktorladung = Item↔Faktor</li><li>Korrelation ≠ Kausalität (Drittvariablen)</li></ul>',
      'Verwechslungsgefahr nomothetisch ideografisch r2 Faktorladung Kausalität'),
]

CARDS = {'k1': CARDS_K1, 'k2': CARDS_K2}

# ---------------------------------------------------------------- Tests (Kapitel 1–2)
ITEMS = []
def add(**k): ITEMS.append(k)

S1 = 'Teil 1 · Kap. 1'
S2 = 'Teil 2 · Kap. 2'

# Multiple Choice
add(id='pp-mc-01', type='mc', q='Welches Merkmal gehört <b>nicht</b> zur Arbeitsdefinition der Persönlichkeitspsychologie (Asendorpf, 2004)?',
    options=['empirisch', 'überdauernd', 'pathologisch (krankhaft)', 'verhaltensrelevant'], correct=2,
    expl='Die Definition verlangt <b>nicht-pathologisch</b>: untersucht werden gesunde Personen.', src=S1, kw='Definition nichtpathologisch Asendorpf')
add(id='pp-mc-02', type='mc', q='Wie lange muss ein Merkmal mindestens überdauern, um als <b>Disposition</b> zu gelten (Asendorpf)?',
    options=['Stunden bis Tage', 'Wochen oder Monate', 'Mehrere Jahre', 'Ein Leben lang'], correct=1,
    expl='Disposition = <b>mittelfristige</b> Stabilität: zumindest Wochen oder Monate.', src=S1, kw='Disposition Stabilität Wochen Monate')
add(id='pp-mc-03', type='mc', q='Wer bei <b>allen</b> Prüfungen die Nerven verliert, zeigt …',
    options=['Besorgnis als State', 'Prüfungsangst als Trait', 'einen ideografischen Befund', 'eine Scheinkorrelation'], correct=1,
    expl='Über Situationen hinweg stabil = <b>Trait</b> (Prüfungsangst).', src=S1, kw='Trait Prüfungsangst Prüfung')
add(id='pp-mc-04', type='mc', q='Sich für eine Prüfung nicht vorbereitet zu haben führt zu Besorgnis. Das ist …',
    options=['ein Trait', 'ein State', 'ein Konstrukt 2. Ordnung', 'eine Faktorladung'], correct=1,
    expl='Aktueller, situationsabhängiger Zustand = <b>State</b>.', src=S1, kw='State Besorgnis Prüfung')
add(id='pp-mc-05', type='mc', q='Lisa reagiert in allen acht Situationen mit Angst, Anna je nach Situation unterschiedlich. Was stimmt?',
    options=['Lisa: State-Angst, Anna: Trait-Angst', 'Lisa: Trait-Angst, Anna: State-Angst', 'Beide zeigen Trait-Angst', 'Beide zeigen State-Angst'], correct=1,
    expl='Stabil über Situationen = Trait (Lisa); situationsabhängig = State (Anna).', src=S1, kw='Lisa Anna Trait State Angst')
add(id='pp-mc-06', type='mc', q='Was beschreibt ein <b>latentes Konstrukt</b> am besten?',
    options=['Ein direkt beobachtbares Verhalten', 'Ein nicht direkt beobachtbarer Sachverhalt, der aus Indikatoren erschlossen wird', 'Ein Messwert eines Tests', 'Ein statistisches Maß für Streuung'], correct=1,
    expl='Konstrukte sind theoretischer Natur und werden über messbare <b>Indikatoren</b> erschlossen.', src=S1, kw='Konstrukt latent Indikatoren')
add(id='pp-mc-07', type='mc', q='Wie heißt das Erschließen eines Konstrukts aus messbaren Indikatoren?',
    options=['Konfundierung', 'Operationalisierung', 'Normierung', 'Faktorisierung'], correct=1,
    expl='Der Prozess des Erschließens heißt <b>Operationalisierung</b>.', src=S1, kw='Operationalisierung Konstrukt')
add(id='pp-mc-08', type='mc', q='Was ist mit der „Ökonomie von Konstrukten“ gemeint?',
    options=['Konstrukte sparen Testzeit', 'Ein Konstrukt (z. B. Ängstlichkeit) fasst viele Beobachtungen sparsam zusammen', 'Konstrukte sind kostenlos messbar', 'Jede Beobachtung braucht ein eigenes Konstrukt'], correct=1,
    expl='Verschiedene Ereignisse führen zu denselben Beobachtungen, die <b>ein</b> Konstrukt zusammenfasst.', src=S1, kw='Ökonomie Konstrukt Ängstlichkeit')
add(id='pp-mc-09', type='mc', q='Welcher Ansatz untersucht <b>eine</b> Disposition an <b>vielen</b> Individuen?',
    options=['Ideografischer Ansatz', 'Nomothetischer Ansatz', 'Psychografischer Ansatz', 'Komparationsansatz'], correct=1,
    expl='<b>Nomothetisch</b>: eine Disposition, viele Personen. Ideografisch: viele Dispositionen, ein Individuum.', src=S2, kw='nomothetisch ideografisch')
add(id='pp-mc-10', type='mc', q='Eine Lehrkraft vergleicht alle Schüler der Klasse 4a auf einer Disposition mit dem <b>Klassenmittelwert</b>. Welcher Ansatz?',
    options=['Ideografisch', 'Nomothetisch', 'Psychografisch', 'Keiner, das ist keine Forschung'], correct=1,
    expl='Position aller Schüler im Vergleich zum Mittelwert = <b>nomothetisch</b>. Das Profil einer einzelnen Schülerin wäre ideografisch.', src=S2, kw='Klassenmittelwert nomothetisch Schule')
add(id='pp-mc-11', type='mc', q='Wie heißt das Schema „<b>eine</b> Individualität, <b>viele</b> Merkmale“?',
    options=['Variationsforschung', 'Korrelationsforschung', 'Psychografie', 'Komparationsforschung'], correct=2,
    expl='<b>Psychografie</b>. Komparationsforschung = zwei oder mehr Individualitäten.', src=S2, kw='Psychografie Komparationsforschung')
add(id='pp-mc-12', type='mc', q='Wie heißt das Schema „<b>zwei oder mehr</b> Merkmale an <b>vielen</b> Individuen“?',
    options=['Variationsforschung', 'Korrelationsforschung', 'Psychografie', 'Komparationsforschung'], correct=1,
    expl='<b>Korrelationsforschung</b>. Variationsforschung = nur ein Merkmal.', src=S2, kw='Korrelationsforschung Variationsforschung')
add(id='pp-mc-13', type='mc', q='Matheleistung und Intelligenz korrelieren mit r = .5. Wie viel Varianz der Matheleistung wird durch Intelligenz erklärt?',
    options=['5 %', '25 %', '50 %', '75 %'], correct=1,
    expl='r² = .25 → <b>25 %</b>. Nicht 50 %!', src=S2, kw='r2 Bestimmtheitsmaß Varianz Matheleistung Intelligenz')
add(id='pp-mc-14', type='mc', q='Ab welcher Größenordnung spricht die Folie ungefähr von einer <b>hohen</b> Korrelation?',
    options=['ab r = .1', 'ab r = .3', 'ab r = .5', 'ab r = .9'], correct=2,
    expl='Bis .3 gering, ab ca. <b>.5 hoch</b>, ab ca. .7–.8 (sehr) hoch.', src=S2, kw='Korrelation Größenordnung')
add(id='pp-mc-15', type='mc', q='Schuhgröße korreliert (r = .39) mit dem Einkommen. Warum?',
    options=['Große Füße verursachen höheres Einkommen', 'Die Drittvariable Geschlecht (Konfundierung)', 'Zufall bei einer zu kleinen Stichprobe von 5 Personen', 'Einkommen verursacht größere Füße'], correct=1,
    expl='Männer tragen größere Schuhe und verdienen im Schnitt mehr. Getrennt nach Geschlecht verschwindet die Korrelation (<b>Scheinkorrelation</b>).', src=S2, kw='Schuhgröße Einkommen Konfundierung')
add(id='pp-mc-16', type='mc', q='Was ist eine <b>Faktorladung</b>?',
    options=['Korrelation zwischen zwei Items', 'Korrelation zwischen einer Variable (Item) und einem Faktor', 'Anzahl der Faktoren', 'Varianz eines Faktors'], correct=1,
    expl='Faktorladung = Korrelation <b>Item ↔ Faktor</b>.', src=S2, kw='Faktorladung Item Faktor')
add(id='pp-mc-17', type='mc', q='Was ist das Ziel der <b>Faktorenanalyse</b>?',
    options=['Ursachen von Verhalten nachweisen', 'Viele Variablen auf wenige möglichst unabhängige Faktoren reduzieren', 'Mittelwerte vergleichen', 'Einzelne Personen diagnostizieren'], correct=1,
    expl='<b>Reduktion</b> einer größeren Zahl von Variablen auf eine kleinere Zahl möglichst unabhängiger Faktoren.', src=S2, kw='Faktorenanalyse Reduktion')
add(id='pp-mc-18', type='mc', q='Welche Aussage zu Faktoren stimmt?',
    options=['Items desselben Faktors sollen unkorreliert sein', 'Items desselben Faktors sollen hoch korreliert, die Faktoren untereinander unkorreliert sein', 'Alle Faktoren sollen hoch miteinander korrelieren', 'Faktoren müssen vorab als Modell festgelegt werden'], correct=1,
    expl='Beobachtete Variablen eines Faktors: hoch korreliert; Faktoren untereinander: unkorreliert.', src=S2, kw='Faktoren Items korreliert unkorreliert')
add(id='pp-mc-19', type='mc', q='Im Beispiel „Fragebogen Zielverfolgung“ steht Faktor 1 für …',
    options=['Flexibilität', 'Hartnäckigkeit', 'Gewissenhaftigkeit', 'Prüfungsangst'], correct=1,
    expl='Faktor 1 = <b>Hartnäckigkeit</b>, Faktor 2 = <b>Flexibilität</b>, Faktor 3 offen.', src=S2, kw='Zielverfolgung Hartnäckigkeit Flexibilität Faktor')
add(id='pp-mc-20', type='mc', q='Zu welchem Ansatz gehört die <b>korrelative Forschung</b>?',
    options=['Ideografisch', 'Nomothetisch', 'Experimentell-ideografisch', 'Psychografisch'], correct=1,
    expl='Untersuchung vieler Personen = <b>nomothetisch</b>.', src=S2, kw='korrelative Forschung nomothetisch')

# Richtig / Falsch
add(id='pp-tf-01', type='tf', statement='Die Persönlichkeitspsychologie untersucht in ihrer Arbeitsdefinition vor allem Menschen mit psychischen Störungen.', answer=False,
    expl='Sie untersucht <b>nicht-pathologische</b>, also gesunde Personen.', src=S1, kw='nichtpathologisch Definition')
add(id='pp-tf-02', type='tf', statement='Eigenschaften sind Dimensionen (Kontinuum): jede Person liegt irgendwo auf der Skala.', answer=True,
    expl='Eigenschaften sind keine Kategorien, sondern Kontinua, meist normalverteilt.', src=S1, kw='Kontinuum Normalverteilung Eigenschaften')
add(id='pp-tf-03', type='tf', statement='Dispositionen sind direkt beobachtbar.', answer=False,
    expl='Dispositionen sind <b>Konstrukte</b>: nicht direkt beobachtbar, nur über Indikatoren erschlossen.', src=S1, kw='Disposition Konstrukt beobachtbar')
add(id='pp-tf-04', type='tf', statement='State-Angst ist über Situationen hinweg stabil.', answer=False,
    expl='Stabil über Situationen ist der <b>Trait</b>. Ein State variiert.', src=S1, kw='State Trait Angst')
add(id='pp-tf-05', type='tf', statement='Eine Disposition ist nach Asendorpf mindestens wochen- oder monatelang stabil.', answer=True,
    expl='Mittelfristige Stabilität: zumindest Wochen oder Monate.', src=S1, kw='Disposition Stabilität')
add(id='pp-tf-06', type='tf', statement='Der Zweck der Alltagspsychologie ist es, Menschen zu beschreiben sowie ihr Verhalten zu erklären und vorherzusagen.', answer=True,
    expl='Beschreiben, erklären, vorhersagen.', src=S1, kw='Alltagspsychologie')
add(id='pp-tf-07', type='tf', statement='Variationsforschung untersucht ein Merkmal an vielen Individuen.', answer=True,
    expl='Ja, nomothetisch. Korrelationsforschung: zwei oder mehr Merkmale.', src=S2, kw='Variationsforschung')
add(id='pp-tf-08', type='tf', statement='Eine Korrelation von r = .5 bedeutet, dass 50 % der Varianz erklärt werden.', answer=False,
    expl='r² = .25, also <b>25 %</b>.', src=S2, kw='r2 Varianz')
add(id='pp-tf-09', type='tf', statement='Korrelationen erlauben keine Kausalaussagen.', answer=True,
    expl='Es kann A→B, B→A oder eine Drittvariable C wirken.', src=S2, kw='Korrelation Kausalität')
add(id='pp-tf-10', type='tf', statement='Ohne Streuung (keine Varianz) lässt sich eine Korrelation berechnen.', answer=False,
    expl='Ohne Varianz (Beispiel Aliens) ist keine Korrelation berechenbar.', src=S2, kw='Varianz Korrelation Aliens')
add(id='pp-tf-11', type='tf', statement='Sehr hohe Korrelationen sind in der Psychologie selten.', answer=True,
    expl='Ein Phänomen wird selten nur von einem anderen beeinflusst.', src=S2, kw='Korrelation selten')
add(id='pp-tf-12', type='tf', statement='Bei der Faktorenanalyse wird vorab ein explizites Modell festgelegt.', answer=False,
    expl='Die Daten „sprechen“ für sich selbst. Das Modell ist das <b>Ziel</b>, nicht der Ausgangspunkt.', src=S2, kw='Faktorenanalyse Modell')
add(id='pp-tf-13', type='tf', statement='Im Beispiel der Zielverfolgung lädt Item G hauptsächlich auf Faktor 3.', answer=True,
    expl='G lädt mit .76 auf Faktor 3.', src=S2, kw='Faktorladung Item G Faktor 3')

# Lückentext
add(id='pp-gap-01', type='gap', text='Persönlichkeitspsychologie ist die {{empirische}} Wissenschaft von den {{überdauernden}}, nichtpathologischen, verhaltensrelevanten individuellen Besonderheiten von Menschen innerhalb einer bestimmten {{Population}}.',
    expl='Arbeitsdefinition nach Asendorpf (2004).', src=S1, kw='Definition empirisch überdauernd Population')
add(id='pp-gap-02', type='gap', text='Merkmale, die Verhalten steuern oder beeinflussen, heißen Eigenschaften, Dispositionen oder {{Traits|Trait}}.',
    expl='Eigenschaft = Disposition = Trait.', src=S1, kw='Eigenschaft Disposition Trait')
add(id='pp-gap-03', type='gap', text='Das Erschließen eines Konstrukts aus messbaren Indikatoren heißt {{Operationalisierung}}.',
    expl='Latente Konstrukte werden operationalisiert.', src=S1, kw='Operationalisierung Konstrukt')
add(id='pp-gap-04', type='gap', text='Der aktuelle, über Situationen hinweg variierende Zustand einer Person heißt {{State}}.',
    expl='Gegenstück zum überdauernden Trait.', src=S1, kw='State Zustand')
add(id='pp-gap-05', type='gap', text='Der {{nomothetische}} Ansatz untersucht eine Disposition an vielen Individuen, der {{ideografische|idiografische|ideographische}} viele Dispositionen an einem Individuum.',
    expl='Merkhilfe: ideografisch = das Individuum.', src=S2, kw='nomothetisch ideografisch')
add(id='pp-gap-06', type='gap', text='Eine Korrelation von r = .5 erklärt {{25}} Prozent der Varianz.',
    expl='r² = .25.', src=S2, kw='r2 Varianz Korrelation')
add(id='pp-gap-07', type='gap', text='Eine Scheinkorrelation durch eine dritte Variable (z. B. Geschlecht bei Schuhgröße und Einkommen) nennt man {{Konfundierung}}.',
    expl='Konfundierung: Vermischung zweier Einflüsse.', src=S2, kw='Konfundierung Scheinkorrelation')
add(id='pp-gap-08', type='gap', text='Eine Faktorladung ist die {{Korrelation}} zwischen einer Variable (Item) und einem {{Faktor}}.',
    expl='Item ↔ Faktor, nicht Item ↔ Item.', src=S2, kw='Faktorladung Korrelation Faktor')
