# Psycho 2 · Persönlichkeitspsychologie · Teil 3 (Geschichte und Persönlichkeitstheorien), geteilt in Kap. 3a und 3b
# Quelle: Zusammenfassung_PersPsych_Teil1-5.md, Teil 3. Klärungen von Konsti (13. Nov. 2026):
# - Viersäftelehre: nur Saft – Organ – Beschreibung abfragen (Organe von Konsti ergänzt), keine Temperament-Namen, keine Elemente.
# - Behaviorismus 1920–1979 und „idiografische Forschungsausrichtung“ bei Pawlow/Skinner stimmen so.
# - Okzipitallappen „Verarbeitung von Gedanken“ weglassen.
# - Ergänzungen, die nicht auf den Folien stehen, nur als markierter Hinweis auf Karten, nie in Testfragen.
# - Werte aus Grafiken (Lewis & Duncan) nicht abfragen.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

def H(t):
    return '<p><i>Hinweis (nicht auf der Folie): ' + t + '</i></p>'

GA = 'Teil 3 · Geschichte'
EA = 'Teil 3 · Eigenschaftsparadigma'
BE = 'Teil 3 · Behaviorismus'
EV = 'Teil 3 · Evolutionspsychologie'
IV = 'Teil 3 · Informationsverarbeitung'
NW = 'Teil 3 · Neurowissenschaft'

