# Psycho 2 · Diagnostische Psychologie (Vorlesung Barchfeld-Pekrun, LMU) · Teil 1
# Quelle: Folien „2025 Diagnostik Teil 1 KURZ“ (36 Folien). Nur Inhalte aus den Folien
# plus zwei Erläuterungen des Nutzers (Zuordnung Folie 3, rote Linien Folie 25 = nur Unkenntlichmachung durch die Dozentin, kein Inhalt).

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

D = 'Teil 1 · Definition'
B = 'Teil 1 · Verhaltensbeobachtung'
T = 'Teil 1 · Testverfahren'
W = 'Teil 1 · WISC-V'
I = 'Teil 1 · Interviews'

CARDS_D1 = [
    C('begriff', D, 'Woher kommt der Begriff <b>Diagnostik</b> und was bedeutet er?',
      'Griechisch <b>„diagignoskein“</b>: bezeichnet Aspekte eines kognitiven Vorgangs <b>vom Erkennen bis zum Beschließen</b>.<br><br>Das Verb bedeutet <b>„gründlich kennenlernen“</b>, <b>„entscheiden“</b> und <b>„beschließen“</b>.',
      'diagignoskein griechisch Erkennen Beschließen gründlich kennenlernen entscheiden'),
    C('gegenstand', D, 'Was ist der <b>Gegenstand der Diagnostik</b>? (drei Definitionen)',
      '<ul><li><b>Amelang &amp; Schmidt-Atzert (2006):</b> Erfassen von <b>interindividuellen Unterschieden</b> im Verhalten und Erleben sowie <b>intraindividuellen Merkmalen und Veränderungen</b> einschließlich ihrer jeweils relevanten Bedingungen.</li><li><b>Eid &amp; Petermann (2006):</b> Sammeln von Informationen, die für das <b>Verständnis menschlichen Verhaltens und Erlebens</b> bedeutsam sind.</li><li><b>Kubinger (2009):</b> Erfassen von <b>psychischen Merkmalen</b> von einem (oder mehreren) Menschen.</li></ul>',
      'Gegenstand Definition Amelang Schmidt-Atzert Eid Petermann Kubinger interindividuell intraindividuell'),
    C('aufgaben', D, 'Welche <b>Aufgabenbereiche</b> hat die (Alltags-)Diagnostik? Nenne die fünf Entwicklungsbereiche mit ihren Merkmalen.',
      'Im Mittelpunkt steht <b>die Entwicklung des ganzen Kindes</b>:<ul><li><b>Soziale Entwicklung:</b> Kontaktfähigkeit, Konfliktfähigkeit, Selbständigkeit</li><li><b>Sprachliche Entwicklung:</b> Sprachfähigkeit, Sprachverständnis</li><li><b>Intellektuelle Entwicklung:</b> Konzentration, Aufmerksamkeit, Gliederungsfähigkeit, Mengenerfassung, Arbeitsverhalten, Denkfähigkeit, Gedächtnis, Wahrnehmung</li><li><b>Motorische Entwicklung:</b> Feinmotorik, Grobmotorik</li><li><b>Gefühlsmäßige (emotionale) Entwicklung:</b> Motivation, Selbstvertrauen</li></ul>',
      'Aufgabenbereiche Alltagsdiagnostik Entwicklung ganzes Kind sozial sprachlich intellektuell motorisch emotional gefühlsmäßig'),
    C('ziel', D, 'Was ist das <b>Ziel</b> der pädagogischen Diagnostik?',
      '<b>Individuelles Lernen optimieren:</b> Voraussetzungen schaffen, um <b>jeden (jeden!)</b> Lernenden <b>nach seinen Fähigkeiten</b> fördern zu können.',
      'Ziel individuelles Lernen optimieren fördern Fähigkeiten'),
    C('drei-fragen', D, 'Welche <b>drei Fragen</b> sind Voraussetzungen für die Optimierung individuellen Lernens?',
      '<ol><li><b>Was</b> wird gemessen?</li><li><b>Wozu</b> wird gemessen?</li><li><b>Wie</b> wird gemessen?</li></ol>',
      'Voraussetzungen Was Wozu Wie gemessen'),
    C('was', D, '<b>Was wird gemessen?</b> Welche zwei Arten von Merkmalen gibt es?',
      '<ul><li><b>Personenmerkmale:</b> Verhalten &amp; Eigenschaften = <b>Persönlichkeit</b></li><li><b>Umweltmerkmale:</b><ul><li><b>Schule</b>, z. B. Unterrichtsqualität, Klassenklima</li><li><b>Elternhaus</b>, z. B. elterliche Unterstützung, Familiengröße, sozioökonomischer Status</li></ul></li></ul>',
      'Personenmerkmale Umweltmerkmale Schule Elternhaus Unterrichtsqualität Klassenklima Familiengröße sozioökonomischer Status'),
    C('persoenlichkeit', D, 'Wie definiert <b>Pekrun (1988)</b> die <b>Persönlichkeit</b> eines Menschen?',
      'Die <b>Gesamtheit derjenigen Merkmale</b> eines Menschen, die<br>a) <b>(mindestens relativ) zeitstabil</b> sind und<br>b) ihn <b>von anderen Menschen unterscheiden</b> können.',
      'Persönlichkeit Pekrun zeitstabil unterscheiden Gesamtheit Merkmale'),
    C('wozu-1', D, '<b>Wozu wird gemessen? (I)</b> Welche drei Ziele bezogen auf Verhalten gibt es?',
      '<ul><li><b>Beschreiben</b> von Verhalten: Eigenschaften als <b>hypothetisches Konstrukt</b>; Schaffung künstlicher Klassen (<b>Klassifikation</b>)</li><li><b>Erklären</b> von Verhalten: Ereignisse und Eigenschaften als <b>Ursache</b>; Bedingungen für die <b>Aufrechterhaltung eines Fehlverhaltens</b></li><li><b>Vorhersagen</b> von Verhalten: Verhalten ist <b>nur zum Teil</b> vorhersagbar</li></ul>',
      'Wozu Beschreiben Erklären Vorhersagen hypothetisches Konstrukt Klassifikation Fehlverhalten'),
    C('wozu-2', D, '<b>Wozu wird gemessen? (II)</b> Für welche Entscheidungen und welche Forschung?',
      '<b>Basis für „richtige“ Entscheidungen „im Sinne“ des Individuums:</b><ul><li>Optimierungs-/<b>Fördermaßnahmen</b></li><li><b>Platzierungsmaßnahmen</b> (Platzierung von Schülern)</li><li><b>Selektionsmaßnahmen</b> (Selektion von Bedingungen/Maßnahmen)</li></ul><b>Im Kontext erziehungswissenschaftlicher Forschung:</b><ul><li>Determinanten des Lernens</li><li>Wirksamkeit von Lehr-Lern-Arrangements</li><li>Qualitätsmerkmale von Unterricht/Schule</li></ul>',
      'Entscheidungen Förderung Platzierung Selektion Forschung Determinanten Lehr-Lern-Arrangements Qualität'),
    C('wie', D, '<b>Wie wird gemessen?</b> Welche vier diagnostischen Verfahren gibt es?',
      '<ul><li><b>Verhaltensbeobachtung</b> (Verhalten in bestimmten Situationen): Fachkompetenz (Mathefähigkeiten, sprachliche Kompetenzen), Verhaltensstil/Persönlichkeit (gesellig, gewissenhaft …), Temperamentsmerkmale (Ausdauer, Aktivität …), soziale Kompetenzen (Umgang mit Peers, Lehrern …)</li><li><b>Testverfahren</b> (Intelligenz-, Leistungs-, Persönlichkeitstests)</li><li><b>Interviews</b></li><li><b>Akteninformation</b> (Zeugnisse, Tagebücher, Facebook …)</li></ul>',
      'Verfahren Verhaltensbeobachtung Testverfahren Interviews Akteninformation Temperament'),

    C('inferenz', B, 'Was ist bei der Verhaltensbeobachtung <b>kritisch</b>? Was ist <b>Inferenz</b>?',
      'Kritisch ist, <b>welche Schlussfolgerungen</b> eine Lehrkraft aus den Beobachtungen zieht (= <b>Inferenz</b>).<br><br>Inferenzprozesse laufen im Alltag in der Regel <b>automatisch</b> ab. Beispiel: Schüler*in beteiligt sich oft am Unterricht = Schüler*in ist interessiert.',
      'Inferenz Schlussfolgerung automatisch Verhaltensbeobachtung'),
    C('selektion', B, 'Warum ist Beobachtung <b>keine Abbildung der Wirklichkeit</b>?',
      'Nicht alles Wahrnehmbare wird auch beobachtet: Beobachtung ist immer ein <b>Selektionsprozess</b>. Im Alltag ziehen oft die <b>erwartungswidrigen</b> Verhaltensweisen die Aufmerksamkeit auf sich.<br><br>Beobachtung ist also ein <b>aktiver Konstruktionsprozess</b>.',
      'Selektionsprozess erwartungswidrig aktiver Konstruktionsprozess Wirklichkeit'),
    C('sampling', B, 'Was ist der Unterschied zwischen <b>Time Sampling</b> und <b>Event Sampling</b>?',
      '<b>Beobachtungsstichproben:</b><ul><li><b>Time Sampling:</b> Beobachtung von Verhaltensweisen in einem <b>bestimmten Zeitabschnitt</b> (z. B. Wie oft tritt Verhalten X in einer Minute auf?) → <b>Häufigkeitsregistrierung</b></li><li><b>Event Sampling:</b> Beobachtet wird <b>nur, wenn Verhalten X auftritt</b>; Messung der <b>Dauer</b> des Verhaltens möglich; sinnvoll, wenn das Zielverhalten <b>selten</b> ist</li></ul>',
      'Time Sampling Event Sampling Beobachtungsstichproben Häufigkeit Dauer selten'),
    C('frei-syst', B, 'Was kennzeichnet <b>freie</b> und <b>systematische</b> Beobachtung?',
      '<b>Freie Beobachtung:</b><ul><li>Beobachter entscheidet über den Gegenstand der Beobachtung</li><li>Aufmerksamkeit gilt einem bestimmten Bereich</li><li>Ergebnis oft in <b>qualitativer</b> Form</li></ul><b>Systematische Beobachtung:</b><ul><li><b>Hypothesengeleitet</b></li><li>Genaue Vorgaben</li><li>Ergebnisse in <b>quantitativer</b> Form</li></ul>',
      'freie Beobachtung systematische Beobachtung hypothesengeleitet qualitativ quantitativ'),
    C('frei-syst-vn', B, 'Vor- und Nachteile von <b>systematischer</b> und <b>freier</b> Beobachtung?',
      '<b>Systematisch</b><br>+ Erlaubt Quantifizierung<br>− Vorbereitungsaufwand<br>− Einübung der Beobachter nötig<br><br><b>Frei</b><br>+ Geeignet zur Ersterkundung eines Beobachtungsziels<br>+ Qualitative Ergebnisse<br>− Ergebnisse wenig objektiv und messgenau<br>− Aufwand und Ertrag wenig kalkulierbar',
      'Vorteile Nachteile systematisch frei Quantifizierung Ersterkundung objektiv messgenau'),
    C('teilnehmend', B, 'Welche Formen <b>teilnehmender</b> und <b>nicht teilnehmender</b> Beobachtung gibt es?',
      '<b>Teilnehmende Beobachtung:</b><ul><li><b>Aktive Teilnahme:</b> Beobachter ist Teil des Geschehens</li><li><b>Passive Teilnahme:</b> Beobachter ist anwesend, aber nicht Teil der Interaktion</li></ul><b>Nicht teilnehmende Beobachtung</b> (= <b>verdeckte</b> Beobachtung): Beobachter ist <b>nicht sichtbar</b>.',
      'teilnehmend aktiv passiv nicht teilnehmend verdeckt'),
    C('teilnehmend-vn', B, 'Vor- und Nachteile von <b>teilnehmender</b> und <b>nicht teilnehmender</b> Beobachtung?',
      '<b>Teilnehmend</b><br>+ Manchmal einzig mögliche Methode<br>+ Technisch unaufwändig<br>− Doppelbelastung bei aktiver Teilnahme<br>− Beobachtete fühlen sich gestört (<b>Reaktivität</b>)<br><br><b>Nicht teilnehmend</b><br>+ Situation wird nicht verändert<br>− Technischer Aufwand<br>− Meist fester Beobachtungsblickwinkel',
      'Vorteile Nachteile teilnehmend Reaktivität Doppelbelastung Blickwinkel'),
    C('direkt', B, 'Was ist <b>direkte</b> und <b>indirekte</b> Beobachtung?',
      '<b>Direkte Beobachtung:</b> zeitgleich; Standpunktveränderungen möglich.<br><br><b>Indirekte Beobachtung:</b> zeitversetzt durch <b>Videoaufnahmen</b>.',
      'direkte indirekte Beobachtung zeitgleich zeitversetzt Video'),
    C('direkt-vn', B, 'Vor- und Nachteile von <b>direkter</b> und <b>indirekter</b> Beobachtung?',
      '<b>Direkt</b><br>+ Standortwechsel möglich<br>+ Keine Verzerrung durch Erinnerung<br>− Beschränkte Menge der registrierten Einzeldaten<br>− Zeitgleich beobachten und codieren<br>− Aufwändige Vorbereitung<br><br><b>Indirekt</b><br>+ Datenaggregation vor der Beurteilung<br>+ Wiederholtes Ansehen möglich<br>+ Längere Verhaltensausschnitte<br>− Eine Perspektive<br>− Qualität abhängig von der Definition der Beobachtungseinheiten',
      'Vorteile Nachteile direkt indirekt Erinnerung Datenaggregation Perspektive Beobachtungseinheiten'),
    C('drift', B, 'Was ist <b>Beobachterdrift</b>, wodurch entsteht er und was hilft dagegen?',
      'Ohne tatsächliche Verhaltensänderung werden <b>zunehmend mehr oder weniger</b> relevante Ereignisse entdeckt.<ul><li><b>Ermüdung</b> und nachlassende Aufmerksamkeit → <b>Abnahme</b></li><li><b>Mangelnde Übung</b> → <b>Zunahme</b></li></ul><b>Gegenmaßnahmen:</b><ul><li>Angemessen lange Beobachtungsphasen (<b>max. 20 Minuten</b>)</li><li>Ausreichendes <b>Beobachtertraining</b></li></ul>',
      'Beobachterdrift Beobachtungsfehler Ermüdung Übung 20 Minuten Beobachtertraining'),
    C('reaktivitaet', B, 'Welches Beobachterverhalten <b>fördert Reaktivität</b>? Was ist angemessen?',
      '<ul><li>Hervorhebung der Präsenz</li><li>Auskosten der „Macht“</li><li>Geflüster, Gespräche</li><li>Nonverbale „Kommentierung“ des Geschehens (Lächeln, Kopfschütteln, Hochziehen der Augenbrauen etc.)</li></ul>→ Angemessen ist <b>neutrales, zurückhaltendes Verhalten</b>.',
      'Reaktivität Beobachtungsfehler Präsenz Macht nonverbal neutral zurückhaltend'),

    C('test-def', T, 'Wie definieren <b>Hasselhorn &amp; Gold (2006)</b> einen <b>Test</b>?',
      'Ein <b>systematisches und routinemäßig einsetzbares Verfahren</b> zur Messung <b>definierter Ausschnitte menschlichen Verhaltens</b>.<br><br>Die Messung wird verwendet, um den <b>Grad der Ausprägung</b> einer Eigenschaft, Fähigkeit oder Fertigkeit festzustellen und/oder um <b>zukünftiges Verhalten vorherzusagen</b>.',
      'Test Definition Hasselhorn Gold systematisch routinemäßig Ausprägung vorhersagen'),
    C('leistungstests', T, 'Welche vier Arten von <b>Leistungstests</b> gibt es?',
      '<ul><li><b>Entwicklungstests:</b> zeigen den Entwicklungsstand global oder einzelner Funktionsbereiche (Sprache, Motorik)</li><li><b>Intelligenztests:</b> erfassen die kognitive Leistungsfähigkeit</li><li><b>Allgemeine Leistungstests:</b> messen allgemeine Voraussetzungen von Leistung, z. B. Konzentration, Aufmerksamkeit</li><li><b>Schulleistungstests:</b> messen Schulfähigkeit und den schulischen Leistungsstand</li></ul>Daneben gibt es <b>psychometrische Persönlichkeitstests</b> (werden in der VL Persönlichkeitspsychologie behandelt).',
      'Leistungstests Entwicklungstests Intelligenztests allgemeine Leistungstests Schulleistungstests Persönlichkeitstests'),
    C('wechsler-def', T, 'Wie definiert <b>David Wechsler (1944)</b> Intelligenz und welche Bereiche gehören dazu?',
      'Intelligenz ist die „Fähigkeit des Individuums, <b>zweckvoll zu handeln</b>, <b>vernünftig zu denken</b> und sich mit seiner Umgebung <b>wirkungsvoll auseinanderzusetzen</b>“.<ul><li>Sprachliches Verständnis</li><li>Abstraktes logisches Denken</li><li>Wahrnehmungsorganisation</li><li>Mengenbezogenes Denken</li><li>Gedächtnis</li><li>Verarbeitungsgeschwindigkeit</li></ul>',
      'Intelligenz Definition Wechsler zweckvoll handeln vernünftig denken Umgebung'),
    C('normalverteilung', T, 'Wie ist Intelligenz verteilt? Welche <b>Kennwerte</b> und <b>Begabungsbereiche</b> gibt es?',
      '<b>Normalverteilung</b>; alle IQ-Tests: <b>M = 100, SD = 15</b>.<ul><li>unter 70: <b>Minderbegabung</b></li><li>70–85: <b>unterdurchschnittliche</b> Begabung</li><li>85–115: <b>normale</b> Begabung</li><li>115–130: <b>überdurchschnittliche</b> Begabung</li><li>über 130: <b>Hochbegabung</b></li></ul>Anteile je Abschnitt (55 · 70 · 85 · 100 · 115 · 130 · 145): 0,13 % · 2,14 % · 13,60 % · 34,13 % · 34,13 % · 13,60 % · 2,14 % · 0,13 %.',
      'Normalverteilung IQ Mittelwert 100 Standardabweichung 15 Hochbegabung Minderbegabung'),
    C('stern', T, 'Wie berechnet sich der <b>Intelligenzquotient nach Stern (1912)</b>?',
      'IQ = <b>geistiges Alter / reales Alter × 100</b><br><br>Beispiel: geistiges Alter 8, reales Alter 10 → IQ = 8/10 × 100 = <b>80</b>.',
      'Intelligenzquotient Stern 1912 geistiges Alter Lebensalter Formel'),
    C('stern-problem', T, 'Welches <b>Problem</b> hat der IQ nach Stern und wie löste <b>Wechsler</b> es?',
      '<b>Problem:</b> Die Relation Lebensalter / geistiges Alter ändert sich. Beispiel: 25/25 × 100 = 100, aber 25/55 × 100 = <b>45</b>.<br><br><b>Lösung (David Wechsler):</b> IQ in Relation zum <b>Mittelwert der Altersgruppe</b>, nicht zum Lebensalter.',
      'Stern Problem Wechsler Lösung Altersgruppe Mittelwert Lebensalter'),

    C('wisc', W, 'Was sind die <b>Eckdaten des WISC-V</b> (Wechsler Intelligenztest für Kinder)?',
      '<ul><li><b>Individualtest</b></li><li>Untersuchung der <b>kognitiven Entwicklung</b></li><li>Altersbereich: <b>6 bis 16 Jahre, 11 Monate</b></li><li>Für Deutschland, Österreich und die deutschsprachige Schweiz</li><li><b>5 Gruppen (Indizes) mit 15 Untertests</b></li></ul>',
      'WISC-V Wechsler Kinder Individualtest Altersbereich Indizes Untertests'),
    C('wisc-eignung', W, 'Wofür ist der <b>WISC-V geeignet</b>?',
      '<ul><li>Feststellung des <b>sonderpädagogischen Förderbedarfs</b></li><li>Diagnostik von <b>Lernbehinderungen</b>: Klärung der Ursachen von Leistungsproblemen (Legasthenie, Dyskalkulie)</li><li>Diagnostik von <b>Hochbegabung</b></li></ul>',
      'WISC Eignung sonderpädagogischer Förderbedarf Lernbehinderung Legasthenie Dyskalkulie Hochbegabung'),
    C('indizes', W, 'Welche <b>fünf Indizes</b> hat der WISC-V und welcher Untertest gehört (laut Folien) jeweils dazu?',
      'Alle fünf fließen in den <b>Gesamt-IQ</b> ein, je <b>2 Subtests</b> pro Index:<ul><li><b>SV</b> Sprachverständnis → Gemeinsamkeiten finden</li><li><b>VRV</b> Visuell-räumliche Verarbeitung → Mosaiktest</li><li><b>FS</b> Fluides Schlussfolgern → Formenwaage</li><li><b>AGD</b> Arbeitsgedächtnis → Buchstaben-Zahlen-Folgen</li><li><b>VG</b> Verarbeitungsgeschwindigkeit → Zahlen-Symbol-Test A</li></ul>',
      'WISC Indizes SV VRV FS AGD VG Gesamt-IQ Subtests'),
    C('agd', W, 'Was misst der Index <b>Arbeitsgedächtnis (AGD)</b> und wie funktioniert der Subtest <b>Buchstaben-Zahlen-Folgen</b>?',
      '<b>Arbeitsgedächtnis:</b> ein Teil des menschlichen Gedächtnisses für <b>kurze (ca. 30 Sek.) Speicherung und Veränderungen</b>; hat eine <b>geringe Kapazität (± 7 Einheiten)</b>.<br><br><b>Buchstaben-Zahlen-Folgen (BZF):</b> Eine gemischte Folge wird vorgegeben und muss geordnet wiedergegeben werden, Zahlen und Buchstaben jeweils sortiert:<ul><li>A-2 → A-2 oder 2-A</li><li>2-A-3 → A-2-3 oder 2-3-A</li><li>L-2-J-6-Q-3-G → 2-3-6-G-J-L-Q oder G-J-L-Q-2-3-6</li></ul>',
      'Arbeitsgedächtnis AGD 30 Sekunden Kapazität 7 Buchstaben-Zahlen-Folgen BZF'),
    C('sv', W, 'Was misst der Index <b>Sprachverständnis (SV)</b> und wie funktioniert <b>Gemeinsamkeiten finden</b>?',
      '<b>Sprachverständnis:</b> Fähigkeit, <b>Sinn und Bedeutung von Lautäußerungen</b> zu erfassen. Beziehung zu Phonetik und Phonologie in der Linguistik sowie zu Kognitionspsychologie und Wahrnehmung in der Psychologie.<br><br><b>Gemeinsamkeiten finden (GF):</b> Gemeinsamkeiten von je <b>2 Wörtern</b> (Gegenstände/abstrakte Begriffe) finden, z. B. Rot – Grün, Fluss – Berg, Wütend – Fröhlich.',
      'Sprachverständnis SV Lautäußerungen Phonetik Phonologie Gemeinsamkeiten finden GF'),
    C('vg', W, 'Was misst der Index <b>Verarbeitungsgeschwindigkeit (VG)</b> und welcher Untertest gehört dazu?',
      '<b>Verarbeitungsgeschwindigkeit:</b> die <b>Menge an Bit</b>, die ein Lebewesen <b>pro Zeiteinheit</b> mit seinen Sinnesorganen aufnehmen und in seinem Gehirn verarbeiten kann.<br><br>Untertest: <b>Zahlen-Symbol-Test A</b>.',
      'Verarbeitungsgeschwindigkeit VG Bit Zeiteinheit Zahlen-Symbol-Test'),
    C('fs', W, 'Was misst der Index <b>Fluides Schlussfolgern (FS)</b> und welcher Untertest gehört dazu?',
      '<b>Fluides Schlussfolgern:</b> <b>simultane Verarbeitung von visuellen Reizen</b>; <b>induktives Denken</b>.<br><br>Untertest: <b>Formenwaage</b> (Waagen mit Formen; gesucht ist, was die letzte Waage ausgleicht; einfache und schwierige Aufgaben).',
      'Fluides Schlussfolgern FS simultan visuell induktives Denken Formenwaage'),
    C('vrv', W, 'Was misst der Index <b>Visuell-räumliche Verarbeitung (VRV)</b> und welcher Untertest gehört dazu?',
      '<b>Visuell-räumliche Verarbeitung:</b> Fähigkeit, <b>räumliche Beziehungen</b> zu erfassen; <b>abstrakt logisches Schließen</b>.<br><br>Untertest: <b>Mosaiktest</b> (rot-weiße Würfel nach Vorlage zu einem Muster legen).',
      'Visuell-räumliche Verarbeitung VRV räumliche Beziehungen Mosaiktest'),
    C('wisc-beobachtung', W, 'Worauf achtet man bei der <b>Verhaltensbeobachtung</b> während der WISC-Testung?',
      '<ul><li>Gründe für die Überweisung</li><li>Sprache</li><li>Körperliche Erscheinung</li><li>Aufmerksamkeit</li><li>Konzentration</li><li>Einstellung zur Testung</li><li>Affekt/Stimmungslage</li></ul>',
      'Verhaltensbeobachtung WISC Testung Überweisung Affekt Stimmungslage Einstellung'),
    C('auswertung', W, 'Wie läuft die <b>Auswertung des WISC</b> ab?',
      '<b>Umrechnung in Wertpunkte:</b><ol><li>Ermittlung der <b>Rohwerte</b></li><li>Umrechnung der Rohwerte in <b>Wertpunkte</b> (<b>altersnormiert</b>, über Normtabellen)</li><li>Berechnung der <b>Wertpunktsummen der Indizes</b></li></ol>Danach: Umrechnung in <b>Index-Werte</b> (<b>IQ-standardisiert</b>) und Ermittlung des <b>Gesamt-IQ</b> mit <b>Prozentrang</b> und <b>Vertrauensintervall</b> (90 % / 95 %).',
      'Auswertung Rohwerte Wertpunkte altersnormiert Normtabellen Indexwerte Gesamt-IQ Prozentrang Konfidenzintervall'),
    C('normtabelle', W, 'Warum braucht man <b>altersnormierte Normtabellen</b>? (Beispiel von der Folie)',
      'Der gleiche Rohwert ergibt je nach Alter unterschiedliche Wertpunkte. Beispiel Mosaik-Test (MT):<ul><li>Alter 8;0–8;3: Rohwert <b>39–42</b> → <b>13</b> Wertpunkte</li><li>Alter 14;0–14;3: Rohwert <b>38–41</b> → <b>8</b> Wertpunkte</li></ul>',
      'Normtabellen altersnormiert Rohwert Wertpunkte Alter Mosaik'),
    C('anna', W, 'Beispiel <b>Anna Musterkind</b> (11 J, 10 M, 13 T): Welche Indexwerte und welchen Gesamt-IQ hat sie?',
      '<table><tr><th>Index</th><th>WP-Summe</th><th>Indexwert</th><th>PR</th><th>KI</th></tr><tr><td>SV</td><td>30</td><td>127</td><td>96</td><td>117–132</td></tr><tr><td>VRV</td><td>27</td><td>119</td><td>90</td><td>109–125</td></tr><tr><td>FS</td><td>29</td><td>126</td><td>96</td><td>117–131</td></tr><tr><td>AGD</td><td>34</td><td>138</td><td>99</td><td>127–143</td></tr><tr><td>VG</td><td>35</td><td>144</td><td>99,8</td><td>130–148</td></tr><tr><td><b>G-IQ</b></td><td>106</td><td><b>136</b></td><td>99</td><td>129–140</td></tr></table>Mit 136 liegt sie über 130 (Bereich Hochbegabung).',
      'Beispiel Anna Musterkind Gesamt-IQ 136 Prozentrang Konfidenzintervall Indexwerte'),

    C('interview', I, 'Was sind <b>Interviews</b> in der Diagnostik und wofür werden sie eingesetzt?',
      '<b>Mündliche Informationsgewinnung mittels Gespräch</b>, z. B.:<ul><li><b>Anamnesen</b> (Sammlung von Informationen über eine Erkrankung oder Störung)</li><li>Einstellungs-/Auswahlgespräche</li></ul>Interviews unterscheiden sich nach dem <b>Grad ihrer Standardisierung</b>.',
      'Interview mündlich Gespräch Anamnese Einstellungsgespräch Auswahlgespräch Standardisierung'),
    C('standardisierung', I, 'Welche drei <b>Grade der Standardisierung</b> von Interviewfragen gibt es? (mit Beispiel)',
      '<ul><li><b>Unstandardisiert:</b> nur das Ziel (Diagnose) steht fest, Fragen ergeben sich im Laufe des Gesprächs. Initialfrage: „Warum sind Sie zu uns gekommen?“</li><li><b>Halbstandardisiert:</b> Standardisierung wird angestrebt, exakte Wortlaute sind aber nicht gewollt oder nicht möglich. Anweisung: „Fragen Sie nach Art, Dauer und Häufigkeit des Problems.“</li><li><b>Völlig standardisiert:</b> jede Frage ist genau festgelegt und immer im gleichen Wortlaut vorzutragen („Seit wann haben Sie diese Probleme?“); auch die <b>Antworten sind vorgegeben</b> (nie, selten, manchmal, oft, sehr oft).</li></ul>',
      'Standardisierung unstandardisiert halbstandardisiert völlig standardisiert Initialfrage Wortlaut'),
    C('standard-einsatz', I, 'Wo werden <b>völlig standardisierte</b> Interviews eingesetzt und wann sind sie sinnvoll?',
      'Häufig im <b>klinischen Bereich</b> und in der <b>Eignungsdiagnostik</b>.<br><br>Sinnvoll, wenn<ul><li>sich die Fragestellung <b>oft wiederholt</b></li><li>Ergebnisse <b>mit anderen Probanden verglichen</b> werden sollen</li></ul>',
      'völlig standardisiert klinisch Eignungsdiagnostik vergleichen wiederholt'),
    C('verwechslung', D, '<b>Verwechslungsgefahr</b> in Diagnostik Teil 1',
      '<ul><li><b>Time Sampling</b> = Zeitabschnitt, Häufigkeit ≠ <b>Event Sampling</b> = nur bei Verhalten X, Dauer, seltenes Verhalten</li><li><b>Platzierung</b> (von Schülern) ≠ <b>Selektion</b> (von Bedingungen/Maßnahmen)</li><li>Beobachterdrift: <b>Ermüdung → Abnahme</b>, <b>mangelnde Übung → Zunahme</b></li><li><b>Stern</b>: geistiges/reales Alter ≠ <b>Wechsler</b>: Mittelwert der Altersgruppe</li><li><b>Rohwert → Wertpunkte</b> (altersnormiert) <b>→ Indexwert</b> (IQ-standardisiert)</li><li><b>Nicht teilnehmend</b> = verdeckt, Beobachter nicht sichtbar ≠ <b>passiv teilnehmend</b> = anwesend, aber nicht Teil der Interaktion</li><li>Systematisch = quantitativ, hypothesengeleitet ≠ frei = qualitativ</li></ul>',
      'Verwechslungsgefahr Time Event Sampling Platzierung Selektion Stern Wechsler Wertpunkte'),
]

