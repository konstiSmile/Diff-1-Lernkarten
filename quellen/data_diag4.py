# Psycho 2 · Diagnostische Psychologie · Teil 4 (Informelle und formelle Schulleistungstests)
# Quelle: Zusammenfassung „Diagnostik Teil 4“ von Konsti (aus „2025 Diagnostik Teil 4 KURZ“, 27 Folien).
# Klärungen von Konsti (21. Nov. 2026, Chat 1.17):
# - Ein Kapitel (d4), kein Vermerk.
# - Klassifikationsschema: beim formellen kriteriumsorientierten Zweig steht auf der Folie nur „(???)“.
#   „Formelle Schulleistungstests sind überwiegend sozialnormorientiert“ (Fachliteratur) nur als Hinweis, nicht abfragen;
#   kein Testbeispiel für den kriteriumsorientierten Zweig abfragen.
# - Vor-/Nachteil-Tabelle gilt als Vor- und Nachteile formeller Schulleistungstests und wird so abgefragt.
# - Zahlen dürfen abgefragt werden: 50–100 % mehr Aufgaben, 200–400 Schüler, Extemporale max. 20 Minuten,
#   Lederer: 100 Schulaufgaben, 2/3 gering komplex, 80 % halten die Reihenfolge ein. Jahr und Klassenstufen nur anzeigen.
# - Supermarkt-Aufgabe als Negativbeispiel abfragen; Comic (Newtons Gesetz) nur auf der Karte.
# - [ERGÄNZUNG]-Stellen nur als Hinweis auf Karten.
# MC im echten Klausurformat: genau 4 Optionen, 1–4 richtig. Richtige Optionen sind mit „*“ markiert.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

def H(t):
    return '<p><i>Hinweis (nicht auf der Folie): ' + t + '</i></p>'

KL = 'Teil 4 · Klassifikation'
FT = 'Teil 4 · Formelle Tests'
IT = 'Teil 4 · Informelle Tests'
AF = 'Teil 4 · Aufgabenformate'
PG = 'Teil 4 · Prüfungsgestaltung'

