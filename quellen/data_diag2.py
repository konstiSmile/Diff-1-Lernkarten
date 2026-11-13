# Psycho 2 · Diagnostische Psychologie · Teil 2 (Diagnostische Strategien, Messfehler, Gütekriterien)
# Quelle: Folien „2025 Diagnostik Teil 2 KURZ“ (45 Folien). Nur Inhalte aus den Folien.
# Klärungen von Konsti (13. Nov. 2026):
# - Folie 40 (Baum der Validität): genau wie auf der Folie übernehmen und auch so abfragen.
# - Folie 15 (Operationalisierung): Bedeutung von „Tagesform, Interesse, Vorbereitung“ unklar → nur beschreiben, nicht abfragen.
# - Folie 41 (Objektivität → Reliabilität → Validität): alle Pfeile auf der Karte, abgefragt wird nur die Grundidee.
# - Autoren/Jahreszahlen und Beispielwerte (r = .85/.55, M = 107,4/107,2) nur anzeigen (Karten, Erklärungen), nicht direkt abfragen.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

ST = 'Teil 2 · Diagnostische Strategien'
BN = 'Teil 2 · Bezugsnormen'
KT = 'Teil 2 · Klassische Testtheorie'
OB = 'Teil 2 · Objektivität'
RE = 'Teil 2 · Reliabilität'
VA = 'Teil 2 · Validität'

