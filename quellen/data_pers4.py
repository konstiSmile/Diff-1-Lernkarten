# Psycho 2 · Persönlichkeitspsychologie · Teil 4, geteilt in Kap. 4a (Persönlichkeitserfassung) und 4b (Schülerpersönlichkeit)
# Quelle: Zusammenfassung_PersPsych_Teil1-5.md, Teil 4. Klärungen von Konsti (21. Nov. 2026, Chat 1.15):
# - Prüfungsangst: Zusammenhang Angst–Leistung (Folie „U-förmig“, Grafik umgekehrtes U) nur auf der Karte, nicht abfragen.
# - Entwicklungsverläufe: Richtung abfragen; Klassenstufen nur, wo sie als Text auf der Folie stehen.
# - Liste unter der Grafik zur Lernzielorientierung (ohne Überschrift): nur zeigen, nicht abfragen.
# - Nur auf Karten: Tabelle Intelligenz × Schicht/Noten, Pfadmodell-Zahlen, Amelang-Werte, Schilling-d-Werte,
#   Pfeildicke bei Helmke, Details der NEO-FFI-Auswertung. Wechsler ohne Lebensdaten (Folie: 1886, richtig 1896).
# - Beispielaufgaben Wortschatz/Analogien gelten als kristallin (Überschrift der Folie).
# MC im echten Klausurformat: genau 4 Optionen, 1–4 richtig. Richtige Optionen sind unten mit „*“ markiert.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

def H(t):
    return '<p><i>Hinweis (nicht auf der Folie): ' + t + '</i></p>'

ER = 'Teil 4 · Persönlichkeitserfassung'
SP = 'Teil 4 · Schülerpersönlichkeit'
IN = 'Teil 4 · Intelligenz'
SK = 'Teil 4 · Fähigkeitsselbstkonzept'
SW = 'Teil 4 · Selbstwirksamkeit'
PA = 'Teil 4 · Prüfungsängstlichkeit'
ZO = 'Teil 4 · Zielorientierung'

# ---------------------------------------------------------------- Kapitel 4a
CARDS_K4A = [
    C('methoden-1', ER, 'Methoden der Persönlichkeitserfassung (1/2): <b>Inventare, Fremdratings, Nominationen, Interviews, Verhaltensbeobachtungen</b> – welche Beispiele nennt die Folie?',
      '<table><tr><th>Methode</th><th>Beispiele</th></tr><tr><td><b>Persönlichkeitsinventare</b></td><td>MMPI, NEO-FFI, 16PF</td></tr><tr><td><b>Fremdratings</b></td><td>durch Partner, Eltern, Fachleute</td></tr><tr><td><b>Nominationen</b></td><td>durch Klassenkameraden</td></tr><tr><td><b>Interviews</b></td><td>klinische Interviews, Typ-A-strukturiertes Interview</td></tr><tr><td><b>Verhaltensbeobachtungen</b></td><td>stichprobenartige Beobachtung, Videoaufzeichnungen</td></tr></table>',
      'Methoden Persönlichkeitserfassung Inventar MMPI NEO-FFI 16PF Fremdrating Nomination Interview Typ-A Verhaltensbeobachtung Video'),
    C('methoden-2', ER, 'Methoden der Persönlichkeitserfassung (2/2): <b>Dokumente, Biologie, Ausdruck, Demografie, projektive Tests</b> – welche Beispiele nennt die Folie?',
      '<table><tr><th>Methode</th><th>Beispiele</th></tr><tr><td><b>Dokumentenanalyse</b></td><td>Psychobiographie, Traumtagebücher</td></tr><tr><td><b>Biologische Messungen</b></td><td>Reaktionszeit, Hautleitfähigkeit, EEG, PET</td></tr><tr><td><b>Analyse des Ausdrucksverhaltens</b></td><td>Sprechgeschwindigkeit, Gesten, interpersonelle Distanz</td></tr><tr><td><b>Demografische und Lifestyle-Angaben</b></td><td>Alter, kulturelle Gruppe, politische Orientierung</td></tr><tr><td><b>Projektive Tests</b></td><td>Mann-Zeichen-Test, TAT, Rorschach</td></tr></table><p>Zusammen mit Teil 1/2 sind es <b>10 Verfahren</b>.</p>',
      'Dokumentenanalyse Psychobiographie Traumtagebuch biologische Messung EEG PET Hautleitfähigkeit Ausdrucksverhalten Gesten Distanz demografisch Lifestyle projektiv Rorschach TAT Mann-Zeichen-Test'),
    C('selbst', ER, 'Wie funktioniert eine <b>Selbsteinschätzung</b> mit einem Persönlichkeitsinventar?',
      '<p>Die Person schätzt sich <b>selbst</b> ein: entweder, ob Aussagen <b>generell richtig oder falsch</b> sind, oder als <b>abgestufte Zustimmung/Ablehnung</b> zu Fragen und Stellungnahmen.</p><p>Inventare erfassen meist <b>mehrere Persönlichkeitsdimensionen (Skalen)</b>. Die Ausprägungen ergeben zusammen ein <b>Muster der Persönlichkeit = Persönlichkeitsprofil</b>.</p>',
      'Selbsteinschätzung Persönlichkeitsinventar Skalen Persönlichkeitsprofil Zustimmung'),
    C('neo-n', ER, 'NEO-FFI: Welche <b>Facetten</b> hat <b>Neurotizismus</b>? Beispielitem?',
      '<p>Ängstlichkeit, Reizbarkeit, Depression, soziale Befangenheit, <b>Impulsivität</b>, Verletzlichkeit.</p><p>Item: „Ich fühle mich oft angespannt und nervös.“</p>',
      'NEO-FFI Neurotizismus Facetten Ängstlichkeit Reizbarkeit Depression Befangenheit Impulsivität Verletzlichkeit'),
    C('neo-e', ER, 'NEO-FFI: Welche <b>Facetten</b> hat <b>Extraversion</b>? Beispielitem?',
      '<p>Herzlichkeit, Geselligkeit, Durchsetzungsfähigkeit, Aktivität, Erlebnishunger, Frohsinn.</p><p>Item: „Ich habe gern viele Leute um mich herum.“</p>',
      'NEO-FFI Extraversion Facetten Herzlichkeit Geselligkeit Durchsetzungsfähigkeit Aktivität Erlebnishunger Frohsinn'),
    C('neo-a', ER, 'NEO-FFI: Welche <b>Facetten</b> hat <b>Verträglichkeit</b> (Agreeableness)? Beispielitem?',
      '<p>Vertrauen, Freimütigkeit, Altruismus, Entgegenkommen, Bescheidenheit, Gutherzigkeit.</p><p>Item: „Ich versuche zu jedem, dem ich begegne, freundlich zu sein.“</p>',
      'NEO-FFI Verträglichkeit Agreeableness Facetten Vertrauen Freimütigkeit Altruismus Entgegenkommen Bescheidenheit Gutherzigkeit'),
    C('neo-c', ER, 'NEO-FFI: Welche <b>Facetten</b> hat <b>Gewissenhaftigkeit</b>? Beispielitem?',
      '<p>Kompetenz, Ordnungsliebe, Pflichtbewusstsein, Leistungsstreben, Selbstdisziplin, Besonnenheit.</p><p>Item: „Ich arbeite hart, um meine Ziele zu erreichen.“</p>',
      'NEO-FFI Gewissenhaftigkeit Facetten Kompetenz Ordnungsliebe Pflichtbewusstsein Leistungsstreben Selbstdisziplin Besonnenheit'),
    C('neo-o', ER, 'NEO-FFI: Welche <b>Facetten</b> hat <b>Offenheit für Erfahrungen</b>? Beispielitem?',
      '<p>Offenheit für Fantasie, Ästhetik, Gefühle, Handlungen, Ideen; Offenheit des Werte- und Normensystems.</p><p>Item: „Ich finde philosophische Diskussionen langweilig.“ – ein <b>invertiertes Item</b> (Zustimmung spricht für <b>niedrige</b> Offenheit).</p>',
      'NEO-FFI Offenheit Facetten Fantasie Ästhetik Gefühle Handlungen Ideen Werte Normen invertiertes Item philosophische Diskussionen'),
    C('neo-auswertung', ER, 'Wie wird der <b>NEO-FFI</b> beantwortet und ausgewertet (Antwortbogen)?',
      '<p>Antwortskala: <b>SA</b> (starke Ablehnung), <b>A</b> (Ablehnung), <b>N</b> (neutral), <b>Z</b> (Zustimmung), <b>SZ</b> (starke Zustimmung).</p><p>Punkte <b>0–4</b> pro Item; <b>invertierte Items werden umgekehrt gepunktet</b>. Die Items werden den fünf Faktoren zugeordnet.</p><p>Details der Auswertung stehen nur als Abbildung auf der Folie.</p>',
      'NEO-FFI Auswertung Antwortbogen SA A N Z SZ Punkte invertiert'),
    C('neo-profile', ER, 'NEO-FFI-Profile: Was ist am <b>Profil von Anna</b> und am <b>Profil der Klasse 4a</b> jeweils typisch?',
      '<ul><li><b>Profil von Anna</b>: eine Person, viele Merkmale → <b>idiografisch</b>.</li><li><b>Profil der Klasse 4a</b>: Gruppenmittelwerte → <b>nomothetisch</b>.</li></ul><p>Skala 0–4 für die fünf Faktoren.</p>',
      'NEO-FFI Profil Anna Klasse 4a idiografisch nomothetisch'),
    C('selbst-vorzuege', ER, 'Welche <b>Vorzüge</b> haben Selbsteinschätzungen?',
      '<ul><li>Erfassung von <b>vergangenem oder nicht beobachtbarem Verhalten</b> möglich</li><li><b>Ökonomie</b> (minimale Kosten, viele Personen befragbar)</li><li><b>Anonymität</b></li></ul>',
      'Selbsteinschätzung Vorzüge Ökonomie Anonymität vergangenes Verhalten'),
    C('selbst-probleme', ER, 'Welche <b>Probleme</b> haben Selbsteinschätzungen? Was sind <b>Response-Sets</b>?',
      '<ul><li>Unvollständige Antworten, <b>Rücklaufquoten</b></li><li><b>Mangelnde Übereinstimmung</b> von mitgeteilten Einstellungen und tatsächlichem Verhalten</li><li><b>Systematische, verzerrende Antworttendenzen</b>, Täuschungsversuche</li><li><b>Response-Sets</b>: Tendenz zur <b>Bejahung</b> (Ja-Sage-Tendenz), zu <b>ungewöhnlichen Antworten</b>, zu <b>sozialer Erwünschtheit</b></li></ul>',
      'Selbsteinschätzung Probleme Rücklaufquote Antworttendenzen Täuschung Response-Sets Ja-Sage-Tendenz soziale Erwünschtheit'),
    C('fremd', ER, 'Was ist ein <b>Fremdrating</b>? Welches Problem hat es?',
      '<p><b>Einschätzung des Verhaltens einer Person X durch eine Person Y</b> auf vorgegebenen Skalen. Y kennt X meist <b>gut</b>.</p><p>Problem: <b>Beurteilungsfehler</b>.</p>',
      'Fremdrating Fremdeinschätzung Beurteilungsfehler'),
    C('fehler', ER, 'Welche drei <b>Beurteilungsfehler</b> nennt die Folie?',
      '<ul><li><b>Halo-Effekt</b>: Von einem <b>hervorstechenden Merkmal</b> wird auf <b>andere Persönlichkeitsmerkmale</b> geschlossen.</li><li><b>Fehler der zentralen Tendenz</b>: <b>Vermeiden der Extreme</b>, Einschätzungen vor allem im <b>mittleren Bereich</b>.</li><li><b>Reihenfolge-Effekte</b>: Beim Zusammenfügen von Einzelbeobachtungen zu einem Gesamteindruck wirken der <b>erste Eindruck (Primacy-Effekt)</b> und die <b>letzte Beobachtung (Recency-Effekt)</b> besonders.</li></ul>',
      'Beurteilungsfehler Halo-Effekt zentrale Tendenz Reihenfolge-Effekt Primacy Recency'),
    C('amelang', ER, 'Wie gut stimmen <b>Selbst- und Bekanntenurteil</b> überein (Amelang, 1989)?',
      '<table><tr><th>Bekannte ↓ / Selbst →</th><th>verbal</th><th>abstrakt-theor.</th><th>sozial</th></tr><tr><td>verbal</td><td><b>.38</b></td><td>.06</td><td>−.08</td></tr><tr><td>abstrakt-theor.</td><td></td><td><b>.27</b></td><td></td></tr><tr><td>sozial</td><td>.04</td><td>−.11</td><td><b>.28</b></td></tr></table><p>Für <b>dasselbe</b> Merkmal (Diagonale) nur <b>mäßige</b> Übereinstimmung, für <b>verschiedene</b> Merkmale <b>nahe null</b>.</p>',
      'Amelang Selbsturteil Bekanntenurteil Übereinstimmung Intelligenz soziale Kompetenz'),
    C('nomination', ER, 'Wie funktioniert eine <b>Nomination</b>?',
      '<p>Eine Person wird von <b>vielen verschiedenen Personen</b> beurteilt. <b>Wert = prozentuale Häufigkeit der Nominationen.</b></p><p>Beispiel: Klasse mit 30 Kindern, 15 nennen Paul als Kind, das nicht still sitzen kann → Paul erhält <b>50 %</b>.</p>',
      'Nomination Prozent Häufigkeit Paul still sitzen'),
    C('nomination-bewertung', ER, 'Welche <b>Vor- und Nachteile</b> haben Nominationen?',
      '<ul><li><b>Vorteil</b>: viele Beurteiler → <b>Reduktion systematischer Beurteilungsfehler</b>.</li><li>Verzerrungen sind aber <b>nicht ausgeschlossen</b> (auch viele können sich systematisch irren).</li><li><b>Nachteile</b>: <b>sehr aufwändig</b>, <b>auf Beobachtbares beschränkt</b>.</li></ul>',
      'Nomination Vorteil Nachteil aufwändig Beobachtbares Beurteilungsfehler'),
    C('verwechslung', ER, '<b>Verwechslungsgefahr</b> Kap. 4a',
      '<ul><li><b>Halo</b> (von einem Merkmal auf andere schließen) ≠ <b>zentrale Tendenz</b> (Mitte bevorzugen) ≠ <b>Reihenfolge</b> (Primacy = erster Eindruck, Recency = letzte Beobachtung).</li><li><b>Fremdrating</b> (ein Beurteiler, kennt X gut) ≠ <b>Nomination</b> (viele Beurteiler, Prozentwert).</li><li><b>Response-Sets</b> betreffen die <b>Selbsteinschätzung</b>, Beurteilungsfehler das <b>Fremdrating</b>.</li><li>NEO-FFI: <b>Impulsivität</b> gehört zu <b>Neurotizismus</b>, <b>Erlebnishunger</b> zu <b>Extraversion</b>, <b>Altruismus</b> zu <b>Verträglichkeit</b>, <b>Besonnenheit</b> zu <b>Gewissenhaftigkeit</b>.</li><li>Profil einer Person = <b>idiografisch</b>, Klassenprofil = <b>nomothetisch</b>.</li></ul>',
      'Verwechslung Halo zentrale Tendenz Fremdrating Nomination Response-Sets Facetten'),
]