# ---------------------------------------------------------------- Kapitel 3a
CARDS_K3A = [
    C('persona', GA, 'Welche <b>vier Bedeutungen</b> hatte „persona“ (Maske) in der Antike nach <b>Cicero</b>?',
      '<ol><li>Wie man anderen <b>erscheint</b> (aber nicht ist)</li><li>Die <b>Rolle</b>, die jemand im Leben spielt</li><li>Eine <b>Häufung persönlicher Eigenschaften</b>, die jemanden zu seiner Arbeit befähigen</li><li><b>Besonderheit und Würde</b> (z. B. ein bestimmter Stil)</li></ol><p>Cicero (106–43 v. Chr.), nach Laux (2003).</p>',
      'persona Maske Cicero Laux Rolle Würde'),
    C('galenus', GA, 'Was verknüpfte <b>Galenus von Pergamon</b> (1. Jh. n. Chr.)?',
      'Die <b>Viersäftelehre</b> mit der <b>Lehre von den vier Temperamenten</b>.',
      'Galenus Pergamon Viersäftelehre Temperamente'),
    C('saefte', GA, 'Viersäftelehre: Welcher <b>Saft</b> gehört zu welchem <b>Organ</b> und welcher <b>Beschreibung</b>?',
      '<table><tr><th>Saft</th><th>Organ</th><th>Beschreibung</th></tr><tr><td>Blut</td><td>Herz</td><td>heiter, optimistisch</td></tr><tr><td>Schleim</td><td>Gehirn</td><td>langsam, apathisch</td></tr><tr><td>gelbe Galle</td><td>Leber</td><td>wütend, jähzornig</td></tr><tr><td>schwarze Galle</td><td>Milz</td><td>traurig, depressiv</td></tr></table>',
      'Viersäftelehre Blut Herz Schleim Gehirn gelbe Galle Leber schwarze Galle Milz heiter jähzornig traurig apathisch'),
    C('kretschmer', GA, 'Welche <b>Körperbautypen</b> unterschied <b>Ernst Kretschmer</b> (1888–1964)?',
      '<p>Zusammenhänge zwischen <b>körperlichen Merkmalen und Charakter</b>:</p><table><tr><th>Typ</th><th>Störung</th><th>Temperament</th></tr><tr><td><b>Leptosom</b> (leptos = fein): schmal</td><td>Schizophrenie</td><td>schizothym</td></tr><tr><td><b>Athletisch</b> (zum Wettkampf geeignet): muskulös</td><td>Epilepsie</td><td>viskös</td></tr><tr><td><b>Pyknisch</b> (pyknos = dicht, fest): rundlich</td><td>Depression–Manie</td><td>zyklothym</td></tr></table>',
      'Kretschmer Körperbau leptosom athletisch pyknisch schizothym viskös zyklothym'),
    C('kretschmer-charakter', GA, 'Welchen <b>Charakter</b> schrieb Kretschmer den drei Körperbautypen zu?',
      '<ul><li><b>Leptosom:</b> abstraktes Denken, befasst sich mit Details, denkt viel nach – ein „Kopfmensch“.</li><li><b>Athletisch:</b> anhänglich, wenig innovativ, aber stark und durchsetzungsfähig; leicht zu überrumpeln, durchdenkt Dinge wenig intensiv.</li><li><b>Pyknisch:</b> gemütlich, gesellig, erträglich; isst gern, lässt den Dingen ihren Lauf; anfällig für Stimmungsschwankungen.</li></ul>',
      'Kretschmer Kopfmensch leptosom athletisch pyknisch gesellig'),
    C('kretschmer-kritik', GA, 'Wie wird Kretschmers Typologie <b>bewertet</b>?',
      '<ul><li>Körperbau und Temperament sind <b>konfundiert</b> (beide <b>alterskorreliert</b>).</li><li>Die Zusammenhänge waren <b>altersbedingte Scheinkorrelationen</b>.</li><li>Dennoch gibt es einen <b>schwachen</b> Zusammenhang zwischen Körperbau und Persönlichkeit.</li><li>Unklar, was die Zusammenhänge bedeuten (<b>Problem der Interpretation von Korrelationen</b>).</li></ul>',
      'Kretschmer Bewertung konfundiert Alter Scheinkorrelation'),
    C('beginn', GA, 'Wann und wie entstand die <b>wissenschaftliche</b> Persönlichkeitspsychologie?',
      'In der <b>ersten Hälfte des 20. Jahrhunderts</b> als eigenständiges Fach <b>neben den Hauptströmungen Behaviorismus und Psychoanalyse</b>. Fokus auf den <b>Eigenschaftsbegriff</b>, Zugang über <b>alltagssprachliche Eigenschaftszuschreibungen</b>.',
      'Beginn 20. Jahrhundert Behaviorismus Psychoanalyse Eigenschaftsbegriff'),
    C('paradigmen', 'Teil 3 · Paradigmen', '„Warum ist Lara so intelligent?“ – Was antworten die <b>fünf Paradigmen</b>?',
      '<table><tr><th>Paradigma</th><th>Antwort</th></tr><tr><td>Eigenschaft</td><td>Weil sie einen hohen IQ hat.</td></tr><tr><td>Evolutionspsychologie</td><td>Weil sie gut angepasste Gene hat.</td></tr><tr><td>Behaviorismus</td><td>Weil sie oft für kognitive Leistungen belohnt wurde.</td></tr><tr><td>Informationsverarbeitung</td><td>Weil ihr Arbeitsgedächtnis effizient arbeitet.</td></tr><tr><td>Neurowissenschaft</td><td>Weil ihre Nervenfasern gut isoliert sind.</td></tr></table>',
      'Paradigmen Lara intelligent Eigenschaft Evolution Behaviorismus Informationsverarbeitung Neurowissenschaft'),
    C('eig-def', EA, 'Was ist das <b>Eigenschaftsparadigma</b> (dispositionaler Ansatz)?',
      'Klassifikationen der Persönlichkeit: die <b>wissenschaftliche Suche nach den grundlegenden Dimensionen, auf denen sich Personen voneinander unterscheiden</b>.',
      'Eigenschaftsparadigma dispositionaler Ansatz Dimensionen'),
    C('sediment', EA, 'Was besagt die <b>Sedimentationshypothese</b> (Klages, 1926)?',
      'Eigenschaften, die für den Alltag besonders wichtig sind, finden Eingang in die <b>naive Persönlichkeitstheorie</b> (Alltagssprache). Je wichtiger, desto eher werden sie in <b>einem einzigen Wort</b> abgebildet – einem <b>Adjektiv oder Substantiv, seltener einem Verb</b>.',
      'Sedimentationshypothese Klages Alltagssprache Adjektiv Substantiv'),
    C('differentiell', EA, 'Was besagt der <b>differentielle Ansatz</b>?',
      '<ul><li>Persönlichkeitseigenschaften sind <b>Merkmale, die eine Population charakterisieren</b>, nicht Merkmale der Person.</li><li>Merkmal der Person ist, <b>welche Ausprägung</b> sie auf einer Eigenschaft zeigt.</li><li><b>Persönlichkeit einer Person</b> = Gesamtheit ihrer Merkmalsausprägungen in allen Merkmalen, in denen sich die Mitglieder einer Population unterscheiden.</li><li>Veranschaulicht durch ein <b>Persönlichkeitsprofil</b>.</li></ul>',
      'differentieller Ansatz Population Ausprägung Persönlichkeitsprofil'),
    C('eig-konzept', EA, 'Welches <b>Persönlichkeitskonzept</b> hat das Eigenschaftsparadigma?',
      'Reaktionen entstehen auf <b>komplexe Situationen</b>. Es gibt <b>funktionale Abhängigkeiten zwischen Situation und Reaktion aufgrund von Eigenschaften</b>: Eigenschaften bestimmen die Reaktion in einer spezifischen Situation.',
      'Persönlichkeitskonzept Situation Reaktion Eigenschaften'),
    C('cattell-vorgehen', EA, 'Wie ging <b>Raymond B. Cattell</b> (1905–1998) vor?',
      '<p>Frage: Welches <b>Variablensystem</b> beschreibt Personenmerkmale angemessen und umfassend?</p><ol><li>Sammlung von <b>Alltagsbegriffen</b></li><li><b>Eliminierung ähnlicher Wörter</b></li><li>Reduktion auf eine sinnvolle Variablenmenge</li><li>Beschreibung von Personen mit den verbliebenen Variablen</li><li>Korrelationen betrachten und <b>Reduktion mittels Faktorenanalyse</b></li></ol>' + H('In der Literatur heißt dieses Vorgehen „lexikalischer Ansatz“.'),
      'Cattell Vorgehen Alltagsbegriffe Faktorenanalyse lexikalisch'),
    C('cattell-16pf', EA, 'Was war Cattells <b>Ergebnis</b>?',
      '<b>16 Persönlichkeitsfaktoren</b> → Fragebogen <b>16PF</b> (16 Personality Factors). Deutsche Version: <b>16PF-R</b> (Schneewind &amp; Graf, 1998).<br><b>Problem:</b> Einige Faktoren <b>korrelieren hoch miteinander</b>.',
      'Cattell 16PF 16PF-R Schneewind Graf Faktoren korrelieren'),
    C('cattell-1-8', EA, 'Cattells 16 Faktoren: Wie heißen <b>Faktor 1–8</b>?',
      '<ol><li>Wärme (z. B. Wohlfühlen in Gesellschaft)</li><li>Logisches Schlussfolgern</li><li>Emotionale Stabilität</li><li>Dominanz</li><li>Lebhaftigkeit</li><li>Regelbewusstsein (z. B. Moral)</li><li>Soziale Kompetenz (Kontaktfreude, Selbstsicherheit)</li><li>Empfindsamkeit</li></ol>',
      'Cattell 16PF Wärme Dominanz Lebhaftigkeit Regelbewusstsein Empfindsamkeit'),
    C('cattell-9-16', EA, 'Cattells 16 Faktoren: Wie heißen <b>Faktor 9–16</b>?',
      '<ol start="9"><li>Wachsamkeit (z. B. Misstrauen)</li><li>Abgehobenheit (z. B. Realitätsnähe)</li><li>Privatheit (z. B. Umgang mit Problemen)</li><li>Besorgtheit</li><li>Offenheit für Veränderungen</li><li>Selbstgenügsamkeit</li><li>Perfektionismus</li><li>Anspannung</li></ol>',
      'Cattell 16PF Wachsamkeit Abgehobenheit Privatheit Besorgtheit Perfektionismus Anspannung'),
    C('eysenck-kritik', EA, 'Was kritisierte <b>Hans Jürgen Eysenck</b> (1916–1997) an Cattell, und was entwickelte er?',
      'Die <b>Interkorrelationen</b> der 16 Faktoren weisen auf <b>Faktoren 2. Ordnung</b> hin. Eysenck entwickelte ein <b>hierarchisches Modell</b>: Persönlichkeit lässt sich <b>sparsamer</b> durch nur <b>drei Faktoren zweiter Ordnung (Supertraits)</b> beschreiben.<br>Zentrale Frage: Auf welcher Ebene liegen die Eigenschaften, die in Anzahl und Art <b>notwendig und ausreichend</b> sind?',
      'Eysenck Kritik Cattell Faktoren 2. Ordnung Supertraits hierarchisch'),
    C('eysenck-typen', EA, 'Was meinte Eysenck mit <b>Persönlichkeitstypen</b>?',
      'Dimensionen, die <b>normalverteilt</b> sind und auf denen alle Menschen eingeordnet werden können. Etwa <b>2/3 der Bevölkerung</b> liegen im mittleren Bereich jeder Dimension.',
      'Eysenck Typen normalverteilt zwei Drittel'),
    C('pen', EA, 'Wofür steht <b>PEN</b> (Eysenck), und wie heißt sein Fragebogen?',
      '<ul><li><b>P</b> – Psychotizismus vs. Über-Ich-Funktion</li><li><b>E</b> – Extraversion vs. Introversion</li><li><b>N</b> – Neurotizismus vs. Emotionale Stabilität</li></ul>Fragebogen: <b>EPQ</b> (Eysenck Personality Questionnaire).',
      'PEN Psychotizismus Extraversion Neurotizismus EPQ Eysenck'),
    C('hierarchie', EA, 'Welche <b>vier Ebenen</b> hat Eysencks Hierarchie am Beispiel Extraversion?',
      '<ol><li><b>Typ-Level:</b> Extraversion</li><li><b>Trait-Level:</b> Soziabilität, Impulsivität, Aktivität, Lebendigkeit</li><li><b>Verhaltenslevel – Gewohnheiten:</b> z. B. Vereine, Sport</li><li><b>Verhaltenslevel – spezifisches Verhalten:</b> z. B. DRK, Schützenverein, Tennis, Reiten</li></ol>',
      'Hierarchie Typ Trait Gewohnheiten spezifisches Verhalten Extraversion'),
    C('extra', EA, 'Wie werden <b>Extraversion</b> und <b>Introversion</b> beschrieben?',
      '<ul><li><b>Extraversion:</b> Orientierung an <b>externen Stimulationsquellen</b>; Anregung aus sozialer und physischer Umgebung; sozial aktiv, nach außen ausgerichtet.</li><li><b>Introversion:</b> passiver, stiller, nüchterner, reservierter, nachdenklicher; <b>Orientierung nach innen</b>.</li></ul><p>Trait-Level Extravertierter: Geselligkeit, Lebhaftigkeit, Aktivität, Selbstbehauptung, Sensationshunger, Sorglosigkeit, Dominanz, Aufgeschlossenheit, Abenteuerlust.</p>',
      'Extraversion Introversion externe Stimulation Sensationshunger'),
    C('extra-befunde', EA, 'Welche <b>Befunde zu Extraversion</b> gibt es?',
      '<ul><li>Positive Korrelation mit <b>Optimismus</b> und der <b>Suche nach sozialer Unterstützung</b> (Amirkhan, Risinger &amp; Swickert, 1995)</li><li>Extravertierte reagieren <b>stärker auf positive als auf negative Stimuli</b> (Carpenter, 2001)</li><li>Positive Korrelation mit der <b>Valenz von Emotionen</b> (Lucas &amp; Fujita, 2000; Lucas, Diener et al., 2000)</li><li>Bei <b>Multi-Tasking schneller</b> als Introvertierte (Lieberman &amp; Rosenthal, 2001)</li></ul>',
      'Extraversion Befunde Optimismus Carpenter Multitasking Lieberman Rosenthal'),
    C('neuro', EA, 'Wie werden <b>Neurotizismus</b> und <b>Emotionale Stabilität</b> beschrieben?',
      '<ul><li><b>Neurotizismus:</b> labil, emotional schnell störbar</li><li><b>Emotionale Stabilität:</b> ausgeglichen, emotional stabil</li></ul><p>Trait-Level Neurotischer: Ängstlichkeit, Bedrücktsein, Schuldgefühle, geringe Selbstachtung, Anspannung, Irrationalität, Schüchternheit, Launenhaftigkeit, hohe Emotionalität.</p>',
      'Neurotizismus emotionale Stabilität labil Ängstlichkeit'),
    C('neuro-befunde', EA, 'Welche <b>Befunde zu Neurotizismus</b> gibt es?',
      '<ul><li>Emotionale Stabilität hängt <b>positiv mit Zufriedenheit in Schule und Studium</b> zusammen (Giesen et al., 1986)</li><li>Hoher Neurotizismus: <b>mehr negative Erfahrungen</b> werden erinnert und berichtet</li><li>Positiver Zusammenhang mit <b>Stimmungsschwankungen</b> und <b>Vulnerabilität für depressive Verstimmungen</b> (Saklofske, Kelly &amp; Janzen, 1995)</li><li>Bei Männern und Frauen <b>geringeres Selbstvertrauen</b> (Marusic, Bratko &amp; Zarevski, 1995)</li></ul>',
      'Neurotizismus Befunde Giesen Saklofske Marusic Selbstvertrauen'),
    C('psycho', EA, 'Wie werden <b>Psychotizismus</b> und <b>Über-Ich-Funktion</b> beschrieben?',
      '<ul><li><b>Psychotizismus:</b> Anfälligkeit für Störungen mit <b>geringem Realitätsbezug</b>, Neigung zu <b>soziopathischem Verhalten</b>, mangelnde Loyalität</li><li><b>Über-Ich-Funktion:</b> extreme Angepasstheit, „Kadavergehorsam“, Unterwürfigkeit, Regelorientierung</li></ul><p>Trait-Level: Aggressivität, Kälte, Egozentrik, Unpersönlichkeit, Impulsivität, antisoziale Tendenz, Uneinfühlsamkeit, <b>Kreativität</b>, Härte, Hartherzigkeit.</p>',
      'Psychotizismus Über-Ich Kadavergehorsam Kreativität soziopathisch'),
    C('psycho-befunde', EA, 'Welche <b>Befunde zu Psychotizismus</b> gibt es?',
      '<ul><li><b>Männer &gt; Frauen</b>, <b>Häftlinge &gt; Nicht-Häftlinge</b>, zum Teil erblich (Liebert &amp; Liebert, 1998)</li><li>Positive Korrelation mit <b>ablehnender Haltung gegenüber Autoritäten</b> (Rigby &amp; Slee, 1987)</li><li><b>Negative</b> Korrelation mit <b>akademischer Leistung</b> (Furnham &amp; Medhurst, 1995)</li></ul>',
      'Psychotizismus Befunde Häftlinge Autoritäten akademische Leistung Furnham'),
    C('fernbedienung', EA, 'Was zeigte die <b>Fernbedienungs-Studie</b> (Weaver, Walker, McCord &amp; Bellamy, 1996)?',
      'EPQ und Fragebogen zur Fernbedienungsnutzung, 600 Vpn:<ul><li>Hoher <b>Psychotizismus → offensive</b> Nutzung (andere dominieren)</li><li>Hoher <b>Neurotizismus → defensive</b> Nutzung (unerwünschte Inhalte vermeiden)</li></ul>',
      'Fernbedienung Weaver offensiv defensiv Psychotizismus Neurotizismus'),
    C('bigfive-entstehung', EA, 'Wie entstand das <b>Fünf-Faktoren-Modell</b> („Big Five“)?',
      '<b>McCrae &amp; Costa</b> (1985, 1987): Aus <b>Listen mit über 18.000 Begriffen</b> wurden per <b>Faktorenanalyse</b> fünf <b>sehr stabile, unabhängige und weitgehend kulturstabile</b> Faktoren gewonnen. Fragebogen: <b>NEO-FFI</b> (NEO-Fünf-Faktoren-Inventar).',
      'Big Five McCrae Costa 18000 NEO-FFI'),
    C('bigfive', EA, 'Wie heißen die <b>Big Five</b> und ihre typischen Eigenschaften?',
      '<table><tr><th>Faktor</th><th>typisch</th></tr><tr><td><b>Offenheit für Erfahrungen</b> (Openness; Kultur, Intellekt)</td><td>Gebildetheit, Kreativität, Gefühl für Kunst</td></tr><tr><td><b>Gewissenhaftigkeit</b> (Conscientiousness)</td><td>Ordentlichkeit, Beharrlichkeit, Zuverlässigkeit</td></tr><tr><td><b>Extraversion</b> (Surgency)</td><td>Geselligkeit, Nicht-Schüchternheit, Aktivität</td></tr><tr><td><b>Verträglichkeit</b> (Agreeableness; Liebenswürdigkeit)</td><td>Wärme, Toleranz, Hilfsbereitschaft</td></tr><tr><td><b>Neurotizismus</b> (Emotionale Instabilität)</td><td>Ängstlichkeit, Reizbarkeit, Depression, Verletzlichkeit</td></tr></table>' + H('Merkwort OCEAN.'),
      'Big Five Offenheit Gewissenhaftigkeit Extraversion Verträglichkeit Neurotizismus OCEAN'),
    C('bigfive-befunde', EA, 'Welche <b>allgemeinen Befunde</b> gibt es zu den Big Five?',
      '<ul><li>Mit <b>verschiedenen Datenquellen</b> nachweisbar (Fragebogen, Q-, L-, T-Daten)</li><li>Auch für <b>Kinder und Jugendliche</b> geeignet (Digman, 1989; Asendorpf &amp; van Aken, 2003; Kohnstamm et al., 1995)</li><li>Bei <b>Erwachsenen sehr stabil</b> (Costa &amp; McCrae, 1988)</li><li>Gut bestätigt im <b>angloamerikanischen und nordeuropäischen Raum</b></li></ul>',
      'Big Five Befunde Datenquellen Kinder stabil Digman'),
    C('bigfive-einzel', EA, 'Welche Befunde gibt es zu <b>Offenheit, Verträglichkeit und Gewissenhaftigkeit</b>?',
      '<ul><li><b>Offenheit:</b> suchen aktiv Bildungsmöglichkeiten und berufliche Herausforderungen (Barrick &amp; Mount, 1991); <b>leichter hypnotisierbar</b> (Roche &amp; McConkey, 1990); <b>positiv mit Intelligenz</b> korreliert</li><li><b>Verträglichkeit:</b> in Verbindung mit <b>politischer Gesinnung</b></li><li><b>Gewissenhaftigkeit:</b> positiv korreliert mit <b>akademischem und beruflichem Erfolg</b></li></ul>',
      'Offenheit hypnotisierbar Intelligenz Verträglichkeit politisch Gewissenhaftigkeit Erfolg'),
    C('kritik', EA, 'Welche <b>Kritik</b> gibt es am dispositionalen Ansatz (8 Punkte)?',
      '<ol><li>Mangel an <b>theoretischen Konzepten</b></li><li>Mangel an <b>adäquaten Erklärungen</b> von Verhalten</li><li><b>Individuelles Verhalten</b> kann nicht vorhergesagt werden</li><li><b>Situative Faktoren</b> werden unterschätzt</li><li>Nicht spezifiziert, <b>wann</b> sich Dispositionen in Verhalten zeigen</li><li><b>Persönlichkeitsentwicklung/-veränderung</b> zu wenig berücksichtigt</li><li>Faktorenanalysen enthalten <b>viele subjektive Entscheidungen</b></li><li><b>Soziale Erwünschtheit</b> in Selbstberichten und Einschätzungen durch Verwandte/Freunde</li></ol>',
      'Kritik dispositionaler Ansatz situative Faktoren soziale Erwünschtheit'),
    C('vergleich', EA, '<b>Cattell, Eysenck, McCrae &amp; Costa</b>: Wie viele Faktoren, welcher Fragebogen?',
      '<table><tr><th>Wer</th><th>Faktoren</th><th>Fragebogen</th></tr><tr><td>Cattell</td><td>16</td><td>16PF</td></tr><tr><td>Eysenck</td><td>3 (PEN, Supertraits)</td><td>EPQ</td></tr><tr><td>McCrae &amp; Costa</td><td>5 (Big Five)</td><td>NEO-FFI</td></tr></table>',
      'Cattell Eysenck McCrae Costa 16PF EPQ NEO-FFI Vergleich'),
]