CARDS = {'d1': CARDS_D1}

# ---------------------------------------------------------------- Tests Teil 1
ITEMS = []
def add(**k): ITEMS.append(dict(k, src=S))

S = 'Diagnostik · Teil 1'

# Multiple Choice
add(id='pd-mc-01', type='mc', q='Was bedeutet das griechische Verb <b>„diagignoskein“</b>?',
    options=['messen, zählen, vergleichen', 'gründlich kennenlernen, entscheiden, beschließen', 'beobachten, aufschreiben, bewerten', 'heilen, behandeln, fördern'], correct=1,
    expl='Es bezeichnet einen kognitiven Vorgang vom <b>Erkennen bis zum Beschließen</b>.', kw='diagignoskein Begriff')
add(id='pd-mc-02', type='mc', q='Welche Definition des Gegenstands der Diagnostik stammt von <b>Kubinger (2009)</b>?',
    options=['Erfassen von inter- und intraindividuellen Unterschieden und Veränderungen', 'Sammeln von Informationen, die für das Verständnis menschlichen Verhaltens und Erlebens bedeutsam sind', 'Erfassen von psychischen Merkmalen von einem (oder mehreren) Menschen', 'Gesamtheit der zeitstabilen Merkmale eines Menschen'], correct=2,
    expl='Kubinger: psychische Merkmale. Inter-/intraindividuelle Unterschiede = Amelang &amp; Schmidt-Atzert; Informationen für das Verständnis = Eid &amp; Petermann; zeitstabile Merkmale = Pekrun (Persönlichkeit).', kw='Gegenstand Kubinger Definition')