# ---------------------------------------------------------------- Kapitel 4b
CARDS_K4B = [
    C('fragen', SP, 'Welche <b>zwei zentralen Fragen</b> stellt die Forschung zur Schülerpersönlichkeit?',
      '<ol><li>Wie wird die <b>Entwicklung der Persönlichkeit durch die Schule</b> (als <b>Sozialisationsinstanz</b>) und durch das <b>Erziehungsverhalten der Lehrkräfte</b> beeinflusst?</li><li>Welchen Einfluss hat die <b>Persönlichkeit der Schüler</b> auf deren <b>Schulleistung</b>?</li></ol>',
      'Schülerpersönlichkeit Fragen Sozialisationsinstanz Schulleistung'),
    C('merkmale', SP, 'Welche wichtigen <b>Merkmale der Schülerpersönlichkeit</b> nennt die Folie?',
      '<ul><li><b>kognitiv/evaluativ</b>: Intelligenz, Fähigkeitsselbstkonzept, Selbstwirksamkeitserwartung, Kontrollerwartungen</li><li><b>emotional/motivational</b>: Prüfungsängstlichkeit als Personenmerkmal, Leistungs- und Lernmotivation, Zielorientierung</li></ul>',
      'Schülerpersönlichkeit Merkmale kognitiv evaluativ emotional motivational'),
    C('implizit', SP, 'Implizite Persönlichkeitstheorie von Lehrkräften (Höhn, 1967): Wie werden <b>gute</b> und <b>schlechte</b> Schüler beschrieben?',
      '<ul><li><b>Schlechter Schüler</b>: faul, dumm, frech, angeberisch, unaufmerksam, unordentlich, unangepasst, <b>milieubelastet</b>.</li><li><b>Guter Schüler</b>: fleißig, ehrlich, ordentlich, angepasst, <b>milieubegünstigt</b>.</li></ul>',
      'implizite Persönlichkeitstheorie Lehrkräfte Höhn guter schlechter Schüler milieubelastet'),
    C('hofer', SP, 'Nach welchen <b>vier Dimensionen</b> beurteilen Lehrkräfte Schüler (Hofer, 1986)?',
      '<ol><li><b>intellektuelle Ausstattung</b></li><li><b>Motivation</b> (Fleiß, Ehrgeiz)</li><li><b>soziales Verhalten</b></li><li><b>emotionale Stabilität</b></li></ol>',
      'Beurteilungsdimensionen Hofer intellektuell Motivation sozial emotionale Stabilität'),
    C('kleber', SP, 'Woran beurteilen Lehrkräfte <b>Intelligenz</b> (Kleber, 1992)?',
      '<ul><li>Merkmale nach einer <b>fundierten Theorie</b> (grüne Pfeile): sprachliche Gewandtheit, rechnerische Leistungen, abstraktes Denken, Erinnerungsvermögen, Problemlösefähigkeiten, Verarbeitungsgeschwindigkeit.</li><li>Merkmale nach einer <b>nicht fundierten impliziten Theorie</b> (rote Pfeile): wacher Gesichtsausdruck, Durchsetzungsvermögen, Ordentlichkeit, hohe Stirn, geordnetes Elternhaus, macht Hausaufgaben.</li></ul>',
      'Kleber Intelligenz Lehrkräfte fundiert nicht fundiert implizite Theorie hohe Stirn Gesichtsausdruck'),
    C('int-def', IN, 'Wie definiert <b>Wechsler</b> Intelligenz?',
      'Intelligenz ist die <b>zusammengesetzte oder globale Fähigkeit</b> des Individuums, <b>zweckvoll zu handeln, vernünftig zu denken und sich mit seiner Umgebung wirkungsvoll auseinanderzusetzen</b>.',
      'Wechsler Intelligenz Definition zweckvoll handeln vernünftig denken Umgebung'),
    C('int-was', IN, 'Was <b>ist</b> Intelligenz – und was <b>nicht</b>?',
      '<ul><li><b>Ist</b>: denkgestütztes Lösen von neuen Aufgaben und Problemen, <b>schlussfolgerndes Denken</b>, <b>Abstraktionsvermögen</b>, Verständnis und Einsicht, Erkennen und Herstellen von <b>Struktur und Bedeutung</b>.</li><li><b>Ist nicht</b>: <b>Erfolg, Wissen, Kompetenz, Talent</b>.</li></ul>',
      'Intelligenz schlussfolgerndes Denken Abstraktion Struktur nicht Erfolg Wissen Kompetenz Talent'),
    C('int-verteilung', IN, 'Wie ist <b>Intelligenz verteilt</b> (IQ: M = 100, SD = 15)?',
      '<table><tr><th>Bereich</th><th>IQ</th><th>Anteil</th></tr><tr><td>Minderbegabung</td><td>unter 70</td><td>2,2 % (+ 0,1 %)</td></tr><tr><td>unterdurchschnittlich</td><td>70–85</td><td>13,6 %</td></tr><tr><td>normale Begabung</td><td>85–115</td><td>34,1 % + 34,1 % = <b>68,2 %</b></td></tr><tr><td>überdurchschnittlich</td><td>115–130</td><td>13,6 %</td></tr><tr><td>Hochbegabung</td><td>über 130</td><td>2,2 % (+ 0,1 %)</td></tr></table><p>Prozentränge: IQ 70 ≈ 2,3 · 85 ≈ 15,9 · 100 = 50 · 115 ≈ 84,1 · 130 ≈ 97,7.</p>',
      'Intelligenz Verteilung Normalverteilung IQ 100 15 Hochbegabung Minderbegabung 68,2 Prozentrang'),
    C('stern-guthke', IN, 'Welche <b>paradigmenübergreifenden Annahmen</b> zur Intelligenz nennen Stern &amp; Guthke (2001)?',
      '<ol><li>Intelligenz ist ein <b>stabiles Persönlichkeitsmerkmal</b>.</li><li><b>Mindestens 50 % der Varianz</b> in Intelligenztestleistungen sind – wo Kindern weitgehend alle Lerngelegenheiten offenstehen – <b>genetisch erklärbar</b>.</li><li>Intelligenzunterschiede haben eine <b>zerebrale Grundlage</b>, die weitgehend aufgeklärt werden kann.</li><li>Der <b>kulturelle und individuelle Kontext</b> entscheidet, wie kognitive Fähigkeiten Aneignung und Nutzung von Wissen beeinflussen.</li></ol>',
      'Stern Guthke Annahmen Intelligenz stabil genetisch 50 Prozent zerebral Kontext'),
    C('spearman', IN, 'Was besagt die <b>Generalfaktoren-Theorie</b> von Spearman?',
      '<ul><li>Intelligenz wird auf einen <b>Generalfaktor (g)</b> zurückgeführt; <b>spezielle Fähigkeiten (s)</b> erklären Unterschiede in einzelnen Subtests (z. B. räumliches Denken vs. Verstehen von Begriffen).</li><li>Begründung: Viele unterschiedliche Intelligenzaufgaben <b>korrelieren</b>, aber nur <b>mittelhoch</b>.</li><li>Beispiel für eine Aufgabe mit <b>hoher g-Ladung</b>: eine <b>Matrizenaufgabe</b> (fehlende Figur im 3×3-Raster ergänzen).</li></ul><p>Charles Spearman (1863–1945).</p>',
      'Spearman Generalfaktor g s spezielle Fähigkeiten Matrizen g-Ladung'),
    C('gf-gc', IN, 'Was unterscheidet <b>fluide (Gf)</b> und <b>kristalline (Gc)</b> Intelligenz nach Cattell?',
      '<table><tr><th></th><th>Fluide (Gf)</th><th>Kristalline (Gc)</th></tr><tr><td>Herkunft</td><td><b>angeboren bzw. vererbt</b>, laut Folie nicht durch die Umwelt beeinflussbar (ähnlich dem g-Faktor)</td><td><b>im Laufe des Lebens erlernt</b>, durch die Umwelt bestimmt</td></tr><tr><td>Inhalt</td><td>geistige Kapazität, Auffassungsgabe, generelles Verarbeitungsniveau</td><td><b>explizites Wissen</b> (semantisch, episodisch, z. B. Fakten) und <b>implizit Gelerntes</b> (Verhaltensweisen, Fahrradfahren, Rechnen)</td></tr></table><p>Die <b>kristalline ist von der fluiden Intelligenz abhängig</b>. Raymond B. Cattell (1905–1998).</p>',
      'fluide kristalline Intelligenz Gf Gc Cattell angeboren erlernt Wissen abhängig'),
    C('gc-aufgaben', IN, 'Welche <b>Beispielaufgaben</b> zur kristallinen Intelligenz zeigt die Folie?',
      '<ul><li><b>Wortschatz</b>: „Welches Wort passt in der Bedeutung nicht zu den anderen? Hose, Wolle, Kleid, Jacke“</li><li><b>Verbale Analogien</b>: „Saft zu Milch wie Apfel zu ? – Frucht, Obst, Banane, Boskop“</li></ul><p>Die Aufgaben stehen unter der Überschrift „Beispielaufgaben zur Erfassung der kristallinen Intelligenz“ (der Folientitel davor nennt auch „fluide“).</p>',
      'kristalline Intelligenz Beispielaufgaben Wortschatz verbale Analogien'),
    C('chc', IN, 'Was ist das <b>Cattell-Horn-Carroll-Modell (CHC)</b>?',
      '<ul><li><b>Aktuelles Intelligenzmodell</b> (Mehrfaktorentheorie), 1997 von Kevin McGrew entwickelt.</li><li>Basiert auf <b>Cattell</b> (Gf-Gc-Modell), <b>Horn</b> (erweitertes Gf-Gc-Modell) und <b>Carroll</b> (Drei-Schichten-Modell, 1993).</li><li>Intelligenz ist <b>hierarchisch</b> organisiert, <b>drei Schichten</b>: genereller Faktor <b>G</b> (Schicht III) → <b>Unterfaktoren</b> (Schicht II) → <b>spezifische Fähigkeiten</b> (Schicht I).</li><li><b>Offen für Erweiterungen</b> der Unterfaktoren und Fähigkeiten.</li></ul>',
      'CHC Cattell Horn Carroll McGrew hierarchisch drei Schichten Mehrfaktorentheorie'),
    C('chc-faktoren', IN, 'Welche <b>breiten Faktoren</b> (Schicht II) zeigt die Abbildung zum CHC-Modell?',
      'Fluide Intelligenz (Gf), Kristalline Intelligenz (Gc), Kurzzeitgedächtnis (Gsm), Visuelle Verarbeitung (Gv), Auditive Verarbeitung (Ga), Langzeitgedächtnis (Glr), Verarbeitungsgeschwindigkeit (Gs), Reaktionsgeschwindigkeit (Gt), Quantitatives Wissen (Gq), Lesen und Schreiben (Grw).',
      'CHC Faktoren Gf Gc Gsm Gv Ga Glr Gs Gt Gq Grw'),
    C('int-entwicklung', IN, 'Wie <b>entwickelt</b> sich Intelligenz?',
      '<ul><li><b>Anstieg bis nach Schulende</b>, Maximum mit ca. <b>Mitte 20</b>.</li><li><b>Prädizierbar ab ca. der 3. Klasse</b>, davor instabil.</li><li>Zu ca. <b>60–70 % genetisch bedingt</b>.</li></ul>' + H('Laut Grafik sinkt die Verarbeitungsgeschwindigkeit früher ab als die kristalline Intelligenz; die genauen Kurven sind nicht prüfungsrelevant.'),
      'Intelligenz Entwicklung Mitte 20 prädizierbar 3. Klasse genetisch 60 70'),
    C('int-schicht', IN, 'Wie hängen Intelligenz, <b>soziale Schicht</b> und <b>Schulnoten</b> zusammen (Tabelle)?',
      '<table><tr><th>Alter</th><th>verbal × nonverbal</th><th>Schicht × verbal</th><th>Schicht × nonverbal</th><th>Noten × verbal</th><th>Noten × nonverbal</th></tr><tr><td>5–6</td><td>.38</td><td>.19</td><td>.18</td><td>–</td><td>–</td></tr><tr><td>7–8</td><td>.44</td><td>.36</td><td>.12</td><td>–</td><td>–</td></tr><tr><td>9–10</td><td>.50</td><td>.35</td><td>.14</td><td>−.50</td><td>−.48</td></tr><tr><td>11–12</td><td>.43</td><td>.33</td><td>.16</td><td>–</td><td>–</td></tr></table><p>Die Werte sind auf der Folie teilweise unklar zugeordnet.</p>' + H('Die Korrelation mit Schulnoten ist negativ, weil in Deutschland eine niedrigere Note besser ist.'),
      'Intelligenz soziale Schicht Schulnoten Korrelation verbal nonverbal'),
    C('fsk-def', SK, 'Was ist das <b>Fähigkeitsselbstkonzept</b>?',
      'Die Einschätzung, <b>wie gut eine Person nach eigener Einschätzung bei einer bestimmten Aktivität ist</b>. Es spiegelt <b>Erwartungen für zukünftige Leistungen</b> wider, auch im Sinne von Selbstwirksamkeitserwartungen.',
      'Fähigkeitsselbstkonzept Definition eigene Einschätzung Erwartungen'),
    C('fsk-ebenen', SK, 'Welche <b>Spezifitätsebenen</b> des Selbstkonzepts gibt es?',
      '<ol><li><b>Selbstkonzept</b> (allgemein): Gesamtheit der auf das Individuum bezogenen Gedanken/Gefühle – „Ich bin zufrieden mit mir.“</li><li><b>Schulisches Fähigkeitsselbstkonzept</b>: „Ich bin ein guter Schüler.“</li><li><b>Schulfach-/domänenspezifisches</b> Fähigkeitsselbstkonzept: „Ich bin gut in Mathe.“</li></ol><p>Hierarchie: Selbstkonzept → Körper, Schulleistungen, Emotional, Sozial → Schulleistungen mathematisch/verbal → schulfachspezifisch → anforderungsspezifisch → <b>Selbstwirksamkeit = aufgabenspezifisch</b> (am spezifischsten).</p>',
      'Selbstkonzept Spezifitätsebenen schulisch domänenspezifisch Hierarchie Selbstwirksamkeit aufgabenspezifisch'),
    C('fsk-entwicklung', SK, 'Wie <b>entwickelt</b> sich das Fähigkeitsselbstkonzept in der Schulzeit?',
      '<ul><li><b>Hoch zu Schulbeginn, dann Abfall</b> – in der <b>2. Klasse durch sozialen Vergleich</b>.</li><li>Das <b>Lehrerurteil wird bedeutsamer</b>.</li></ul>' + H('Laut Grafik sinkt die Kurve bis ca. zur 6.–7. Klasse und bleibt dann niedrig.'),
      'Fähigkeitsselbstkonzept Entwicklung Abfall 2. Klasse sozialer Vergleich Lehrerurteil'),
    C('frame', SK, 'Was bedeuten <b>external</b> und <b>internal frame of reference</b>?',
      '<ul><li><b>External frame</b>: Vergleich mit <b>den anderen</b> („besser als die anderen“).</li><li><b>Internal frame</b>: Vergleich mit den <b>eigenen Leistungen in anderen Fächern</b> („aber nicht so gut wie in Deutsch“).</li></ul>',
      'frame of reference Bezugsrahmen external internal Vergleich'),
    C('fsk-leistung', SK, 'Was wirkt auf was: <b>Fähigkeitsselbstkonzept und Leistung</b>?',
      '<ul><li><b>Grundschule</b> (Helmke, 1998, 2.–4. Klasse): <b>Leistung wirkt auf das spätere Selbstkonzept</b>.</li><li><b>Jugendliche</b> (Marsh, 1995): Es wirkt bevorzugt das <b>Fähigkeitsselbstkonzept von heute auf die Noten von morgen</b>.</li></ul><p>In der Grafik zu Helmke ist der Pfeil Leistung → Selbstkonzept im Folgejahr dick, der Pfeil Selbstkonzept → spätere Leistung dünn.</p>',
      'Fähigkeitsselbstkonzept Leistung Helmke Marsh Grundschule Jugendliche Noten'),
    C('fsk-schaetzung', SK, 'Wann ist eine <b>Überschätzung</b> des Fähigkeitsselbstkonzepts günstig, wann ungünstig?',
      '<ul><li><b>Leichte Überschätzung: sehr günstig</b> – schwierige Aufgaben werden angepackt, bei Problemen wird durchgehalten.</li><li><b>Starke Überschätzung: ungünstig</b> – Lernerfolg wird für selbstverständlich gehalten.</li></ul>',
      'Überschätzung Fähigkeitsselbstkonzept leicht stark günstig ungünstig'),
    C('fsk-geschlecht', SK, 'Wie unterscheidet sich das Fähigkeitsselbstkonzept von <b>Mädchen und Jungen</b> (Schilling, Sparfeld &amp; Rost, 2006)?',
      '<p><b>Stereotypkonform</b>: Jungen haben ein höheres Selbstkonzept in <b>Mathe/Physik</b>, Mädchen in <b>Deutsch/Englisch</b>.</p><p>Effektstärken d (Zeile „Sk“): Deutsch −.40, Englisch −.22, Biologie .14, Geschichte .36, Mathe .40, Physik .73.</p>' + H('Vorzeichen so gelesen, dass positive Werte „Jungen höher“ bedeuten.'),
      'Fähigkeitsselbstkonzept Geschlecht Mädchen Jungen Mathe Physik Deutsch Englisch stereotyp'),
    C('bflp', SK, 'Was ist der <b>Big-Fish-Little-Pond-Effekt</b> (Marsh, 2001, 2005)?',
      '<p>Er beschreibt die <b>Auswirkung der Referenzgruppe auf das Selbstkonzept</b>: <b>Je besser die Klasse, desto niedriger das Fähigkeitsselbstkonzept</b> des einzelnen Schülers (und umgekehrt).</p><p>Beispiel: Zwei Schüler mit <b>gleicher Leistung</b>. In der leistungsstärkeren Klasse 6a („kleiner Fisch im großen Teich“) → <b>niedrigeres</b> Selbstkonzept; in der leistungsschwächeren 6b („großer Fisch im kleinen Teich“) → <b>höheres</b>.</p>',
      'Big-Fish-Little-Pond Referenzgruppe Klasse Selbstkonzept Marsh'),
    C('swe-def', SW, 'Was ist eine <b>Selbstwirksamkeitserwartung</b>? Wovon ist sie abzugrenzen?',
      '<p>Die <b>Überzeugung, eine bestimmte Handlung durchführen zu können</b>.</p><p>Abzugrenzen von der <b>Instrumentalität</b>: der Überzeugung, dass die Handlung <b>zum angestrebten Ziel führt</b>.</p>',
      'Selbstwirksamkeitserwartung Definition Handlung Instrumentalität'),
    C('swe-einfluss', SW, 'Worauf wirken Selbstwirksamkeitserwartungen im <b>Leistungsverhalten</b>?',
      '<ul><li><b>Auswahl von Aufgaben</b> (z. B. Fachgebiete)</li><li><b>Auswahl des Schwierigkeitsniveaus</b></li><li><b>Ausdauer, Persistenz, investierte Anstrengung</b></li><li><b>Lern- und Leistungsverhalten insgesamt</b> (Verhaltensänderung)</li></ul>',
      'Selbstwirksamkeit Leistungsverhalten Aufgabenwahl Schwierigkeit Ausdauer Anstrengung'),
    C('swe-foerdern', SW, 'Wie entstehen <b>positive Selbstwirksamkeitserwartungen</b>?',
      '<ul><li>Schüler in die Lage versetzen, Ziele zu erreichen: <b>geschickte Zielwahl, Überredung, Modelllernen</b>.</li><li>Schüler müssen Zielerreichungen <b>internal attribuieren</b>.</li><li><b>Unterstützung von Autonomie</b> durch Offenheit und Engagement des Lehrers.</li><li><b>Mütterliches Engagement</b>.</li></ul>',
      'Selbstwirksamkeit fördern Zielwahl Überredung Modelllernen internal attribuieren Autonomie mütterliches Engagement'),
    C('swe-verlauf', SW, 'Wie verlaufen <b>Selbstwirksamkeitserwartung</b> und <b>Fähigkeitsselbstkonzept</b> in der Schulzeit?',
      '<ul><li><b>Selbstwirksamkeitserwartung steigt</b> (laut Grafik annähernd linear) von der Einschulung bis zum Schulende.</li><li><b>Fähigkeitsselbstkonzept sinkt</b>.</li></ul><p>Selbstwirksamkeit ist die <b>am stärksten aufgaben-/anforderungsspezifische</b> Ebene des Selbstkonzepts.</p>',
      'Selbstwirksamkeit steigt Fähigkeitsselbstkonzept sinkt Verlauf Schulzeit'),
    C('pa-def', PA, 'Was ist <b>Prüfungsängstlichkeit</b>? Welche <b>zwei Komponenten</b> hat sie?',
      '<p>Eine <b>stabile, überdauernde dispositionelle Eigenschaft</b>, in <b>Prüfungssituationen oder bei Leistungsabfragen mit Angst zu reagieren</b>.</p><ul><li><b>Besorgtheit (kognitiv)</b>: negative Erwartungen und Befürchtungen</li><li><b>Aufgeregtheit (physiologisch)</b>: Wahrnehmung von Erregtheit und körperlichem Unwohlsein (Zittern, Schwitzen, Übelkeit …)</li></ul>',
      'Prüfungsängstlichkeit Prüfungsangst Definition Besorgtheit kognitiv Aufgeregtheit physiologisch'),
    C('pa-auswirkungen', PA, 'Welche <b>Auswirkungen</b> hat Prüfungsangst?',
      '<p><b>Angst bindet kognitive Kapazitäten</b> →</p><ul><li><b>Verengung der Aufmerksamkeit</b></li><li>Beeinträchtigung der <b>aufarbeitenden Prozesse</b></li><li>Beeinträchtigung des <b>Abrufs aus dem Gedächtnis (Blackout)</b></li><li>Verlust von <b>Interesse und intrinsischer Motivation</b></li></ul>',
      'Prüfungsangst Auswirkungen kognitive Kapazität Aufmerksamkeit Blackout Motivation'),
    C('pa-leistung', PA, 'Wie hängen <b>Angst und Leistung</b> zusammen?',
      '<ul><li><b>Kein linearer Zusammenhang</b>.</li><li><b>Höchste Leistungsfähigkeit zwischen geringem und mittlerem Angstniveau</b>.</li><li><b>Starke Angst (Prüfungsangst) führt zum Leistungszusammenbruch.</b></li></ul><p>Die Folie schreibt „U-förmig“, die Grafik zeigt aber ein <b>umgekehrtes U</b> (Leistung am höchsten bei mittlerer Angst).</p>',
      'Angst Leistung Zusammenhang nicht linear U-förmig Leistungszusammenbruch'),
    C('pa-entwicklung', PA, 'Wie <b>entwickelt</b> sich Prüfungsangst in der Schulzeit?',
      'Sie <b>steigt zunächst an</b>, bleibt eine Weile hoch und <b>sinkt gegen Schulende wieder etwas ab</b>.' + H('Laut Grafik Anstieg ab etwa der 3.–4. Klasse, Höhepunkt um die 6.–7. Klasse.'),
      'Prüfungsangst Entwicklung Verlauf Schulzeit'),
    C('pa-einfluss', PA, 'Welche <b>Einflussfaktoren</b> auf Prüfungsangst nennt die Folie?',
      '<ul><li><b>Mädchen &gt; Jungen</b></li><li><b>Elterliche Strenge</b>, mangelnde Unterstützung, Inkonsistenz</li><li><b>Kompetitives Schulklima</b>, <b>autoritäres Lehrerverhalten</b>, strenge, an <b>sozialer Bezugsnorm</b> orientierte Leistungsbewertung</li><li><b>Kompliziert und unverständlich vorgetragener Lehrstoff</b>, <b>unklare</b> oder die <b>Schwierigkeit betonende Prüfungsankündigungen</b></li></ul>',
      'Prüfungsangst Einflussfaktoren Mädchen elterliche Strenge kompetitiv autoritär soziale Bezugsnorm Prüfungsankündigung'),
    C('lz-lv', ZO, 'Was unterscheidet <b>Lernzielorientierung</b> und <b>Leistungszielorientierung</b>?',
      '<table><tr><th></th><th>Lernziel = Aufgabenorientierung</th><th>Leistungsziel = Folgenorientierung</th></tr><tr><td>Ziel</td><td><b>Kompetenzen erweitern</b>, Neues lernen</td><td><b>Kompetenzen beweisen</b> oder fehlende verbergen, positive Bewertungen erhalten</td></tr><tr><td>Fähigkeit beurteilt</td><td>nach <b>objektiven Kriterien</b> oder <b>individuellem Lernfortschritt</b></td><td>durch <b>Sozialvergleich</b></td></tr><tr><td>Rückmeldung</td><td><b>willkommen</b>, wird aufgesucht</td><td><b>Bestandsaufnahme</b> eigener Fähigkeiten</td></tr><tr><td>Misserfolg</td><td><b>Teil des Lernprozesses</b>, informativ</td><td>wird als <b>Versagen</b> gedeutet</td></tr></table>',
      'Lernzielorientierung Leistungszielorientierung Aufgabenorientierung Folgenorientierung Sozialvergleich Misserfolg'),
    C('2x2', ZO, 'Wie sieht das <b>2×2-Modell der Zielorientierungen</b> (Elliot &amp; McGregor, 2001) aus?',
      '<table><tr><th></th><th>intrapersonal/absolut (Lernziele)</th><th>normativ (Leistungsziele)</th></tr><tr><td><b>positiv</b> (Streben nach Erfolg)</td><td><b>Annäherungs-Lernziele</b>: Neues dazulernen, Kompetenzen erweitern</td><td><b>Annäherungs-Leistungsziele</b>: bessere Leistungen als andere zeigen</td></tr><tr><td><b>negativ</b> (Vermeidung von Misserfolg)</td><td><b>Vermeidungs-Lernziele</b>: Erlerntes nicht vergessen, Fähigkeiten nicht verlieren</td><td><b>Vermeidungs-Leistungsziele</b>: keine schlechteren Leistungen als andere zeigen</td></tr></table>',
      '2x2 Modell Zielorientierung Elliot McGregor Annäherung Vermeidung Lernziele Leistungsziele'),
    C('pfad', ZO, 'Was zeigt das <b>hierarchische Pfadmodell</b> der Zielorientierungen?',
      '<p><b>Kernaussage: Nur Annäherungs- und Vermeidungs-Leistungsziele sagen Noten vorher.</b></p><p>Pfade laut Folie: Bedürfnis nach Erfolg → Annäherungs-Lernziele .34, Vermeidungs-Lernziele .21, Annäherungs-Leistungsziele .22; Vermeidung von Misserfolg → Vermeidungs-Lernziele .15, Annäherungs-Leistungsziele .24, Vermeidungs-Leistungsziele .31. Annäherungs-Lernziele → intrinsische Motivation .28; Vermeidungs-Leistungsziele → intrinsische Motivation −.15; Annäherungs-Leistungsziele → Prüfungsnoten .46; Vermeidungs-Leistungsziele → Prüfungsnoten −.48.</p>',
      'Pfadmodell Zielorientierung Noten vorhersagen Leistungsziele intrinsische Motivation'),
    C('lz-hoch', ZO, 'Womit geht eine <b>hohe Lernzielorientierung</b> einher?',
      '<ul><li>höhere <b>Leistungsmotivation</b></li><li>höhere <b>intrinsische Motivation</b></li><li>besseres <b>Fähigkeitsselbstkonzept</b></li><li><b>günstigere Attributionen</b> (Erfolg → internal, stabil; Misserfolg → external, labil)</li><li>positivere <b>Einstellungen</b> zu Schule, Lernen, auch schwierigen Aufgaben</li><li>besseres <b>subjektives Wohlbefinden</b></li></ul>',
      'Lernzielorientierung hoch intrinsische Motivation Attribution Wohlbefinden'),
    C('keine-pole', ZO, 'Sind Lern- und Leistungszielorientierung <b>Gegensätze</b>?',
      '<b>Nein</b>, sie sind <b>keine gegensätzlichen Pole</b>. <b>Hohe Lernziel- und hohe Leistungszielorientierung zusammen haben keine ungünstigen Effekte.</b>',
      'Lernziel Leistungsziel keine Pole kombiniert'),
    C('lz-entwicklung', ZO, 'Wie <b>entwickelt</b> sich die Lernzielorientierung? Welche Liste steht dazu auf der Folie?',
      '<p>Zu Schulbeginn <b>hoch</b>, <b>sinkt</b> im Verlauf der Schulzeit.</p><p>Unter der Grafik steht ohne Überschrift: sozialer Vergleich · Verständnis von Fähigkeit als fester Kapazität · positive und negative Leistungsrückmeldung der Umwelt · Entity Theory der eigenen Fähigkeit.</p>',
      'Lernzielorientierung Entwicklung sinkt Entity Theory sozialer Vergleich'),
    C('verlaeufe', SP, '<b>Überblick</b>: Wie verlaufen die Merkmale von der Einschulung bis zum Schulende?',
      '<table><tr><th>Merkmal</th><th>Verlauf</th></tr><tr><td>Intelligenz</td><td><b>steigt</b>, prädizierbar ab ca. 3. Klasse</td></tr><tr><td>Fähigkeitsselbstkonzept</td><td><b>sinkt</b> (Abfall ab 2. Klasse)</td></tr><tr><td>Selbstwirksamkeitserwartung</td><td><b>steigt</b></td></tr><tr><td>Prüfungsangst</td><td>steigt zunächst, später leichter <b>Rückgang</b></td></tr><tr><td>Lernzielorientierung</td><td><b>sinkt</b></td></tr></table>',
      'Entwicklungsverlauf Schulzeit Überblick Intelligenz Selbstkonzept Selbstwirksamkeit Prüfungsangst Lernzielorientierung'),
    C('verwechslung', SP, '<b>Verwechslungsgefahr</b> Kap. 4b',
      '<ul><li><b>Spearman</b>: g + s · <b>Cattell</b>: Gf (angeboren) + Gc (erlernt) · <b>CHC</b>: hierarchisch, drei Schichten.</li><li><b>Fähigkeitsselbstkonzept</b> (sinkt) ≠ <b>Selbstwirksamkeit</b> (Handlung durchführen können; steigt) ≠ <b>Instrumentalität</b> (Handlung führt zum Ziel).</li><li><b>Lernziele</b> (intrapersonal) ≠ <b>Leistungsziele</b> (normativ); <b>Annäherung</b> ≠ <b>Vermeidung</b>.</li><li><b>Nur Leistungsziele</b> sagen Noten vorher.</li><li>Besorgtheit = <b>kognitiv</b>, Aufgeregtheit = <b>physiologisch</b>.</li><li>Big-Fish-Little-Pond: bessere Klasse → <b>niedrigeres</b> Selbstkonzept.</li><li>External frame = Vergleich mit <b>anderen</b>, internal frame = Vergleich mit <b>eigenen anderen Fächern</b>.</li></ul>',
      'Verwechslung Spearman Cattell CHC Selbstkonzept Selbstwirksamkeit Instrumentalität Lernziel Leistungsziel'),
]