# ---------------------------------------------------------------- Kapitel 3b
CARDS_K3B = [
    C('watson', BE, 'Wer begründete den <b>Behaviorismus</b>, und was untersucht er?',
      '<b>John B. Watson</b> (1878–1958). Gegenstand: <b>objektiv messbares Verhalten</b>, Psychologie als <b>Naturwissenschaft</b>. Methodik: direkte Beobachtung, Objektivität, präzise Definitionen, kontrollierte Experimente. <b>Radikaler Behaviorismus = Reiz-Reaktions-Psychologie.</b> Hauptstrom der amerikanischen Empirie von <b>1920–1979</b>.',
      'Watson Behaviorismus Verhalten Naturwissenschaft Reiz-Reaktion 1920'),
    C('blackbox', BE, 'Welches <b>Persönlichkeitskonzept</b> hat der Behaviorismus?',
      '<ul><li>Mensch als <b>„Black Box“</b>: Reiz → Black Box → Reaktion</li><li>Persönlichkeit entwickelt sich über <b>Lernprozesse</b> und ist Resultat der <b>individuellen Lerngeschichte</b></li><li>Der Mensch kommt als <b>„leere Hülle“</b> zur Welt und kann durch Lernen <b>beliebig geformt</b> werden (Watson)</li></ul>',
      'Black Box leere Hülle Lerngeschichte Watson'),
    C('lernmech', BE, 'Welche <b>drei zentralen Lernmechanismen</b> gibt es?',
      '<ul><li><b>Klassische Konditionierung:</b> Erwerb von <b>Reiz-Reaktions-Assoziationen</b></li><li><b>Operante Konditionierung:</b> Formung durch <b>Verhaltenskonsequenzen</b> (Belohnung, Bestrafung)</li><li><b>Beobachtungs-/Nachahmungslernen:</b> durch Beobachtung und Nachahmung anderer (<b>Modelle</b>)</li></ul>',
      'Lernmechanismen klassisch operant Beobachtungslernen Modelle'),
    C('pawlow', BE, 'Was ist das Besondere an <b>Iwan P. Pawlow</b> (1849–1936)?',
      'Erster bedeutender Ansatz zur Erklärung von Lernprozessen; <b>Grundlage des Lernens: angeborene Reflexe</b>. Beschrieb als Erster die <b>klassische Konditionierung</b> (Studien über den <b>Verdauungsapparat des Hundes</b>). Folie: <b>idiografische</b> Forschungsausrichtung.',
      'Pawlow klassische Konditionierung Reflexe Hund idiografisch'),
    C('pawlow-exp', BE, 'Wie läuft Pawlows <b>Experiment</b> ab (UCS, UCR, NS, CS, CR)?',
      '<table><tr><th>Phase</th><th>Reiz</th><th>Reaktion</th></tr><tr><td>vorher</td><td>Nahrung = <b>UCS</b></td><td>Speichelfluss = <b>UCR</b></td></tr><tr><td>vorher</td><td>Ton = <b>NS</b></td><td>kein Speichelfluss</td></tr><tr><td>Konditionierung</td><td>Nahrung + Ton</td><td>Speichelfluss (UCR)</td></tr><tr><td>nachher</td><td>Ton = <b>CS</b></td><td>Speichelfluss = <b>CR</b></td></tr></table>',
      'Pawlow UCS UCR NS CS CR Ton Nahrung Speichelfluss'),
    C('reizsub', BE, 'Was ist <b>Reizsubstitution</b>?',
      'Ein <b>neutraler Stimulus</b> (NS, löst keine spezifische Reaktion aus) wird <b>gemeinsam mit einem UCS</b> dargeboten. Danach löst der NS <b>allein</b> eine <b>konditionierte Reaktion (CR)</b> aus: Der <b>NS wird zum CS</b>.',
      'Reizsubstitution neutraler Stimulus konditioniert'),
    C('extinktion', BE, 'Was ist <b>Löschung (Extinktion)</b>?',
      'Der <b>CS</b> (Ton) wird <b>ohne den UCS</b> (Nahrung) dargeboten → die konditionierte Reaktion (Speichelfluss) wird <b>geschwächt oder ganz gelöscht</b>. Gegenstück: <b>Akquisition</b> (Aufbau).',
      'Löschung Extinktion CS ohne UCS Akquisition'),
    C('albert', BE, 'Was zeigt das Beispiel <b>„Der kleine Albert“</b>?',
      '<p>Dass sich <b>Furcht konditionieren</b> lässt:</p><ul><li>Vorher: lautes Geräusch (UCS) → Furcht (UCR); weiße Maus (NS) → keine Furcht</li><li>Konditionierung: Maus + Geräusch → Furcht</li><li>Danach: Maus (CS) → <b>Furcht (CR)</b></li></ul>' + H('Die Studie stammt von Watson.'),
      'kleiner Albert Furcht Maus Geräusch Konditionierung'),
    C('skinner', BE, 'Was vertrat <b>Burrhus F. Skinner</b> (1904–1990)?',
      '<b>Radikaler Behaviorismus</b>: Menschliches Verhalten wird <b>primär durch die Umwelt bzw. die Konsequenzen des Verhaltens</b> beeinflusst → <b>operante Konditionierung</b>. Folie: <b>idiografische</b> Forschungsausrichtung.',
      'Skinner operante Konditionierung Konsequenzen radikal idiografisch'),
    C('verstaerker', BE, 'Was sind <b>Verstärker</b>, was ist <b>Bestrafung</b>?',
      '<ul><li><b>Verstärker:</b> alle Konsequenzen, die die <b>Auftretenswahrscheinlichkeit</b> eines Verhaltens <b>erhöhen</b></li><li><b>Bestrafung:</b> alle Konsequenzen, die sie <b>reduzieren</b></li></ul>',
      'Verstärker Bestrafung Wahrscheinlichkeit'),
    C('vierfeld', BE, 'Positive/negative <b>Verstärkung</b> und <b>Bestrafung Typ 1/2</b>: Was ist was?',
      '<table><tr><th></th><th>positiver Reiz</th><th>negativer Reiz</th></tr><tr><td><b>hinzugefügt</b></td><td>positive Verstärkung</td><td>Bestrafung Typ 1</td></tr><tr><td><b>entfernt</b></td><td>Bestrafung Typ 2</td><td>negative Verstärkung</td></tr></table><p>Beide Verstärkungen <b>erhöhen</b>, beide Bestrafungen <b>senken</b> die Wahrscheinlichkeit.</p>',
      'positive negative Verstärkung Bestrafung Typ 1 Typ 2'),
    C('plaene', BE, 'Welche <b>Verstärkungspläne</b> gibt es, und wofür?',
      '<ul><li><b>Kontinuierliche</b> Verstärkung → <b>Etablierung</b> (Aufbau) erwünschten Verhaltens</li><li><b>Intermittierende</b> Verstärkung → <b>Intensivierung oder Aufrechterhaltung</b></li></ul><p>Grafik (Lewis &amp; Duncan, 1956): Je seltener verstärkt (25 % statt 100 %), desto mehr Hebelbetätigungen insgesamt.</p>',
      'Verstärkungspläne kontinuierlich intermittierend Lewis Duncan'),
    C('robbie', BE, 'Was zeigt das <b>Fallbeispiel Robbie</b> (Liebert &amp; Liebert, 1998)?',
      'Robbie verweigert die Mitarbeit im Unterricht. Phasen: <b>Basisrate → Konditionierung → Löschung → Rekonditionierung → Posttest</b>. Das Arbeitsverhalten steigt in der Konditionierung, sinkt in der Löschung und steigt in der Rekonditionierung wieder.',
      'Robbie Basisrate Konditionierung Löschung Rekonditionierung'),
    C('beh-probleme', BE, 'Welche <b>Probleme</b> hat das behavioristische Paradigma?',
      '<ol><li><b>Schon Neugeborene unterscheiden sich im Temperament</b> (Reizschwellen, Aufmerksamkeitsdauer, Ablenkbarkeit) – ohne Lerngelegenheit.</li><li>Viele Lerneffekte sind <b>wenig stabil</b> (Verhaltenstherapie bei Rauchern), andere entstehen in <b>einem einzigen Lerndurchgang</b> (Traumata).</li><li>Klassisch konditioniert werden kann nur <b>angeborenes Verhalten</b>; <b>neue Verhaltensweisen</b> lassen sich so nicht erlernen.</li></ol>',
      'Behaviorismus Probleme Neugeborene Temperament Traumata'),
    C('evo-konzept', EV, 'Welches <b>Persönlichkeitskonzept</b> hat das evolutionspsychologische Paradigma?',
      'Erleben und Verhalten sind das <b>Ergebnis der Evolution</b>: Über Millionen Jahre führt <b>genetische Anpassung</b> an die Umwelt zur <b>Selektion arttypischer körperlicher und Verhaltensmerkmale</b>. Der evolutionäre Prozess formt die <b>Variationsbreite</b> eines Verhaltens.',
      'Evolution Persönlichkeitskonzept Anpassung Selektion Variationsbreite'),
    C('fittest', EV, 'Was bedeutet <b>Fitness</b> bei „Survival of the fittest“?',
      'Fitness ist <b>kein Merkmal eines Menschen</b>, sondern eine <b>Funktion eines Allels und seiner Umwelt</b>.',
      'Survival of the fittest Fitness Allel Umwelt'),
    C('selektion', EV, 'Welche <b>Selektionsarten</b> gibt es?',
      '<ul><li><b>Natürliche Selektion:</b> Fortpflanzungserfolg mancher Individuen sinkt, „überlebenstüchtigere“ vermehren sich stärker; entscheidend sind <b>äußere Umweltfaktoren</b> (Selektionsfaktoren)</li><li><b>Intrasexuell:</b> Mitglieder <b>des gleichen Geschlechts konkurrieren</b> um das andere Geschlecht</li><li><b>Intersexuell:</b> Mitglieder eines Geschlechts <b>wählen</b> die des anderen nach Kriterien</li><li><b>Künstlich:</b> Zuchtwahl</li></ul>',
      'Selektion natürlich intrasexuell intersexuell künstlich Zuchtwahl'),
    C('ultimat', EV, '<b>Ultimate</b> vs. <b>proximate</b> Erklärungen?',
      '<ul><li><b>Ultimat:</b> <b>Anpassungswert</b> eines Verhaltens, Nutzen für das Individuum (<b>Wozu?</b>)</li><li><b>Proximat:</b> alle <b>inneren</b> Bedingungen (physiologisch, chemisch, psychisch) sowie <b>äußere Auslöser</b> (Schlüsselreize) und <b>soziale Bedingungen</b> (<b>Wie/Wodurch?</b>)</li></ul>',
      'ultimat proximat Anpassungswert Wozu Wie'),
    C('lausen', EV, 'Fellpflege („Lausen“) bei Primaten: <b>proximate</b> und <b>ultimate</b> Erklärung?',
      '<ul><li><b>Proximat:</b> <b>Endorphinspiegel</b> steigt bei beiden, <b>Aggressionsbereitschaft</b> wird gehemmt</li><li><b>Ultimat:</b> stiftet und erhält <b>Bindungen</b>; Vorteile bei Schutz vor Beutegreifern, gemeinsamer Jagd, Brutpflege, Konfliktschlichtung</li></ul>',
      'Lausen Fellpflege Primaten Endorphin Bindung'),
    C('frequenz', EV, 'Was ist <b>frequenzabhängige Selektion</b>?',
      'Antwort auf die Frage, warum es bei ähnlicher Umwelt unterschiedliches Verhalten gibt: Die <b>Fitness eines Gens hängt von seiner Häufigkeit in der Population ab</b>. Stabilisiert werden die Häufigkeitsverhältnisse mit dem <b>größten Fortpflanzungserfolg</b>. Beispiel: <b>Soziosexualität</b> (Tendenz zu Sex mit vielen Partnern).',
      'frequenzabhängige Selektion Häufigkeit Soziosexualität'),
    C('evo-probleme', EV, 'Welche <b>Probleme</b> hat der evolutionspsychologische Ansatz?',
      '<ul><li><b>Sehr junge Disziplin</b> (ca. 1990)</li><li>Gefahr von <b>Scheinerklärungen</b>; Annahmen über die Umwelt der Vorfahren <b>sehr spekulativ</b></li><li><b>Geringe empirische Testbarkeit</b></li><li>Fraglich, ob die <b>Stabilität von Umwelt und Genen</b> ausreicht</li></ul>',
      'Evolutionspsychologie Probleme jung 1990 spekulativ Testbarkeit'),
    C('iv-konzept', IV, 'Welches <b>Persönlichkeitskonzept</b> hat das Informationsverarbeitungsparadigma?',
      '<p>Menschen unterscheiden sich in der <b>Verarbeitung von Informationen</b>; Erleben und Verhalten beruhen auf der <b>Informationsübertragung im Nervensystem</b>. Eigenschaften beruhen auf:</p><ul><li><b>individualtypischen, zeitlich stabilen Parametern</b> der Informationsverarbeitung (z. B. <b>Reaktionsgeschwindigkeit</b>, <b>Kapazität des Arbeitsgedächtnisses</b>)</li><li><b>individualtypischen Inhalten im Langzeitgedächtnis</b></li></ul>',
      'Informationsverarbeitung Reaktionsgeschwindigkeit Arbeitsgedächtnis Langzeitgedächtnis'),
    C('iv-beispiele', IV, 'Welche <b>Beispiele</b> nennt das Informationsverarbeitungsparadigma?',
      '<ul><li><b>Geschwindigkeit</b> der Informationsverarbeitung → Zusammenhang <b>Intelligenz</b> mit <b>Reaktions- und Inspektionszeit</b></li><li><b>Kapazität des Arbeitsgedächtnisses</b> → Zusammenhang <b>Arbeitsgedächtnis und Intelligenz</b></li></ul>',
      'Inspektionszeit Reaktionszeit Intelligenz Arbeitsgedächtnis'),
    C('systeme', IV, '<b>Impulsives</b> vs. <b>reflexives System</b>?',
      '<p>Zwei mentale Systeme, die sich in <b>Repräsentation und Verarbeitung</b> unterscheiden und <b>koexistieren und interagieren</b> können.</p><ul><li><b>Impulsiv:</b> <b>automatisch, schnell, unbewusst</b>; basiert auf <b>gelernten Assoziationen</b> und <b>motivationaler Orientierung</b></li><li><b>Reflexiv:</b> erfordert <b>bewusstes Reflektieren</b>, auch über Konsequenzen; basiert auf gelernten <b>Werten und Fakten</b>; der <b>„rationale“ Generator</b> von Verhalten</li></ul>',
      'impulsives reflexives System automatisch bewusst rational'),
    C('einstellung', IV, 'Was sind <b>Einstellungen</b>, und was gilt für <b>implizite</b> Einstellungen?',
      '<b>Einstellung:</b> Bewertung von Objekten auf der Dimension <b>positiv–negativ</b> (z. B. Parteien, Automarke, Coronaimpfung). Zwischen <b>erfragten</b> Einstellungen und Verhalten besteht oft nur ein <b>geringer Zusammenhang</b>. <b>Implizite Einstellungen</b> sind dem Bewusstsein <b>nur schwer zugänglich</b>.',
      'Einstellung implizit positiv negativ Verhalten'),
    C('iv-probleme', IV, 'Welche <b>Probleme</b> hat das Informationsverarbeitungsparadigma?',
      '<ul><li><b>Zeitliche Stabilität</b> der Messungen oft <b>gering</b>, oft nicht geprüft</li><li><b>Transsituative Konsistenz</b> (über ähnliche Aufgaben hinweg) oft <b>gering</b></li></ul>',
      'Informationsverarbeitung Probleme zeitliche Stabilität transsituative Konsistenz'),
    C('nw-konzept', NW, 'Welches <b>Persönlichkeitskonzept</b> hat das neurowissenschaftliche Paradigma?',
      'Informationsverarbeitung beruht auf dem <b>Nervensystem</b>, das mit <b>Herz-Kreislauf-, Hormon- und Immunsystem</b> interagiert. Persönlichkeitsunterschiede können sich daher auch auf <b>biologische Systeme außerhalb des Nervensystems</b> beziehen, z. B. das <b>Mikrobiom im Darm</b>.',
      'Neurowissenschaft Nervensystem Hormonsystem Immunsystem Mikrobiom'),
    C('lappen', NW, 'Welche Funktionen haben die <b>Hirnlappen</b> laut Folie?',
      '<ul><li><b>Frontallappen:</b> Denken, Problemlösen, <b>Persönlichkeit</b>, exekutive Funktionen, Planung, Motorik, Emotionsregulation, Sprachproduktion, Arbeitsgedächtnis, Entscheidungen, Motivation</li><li><b>Parietallappen:</b> sensorische Informationen, räumliches Denken, Zahlenverständnis, Schmerz, binokulares Sehen</li><li><b>Okzipitallappen:</b> visuelle Wahrnehmung, Farbunterscheidung</li><li><b>Temporallappen:</b> Sprachverständnis, Hören, Verhalten, Emotionsregulation, Gleichgewicht, Gesichtererkennung</li><li><b>Kleinhirn:</b> Bewegungsabläufe, Koordination</li></ul>',
      'Hirnlappen Frontallappen Parietallappen Okzipitallappen Temporallappen Kleinhirn'),
    C('transmitter', NW, 'Welche Funktion haben die <b>Neurotransmitter und Hormone</b> laut Folie?',
      '<table><tr><th>Substanz</th><th>Funktion</th></tr><tr><td>Dopamin</td><td>Anreizmotivation</td></tr><tr><td>Serotonin</td><td>Stimmungsregulation</td></tr><tr><td>Noradrenalin</td><td>Aktivierung, Aufmerksamkeit</td></tr><tr><td>Kortisol (Hormon)</td><td>stressabhängige Aktivierung</td></tr><tr><td>Adrenalin</td><td>Angriff/Flucht</td></tr><tr><td>Testosteron</td><td>männliche Attribute</td></tr><tr><td>Oxytocin (Hormon)</td><td>Beruhigung, Bindung, Sexualität</td></tr></table>',
      'Dopamin Serotonin Noradrenalin Kortisol Adrenalin Testosteron Oxytocin'),
    C('korrelativ', NW, 'Was ist der <b>korrelative Ansatz</b> der Neurowissenschaft?',
      'Persönlichkeit wird in einer größeren Stichprobe per <b>Selbst- oder Fremdbeschreibung</b> gemessen und mit <b>neuroanatomischen oder physiologischen Merkmalen korreliert</b>. Wichtig: Parameter <b>zeitstabil</b> (mehrere Messungen an mehreren Tagen), Messung in <b>eigenschaftsrelevanten Situationen</b>, <b>nicht kausal</b> interpretierbar.',
      'korrelativer Ansatz Neurowissenschaft zeitstabil nicht kausal'),
    C('aktivierung', NW, 'Was besagt Eysencks (1967) Annahme zum <b>Aktivierungspotential</b> Intro- und Extravertierter?',
      '<b>Introvertierte</b> haben eine <b>niedrige physiologische Aktivierungsschwelle</b> → schon bei geringen Reizen starke Aktivierung. Bei hoher Erregung greift der Schutzmechanismus der <b>transmarginalen Hemmung</b> → niedrige Aktivierung. <b>Extravertierte</b> haben ihr Optimum bei <b>höherer</b> Aktivierung.',
      'Eysenck 1967 Aktivierung transmarginale Hemmung introvertiert'),
    C('multivariat', NW, 'Was ist <b>multivariate Psychophysiologie</b>?',
      '<b>Erweiterung des korrelativen Ansatzes</b>: <b>mehrere physiologische Reaktionen</b> in <b>mehreren eigenschaftsrelevanten Situationen</b> – so lässt sich die <b>transsituative Konsistenz</b> untersuchen. Beispiel: Stressparameter (Herzrate, Blutdruck, Schlagvolumen …) in unterschiedlich stressigen Situationen (<b>Stemmler, 1992</b>).',
      'multivariate Psychophysiologie Stemmler transsituative Konsistenz'),
    C('system', NW, 'Was ist der <b>systemorientierte Ansatz</b>?',
      '<b>Alternative zum multivariaten Ansatz</b>; es geht um die <b>Kohärenz von Reaktionen über Personen</b>. Ausgangspunkt ist ein <b>genau umschriebenes System</b> (Anatomie, Biochemie, Physiologie). <b>Unterschiede in der Reaktivität des Systems</b> werden auf Persönlichkeitsdispositionen bezogen. Überprüfung durch <b>Manipulation der Systemparameter</b>.',
      'systemorientierter Ansatz Kohärenz Manipulation'),
    C('oxytocin', NW, 'Was zeigte die Studie zu <b>Oxytocin als „Treuehormon“</b> (Scheele, 2012)?',
      'Oxytocin oder Placebo an <b>verheiratete</b> und <b>Single-Männer</b>: Verheiratete hielten unter Oxytocin <b>mehr Abstand zu einer attraktiven Frau</b> als unter Placebo und als die Singles. Beispiel für den <b>systemorientierten</b> Ansatz.',
      'Oxytocin Treuehormon Scheele verheiratet Abstand'),
    C('nw-probleme', NW, 'Welche <b>Probleme</b> hat das neurowissenschaftliche Paradigma?',
      '<p>Meist nur <b>niedrige Korrelationen</b> zwischen Eigenschaft und Messung, weil</p><ul><li>Selbstbeurteilungen <b>Verzerrungen</b> unterliegen (soziale Erwünschtheit),</li><li><b>individuelle Reaktionshierarchien</b> dämpfen (niedrige Herzrate bei Sportlern),</li><li>Messungen dem <b>technisch Machbaren</b> folgen statt systemspezifisch zu sein.</li></ul><p>Außerdem: <b>fehlendes Wissen</b> über physiologische Systeme und ihre Wechselwirkungen.</p>',
      'Neurowissenschaft Probleme niedrige Korrelationen Reaktionshierarchien'),
]