CARDS2 = [
    # ---------------------------------------------------------- Diagnostische Strategien
    C('strategien', ST, 'Welche <b>vier diagnostischen Strategien</b> werden unterschieden?',
      '<ol><li><b>Zeitpunkt</b> (Eingangs-, Verlaufsdiagnostik, Erfolgskontrolle)</li><li><b>Personenauswahl</b> (Selektion, Platzierung, Klassifikation)</li><li><b>Veränderung</b> (Modifikations- bzw. Förderdiagnostik)</li><li><b>Vergleichsmaßstab</b> (soziale, kriteriale/sachliche, individuelle Bezugsnorm)</li></ol>',
      'diagnostische Strategien Zeitpunkt Personenauswahl Veränderung Vergleichsmaßstab'),
    C('zeitpunkt', ST, 'Strategie <b>Zeitpunkt</b>: Was ist Eingangsdiagnostik, Verlaufsdiagnostik und Erfolgskontrolle?',
      '<b>Eingangsdiagnostik (Statusdiagnostik)</b><ul><li>Erfasst den <b>Ist-Zustand</b> zu einem bestimmten Zeitpunkt</li><li>Voraussetzung: <b>Merkmal ist stabil</b>, z. B. Vorliegen eines psychischen Problems; Erfassung von Eigenschaften</li></ul><b>Verlaufsdiagnostik (Prozessdiagnostik)</b><ul><li>Begleitet den (Interventions-)Prozess durch <b>mehrfache Messungen</b></li><li>Zeigt die <b>Entwicklung</b> einer Person an, z. B. Erfassung von Schulleistungen, Therapiefortschritt</li></ul><b>Erfolgskontrolle</b><ul><li><b>Vergleich mit Eingangsdiagnostik</b></li></ul>',
      'Zeitpunkt Eingangsdiagnostik Statusdiagnostik Verlaufsdiagnostik Prozessdiagnostik Erfolgskontrolle Ist-Zustand stabil mehrfache Messungen'),
    C('selektion', ST, 'Strategie <b>Personenauswahl</b>: Was ist <b>Selektionsdiagnostik</b>? Welche zwei Formen gibt es?',
      '<b>Suche nach Passung zwischen Person und Bedingung/en.</b><ul><li><b>Selektion von Personen:</b> Welche Person passt auf die Bedingung? z. B. <b>Stellenbesetzung</b></li><li><b>Selektion von Bedingungen:</b> Welche Bedingung passt auf die Person? z. B. <b>Berufswahl</b></li></ul>',
      'Selektionsdiagnostik Passung Selektion von Personen Selektion von Bedingungen Stellenbesetzung Berufswahl'),
    C('platzierung', ST, 'Was ist <b>Platzierung</b> und wie unterscheidet sie sich von der <b>Selektion</b>?',
      '<b>Platzierung:</b> Zuordnung einer Person zu bestimmten Leistungs- oder Berufsgruppen aufgrund <b>eines Merkmals</b> (z. B. <b>Übertrittszeugnis, 4. Kl.</b>).<br><br><b>Unterschied:</b><ul><li><b>Selektion:</b> 10 Plätze sind verfügbar – die <b>10 Passendsten</b> werden gesucht.</li><li><b>Platzierung:</b> <b>Alle</b> mit einer gesuchten Merkmalsausprägung erhalten einen Platz.</li></ul>',
      'Platzierung Übertrittszeugnis ein Merkmal Unterschied Selektion Plätze Passendsten Merkmalsausprägung'),
    C('klassifikation', ST, 'Was ist <b>Klassifikation</b> (Strategie Personenauswahl)?',
      'Personen werden <b>alternativen Anforderungsprofilen</b> zugeordnet. Anders als bei Selektionen wird bei der Klassifikation <b>für jede/n Bewerber/in eine individuell passende Zielgruppe</b> angeboten.<br><br>Beispiele: <b>Schultypen, Störungsbilder, Zensuren</b>',
      'Klassifikation alternative Anforderungsprofile individuell passende Zielgruppe Schultypen Störungsbilder Zensuren'),
    C('modifikation', ST, 'Strategie <b>Veränderung</b>: Was ist <b>Modifikations- bzw. Förderdiagnostik</b>?',
      'Diagnostik mit dem Ziel, <b>Personen oder Bedingungen zu verändern</b>, z. B. besonderer Förderbedarf, Einzelfallbetreuung, Praktika, Beschulung.<ul><li><b>Modifikation von Personen:</b> Was kann die Person tun, um zu „passen“? z. B. <b>Nachhilfeunterricht</b></li><li><b>Modifikation von Bedingungen:</b> Was kann durch Änderung der Bedingung für die Person erreicht werden? z. B. <b>Klassenwiederholung, Hochbegabtenklasse</b></li></ul>',
      'Veränderung Modifikationsdiagnostik Förderdiagnostik Modifikation von Personen Bedingungen Nachhilfe Klassenwiederholung Hochbegabtenklasse'),

    # ---------------------------------------------------------- Bezugsnormen
    C('sozial', BN, 'Strategie <b>Vergleichsmaßstab</b>: Was ist die <b>soziale Bezugsnorm</b>? Wann ist sie sinnvoll?',
      'Aussagen über Leistung werden aufgrund des <b>Vergleichs mit Leistungen einer für die jeweilige Altersstufe oder Schulart repräsentativen Stichprobe</b> getroffen.<ul><li><b>Sinnvoll, wenn über Selektion u. Ä. entschieden werden muss.</b> Dazu müssen die Einzelleistungen mit denen der gesamten Bezugsgruppe <b>objektiv, gültig und zuverlässig</b> verglichen werden.</li><li>Angewandt häufig bei <b>formellen Schulleistungstests (Jahrgangsstufentests)</b></li><li>Als Grundlage der Leistungsbeurteilung in der <b>normalen Lerngruppe</b> (Schulklasse, aber auch Jahrgang einer Schule) ist sie <b>pädagogisch und psychologisch problematisch</b>.</li></ul>',
      'soziale Bezugsnorm repräsentative Stichprobe Altersstufe Schulart Selektion Jahrgangsstufentests problematisch Leistungsbeurteilung'),
    C('sozial-vn', BN, '<b>Vor- und Nachteile</b> der <b>sozialen Bezugsnorm</b>?',
      '<b>Vorteile</b><ul><li>Leistungen werden <b>nicht nach einer starr linearen Verknüpfung zwischen Fehlerzahl und Note</b> (z. B. in Diktaten) beurteilt.</li><li>Die Beurteilung richtet sich nach der <b>Leistungsfähigkeit der Lerngruppe</b>.</li></ul><b>Nachteile</b><ul><li>Bezieht sich lediglich auf die einzelne Lerngruppe, <b>kein Vergleich mit anderen Lerngruppen</b>.</li><li>Macht <b>keine Aussagen, inwieweit die Lernziele erreicht</b> worden sind.</li><li>Kann sowohl <b>zu großzügig als auch zu streng</b> sein.</li><li><b>Lernfortschritte schwächerer Schüler</b> können nicht mit einer besseren Note gewürdigt werden, weil bei wirksamem Unterricht die durchschnittliche Leistung der Lerngruppe gleichfalls steigt.</li></ul>',
      'soziale Bezugsnorm Vorteile Nachteile Fehlerzahl Note Diktat Lerngruppe Lernziele großzügig streng Lernfortschritte schwächere Schüler'),
    C('klassenintern', BN, 'Was ist das <b>klasseninterne Bezugssystem</b> und welches Problem hat es?',
      '<ul><li>Die soziale Bezugsnorm orientiert sich an einer <b>repräsentativen Stichprobe</b>. Lehrkräfte haben aber <b>keine genauen Informationen über die durchschnittlichen Leistungen der Jahrgangsstufe</b> → Vergleichsmaßstab sind daher die <b>Ergebnisse der Schulklasse</b> (Baumert &amp; Watermann, 2000; Thiel &amp; Valentin, 2002).</li><li><b>Problem:</b> Die Note hängt nicht nur von der Leistung der Schüler*innen ab, sondern <b>auch vom Leistungsniveau der Klasse</b> → Schulnoten daher <b>nicht vergleichbar</b> (Trautwein, 2007).</li><li>Solche Noten sind deshalb <b>nicht zur Selektion oder Platzierung geeignet</b>.</li></ul><b>Studie Milek et al. (2009):</b> <b>Negativer Zusammenhang</b> zwischen <b>mittlerem Leistungsniveau einer Klasse</b> und der <b>Schulempfehlung</b>.',
      'klasseninternes Bezugssystem soziale Bezugsnorm Schulklasse Leistungsniveau Noten nicht vergleichbar Selektion Platzierung Milek Schulempfehlung negativer Zusammenhang Trautwein Baumert Watermann Thiel Valentin'),
    C('kriterial', BN, 'Was ist die <b>kriteriale / sachliche Bezugsnorm</b>? Welche anderen Namen hat sie?',
      'Aussagen über Leistung werden <b>direkt in Bezug auf einen definierten Leistungsstandard</b> interpretiert.<ul><li>Die Norm bezieht sich auf die <b>Sache</b> – daher die Bezeichnung <b>sachliche Bezugsnorm</b> (Ingenkamp, 1985).</li><li>Weil sie <b>reale Leistungen mit idealen Leistungen</b> (der optimalen Erreichung von Lernzielen) vergleicht, heißt sie auch <b>Idealnorm</b> (Gaude, 1989).</li><li>Andere Autoren sprechen von <b>kriterienbezogener Norm</b>.</li><li>Der Vergleich mit anderen Schülern interessiert hier <b>höchstens am Rande</b>; entscheidend ist der <b>Grad, in dem ein Lernziel erreicht</b> worden ist.</li></ul>',
      'kriteriale sachliche Bezugsnorm Leistungsstandard Idealnorm kriterienbezogene Norm Lernziel Ingenkamp Gaude Sache'),
    C('kriterial-vn', BN, '<b>Vor- und Nachteile</b> der <b>kriterialen / sachlichen Bezugsnorm</b>?',
      '<b>Vorteile</b><ul><li>Informiert über die <b>Ergebnisse des Lernens</b>, also über erreichte Kompetenzen oder noch bestehende Lücken.</li><li><b>Lernfortschritte schwächerer Schüler werden erkannt</b> und dadurch deren <b>Motivation gefördert</b>.</li><li>Macht die <b>Anforderungen für Schüler und Eltern eindeutig und durchsichtig</b>.</li></ul><b>Nachteile</b><ul><li>Die Bestimmung der Lernziele ist eng mit dem <b>Problem der Standards</b> verknüpft: Für den einzelnen Lehrer ist es nicht einfach, zwischen zu hohen und zu niedrigen Anforderungen ein angemessenes Niveau zu finden. Die Verführung ist beträchtlich, die <b>Anforderungen zu niedrig</b> anzusetzen.</li></ul>',
      'kriteriale sachliche Bezugsnorm Vorteile Nachteile Kompetenzen Lücken Motivation Anforderungen durchsichtig Standards zu niedrig'),
    C('individuell', BN, 'Was ist die <b>individuelle Bezugsnorm</b>? Vor- und Nachteile?',
      'Aussagen über Leistung werden durch einen <b>Vergleich mit den früheren Lernergebnissen des Individuums</b> getroffen.<br><br><b>Vorteil</b><ul><li>Entspricht am besten dem Wunsch, die <b>Leistungen des einzelnen Schülers zu würdigen</b> und ihn so wirksam zu <b>fördern</b>.</li></ul><b>Nachteile</b><ul><li>Kann durch unterschiedliche Maßstäbe mit dem <b>Gleichheitsgrundsatz</b> in Konflikt geraten (er gebietet, alle Leistungen nach demselben Maßstab zu bewerten).</li><li>Die <b>Bindung an einen vorgegebenen Standard</b>, aber auch an konkrete Lernziele, kann aus falsch verstandener Rücksicht auf das Individuum leicht <b>vernachlässigt</b> werden.</li></ul>',
      'individuelle Bezugsnorm frühere Lernergebnisse würdigen fördern Gleichheitsgrundsatz Standard Lernziele vernachlässigt'),
    C('bezugsnormen-grafik', BN, 'Abbildung „Vergleichsperspektiven bei drei Bezugsnormen“: Was zeigen ①, ② und ③?',
      'Achsen: <b>Lernzeit</b> (x) und <b>Kenntnisse/Fertigkeiten</b> (y). <b>A, B, C</b> = Schüler mit <b>unterschiedlichem Lerntempo</b> (drei ansteigende Kurven, A am höchsten).<ul><li><b>① individuelle Bezugsnorm:</b> Pfeil <b>entlang einer Kurve</b> (Schüler C früher ↔ später) – Vergleich mit sich selbst über die Lernzeit</li><li><b>② soziale Bezugsnorm:</b> senkrechter Pfeil <b>zwischen den Kurven</b> zum selben Zeitpunkt – Vergleich der Schüler untereinander</li><li><b>③ sachliche Bezugsnorm:</b> senkrechte Pfeile von einer <b>festen Markierung</b> (Standard) aus – Vergleich mit einem festgelegten Leistungsstand</li></ul>',
      'Abbildung Vergleichsperspektiven Bezugsnormen Lernzeit Kenntnisse Fertigkeiten Lerntempo individuell sozial sachlich'),

    # ---------------------------------------------------------- Klassische Testtheorie
    C('guetekriterien', KT, 'Was ist das <b>Ziel jeder Testung</b>? Welche <b>Gütekriterien</b> und <b>Nebengütekriterien</b> gibt es?',
      '<b>Ziel jeder Testung:</b> Dem <b>wahren Wert so nah wie möglich</b> kommen und den <b>Messfehler so gering wie möglich</b> halten.<br><br><b>Gütekriterien</b><ul><li>Objektivität</li><li>Reliabilität</li><li>Validität</li></ul><b>Nebengütekriterien</b><ul><li>Umfang der Normierungen</li><li>Testfairness</li><li>Vergleichbarkeit mit anderen Tests</li><li>(Ökonomische) Nützlichkeit des Tests</li><li>Spezifische Nützlichkeit</li></ul>',
      'Ziel jeder Testung wahrer Wert Messfehler Gütekriterien Objektivität Reliabilität Validität Nebengütekriterien Normierung Testfairness Vergleichbarkeit Nützlichkeit'),
    C('ktt', KT, 'Womit beschäftigt sich die <b>Testtheorie</b>? Welche Bedeutung hat die <b>Klassische Testtheorie</b>?',
      '<ul><li>Die Testtheorie beschäftigt sich mit dem <b>Zusammenhang zwischen dem Testverhalten und dem mit dem Test zu erfassenden psychischen Merkmal</b>.</li><li>Die <b>Klassische Testtheorie (KTT)</b> ist die Grundlage für die Konstruktion und Interpretation von <b>95 % aller psychologischen Testverfahren</b> (Rost, 1999).</li></ul>',
      'Testtheorie Testverhalten psychisches Merkmal Klassische Testtheorie KTT 95 Prozent Rost'),
    C('operationalisierung', KT, 'Was versteht man unter <b>Operationalisierung</b>?',
      '<b>Standardisierung eines Konstrukts</b> durch Angabe des <b>Verhaltens</b>, das zur Erfassung des Konstrukts notwendig ist oder das die Ausprägung des Konstrukts anzeigt (<b>Indikatoren</b>).<br><br>Abbildung auf der Folie: <b>Rechenfähigkeit</b> → <b>Mathetest</b> (mit <b>Punktzahl</b>); von der anderen Seite zeigt ein Pfeil von <b>Tagesform, Interesse, Vorbereitung</b> ebenfalls auf den Mathetest. (Auf der Folie nicht weiter erklärt.)',
      'Operationalisierung Standardisierung Konstrukt Verhalten Indikatoren Rechenfähigkeit Mathetest Punktzahl'),
    C('axiom1', KT, 'Was besagt das <b>1. Axiom der KTT</b>? Was sind wahrer Wert und Messfehler?',
      'Beobachtete (Test-)Werte <b>(X)</b> setzen sich immer aus zwei Komponenten zusammen: aus dem <b>„wahren Wert“</b> der Ausprägung des untersuchten Merkmals <b>W(T)</b> und einem <b>zufällig verteilten Messfehler (e)</b>:<br><br><b>X = W(T) + e</b><ul><li><b>Wahrer Wert (W):</b> Wert, den man in einer <b>perfekten, absolut fehlerfreien Messung</b> erhalten würde, z. B. wahre Intelligenz.</li><li><b>Messfehler (e):</b> repräsentiert alle <b>unkontrollierten und unsystematischen Störeinflüsse</b> bei der Messung, z. B. Tagesform, Motivation, Testbedingungen.</li></ul>Beide sind <b>nicht messbar, nur schätzbar!</b>',
      '1. Axiom KTT X = W(T) + e wahrer Wert Messfehler zufällig unsystematisch Störeinflüsse nicht messbar schätzbar'),
    C('messfehler', KT, 'Was ist ein <b>Messfehler</b> und <b>wie entstehen</b> Messfehler?',
      '<b>Was ist ein Messfehler?</b><ul><li>Testwerte sind fehlerhaft. Beispiel: IQ laut Testwert = 130, IQ laut wahrem Wert = ?</li><li><b>Differenz zwischen Testwert und wahrem Wert = Messfehler</b></li></ul><b>Wie entstehen Messfehler?</b> Durch Fehler …<ul><li><b>bei der Testkonstruktion:</b> mehrdeutige Items, missverständliche Instruktion</li><li><b>bei der Durchführung:</b> Testsituation, Person (Motivation, Wachheit)</li><li><b>bei der Auswertung des Tests:</b> Interpretation der Antworten, Zusammenzählen von Punkten</li></ul>',
      'Messfehler Differenz Testwert wahrer Wert Entstehung Testkonstruktion mehrdeutige Items Instruktion Durchführung Testsituation Motivation Wachheit Auswertung Punkte'),
    C('axiom2', KT, 'Was besagt das <b>2. Axiom der KTT</b>?',
      'Die Varianz der Messung eines Merkmals bei einer Person ist <b>Fehlervarianz</b> des Messfehlers: <b>Die Messung variiert um den wahren Wert.</b><ul><li>⇒ Der (erwartete) <b>Mittelwert (E) des Fehlers (e) ist Null</b>.</li><li>⇒ Die <b>Korrelation zwischen Testwert und Messfehler ist ebenfalls Null</b>.</li></ul>Abbildung: IQ eines Kindes zu T1–T4; die Balken liegen mal über (Messfehler positiv), mal unter (Messfehler negativ) dem <b>mutmaßlichen wahren Wert</b> (gestrichelte Linie).',
      '2. Axiom KTT Fehlervarianz variiert um wahren Wert Mittelwert Fehler Null Korrelation Testwert Messfehler Null positiv negativ'),
    C('axiom3', KT, 'Was besagt das <b>3. Axiom der KTT</b>? Welche Folgerung steht auf der Folie?',
      'Die <b>Messfehler bei unterschiedlichen Personen i und j sind unkorreliert</b>.<br><br>Abbildung: IQ von Kind i und Kind j zu T1–T4, die Abweichungen vom jeweiligen wahren Wert hängen nicht zusammen.<br><br><b>Je häufiger man misst, desto mehr nähert man sich dem wahren Wert.</b>',
      '3. Axiom KTT Messfehler Personen unkorreliert häufiger messen wahrer Wert'),

    # ---------------------------------------------------------- Objektivität
    C('objektivitaet', OB, 'Was ist <b>Objektivität</b>? Welches Beispiel zeigt die Folie?',
      'Objektivität ist ein Maß dafür, inwieweit die Ergebnisse einer Testung <b>unabhängig von der Person des Testleiters und des Auswerters</b> sind.<br><br>Beispiel: Rechenfähigkeit → Matheprüfung mit <b>30 von 40 Punkten</b>.<ul><li><b>Hohe Objektivität:</b> Lehrer A, B und C geben alle Note 2.</li><li><b>Geringe Objektivität:</b> Lehrer A = Note 2, Lehrer B = Note 4, Lehrer C = Note 3.</li></ul>Drei Arten: <b>Durchführungs-, Auswertungs- und Interpretationsobjektivität</b>.',
      'Objektivität unabhängig Testleiter Auswerter 30 von 40 Punkten Lehrer Note Durchführung Auswertung Interpretation'),
    C('durchfuehrung', OB, 'Was ist <b>Durchführungsobjektivität</b>? Beispiele, Beeinträchtigung, Verbesserung?',
      'Maß dafür, inwieweit die Ergebnisse eines Tests <b>von der Person des Versuchsleiters unabhängig</b> sind. Für alle Getesteten gelten die <b>gleichen Anforderungen unter den gleichen Bedingungen</b>.<br><br>Verletzt z. B. bei:<ul><li>Lehrer A: Taschenrechner erlaubt, Lehrer B: Taschenrechner verboten</li><li>Lehrer A nuschelt, Lehrer B spricht deutlich</li><li>Klassenraum A laut, Klassenraum B leise</li></ul><b>Beeinträchtigung:</b> <b>soziale Interaktionen</b> zwischen Testperson und Testleiter<br><b>Verbesserung:</b> <b>maximale Standardisierung</b> der Testsituation (Material, Situation, Testanweisung usw.)',
      'Durchführungsobjektivität Versuchsleiter gleiche Bedingungen Taschenrechner nuscheln laut leise soziale Interaktion Standardisierung'),
    C('auswertung', OB, 'Was ist <b>Auswertungsobjektivität</b>? Beispiel, Beeinträchtigung, Verbesserung?',
      'Maß dafür, inwieweit <b>gleiches Verhalten von Testpersonen stets auf die gleiche Weise ausgewertet</b> wird.<br><br>Beispiel: Lehrer A wertet Rechtschreibfehler, Lehrer B wertet Rechtschreibfehler nicht.<br><br><b>Beeinträchtigung:</b> Auswertung <b>offener Antworten</b>, die eine inhaltliche Klassifikation erfordern (z. B. mündliche Prüfungen); Fehler bei der <b>Punktevergabe</b> (Konzentration, Unsicherheit); Fehler beim <b>Addieren</b> der Punkte<br><b>Verbesserung:</b> <b>gebundene Antworten</b> (z. B. Kreuze auf Skalen), <b>Scanner-Auswertung</b> oder <b>computergestützte Auswertung</b>',
      'Auswertungsobjektivität gleiches Verhalten gleich ausgewertet Rechtschreibfehler offene Antworten mündliche Prüfung Punktevergabe Addieren gebundene Antworten Scanner computergestützt'),
    C('interpretation', OB, 'Was ist <b>Interpretationsobjektivität</b>? Beispiel, Beeinträchtigung, Verbesserung?',
      'Maß dafür, inwieweit die Ergebnisse eines Tests von den <b>interpretativen Schlüssen</b> abhängen, die ein Diagnostiker vornimmt. Hohe Interpretationsobjektivität besteht, wenn <b>verschiedene Diagnostiker gewonnene Befunde in gleicher Weise interpretieren</b>.<br><br>Beispiel: 30 von 40 Punkten im Mathetest → Lehrer A = Note 2, Lehrer B = Note 4, Lehrer C = Note 3.<br><br><b>Beeinträchtigung:</b> wenn <b>Intuition und Erfahrung</b> des Testleiters einen Schluss begründen<br><b>Verbesserung:</b> wenn aus den Punktwerten auf die <b>individuelle Position auf einer Merkmalsdimension</b> geschlossen wird',
      'Interpretationsobjektivität interpretative Schlüsse Diagnostiker gleiche Interpretation Intuition Erfahrung Merkmalsdimension Punktwerte'),

    # ---------------------------------------------------------- Reliabilität
    C('reliabilitaet', RE, 'Was ist <b>Reliabilität</b>? Welche Werte können Reliabilitätskoeffizienten annehmen?',
      '<b>Reliabilität (Zuverlässigkeit): Messfehler charakterisieren</b><ul><li>Reliabilität ist ein <b>korrelatives Maß für die Genauigkeit</b>, mit der ein Test ein Merkmal erfasst. Um sich dem wahren Wert so weit wie möglich zu nähern, muss man den Messfehler <b>so klein wie möglich halten</b> und <b>seine Grenzen angeben</b> können.</li><li>Reliabilitätskoeffizienten (r) liegen <b>zwischen 0 und +1</b>:<ul><li>r = 1 → <b>kein Messfehler</b> (keine Schwankungen der Testwerte)</li><li>r = 0 → <b>riesiger Messfehler</b> (Test erfasst überhaupt nichts Stabiles)</li><li><b>r &gt; .7</b> → <b>ausreichende Reliabilität</b> eines Tests</li></ul></li><li><b>Reliabilität kann nur geschätzt, nicht gemessen werden.</b></li></ul>',
      'Reliabilität Zuverlässigkeit korrelatives Maß Genauigkeit Messfehler Koeffizient 0 bis 1 .7 ausreichend geschätzt nicht gemessen'),
    C('retest', RE, 'Was ist <b>Retestreliabilität</b>? Welche Probleme hat sie?',
      '<ul><li>Man legt einen Test <b>zu zwei Zeitpunkten derselben Gruppe</b> von Personen vor und schätzt aus der <b>Korrelation der Testwerte</b> die Reliabilität.</li><li>Die Retest-Reliabilität gibt einen Hinweis auf die <b>Stabilität des untersuchten Merkmals (Traits)</b>.</li></ul>Beispiele auf den Folien (IQ zu T1 und T2): r = .85 = hohe Retestreliabilität; r = .55 = geringe Retestreliabilität – obwohl die Mittelwerte fast gleich sind (M = 107,4 und M = 107,2).<br><br><b>Probleme:</b> <b>Gedächtniseffekte</b>, <b>Instabilität des Merkmals</b>, <b>lange Zeiträume</b> zwischen den Testungen.',
      'Retestreliabilität zwei Zeitpunkte dieselbe Gruppe Korrelation Stabilität Trait Probleme Gedächtniseffekte Instabilität lange Zeiträume'),
    C('retest-effekte', RE, 'Wann wird die <b>Retestreliabilität</b> durch Veränderungen zwischen T1 und T2 gemindert – und wann nicht?',
      '<ul><li>Sie wird <b>nicht</b> durch Veränderungen beeinflusst, die <b>alle Personen betreffen</b>. Wenn z. B. alle Testpersonen bei der zweiten Durchführung <b>zehn Punkte mehr</b> erreichen, weil sie sich an einige Lösungen erinnern, wird die Reliabilität dadurch <b>nicht gemindert</b>.</li><li>Sie <b>verringert sich nur</b>, wenn die Effekte <b>interindividuell unterschiedlich groß</b> ausfallen, also einige Personen große Erinnerungseffekte zeigen und andere kleine.</li></ul>Abbildung: oben liegen alle T2-Punkte gleichmäßig über T1; unten unterschiedlich weit.',
      'Retestreliabilität Veränderung alle Personen zehn Punkte mehr nicht gemindert interindividuell unterschiedlich Erinnerungseffekte'),
    C('parallel', RE, 'Was ist <b>Paralleltestreliabilität</b>? Vorteil und Probleme?',
      'Der <b>Königsweg</b> zur Schätzung der Reliabilität: Man konstruiert <b>zwei äquivalente Formen A und B</b> (Mittelwert und Varianz gleich, Korrelation der Werte nahe r = 1) und legt sie <b>zeitgleich derselben Gruppe</b> vor.<br><br>→ <b>Übungs- oder Gedächtniseffekte werden vermieden.</b><br><br><b>Probleme</b><ul><li>Konstruktion paralleler Tests <b>sehr aufwendig</b>, wird nur selten gemacht.</li><li>Nicht für alle Bereiche äquivalente Testformen möglich (z. B. <b>Kreativitätstests</b>).</li></ul>',
      'Paralleltestreliabilität Königsweg äquivalente Formen A B Mittelwert Varianz zeitgleich Übungseffekte Gedächtniseffekte aufwendig Kreativitätstests'),
    C('splithalf', RE, 'Was ist <b>Split-Half-Reliabilität</b>? Methoden und Probleme?',
      'Test <b>nachträglich in zwei äquivalente Hälften teilen</b> und die Items beider Hälften miteinander korrelieren.<br><br><b>Methoden</b><ul><li>Trennung in gerad- und ungeradzahlige Items (<b>Odd-even-Methode</b>)</li><li>Trennung in <b>erste und zweite Testhälfte</b> (problematisch bei <b>nachlassender Aufmerksamkeit</b> oder <b>ansteigender Schwierigkeit</b>)</li><li>Wichtig: Bildung von <b>Item-Paarlingen mit annähernd gleicher Schwierigkeit</b></li></ul><b>Probleme:</b> Erstellung identischer Hälften',
      'Split-Half-Reliabilität Testhälften Odd-even gerade ungerade erste zweite Hälfte Aufmerksamkeit Schwierigkeit Item-Paarlinge identische Hälften'),

    # ---------------------------------------------------------- Validität
    C('validitaet', VA, 'Was bezeichnet <b>Validität (Gültigkeit)</b>?',
      'Validität bezeichnet die <b>inhaltliche Übereinstimmung einer empirischen Messung mit einem logischen Messkonzept</b>. Allgemein ist dies der <b>Grad an Genauigkeit, mit der dasjenige Merkmal tatsächlich gemessen wird, das gemessen werden soll</b>.',
      'Validität Gültigkeit Übereinstimmung empirische Messung logisches Messkonzept Merkmal gemessen werden soll'),
    C('inhalt', VA, 'Was ist <b>inhaltliche Validität</b> (Augenscheinvalidität, Face Validity)? Methode und Problem?',
      'Bilden die Items eine <b>repräsentative Stichprobe aus dem zu erfassenden Merkmalsbereich</b>, kann die Validität mittels eines <b>Repräsentationsschlusses</b> ermittelt werden (z. B. <b>Englisch-Vokabeln</b> zur Erfassung des Merkmals Englischkenntnisse).<br><br><b>Methode:</b> Bewertung durch <b>Expertenurteil</b><br><b>Problematisch:</b> Es gibt <b>keine empirische Überprüfungsmöglichkeit</b>.<br><br>Abbildung: Aus einer Liste englischer Obst- und Gemüsewörter (Potato, Apple, Lemon …) werden einige (Apple, Banana, Leek, Carrot) für den Test gezogen.',
      'inhaltliche Validität Inhaltsvalidität Augenscheinvalidität Face Validity repräsentative Stichprobe Repräsentationsschluss Englisch-Vokabeln Expertenurteil keine empirische Überprüfung'),
    C('empirisch', VA, 'Was sind <b>konvergente</b> und <b>diskriminante Validität</b> (empirische Validität)?',
      '<ul><li><b>Konvergente Validität:</b> Testdaten, die <b>dasselbe Merkmal</b> abbilden sollen, sollen <b>hoch</b> miteinander korrelieren.</li><li><b>Diskriminante Validität:</b> Testdaten, die <b>verschiedene Merkmale</b> abbilden sollen, sollen <b>gering</b> miteinander korrelieren.</li></ul>Beispiel: Alter Mathetest und neuer Mathetest (beide Rechenleistung) → hoch korrelieren (konvergent). Neuer Mathetest und Sportnote (Sportlichkeit) → gering korrelieren (diskriminant).',
      'empirische Validität konvergente diskriminante Validität dasselbe Merkmal hoch verschiedene Merkmale gering Mathetest Sportnote'),
    C('kriterium', VA, 'Was ist <b>Kriteriumsvalidität</b>? Wovon hängt die Höhe der Korrelation ab?',
      'Wenn ein <b>messbares Kriterium</b> vorliegt, kann man die Validität aus der <b>Korrelation zwischen Testwerten und Kriteriumswerten</b> schätzen (Beispiel: <b>Schulnoten als Kriterium für Intelligenz</b>).<br><br>Diese Korrelation kann <b>zwischen −1 und +1</b> liegen.<br><br>Die Höhe der Korrelation hängt ab von:<ul><li>der <b>Reliabilität des Tests</b></li><li>der <b>Reliabilität des Kriteriums</b></li><li>den <b>inhaltlichen Gemeinsamkeiten</b> von Test und Kriterium</li></ul>',
      'Kriteriumsvalidität messbares Kriterium Korrelation Testwert Kriteriumswert Schulnoten Intelligenz -1 +1 Reliabilität Test Kriterium Gemeinsamkeiten'),
    C('kriterium-arten', VA, 'Kriteriumsvalidität: Was sind <b>innere</b>, <b>äußere</b>, <b>konkurrente</b> und <b>prädiktive</b> Validität?',
      '<ul><li><b>Innere Validität:</b> Kriterium ist ein <b>anderer (alter) Test, der das Gleiche misst</b>.</li><li><b>Äußere Validität:</b> Kriterium ist ein anderer Test, der <b>ein Merkmal erfasst, das hoch korreliert</b>, z. B. IQ und Noten.</li><li><b>Konkurrente Validität:</b> Messung und Erhebung des Kriteriums (z. B. ein anderer Test) werden <b>zeitgleich</b> durchgeführt.</li><li><b>Prädiktive Validität:</b> Kriterium ist ein <b>in der Zukunft liegender Verhaltensaspekt</b>, z. B. Übertrittszeugnis → Gymnasialeignung.</li></ul>Die Pfeile auf der Folie kreuzen sich: <b>Innere wie äußere</b> Validität können jeweils <b>konkurrent oder prädiktiv</b> sein.',
      'Kriteriumsvalidität innere äußere konkurrente prädiktive Validität alter Test zeitgleich Zukunft Übertrittszeugnis Gymnasialeignung IQ Noten'),
    C('konstrukt', VA, 'Was ist ein <b>Konstrukt</b>?',
      'Ein <b>nicht empirisch erkennbarer Sachverhalt</b> innerhalb einer wissenschaftlichen Theorie. Konstrukte sind somit <b>gedanklicher bzw. theoretischer Natur</b> (Begriffe wie „Intelligenz“, „Angst“, „Introversion“).<br><br>Das bedeutet nicht, dass der Sachverhalt nicht „existiert“, sondern nur, dass er <b>aus anderen, messbaren Sachverhalten (Indikatoren) erschlossen</b> wird = <b>latente Konstrukte</b>.',
      'Konstrukt nicht empirisch erkennbar theoretisch Intelligenz Angst Introversion Indikatoren erschlossen latent'),
    C('pruefungsangst', VA, 'Beispiel Konstrukt <b>Prüfungsangst</b>: Welche Beobachtungen auf welchen Ebenen?',
      '<ul><li><b>Verhalten:</b> Vermeidung, sich abwenden</li><li><b>Physiologie:</b> Zittern, Herzrasen, Schweißausbruch</li><li><b>Kognition:</b> negativ („Das schaffe ich nie“, „Ich werde eine 6 schreiben“, „Die anderen sind viel besser als ich“ …)</li><li><b>Emotion:</b> Angst</li></ul>→ <b>Konstrukt: Prüfungsangst</b>',
      'Prüfungsangst Konstrukt Verhalten Vermeidung Physiologie Zittern Herzrasen Kognition negativ Emotion Angst'),
    C('konstruktvaliditaet', VA, 'Was ist <b>Konstruktvalidität</b>? Wie validiert man einen Prüfungsangst-Test?',
      '<ul><li>Tests stellen die <b>Operationalisierungsversuche von Konstrukten</b> dar.</li><li>Ein Test soll <b>hoch</b> mit Kriterien korrelieren, die nach der Theorie <b>mit dem Konstrukt verbunden</b> sind (<b>konvergente Validität</b>).</li><li>Ein Test soll <b>niedrig</b> mit Kriterien korrelieren, die nach der Theorie <b>nicht mit dem Konstrukt verbunden</b> sind (<b>diskriminante Validität</b>).</li></ul><b>Validierung Prüfungsangst-Test:</b><ul><li>hoch korrelieren mit: Angst, Zittern, Fluchtgedanken etc.</li><li>niedrig korrelieren mit: Entspannung, Freude, positiven Kognitionen („Das kriege ich hin, ich habe gut gelernt“, „Ich werde sicher eine 2 schreiben.“)</li></ul>',
      'Konstruktvalidität Operationalisierung hoch konvergent niedrig diskriminant Prüfungsangst Validierung Entspannung Freude'),
    C('baum', VA, 'Wie ist der <b>Baum der Validität</b> auf der Folie aufgebaut?',
      '<b>Validität</b><ul><li><b>Inhaltsvalidität</b> (Augenscheinvalidität)</li><li><b>Empirische Validität</b><ul><li><b>Konvergente Validität</b><ul><li><b>Konstruktvalidität</b></li><li><b>Kriteriumsvalidität</b><ul><li><b>Innere Validität</b> → konkurrent und prädiktiv</li><li><b>Äußere Validität</b> → konkurrent und prädiktiv</li></ul></li></ul></li><li><b>Diskriminante Validität</b></li></ul></li></ul>Unterste Ebene: <b>Konkurrente Validität</b> und <b>Prädiktive Validität</b> (sich kreuzende Pfeile von innerer und äußerer Validität).',
      'Baum Validität Inhaltsvalidität empirische konvergente diskriminante Konstruktvalidität Kriteriumsvalidität innere äußere konkurrente prädiktive Übersicht'),
    C('beziehung-orv', VA, '<b>Beziehung von Objektivität, Reliabilität und Validität</b>: Was zeigt die Abbildung?',
      'Drei Ebenen von oben nach unten: <b>Objektivität → Reliabilität → Validität</b>.<ul><li><b>Interpretationsobjektivität</b> → direkt auf die <b>Validität</b></li><li><b>Durchführungsobjektivität</b> → auf die <b>Reliabilität</b> und auf die <b>Retest- und Paralleltestreliabilität</b></li><li><b>Auswertungsobjektivität</b> → auf die <b>interne Konsistenz</b> und auf die <b>Retest- und Paralleltestreliabilität</b></li><li><b>Reliabilität</b> → <b>Validität</b></li></ul>',
      'Beziehung Objektivität Reliabilität Validität Interpretationsobjektivität Durchführungsobjektivität Auswertungsobjektivität interne Konsistenz Retest Paralleltest'),
    C('beziehung-vr', VA, '<b>Beziehung von Validität und Reliabilität</b>: Was gilt nach der KTT?',
      '<ul><li>Ein Test, der <b>nicht reliabel</b> ist, kann <b>auch nicht valide</b> sein.</li><li>Ein <b>reliabler Test kann aber nicht valide</b> sein – er erfasst etwas genau, nur <b>nicht das, was man erfassen möchte</b>.</li><li>Schätzungen der Reliabilität und Bestimmung der Validität sind <b>zwei unabhängige Prozeduren</b>!</li></ul>Bildbeispiel: Ein <b>Lineal</b> misst die <b>Länge</b> eines Briefes (✓), aber nicht sein <b>Gewicht</b> (✗); das Gewicht misst die <b>Waage</b> (✓).',
      'Beziehung Validität Reliabilität nicht reliabel nicht valide reliabel aber nicht valide unabhängige Prozeduren Lineal Länge Gewicht Waage'),
    C('probleme', VA, 'Welche <b>Probleme der Validität</b> in der klassischen Testtheorie gibt es?',
      '<ul><li>Wenn schon ein <b>valides Instrument vorliegt, wozu dann ein zweites</b>? Oder: Wenn <b>keines vorliegt</b>, wie will man dann die Validität berechnen?</li><li><b>Niedrige Korrelation</b> zwischen Test und Kriterium durch <b>Konfundierung mit anderen Variablen</b>.</li><li><b>Prädiktive Validität</b> (z. B. gute Staatsexamensnote = guter Lehrer) meist <b>nicht möglich, wenn der Zeitraum zu groß</b> ist – relevante Eigenschaften werden vielleicht <b>erst später erworben</b>.</li></ul>',
      'Probleme Validität klassische Testtheorie valides Instrument zweites Konfundierung prädiktiv Staatsexamensnote Zeitraum später erworben'),
]