CARDS4 = {'k4a': CARDS_K4A, 'k4b': CARDS_K4B}

# ---------------------------------------------------------------- Tests
ITEMS4 = []
SA = 'Teil 4 · Kap. 4a'
SB = 'Teil 4 · Kap. 4b'
def mc(id, src, q, options, expl, kw):
    assert len(options) == 4, id
    corr = [i for i, o in enumerate(options) if o.startswith('*')]
    assert 1 <= len(corr) <= 4, id
    opts = [o[1:] if o.startswith('*') else o for o in options]
    ITEMS4.append(dict(id=id, type='mc', q=q, options=opts, correct=corr[0] if len(corr) == 1 else corr, expl=expl, src=src, kw=kw))
def tf(id, src, statement, answer, expl, kw):
    ITEMS4.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=src, kw=kw))
def gap(id, src, text, expl, kw):
    ITEMS4.append(dict(id=id, type='gap', text=text, expl=expl, src=src, kw=kw))

# ---- 4a Multiple Choice
mc('p4a-mc-01', SA, 'Welche dieser Verfahren nennt die Folie als <b>Methoden der Persönlichkeitserfassung</b>?',
   ['*Nominationen', '*Dokumentenanalyse', '*Analyse des Ausdrucksverhaltens', 'Faktorenanalyse'],
   'Die Folie nennt 10 Verfahren, darunter Nominationen, Dokumentenanalyse und Analyse des Ausdrucksverhaltens. Die Faktorenanalyse ist ein Auswertungsverfahren für Korrelationsmuster, keine der genannten Erfassungsmethoden.', 'Methoden Persönlichkeitserfassung')