add(id='pd-mc-03', type='mc', q='Zu welchem Entwicklungsbereich gehört <b>Gliederungsfähigkeit</b>?',
    options=['soziale Entwicklung', 'sprachliche Entwicklung', 'intellektuelle Entwicklung', 'motorische Entwicklung'], correct=2,
    expl='Intellektuell: Konzentration, Aufmerksamkeit, Gliederungsfähigkeit, Mengenerfassung, Arbeitsverhalten, Denkfähigkeit, Gedächtnis, Wahrnehmung.', kw='Aufgabenbereiche intellektuelle Entwicklung')
add(id='pd-mc-04', type='mc', q='Welche Merkmale gehören zur <b>gefühlsmäßigen (emotionalen) Entwicklung</b>?',
    options=['Kontaktfähigkeit, Konfliktfähigkeit', 'Motivation, Selbstvertrauen', 'Feinmotorik, Grobmotorik', 'Sprachfähigkeit, Sprachverständnis'], correct=1,
    expl='Kontakt/Konflikt = sozial, Motorik = motorisch, Sprache = sprachlich.', kw='emotionale Entwicklung Motivation Selbstvertrauen')
add(id='pd-mc-05', type='mc', q='Welches Beispiel ist ein <b>Umweltmerkmal aus dem Elternhaus</b>?',
    options=['Klassenklima', 'Unterrichtsqualität', 'sozioökonomischer Status', 'Gewissenhaftigkeit'], correct=2,
    expl='Elternhaus: elterliche Unterstützung, Familiengröße, sozioökonomischer Status. Klassenklima und Unterrichtsqualität = Schule; Gewissenhaftigkeit = Personenmerkmal.', kw='Umweltmerkmale Elternhaus')