CARDS2 = {'d2': CARDS2}

# ---------------------------------------------------------------- Tests Teil 2
ITEMS2 = []
S = 'Diagnostik · Teil 2'
def add(**k): ITEMS2.append(dict(k, src=S))

# Multiple Choice
add(id='pd2-mc-01', type='mc', q='Welche Diagnostik erfasst den <b>Ist-Zustand zu einem bestimmten Zeitpunkt</b> und setzt ein <b>stabiles Merkmal</b> voraus?',
    options=['Verlaufsdiagnostik (Prozessdiagnostik)', 'Eingangsdiagnostik (Statusdiagnostik)', 'Erfolgskontrolle', 'Förderdiagnostik'], correct=1,
    expl='Verlaufsdiagnostik begleitet den Prozess durch mehrfache Messungen; Erfolgskontrolle = Vergleich mit der Eingangsdiagnostik.', kw='Eingangsdiagnostik Statusdiagnostik')
add(id='pd2-mc-02', type='mc', q='Die Erfassung des <b>Therapiefortschritts</b> durch mehrfache Messungen ist ein Beispiel für …',
    options=['Statusdiagnostik', 'Selektionsdiagnostik', 'Prozessdiagnostik', 'Klassifikation'], correct=2,
    expl='Verlaufs-/Prozessdiagnostik zeigt die Entwicklung einer Person an, z. B. Schulleistungen, Therapiefortschritt.', kw='Verlaufsdiagnostik Prozessdiagnostik')