mc('p4a-mc-02', SA, 'Welche Beispiele nennt die Folie für <b>Persönlichkeitsinventare</b>?',
   ['*MMPI', '*NEO-FFI', '*16PF', 'TAT'],
   'MMPI, NEO-FFI und 16PF sind Fragebögen zur Selbsteinschätzung. Der TAT ist ein projektiver Test.', 'Persönlichkeitsinventare MMPI NEO-FFI 16PF')
mc('p4a-mc-03', SA, 'Welches Beispiel gehört zu den <b>projektiven Tests</b>?',
   ['*Rorschach', 'Typ-A-strukturiertes Interview', 'Traumtagebücher', 'Hautleitfähigkeit'],
   'Projektive Tests: Mann-Zeichen-Test, TAT, Rorschach. Typ-A-Interview = Interview, Traumtagebücher = Dokumentenanalyse, Hautleitfähigkeit = biologische Messung.', 'projektive Tests Rorschach')
mc('p4a-mc-04', SA, 'Welche Beispiele nennt die Folie für <b>biologische Messungen</b>?',
   ['*Reaktionszeit', '*Hautleitfähigkeit', '*EEG', '*PET'],
   'Alle vier stehen auf der Folie unter biologischen Messungen.', 'biologische Messungen EEG PET')