add(id='pd-mc-06', type='mc', q='Nach <b>Pekrun (1988)</b> gehören zur Persönlichkeit die Merkmale, die …',
    options=['angeboren und unveränderlich sind', '(mindestens relativ) zeitstabil sind und einen von anderen unterscheiden', 'direkt beobachtbar sind', 'in allen Situationen gleich auftreten'], correct=1,
    expl='a) (mindestens relativ) zeitstabil und b) unterscheiden von anderen Menschen.', kw='Persönlichkeit Pekrun')
add(id='pd-mc-07', type='mc', q='„Bedingungen für die Aufrechterhaltung eines Fehlverhaltens“ gehört zu welchem Ziel des Messens?',
    options=['Beschreiben', 'Erklären', 'Vorhersagen', 'Platzieren'], correct=1,
    expl='Erklären: Ereignisse und Eigenschaften als Ursache; Bedingungen für Aufrechterhaltung eines Fehlverhaltens.', kw='Wozu Erklären Fehlverhalten')
add(id='pd-mc-08', type='mc', q='Worauf beziehen sich laut Folie <b>Selektionsmaßnahmen</b>?',
    options=['Auf Schüler', 'Auf Bedingungen / Maßnahmen', 'Auf Lehrkräfte', 'Auf Testverfahren'], correct=1,
    expl='Selektion von <b>Bedingungen/Maßnahmen</b>; Platzierung betrifft Schüler.', kw='Selektion Platzierung Entscheidungen')