CARDS3 = {'k3a': CARDS_K3A, 'k3b': CARDS_K3B}

# ---------------------------------------------------------------- Tests
ITEMS3 = []
SA = 'Teil 3 · Kap. 3a'
SB = 'Teil 3 · Kap. 3b'
def mc(id, src, q, options, correct, expl, kw):
    ITEMS3.append(dict(id=id, type='mc', q=q, options=options, correct=correct, expl=expl, src=src, kw=kw))
def tf(id, src, statement, answer, expl, kw):
    ITEMS3.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=src, kw=kw))
def gap(id, src, text, expl, kw):
    ITEMS3.append(dict(id=id, type='gap', text=text, expl=expl, src=src, kw=kw))

# ---- 3a Multiple Choice
mc('p3a-mc-01', SA, 'Welche Bedeutung von „persona“ nennt Cicero <b>nicht</b>?',
   ['wie man anderen erscheint (aber nicht ist)', 'die Rolle, die jemand im Leben spielt', 'Besonderheit und Würde', 'die angeborene Körperbeschaffenheit'], 3,
   'Cicero: Erscheinung, Rolle, Häufung persönlicher Eigenschaften (befähigen zur Arbeit), Besonderheit und Würde.', 'persona Cicero')
mc('p3a-mc-02', SA, 'Viersäftelehre: Welcher Saft gehört zu „<b>wütend, jähzornig</b>“?',
   ['Blut', 'Schleim', 'gelbe Galle', 'schwarze Galle'], 2,
   'Gelbe Galle – Leber – wütend, jähzornig.', 'gelbe Galle Leber jähzornig')