CARDS4 = [
    # ---------------------------------------------------------- Klassifikation
    C('ingenkamp', KL, 'Wie definiert <b>Ingenkamp (1997)</b> Schulleistungstests?',
      '<p>„Schulleistungstests sind Verfahren, mit deren Hilfe <b>Ergebnisse geplanter und an Curricula orientierter Lernvorgänge</b> möglichst <b>objektiv, zuverlässig und gültig</b> gemessen und durch <b>Lehrende oder Beratende</b> ausgewertet, interpretiert und für <b>pädagogisches Handeln</b> nutzbar gemacht werden können.“</p>',
      'Ingenkamp Definition Schulleistungstests Curricula objektiv zuverlässig gültig pädagogisches Handeln'),
    C('drei-arten', KL, 'Welche <b>drei Arten von Leistungstests</b> werden unterschieden?',
      '<ul><li><b>Formelle Leistungstests</b>: von <b>Experten(gremien)</b> entwickelt, z. B. PISA, VERA, TIMSS.</li><li><b>Informelle Leistungstests</b>: von <b>Lehrern nach festen Aufbaukriterien</b> konzipiert.</li><li><b>Informelle Tests</b>: von <b>Lehrern</b> entwickelt, <b>am Lehrstoff orientiert</b>, zur Überprüfung des Leistungsstandes <b>meist einer Klasse</b>.</li></ul>',
      'formelle Leistungstests informelle Leistungstests informelle Tests Experten Lehrer PISA VERA TIMSS'),
    C('schema', KL, 'Wie sieht das <b>Klassifikationsschema</b> der Leistungstests aus?',
      '<ul><li><b>Formelle Leistungstests</b><ul><li>sozialnormorientiert (PISA, VERA, TIMSS)</li><li>kriteriumsorientiert (auf der Folie als Beispiel nur „(???)“)</li></ul></li><li><b>Informelle Leistungstests</b> (keine weitere Unterteilung)</li><li><b>Informelle Tests</b><ul><li>schriftlich (Exen, Proben, Aufsätze, Essays)</li><li>mündlich (Ausfragen, Kolloquien)</li></ul></li></ul><p>Pfeil darunter: Die <b>Erfüllung der Gütekriterien nimmt ab</b> – von formellen Tests über informelle Leistungstests zu informellen Tests.</p>'
      + H('Die „(???)“ sind wohl Absicht: Es gibt kaum veröffentlichte formelle kriteriumsorientierte Schulleistungstests; in Deutschland sind fast alle standardisierten Schulleistungstests sozialnormorientiert.'),
      'Klassifikationsschema sozialnormorientiert kriteriumsorientiert schriftlich mündlich Exen Proben Ausfragen Kolloquien Gütekriterien nehmen ab'),
    C('formell-informell', KL, 'Wie unterscheiden sich <b>formelle Schulleistungstests</b> und <b>informelle Tests</b>?',
      '<table><tr><th>Formell</th><th>Informell</th></tr><tr><td>Ergebnis am <b>Ende</b> eines Kurses, Lehrgangs, Schuljahrs</td><td>Lernfortschritt <b>im Laufe</b> des Unterrichts</td></tr><tr><td>Erstellung <b>zentral</b></td><td>durch <b>Lehrende bei Bedarf</b></td></tr><tr><td>Lernstoff eines <b>Unterrichtszyklus</b></td><td><b>begrenzter</b> Lernstoff</td></tr><tr><td><b>kein</b> Bezug auf eine bestimmte, begrenzte Gruppe</td><td>Bezug auf eine <b>bestimmte, begrenzte Gruppe</b></td></tr><tr><td>Gütekriterien</td><td>keine Gütekriterien</td></tr><tr><td>offizielle Bewertungskriterien</td><td>keine offiziellen Bewertungskriterien</td></tr><tr><td><b>objektive</b> Aussagen über Wissen und Können</td><td>nur <b>subjektive</b> Aussagen (Gruppe, Unterrichtssituation)</td></tr><tr><td>Vorbereitung und terminliche Festlegung</td><td>ohne besondere Vorbereitung, nach Bedarf</td></tr><tr><td>zur Platzierung <b>geeignet</b></td><td>zur Platzierung <b>ungeeignet</b></td></tr><tr><td><b>Sozialnorm</b> oder <b>kriteriale Norm</b></td><td><b>kriteriale Norm</b></td></tr></table>',
      'formell informell Unterschied zentral Lehrende Gütekriterien objektiv subjektiv Platzierung Sozialnorm kriteriale Norm'),
    C('normen', KL, 'Was bedeuten <b>Sozialnorm</b> und <b>kriteriale Norm</b> bei Schulleistungstests?',
      '<ul><li><b>Sozialnorm</b>: Leistungen werden mit einer <b>großen repräsentativen Stichprobe</b> verglichen („Wie gut ist Schüler A verglichen mit allen Schülern seines Jahrgangs?“). Beispiele: <b>Jahrgangsstufentests, PISA, IGLU</b>.</li><li><b>Kriteriale Norm (formell)</b>: Wie gut ist der Schüler in Bezug auf ein <b>Kriterium</b>? Hat er das Leistungsziel erreicht? → <b>dichotom</b>.</li><li><b>Kriteriale Norm (informell)</b>: Leistungen werden mit dem <b>Inhalt des Curriculums</b> verglichen („Beherrscht Schüler A die Bruchrechnung?“). Beispiele: <b>Proben, Schulaufgaben, Exen</b>.</li></ul>',
      'Sozialnorm kriteriale Norm repräsentative Stichprobe Jahrgang dichotom Curriculum Bruchrechnung IGLU Proben'),

    # ---------------------------------------------------------- Formelle Tests
    C('konstruktion', FT, 'In welchen <b>sechs Schritten</b> wird ein formeller Schulleistungstest konstruiert?',
      '<ol><li><b>Analyse der Lehrpläne</b></li><li><b>Entwurf von Testitems</b>: <b>50–100 % mehr</b> Aufgaben als für die Endform nötig; Beurteilung durch erfahrene Lehrkräfte (<b>ExpertInnenrating</b>)</li><li><b>Vorerprobung an wenigen Fällen</b>: Verständlichkeit der Aufgabenformulierung</li><li><b>Testdurchführung an einer ersten Stichprobe (200–400 Schüler*innen)</b>: Aufgaben- und Testanalyse – Aufgabenschwierigkeit, Trennschärfe, erste Reliabilitätsschätzung</li><li><b>Testvalidierung an kleineren Stichproben</b></li><li><b>Testeichung und Validierung an einer repräsentativen Stichprobe</b>: Berechnung von <b>Normwerten</b></li></ol>',
      'Konstruktion formeller Test Schritte Lehrplananalyse Testitems Vorerprobung erste Stichprobe Trennschärfe Validierung Eichung Normwerte'),
    C('einsatz', FT, 'Wie lassen sich <b>formelle sozialnormorientierte Schulleistungstests</b> in der Schule einsetzen?',
      '<ul><li>Vergleich des Leistungsstandes der Klasse mit der <b>Eichstichprobe</b></li><li>Überprüfung des <b>eigenen Benotungssystems</b> durch Vergleich mit den Testwertklassen</li><li><b>Objektivierung</b> bei Schulart- oder Kurswechsel</li><li>Einteilung nach <b>Leistungsgruppen</b></li><li>als <b>Ersatz für Klassenarbeiten</b></li></ul>',
      'Einsatz formelle Tests Eichstichprobe Benotungssystem Schulartwechsel Leistungsgruppen Klassenarbeiten'),
    C('vor-nachteile', FT, 'Welche <b>Vor- und Nachteile</b> haben formelle Schulleistungstests?',
      '<table><tr><th>Vorteile</th><th>Nachteile</th></tr><tr><td>Erfüllung der <b>Gütekriterien</b></td><td><b>negative motivationale Folgen</b> (bes. für Leistungsschwache)</td></tr><tr><td>Überprüfung des <b>eigenen Benotungssystems</b></td><td><b>Erstarrung des Unterrichts</b> und <b>Verarmung der Lehrpläne</b></td></tr><tr><td><b>gerechtere Selektion</b></td><td><b>unfair</b> bei mangelnder Lerngelegenheit</td></tr><tr><td>Entdeckung <b>individueller Schwächen und Stärken</b></td><td><b>häufig veraltet</b></td></tr></table>'
      + H('Die Folie hat nur die Überschrift „Informelle und formelle Schulleistungstests“; aus dem Zusammenhang beziehen sich die Punkte auf formelle Tests.'),
      'Vorteile Nachteile formelle Schulleistungstests gerechtere Selektion Motivation Erstarrung Verarmung Lehrpläne veraltet'),
    C('auswahl', FT, 'Was ist bei der <b>Auswahl von Tests</b> grundsätzlich zu beachten?',
      '<ul><li><b>Gütekriterien</b></li><li><b>Normierung aktuell</b></li><li>ausreichend große <b>Eichstichprobe</b></li><li><b>Aktualität des Materials</b></li><li><b>Durchführungsdauer / Ökonomie</b></li></ul>',
      'Testauswahl Gütekriterien Normierung Eichstichprobe Aktualität Material Durchführungsdauer Ökonomie'),

    # ---------------------------------------------------------- Informelle Tests
    C('comic', IT, 'Was zeigt der <b>Comic</b> auf der Einstiegsfolie zur Konstruktion informeller Tests?',
      '<p>Ein Schüler soll „Newtons erstes Gesetz <b>in eigenen Worten</b> erklären“ und schreibt Fantasiewörter – es sind ja „eigene Worte“.</p>'
      + H('Die Folie nennt keine Aussage. Wahrscheinlich soll der Comic zeigen: Aufgaben und Lehrziele müssen präzise formuliert bzw. operationalisiert sein, sonst lassen sie unerwünschte Lösungen zu.'),
      'Comic Newton eigene Worte Aufgabe präzise'),
    C('lehrziele', IT, 'Was misst ein informeller Test laut <b>Wilson (2005)</b>, Schritt 1? Was sind <b>Lehrziele</b>?',
      '<p><b>1. Das Konstrukt – Was wird gemessen?</b> → <b>Lehrziele</b> (viele Synonyme: Instruktionsziele, Lernziele usw.; „Lehrziele“, weil es um Ziele geht, die Lehrende setzen und deren Erreichung sie überprüfen).</p><p>Definition (<b>Lukesch, 1998</b>): „Umschreibungen von bestimmten <b>Persönlichkeitseigenschaften</b> (Fähigkeiten, Fertigkeiten, Neigungen, Gesinnungen, Haltungen), die es bei einem Schüler zu <b>verwirklichen</b> gilt.“</p><p>Die spätere Folie „Die Aufgaben: <b>Wie</b> wird gemessen?“ entspricht inhaltlich dem nächsten Schritt.</p>',
      'Wilson Konstrukt Lehrziele Lukesch Definition Persönlichkeitseigenschaften Lernziele'),
    C('lehrziele-relevanz', IT, 'Warum sind <b>Lehrziele</b> relevant, und was muss man dafür wissen?',
      '<p><b>Relevanz:</b></p><ul><li>Man kann den <b>Unterricht danach ausrichten</b>.</li><li>Um den „an der Schule mittelbar und unmittelbar Beteiligten“ (Schüler*innen, Eltern …) zu <b>kommunizieren</b>, was gelehrt werden soll.</li><li>Als <b>konkrete Basis für die Leistungsüberprüfung</b>.</li></ul><p><b>Dazu muss man wissen</b> (Gronlund & Brookhart, 2009):</p><ul><li>was die Schüler*innen lernen sollen (<b>Inhalte</b>),</li><li>welche <b>Schüler*innenaktivitäten zeigen</b>, dass gelernt wurde,</li><li>welche <b>Aufgaben/Methoden</b> sich am besten eignen, um eine Lernleistung zu erfassen und zu bewerten.</li></ul>',
      'Lehrziele Relevanz Unterricht ausrichten kommunizieren Basis Leistungsüberprüfung Gronlund Brookhart'),
    C('lehrziele-probleme', IT, 'Welche <b>Probleme</b> haben Lehrziele?',
      '<ul><li>Oft <b>zu vage</b> formuliert: „Verstehen“ oder „Beherrschen“ eines Stoffes – was genau heißt das?</li><li>Lehrziele sind <b>hypothetische, nicht beobachtbare Konstrukte</b>.</li><li>Man muss spezifizieren, wann welches <b>Verhalten</b> Rückschlüsse auf „Kenntnis“, „Verständnis“ usw. zulässt = <b>Operationalisierung</b> der Konstrukte.</li></ul>',
      'Lehrziele Probleme vage hypothetisch nicht beobachtbar Konstrukt Operationalisierung'),
    C('bloom', IT, 'Welche Stufen hat die <b>Lehrzieltaxonomie nach Bloom (1972)</b>?',
      '<p>Lehrzieltaxonomie = Klassifikation zur Unterteilung von Lehrzielen. Pyramide von <b>unten (niedrigste)</b> nach <b>oben (höchste)</b>, Beispiele zum Thema Pflanzen:</p><table><tr><th>Stufe</th><th>Beispiel</th></tr><tr><td>1. <b>Wissen</b></td><td>Nennen Sie die Bestandteile einer Pflanze.</td></tr><tr><td>2. <b>Verstehen</b></td><td>Warum gedeihen Pflanzen auf verschiedenen Böden unterschiedlich gut?</td></tr><tr><td>3. <b>Anwendung</b></td><td>Welche Folgen haben Entlaubungsmittel für eine Pflanze?</td></tr><tr><td>4. <b>Analyse</b></td><td>Wenn eine Pflanze wenig Wasser verdunsten kann … wächst sie langsamer / erzeugt mehr Nährstoffe / bildet die Wurzel besser aus</td></tr><tr><td>5. <b>Synthese</b></td><td>Pflanzen können sich nur ernähren, wenn sie gerade gewachsen sind. Wie lässt sich diese Aussage beweisen?</td></tr><tr><td>6. <b>Bewerten</b></td><td>Halten Sie die Umweltpolitik der aktuellen Regierung für sinnvoll?</td></tr></table>',
      'Bloom Taxonomie Lehrziele Wissen Verstehen Anwendung Analyse Synthese Bewerten Pyramide'),
    C('grundsaetze', IT, 'Welche zwei <b>Grundsätze</b> gelten beim Konzipieren von Prüfungen?',
      '<ul><li><b>Grundsatz der proportionalen Abbildung</b>: Kompetenz wird an Inhalts- und Aufgabenstichproben überprüft → die Aufgabenstichprobe muss einen <b>repräsentativen Querschnitt</b> des vorangegangenen Unterrichts darstellen. (Häufig überproportional viele <b>mittelschwere</b> Aufgaben = <b>Nachteil für Leistungsschwache</b>.)</li><li><b>Grundsatz der Variabilität</b>: <b>Alle Prüfungsmodalitäten bevorzugen bestimmte Schüler*innen und benachteiligen andere</b> → Varianz in Formenreichtum, Umfang und Komplexität.</li></ul>',
      'Grundsatz proportionale Abbildung repräsentativer Querschnitt mittelschwer Variabilität Prüfungsmodalitäten'),
    C('inhalte-formen', IT, 'Was gilt für <b>Prüfungsinhalte</b> und <b>Prüfungsformen</b>? Vor- und Nachteile mündlich/schriftlich?',
      '<p><b>Inhalte:</b> vorzuziehen sind Inhalte, die für den <b>weiteren Lernprozess</b> von Bedeutung sind.</p><p><b>Formen</b> (schriftlich, mündlich, praktisch) sollten mit der <b>Arbeitsform des vergangenen Unterrichts</b> übereinstimmen.</p><table><tr><th>Mündlich</th><th>Schriftlich</th></tr><tr><td>durch Nachfragen mehr <b>in die Tiefe</b></td><td><b>einfach</b> zu organisieren</td></tr><tr><td>mehr <b>Hilfestellung</b> möglich</td><td><b>rechtlich sicherer</b></td></tr><tr><td><b>adaptives Testen</b> möglich</td><td>Problemfall: <b>Extemporale</b> als Ersatz für mündliche Beurteilungen</td></tr><tr><td>oft <b>angstbesetzt</b>, wenig Zeit zum Überlegen</td><td></td></tr></table>',
      'Prüfungsinhalte Lernprozess Prüfungsformen Arbeitsform mündlich schriftlich adaptiv angstbesetzt rechtlich sicherer Extemporale'),

    # ---------------------------------------------------------- Aufgabenformate
    C('formate', AF, 'Welche <b>Aufgabenformate</b> gibt es bei informellen Tests?',
      '<ul><li><b>Performanz</b></li><li><b>Kurze Antworten</b><ul><li><b>offen</b> (Ergänzungsaufgaben)</li><li><b>geschlossen</b>: Richtig/Falsch, Mehrfachwahl, Zuordnung</li></ul></li><li><b>Lange Antworten</b> (Essay, offen)</li></ul>',
      'Aufgabenformate Performanz kurze Antworten offen geschlossen Richtig Falsch Mehrfachwahl Zuordnung lange Antworten Essay'),
    C('performanz', AF, 'Was sind <b>Performanzaufgaben</b>? (Beispiel Bowling)',
      '<p><b>„Show how“ statt „Know how“</b>: nicht zeigen, was man weiß, sondern <b>tun, was man weiß</b> (Ingenkamp & Lissmann, 2008).</p><p>Beispiel: Als Kapitän der Bowling-Mannschaft zwischen Bill und Dave wählen und die Wahl <b>mit den Daten begründen</b> und erklären, wie man zur Entscheidung kam.</p><ul><li>Dave: 152, 138, 141, 144, 141, 138</li><li>Bill: 210, 105, 118, 131, 105, 215</li></ul>'
      + H('Keine Musterlösung auf der Folie. Dave spielt konstant (Mittel ≈ 142,3), Bill schwankt stark (Mittel ≈ 147,3); je nach Argumentation sind beide wählbar – bewertet wird die Begründung.'),
      'Performanzaufgaben Show how Know how Ingenkamp Lissmann Bowling'),
    C('langantwort', AF, 'Welche Arten von <b>Langantworten</b> (Kurzaufsätze, Essays) zeigt die Folie?',
      '<ul><li><b>Freie Gestaltung</b>: „Sind MC-Aufgaben geeignet, um Verständnis zu erfassen? Begründen Sie kurz (max. fünf Sätze).“</li><li><b>Freie Assoziation / Brainstorming</b>: „Schreiben Sie möglichst viele Bands auf, die mit ‚P‘ beginnen!“</li><li><b>Kreativität</b>: „Wie könnten Sie bei der Klausur ‚spicken‘? Überlegen Sie sich originelle Varianten.“</li></ul>',
      'Langantwort Essay Kurzaufsatz freie Gestaltung freie Assoziation Brainstorming Kreativität'),
    C('ergaenzung', AF, 'Was sind <b>Ergänzungsaufgaben</b> (offene Kurzantwort)?',
      '<ul><li>Aufgabenform mit <b>freien Antworten</b>.</li><li><b>Keine festen Antwortkategorien</b>; Beantwortung <b>frei oder teilstrukturiert</b> (Teile der Lösung vorgegeben).</li></ul><p>Beispiele (Lückentext): Der 30-jährige Krieg wurde mit dem … beendet (Westfälischen Frieden). · Die Biene bringt … auf den Stempel der Blüte (Pollen). · 20 € sind … % von 200 € (10).</p>',
      'Ergänzungsaufgaben offene Kurzantwort freie Antworten teilstrukturiert Lückentext'),
    C('wahr-falsch', AF, 'Was kennzeichnet <b>Zweifachwahl- / Wahr-Falsch-Aufgaben</b>?',
      '<ul><li><b>Kurze und gebundene</b> Antworten.</li><li><b>Feste Antwortkategorien</b>, komplett vorstrukturiert.</li></ul><p>Beispiele: „Die Reliabilität zeigt, ob ein Test misst, was er messen soll.“ → falsch (Validität). · „Der Messfehler ist abhängig vom Messzeitpunkt.“ → falsch. · „5 × 7 + 3 − 16 / 4 = 34“ → wahr.</p>',
      'Zweifachwahl Wahr-Falsch gebunden feste Antwortkategorien vorstrukturiert'),
    C('mc', AF, 'Wie sind <b>Multiple-Choice-Aufgaben</b> aufgebaut?',
      '<ul><li><b>Itemstamm</b> und mehrere <b>Antwortalternativen</b>: <b>eine</b> richtig (<b>n-alternative, forced-choice</b>) oder <b>mehrere</b> richtig (<b>multiple-choice</b>).</li><li>Itemstamm: eine <b>Frage</b> oder eine <b>unvollständige Aussage</b>.</li><li><b>Attraktor</b> = richtige Alternative(n)</li><li><b>Distraktoren</b> = falsche Alternative(n)</li></ul>',
      'Multiple Choice Itemstamm Antwortalternativen Attraktor Distraktor forced-choice n-alternative'),
    C('vgl-performanz', AF, 'Vergleich der Aufgabenformate: Was gilt für <b>Performanzaufgaben</b>?',
      '<ul><li>Für einige Fertigkeiten (Musikinstrumente, Sport, Sprachen) <b>alternativlos</b></li><li><b>hohe ökologische Validität</b></li><li><b>höhere kognitive Lehrziele</b> können erfasst werden</li><li><b>zeitaufwendig</b></li><li>Erstellung von <b>Bewertungskriterien oft nicht einfach</b></li><li>(Auswertungs-)<b>Objektivität gering</b></li></ul>',
      'Performanzaufgaben Vorteile Nachteile ökologische Validität alternativlos Objektivität gering'),
    C('vgl-geschlossen', AF, 'Vergleich der Aufgabenformate: Was gilt für <b>geschlossene Aufgaben</b>?',
      '<ul><li>nur <b>passives Wissen</b> überprüfbar</li><li><b>keine Prozessdiagnostik</b> möglich</li><li>Erfassung <b>kreativer Leistungen nicht möglich</b></li><li><b>zeitaufwändig in der Erstellung, schnell in der Korrektur</b></li><li>schnellere Bearbeitung → <b>mehr Aufgaben</b> möglich → <b>Verbesserung der Reliabilität</b></li><li>Leistungen <b>besser vergleichbar</b></li><li><b>Rateerfolg höher</b></li></ul>',
      'geschlossene Aufgaben passives Wissen Prozessdiagnostik kreativ Erstellung Korrektur Reliabilität vergleichbar Rateerfolg'),
    C('vgl-offen', AF, 'Vergleich der Aufgabenformate: Was gilt für <b>offene Aufgaben</b>?',
      '<ul><li><b>aktives Wissen</b> überprüfbar, passives nicht → <b>Kenntnisstand wird unterschätzt</b></li><li><b>hohe Sprachkompetenz</b> notwendig → Validität?</li><li><b>zeitaufwändig in der Korrektur</b></li></ul>',
      'offene Aufgaben aktives Wissen Kenntnisstand unterschätzt Sprachkompetenz Validität Korrektur'),

    # ---------------------------------------------------------- Prüfungsgestaltung
    C('anforderung', PG, 'Was gilt für das <b>Anforderungsniveau</b> einer Prüfung?',
      '<ul><li><b>Übereinstimmung</b> von Prüfungsniveau mit <b>Unterrichtsniveau</b>.</li><li><b>Unfair</b>: eine besonders schwere Aufgabe („<b>Einserbremse</b>“) zur Bestimmung der Leistungsbesten → viele Fünfer und Sechser.</li><li>Besser: <b>mehrere anspruchsvolle Aufgaben</b>.</li></ul>',
      'Anforderungsniveau Unterrichtsniveau Einserbremse unfair mehrere anspruchsvolle Aufgaben'),
    C('formulierung', PG, 'Was gilt für die <b>Aufgabenformulierung</b>? (Beispiel Supermarkt)',
      '<ul><li><b>Schlichtes Sprachniveau</b>, da das Sprachverständnis durch <b>Nervosität</b> oft eingeschränkt ist.</li><li><b>Strukturierungshilfen</b> (Hervorhebungen, Nummerierungen, Grafiken).</li></ul><p>Beispiel der Folie: lange, unstrukturierte Textaufgabe (Vater kauft im Supermarkt ein, zahlt mit 100-€-Schein, nimmt an der Kasse noch Bonbons und Schokolade mit – was bekommt er heraus?) = <b>Negativbeispiel</b>: ein einziger Fließtext ohne Hervorhebungen, Nummerierung oder Tabelle; eine Information kommt zeitlich versetzt dazu.</p>'
      + H('Rechnerisch 31,20 € Einkauf, 68,80 € Rückgeld.'),
      'Aufgabenformulierung schlichtes Sprachniveau Nervosität Strukturierungshilfen Supermarkt Negativbeispiel'),
    C('umfang', PG, 'Was gilt für den <b>Prüfungsumfang</b>? (Extemporale, Lederer 1998)',
      '<ul><li><b>Je mehr Aufgaben, desto reliabler</b> – aber oft nur schlichte Fakten abprüfbar; Komplexes ist umfangreicher und zeitintensiver → <b>Mischung sinnvoll</b>.</li><li><b>Nur sehr wenige Aufgaben vermeiden</b>, da Glück und Pech eine große Rolle spielen.</li><li>Problemfall <b>Extemporale</b>: höchstens <b>20 Minuten</b>, bezieht sich auf die <b>letzte Unterrichtsstunde</b> bzw. Grundkenntnisse → nur wenige Aufgaben möglich.</li><li><b>Lederer (1998)</b>: Analyse von <b>100 Schulaufgaben</b> (mehrere Fächer, 7.–10. Klasse Realschule). In der Praxis dominieren wenig komplexe Aufgaben: <b>2/3</b> aller Aufgaben haben einen <b>geringen Komplexitätsgrad</b>.</li></ul>',
      'Prüfungsumfang reliabel Mischung wenige Aufgaben Glück Pech Extemporale 20 Minuten Lederer Schulaufgaben Komplexität'),
    C('reihenfolge', PG, 'Was gilt für die <b>Reihenfolge der Aufgaben</b>?',
      '<ul><li>Die Reihenfolge wird <b>in der Regel den Schüler*innen überlassen</b>.</li><li>Deshalb: <b>leichtere</b>, wenig komplexe Aufgaben an den <b>Anfang</b> (Kompetenzerleben), <b>hoch komplexe</b> im <b>Mittelteil</b>, gegen <b>Ende wieder leichtere</b> (wegen Ermüdung).</li><li><b>Lederer (1998)</b>, gleiche 100 Schulaufgaben: <b>80 %</b> der Schüler halten die gegebene Reihenfolge ein. Komplexe Aufgaben <b>am Ende</b> werden <b>weniger in Angriff genommen</b>. Leistungsrückgang besonders hoch bei <b>Matheaufgaben</b>.</li></ul>'
      + H('Obwohl die Reihenfolge freigestellt ist, halten sich die meisten an die vorgegebene – die Anordnung durch die Lehrkraft beeinflusst die Leistung deshalb stark.'),
      'Reihenfolge Aufgaben leicht Anfang komplex Mitte Ende Ermüdung Kompetenzerleben Lederer 80 Prozent Mathe'),
    C('punkte', PG, 'Was gilt für die <b>Punkte- und Fehlerzuweisung</b>?',
      '<ul><li><b>Jede Teilleistung ist gleich zu gewichten.</b></li><li><b>Nicht</b> für komplexere Aufgaben mehr Punkte vergeben → sonst <b>Nachteil für schwächere Schüler</b>.</li></ul>',
      'Punktevergabe Fehlerzuweisung Teilleistung gleich gewichten komplexe Aufgaben schwächere Schüler'),
]