add(id='pd2-mc-03', type='mc', q='Was ist die <b>Erfolgskontrolle</b>?',
    options=['Vergleich mit der Eingangsdiagnostik', 'Vergleich mit einer repräsentativen Stichprobe', 'Einmalige Messung am Ende', 'Vergleich mit einem Paralleltest'], correct=0,
    expl='Strategie Zeitpunkt: Erfolgskontrolle = Vergleich mit Eingangsdiagnostik.', kw='Erfolgskontrolle')
add(id='pd2-mc-04', type='mc', q='Die <b>Berufswahl</b> ist ein Beispiel für …',
    options=['Selektion von Personen', 'Selektion von Bedingungen', 'Platzierung', 'Modifikation von Bedingungen'], correct=1,
    expl='Selektion von Bedingungen: Welche Bedingung passt auf die Person? Selektion von Personen wäre z. B. Stellenbesetzung.', kw='Selektion von Bedingungen Berufswahl')
add(id='pd2-mc-05', type='mc', q='<b>Alle</b> Personen mit einer gesuchten Merkmalsausprägung erhalten einen Platz. Das ist …',
    options=['Selektion', 'Platzierung', 'Klassifikation', 'Modifikation'], correct=1,
    expl='Bei der Selektion sind z. B. 10 Plätze verfügbar und die 10 Passendsten werden gesucht.', kw='Platzierung Unterschied Selektion')