mc('p3a-mc-03', SA, 'Viersäftelehre: Welches Organ gehört zur <b>schwarzen Galle</b>?',
   ['Herz', 'Gehirn', 'Leber', 'Milz'], 3,
   'Schwarze Galle – Milz – traurig, depressiv.', 'schwarze Galle Milz traurig')
mc('p3a-mc-04', SA, 'Viersäftelehre: Welche Beschreibung gehört zu <b>Schleim</b> (Gehirn)?',
   ['heiter, optimistisch', 'langsam, apathisch', 'wütend, jähzornig', 'traurig, depressiv'], 1,
   'Schleim – Gehirn – langsam, apathisch. Blut – Herz – heiter, optimistisch.', 'Schleim Gehirn apathisch')
mc('p3a-mc-05', SA, 'Welcher Kretschmer-Typ wird als „Kopfmensch“ beschrieben (abstraktes Denken, viel Nachdenken)?',
   ['pyknisch', 'athletisch', 'leptosom', 'zyklothym'], 2,
   'Leptosom (schmal, fein): schizothym, „Kopfmensch“. Zyklothym ist ein Temperament, kein Körperbautyp.', 'leptosom Kopfmensch Kretschmer')
mc('p3a-mc-06', SA, 'Welche Zuordnung nach Kretschmer stimmt?',
   ['pyknisch – Schizophrenie – schizothym', 'athletisch – Epilepsie – viskös', 'leptosom – Depression/Manie – zyklothym', 'athletisch – Depression/Manie – zyklothym'], 1,
   'Leptosom – Schizophrenie – schizothym; athletisch – Epilepsie – viskös; pyknisch – Depression/Manie – zyklothym.', 'Kretschmer athletisch Epilepsie viskös')
mc('p3a-mc-07', SA, 'Warum gelten Kretschmers Befunde als problematisch?',
   ['Er untersuchte nur Frauen', 'Körperbau und Temperament sind beide alterskorreliert (Scheinkorrelation)', 'Es gab überhaupt keinen Zusammenhang', 'Er nutzte keine Korrelationen'], 1,
   'Körperbau und Temperament sind <b>konfundiert</b> durch das Alter → altersbedingte Scheinkorrelationen. Ein schwacher Zusammenhang bleibt.', 'Kretschmer Scheinkorrelation Alter')
mc('p3a-mc-08', SA, '„Warum ist Lara so intelligent? – Weil ihr Arbeitsgedächtnis effizient arbeitet.“ Welches Paradigma antwortet so?',
   ['Eigenschaftsparadigma', 'Behavioristisches Paradigma', 'Informationsverarbeitungsparadigma', 'Neurowissenschaftliches Paradigma'], 2,
   'Arbeitsgedächtnis = Informationsverarbeitung. Neurowissenschaft: gut isolierte Nervenfasern.', 'Lara Paradigma Arbeitsgedächtnis')
mc('p3a-mc-09', SA, '„Weil sie oft für kognitive Leistungen belohnt wurde.“ Welches Paradigma?',
   ['Behavioristisches Paradigma', 'Evolutionspsychologisches Paradigma', 'Eigenschaftsparadigma', 'Informationsverarbeitungsparadigma'], 0,
   'Belohnung = Lernen durch Konsequenzen = Behaviorismus.', 'Lara Behaviorismus belohnt')
mc('p3a-mc-10', SA, 'Was besagt die <b>Sedimentationshypothese</b> (Klages, 1926)?',
   ['Wichtige Eigenschaften schlagen sich als einzelnes Wort in der Alltagssprache nieder', 'Eigenschaften lagern sich im Laufe des Lebens ab und werden stabiler', 'Persönlichkeit besteht aus Schichten von Gewohnheiten', 'Gene setzen sich über Generationen durch'], 0,
   'Je wichtiger eine Eigenschaft im Alltag, desto eher ein einzelnes Wort (Adjektiv oder Substantiv, seltener Verb).', 'Sedimentationshypothese Klages')
mc('p3a-mc-11', SA, 'Welche Wortart bildet laut Sedimentationshypothese wichtige Eigenschaften am <b>seltensten</b> ab?',
   ['Adjektiv', 'Substantiv', 'Verb', 'alle gleich häufig'], 2,
   'Adjektiv oder Substantiv, <b>seltener ein Verb</b>.', 'Sedimentationshypothese Verb')
mc('p3a-mc-12', SA, 'Was ist laut <b>differentiellem Ansatz</b> ein Merkmal der Person?',
   ['die Persönlichkeitseigenschaft selbst', 'die Ausprägung, die sie auf einer Eigenschaft zeigt', 'ihre Gene', 'ihre Lerngeschichte'], 1,
   'Eigenschaften charakterisieren die <b>Population</b>; Merkmal der Person ist ihre <b>Ausprägung</b>.', 'differentieller Ansatz Ausprägung Population')
mc('p3a-mc-13', SA, 'Wie viele Persönlichkeitsfaktoren fand <b>Cattell</b>?',
   ['3', '5', '16', '18.000'], 2,
   '16 Faktoren → 16PF. Eysenck: 3, Big Five: 5, über 18.000 Begriffe waren die Ausgangsliste der Big Five.', 'Cattell 16')
mc('p3a-mc-14', SA, 'Welcher Faktor gehört <b>nicht</b> zu Cattells 16 Faktoren?',
   ['Wachsamkeit', 'Perfektionismus', 'Abgehobenheit', 'Psychotizismus'], 3,
   'Psychotizismus ist ein Supertrait bei <b>Eysenck</b>.', 'Cattell Faktoren Psychotizismus')
mc('p3a-mc-15', SA, 'Was ist das Hauptproblem von Cattells 16 Faktoren?',
   ['Sie sind nicht normalverteilt', 'Einige korrelieren hoch miteinander', 'Sie wurden ohne Faktorenanalyse gewonnen', 'Sie gelten nur für Kinder'], 1,
   'Hohe Interkorrelationen → Hinweis auf Faktoren 2. Ordnung (Eysencks Kritik).', 'Cattell Problem korrelieren')
mc('p3a-mc-16', SA, 'Was sind Eysencks <b>Supertraits</b>?',
   ['16 Faktoren erster Ordnung', 'drei Faktoren zweiter Ordnung', 'fünf kulturstabile Faktoren', 'spezifische Verhaltensweisen'], 1,
   'Drei Faktoren zweiter Ordnung: P, E, N.', 'Eysenck Supertraits zweiter Ordnung')
mc('p3a-mc-17', SA, 'Welcher Gegenpol gehört zu <b>Psychotizismus</b>?',
   ['Introversion', 'Emotionale Stabilität', 'Über-Ich-Funktion', 'Verträglichkeit'], 2,
   'P: Psychotizismus vs. <b>Über-Ich-Funktion</b>; E: Extraversion vs. Introversion; N: Neurotizismus vs. Emotionale Stabilität.', 'Psychotizismus Über-Ich')
mc('p3a-mc-18', SA, 'Wie heißt Eysencks Fragebogen?',
   ['16PF', 'EPQ', 'NEO-FFI', 'MMPI'], 1,
   'EPQ = Eysenck Personality Questionnaire. 16PF: Cattell. NEO-FFI: McCrae &amp; Costa.', 'EPQ Eysenck')