mc('p4a-mc-05', SA, 'Was gehört laut Folie zur <b>Analyse des Ausdrucksverhaltens</b>?',
   ['*Sprechgeschwindigkeit', '*interpersonelle Distanz', 'politische Orientierung', 'Psychobiographie'],
   'Ausdrucksverhalten: Sprechgeschwindigkeit, Gesten, interpersonelle Distanz. Politische Orientierung gehört zu den demografischen und Lifestyle-Angaben, Psychobiographie zur Dokumentenanalyse.', 'Ausdrucksverhalten Sprechgeschwindigkeit Distanz')
mc('p4a-mc-06', SA, 'Welche Facetten gehören im NEO-FFI zur <b>Gewissenhaftigkeit</b>?',
   ['*Ordnungsliebe', '*Selbstdisziplin', '*Besonnenheit', 'Altruismus'],
   'Gewissenhaftigkeit: Kompetenz, Ordnungsliebe, Pflichtbewusstsein, Leistungsstreben, Selbstdisziplin, Besonnenheit. Altruismus gehört zur Verträglichkeit.', 'Gewissenhaftigkeit Facetten')
mc('p4a-mc-07', SA, 'Welche Facetten gehören im NEO-FFI zum <b>Neurotizismus</b>?',
   ['*Impulsivität', '*soziale Befangenheit', 'Erlebnishunger', 'Bescheidenheit'],
   'Neurotizismus: Ängstlichkeit, Reizbarkeit, Depression, soziale Befangenheit, Impulsivität, Verletzlichkeit. Erlebnishunger gehört zur Extraversion, Bescheidenheit zur Verträglichkeit.', 'Neurotizismus Facetten Impulsivität')
mc('p4a-mc-08', SA, 'NEO-FFI-Item: „Ich finde philosophische Diskussionen langweilig.“ Welche Aussagen stimmen?',
   ['*Es gehört zum Faktor Offenheit für Erfahrungen.', '*Es wird umgekehrt gepunktet (invertiertes Item).', 'Es gehört zum Faktor Extraversion.', 'Starke Zustimmung spricht für hohe Offenheit.'],
   'Das Item ist das invertierte Beispielitem der Offenheit: Zustimmung spricht für <b>niedrige</b> Offenheit, deshalb wird es umgekehrt gepunktet.', 'invertiertes Item Offenheit')
mc('p4a-mc-09', SA, 'Welche <b>Vorzüge</b> von Selbsteinschätzungen nennt die Folie?',
   ['*Auch vergangenes oder nicht beobachtbares Verhalten ist erfassbar.', '*Ökonomie: geringe Kosten, viele Personen befragbar', '*Anonymität', 'Unabhängigkeit von Antworttendenzen'],
   'Vorzüge: vergangenes/nicht beobachtbares Verhalten, Ökonomie, Anonymität. Antworttendenzen (Response-Sets) sind gerade ein <b>Problem</b> der Selbsteinschätzung.', 'Selbsteinschätzung Vorzüge')
mc('p4a-mc-10', SA, 'Welche <b>Response-Sets</b> nennt die Folie bei Selbsteinschätzungen?',
   ['*Tendenz zur Bejahung (Ja-Sage-Tendenz)', '*Tendenz zu sozialer Erwünschtheit', 'Primacy-Effekt', 'Halo-Effekt'],
   'Response-Sets: Bejahung, ungewöhnliche Antworten, soziale Erwünschtheit. Primacy- und Halo-Effekt sind Beurteilungsfehler bei Fremdratings.', 'Response-Sets Ja-Sage soziale Erwünschtheit')
mc('p4a-mc-11', SA, 'Eine Lehrerin hält einen sehr redegewandten Schüler deshalb auch für fleißig, ordentlich und hilfsbereit. Welcher Beurteilungsfehler liegt vor?',
   ['*Halo-Effekt', 'Fehler der zentralen Tendenz', 'Recency-Effekt', 'Primacy-Effekt'],
   'Halo-Effekt: Von einem hervorstechenden Merkmal wird auf andere Merkmale geschlossen. Reihenfolge-Effekte betreffen die Rolle des ersten bzw. letzten Eindrucks.', 'Halo-Effekt Beispiel')
mc('p4a-mc-12', SA, 'Welche Aussagen zu den <b>Reihenfolge-Effekten</b> stimmen?',
   ['*Der Primacy-Effekt beschreibt die besondere Rolle des ersten Eindrucks.', '*Der Recency-Effekt beschreibt die besondere Rolle der letzten Beobachtung.', '*Sie wirken beim Zusammenfügen von Einzelbeobachtungen zu einem Gesamteindruck.', 'Der Fehler der zentralen Tendenz ist ein Reihenfolge-Effekt.'],
   'Primacy = erster Eindruck, Recency = letzte Beobachtung, beides bei der Integration zu einem Gesamteindruck. Die zentrale Tendenz (Extreme vermeiden) ist ein eigener Beurteilungsfehler.', 'Reihenfolge-Effekte Primacy Recency')
mc('p4a-mc-13', SA, 'Was zeigt der Vergleich von <b>Selbst- und Bekanntenurteil</b> zu Intelligenz und sozialer Kompetenz?',
   ['*Für dasselbe Merkmal stimmen die Urteile nur mäßig überein.', '*Für verschiedene Merkmale liegen die Zusammenhänge nahe null.', 'Für dasselbe Merkmal stimmen die Urteile fast perfekt überein.', 'Selbst- und Bekanntenurteil hängen bei keinem Merkmal zusammen.'],
   'Die Diagonale (gleiches Merkmal) zeigt nur mäßige Werte, die übrigen Zellen liegen nahe null.', 'Selbsturteil Fremdurteil Übereinstimmung')
mc('p4a-mc-14', SA, 'In einer Klasse mit 30 Kindern nennen 12 Kinder Lena als besonders hilfsbereit. Welchen Wert erhält Lena bei dieser <b>Nomination</b>?',
   ['*40 %', '12 %', '30 %', '60 %'],
   'Wert = prozentuale Häufigkeit der Nominationen: 12 von 30 = 40 %.', 'Nomination Prozent berechnen')
mc('p4a-mc-15', SA, 'Welche Aussagen zu <b>Nominationen</b> stimmen?',
   ['*Sie reduzieren systematische Beurteilungsfehler.', '*Sie sind sehr aufwändig.', '*Sie sind auf Beobachtbares beschränkt.', 'Sie schließen Verzerrungen vollständig aus.'],
   'Viele Beurteiler verringern Beurteilungsfehler, Verzerrungen sind aber nicht ausgeschlossen – auch viele können sich systematisch irren.', 'Nomination Vorteil Nachteil')