ITEMS4 = []
S = 'Diagnostik · Teil 4'
def mc(id, q, options, expl, kw):
    assert len(options) == 4, id
    corr = [i for i, o in enumerate(options) if o.startswith('*')]
    assert 1 <= len(corr) <= 4, id
    opts = [o[1:] if o.startswith('*') else o for o in options]
    ITEMS4.append(dict(id=id, type='mc', q=q, options=opts, correct=corr[0] if len(corr) == 1 else corr, expl=expl, src=S, kw=kw))
def tf(id, statement, answer, expl, kw):
    ITEMS4.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=S, kw=kw))
def gap(id, text, expl, kw):
    ITEMS4.append(dict(id=id, type='gap', text=text, expl=expl, src=S, kw=kw))

# ---- Multiple Choice
mc('pd4-mc-01', 'Was gehört zur Definition von <b>Schulleistungstests nach Ingenkamp (1997)</b>?',
   ['*Sie messen Ergebnisse geplanter, an Curricula orientierter Lernvorgänge.', '*Die Messung soll möglichst objektiv, zuverlässig und gültig sein.', '*Die Ergebnisse sollen für pädagogisches Handeln nutzbar gemacht werden.', 'Sie werden ausschließlich von Expertengremien ausgewertet.'],
   'Ausgewertet und interpretiert werden sie durch Lehrende oder Beratende.', 'Ingenkamp Definition')