add(id='pd-mc-09', type='mc', q='Was zählt <b>nicht</b> zu den vier diagnostischen Verfahren („Wie wird gemessen?“)?',
    options=['Verhaltensbeobachtung', 'Akteninformation', 'Interviews', 'Experimente'], correct=3,
    expl='Die vier Verfahren: Verhaltensbeobachtung, Testverfahren, Interviews, Akteninformation.', kw='Verfahren Wie gemessen')
add(id='pd-mc-10', type='mc', q='Ein Zielverhalten tritt nur <b>selten</b> auf, und du willst seine <b>Dauer</b> messen. Welche Stichprobe passt?',
    options=['Time Sampling', 'Event Sampling', 'Freie Beobachtung', 'Indirekte Beobachtung'], correct=1,
    expl='Event Sampling: beobachtet wird nur, wenn Verhalten X auftritt; Dauer messbar; sinnvoll bei seltenem Zielverhalten.', kw='Event Sampling selten Dauer')
add(id='pd-mc-11', type='mc', q='Was ist ein <b>Nachteil der freien</b> Beobachtung?',
    options=['Einübung der Beobachter nötig', 'Vorbereitungsaufwand', 'Aufwand und Ertrag wenig kalkulierbar', 'Erlaubt keine qualitativen Ergebnisse'], correct=2,
    expl='Frei: Ergebnisse wenig objektiv und messgenau; Aufwand und Ertrag wenig kalkulierbar. A und B sind Nachteile der systematischen Beobachtung.', kw='freie Beobachtung Nachteile')