mc('p4a-mc-16', SA, 'NEO-FFI-Profile: Welche Zuordnungen stimmen?',
   ['*Das Profil einer einzelnen Schülerin (Anna) ist idiografisch.', '*Das Profil der Klasse 4a (Mittelwerte) ist nomothetisch.', 'Das Profil einer einzelnen Schülerin ist nomothetisch.', 'Das Klassenprofil ist Psychografie.'],
   'Eine Person, viele Merkmale = idiografisch. Gruppenmittelwerte = nomothetisch. Psychografie betrifft eine einzelne Person.', 'Profil idiografisch nomothetisch')
mc('p4a-mc-17', SA, 'Welche <b>Probleme</b> von Selbsteinschätzungen nennt die Folie?',
   ['*Rücklaufquoten und unvollständige Antworten', '*mangelnde Übereinstimmung von Einstellungen und tatsächlichem Verhalten', '*Täuschungsversuche', '*systematische, verzerrende Antworttendenzen'],
   'Alle vier stehen auf der Folie.', 'Selbsteinschätzung Probleme')
mc('p4a-mc-18', SA, 'Wer schätzt bei einem <b>Fremdrating</b> meist das Verhalten von Person X ein?',
   ['*eine Person, die X gut kennt', 'X selbst', 'viele Mitschüler, deren Nennungen in Prozent umgerechnet werden', 'ein Biofeedback-Gerät'],
   'Fremdrating: Person Y schätzt X auf vorgegebenen Skalen ein, meist jemand, der X gut kennt. Viele Beurteiler mit Prozentwert = Nomination.', 'Fremdrating Beurteiler')

# ---- 4a Richtig/Falsch
tf('p4a-tf-01', SA, 'Bei einem Persönlichkeitsinventar schätzt sich die Person selbst ein.', True,
   'Selbsteinschätzung per Fragebogen, z. B. NEO-FFI.', 'Persönlichkeitsinventar Selbsteinschätzung')
tf('p4a-tf-02', SA, 'Persönlichkeitsinventare erfassen in der Regel nur eine einzige Persönlichkeitsdimension.', False,
   'Sie erfassen meist <b>mehrere</b> Dimensionen (Skalen); zusammen ergeben sie ein Persönlichkeitsprofil.', 'Persönlichkeitsinventar Skalen')
tf('p4a-tf-03', SA, 'Beim Fehler der zentralen Tendenz bevorzugen Beurteiler extreme Urteile.', False,
   'Umgekehrt: Extreme werden <b>vermieden</b>, Urteile liegen vor allem im mittleren Bereich.', 'zentrale Tendenz')
tf('p4a-tf-04', SA, 'Beim Recency-Effekt prägt die letzte Beobachtung den Gesamteindruck besonders.', True,
   'Primacy = erster Eindruck, Recency = letzte Beobachtung.', 'Recency-Effekt')
tf('p4a-tf-05', SA, 'Weil bei Nominationen viele Personen urteilen, sind Verzerrungen ausgeschlossen.', False,
   'Beurteilungsfehler werden <b>reduziert</b>, aber auch viele Personen können sich systematisch irren.', 'Nomination Verzerrung')
tf('p4a-tf-06', SA, 'Psychobiographie und Traumtagebücher gehören zur Dokumentenanalyse.', True,
   'Beispiele der Folie für die Dokumentenanalyse.', 'Dokumentenanalyse Psychobiographie Traumtagebuch')
tf('p4a-tf-07', SA, 'Das Typ-A-strukturierte Interview ist ein projektiver Test.', False,
   'Es gehört zu den <b>Interviews</b> (wie das klinische Interview). Projektive Tests: Mann-Zeichen-Test, TAT, Rorschach.', 'Typ-A Interview projektiv')
tf('p4a-tf-08', SA, 'Im NEO-FFI ist „Erlebnishunger“ eine Facette der Extraversion.', True,
   'Extraversion: Herzlichkeit, Geselligkeit, Durchsetzungsfähigkeit, Aktivität, Erlebnishunger, Frohsinn.', 'Erlebnishunger Extraversion')
tf('p4a-tf-09', SA, 'Im NEO-FFI sind „Vertrauen“ und „Altruismus“ Facetten der Gewissenhaftigkeit.', False,
   'Sie gehören zur <b>Verträglichkeit</b>.', 'Vertrauen Altruismus Verträglichkeit')
tf('p4a-tf-10', SA, 'Mit Selbsteinschätzungen lässt sich auch vergangenes oder nicht beobachtbares Verhalten erfassen.', True,
   'Einer der Vorzüge neben Ökonomie und Anonymität.', 'Selbsteinschätzung Vorzug')
tf('p4a-tf-11', SA, 'Selbst- und Bekanntenurteil stimmen für dasselbe Merkmal nur mäßig überein.', True,
   'Für verschiedene Merkmale liegen die Zusammenhänge sogar nahe null.', 'Selbsturteil Bekanntenurteil')
tf('p4a-tf-12', SA, 'Nominationen eignen sich gut, um nicht beobachtbares Verhalten zu erfassen.', False,
   'Nominationen sind <b>auf Beobachtbares beschränkt</b> und außerdem sehr aufwändig.', 'Nomination Beobachtbares')

# ---- 4a Lückentext
gap('p4a-gap-01', SA, 'Wird von einem hervorstechenden Merkmal auf andere Persönlichkeitsmerkmale geschlossen, spricht man vom {{Halo-Effekt|Halo|Haloeffekt|Halo Effekt}}.',
    'Ein Beurteilungsfehler bei Fremdratings.', 'Halo-Effekt')
gap('p4a-gap-02', SA, 'Werden auf Ratingskalen die Extreme vermieden, spricht man vom Fehler der {{zentralen}} Tendenz.',
    'Urteile liegen dann vor allem im mittleren Bereich.', 'zentrale Tendenz')
gap('p4a-gap-03', SA, 'Den besonderen Einfluss des ersten Eindrucks nennt man {{Primacy-Effekt|Primacy|Primacyeffekt|Primacy Effekt}}, den der letzten Beobachtung {{Recency-Effekt|Recency|Recencyeffekt|Recency Effekt}}.',
    'Beides sind Reihenfolge-Effekte.', 'Primacy Recency')
gap('p4a-gap-04', SA, 'Die Ausprägungen auf mehreren Skalen eines Inventars ergeben zusammen ein {{Persönlichkeitsprofil|Profil}}.',
    'Muster der Persönlichkeit.', 'Persönlichkeitsprofil')
gap('p4a-gap-05', SA, 'Ein Item wie „Ich finde philosophische Diskussionen langweilig.“ ist ein {{invertiertes|umgepoltes|invertiert}} Item und wird umgekehrt gepunktet.',
    'Zustimmung spricht hier für niedrige Offenheit.', 'invertiertes Item')
gap('p4a-gap-06', SA, 'Wird eine Person von vielen verschiedenen Personen beurteilt und ihr Wert als prozentuale Häufigkeit angegeben, spricht man von einer {{Nomination}}.',
    'Beispiel: Paul wird von 15 von 30 Mitschülern genannt → 50 %.', 'Nomination')

# ---- 4b Multiple Choice
mc('p4b-mc-01', SB, 'Welche Merkmale ordnet die Folie dem <b>kognitiv/evaluativen</b> Bereich der Schülerpersönlichkeit zu?',
   ['*Fähigkeitsselbstkonzept', '*Selbstwirksamkeitserwartung', '*Kontrollerwartungen', 'Prüfungsängstlichkeit'],
   'Kognitiv/evaluativ: Intelligenz, Fähigkeitsselbstkonzept, Selbstwirksamkeitserwartung, Kontrollerwartungen. Prüfungsängstlichkeit ist emotional/motivational.', 'Schülerpersönlichkeit kognitiv evaluativ')
mc('p4b-mc-02', SB, 'Welche Merkmale gehören in der impliziten Persönlichkeitstheorie von Lehrkräften zum <b>„schlechten Schüler“</b>?',
   ['*unangepasst', '*milieubelastet', 'angepasst', 'milieubegünstigt'],
   'Schlechter Schüler: faul, dumm, frech, angeberisch, unaufmerksam, unordentlich, unangepasst, milieubelastet. Angepasst und milieubegünstigt beschreiben den guten Schüler.', 'implizite Theorie schlechter Schüler')
mc('p4b-mc-03', SB, 'Welche <b>Beurteilungsdimensionen</b> von Lehrkräften nennt die Folie?',
   ['*intellektuelle Ausstattung', '*Motivation (Fleiß, Ehrgeiz)', '*soziales Verhalten', '*emotionale Stabilität'],
   'Alle vier Dimensionen stehen auf der Folie.', 'Beurteilungsdimensionen Lehrkräfte')
mc('p4b-mc-04', SB, 'Welche Merkmale gehören bei der Intelligenzbeurteilung durch Lehrkräfte zur <b>nicht fundierten impliziten Theorie</b>?',
   ['*hohe Stirn', '*macht Hausaufgaben', 'abstraktes Denken', 'Verarbeitungsgeschwindigkeit'],
   'Nicht fundiert: wacher Gesichtsausdruck, Durchsetzungsvermögen, Ordentlichkeit, hohe Stirn, geordnetes Elternhaus, macht Hausaufgaben. Abstraktes Denken und Verarbeitungsgeschwindigkeit gehören zur fundierten Theorie.', 'Intelligenzbeurteilung nicht fundiert')
mc('p4b-mc-05', SB, 'Was gehört laut Wechsler zur Intelligenz?',
   ['*zweckvoll handeln', '*vernünftig denken', '*sich mit der Umgebung wirkungsvoll auseinandersetzen', 'umfangreiches Faktenwissen besitzen'],
   'Wechsler: zusammengesetzte oder globale Fähigkeit, zweckvoll zu handeln, vernünftig zu denken und sich mit der Umgebung wirkungsvoll auseinanderzusetzen. Wissen ist laut Folie gerade <b>nicht</b> Intelligenz.', 'Wechsler Definition')
mc('p4b-mc-06', SB, 'Was ist laut Folie <b>nicht</b> Intelligenz?',
   ['*Erfolg', '*Wissen', '*Talent', 'Abstraktionsvermögen'],
   'Intelligenz ist nicht: Erfolg, Wissen, Kompetenz, Talent. Abstraktionsvermögen gehört dagegen zur Intelligenz.', 'Intelligenz nicht Erfolg Wissen Talent')
mc('p4b-mc-07', SB, 'Welcher Anteil der Bevölkerung hat eine <b>normale Begabung</b> (IQ 85–115)?',
   ['*68,2 %', '34,1 %', '95,4 %', '13,6 %'],
   'Je 34,1 % auf beiden Seiten des Mittelwerts (±1 SD) ergeben 68,2 %. 13,6 % liegen jeweils zwischen 1 und 2 SD.', 'normale Begabung 68,2')
mc('p4b-mc-08', SB, 'IQ-Bereiche (M = 100, SD = 15): Welche Zuordnungen stimmen?',
   ['*Hochbegabung: über 130', '*Minderbegabung: unter 70', 'Überdurchschnittliche Intelligenz: 100–115', 'Unterdurchschnittliche Intelligenz: 55–70'],
   'Unter 70 Minderbegabung, 70–85 unterdurchschnittlich, 85–115 normal, 115–130 überdurchschnittlich, über 130 Hochbegabung.', 'IQ Bereiche Grenzen')