mc('pd4-mc-02', 'Welche Tests nennt die Folie als Beispiele für <b>formelle Leistungstests</b>?',
   ['*PISA', '*VERA', '*TIMSS', 'Exen'],
   'Exen sind schriftliche informelle Tests.', 'formelle Leistungstests Beispiele')
mc('pd4-mc-03', 'Wer entwickelt welche Art von Leistungstest?',
   ['*Formelle Leistungstests: Experten(gremien)', '*Informelle Leistungstests: Lehrer nach festen Aufbaukriterien', '*Informelle Tests: Lehrer, orientiert am Lehrstoff', 'Informelle Tests: Expertengremien nach festen Aufbaukriterien'],
   'Informelle Tests dienen meist der Überprüfung des Leistungsstandes einer Klasse.', 'drei Arten Leistungstests')
mc('pd4-mc-04', 'Was zeigt der Pfeil „<b>Erfüllung der Gütekriterien</b>“ im Klassifikationsschema?',
   ['*Die Erfüllung nimmt von formellen Tests über informelle Leistungstests zu informellen Tests ab.', 'Die Erfüllung nimmt von informellen zu formellen Tests ab.', 'Alle drei Testarten erfüllen die Gütekriterien gleich gut.', 'Nur informelle Tests erfüllen die Gütekriterien.'],
   'Der Pfeil wird von links (formell) nach rechts (informell) schmaler.', 'Gütekriterien Klassifikationsschema')