add(id='pd2-mc-06', type='mc', q='Das <b>Übertrittszeugnis in der 4. Klasse</b> ist laut Folie ein Beispiel für …',
    options=['Platzierung', 'Klassifikation', 'Selektion von Personen', 'Erfolgskontrolle'], correct=0,
    expl='Platzierung: Zuordnung zu Leistungs- oder Berufsgruppen aufgrund eines Merkmals.', kw='Platzierung Übertrittszeugnis')
add(id='pd2-mc-07', type='mc', q='Bei welcher Strategie wird <b>für jede/n Bewerber/in eine individuell passende Zielgruppe</b> angeboten?',
    options=['Selektion', 'Platzierung', 'Klassifikation', 'Verlaufsdiagnostik'], correct=2,
    expl='Klassifikation: Zuordnung zu alternativen Anforderungsprofilen, z. B. Schultypen, Störungsbilder, Zensuren.', kw='Klassifikation')
add(id='pd2-mc-08', type='mc', q='Eine <b>Klassenwiederholung</b> ist ein Beispiel für …',
    options=['Modifikation von Personen', 'Modifikation von Bedingungen', 'Selektion von Bedingungen', 'Klassifikation'], correct=1,
    expl='Modifikation von Bedingungen: Was kann durch Änderung der Bedingung erreicht werden? (Klassenwiederholung, Hochbegabtenklasse). Nachhilfe = Modifikation von Personen.', kw='Modifikation Bedingungen Klassenwiederholung')
add(id='pd2-mc-09', type='mc', q='Wann ist die <b>soziale Bezugsnorm</b> laut Folie sinnvoll?',
    options=['Wenn Lernfortschritte schwächerer Schüler gewürdigt werden sollen', 'Wenn über Selektion u. Ä. entschieden werden muss', 'Wenn ein definierter Leistungsstandard vorliegt', 'Bei der Notengebung in der normalen Schulklasse'], correct=1,
    expl='Dazu müssen die Einzelleistungen mit der gesamten Bezugsgruppe objektiv, gültig und zuverlässig verglichen werden. In der normalen Lerngruppe ist sie problematisch.', kw='soziale Bezugsnorm sinnvoll Selektion')