mc('p3a-mc-19', SA, 'Wie viel der Bevölkerung liegt nach Eysenck im <b>mittleren Bereich</b> jeder Dimension?',
   ['etwa 1/3', 'etwa 1/2', 'etwa 2/3', 'fast alle'], 2,
   'Etwa <b>2/3</b>; die Dimensionen sind normalverteilt.', 'Eysenck zwei Drittel')
mc('p3a-mc-20', SA, 'In Eysencks Hierarchie: Auf welcher Ebene liegen <b>Soziabilität, Impulsivität, Aktivität, Lebendigkeit</b>?',
   ['Typ-Level', 'Trait-Level', 'Gewohnheiten', 'spezifisches Verhalten'], 1,
   'Typ: Extraversion → Traits: Soziabilität, Impulsivität, Aktivität, Lebendigkeit → Gewohnheiten (Vereine, Sport) → spezifisches Verhalten (Tennis, Reiten …).', 'Hierarchie Trait-Level')
mc('p3a-mc-21', SA, 'Welche Eigenschaft wird auf der Folie (überraschend) dem <b>Psychotizismus</b> zugeordnet?',
   ['Kreativität', 'Geselligkeit', 'Ordentlichkeit', 'Schüchternheit'], 0,
   'Trait-Level Psychotizismus enthält auch <b>Kreativität</b>.', 'Psychotizismus Kreativität')
mc('p3a-mc-22', SA, 'Fernbedienungs-Studie (Weaver et al., 1996): Wer nutzt die Fernbedienung <b>defensiv</b> (unerwünschte Inhalte vermeiden)?',
   ['hoch Extravertierte', 'hoch Neurotische', 'hoch Psychotische', 'hoch Gewissenhafte'], 1,
   'Neurotizismus → defensiv; Psychotizismus → offensiv (andere dominieren).', 'Fernbedienung defensiv Neurotizismus')
mc('p3a-mc-23', SA, 'Womit korreliert Psychotizismus <b>negativ</b> (Furnham &amp; Medhurst, 1995)?',
   ['ablehnender Haltung gegenüber Autoritäten', 'akademischer Leistung', 'Geschlecht männlich', 'Haft'], 1,
   'Negativ mit <b>akademischer Leistung</b>. Mit ablehnender Haltung gegenüber Autoritäten positiv (Rigby &amp; Slee, 1987).', 'Psychotizismus akademische Leistung')
mc('p3a-mc-24', SA, 'Welcher Befund gehört zu <b>Extraversion</b>?',
   ['schneller bei Multi-Tasking als Introvertierte', 'mehr negative Erinnerungen', 'geringeres Selbstvertrauen', 'leichter hypnotisierbar'], 0,
   'Lieberman &amp; Rosenthal (2001). Negative Erinnerungen und geringes Selbstvertrauen: Neurotizismus; hypnotisierbar: Offenheit.', 'Extraversion Multitasking')
mc('p3a-mc-25', SA, 'Aus wie vielen Begriffen wurden die Big Five gewonnen?',
   ['rund 160', 'rund 1.600', 'über 18.000', 'über 180.000'], 2,
   'Listen mit <b>über 18.000 Begriffen</b>, reduziert per Faktorenanalyse.', 'Big Five 18000')
mc('p3a-mc-26', SA, 'Welcher Big-Five-Faktor korreliert positiv mit <b>akademischem und beruflichem Erfolg</b>?',
   ['Offenheit', 'Verträglichkeit', 'Gewissenhaftigkeit', 'Neurotizismus'], 2,
   'Gewissenhaftigkeit. Offenheit: Bildungsmöglichkeiten, Hypnotisierbarkeit, Intelligenz. Verträglichkeit: politische Gesinnung.', 'Gewissenhaftigkeit Erfolg')
mc('p3a-mc-27', SA, 'Welcher Big-Five-Faktor wurde mit <b>politischer Gesinnung</b> in Verbindung gebracht?',
   ['Verträglichkeit', 'Extraversion', 'Gewissenhaftigkeit', 'Neurotizismus'], 0,
   'Verträglichkeit.', 'Verträglichkeit politisch')
mc('p3a-mc-28', SA, '„Ordentlichkeit, Beharrlichkeit, Zuverlässigkeit“ – welcher Big-Five-Faktor?',
   ['Offenheit', 'Gewissenhaftigkeit', 'Verträglichkeit', 'Extraversion'], 1,
   'Gewissenhaftigkeit. Verträglichkeit: Wärme, Toleranz, Hilfsbereitschaft.', 'Gewissenhaftigkeit Ordentlichkeit')
mc('p3a-mc-29', SA, 'Was ist <b>kein</b> Kritikpunkt am dispositionalen Ansatz?',
   ['situative Faktoren werden unterschätzt', 'Faktorenanalysen enthalten viele subjektive Entscheidungen', 'individuelles Verhalten kann nicht vorhergesagt werden', 'der Mensch wird als Black Box gesehen'], 3,
   'Black Box ist das Menschenbild des <b>Behaviorismus</b>, kein Kritikpunkt am Eigenschaftsansatz.', 'Kritik dispositional Black Box')

# ---- 3a Richtig/Falsch
tf('p3a-tf-01', SA, 'Galenus von Pergamon verknüpfte die Viersäftelehre mit der Lehre von den vier Temperamenten.', True,
   'Richtig, 1. Jh. n. Chr.', 'Galenus Viersäftelehre')
tf('p3a-tf-02', SA, 'In der Viersäftelehre gehört das Blut zum Herzen und zu „heiter, optimistisch“.', True,
   'Blut – Herz – heiter, optimistisch.', 'Blut Herz heiter')
tf('p3a-tf-03', SA, 'In der Viersäftelehre gehört die gelbe Galle zur Milz.', False,
   'Gelbe Galle – <b>Leber</b>. Die Milz gehört zur schwarzen Galle.', 'gelbe Galle Leber Milz')
tf('p3a-tf-04', SA, 'Laut Bewertung gibt es zwischen Körperbau und Persönlichkeit überhaupt keinen Zusammenhang.', False,
   'Ein <b>schwacher</b> Zusammenhang bleibt, aber die starken Befunde Kretschmers waren altersbedingte Scheinkorrelationen.', 'Kretschmer schwacher Zusammenhang')
tf('p3a-tf-05', SA, 'Die wissenschaftliche Persönlichkeitspsychologie entstand in der ersten Hälfte des 20. Jahrhunderts neben Behaviorismus und Psychoanalyse.', True,
   'Mit Fokus auf den Eigenschaftsbegriff.', 'Beginn Persönlichkeitspsychologie')
tf('p3a-tf-06', SA, 'Laut differentiellem Ansatz sind Persönlichkeitseigenschaften Merkmale, die eine Population charakterisieren.', True,
   'Merkmal der Person ist ihre Ausprägung.', 'differentieller Ansatz Population')
tf('p3a-tf-07', SA, 'Cattell reduzierte Alltagsbegriffe schließlich mithilfe der Faktorenanalyse.', True,
   'Alltagsbegriffe sammeln, ähnliche Wörter streichen, reduzieren, Personen beschreiben, Faktorenanalyse.', 'Cattell Faktorenanalyse')
tf('p3a-tf-08', SA, 'Die deutsche Version des 16PF heißt NEO-FFI.', False,
   'Deutsche Version: <b>16PF-R</b> (Schneewind &amp; Graf, 1998). NEO-FFI gehört zu den Big Five.', '16PF-R NEO-FFI')
tf('p3a-tf-09', SA, 'Eysenck kritisierte, dass Cattells Faktoren auf Faktoren 2. Ordnung hinweisen.', True,
   'Wegen der Interkorrelationen → drei Supertraits.', 'Eysenck Kritik Cattell')
tf('p3a-tf-10', SA, 'Bei Eysenck ist der Gegenpol zu Neurotizismus die Introversion.', False,
   'Gegenpol zu Neurotizismus: <b>Emotionale Stabilität</b>. Introversion ist der Gegenpol zu Extraversion.', 'Neurotizismus Gegenpol')
tf('p3a-tf-11', SA, 'Extravertierte reagieren stärker auf negative als auf positive Stimuli.', False,
   'Umgekehrt: stärker auf <b>positive</b> Stimuli (Carpenter, 2001).', 'Extraversion positive Stimuli')
tf('p3a-tf-12', SA, 'Emotionale Stabilität hängt positiv mit Zufriedenheit in Schule und Studium zusammen.', True,
   'Giesen et al. (1986).', 'emotionale Stabilität Zufriedenheit')
tf('p3a-tf-13', SA, 'Psychotizismus ist bei Frauen höher ausgeprägt als bei Männern.', False,
   '<b>Männer &gt; Frauen</b>, Häftlinge &gt; Nicht-Häftlinge (Liebert &amp; Liebert, 1998).', 'Psychotizismus Männer')
tf('p3a-tf-14', SA, 'Die Big Five sind nur mit Fragebögen nachweisbar.', False,
   'Mit <b>verschiedenen Datenquellen</b> (Fragebogen, Q-, L-, T-Daten).', 'Big Five Datenquellen')
tf('p3a-tf-15', SA, 'Die Big Five eignen sich auch zur Beschreibung von Kindern und Jugendlichen.', True,
   'Digman (1989); Asendorpf &amp; van Aken (2003); Kohnstamm et al. (1995).', 'Big Five Kinder')
tf('p3a-tf-16', SA, 'Offenheit für Erfahrungen korreliert positiv mit Intelligenz.', True,
   'Außerdem: mehr Bildungssuche, leichter hypnotisierbar.', 'Offenheit Intelligenz')
tf('p3a-tf-17', SA, 'Soziale Erwünschtheit in Selbstberichten ist ein Kritikpunkt am dispositionalen Ansatz.', True,
   'Punkt 8 der Kritik.', 'Kritik soziale Erwünschtheit')
tf('p3a-tf-18', SA, 'Das Fünf-Faktoren-Modell ist vor allem im asiatischen Raum gut bestätigt.', False,
   'Gut bestätigt im <b>angloamerikanischen und nordeuropäischen</b> Raum.', 'Big Five Kultur')

# ---- 3a Lücken
gap('p3a-gap-01', SA, 'Blut gehört zum {{Herz|Herzen}}, Schleim zum {{Gehirn}}, gelbe Galle zur {{Leber}}, schwarze Galle zur {{Milz}}.',
    'Viersäftelehre (Galenus).', 'Viersäftelehre Organe')
gap('p3a-gap-02', SA, 'Kretschmers drei Körperbautypen heißen leptosom, athletisch und {{pyknisch}}.',
    'Pyknisch = rundlich, zyklothym.', 'Kretschmer pyknisch')
gap('p3a-gap-03', SA, 'Nach der {{Sedimentationshypothese}} (Klages, 1926) werden wichtige Eigenschaften in einem einzigen Wort der Alltagssprache abgebildet.',
    'Adjektiv oder Substantiv, seltener Verb.', 'Sedimentationshypothese')
gap('p3a-gap-04', SA, 'Cattells Fragebogen heißt {{16PF}}, die deutsche Version 16PF-R.',
    '16 Personality Factors.', '16PF')