mc('pd4-mc-05', 'Wie werden <b>informelle Tests</b> im Klassifikationsschema unterteilt?',
   ['*schriftlich, z. B. Exen, Proben, Aufsätze, Essays', '*mündlich, z. B. Ausfragen, Kolloquien', 'sozialnormorientiert, z. B. PISA', 'kriteriumsorientiert, z. B. VERA'],
   'Die Unterteilung sozialnorm- vs. kriteriumsorientiert gehört zu den formellen Leistungstests.', 'informelle Tests schriftlich mündlich')
mc('pd4-mc-06', 'Was trifft auf <b>formelle Schulleistungstests</b> zu (im Vergleich zu informellen Tests)?',
   ['*Erstellung zentral', '*zur Platzierung geeignet', '*objektive Aussagen über Wissen und Können', 'Bezug auf eine bestimmte, begrenzte Gruppe'],
   'Der Bezug auf eine bestimmte, begrenzte Gruppe kennzeichnet informelle Tests.', 'formell informell Vergleich')
mc('pd4-mc-07', 'Was trifft auf <b>informelle Tests</b> zu?',
   ['*Feststellung des Lernfortschritts im Laufe des Unterrichts', '*keine Gütekriterien', '*zur Platzierung ungeeignet', 'orientiert an der Sozialnorm'],
   'Informelle Tests orientieren sich an der kriterialen Norm.', 'informelle Tests Merkmale')
mc('pd4-mc-08', 'An welcher Norm können sich <b>formelle Schulleistungstests</b> orientieren?',
   ['*an der Sozialnorm', '*an der kriterialen Norm', 'nur an der individuellen Norm', 'an keiner Norm'],
   'Formell: Sozialnorm (a) oder kriteriale Norm (b). Informell: kriteriale Norm.', 'formell Sozialnorm kriteriale Norm')
mc('pd4-mc-09', 'Was kennzeichnet die <b>Sozialnorm</b> bei Schulleistungstests?',
   ['*Vergleich mit einer großen repräsentativen Stichprobe', '*Frage: Wie gut ist Schüler A verglichen mit allen Schülern seines Jahrgangs?', '*Beispiele: Jahrgangsstufentests, PISA, IGLU', 'Frage: Beherrscht Schüler A die Bruchrechnung?'],
   '„Beherrscht Schüler A die Bruchrechnung?“ ist die kriteriale Norm bei informellen Tests.', 'Sozialnorm')
mc('pd4-mc-10', 'Was kennzeichnet die <b>kriteriale Norm</b>?',
   ['*Bei formellen Tests: Hat der Schüler das Leistungsziel erreicht? (dichotom)', '*Bei informellen Tests: Vergleich der Leistungen mit dem Inhalt des Curriculums', '*Beispiele bei informellen Tests: Proben, Schulaufgaben, Exen', 'Vergleich mit allen Schülern des Jahrgangs'],
   'Der Vergleich mit dem Jahrgang ist die Sozialnorm.', 'kriteriale Norm')
mc('pd4-mc-11', 'Was ist der <b>erste Schritt</b> bei der Konstruktion eines formellen Schulleistungstests?',
   ['*Analyse der Lehrpläne', 'Entwurf von Testitems', 'Vorerprobung an wenigen Fällen', 'Testeichung an einer repräsentativen Stichprobe'],
   'Reihenfolge: Lehrpläne → Testitems → Vorerprobung → erste Stichprobe → Validierung an kleineren Stichproben → Eichung.', 'Konstruktion Reihenfolge')
mc('pd4-mc-12', 'Was gehört zum Schritt <b>Entwurf von Testitems</b>?',
   ['*50–100 % mehr Aufgaben konstruieren, als für die Endform nötig', '*Beurteilung der Aufgaben durch erfahrene Lehrkräfte (ExpertInnenrating)', 'Berechnung von Normwerten', 'Trennschärfenberechnung'],
   'Normwerte entstehen bei der Eichung (letzter Schritt), Trennschärfen bei der ersten Stichprobe.', 'Testitems ExpertInnenrating')