mc('p4b-mc-09', SB, 'Welche Aussagen gehören zu den <b>paradigmenübergreifenden Annahmen</b> über Intelligenz?',
   ['*Intelligenz ist ein stabiles Persönlichkeitsmerkmal.', '*Intelligenzunterschiede haben eine zerebrale Grundlage.', '*Der kulturelle und individuelle Kontext ist entscheidend dafür, wie kognitive Fähigkeiten die Aneignung von Wissen beeinflussen.', 'Intelligenzunterschiede sind vollständig durch die Umwelt erklärbar.'],
   'Laut Folie sind mindestens 50 % der Varianz genetisch erklärbar – also nicht vollständig durch die Umwelt.', 'Annahmen Intelligenz Stern Guthke')
mc('p4b-mc-10', SB, 'Welche Aussagen zur <b>Generalfaktoren-Theorie</b> stimmen?',
   ['*Intelligenz wird auf einen Generalfaktor g zurückgeführt.', '*Spezielle Fähigkeiten s erklären Unterschiede in einzelnen Subtests.', '*Begründet wird sie damit, dass unterschiedliche Intelligenzaufgaben korrelieren, aber nur mittelhoch.', 'Sie unterscheidet fluide und kristalline Intelligenz.'],
   'g + s ist Spearmans Theorie. Fluide und kristalline Intelligenz stammen von Cattell.', 'Generalfaktor Spearman g s')
mc('p4b-mc-11', SB, 'Welche Aufgabe nennt die Folie als Beispiel mit <b>hoher g-Ladung</b>?',
   ['*eine Matrizenaufgabe (fehlende Figur im Raster ergänzen)', 'eine Wortschatzaufgabe', 'eine verbale Analogie', 'eine Rechenaufgabe aus dem Schulbuch'],
   'Matrizenaufgabe mit geometrischen Figuren. Wortschatz und Analogien sind Beispielaufgaben zur kristallinen Intelligenz.', 'g-Ladung Matrizen')
mc('p4b-mc-12', SB, 'Welche Aussagen zur <b>fluiden Intelligenz</b> nach Cattell stimmen?',
   ['*Sie gilt als angeboren bzw. vererbt.', '*Sie umfasst geistige Kapazität und Auffassungsgabe.', 'Sie umfasst Faktenwissen und Fahrradfahren.', 'Sie ist von der kristallinen Intelligenz abhängig.'],
   'Umgekehrt: Die <b>kristalline</b> ist von der fluiden abhängig. Faktenwissen und Fahrradfahren gehören zur kristallinen Intelligenz.', 'fluide Intelligenz')
mc('p4b-mc-13', SB, 'Was gehört zur <b>kristallinen Intelligenz</b>?',
   ['*Faktenwissen', '*Fahrradfahren', '*Rechnen', '*Wortschatz'],
   'Kristallin: explizites Wissen (z. B. Fakten) und implizit Gelerntes (Verhaltensweisen, Fahrradfahren, Rechnen). Wortschatzaufgaben sind Beispielaufgaben zur kristallinen Intelligenz.', 'kristalline Intelligenz Beispiele')
mc('p4b-mc-14', SB, 'Welche Aussagen zum <b>CHC-Modell</b> stimmen?',
   ['*Es gilt als aktuelles Intelligenzmodell.', '*Intelligenz ist darin hierarchisch in drei Schichten organisiert.', 'An der Spitze stehen gleichrangig fluide und kristalline Intelligenz, ohne generellen Faktor.', 'Die Zahl der Faktoren ist festgelegt und nicht erweiterbar.'],
   'Ganz oben steht ein genereller Faktor G, darunter breite Faktoren (u. a. Gf, Gc), darunter spezifische Fähigkeiten. Das Modell ist offen für Erweiterungen.', 'CHC Modell hierarchisch')
mc('p4b-mc-15', SB, 'Welche Aussagen zur <b>Entwicklung der Intelligenz</b> stimmen?',
   ['*Sie steigt bis nach dem Schulende an.', '*Sie ist ab etwa der 3. Klasse prädizierbar.', '*Ihr Maximum liegt bei etwa Mitte 20.', 'Sie ist schon im Kindergarten gut vorhersagbar.'],
   'Vor der 3. Klasse ist sie instabil.', 'Intelligenz Entwicklung')
mc('p4b-mc-16', SB, 'Welche <b>Spezifitätsebenen</b> des Selbstkonzepts passen zu den Beispielsätzen?',
   ['*„Ich bin gut in Mathe.“ – schulfachspezifisches Fähigkeitsselbstkonzept', '*„Ich bin ein guter Schüler.“ – schulisches Fähigkeitsselbstkonzept', '*„Ich bin zufrieden mit mir.“ – allgemeines Selbstkonzept', 'Selbstwirksamkeit ist die allgemeinste Ebene.'],
   'Selbstwirksamkeit ist die <b>spezifischste</b> (aufgabenspezifische) Ebene.', 'Spezifitätsebenen Selbstkonzept')
mc('p4b-mc-17', SB, 'Welche Aussagen zur <b>Entwicklung des Fähigkeitsselbstkonzepts</b> stimmen?',
   ['*Es ist zu Schulbeginn hoch.', '*In der 2. Klasse fällt es durch sozialen Vergleich ab.', '*Das Lehrerurteil wird bedeutsamer.', 'Es steigt bis zum Schulende stetig an.'],
   'Es sinkt im Verlauf der Schulzeit. Stetig steigen die Selbstwirksamkeitserwartungen.', 'Fähigkeitsselbstkonzept Entwicklung')
mc('p4b-mc-18', SB, 'Ein Schüler denkt: „In Mathe bin ich zwar gut, aber nicht so gut wie in Deutsch.“ Welcher Bezugsrahmen ist das?',
   ['*internal frame of reference', 'external frame of reference', 'Big-Fish-Little-Pond-Effekt', 'soziale Bezugsnorm'],
   'Internal frame = Vergleich mit den eigenen Leistungen in anderen Fächern. External frame = Vergleich mit anderen.', 'internal frame')
mc('p4b-mc-19', SB, 'Wie hängen Fähigkeitsselbstkonzept und Leistung zusammen?',
   ['*In der Grundschule wirkt eher die Leistung auf das spätere Selbstkonzept.', '*Bei Jugendlichen wirkt eher das heutige Selbstkonzept auf die Noten von morgen.', 'In der Grundschule wirkt vor allem das Selbstkonzept auf die spätere Leistung.', 'Bei Jugendlichen besteht kein Zusammenhang mehr.'],
   'Grundschule (Helmke): Leistung → späteres Selbstkonzept. Jugendliche (Marsh): Selbstkonzept heute → Noten morgen.', 'Selbstkonzept Leistung Richtung')
mc('p4b-mc-20', SB, 'Was gilt für eine <b>Überschätzung</b> des eigenen Fähigkeitsselbstkonzepts?',
   ['*Eine leichte Überschätzung ist sehr günstig.', '*Bei leichter Überschätzung werden schwierige Aufgaben eher angepackt.', '*Eine starke Überschätzung ist ungünstig, weil Lernerfolg für selbstverständlich gehalten wird.', 'Jede Überschätzung ist ungünstig.'],
   'Leicht = günstig (anpacken, durchhalten), stark = ungünstig.', 'Überschätzung Selbstkonzept')
mc('p4b-mc-21', SB, 'Zwei Schüler zeigen die <b>gleiche Leistung</b>. Einer ist in einer leistungsstarken, der andere in einer leistungsschwachen Klasse. Was sagt der <b>Big-Fish-Little-Pond-Effekt</b> voraus?',
   ['*Der Schüler in der leistungsstarken Klasse hat ein niedrigeres Fähigkeitsselbstkonzept.', '*Der Schüler in der leistungsschwachen Klasse hat ein höheres Fähigkeitsselbstkonzept.', 'Beide haben dasselbe Fähigkeitsselbstkonzept, weil die Leistung gleich ist.', 'Der Schüler in der leistungsstarken Klasse hat ein höheres Fähigkeitsselbstkonzept.'],
   'Je besser die Klasse (Referenzgruppe), desto niedriger das Fähigkeitsselbstkonzept – und umgekehrt.', 'Big-Fish-Little-Pond')
mc('p4b-mc-22', SB, 'Welche Aussagen zur <b>Selbstwirksamkeitserwartung</b> stimmen?',
   ['*Sie ist die Überzeugung, eine bestimmte Handlung durchführen zu können.', '*Sie beeinflusst die Auswahl des Schwierigkeitsniveaus.', 'Sie ist die Überzeugung, dass eine Handlung zum Ziel führt.', 'Sie sinkt im Verlauf der Schulzeit.'],
   'Die Überzeugung, dass die Handlung zum Ziel führt, ist die <b>Instrumentalität</b>. Selbstwirksamkeitserwartungen steigen in der Schulzeit.', 'Selbstwirksamkeit Instrumentalität')
mc('p4b-mc-23', SB, 'Was fördert laut Folie <b>positive Selbstwirksamkeitserwartungen</b>?',
   ['*geschickte Zielwahl, Überredung und Modelllernen', '*Zielerreichungen internal attribuieren', '*Unterstützung von Autonomie durch Offenheit und Engagement des Lehrers', '*mütterliches Engagement'],
   'Alle vier stehen auf der Folie.', 'Selbstwirksamkeit fördern')
mc('p4b-mc-24', SB, 'Prüfungsängstlichkeit: Welche Zuordnungen stimmen?',
   ['*Besorgtheit ist die kognitive Komponente.', '*Aufgeregtheit ist die physiologische Komponente.', 'Besorgtheit zeigt sich vor allem in Zittern und Schwitzen.', 'Prüfungsängstlichkeit ist ein kurzfristiger Zustand (State).'],
   'Besorgtheit = negative Erwartungen und Befürchtungen; Zittern, Schwitzen, Übelkeit gehören zur Aufgeregtheit. Prüfungsängstlichkeit ist eine stabile, dispositionelle Eigenschaft.', 'Prüfungsangst Komponenten')
mc('p4b-mc-25', SB, 'Welche <b>Auswirkungen</b> von Prüfungsangst nennt die Folie?',
   ['*Verengung der Aufmerksamkeit', '*Beeinträchtigung des Abrufs aus dem Gedächtnis (Blackout)', '*Verlust von Interesse und intrinsischer Motivation', 'Erweiterung der kognitiven Kapazität'],
   'Angst <b>bindet</b> kognitive Kapazitäten.', 'Prüfungsangst Auswirkungen')
mc('p4b-mc-26', SB, 'Welche <b>Einflussfaktoren</b> auf Prüfungsangst nennt die Folie?',
   ['*kompetitives Schulklima', '*an sozialer Bezugsnorm orientierte Leistungsbewertung', '*unklare Prüfungsankündigungen', 'Jungen sind stärker betroffen als Mädchen.'],
   'Laut Folie Mädchen &gt; Jungen. Außerdem: elterliche Strenge, autoritäres Lehrerverhalten, kompliziert vorgetragener Lehrstoff.', 'Prüfungsangst Einflussfaktoren')
mc('p4b-mc-27', SB, 'Welche Aussagen beschreiben die <b>Lernzielorientierung</b>?',
   ['*Ziel ist, Kompetenzen zu erweitern.', '*Misserfolg gilt als informativer Teil des Lernprozesses.', 'Fähigkeit wird durch Sozialvergleich beurteilt.', 'Leistungsrückmeldung dient vor allem der Bestandsaufnahme.'],
   'Sozialvergleich und Bestandsaufnahme gehören zur Leistungszielorientierung (Folgenorientierung).', 'Lernzielorientierung')