gap('p3a-gap-05', SA, 'Eysenck beschrieb Persönlichkeit durch drei Faktoren zweiter Ordnung, sogenannte {{Supertraits|Supertrait}}.',
    'P, E, N.', 'Supertraits')
gap('p3a-gap-06', SA, 'PEN steht für Psychotizismus, {{Extraversion}} und {{Neurotizismus}}.',
    'Fragebogen: EPQ.', 'PEN')
gap('p3a-gap-07', SA, 'Der Gegenpol zu Psychotizismus heißt {{Über-Ich-Funktion|Über-Ich}}.',
    'Extreme Angepasstheit, „Kadavergehorsam“.', 'Über-Ich-Funktion')
gap('p3a-gap-08', SA, 'Hoher Psychotizismus führt zu {{offensiver|offensive}} Fernbedienungsnutzung, hoher Neurotizismus zu {{defensiver|defensive}}.',
    'Weaver et al. (1996).', 'Fernbedienung offensiv defensiv')
gap('p3a-gap-09', SA, 'Der Fragebogen zu den Big Five heißt {{NEO-FFI}}.',
    'NEO-Fünf-Faktoren-Inventar (McCrae &amp; Costa).', 'NEO-FFI')
gap('p3a-gap-10', SA, 'Die Big Five sind Offenheit, Gewissenhaftigkeit, Extraversion, {{Verträglichkeit}} und Neurotizismus.',
    'Verträglichkeit = Agreeableness.', 'Big Five Verträglichkeit')
gap('p3a-gap-11', SA, 'Offenheit für Erfahrungen geht mit leichterer {{Hypnotisierbarkeit}} einher (Roche &amp; McConkey, 1990).',
    'Außerdem: positiv mit Intelligenz korreliert.', 'Offenheit Hypnotisierbarkeit')

# ---- 3b Multiple Choice
mc('p3b-mc-01', SB, 'Wer gilt als <b>Begründer des Behaviorismus</b>?',
   ['Iwan P. Pawlow', 'John B. Watson', 'Burrhus F. Skinner', 'Hans J. Eysenck'], 1,
   'John B. Watson (1878–1958).', 'Watson Behaviorismus')
mc('p3b-mc-02', SB, 'Von wann bis wann war der Behaviorismus Hauptstrom der amerikanischen Empirie?',
   ['1880–1920', '1920–1979', '1950–1990', '1990 bis heute'], 1,
   'Laut Folie <b>1920–1979</b>.', 'Behaviorismus 1920 1979')
mc('p3b-mc-03', SB, 'Wie sieht der Behaviorismus den Menschen?',
   ['als Ergebnis genetischer Anpassung', 'als „Black Box“ und „leere Hülle“, die durch Lernen geformt wird', 'als System von Arbeitsgedächtnis und Langzeitgedächtnis', 'als Bündel normalverteilter Eigenschaften'], 1,
   'Reiz → Black Box → Reaktion; Persönlichkeit = Resultat der Lerngeschichte.', 'Black Box leere Hülle')
mc('p3b-mc-04', SB, 'Welcher Lernmechanismus formt Verhalten durch <b>Konsequenzen</b> (Belohnung, Bestrafung)?',
   ['klassische Konditionierung', 'operante Konditionierung', 'Beobachtungslernen', 'Reizsubstitution'], 1,
   'Operant = Konsequenzen (Skinner). Klassisch = Reiz-Reaktions-Assoziationen (Pawlow).', 'operante Konditionierung Konsequenzen')
mc('p3b-mc-05', SB, 'Was ist laut Pawlow die <b>Grundlage des Lernens</b>?',
   ['angeborene Reflexe', 'Belohnungen', 'Modelle', 'Gedächtniskapazität'], 0,
   'Angeborene Reflexe (Verdauungsapparat des Hundes).', 'Pawlow Reflexe')
mc('p3b-mc-06', SB, 'Im Pawlow-Experiment ist der Ton <b>nach</b> der Konditionierung …',
   ['ein unkonditionierter Stimulus (UCS)', 'ein neutraler Stimulus (NS)', 'ein konditionierter Stimulus (CS)', 'eine konditionierte Reaktion (CR)'], 2,
   'Vorher NS, nachher <b>CS</b>. Der Speichelfluss auf den Ton ist dann die CR.', 'Pawlow Ton CS')
mc('p3b-mc-07', SB, 'Was ist im Pawlow-Experiment die <b>unkonditionierte Reaktion (UCR)</b>?',
   ['Ton', 'Nahrung', 'Speichelfluss auf Nahrung', 'Speichelfluss auf den Ton allein'], 2,
   'Nahrung = UCS → Speichelfluss = UCR. Speichelfluss auf den Ton allein = CR.', 'UCR Speichelfluss')
mc('p3b-mc-08', SB, 'Wie kommt es zur <b>Löschung (Extinktion)</b>?',
   ['UCS wird ohne CS dargeboten', 'CS wird ohne UCS dargeboten', 'CS und UCS werden häufiger gekoppelt', 'Verhalten wird bestraft'], 1,
   'CS (Ton) ohne UCS (Nahrung) → CR wird geschwächt oder gelöscht.', 'Extinktion CS ohne UCS')
mc('p3b-mc-09', SB, '„Der kleine Albert“: Was war die <b>weiße Maus</b> nach der Konditionierung?',
   ['UCS', 'UCR', 'CS', 'NS'], 2,
   'Vorher NS, danach CS, der Furcht (CR) auslöst. Das laute Geräusch war der UCS.', 'kleiner Albert Maus CS')
mc('p3b-mc-10', SB, 'Ein lästiger Reiz wird <b>entfernt</b>, und das Verhalten tritt danach häufiger auf. Das ist …',
   ['positive Verstärkung', 'negative Verstärkung', 'Bestrafung Typ 1', 'Bestrafung Typ 2'], 1,
   'Negativer Reiz entfernt = <b>negative Verstärkung</b> (erhöht die Wahrscheinlichkeit).', 'negative Verstärkung')
mc('p3b-mc-11', SB, 'Ein <b>positiver</b> Reiz wird <b>entfernt</b> (z. B. Handyverbot). Das ist …',
   ['positive Verstärkung', 'negative Verstärkung', 'Bestrafung Typ 1', 'Bestrafung Typ 2'], 3,
   'Positiver Reiz entfernt = <b>Bestrafung Typ 2</b>. Negativer Reiz hinzugefügt = Typ 1.', 'Bestrafung Typ 2')
mc('p3b-mc-12', SB, 'Wozu dient <b>intermittierende</b> Verstärkung?',
   ['Etablierung neuen Verhaltens', 'Intensivierung oder Aufrechterhaltung von Verhalten', 'Löschung von Verhalten', 'Bestrafung'], 1,
   'Kontinuierlich → Etablierung; intermittierend → Intensivierung/Aufrechterhaltung.', 'intermittierende Verstärkung')
mc('p3b-mc-13', SB, 'Welche Phasen hat das <b>Fallbeispiel Robbie</b>?',
   ['Basisrate – Konditionierung – Löschung – Rekonditionierung – Posttest', 'Akquisition – Extinktion – Spontanerholung', 'Pretest – Training – Follow-up', 'Beobachtung – Nachahmung – Verstärkung'], 0,
   'Arbeitsverhalten steigt bei Konditionierung, sinkt bei Löschung, steigt bei Rekonditionierung.', 'Robbie Phasen')
mc('p3b-mc-14', SB, 'Welches ist <b>kein</b> Problem des behavioristischen Paradigmas?',
   ['Neugeborene unterscheiden sich schon im Temperament', 'manche Lerneffekte entstehen in einem einzigen Durchgang (Traumata)', 'klassisch können keine neuen Verhaltensweisen erlernt werden', 'Annahmen über die Umwelt der Vorfahren sind spekulativ'], 3,
   'Spekulative Annahmen über die Vorfahren sind ein Problem der <b>Evolutionspsychologie</b>.', 'Behaviorismus Probleme')
mc('p3b-mc-15', SB, 'Was ist <b>Fitness</b> im evolutionspsychologischen Sinn?',
   ['körperliche Leistungsfähigkeit eines Menschen', 'eine Funktion eines Allels und seiner Umwelt', 'Intelligenz', 'Zahl der Nachkommen eines Individuums'], 1,
   'Fitness ist <b>kein Merkmal eines Menschen</b>, sondern Funktion eines Allels und seiner Umwelt.', 'Fitness Allel')
mc('p3b-mc-16', SB, 'Männchen kämpfen untereinander um Weibchen. Welche Selektionsart?',
   ['natürliche Selektion', 'intrasexuelle Selektion', 'intersexuelle Selektion', 'künstliche Selektion'], 1,
   'Gleiches Geschlecht konkurriert = <b>intrasexuell</b>. Wählt ein Geschlecht das andere = intersexuell.', 'intrasexuelle Selektion')
mc('p3b-mc-17', SB, 'Was ist <b>künstliche Selektion</b>?',
   ['Partnerwahl nach Kriterien', 'Zuchtwahl', 'Selektion durch Umweltfaktoren', 'Selektion nach Häufigkeit'], 1,
   'Künstliche Selektion = Zuchtwahl.', 'künstliche Selektion Zuchtwahl')
mc('p3b-mc-18', SB, 'Fellpflege: „Der Endorphinspiegel steigt, die Aggressionsbereitschaft sinkt.“ Welche Erklärung ist das?',
   ['ultimat', 'proximat', 'frequenzabhängig', 'intersexuell'], 1,
   'Innere physiologische Bedingungen = <b>proximat</b> (Wie?). Bindung und Schutz = ultimat (Wozu?).', 'proximat Endorphin Lausen')
mc('p3b-mc-19', SB, 'Warum gibt es bei ähnlicher Umwelt unterschiedliches Verhalten? Die Evolutionspsychologie antwortet mit …',
   ['intrasexueller Selektion', 'frequenzabhängiger Selektion', 'künstlicher Selektion', 'Reizsubstitution'], 1,
   'Fitness eines Gens hängt von seiner Häufigkeit ab (Beispiel Soziosexualität).', 'frequenzabhängige Selektion')
mc('p3b-mc-20', SB, 'Seit wann etwa gibt es die Evolutionspsychologie als Disziplin?',
   ['ca. 1890', 'ca. 1920', 'ca. 1960', 'ca. 1990'], 3,
   'Sehr junge Disziplin, ca. <b>1990</b>.', 'Evolutionspsychologie 1990')
mc('p3b-mc-21', SB, 'Welches System ist <b>automatisch, schnell, unbewusst</b>?',
   ['reflexives System', 'impulsives System', 'Langzeitgedächtnis', 'Über-Ich'], 1,
   'Impulsiv: gelernte Assoziationen, motivationale Orientierung. Reflexiv: bewusst, „rationaler Generator“.', 'impulsives System')
mc('p3b-mc-22', SB, 'Welches Problem hat das <b>Informationsverarbeitungsparadigma</b>?',
   ['geringe zeitliche Stabilität und geringe transsituative Konsistenz', 'es ignoriert Gene völlig', 'es ist nicht empirisch', 'es gibt nur eine Dimension'], 0,
   'Zeitliche Stabilität oft gering/ungeprüft, transsituative Konsistenz oft gering.', 'Informationsverarbeitung Probleme')