mc('pd4-mc-13', 'Was geschieht bei der <b>Testdurchführung an der ersten Stichprobe</b>?',
   ['*Ermittlung der Aufgabenschwierigkeit', '*Trennschärfenberechnung', '*erste Reliabilitätsschätzung', 'Überprüfung der Verständlichkeit an wenigen Fällen'],
   'Die Verständlichkeit wird vorher bei der Vorerprobung an wenigen Fällen geprüft.', 'erste Stichprobe Testanalyse')
mc('pd4-mc-14', 'Wie groß ist laut Folie die <b>erste Stichprobe</b> bei der Konstruktion formeller Tests?',
   ['*200–400 Schüler*innen', '20–40 Schüler*innen', '1000–2000 Schüler*innen', '50–100 Schüler*innen'],
   'Danach folgen Validierung an kleineren Stichproben und Eichung an einer repräsentativen Stichprobe.', 'erste Stichprobe Größe')
mc('pd4-mc-15', 'In welchem Schritt werden <b>Normwerte</b> berechnet?',
   ['*bei der Testeichung und Validierung an einer repräsentativen Stichprobe', 'bei der Vorerprobung an wenigen Fällen', 'bei der Analyse der Lehrpläne', 'beim Entwurf der Testitems'],
   'Testeichung ist der sechste und letzte Schritt.', 'Normwerte Eichung')
mc('pd4-mc-16', 'Welche <b>Einsatzmöglichkeiten formeller sozialnormorientierter Tests</b> nennt die Folie?',
   ['*Vergleich des Leistungsstandes der Klasse mit der Eichstichprobe', '*Überprüfung des eigenen Benotungssystems', '*Einteilung nach Leistungsgruppen', '*als Ersatz für Klassenarbeiten'],
   'Außerdem: Objektivierung bei Schulart- oder Kurswechsel.', 'Einsatz formelle Tests')
mc('pd4-mc-17', 'Welche <b>Vorteile</b> formeller Schulleistungstests nennt die Folie?',
   ['*gerechtere Selektion', '*Hilfe bei der Entdeckung individueller Schwächen und Stärken', '*Erfüllung der Gütekriterien', 'Bereicherung der Lehrpläne'],
   'Im Gegenteil: Ein Nachteil ist die Verarmung der Lehrpläne.', 'Vorteile formelle Tests')
mc('pd4-mc-18', 'Welche <b>Nachteile</b> formeller Schulleistungstests nennt die Folie?',
   ['*negative motivationale Folgen, besonders für Leistungsschwache', '*Erstarrung des Unterrichts', '*unfair bei mangelnder Lerngelegenheit', '*häufig veraltet'],
   'Außerdem: Verarmung der Lehrpläne.', 'Nachteile formelle Tests')
mc('pd4-mc-19', 'Was ist bei der <b>Auswahl von Tests</b> grundsätzlich zu beachten?',
   ['*Gütekriterien', '*aktuelle Normierung', '*ausreichend große Eichstichprobe', '*Durchführungsdauer / Ökonomie'],
   'Außerdem: Aktualität des Materials.', 'Testauswahl')
mc('pd4-mc-20', 'Was sind <b>Lehrziele</b> nach Lukesch (1998)?',
   ['*Umschreibungen bestimmter Persönlichkeitseigenschaften, die es bei einem Schüler zu verwirklichen gilt', '*Dazu zählen Fähigkeiten, Fertigkeiten, Neigungen, Gesinnungen, Haltungen.', 'direkt beobachtbare Verhaltensweisen', 'die Noten, die ein Schüler erreichen soll'],
   'Lehrziele sind hypothetische, nicht beobachtbare Konstrukte.', 'Lehrziele Lukesch')
mc('pd4-mc-21', 'Warum sind <b>Lehrziele</b> relevant?',
   ['*Man kann den Unterricht danach ausrichten.', '*Man kann den Beteiligten (Schüler*innen, Eltern …) kommunizieren, was gelehrt werden soll.', '*Sie sind eine konkrete Basis für die Leistungsüberprüfung.', 'Sie ersetzen die Gütekriterien.'],
   'Dazu muss man nach Gronlund & Brookhart (2009) Inhalte, zeigende Aktivitäten und geeignete Aufgaben/Methoden kennen.', 'Lehrziele Relevanz')
mc('pd4-mc-22', 'Welche <b>Probleme von Lehrzielen</b> nennt die Folie?',
   ['*Sie sind oft zu vage formuliert, z. B. „Verstehen“ oder „Beherrschen“.', '*Sie sind hypothetische, nicht beobachtbare Konstrukte.', '*Sie müssen operationalisiert werden.', 'Sie lassen sich direkt beobachten.'],
   'Operationalisierung: festlegen, welches Verhalten Rückschlüsse auf „Kenntnis“ oder „Verständnis“ zulässt.', 'Lehrziele Probleme Operationalisierung')
mc('pd4-mc-23', 'Welche Reihenfolge der <b>Bloom-Taxonomie</b> (von unten nach oben) ist richtig?',
   ['*Wissen – Verstehen – Anwendung – Analyse – Synthese – Bewerten', 'Wissen – Anwendung – Verstehen – Synthese – Analyse – Bewerten', 'Verstehen – Wissen – Analyse – Anwendung – Bewerten – Synthese', 'Bewerten – Synthese – Analyse – Anwendung – Verstehen – Wissen'],
   'Wissen ist die niedrigste, Bewerten die höchste Stufe.', 'Bloom Reihenfolge')
mc('pd4-mc-24', 'Bloom: Zu welcher Stufe gehört die Aufgabe „<b>Nennen Sie die verschiedenen Bestandteile einer Pflanze.</b>“?',
   ['*Wissen', 'Verstehen', 'Anwendung', 'Analyse'],
   'Wissen ist die unterste Stufe.', 'Bloom Wissen Beispiel')
mc('pd4-mc-25', 'Bloom: Zu welcher Stufe gehört „<b>Halten Sie die Umweltpolitik der aktuellen Regierung für sinnvoll?</b>“?',
   ['*Bewerten', 'Synthese', 'Analyse', 'Verstehen'],
   'Bewerten ist die höchste Stufe.', 'Bloom Bewerten Beispiel')
mc('pd4-mc-26', 'Bloom: Welche Zuordnungen von Beispielaufgabe und Stufe stimmen?',
   ['*„Warum gedeihen Pflanzen auf verschiedenen Böden unterschiedlich gut?“ – Verstehen', '*„Welche Folgen haben Entlaubungsmittel für eine Pflanze?“ – Anwendung', '*„Wie lässt sich die Aussage beweisen, dass Pflanzen sich nur beim Wachsen ernähren?“ – Synthese', '„Nennen Sie die Bestandteile einer Pflanze.“ – Analyse'],
   'Das Nennen der Bestandteile gehört zu Wissen. Analyse: „Wenn eine Pflanze wenig Wasser verdunsten kann …“ mit Antwortvorgaben.', 'Bloom Beispiele Zuordnung')