add(id='pd2-mc-10', type='mc', q='Was ist ein <b>Vorteil</b> der <b>sozialen</b> Bezugsnorm?',
    options=['Sie zeigt, inwieweit Lernziele erreicht wurden', 'Keine starr lineare Verknüpfung zwischen Fehlerzahl und Note', 'Lernfortschritte schwächerer Schüler werden gewürdigt', 'Anforderungen sind für Eltern durchsichtig'], correct=1,
    expl='Außerdem richtet sich die Beurteilung nach der Leistungsfähigkeit der Lerngruppe. Aussagen über Lernziele macht sie gerade nicht.', kw='soziale Bezugsnorm Vorteile')
add(id='pd2-mc-11', type='mc', q='Warum können bei der sozialen Bezugsnorm <b>Lernfortschritte schwächerer Schüler</b> nicht mit besserer Note gewürdigt werden?',
    options=['Weil die Lernziele zu niedrig angesetzt werden', 'Weil bei wirksamem Unterricht die durchschnittliche Leistung der Lerngruppe gleichfalls steigt', 'Weil der Gleichheitsgrundsatz verletzt wird', 'Weil die Fehlerzahl starr in Noten umgerechnet wird'], correct=1,
    expl='Die Note hängt vom Vergleich mit der Gruppe ab; steigt die ganze Gruppe, ändert sich die relative Position nicht.', kw='soziale Bezugsnorm Nachteil Lernfortschritte')
add(id='pd2-mc-12', type='mc', q='Welcher Zusammenhang wurde zwischen dem <b>mittleren Leistungsniveau einer Klasse</b> und der <b>Schulempfehlung</b> gefunden?',
    options=['Positiver Zusammenhang', 'Negativer Zusammenhang', 'Kein Zusammenhang', 'U-förmiger Zusammenhang'], correct=1,
    expl='Studie Milek et al. (2009). Hintergrund: Im klasseninternen Bezugssystem hängt die Note auch vom Leistungsniveau der Klasse ab.', kw='klasseninternes Bezugssystem Schulempfehlung')
add(id='pd2-mc-13', type='mc', q='Welche Bezeichnung gehört <b>nicht</b> zur kriterialen/sachlichen Bezugsnorm?',
    options=['Idealnorm', 'kriterienbezogene Norm', 'sachliche Bezugsnorm', 'klasseninternes Bezugssystem'], correct=3,
    expl='Das klasseninterne Bezugssystem ist eine Form der sozialen Bezugsnorm. Sachliche Bezugsnorm (Ingenkamp, 1985), Idealnorm (Gaude, 1989).', kw='kriteriale Bezugsnorm Idealnorm')
add(id='pd2-mc-14', type='mc', q='Was ist laut Folie der <b>Nachteil</b> der <b>kriterialen/sachlichen</b> Bezugsnorm?',
    options=['Kein Vergleich mit anderen Lerngruppen möglich', 'Konflikt mit dem Gleichheitsgrundsatz', 'Problem der Standards: Verführung, die Anforderungen zu niedrig anzusetzen', 'Sie kann zu großzügig und zu streng sein'], correct=2,
    expl='Gleichheitsgrundsatz = Nachteil der individuellen; kein Vergleich mit anderen Lerngruppen und zu großzügig/streng = Nachteile der sozialen Bezugsnorm.', kw='kriteriale Bezugsnorm Nachteil Standards')
add(id='pd2-mc-15', type='mc', q='Welche Bezugsnorm kann mit dem <b>Gleichheitsgrundsatz</b> in Konflikt geraten?',
    options=['soziale', 'kriteriale/sachliche', 'individuelle', 'alle drei gleichermaßen'], correct=2,
    expl='Individuelle Bezugsnorm: unterschiedliche Maßstäbe für verschiedene Schüler; der Gleichheitsgrundsatz gebietet denselben Maßstab für alle.', kw='individuelle Bezugsnorm Gleichheitsgrundsatz')
add(id='pd2-mc-16', type='mc', q='Grundlage für die Konstruktion und Interpretation von <b>wie vielen</b> psychologischen Testverfahren ist die Klassische Testtheorie?',
    options=['etwa 50 %', 'etwa 75 %', '95 %', '100 %'], correct=2,
    expl='Rost (1999): 95 % aller psychologischen Testverfahren.', kw='Klassische Testtheorie 95 Prozent')
add(id='pd2-mc-17', type='mc', q='Was besagt das <b>1. Axiom der KTT</b>?',
    options=['Der Mittelwert des Messfehlers ist Null', 'Messfehler verschiedener Personen sind unkorreliert', 'Der beobachtete Wert setzt sich aus wahrem Wert und zufälligem Messfehler zusammen: X = W(T) + e', 'Reliabilität kann nur geschätzt werden'], correct=2,
    expl='Mittelwert des Fehlers Null = 2. Axiom; unkorrelierte Fehler verschiedener Personen = 3. Axiom.', kw='1. Axiom KTT')
add(id='pd2-mc-18', type='mc', q='„Die <b>Korrelation zwischen Testwert und Messfehler ist Null</b>.“ Zu welchem Axiom gehört diese Aussage?',
    options=['1. Axiom', '2. Axiom', '3. Axiom', 'zu keinem'], correct=1,
    expl='2. Axiom: Die Messung variiert um den wahren Wert; Erwartungswert des Fehlers = 0, Korrelation Testwert–Messfehler = 0.', kw='2. Axiom KTT')
add(id='pd2-mc-19', type='mc', q='Ein <b>mehrdeutiges Item</b> erzeugt einen Messfehler …',
    options=['bei der Testkonstruktion', 'bei der Durchführung', 'bei der Auswertung', 'beim wahren Wert'], correct=0,
    expl='Testkonstruktion: mehrdeutige Items, missverständliche Instruktion. Durchführung: Testsituation, Person. Auswertung: Interpretation der Antworten, Zusammenzählen von Punkten.', kw='Messfehler Entstehung Testkonstruktion')
add(id='pd2-mc-20', type='mc', q='Lehrer A erlaubt den <b>Taschenrechner</b>, Lehrer B verbietet ihn. Welche Objektivität ist verletzt?',
    options=['Durchführungsobjektivität', 'Auswertungsobjektivität', 'Interpretationsobjektivität', 'Retestobjektivität'], correct=0,
    expl='Durchführungsobjektivität: gleiche Anforderungen unter gleichen Bedingungen für alle Getesteten.', kw='Durchführungsobjektivität Taschenrechner')
add(id='pd2-mc-21', type='mc', q='Lehrer A wertet <b>Rechtschreibfehler</b>, Lehrer B nicht. Welche Objektivität ist verletzt?',
    options=['Durchführungsobjektivität', 'Auswertungsobjektivität', 'Interpretationsobjektivität', 'Validität'], correct=1,
    expl='Auswertungsobjektivität: gleiches Verhalten wird stets auf die gleiche Weise ausgewertet.', kw='Auswertungsobjektivität Rechtschreibfehler')
add(id='pd2-mc-22', type='mc', q='Wie lässt sich die <b>Auswertungsobjektivität</b> verbessern?',
    options=['Maximale Standardisierung der Testsituation', 'Gebundene Antworten, Scanner- oder computergestützte Auswertung', 'Mehr Erfahrung des Testleiters', 'Paralleltests'], correct=1,
    expl='Standardisierung der Testsituation verbessert die Durchführungsobjektivität.', kw='Auswertungsobjektivität Verbesserung')
add(id='pd2-mc-23', type='mc', q='Gleiche Punktzahl, aber Lehrer A gibt Note 2, Lehrer B Note 4, Lehrer C Note 3. Welche Objektivität ist laut Folie gering?',
    options=['Durchführungsobjektivität', 'Auswertungsobjektivität', 'Interpretationsobjektivität', 'keine – das ist ein Reliabilitätsproblem'], correct=2,
    expl='Interpretationsobjektivität: Verschiedene Diagnostiker sollen gewonnene Befunde gleich interpretieren. Beeinträchtigt, wenn Intuition und Erfahrung einen Schluss begründen.', kw='Interpretationsobjektivität Noten')
add(id='pd2-mc-24', type='mc', q='Ab welchem Reliabilitätskoeffizienten gilt die Reliabilität eines Tests laut Folie als <b>ausreichend</b>?',
    options=['r > .3', 'r > .5', 'r > .7', 'r > .95'], correct=2,
    expl='r = 1: kein Messfehler; r = 0: riesiger Messfehler; r > .7: ausreichend.', kw='Reliabilität .7 ausreichend')
add(id='pd2-mc-25', type='mc', q='Welche Reliabilitätsschätzung gilt als <b>Königsweg</b>?',
    options=['Retestreliabilität', 'Paralleltestreliabilität', 'Split-Half-Reliabilität', 'Interne Konsistenz'], correct=1,
    expl='Zwei äquivalente Formen werden zeitgleich derselben Gruppe vorgelegt; Übungs- und Gedächtniseffekte werden vermieden.', kw='Paralleltestreliabilität Königsweg')