mc('p3b-mc-23', SB, 'Welche Funktion hat <b>Dopamin</b> laut Folie?',
   ['Stimmungsregulation', 'Anreizmotivation', 'Angriff/Flucht', 'stressabhängige Aktivierung'], 1,
   'Dopamin: Anreizmotivation. Serotonin: Stimmung. Adrenalin: Angriff/Flucht. Kortisol: Stress.', 'Dopamin Anreizmotivation')
mc('p3b-mc-24', SB, 'Welche Substanz steht für <b>Beruhigung, Bindung, Sexualität</b>?',
   ['Testosteron', 'Noradrenalin', 'Oxytocin', 'Serotonin'], 2,
   'Oxytocin (Hormon).', 'Oxytocin Bindung')
mc('p3b-mc-25', SB, 'In welchem Hirnlappen wird laut Folie u. a. die <b>Persönlichkeit</b> verortet?',
   ['Frontallappen', 'Parietallappen', 'Okzipitallappen', 'Temporallappen'], 0,
   'Frontallappen: Denken, Problemlösen, Persönlichkeit, exekutive Funktionen …', 'Frontallappen Persönlichkeit')
mc('p3b-mc-26', SB, 'Introvertierte haben laut Eysenck (1967) …',
   ['eine hohe Aktivierungsschwelle', 'eine niedrige Aktivierungsschwelle und bei hoher Erregung transmarginale Hemmung', 'keine physiologischen Unterschiede zu Extravertierten', 'ihr Optimum bei sehr hoher Aktivierung'], 1,
   'Niedrige Schwelle → starke Aktivierung schon bei geringen Reizen; Schutz durch transmarginale Hemmung.', 'Eysenck Aktivierung Introvertierte')
mc('p3b-mc-27', SB, 'Mehrere physiologische Reaktionen in mehreren eigenschaftsrelevanten Situationen messen: Welcher Ansatz?',
   ['korrelativer Ansatz', 'multivariate Psychophysiologie', 'systemorientierter Ansatz', 'Faktorenanalyse'], 1,
   'Multivariat = Erweiterung des korrelativen Ansatzes (Stemmler, 1992).', 'multivariate Psychophysiologie')
mc('p3b-mc-28', SB, 'Die Oxytocin-Studie (Scheele, 2012) ist ein Beispiel für welchen Ansatz?',
   ['korrelativ', 'multivariat', 'systemorientiert', 'behavioristisch'], 2,
   'Systemorientiert: ein System gezielt <b>manipulieren</b> (Oxytocin vs. Placebo).', 'Oxytocin systemorientiert')
mc('p3b-mc-29', SB, 'Warum sind Korrelationen zwischen Eigenschaften und neurophysiologischen Messungen meist <b>niedrig</b>?',
   ['wegen Verzerrungen in Selbstberichten, individueller Reaktionshierarchien und unspezifischer Messungen', 'weil das Nervensystem keine Rolle spielt', 'weil nur Kinder untersucht werden', 'weil die Messungen zu genau sind'], 0,
   'Z. B. soziale Erwünschtheit, niedrige Herzrate bei Sportlern, Messung nach technisch Machbarem.', 'Neurowissenschaft niedrige Korrelationen')

# ---- 3b Richtig/Falsch
tf('p3b-tf-01', SB, 'Der Behaviorismus untersucht objektiv messbares Verhalten und versteht Psychologie als Naturwissenschaft.', True,
   'Direkte Beobachtung, präzise Definitionen, kontrollierte Experimente.', 'Behaviorismus Naturwissenschaft')
tf('p3b-tf-02', SB, 'Pawlow und Skinner werden auf der Folie einer nomothetischen Forschungsausrichtung zugeordnet.', False,
   'Laut Folie: <b>idiografische</b> Forschungsausrichtung.', 'Pawlow Skinner idiografisch')
tf('p3b-tf-03', SB, 'Bei der Reizsubstitution wird ein neutraler Stimulus zum konditionierten Stimulus.', True,
   'NS + UCS gekoppelt → NS löst allein CR aus → CS.', 'Reizsubstitution')
tf('p3b-tf-04', SB, 'Das Beispiel „Der kleine Albert“ zeigt, dass sich Furcht konditionieren lässt.', True,
   'Maus (CS) löst nach Kopplung mit lautem Geräusch Furcht (CR) aus.', 'kleiner Albert Furcht')
tf('p3b-tf-05', SB, 'Negative Verstärkung senkt die Wahrscheinlichkeit eines Verhaltens.', False,
   'Jede Verstärkung <b>erhöht</b> die Wahrscheinlichkeit. Negativ heißt: ein negativer Reiz wird entfernt.', 'negative Verstärkung erhöht')
tf('p3b-tf-06', SB, 'Bestrafung Typ 1 bedeutet: Ein negativer Reiz wird hinzugefügt.', True,
   'Typ 2: positiver Reiz wird entfernt.', 'Bestrafung Typ 1')
tf('p3b-tf-07', SB, 'Kontinuierliche Verstärkung dient vor allem dem Aufbau (Etablierung) von Verhalten.', True,
   'Intermittierend: Intensivierung/Aufrechterhaltung.', 'kontinuierliche Verstärkung')
tf('p3b-tf-08', SB, 'Mit klassischer Konditionierung lassen sich völlig neue Verhaltensweisen erlernen.', False,
   'Nur <b>angeborenes</b> Verhalten kann klassisch konditioniert werden – ein Problem des Paradigmas.', 'klassische Konditionierung neue Verhaltensweisen')
tf('p3b-tf-09', SB, 'Ultimate Erklärungen fragen nach dem Anpassungswert (Wozu?) eines Verhaltens.', True,
   'Proximat: Wie/Wodurch (innere und äußere Bedingungen).', 'ultimat Wozu')
tf('p3b-tf-10', SB, 'Bei intersexueller Selektion konkurrieren Mitglieder desselben Geschlechts miteinander.', False,
   'Das ist <b>intrasexuell</b>. Intersexuell: ein Geschlecht wählt das andere.', 'intersexuell intrasexuell')
tf('p3b-tf-11', SB, 'Eine geringe empirische Testbarkeit ist ein Problem der Evolutionspsychologie.', True,
   'Dazu: Scheinerklärungen, spekulative Annahmen, junge Disziplin.', 'Evolutionspsychologie Testbarkeit')
tf('p3b-tf-12', SB, 'Das reflexive System gilt als „rationaler“ Generator von Verhalten.', True,
   'Bewusstes Reflektieren, Werte und Fakten.', 'reflexives System rational')
tf('p3b-tf-13', SB, 'Erfragte Einstellungen sagen Verhalten meist sehr gut vorher.', False,
   'Oft nur <b>geringer</b> Zusammenhang; implizite Einstellungen sind schwer zugänglich.', 'Einstellungen Verhalten')
tf('p3b-tf-14', SB, 'Laut neurowissenschaftlichem Paradigma können auch Systeme außerhalb des Nervensystems, etwa das Darm-Mikrobiom, Persönlichkeit betreffen.', True,
   'Nervensystem interagiert mit Herz-Kreislauf-, Hormon- und Immunsystem.', 'Mikrobiom')
tf('p3b-tf-15', SB, 'Serotonin steht laut Folie für Angriff/Flucht.', False,
   'Serotonin: <b>Stimmungsregulation</b>. Angriff/Flucht: Adrenalin.', 'Serotonin Adrenalin')
tf('p3b-tf-16', SB, 'Ergebnisse des korrelativen Ansatzes dürfen kausal interpretiert werden.', False,
   '<b>Nicht kausal</b> interpretierbar.', 'korrelativ nicht kausal')
tf('p3b-tf-17', SB, 'In der Oxytocin-Studie hielten verheiratete Männer unter Oxytocin mehr Abstand zu einer attraktiven Frau.', True,
   'Mehr als unter Placebo und als Singles (Scheele, 2012).', 'Oxytocin Abstand')
tf('p3b-tf-18', SB, 'Der systemorientierte Ansatz überprüft seine Annahmen durch Manipulation der Systemparameter.', True,
   'Ausgangspunkt: genau umschriebenes System.', 'systemorientiert Manipulation')

# ---- 3b Lücken
gap('p3b-gap-01', SB, 'Die drei zentralen Lernmechanismen sind klassische Konditionierung, {{operante}} Konditionierung und {{Beobachtungslernen|Nachahmungslernen|Modelllernen}}.',
    'Operant: Konsequenzen; Beobachtung: Modelle.', 'Lernmechanismen')
gap('p3b-gap-02', SB, 'Nahrung ist der {{UCS}}, der Speichelfluss darauf die {{UCR}}.',
    'Unkonditionierter Stimulus und unkonditionierte Reaktion.', 'UCS UCR')
gap('p3b-gap-03', SB, 'Wird der CS ohne den UCS dargeboten, kommt es zur {{Löschung|Extinktion}}.',
    'Die CR wird geschwächt oder gelöscht.', 'Löschung Extinktion')
gap('p3b-gap-04', SB, 'Ein negativer Reiz wird entfernt: Das ist {{negative}} Verstärkung.',
    'Erhöht die Wahrscheinlichkeit.', 'negative Verstärkung')
gap('p3b-gap-05', SB, '{{Intermittierende}} Verstärkung dient der Intensivierung oder Aufrechterhaltung von Verhalten.',
    'Kontinuierliche: Etablierung.', 'intermittierend')
gap('p3b-gap-06', SB, 'Fitness ist eine Funktion eines {{Allels}} und seiner {{Umwelt}}.',
    'Kein Merkmal eines Menschen.', 'Fitness Allel Umwelt')
gap('p3b-gap-07', SB, '{{Proximate}} Erklärungen fragen nach inneren Bedingungen und äußeren Auslösern, {{ultimate}} nach dem Anpassungswert.',
    'Wie? vs. Wozu?', 'proximat ultimat')
gap('p3b-gap-08', SB, 'Bei der {{frequenzabhängigen}} Selektion hängt die Fitness eines Gens von seiner Häufigkeit in der Population ab.',
    'Beispiel: Soziosexualität.', 'frequenzabhängige Selektion')
gap('p3b-gap-09', SB, 'Das {{impulsive}} System arbeitet automatisch, schnell und unbewusst.',
    'Gegenstück: reflexives System.', 'impulsives System')
gap('p3b-gap-10', SB, 'Kortisol steht für {{stressabhängige}} Aktivierung, Dopamin für {{Anreizmotivation}}.',
    'Neurotransmitter/Hormone laut Folie.', 'Kortisol Dopamin')
gap('p3b-gap-11', SB, 'Bei hoher Erregung schützt bei Introvertierten die {{transmarginale}} Hemmung.',
    'Eysenck (1967).', 'transmarginale Hemmung')
gap('p3b-gap-12', SB, 'Die multivariate Psychophysiologie erlaubt es, die {{transsituative}} Konsistenz zu untersuchen.',
    'Mehrere Reaktionen in mehreren Situationen.', 'transsituative Konsistenz')