mc('pd4-mc-27', 'Was besagt der <b>Grundsatz der proportionalen Abbildung</b>?',
   ['*Die Aufgabenstichprobe muss einen repräsentativen Querschnitt des vorangegangenen Unterrichts darstellen.', '*Kompetenz wird an Inhalts- und Aufgabenstichproben überprüft.', 'Alle Prüfungsmodalitäten bevorzugen bestimmte Schüler*innen.', 'Komplexe Aufgaben sollen mehr Punkte bekommen.'],
   'Die Bevorzugung durch Prüfungsmodalitäten gehört zum Grundsatz der Variabilität.', 'proportionale Abbildung')
mc('pd4-mc-28', 'Was besagt der <b>Grundsatz der Variabilität</b>?',
   ['*Alle Prüfungsmodalitäten bevorzugen bestimmte Schüler*innen und benachteiligen andere.', '*Deshalb soll man in Formenreichtum, Umfang und Komplexität variieren.', 'Die Prüfung soll immer dieselbe Form haben.', 'Die Aufgabenstichprobe muss den Unterricht repräsentativ abbilden.'],
   'Der repräsentative Querschnitt ist der Grundsatz der proportionalen Abbildung.', 'Grundsatz Variabilität')
mc('pd4-mc-29', 'Welche <b>Vorteile mündlicher Prüfungen</b> nennt die Folie?',
   ['*durch Nachfragen mehr in die Tiefe gehen', '*mehr Hilfestellung möglich', '*adaptives Testen möglich', 'rechtlich sicherer'],
   '„Rechtlich sicherer“ gilt für schriftliche Prüfungen. Nachteil mündlich: oft angstbesetzt.', 'mündliche Prüfung')
mc('pd4-mc-30', 'Was nennt die Folie zu <b>geschlossenen Aufgaben</b>?',
   ['*nur passives Wissen überprüfbar', '*keine Prozessdiagnostik möglich', '*zeitaufwändig in der Erstellung, schnell in der Korrektur', 'Erfassung kreativer Leistungen möglich'],
   'Kreative Leistungen sind mit geschlossenen Aufgaben nicht erfassbar.', 'geschlossene Aufgaben')
mc('pd4-mc-31', 'Warum verbessern geschlossene Aufgaben die <b>Reliabilität</b>?',
   ['*Schnellere Bearbeitung ermöglicht eine größere Zahl von Aufgaben.', 'Sie haben keinen Rateerfolg.', 'Sie erfassen aktives Wissen.', 'Sie erlauben Prozessdiagnostik.'],
   'Geschlossene Aufgaben haben sogar einen höheren Rateerfolg.', 'geschlossene Aufgaben Reliabilität')
mc('pd4-mc-32', 'Was nennt die Folie zu <b>offenen Aufgaben</b>?',
   ['*Aktives Wissen ist überprüfbar.', '*Der Kenntnisstand wird unterschätzt.', '*Hohe Sprachkompetenz ist notwendig.', '*zeitaufwändig in der Korrektur'],
   'Passives Wissen ist mit offenen Aufgaben nicht überprüfbar.', 'offene Aufgaben')
mc('pd4-mc-33', 'Was nennt die Folie zu <b>Performanzaufgaben</b>?',
   ['*hohe ökologische Validität', '*höhere kognitive Lehrziele können erfasst werden', '*(Auswertungs-)Objektivität gering', 'schnell in der Korrektur'],
   'Performanzaufgaben sind zeitaufwendig; Bewertungskriterien sind oft nicht einfach zu erstellen.', 'Performanzaufgaben')
mc('pd4-mc-34', 'Wie heißen die Teile einer <b>Multiple-Choice-Aufgabe</b>?',
   ['*Itemstamm', '*Attraktor = richtige Alternative', '*Distraktor = falsche Alternative', 'Distraktor = richtige Alternative'],
   'Der Itemstamm kann eine Frage oder eine unvollständige Aussage sein.', 'Multiple Choice Attraktor Distraktor')
mc('pd4-mc-35', 'Welche Aussagen zur <b>Extemporale</b> treffen laut Folie zu?',
   ['*Sie darf nicht länger als 20 Minuten dauern.', '*Sie bezieht sich auf die letzte Unterrichtsstunde bzw. Grundkenntnisse.', '*Es sind nur wenige Aufgaben möglich.', 'Sie ist eine formelle Prüfung mit Gütekriterien.'],
   'Die Extemporale gilt als Problemfall, auch als Ersatz für mündliche Beurteilungen.', 'Extemporale')
mc('pd4-mc-36', 'Was fand <b>Lederer (1998)</b> bei der Analyse von 100 Schulaufgaben?',
   ['*2/3 aller Aufgaben haben einen geringen Komplexitätsgrad.', '*80 % der Schüler halten die gegebene Aufgabenreihung ein.', '*Komplexe Aufgaben am Ende werden weniger in Angriff genommen.', 'Die meisten Aufgaben sind hoch komplex.'],
   'In der Praxis dominieren wenig komplexe Aufgaben. Leistungsrückgang besonders hoch bei Matheaufgaben.', 'Lederer Schulaufgaben')
mc('pd4-mc-37', 'Wie sollte die <b>Reihenfolge der Aufgaben</b> laut Folie gestaltet sein?',
   ['*leichtere Aufgaben am Anfang (Kompetenzerleben)', '*hoch komplexe Aufgaben im Mittelteil', '*gegen Ende wieder leichtere Aufgaben (Ermüdung)', 'die schwersten Aufgaben ganz am Ende'],
   'Komplexe Aufgaben am Ende werden laut Lederer weniger in Angriff genommen.', 'Reihenfolge Aufgaben')
mc('pd4-mc-38', 'Was ist bei <b>Anforderungsniveau, Formulierung und Punktevergabe</b> richtig?',
   ['*Statt einer „Einserbremse“ besser mehrere anspruchsvolle Aufgaben stellen.', '*schlichtes Sprachniveau und Strukturierungshilfen verwenden', '*Jede Teilleistung gleich gewichten.', 'Für komplexere Aufgaben mehr Punkte vergeben.'],
   'Mehr Punkte für komplexere Aufgaben benachteiligen schwächere Schüler.', 'Einserbremse Formulierung Punkte')

# ---- Richtig/Falsch
tf('pd4-tf-01', 'Informelle Leistungstests werden von Lehrern nach festen Aufbaukriterien konzipiert.', True,
   'Informelle Tests: von Lehrern entwickelt, am Lehrstoff orientiert, meist für eine Klasse.', 'informelle Leistungstests')
tf('pd4-tf-02', 'Ausfragen und Kolloquien sind mündliche informelle Tests.', True,
   'Schriftlich: Exen, Proben, Aufsätze, Essays.', 'informelle Tests mündlich')
tf('pd4-tf-03', 'Informelle Tests sind zur Platzierung geeignet.', False,
   'Informelle Tests sind zur Platzierung ungeeignet, formelle geeignet.', 'Platzierung informell')
tf('pd4-tf-04', 'Formelle Schulleistungstests beziehen sich auf eine bestimmte, begrenzte Gruppe.', False,
   'Kein Bezug auf eine bestimmte und begrenzte Gruppe – das kennzeichnet informelle Tests.', 'formell Gruppe')
tf('pd4-tf-05', 'Informelle Tests liefern nur subjektive Aussagen bezogen auf Gruppe und Unterrichtssituation.', True,
   'Formelle Tests liefern objektive Aussagen über Wissen und Können.', 'informell subjektiv')