add(id='pd2-mc-26', type='mc', q='Was ist <b>kein</b> Problem der <b>Retestreliabilität</b>?',
    options=['Gedächtniseffekte', 'Instabilität des Merkmals', 'Lange Zeiträume zwischen den Testungen', 'Alle Personen erreichen beim zweiten Mal gleich viele Punkte mehr'], correct=3,
    expl='Veränderungen, die alle Personen gleich betreffen, mindern die Retestreliabilität nicht; nur interindividuell unterschiedliche Effekte tun das.', kw='Retestreliabilität Probleme')
add(id='pd2-mc-27', type='mc', q='Bei welcher Split-Half-Methode ist <b>nachlassende Aufmerksamkeit</b> oder <b>ansteigende Schwierigkeit</b> ein Problem?',
    options=['Odd-even-Methode', 'Trennung in erste und zweite Testhälfte', 'Bildung von Item-Paarlingen', 'Paralleltest'], correct=1,
    expl='Bei der Odd-even-Methode werden gerad- und ungeradzahlige Items getrennt; wichtig sind Item-Paarlinge mit annähernd gleicher Schwierigkeit.', kw='Split-Half erste zweite Hälfte')
add(id='pd2-mc-28', type='mc', q='Mit welcher <b>Methode</b> wird die <b>inhaltliche Validität</b> bewertet?',
    options=['Korrelation mit einem Kriterium', 'Expertenurteil', 'Retest', 'Faktorenanalyse'], correct=1,
    expl='Problematisch: Es gibt keine empirische Überprüfungsmöglichkeit.', kw='inhaltliche Validität Expertenurteil')
add(id='pd2-mc-29', type='mc', q='Ein neuer Mathetest soll <b>gering</b> mit der Sportnote korrelieren. Welche Validität ist gemeint?',
    options=['konvergente Validität', 'diskriminante Validität', 'prädiktive Validität', 'inhaltliche Validität'], correct=1,
    expl='Diskriminant: Testdaten, die verschiedene Merkmale abbilden sollen, sollen gering korrelieren. Hoch mit dem alten Mathetest = konvergent.', kw='diskriminante Validität')
add(id='pd2-mc-30', type='mc', q='Wovon hängt die Höhe der Korrelation bei der <b>Kriteriumsvalidität</b> laut Folie <b>nicht</b> ab?',
    options=['Reliabilität des Tests', 'Reliabilität des Kriteriums', 'Inhaltliche Gemeinsamkeiten von Test und Kriterium', 'Anzahl der Testleiter'], correct=3,
    expl='Genannt sind die Reliabilität des Tests, die Reliabilität des Kriteriums und die inhaltlichen Gemeinsamkeiten.', kw='Kriteriumsvalidität Höhe Korrelation')
add(id='pd2-mc-31', type='mc', q='Das Kriterium ist ein <b>in der Zukunft liegender Verhaltensaspekt</b> (z. B. Übertrittszeugnis → Gymnasialeignung). Das ist …',
    options=['konkurrente Validität', 'prädiktive Validität', 'innere Validität', 'inhaltliche Validität'], correct=1,
    expl='Konkurrent: Messung und Kriterium werden zeitgleich erhoben.', kw='prädiktive Validität')
add(id='pd2-mc-32', type='mc', q='Das Kriterium ist ein <b>anderer (alter) Test, der das Gleiche misst</b>. Das ist …',
    options=['äußere Validität', 'innere Validität', 'diskriminante Validität', 'Konstruktvalidität'], correct=1,
    expl='Äußere Validität: Kriterium ist ein anderer Test, der ein Merkmal erfasst, das hoch korreliert (z. B. IQ und Noten).', kw='innere Validität')
add(id='pd2-mc-33', type='mc', q='Welche Validitätsarten stehen im Baum der Folie <b>direkt unter der konvergenten Validität</b>?',
    options=['Inhalts- und Augenscheinvalidität', 'Konstruktvalidität und Kriteriumsvalidität', 'Innere und äußere Validität', 'Konkurrente und prädiktive Validität'], correct=1,
    expl='Validität → Inhaltsvalidität / empirische Validität → konvergente und diskriminante Validität; unter der konvergenten: Konstrukt- und Kriteriumsvalidität; unter der Kriteriumsvalidität: innere und äußere.', kw='Baum Validität konvergent')
add(id='pd2-mc-34', type='mc', q='„Zittern, Herzrasen, Schweißausbruch“ gehören beim Konstrukt Prüfungsangst zur Ebene …',
    options=['Verhalten', 'Physiologie', 'Kognition', 'Emotion'], correct=1,
    expl='Verhalten: Vermeidung, sich abwenden; Kognition: negative Gedanken; Emotion: Angst.', kw='Prüfungsangst Physiologie')
add(id='pd2-mc-35', type='mc', q='Was gilt nach der KTT für die <b>Beziehung von Reliabilität und Validität</b>?',
    options=['Ein valider Test kann unreliabel sein', 'Ein nicht reliabler Test kann nicht valide sein, ein reliabler Test muss aber nicht valide sein', 'Ein reliabler Test ist immer valide', 'Reliabilität und Validität werden in einer gemeinsamen Prozedur bestimmt'], correct=1,
    expl='Ein reliabler, aber nicht valider Test erfasst etwas genau, nur nicht das Gewünschte (Lineal misst Länge, nicht Gewicht). Beides sind zwei unabhängige Prozeduren.', kw='Beziehung Validität Reliabilität')

# Richtig / Falsch
add(id='pd2-tf-01', type='tf', statement='Die Verlaufsdiagnostik setzt voraus, dass das Merkmal stabil ist.', answer=False,
    expl='Das ist die Voraussetzung der Eingangs-/Statusdiagnostik. Die Verlaufsdiagnostik begleitet den Prozess durch mehrfache Messungen.', kw='Verlaufsdiagnostik Statusdiagnostik')
add(id='pd2-tf-02', type='tf', statement='Stellenbesetzung ist ein Beispiel für die Selektion von Personen.', answer=True,
    expl='Welche Person passt auf die Bedingung?', kw='Selektion von Personen Stellenbesetzung')
add(id='pd2-tf-03', type='tf', statement='Nachhilfeunterricht ist ein Beispiel für die Modifikation von Bedingungen.', answer=False,
    expl='Nachhilfe = Modifikation von Personen (Was kann die Person tun, um zu „passen“?).', kw='Modifikation von Personen Nachhilfe')
add(id='pd2-tf-04', type='tf', statement='Die soziale Bezugsnorm wird häufig bei formellen Schulleistungstests (Jahrgangsstufentests) angewandt.', answer=True,
    expl='Als Grundlage der Beurteilung in der normalen Lerngruppe ist sie dagegen problematisch.', kw='soziale Bezugsnorm Jahrgangsstufentests')
add(id='pd2-tf-05', type='tf', statement='Die soziale Bezugsnorm macht Aussagen darüber, inwieweit Lernziele erreicht worden sind.', answer=False,
    expl='Das ist gerade ein Nachteil: Sie macht keine Aussagen über das Erreichen der Lernziele.', kw='soziale Bezugsnorm Lernziele')
add(id='pd2-tf-06', type='tf', statement='Im klasseninternen Bezugssystem hängt die Note auch vom Leistungsniveau der Klasse ab; solche Noten sind daher nicht zur Selektion oder Platzierung geeignet.', answer=True,
    expl='Schulnoten sind dadurch nicht vergleichbar (Trautwein, 2007).', kw='klasseninternes Bezugssystem')
add(id='pd2-tf-07', type='tf', statement='Bei der kriterialen Bezugsnorm ist der Vergleich mit anderen Schülern entscheidend.', answer=False,
    expl='Er interessiert höchstens am Rande; entscheidend ist der Grad, in dem ein Lernziel erreicht wurde.', kw='kriteriale Bezugsnorm')
add(id='pd2-tf-08', type='tf', statement='Die kriteriale Bezugsnorm macht die Anforderungen für Schüler und Eltern eindeutig und durchsichtig.', answer=True,
    expl='Weitere Vorteile: informiert über Kompetenzen und Lücken; Lernfortschritte schwächerer Schüler werden erkannt.', kw='kriteriale Bezugsnorm Vorteile')
add(id='pd2-tf-09', type='tf', statement='Die individuelle Bezugsnorm vergleicht die Leistung mit den früheren Lernergebnissen desselben Schülers.', answer=True,
    expl='Vorteil: würdigt und fördert den einzelnen Schüler am besten.', kw='individuelle Bezugsnorm')
add(id='pd2-tf-10', type='tf', statement='Der wahre Wert ist direkt messbar, nur der Messfehler muss geschätzt werden.', answer=False,
    expl='Wahrer Wert und Messfehler sind beide nicht messbar, nur schätzbar.', kw='wahrer Wert schätzbar')
add(id='pd2-tf-11', type='tf', statement='Der Messfehler repräsentiert alle unkontrollierten und unsystematischen Störeinflüsse bei der Messung.', answer=True,
    expl='z. B. Tagesform, Motivation, Testbedingungen.', kw='Messfehler Störeinflüsse')
add(id='pd2-tf-12', type='tf', statement='Nach dem 3. Axiom der KTT sind die Messfehler bei unterschiedlichen Personen unkorreliert.', answer=True,
    expl='Folgerung auf der Folie: Je häufiger man misst, desto mehr nähert man sich dem wahren Wert.', kw='3. Axiom')