add(id='pd-mc-12', type='mc', q='Der Beobachter ist anwesend, aber <b>nicht Teil der Interaktion</b>. Das ist …',
    options=['aktive teilnehmende Beobachtung', 'passive teilnehmende Beobachtung', 'nicht teilnehmende (verdeckte) Beobachtung', 'indirekte Beobachtung'], correct=1,
    expl='Passiv teilnehmend: anwesend, aber nicht Teil der Interaktion. Verdeckt: Beobachter nicht sichtbar.', kw='passive Teilnahme')
add(id='pd-mc-13', type='mc', q='Was ist ein <b>Vorteil der indirekten</b> Beobachtung?',
    options=['Standortwechsel möglich', 'Keine Verzerrung durch Erinnerung', 'Wiederholtes Ansehen möglich', 'Mehrere Perspektiven'], correct=2,
    expl='Indirekt (Video): Datenaggregation vor der Beurteilung, wiederholtes Ansehen, längere Verhaltensausschnitte. Nachteil: nur <b>eine</b> Perspektive.', kw='indirekte Beobachtung Vorteile Video')
add(id='pd-mc-14', type='mc', q='Was verursacht beim <b>Beobachterdrift</b> eine <b>Zunahme</b> entdeckter Ereignisse?',
    options=['Ermüdung', 'Nachlassende Aufmerksamkeit', 'Mangelnde Übung', 'Zu kurze Beobachtungsphasen'], correct=2,
    expl='Ermüdung/nachlassende Aufmerksamkeit → Abnahme; mangelnde Übung → Zunahme.', kw='Beobachterdrift Zunahme Übung')
add(id='pd-mc-15', type='mc', q='Wie lang sollten Beobachtungsphasen gegen Beobachterdrift <b>höchstens</b> sein?',
    options=['5 Minuten', '20 Minuten', '45 Minuten', '90 Minuten'], correct=1,
    expl='Angemessen lange Beobachtungsphasen: max. 20 Minuten, plus Beobachtertraining.', kw='Beobachterdrift 20 Minuten')
add(id='pd-mc-16', type='mc', q='Welche Testart misst <b>Konzentration und Aufmerksamkeit</b>?',
    options=['Entwicklungstests', 'Intelligenztests', 'Allgemeine Leistungstests', 'Schulleistungstests'], correct=2,
    expl='Allgemeine Leistungstests messen allgemeine Voraussetzungen von Leistung.', kw='allgemeine Leistungstests Konzentration')
add(id='pd-mc-17', type='mc', q='Ein 10-jähriges Kind hat ein geistiges Alter von 8 Jahren. IQ nach <b>Stern</b>?',
    options=['80', '90', '125', '108'], correct=0,
    expl='8 / 10 × 100 = 80.', kw='Stern IQ Formel')