tf('pd4-tf-06', 'Die kriteriale Norm bei formellen Tests fragt dichotom, ob ein Leistungsziel erreicht wurde.', True,
   'Bei informellen Tests: Vergleich mit dem Inhalt des Curriculums.', 'kriteriale Norm dichotom')
tf('pd4-tf-07', 'Bei der Konstruktion formeller Tests kommt die Vorerprobung an wenigen Fällen nach der Testeichung.', False,
   'Vorerprobung ist Schritt 3, Testeichung Schritt 6.', 'Konstruktion Reihenfolge')
tf('pd4-tf-08', 'Bei der Vorerprobung wird vor allem die Verständlichkeit der Aufgabenformulierung überprüft.', True,
   'Schwierigkeit, Trennschärfe und erste Reliabilität folgen mit der ersten Stichprobe.', 'Vorerprobung')
tf('pd4-tf-09', 'Ein Nachteil formeller Schulleistungstests ist, dass sie häufig veraltet sind.', True,
   'Weitere Nachteile: negative Motivation, Erstarrung des Unterrichts, Verarmung der Lehrpläne, unfair bei mangelnder Lerngelegenheit.', 'Nachteile formell')
tf('pd4-tf-10', 'Lehrziele sind direkt beobachtbare Verhaltensweisen.', False,
   'Lehrziele sind hypothetische, nicht beobachtbare Konstrukte → Operationalisierung nötig.', 'Lehrziele Konstrukt')
tf('pd4-tf-11', 'In der Bloom-Taxonomie liegt die Synthese über der Analyse.', True,
   'Von unten: Wissen, Verstehen, Anwendung, Analyse, Synthese, Bewerten.', 'Bloom Synthese Analyse')
tf('pd4-tf-12', 'Überproportional viele mittelschwere Aufgaben sind ein Nachteil für leistungsschwache Schüler*innen.', True,
   'Gehört zum Grundsatz der proportionalen Abbildung.', 'mittelschwere Aufgaben')
tf('pd4-tf-13', 'Prüfungsformen sollten mit der Arbeitsform des vergangenen Unterrichts übereinstimmen.', True,
   'Prüfungsformen: schriftlich, mündlich, praktisch.', 'Prüfungsformen Arbeitsform')
tf('pd4-tf-14', 'Schriftliche Prüfungen gelten als rechtlich sicherer als mündliche.', True,
   'Außerdem einfach zu organisieren; Problemfall Extemporale.', 'schriftliche Prüfung')
tf('pd4-tf-15', 'Performanzaufgaben folgen dem Prinzip „Know how“ statt „Show how“.', False,
   'Umgekehrt: „Show how“ statt „Know how“ – tun, was man weiß (Ingenkamp & Lissmann, 2008).', 'Performanz Show how')
tf('pd4-tf-16', 'Bei Ergänzungsaufgaben gibt es feste Antwortkategorien.', False,
   'Ergänzungsaufgaben haben freie Antworten ohne feste Kategorien; Wahr-Falsch-Aufgaben haben feste Kategorien.', 'Ergänzungsaufgaben')
tf('pd4-tf-17', 'Mit offenen Aufgaben wird der Kenntnisstand eher überschätzt.', False,
   'Er wird unterschätzt, weil nur aktives, nicht passives Wissen überprüfbar ist.', 'offene Aufgaben Kenntnisstand')
tf('pd4-tf-18', 'Je mehr Aufgaben eine Prüfung hat, desto reliabler ist sie.', True,
   'Allerdings sind so oft nur schlichte Fakten abprüfbar → Mischung sinnvoll.', 'Prüfungsumfang Reliabilität')
tf('pd4-tf-19', 'Die lange, unstrukturierte Supermarkt-Textaufgabe auf der Folie ist ein Positivbeispiel für Aufgabenformulierung.', False,
   'Sie ist ein Negativbeispiel: ein einziger Fließtext ohne Hervorhebungen, Nummerierung oder Tabelle.', 'Supermarkt Negativbeispiel')
tf('pd4-tf-20', 'Die Reihenfolge der Aufgaben wird in der Regel den Schüler*innen überlassen.', True,
   'Laut Lederer (1998) halten trotzdem 80 % die gegebene Reihenfolge ein.', 'Reihenfolge freigestellt')

# ---- Lückentext (keine Zahlen, Formeln oder Symbole als Antwort)
gap('pd4-gap-01', 'Formelle Leistungstests werden von {{Expertengremien|Experten|Expertengremium|Experten(gremien)}} entwickelt.',
    'Beispiele: PISA, VERA, TIMSS.', 'formelle Leistungstests')
gap('pd4-gap-02', 'Die Erfüllung der {{Gütekriterien}} nimmt von formellen zu informellen Tests ab.',
    'Pfeil unter dem Klassifikationsschema.', 'Gütekriterien abnehmend')
gap('pd4-gap-03', 'Informelle Tests orientieren sich an der {{kriterialen}} Norm.',
    'Formelle: Sozialnorm oder kriteriale Norm.', 'informell kriteriale Norm')
gap('pd4-gap-04', 'Im zweiten Konstruktionsschritt beurteilen erfahrene Lehrkräfte die Aufgaben im {{ExpertInnenrating|Expertenrating|Expertinnenrating}}.',
    'Es werden 50–100 % mehr Aufgaben konstruiert als nötig.', 'ExpertInnenrating')
gap('pd4-gap-05', 'Lehrziele sind hypothetische Konstrukte; man muss festlegen, welches Verhalten Rückschlüsse zulässt. Das nennt man {{Operationalisierung}}.',
    'Lehrziele sind oft zu vage formuliert.', 'Operationalisierung')
gap('pd4-gap-06', 'Die höchste Stufe der Bloom-Taxonomie ist das {{Bewerten|Evaluation}}.',
    'Die niedrigste Stufe ist Wissen.', 'Bloom höchste Stufe')
gap('pd4-gap-07', 'Mündliche Prüfungen ermöglichen {{adaptives}} Testen.',
    'Außerdem mehr Tiefe durch Nachfragen und mehr Hilfestellung.', 'adaptives Testen')
gap('pd4-gap-08', 'Performanzaufgaben haben eine hohe {{ökologische|oekologische}} Validität.',
    'Ihre Auswertungsobjektivität ist dagegen gering.', 'ökologische Validität')
gap('pd4-gap-09', 'Bei Multiple-Choice-Aufgaben heißen die falschen Antwortalternativen {{Distraktoren|Distraktor}}.',
    'Die richtigen heißen Attraktoren.', 'Distraktoren')
gap('pd4-gap-10', 'Bei geschlossenen Aufgaben ist der {{Rateerfolg|Rate-Erfolg}} höher.',
    'Dafür sind sie schnell zu korrigieren und Leistungen besser vergleichbar.', 'Rateerfolg')
gap('pd4-gap-11', 'Eine einzelne, besonders schwere Aufgabe zur Bestimmung der Leistungsbesten nennt man {{Einserbremse}}.',
    'Unfair; besser mehrere anspruchsvolle Aufgaben.', 'Einserbremse')
gap('pd4-gap-12', 'Weil Nervosität das Sprachverständnis einschränkt, sollte man ein {{schlichtes|einfaches}} Sprachniveau wählen.',
    'Dazu Strukturierungshilfen wie Hervorhebungen, Nummerierungen, Grafiken.', 'Sprachniveau')