add(id='pd2-tf-13', type='tf', statement='Soziale Interaktionen zwischen Testperson und Testleiter beeinträchtigen die Auswertungsobjektivität.', answer=False,
    expl='Sie beeinträchtigen die Durchführungsobjektivität.', kw='Durchführungsobjektivität soziale Interaktion')
add(id='pd2-tf-14', type='tf', statement='Mündliche Prüfungen sind wegen offener Antworten ein Risiko für die Auswertungsobjektivität.', answer=True,
    expl='Offene Antworten erfordern eine inhaltliche Klassifikation.', kw='Auswertungsobjektivität mündliche Prüfung')
add(id='pd2-tf-15', type='tf', statement='Die Interpretationsobjektivität wird verbessert, wenn aus den Punktwerten auf die individuelle Position auf einer Merkmalsdimension geschlossen wird.', answer=True,
    expl='Beeinträchtigt wird sie, wenn Intuition und Erfahrung des Testleiters einen Schluss begründen.', kw='Interpretationsobjektivität Verbesserung')
add(id='pd2-tf-16', type='tf', statement='Reliabilitätskoeffizienten liegen zwischen −1 und +1.', answer=False,
    expl='Reliabilitätskoeffizienten liegen zwischen 0 und +1. Zwischen −1 und +1 kann die Korrelation bei der Kriteriumsvalidität liegen.', kw='Reliabilitätskoeffizient Wertebereich')
add(id='pd2-tf-17', type='tf', statement='Reliabilität kann nur geschätzt, nicht gemessen werden.', answer=True,
    expl='Steht ausdrücklich auf der Folie.', kw='Reliabilität geschätzt')
add(id='pd2-tf-18', type='tf', statement='Die Retestreliabilität gibt einen Hinweis auf die Stabilität des untersuchten Merkmals.', answer=True,
    expl='Stabilität des Traits.', kw='Retestreliabilität Stabilität')
add(id='pd2-tf-19', type='tf', statement='Wenn alle Testpersonen beim zweiten Test zehn Punkte mehr erreichen, sinkt die Retestreliabilität.', answer=False,
    expl='Veränderungen, die alle Personen betreffen, mindern sie nicht. Sie sinkt nur bei interindividuell unterschiedlich großen Effekten.', kw='Retestreliabilität zehn Punkte')
add(id='pd2-tf-20', type='tf', statement='Für Kreativitätstests lassen sich nicht immer äquivalente Parallelformen bilden.', answer=True,
    expl='Problem der Paralleltestreliabilität; außerdem ist die Konstruktion sehr aufwendig.', kw='Paralleltest Kreativität')
add(id='pd2-tf-21', type='tf', statement='Bei der inhaltlichen Validität gibt es eine empirische Überprüfungsmöglichkeit.', answer=False,
    expl='Genau das ist das Problem: keine empirische Überprüfung, nur Expertenurteil.', kw='inhaltliche Validität Problem')
add(id='pd2-tf-22', type='tf', statement='Bei der Konstruktvalidität soll ein Test niedrig mit Kriterien korrelieren, die nach der Theorie nicht mit dem Konstrukt verbunden sind.', answer=True,
    expl='Das ist die diskriminante Validität; hoch mit verbundenen Kriterien = konvergente Validität.', kw='Konstruktvalidität diskriminant')
add(id='pd2-tf-23', type='tf', statement='Konstrukte wie Intelligenz oder Angst existieren nicht, weil sie nicht empirisch erkennbar sind.', answer=False,
    expl='Sie werden nur aus messbaren Sachverhalten (Indikatoren) erschlossen = latente Konstrukte. Das heißt nicht, dass sie nicht existieren.', kw='Konstrukt latent')
add(id='pd2-tf-24', type='tf', statement='Laut Abbildung wirkt die Interpretationsobjektivität direkt auf die Validität, die übrigen Objektivitätsarten wirken über die Reliabilität.', answer=True,
    expl='Grundidee: Objektivität → Reliabilität → Validität; die Interpretationsobjektivität geht direkt auf die Validität.', kw='Beziehung Objektivität Reliabilität Validität')
add(id='pd2-tf-25', type='tf', statement='Ein reliabler Test ist automatisch auch valide.', answer=False,
    expl='Er kann etwas genau erfassen, nur nicht das Gewünschte – wie ein Lineal, das die Länge, aber nicht das Gewicht eines Briefes misst.', kw='reliabel nicht valide')
add(id='pd2-tf-26', type='tf', statement='Prädiktive Validität ist meist nicht möglich, wenn der Zeitraum zu groß ist, weil relevante Eigenschaften vielleicht erst später erworben werden.', answer=True,
    expl='Beispiel auf der Folie: gute Staatsexamensnote = guter Lehrer?', kw='Probleme Validität prädiktiv')

# Lückentext
add(id='pd2-gap-01', type='gap', text='Eingangsdiagnostik heißt auch {{Statusdiagnostik}}, Verlaufsdiagnostik auch {{Prozessdiagnostik}}.',
    expl='Strategie Zeitpunkt.', kw='Statusdiagnostik Prozessdiagnostik')
add(id='pd2-gap-02', type='gap', text='Diagnostik mit dem Ziel, Personen oder Bedingungen zu verändern, heißt Modifikations- bzw. {{Förderdiagnostik|Förder}}.',
    expl='Strategie Veränderung.', kw='Förderdiagnostik')
add(id='pd2-gap-03', type='gap', text='Die kriteriale Bezugsnorm heißt auch {{Idealnorm}}, weil sie reale mit idealen Leistungen vergleicht.',
    expl='Bezeichnung bei Gaude (1989); „sachliche Bezugsnorm“ bei Ingenkamp (1985).', kw='Idealnorm')
add(id='pd2-gap-04', type='gap', text='1. Axiom der KTT: X = {{W(T)|W|wahrer Wert}} + e.',
    expl='Beobachteter Wert = wahrer Wert + zufälliger Messfehler.', kw='1. Axiom Formel')
add(id='pd2-gap-05', type='gap', text='Nach dem 2. Axiom ist der erwartete Mittelwert des Messfehlers {{Null|0}}.',
    expl='Auch die Korrelation zwischen Testwert und Messfehler ist Null.', kw='2. Axiom Mittelwert')
add(id='pd2-gap-06', type='gap', text='Je {{häufiger|öfter|mehr}} man misst, desto mehr nähert man sich dem wahren Wert.',
    expl='Folgerung auf der Folie zum 3. Axiom.', kw='häufiger messen wahrer Wert')
add(id='pd2-gap-07', type='gap', text='Standardisierung eines Konstrukts durch Angabe des Verhaltens, das es anzeigt, heißt {{Operationalisierung}}.',
    expl='Das Verhalten dient als Indikator.', kw='Operationalisierung')
add(id='pd2-gap-08', type='gap', text='Die Durchführungsobjektivität verbessert man durch maximale {{Standardisierung}} der Testsituation.',
    expl='Material, Situation, Testanweisung usw.', kw='Durchführungsobjektivität Standardisierung')
add(id='pd2-gap-09', type='gap', text='Reliabilität ist ein {{korrelatives}} Maß für die Genauigkeit, mit der ein Test ein Merkmal erfasst.',
    expl='Werte zwischen 0 und +1; ab r > .7 ausreichend.', kw='Reliabilität korrelatives Maß')
add(id='pd2-gap-10', type='gap', text='Bei der Split-Half-Reliabilität trennt die {{Odd-even|Odd-even-Methode|odd even}}-Methode gerad- und ungeradzahlige Items.',
    expl='Wichtig: Item-Paarlinge mit annähernd gleicher Schwierigkeit.', kw='Odd-even')
add(id='pd2-gap-11', type='gap', text='Inhaltliche Validität wird mittels eines {{Repräsentationsschlusses|Repräsentationsschluss}} ermittelt.',
    expl='Die Items bilden eine repräsentative Stichprobe aus dem Merkmalsbereich (z. B. Englisch-Vokabeln).', kw='Repräsentationsschluss')
add(id='pd2-gap-12', type='gap', text='Die Korrelation bei der Kriteriumsvalidität kann zwischen −1 und +1 liegen, Reliabilitätskoeffizienten dagegen nur zwischen {{0|null}} und +1.',
    expl='Reliabilität: r = 1 kein Messfehler, r = 0 riesiger Messfehler. Kriteriumsvalidität: z. B. Schulnoten als Kriterium für Intelligenz.', kw='Kriteriumsvalidität Wertebereich')
add(id='pd2-gap-13', type='gap', text='Konstrukte werden aus messbaren Sachverhalten, sogenannten {{Indikatoren}}, erschlossen.',
    expl='Deshalb heißen sie latente Konstrukte.', kw='Konstrukt Indikatoren')
add(id='pd2-gap-14', type='gap', text='Konkurrente Validität: Test und Kriterium werden {{zeitgleich|gleichzeitig}} erhoben.',
    expl='Prädiktiv: Kriterium liegt in der Zukunft.', kw='konkurrente Validität')
add(id='pd2-gap-15', type='gap', text='Eine niedrige Korrelation zwischen Test und Kriterium kann durch {{Konfundierung}} mit anderen Variablen entstehen.',
    expl='Eines der Probleme der Validität in der KTT.', kw='Konfundierung')