add(id='pd-mc-18', type='mc', q='Welcher IQ-Bereich gilt als <b>überdurchschnittliche Begabung</b>?',
    options=['85–115', '100–115', '115–130', 'über 130'], correct=2,
    expl='85–115 normal, 115–130 überdurchschnittlich, über 130 Hochbegabung (M = 100, SD = 15).', kw='Normalverteilung überdurchschnittlich')
add(id='pd-mc-19', type='mc', q='Für welchen Altersbereich ist der <b>WISC-V</b>?',
    options=['3 bis 7 Jahre', '6 bis 16 Jahre, 11 Monate', '10 bis 18 Jahre', 'ab 16 Jahren'], correct=1,
    expl='WISC-V: Individualtest, 6 bis 16 Jahre 11 Monate, 5 Indizes mit 15 Untertests.', kw='WISC Altersbereich')
add(id='pd-mc-20', type='mc', q='Zu welchem WISC-V-Index gehört der <b>Mosaiktest</b>?',
    options=['Fluides Schlussfolgern', 'Visuell-räumliche Verarbeitung', 'Verarbeitungsgeschwindigkeit', 'Arbeitsgedächtnis'], correct=1,
    expl='Mosaiktest → VRV. Formenwaage → FS, Zahlen-Symbol-Test → VG, Buchstaben-Zahlen-Folgen → AGD.', kw='Mosaiktest VRV')
add(id='pd-mc-21', type='mc', q='Welcher Index wird u. a. mit <b>„Simultane Verarbeitung visueller Reize, induktives Denken“</b> beschrieben?',
    options=['Sprachverständnis', 'Visuell-räumliche Verarbeitung', 'Fluides Schlussfolgern', 'Verarbeitungsgeschwindigkeit'], correct=2,
    expl='FS: simultane Verarbeitung von visuellen Reizen, induktives Denken (Untertest Formenwaage).', kw='Fluides Schlussfolgern induktiv')
add(id='pd-mc-22', type='mc', q='Welche Kapazität hat das <b>Arbeitsgedächtnis</b> laut Folie?',
    options=['± 3 Einheiten', '± 7 Einheiten', '± 15 Einheiten', 'unbegrenzt'], correct=1,
    expl='Kurze Speicherung (ca. 30 Sek.), geringe Kapazität (± 7 Einheiten).', kw='Arbeitsgedächtnis Kapazität')
add(id='pd-mc-23', type='mc', q='Aufgabe Buchstaben-Zahlen-Folgen: <b>2-A-3</b>. Welche Antwort ist richtig?',
    options=['3-A-2', 'A-2-3', 'A-3-2', '2-A-3'], correct=1,
    expl='Richtig sind A-2-3 oder 2-3-A: Buchstaben und Zahlen jeweils geordnet.', kw='Buchstaben-Zahlen-Folgen')
add(id='pd-mc-24', type='mc', q='Was ist bei der WISC-Auswertung der <b>zweite</b> Schritt?',
    options=['Ermittlung der Rohwerte', 'Umrechnung der Rohwerte in altersnormierte Wertpunkte', 'Berechnung der Wertpunktsummen der Indizes', 'Ermittlung des Gesamt-IQ'], correct=1,
    expl='1. Rohwerte, 2. Wertpunkte (altersnormiert), 3. Wertpunktsummen der Indizes; danach Indexwerte und Gesamt-IQ.', kw='Auswertung Reihenfolge')
add(id='pd-mc-25', type='mc', q='Ein Interview, bei dem <b>nur das Ziel (Diagnose)</b> feststeht und sich die Fragen im Gespräch ergeben, ist …',
    options=['unstandardisiert', 'halbstandardisiert', 'völlig standardisiert', 'eine Anamnese'], correct=0,
    expl='Unstandardisiert, z. B. Initialfrage „Warum sind Sie zu uns gekommen?“', kw='unstandardisiert Interview')
add(id='pd-mc-26', type='mc', q='Wann ist ein <b>völlig standardisiertes</b> Interview sinnvoll?',
    options=['Wenn man ein Thema zum ersten Mal erkundet', 'Wenn Ergebnisse mit anderen Probanden verglichen werden sollen', 'Wenn exakte Wortlaute nicht möglich sind', 'Wenn nur das Ziel feststeht'], correct=1,
    expl='Sinnvoll, wenn sich die Fragestellung oft wiederholt und Ergebnisse verglichen werden sollen.', kw='völlig standardisiert sinnvoll')

# Richtig/Falsch
add(id='pd-tf-01', type='tf', statement='Ziel der pädagogischen Diagnostik ist, jeden Lernenden nach seinen Fähigkeiten fördern zu können.', answer=True,
    expl='Ziel: individuelles Lernen optimieren.', kw='Ziel fördern')
add(id='pd-tf-02', type='tf', statement='Klassenklima ist ein Personenmerkmal.', answer=False,
    expl='Klassenklima ist ein <b>Umweltmerkmal</b> (Schule).', kw='Klassenklima Umweltmerkmal')
add(id='pd-tf-03', type='tf', statement='Laut Folie ist Verhalten vollständig vorhersagbar, wenn man die Eigenschaften kennt.', answer=False,
    expl='Verhalten ist <b>nur zum Teil</b> vorhersagbar.', kw='Vorhersagen Verhalten')
add(id='pd-tf-04', type='tf', statement='Beim Beschreiben von Verhalten werden Eigenschaften als hypothetisches Konstrukt betrachtet.', answer=True,
    expl='Beschreiben: Eigenschaften als hypothetisches Konstrukt, Klassifikation.', kw='Beschreiben hypothetisches Konstrukt')
add(id='pd-tf-05', type='tf', statement='Zeugnisse und Tagebücher gehören zur Akteninformation.', answer=True,
    expl='Akteninformation: Zeugnisse, Tagebücher, Facebook …', kw='Akteninformation')
add(id='pd-tf-06', type='tf', statement='Beobachtung ist eine objektive Abbildung der Wirklichkeit.', answer=False,
    expl='Beobachtung ist ein Selektionsprozess und ein <b>aktiver Konstruktionsprozess</b>.', kw='Beobachtung Konstruktionsprozess')
add(id='pd-tf-07', type='tf', statement='Inferenzprozesse laufen im Alltag meist bewusst und kontrolliert ab.', answer=False,
    expl='Sie laufen in der Regel <b>automatisch</b> ab.', kw='Inferenz automatisch')
add(id='pd-tf-08', type='tf', statement='Time Sampling dient der Häufigkeitsregistrierung.', answer=True,
    expl='Wie oft tritt Verhalten X in einem bestimmten Zeitabschnitt auf?', kw='Time Sampling Häufigkeit')
add(id='pd-tf-09', type='tf', statement='Systematische Beobachtung ist hypothesengeleitet und liefert quantitative Ergebnisse.', answer=True,
    expl='Freie Beobachtung liefert dagegen oft qualitative Ergebnisse.', kw='systematische Beobachtung')