mc('p4b-mc-28', SB, '„Ich will keine schlechteren Leistungen zeigen als die anderen.“ Welche Zielorientierung ist das im 2×2-Modell?',
   ['*Vermeidungs-Leistungsziel', 'Annäherungs-Leistungsziel', 'Vermeidungs-Lernziel', 'Annäherungs-Lernziel'],
   'Normativ (Vergleich mit anderen) + Vermeidung von Misserfolg = Vermeidungs-Leistungsziel. „Erlerntes nicht vergessen“ wäre ein Vermeidungs-Lernziel.', 'Vermeidungs-Leistungsziel')
mc('p4b-mc-29', SB, 'Welche Zielorientierungen sagen laut Pfadmodell <b>Noten</b> vorher?',
   ['*Annäherungs-Leistungsziele', '*Vermeidungs-Leistungsziele', 'Annäherungs-Lernziele', 'Vermeidungs-Lernziele'],
   'Kernaussage der Folie: Nur Annäherungs- und Vermeidungs-Leistungsziele sagen Noten vorher.', 'Pfadmodell Noten Leistungsziele')
mc('p4b-mc-30', SB, 'Womit geht eine <b>hohe Lernzielorientierung</b> einher?',
   ['*höhere intrinsische Motivation', '*besseres Fähigkeitsselbstkonzept', '*besseres subjektives Wohlbefinden', '*günstigere Attributionen'],
   'Alle vier stehen auf der Folie, außerdem höhere Leistungsmotivation und positivere Einstellungen zu Schule und Lernen.', 'Lernzielorientierung hoch')
mc('p4b-mc-31', SB, 'Welche Verläufe von der Einschulung bis zum Schulende stimmen?',
   ['*Selbstwirksamkeitserwartungen steigen.', '*Die Lernzielorientierung sinkt.', '*Das Fähigkeitsselbstkonzept sinkt.', 'Die Intelligenz sinkt.'],
   'Intelligenz steigt bis nach Schulende (Maximum ca. Mitte 20).', 'Verläufe Schulzeit')

# ---- 4b Richtig/Falsch
tf('p4b-tf-01', SB, 'Die Forschung zur Schülerpersönlichkeit fragt unter anderem, wie die Schule als Sozialisationsinstanz die Persönlichkeitsentwicklung beeinflusst.', True,
   'Zweite zentrale Frage: Einfluss der Schülerpersönlichkeit auf die Schulleistung.', 'Schule Sozialisationsinstanz')
tf('p4b-tf-02', SB, 'Prüfungsängstlichkeit zählt zu den kognitiv/evaluativen Merkmalen der Schülerpersönlichkeit.', False,
   'Sie ist ein <b>emotional/motivationales</b> Merkmal, wie Leistungs- und Lernmotivation und Zielorientierung.', 'Prüfungsängstlichkeit emotional motivational')
tf('p4b-tf-03', SB, 'Nach der nicht fundierten impliziten Theorie von Lehrkräften gilt ein „geordnetes Elternhaus“ als Hinweis auf Intelligenz.', True,
   'Ebenso wacher Gesichtsausdruck, Durchsetzungsvermögen, Ordentlichkeit, hohe Stirn, macht Hausaufgaben.', 'nicht fundierte Theorie Elternhaus')
tf('p4b-tf-04', SB, 'Wissen und Kompetenz sind laut Folie Teil der Intelligenz.', False,
   'Intelligenz ist laut Folie <b>nicht</b> Erfolg, Wissen, Kompetenz oder Talent.', 'Intelligenz nicht Wissen')
tf('p4b-tf-05', SB, 'Laut den paradigmenübergreifenden Annahmen ist mindestens die Hälfte der Varianz in Intelligenztestleistungen genetisch erklärbar.', True,
   'Mindestens 50 % – in Kulturkreisen, in denen Kindern weitgehend alle Lerngelegenheiten offenstehen.', 'Intelligenz genetisch Varianz')
tf('p4b-tf-06', SB, 'Nach Cattell ist die kristalline Intelligenz von der fluiden Intelligenz abhängig.', True,
   'Gf = angeboren (Kapazität), Gc = erlernt (Wissen), baut auf Gf auf.', 'kristallin abhängig fluide')
tf('p4b-tf-07', SB, 'Im CHC-Modell steht an der Spitze ein genereller Faktor G.', True,
   'G (Schicht III) → breite Faktoren (Schicht II) → spezifische Fähigkeiten (Schicht I).', 'CHC genereller Faktor')
tf('p4b-tf-08', SB, 'Intelligenz lässt sich schon vor der Einschulung zuverlässig vorhersagen.', False,
   'Prädizierbar erst ab ca. der <b>3. Klasse</b>, davor instabil.', 'Intelligenz prädizierbar')
tf('p4b-tf-09', SB, 'Die Selbstwirksamkeit ist die spezifischste (aufgabenspezifische) Ebene des Selbstkonzepts.', True,
   'Von allgemein nach spezifisch: Selbstkonzept → schulisch → fachspezifisch → anforderungsspezifisch → Selbstwirksamkeit.', 'Selbstwirksamkeit aufgabenspezifisch')
tf('p4b-tf-10', SB, 'Beim external frame of reference vergleicht ein Schüler seine Leistung mit der seiner Mitschüler.', True,
   'Internal frame: Vergleich mit eigenen Leistungen in anderen Fächern.', 'external frame')
tf('p4b-tf-11', SB, 'Jungen haben laut Folie in Mathe und Physik ein höheres Fähigkeitsselbstkonzept, Mädchen in Deutsch und Englisch.', True,
   'Das Muster ist stereotypkonform.', 'Selbstkonzept Geschlecht')
tf('p4b-tf-12', SB, 'Nach dem Big-Fish-Little-Pond-Effekt steigt das Fähigkeitsselbstkonzept, je besser die Klasse ist.', False,
   'Umgekehrt: Je besser die Klasse, desto <b>niedriger</b> das Fähigkeitsselbstkonzept.', 'Big-Fish-Little-Pond')
tf('p4b-tf-13', SB, 'Selbstwirksamkeitserwartungen beeinflussen auch Ausdauer und investierte Anstrengung.', True,
   'Außerdem Auswahl von Aufgaben und Schwierigkeitsniveau sowie Lern- und Leistungsverhalten insgesamt.', 'Selbstwirksamkeit Ausdauer')
tf('p4b-tf-14', SB, 'Prüfungsängstlichkeit ist als stabile, überdauernde Eigenschaft definiert.', True,
   'Dispositionelle Eigenschaft, in Prüfungssituationen mit Angst zu reagieren.', 'Prüfungsängstlichkeit Trait')
tf('p4b-tf-15', SB, 'Prüfungsangst steigt in der Schulzeit zunächst an und geht gegen Schulende wieder etwas zurück.', True,
   'Laut Entwicklungsgrafik.', 'Prüfungsangst Verlauf')
tf('p4b-tf-16', SB, 'Lern- und Leistungszielorientierung sind gegensätzliche Pole: Wer hohe Leistungsziele hat, hat zwangsläufig niedrige Lernziele.', False,
   'Sie sind <b>keine</b> Pole. Hohe Lern- und hohe Leistungszielorientierung zusammen haben keine ungünstigen Effekte.', 'keine Pole')
tf('p4b-tf-17', SB, 'Die Lernzielorientierung ist zu Schulbeginn hoch und sinkt im Verlauf der Schulzeit.', True,
   'Laut Entwicklungsgrafik.', 'Lernzielorientierung sinkt')
tf('p4b-tf-18', SB, 'Bei hoher Lernzielorientierung wird Misserfolg eher internal und stabil attribuiert.', False,
   'Günstige Attribution: Erfolg → internal, stabil; Misserfolg → <b>external, labil</b>.', 'Attribution Lernzielorientierung')

# ---- 4b Lückentext
gap('p4b-gap-01', SB, 'Nach Spearman wird Intelligenz auf einen {{Generalfaktor|g-Faktor|Generalfaktor g|g}} zurückgeführt; spezielle Fähigkeiten erklären Unterschiede in einzelnen Subtests.',
    'g = gemeinsamer Faktor, s = spezielle Faktoren.', 'Generalfaktor')
gap('p4b-gap-02', SB, 'Die {{fluide}} Intelligenz gilt als angeboren, die {{kristalline|kristallisierte}} Intelligenz wird im Laufe des Lebens erlernt.',
    'Cattell; die kristalline ist von der fluiden abhängig.', 'fluide kristalline')
gap('p4b-gap-03', SB, 'Im CHC-Modell ist Intelligenz {{hierarchisch}} organisiert.',
    'Genereller Faktor → breite Faktoren → spezifische Fähigkeiten.', 'CHC hierarchisch')
gap('p4b-gap-04', SB, 'Das Fähigkeitsselbstkonzept fällt in der Grundschule durch {{sozialen Vergleich|Sozialvergleich|soziale Vergleiche}} ab.',
    'Abfall in der 2. Klasse; das Lehrerurteil wird bedeutsamer.', 'Selbstkonzept sozialer Vergleich')
gap('p4b-gap-05', SB, 'Die Überzeugung, dass eine Handlung zum angestrebten Ziel führt, heißt {{Instrumentalität}}.',
    'Abzugrenzen von der Selbstwirksamkeitserwartung (Handlung durchführen können).', 'Instrumentalität')
gap('p4b-gap-06', SB, 'Die Überzeugung, eine bestimmte Handlung durchführen zu können, heißt {{Selbstwirksamkeitserwartung|Selbstwirksamkeit|Selbstwirksamkeitserwartungen}}.',
    'Sie steigt im Verlauf der Schulzeit.', 'Selbstwirksamkeitserwartung')
gap('p4b-gap-07', SB, 'Die kognitive Komponente der Prüfungsangst heißt {{Besorgtheit}}, die physiologische {{Aufgeregtheit}}.',
    'Besorgtheit: negative Erwartungen. Aufgeregtheit: Zittern, Schwitzen, Übelkeit.', 'Besorgtheit Aufgeregtheit')
gap('p4b-gap-08', SB, 'Ein Blackout bei Prüfungsangst ist eine Beeinträchtigung des {{Abrufs|Abruf|Abrufens}} aus dem Gedächtnis.',
    'Angst bindet kognitive Kapazitäten.', 'Blackout Abruf')
gap('p4b-gap-09', SB, 'Bei der Leistungszielorientierung wird die eigene Fähigkeit durch {{Sozialvergleich|sozialen Vergleich}} beurteilt.',
    'Bei der Lernzielorientierung: objektive Kriterien oder individueller Lernfortschritt.', 'Leistungsziel Sozialvergleich')
gap('p4b-gap-10', SB, 'Je besser die Klasse, desto niedriger das Fähigkeitsselbstkonzept des Einzelnen: Das ist der {{Big-Fish-Little-Pond-Effekt|Big-Fish-Little-Pond|Big Fish Little Pond|Big-Fish-Little-Pond Effekt}}.',
    'Wirkung der Referenzgruppe auf das Selbstkonzept.', 'Big-Fish-Little-Pond')