add(id='pd-tf-10', type='tf', statement='Nicht teilnehmende Beobachtung verändert die Situation nicht.', answer=True,
    expl='Vorteil; Nachteile: technischer Aufwand, meist fester Beobachtungsblickwinkel.', kw='nicht teilnehmend Vorteil')
add(id='pd-tf-11', type='tf', statement='Bei direkter Beobachtung gibt es keine Verzerrung durch Erinnerung.', answer=True,
    expl='Direkt: Standortwechsel möglich, keine Verzerrung durch Erinnerung.', kw='direkte Beobachtung Erinnerung')
add(id='pd-tf-12', type='tf', statement='Nonverbales Kommentieren (Lächeln, Kopfschütteln) durch den Beobachter fördert Reaktivität.', answer=True,
    expl='Angemessen ist neutrales, zurückhaltendes Verhalten.', kw='Reaktivität nonverbal')
add(id='pd-tf-13', type='tf', statement='Psychometrische Persönlichkeitstests zählen zu den Leistungstests.', answer=False,
    expl='Sie sind eine eigene Gruppe neben den Leistungstests (behandelt in der VL Persönlichkeitspsychologie).', kw='Persönlichkeitstests Leistungstests')
add(id='pd-tf-14', type='tf', statement='Alle IQ-Tests haben einen Mittelwert von 100 und eine Standardabweichung von 10.', answer=False,
    expl='M = 100, <b>SD = 15</b>.', kw='IQ Standardabweichung')
add(id='pd-tf-15', type='tf', statement='Wechsler setzt den IQ in Relation zum Mittelwert der Altersgruppe statt zum Lebensalter.', answer=True,
    expl='Das löst das Problem des Stern-IQ.', kw='Wechsler Altersgruppe')
add(id='pd-tf-16', type='tf', statement='Der WISC-V ist ein Gruppentest.', answer=False,
    expl='Der WISC-V ist ein <b>Individualtest</b>.', kw='WISC Individualtest')
add(id='pd-tf-17', type='tf', statement='Der WISC-V eignet sich zur Klärung der Ursachen von Leistungsproblemen wie Legasthenie und Dyskalkulie.', answer=True,
    expl='Diagnostik von Lernbehinderungen; außerdem sonderpädagogischer Förderbedarf und Hochbegabung.', kw='WISC Eignung Legasthenie Dyskalkulie')
add(id='pd-tf-18', type='tf', statement='Die Umrechnung von Rohwerten in Wertpunkte erfolgt altersnormiert.', answer=True,
    expl='Gleicher Rohwert → je nach Alter andere Wertpunkte (Normtabellen).', kw='Wertpunkte altersnormiert')
add(id='pd-tf-19', type='tf', statement='Bei einem völlig standardisierten Interview sind auch die Antworten vorgegeben.', answer=True,
    expl='z. B. nie, selten, manchmal, oft, sehr oft.', kw='völlig standardisiert Antworten')
add(id='pd-tf-20', type='tf', statement='Beim halbstandardisierten Interview muss jede Frage im exakt gleichen Wortlaut gestellt werden.', answer=False,
    expl='Standardisierung wird angestrebt, exakte Wortlaute sind aber <b>nicht gewollt oder nicht möglich</b>.', kw='halbstandardisiert Wortlaut')

# Lückentext
add(id='pd-gap-01', type='gap', text='Diagnostik bezeichnet einen kognitiven Vorgang vom {{Erkennen}} bis zum {{Beschließen}}.',
    expl='Griechisch „diagignoskein“.', kw='diagignoskein Erkennen Beschließen')
add(id='pd-gap-02', type='gap', text='Ziel der Diagnostik: {{individuelles}} Lernen optimieren.',
    expl='Jeden Lernenden nach seinen Fähigkeiten fördern.', kw='Ziel individuelles Lernen')
add(id='pd-gap-03', type='gap', text='Personenmerkmale sind Verhalten und Eigenschaften, also die {{Persönlichkeit}}.',
    expl='Gegenüber stehen Umweltmerkmale (Schule, Elternhaus).', kw='Personenmerkmale Persönlichkeit')
add(id='pd-gap-04', type='gap', text='Die Schlussfolgerung einer Lehrkraft aus ihren Beobachtungen heißt {{Inferenz}}.',
    expl='Inferenzprozesse laufen im Alltag meist automatisch ab.', kw='Inferenz')
add(id='pd-gap-05', type='gap', text='Beobachtung ist immer ein {{Selektionsprozess|Selektions-prozess}}: nicht alles Wahrnehmbare wird beobachtet.',
    expl='Im Alltag fallen oft erwartungswidrige Verhaltensweisen auf.', kw='Selektionsprozess')
add(id='pd-gap-06', type='gap', text='Nicht teilnehmende Beobachtung nennt man auch {{verdeckte}} Beobachtung.',
    expl='Der Beobachter ist nicht sichtbar.', kw='verdeckte Beobachtung')
add(id='pd-gap-07', type='gap', text='Fühlen sich Beobachtete durch den Beobachter gestört, spricht man von {{Reaktivität}}.',
    expl='Nachteil teilnehmender Beobachtung.', kw='Reaktivität')
add(id='pd-gap-08', type='gap', text='Indirekte Beobachtung erfolgt zeitversetzt durch {{Videoaufnahmen|Video|Videos}}.',
    expl='Direkte Beobachtung ist zeitgleich.', kw='indirekte Beobachtung Video')
add(id='pd-gap-09', type='gap', text='IQ nach Stern = geistiges Alter / {{reales Alter|Lebensalter|reales}} × 100.',
    expl='Stern (1912).', kw='Stern IQ Formel')
add(id='pd-gap-10', type='gap', text='Der WISC-V hat {{5|fünf}} Indizes mit {{15|fünfzehn}} Untertests.',
    expl='SV, VRV, FS, AGD, VG → Gesamt-IQ.', kw='WISC Indizes Untertests')
add(id='pd-gap-11', type='gap', text='Der Untertest Formenwaage gehört zum Index {{Fluides Schlussfolgern|FS}}.',
    expl='Mosaiktest → VRV, Zahlen-Symbol-Test → VG, Buchstaben-Zahlen-Folgen → AGD, Gemeinsamkeiten finden → SV.', kw='Formenwaage FS')
add(id='pd-gap-12', type='gap', text='Den Gesamt-IQ gibt man mit {{Prozentrang}} und Vertrauensintervall an.',
    expl='Indexwerte sind IQ-standardisiert.', kw='Gesamt-IQ Prozentrang')
add(id='pd-gap-13', type='gap', text='Die Sammlung von Informationen über eine Erkrankung oder Störung heißt {{Anamnese}}.',
    expl='Eine Form des Interviews.', kw='Anamnese')
