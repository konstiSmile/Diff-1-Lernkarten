# Psycho 2 · Diagnostische Psychologie · Teil 3 (Diagnostische Entscheidung, Normwerte, Normskalen)
# Quelle: Zusammenfassung „Diagnostik Teil 3“ von Konsti (aus „2025 Diagnostik Teil 3 KURZ“, 25 Folien).
# Klärungen von Konsti (21. Nov. 2026, Chat 1.17):
# - Ein Kapitel (d3), kein Vermerk „nicht klausurrelevant“.
# - Übliche Bereiche der Normskalen: Folie nennt „0 bis 145“ / „0 bis 80“ (Tippfehler) → korrigiert abfragen
#   (IQ 55–145, T 20–80), auf der Karte Hinweis auf die Folienangabe. Prozentränge aus der Entsprechungstabelle
#   (Folie 23), nicht aus der IQ-Grafik (Folie 3).
# - Legasthenie: Prinzip (1,3 SD, gemeinsame Normskala) und T-Rechnung der Folie (55 − 40 = 1,5 SD) abfragen;
#   Rohwerte (IQ 110, 40 von 60, SD 8) nur auf der Karte.
# - Effektivität/Sensitivität/Spezifität: Folienbeispiel (80 / 92,3 / 57,1 %) nur anzeigen, im Test neue Zahlen.
#   Umrechnungen zwischen Skalen nur über die Tabellenpunkte (±1/2/3 SD), keine freie z-Formel.
# - WISC-Folie: Aussage „Gesamtstichprobe groß, Teilstichproben Österreich/Schweiz sehr klein“ wird abgefragt.
# - [ERGÄNZUNG]-Stellen der Zusammenfassung nur als Hinweis auf Karten, nie in Testfragen.
# MC im echten Klausurformat: genau 4 Optionen, 1–4 richtig. Richtige Optionen sind mit „*“ markiert.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

def H(t):
    return '<p><i>Hinweis (nicht auf der Folie): ' + t + '</i></p>'

CO = 'Teil 3 · Cut-off-Werte'
EF = 'Teil 3 · Entscheidungsfehler'
NW = 'Teil 3 · Normwerte'
NS = 'Teil 3 · Normskalen'

CARDS3 = [
    # ---------------------------------------------------------- Cut-off-Werte
    C('entscheidung', CO, 'Wofür werden Ergebnisse diagnostischer Verfahren häufig genutzt, und was ist dafür <b>Voraussetzung</b>?',
      '<p>Für <b>Platzierungs- oder Klassifizierungsentscheidungen</b>.</p><p>Voraussetzung: die <b>Bestimmung von Cut-off-Werten</b>.</p><p>Kennwerte für die Güte diagnostischer Entscheidungen: <b>Effektivität, Sensitivität, Spezifität</b>.</p>',
      'diagnostische Entscheidung Platzierung Klassifizierung Cut-off Voraussetzung Effektivität Sensitivität Spezifität'),
    C('cutoff', CO, 'Was ist ein <b>Cut-off-Wert</b>?',
      '<p>Ein „<b>festgelegter Testtrennwert</b>, der z. B. kranke Personen von gesunden Personen hinsichtlich des zu testenden Merkmals trennt und somit eine <b>Interpretation des Testergebniswertes</b> ermöglicht.“</p><p>Der Cut-off-Wert <b>teilt eine Stichprobe in Gruppen</b> auf.</p>',
      'Cut-off-Wert Definition Testtrennwert krank gesund Gruppen'),
    C('iq-gruppen', CO, 'Welche <b>Gruppen</b> ergeben die Cut-offs bei IQ 70, 85, 115 und 130?',
      '<table><tr><th>IQ</th><th>Gruppe</th></tr><tr><td>unter 70</td><td>minderbegabt</td></tr><tr><td>70–85</td><td>unterdurchschnittlich begabt</td></tr><tr><td>85–115</td><td>normal begabt</td></tr><tr><td>115–130</td><td>überdurchschnittlich begabt</td></tr><tr><td>über 130</td><td>hochbegabt</td></tr></table><p>Beschriftung der Grafik: unter 85 „außergewöhnlich niedrig“, ab 115 „außergewöhnlich hoch“.</p>'
      + H('Die Grafik dieser Folie nennt auch Prozentränge, teils gerundet bzw. ungenau. Maßgeblich sind die Werte der Entsprechungstabelle (Karte „Entsprechungstabelle“).'),
      'IQ Cut-off 70 85 115 130 minderbegabt normal begabt hochbegabt Gruppen'),
    C('grenzgaenger', CO, 'Was ist das <b>generelle Problem</b> beim Setzen von Cut-off-Werten?',
      '<p>Beispiel: Wo fängt Minderbegabung an (Cut-off bei 70)?</p><ul><li><b>Grenzgänger</b> sind am <b>häufigsten</b>.</li><li>Bei ihnen ist die Diagnose am <b>wenigsten sicher</b>.</li><li><b>Je sicherer die Diagnose, je stärker das Symptom, desto seltener der Fall.</b></li></ul>',
      'Cut-off Problem Grenzgänger häufig Diagnose unsicher Symptom selten'),

    # ---------------------------------------------------------- Entscheidungsfehler
    C('schuleingang', EF, 'Wie lautet das Beispiel <b>Schuleingangstest</b>?',
      '<ul><li><b>100 Kinder</b> nehmen teil: <b>75</b> als geeignet, <b>25</b> als ungeeignet diagnostiziert.</li><li><b>Alle</b> werden eingeschult.</li><li>Am Ende der 1. Klasse: <b>15</b> der laut Test geeigneten Kinder müssen wiederholen, <b>5</b> der laut Test ungeeigneten werden versetzt.</li></ul><p>Daraus ergibt sich die Vierfeldertafel: rp 60, fn 5, fp 15, rn 20.</p>',
      'Schuleingangstest Beispiel 100 Kinder geeignet ungeeignet wiederholen versetzt'),
    C('vierfelder', EF, 'Wie ist die <b>Vierfeldertafel</b> aufgebaut?',
      '<table><tr><th>Wahrer Wert ↓ / Diagnose →</th><th>geeignet</th><th>nicht geeignet</th></tr><tr><td>geeignet</td><td><b>rp</b> (richtig positiv)</td><td><b>fn</b> (falsch negativ)</td></tr><tr><td>nicht geeignet</td><td><b>fp</b> (falsch positiv)</td><td><b>rn</b> (richtig negativ)</td></tr></table><ul><li><b>Zeilen</b> = wahrer Wert (Kriterium, hier Erfolg in der 1. Klasse)</li><li><b>Spalten</b> = Diagnose (Testwert)</li><li><b>Fehler</b> sind die Felder <b>fp</b> und <b>fn</b>.</li></ul><p>Im Schuleingangs-Beispiel: rp 60, fn 5, fp 15, rn 20 (Summe 100).</p>',
      'Vierfeldertafel richtig positiv falsch negativ falsch positiv richtig negativ rp fn fp rn wahrer Wert Diagnose'),
    C('fehlerarten', EF, 'Was ist der <b>Fehler erster Art</b> (α-Fehler), was der <b>Fehler zweiter Art</b> (β-Fehler)?',
      '<ul><li><b>Fehler 1. Art (α-Fehler) = falsch positiv (fp)</b>: Personen werden als <b>geeignet</b> bezeichnet, obwohl sie <b>ungeeignet</b> sind.</li><li><b>Fehler 2. Art (β-Fehler) = falsch negativ (fn)</b>: Personen werden als <b>ungeeignet</b> diagnostiziert, obwohl sie eigentlich der <b>geeigneten</b> Gruppe angehören.</li></ul>',
      'Fehler erster Art zweiter Art Alpha-Fehler Beta-Fehler falsch positiv falsch negativ Zuordnungsfehler'),
    C('effektivitaet', EF, 'Was ist die <b>Effektivität</b> und wie wird sie berechnet?',
      '<p>„Verhältnis von <b>erreichtem Ziel zu definiertem Ziel</b> in %“ (<b>Zielerreichungsgrad</b>).</p><p><b>Effektivität = (rp + rn) / (rp + fn + fp + rn) × 100</b></p><p>Schuleingangs-Beispiel: (60 + 20) / 100 × 100 = <b>80</b> → 80 % der durch diesen Test getroffenen Entscheidungen sind richtig.</p>',
      'Effektivität Formel Zielerreichungsgrad richtige Entscheidungen'),
    C('sensitivitaet', EF, 'Was ist die <b>Sensitivität</b> und wie wird sie berechnet?',
      '<p>Synonyme: <b>Richtig-Positiv-Rate, Empfindlichkeit, Trefferquote</b>.</p><p>Anteil der <b>korrekt als positiv</b> klassifizierten Objekte an der Gesamtheit der <b>tatsächlich positiven</b> Objekte.</p><p><b>Sensitivität = rp / (rp + fn) × 100</b></p><p>Beispiel: 60 / 65 × 100 = <b>92,3</b> → Der Test identifiziert 92,3 % der Geeigneten korrekt.</p>',
      'Sensitivität Formel Richtig-Positiv-Rate Empfindlichkeit Trefferquote'),
    C('spezifitaet', EF, 'Was ist die <b>Spezifität</b> und wie wird sie berechnet?',
      '<p>Synonyme: <b>Richtig-Negativ-Rate, kennzeichnende Eigenschaft</b>.</p><p>Anteil der <b>korrekt als negativ</b> klassifizierten Objekte an der Gesamtheit der <b>in Wirklichkeit negativen</b> Objekte.</p><p><b>Spezifität = rn / (rn + fp) × 100</b></p><p>Beispiel: 20 / 35 × 100 = <b>57,1</b> → Der Test identifiziert 57,1 % der nicht Geeigneten korrekt.</p>'
      + H('Merkhilfe: Sensitivität bezieht sich auf die Zeile „wahrer Wert geeignet/positiv“, Spezifität auf die Zeile „wahrer Wert nicht geeignet/negativ“.'),
      'Spezifität Formel Richtig-Negativ-Rate kennzeichnende Eigenschaft'),
    C('streudiagramm', EF, 'Wo liegen die <b>vier Felder</b> im Streudiagramm mit zwei Cut-off-Linien?',
      '<p>x-Achse: Prädiktor (Schuleingangstest), y-Achse: Erfolg in der 1. Klasse. <b>Senkrechte</b> Linie = Cut-off des Tests (bei 40: links „Eignung nein“, rechts „Eignung ja“), <b>waagrechte</b> Linie = Cut-off Erfolg 1. Klasse.</p><table><tr><th>Lage</th><th>Feld</th></tr><tr><td>oben rechts</td><td><b>rp</b> – Test geeignet, Klasse erfolgreich</td></tr><tr><td>oben links</td><td><b>fn</b> – Test nicht geeignet, aber erfolgreich</td></tr><tr><td>unten links</td><td><b>rn</b> – Test nicht geeignet, nicht erfolgreich</td></tr><tr><td>unten rechts</td><td><b>fp</b> – Test geeignet, aber nicht erfolgreich</td></tr></table>',
      'Streudiagramm Cut-off-Linie senkrecht waagrecht vier Felder oben rechts unten links'),
    C('cutoff-hoeher', EF, 'Wie verbessert man die <b>Spezifität</b> durch Verschieben des Cut-offs?',
      '<p>Cut-off in den Bereich der <b>Eignung (rp)</b> verschieben, also <b>strenger/höher</b> (im Beispiel von 40 auf 60).</p><ul><li>Wahrscheinlichkeit für <b>rp sinkt</b>, für <b>rn steigt</b>.</li><li>„Je höher die Spezifität, desto sicherer werden alle <b>rn</b> erfasst.“</li><li>In der Grafik: <b>weniger fp</b>, dafür deutlich <b>mehr fn</b>.</li></ul>',
      'Cut-off verschieben höher strenger Spezifität verbessern weniger falsch positiv mehr falsch negativ'),
    C('cutoff-niedriger', EF, 'Wie verbessert man die <b>Sensitivität</b> durch Verschieben des Cut-offs?',
      '<p>Cut-off in den Bereich der <b>Nicht-Eignung (rn)</b> verschieben, also <b>lockerer/niedriger</b> (im Beispiel von 40 auf 20).</p><ul><li>Wahrscheinlichkeit für <b>rp steigt</b>, für <b>rn sinkt</b>.</li><li>„Je höher die Sensitivität, desto sicherer werden alle <b>rp</b> erfasst.“</li><li>In der Grafik: <b>weniger fn</b>, dafür deutlich <b>mehr fp</b>.</li></ul><p><b>Kernaussage:</b> Sensitivität und Spezifität hängen über den Cut-off zusammen – verbessert man die eine, verschlechtert sich die andere.</p>',
      'Cut-off verschieben niedriger lockerer Sensitivität verbessern weniger falsch negativ mehr falsch positiv Zusammenhang'),
    C('adhs', EF, 'Beispiel <b>ADHS</b>: Was zeigt der Konzentrationstest über Sensitivität und Spezifität?',
      '<p>Ein Konzentrationstest (KT) wird zur Diagnose von ADHS eingesetzt.</p><ul><li><b>Alle</b> Kinder mit ADHS liegen unter dem Cut-off → <b>hohe Sensitivität</b>.</li><li>Aber auch <b>viele Kinder ohne ADHS</b> liegen unter dem Cut-off → <b>geringe Spezifität</b>.</li></ul>',
      'ADHS Konzentrationstest Sensitivität hoch Spezifität gering'),

    # ---------------------------------------------------------- Normwerte
    C('normwerte', NW, 'Was sind <b>Normwerte</b> (Nebengütekriterium) und was gibt die <b>Normierung</b> an?',
      '<p><b>Vergleich</b> der Ergebnisse diagnostischer Instrumente mit denen einer <b>Referenzpopulation</b> (z. B. IQ von Schüler A verglichen mit der Normalbevölkerung oder mit Abiturienten).</p><p>Die Normierung gibt an, <b>für welche Zielgruppe</b> der Test ein gültiges Messinstrument sein soll.</p><p>Auswertekriterien für 7-Jährige müssen anders sein als für 14-Jährige: 60 von 100 Punkten ergeben bei 7 Jahren IQ 110 – bei 14 Jahren bedeutet <b>derselbe Rohwert etwas anderes</b>.</p>',
      'Normwerte Nebengütekriterium Referenzpopulation Normierung Zielgruppe Rohwert Alter'),
    C('koerperfett', NW, 'Was zeigt die <b>Körperfett-Normtabelle</b> (Frauen)?',
      '<table><tr><th>Alter</th><th>wenig</th><th>normal</th><th>viel</th><th>sehr viel</th></tr><tr><td>10–12</td><td>unter 12</td><td>12–23</td><td>23–30</td><td>über 30</td></tr><tr><td>12–18</td><td>unter 15</td><td>15–25</td><td>25–33</td><td>über 33</td></tr><tr><td>18–30</td><td>unter 20</td><td>20–29</td><td>29–36</td><td>über 36</td></tr><tr><td>30–40</td><td>unter 22</td><td>22–31</td><td>31–38</td><td>über 38</td></tr><tr><td>40–50</td><td>unter 24</td><td>24–33</td><td>33–40</td><td>über 40</td></tr><tr><td>50–60</td><td>unter 26</td><td>26–35</td><td>35–42</td><td>über 42</td></tr><tr><td>60+</td><td>unter 28</td><td>28–37</td><td>37–47</td><td>über 47</td></tr></table><p>(Die Tabelle enthält außerdem Normwerte für Körperwasser und Muskelanteil.)</p><p><b>Kernbeispiel:</b> Frau, 35 Jahre, Wert 20 = <b>wenig</b>; Mädchen, 11 Jahre, Wert 20 = <b>normal</b>. → <b>Derselbe Rohwert wird je nach Normgruppe unterschiedlich interpretiert.</b></p>',
      'Körperfett Normtabelle Frauen Alter Rohwert Normgruppe'),
    C('kleine-stichprobe', NW, 'Was ist das <b>Problem zu kleiner Stichproben</b>?',
      '<p>Bild: In der großen Gruppe (30 Personen) tragen <b>30 %</b> eine Brille, in einer kleinen Teilgruppe (6 Personen) <b>66 %</b>.</p><p>→ <b>Kleine Stichproben können die Verteilung in der Population stark verzerrt abbilden.</b></p>',
      'kleine Stichprobe verzerrt Population Brillenträger'),
    C('wisc', NW, 'Was zeigt die <b>Normierungsstichprobe des WISC</b> (Deutschland, Österreich, Schweiz)?',
      '<ul><li><b>N = 1650</b>, Altersgruppen <b>6 bis 16</b> Jahre (11 Gruppen), je <b>75 Jungen und 75 Mädchen</b> (150 pro Altersgruppe).</li><li>Aufteilung nach Ländern <b>sehr ungleich</b>: Deutschland ca. 58–70 pro Geschlecht und Altersgruppe, <b>Österreich nur 1–9</b>, <b>Schweiz nur 1–10</b>.</li></ul><table><tr><th>Alter</th><th>D (J/M)</th><th>A (J/M)</th><th>CH (J/M)</th></tr><tr><td>6</td><td>67/65</td><td>2/4</td><td>6/6</td></tr><tr><td>7</td><td>64/66</td><td>5/3</td><td>6/6</td></tr><tr><td>8</td><td>66/64</td><td>4/4</td><td>5/7</td></tr><tr><td>9</td><td>65/60</td><td>2/6</td><td>8/9</td></tr><tr><td>10</td><td>66/58</td><td>6/7</td><td>3/10</td></tr><tr><td>11</td><td>63/68</td><td>7/1</td><td>5/6</td></tr><tr><td>12</td><td>63/67</td><td>9/2</td><td>3/6</td></tr><tr><td>13</td><td>70/63</td><td>4/4</td><td>1/8</td></tr><tr><td>14</td><td>67/70</td><td>2/1</td><td>6/4</td></tr><tr><td>15</td><td>66/67</td><td>4/2</td><td>5/6</td></tr><tr><td>16</td><td>70/65</td><td>4/1</td><td>1/9</td></tr></table><p><b>Aussage:</b> Die Gesamtstichprobe ist ausreichend groß, aber die <b>Teilstichproben für Österreich und die Schweiz sind sehr klein</b> (teils nur 1 Kind pro Alters- und Geschlechtsgruppe). Für diese Länder allein wären die Normen nicht aussagekräftig.</p>'
      + H('Gemeint ist die deutschsprachige WISC-IV (HAWIK-IV), normiert 2005/2006. Die Aussage steht nicht wörtlich auf der Folie, sie folgt aus den Zahlen und der Folie davor („zu kleine Stichproben“).'),
      'WISC Normierungsstichprobe 1650 Deutschland Österreich Schweiz Teilstichproben klein'),
    C('normierung', NW, 'Was ist bei der <b>Normierung</b> wichtig, und welche <b>Einflussfaktoren</b> gibt es?',
      '<p>Die <b>Eichstichprobe</b> muss</p><ul><li><b>repräsentativ</b> sein – Faktoren: Alter, Geschlecht, sozioökonomischer Status, Religion, Wohnortgröße, Region usw.</li><li><b>ausreichend groß</b> sein.</li></ul><p><b>Einflussfaktoren</b> (Gründe, warum Normen veralten bzw. nicht übertragbar sind): <b>Kultur, Zeit, gesellschaftliche Veränderungen, Übersetzung in andere Sprachen</b>.</p>',
      'Normierung Eichstichprobe repräsentativ ausreichend groß Einflussfaktoren Kultur Zeit gesellschaftliche Veränderungen Übersetzung'),
    C('testauswahl', NW, 'Was ist bei der <b>Auswahl von Tests</b> in Bezug auf Normen wichtig?',
      '<ul><li>Für welche <b>Referenzgruppen</b> (Alter, Geschlecht, Bildung, Berufe usw.) liegen Normen vor?</li><li>Wie <b>groß und repräsentativ</b> sind die Eichungsstichproben?</li><li>Wie <b>aktuell</b> sind die Normen?</li><li>Welche <b>Art der Normierung</b> liegt vor?<ul><li>(Alters-)<b>Äquivalentnormen</b></li><li><b>Abweichungsnormen</b> (meist bezogen auf eine Normalverteilung)</li><li><b>Prozentrangnormen</b></li></ul></li></ul>',
      'Testauswahl Normen Referenzgruppen aktuell Äquivalentnormen Abweichungsnormen Prozentrangnormen'),

    # ---------------------------------------------------------- Normskalen
    C('transformation', NS, 'Wozu braucht man <b>Normskalen</b>? (Beispiel Legasthenie)',
      '<p>Um eine eindeutige Aussage über die individuelle Merkmalsausprägung zu treffen, braucht man zusätzlich zum Testwert einen <b>Vergleichsmaßstab</b>, an dem der Testwert eingeordnet wird: <b>Normskalen</b>.</p><p><b>Legasthenie</b>: Die Lese-/Rechtschreibfähigkeiten müssen <b>mindestens 1,3 SD unter der Intelligenzleistung</b> liegen.</p><p>Beispiel: IQ = 110 (SD 15); Rechtschreibtest = 40 von 60 Punkten (SD 8) → Legasthenie?</p><ul><li>Problem: Die Werte liegen auf <b>unterschiedlichen Skalen</b> und sind nicht direkt vergleichbar.</li><li>Lösung: <b>Transformation in eine gemeinsame Skala = Normskala</b>.</li></ul>'
      + H('In der Fachliteratur heißt das IQ-Diskrepanzkriterium. Die genaue SD-Grenze unterscheidet sich je nach Leitlinie; für die Klausur gilt der Folienwert 1,3 SD.'),
      'Normskala Transformation Vergleichsmaßstab Legasthenie 1,3 SD unterschiedliche Skalen'),
    C('skalen', NS, 'Welche <b>Mittelwerte und Standardabweichungen</b> haben z-, IQ-, T- und PISA-Werte?',
      '<p>Normskalen mit Verteilungsannahme ermöglichen den <b>Vergleich mehrerer Tests</b> mit unterschiedlichen Mittelwerten, Varianzen oder Standardabweichungen.</p><table><tr><th>Skala</th><th>M</th><th>SD</th><th>Bereich (±3 SD)</th></tr><tr><td>z-Werte</td><td>0</td><td>1</td><td>−3 bis +3</td></tr><tr><td>IQ-Werte</td><td>100</td><td>15</td><td>55 bis 145</td></tr><tr><td>T-Werte</td><td>50</td><td>10</td><td>20 bis 80</td></tr><tr><td>PISA</td><td>500</td><td>100</td><td>–</td></tr></table><p>Auf der Folie steht beim Bereich „0 bis 145“ bzw. „0 bis 80“ – ein Tippfehler; die Übersichtsgrafik zeigt 55–145 bzw. 20–80.</p>'
      + H('Umrechnung: z = (x − M) / SD; IQ = 100 + 15·z; T = 50 + 10·z. T-Werte zwischen 40 und 60 (±1 SD) gelten als durchschnittlich.'),
      'z-Werte IQ-Werte T-Werte PISA Mittelwert Standardabweichung 100 15 50 10 Bereich'),
    C('legasthenie', NS, 'Wie wird im Beispiel <b>Legasthenie</b> mit T-Werten entschieden?',
      '<ul><li>Lese-Rechtschreibtest: <b>T = 40</b>; Intelligenztest: <b>T = 55</b>.</li><li>Differenz: 55 − 40 = 15 T-Punkte = <b>1,5 SD</b> (SD der T-Skala = 10).</li><li>1,5 SD ≥ 1,3 SD → <b>Legasthenie</b>.</li></ul><p>Vorgehen: beide Werte in <b>dieselbe Normskala</b> umrechnen, dann die Differenz in SD mit dem <b>Kriterium 1,3 SD</b> vergleichen.</p>'
      + H('Die beiden Folien passen rechnerisch nicht genau zusammen: IQ 110 entspräche T ≈ 56,7, und für den Rechtschreibtest fehlt der Mittelwert. Am Ergebnis (Legasthenie) ändert das nichts.'),
      'Legasthenie T-Werte Differenz 1,5 SD Kriterium 1,3 SD gleiche Normskala'),
    C('normalverteilung', NS, 'Wie viel Prozent der Personen liegen in den <b>Abschnitten der Normalverteilung</b>?',
      '<table><tr><th>Bereich</th><th>Anteil</th></tr><tr><td>unter −3 SD</td><td>0,13 %</td></tr><tr><td>−3 bis −2 SD</td><td>2,14 %</td></tr><tr><td>−2 bis −1 SD</td><td>13,59 %</td></tr><tr><td>−1 bis 0</td><td>34,13 %</td></tr><tr><td>0 bis +1 SD</td><td>34,13 %</td></tr><tr><td>+1 bis +2 SD</td><td>13,59 %</td></tr><tr><td>+2 bis +3 SD</td><td>2,14 %</td></tr><tr><td>über +3 SD</td><td>0,13 %</td></tr></table>'
      + H('Daraus folgt: ca. 68 % liegen zwischen −1 und +1 SD, ca. 95 % zwischen −2 und +2 SD, ca. 99,7 % zwischen −3 und +3 SD.'),
      'Normalverteilung Prozent Kurvenareal Standardabweichung 34,13 13,59 2,14 0,13'),
    C('entsprechung', NS, 'Wie entsprechen sich <b>SD, Prozentrang, IQ, z- und T-Werte</b>?',
      '<table><tr><th>SD</th><th>PR</th><th>IQ</th><th>z</th><th>T</th></tr><tr><td>−3</td><td>0,1</td><td>55</td><td>−3</td><td>20</td></tr><tr><td>−2</td><td>2,3</td><td>70</td><td>−2</td><td>30</td></tr><tr><td>−1</td><td>15,9</td><td>85</td><td>−1</td><td>40</td></tr><tr><td>0</td><td>50</td><td>100</td><td>0</td><td>50</td></tr><tr><td>+1</td><td>84,1</td><td>115</td><td>+1</td><td>60</td></tr><tr><td>+2</td><td>97,7</td><td>130</td><td>+2</td><td>70</td></tr><tr><td>+3</td><td>99,9</td><td>145</td><td>+3</td><td>80</td></tr></table><p>In der Grafik ist zusätzlich IQ 120 markiert (zwischen +1 und +2 SD).</p>'
      + H('IQ 120 entspricht etwa z = 1,33, T ≈ 63,3, PR ≈ 91.'),
      'Entsprechungstabelle Prozentrang IQ z-Wert T-Wert Standardabweichung Umrechnung'),
    C('prozentrang', NS, 'Was ist ein <b>Prozentrang</b> (Norm ohne Verteilungsannahme)?',
      '<p>Der Prozentrang (PR) gibt an, <b>wie viele Personen der Vergleichsgruppe gleiche oder niedrigere</b> Werte im Test erreicht haben.</p><p>PR 90: <b>90 % aller Gleichaltrigen sind gleich gut oder schlechter</b>.</p><p><b>Achtung:</b> Der PR gibt nur die <b>relative Stellung in einer Gruppe</b> an und sagt nichts über die tatsächliche Leistung aus. Er ist ein <b>Rang und kein Messwert</b>.</p><p><b>Vorteile:</b> anschaulich, leicht zu ermitteln, <b>verteilungsunabhängig</b>.</p>',
      'Prozentrang Prozentrangnorm Rang kein Messwert relative Stellung verteilungsunabhängig PR 90'),
]

ITEMS3 = []
S = 'Diagnostik · Teil 3'
def mc(id, q, options, expl, kw):
    assert len(options) == 4, id
    corr = [i for i, o in enumerate(options) if o.startswith('*')]
    assert 1 <= len(corr) <= 4, id
    opts = [o[1:] if o.startswith('*') else o for o in options]
    ITEMS3.append(dict(id=id, type='mc', q=q, options=opts, correct=corr[0] if len(corr) == 1 else corr, expl=expl, src=S, kw=kw))
def tf(id, statement, answer, expl, kw):
    ITEMS3.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=S, kw=kw))
def gap(id, text, expl, kw):
    ITEMS3.append(dict(id=id, type='gap', text=text, expl=expl, src=S, kw=kw))

# ---- Multiple Choice
mc('pd3-mc-01', 'Wofür ist die <b>Bestimmung von Cut-off-Werten</b> Voraussetzung?',
   ['*für Platzierungsentscheidungen', '*für Klassifizierungsentscheidungen', 'für die Berechnung der Retest-Reliabilität', 'für die Durchführungsobjektivität'],
   'Ergebnisse diagnostischer Verfahren werden häufig für Platzierungs- oder Klassifizierungsentscheidungen genutzt; Voraussetzung sind Cut-off-Werte.', 'Cut-off Voraussetzung')
mc('pd3-mc-02', 'Welche Kennwerte beschreiben laut Folie die <b>Güte diagnostischer Entscheidungen</b>?',
   ['*Effektivität', '*Sensitivität', '*Spezifität', 'Trennschärfe'],
   'Genannt werden Effektivität, Sensitivität und Spezifität.', 'Güte diagnostischer Entscheidungen')
mc('pd3-mc-03', 'Was trifft auf einen <b>Cut-off-Wert</b> zu?',
   ['*Er ist ein festgelegter Testtrennwert.', '*Er teilt eine Stichprobe in Gruppen auf.', '*Er ermöglicht die Interpretation des Testergebniswertes.', 'Er ergibt sich immer genau beim Mittelwert der Normstichprobe.'],
   'Ein Cut-off trennt z. B. kranke von gesunden Personen hinsichtlich des Merkmals. Er liegt nicht zwingend beim Mittelwert (z. B. IQ 70 für Minderbegabung).', 'Cut-off Definition')
mc('pd3-mc-04', 'Ein Kind hat einen IQ von <b>122</b>. Welcher Gruppe wird es nach den Cut-offs der Folie zugeordnet?',
   ['*überdurchschnittlich begabt', 'normal begabt', 'hochbegabt', 'unterdurchschnittlich begabt'],
   '115 bis 130 = überdurchschnittlich begabt; über 130 = hochbegabt.', 'IQ Gruppen')
mc('pd3-mc-05', 'Welche Aussagen zum <b>Setzen von Cut-off-Werten</b> treffen laut Folie zu?',
   ['*Grenzgänger sind am häufigsten.', '*Bei Grenzgängern ist die Diagnose am wenigsten sicher.', '*Je stärker das Symptom, desto seltener der Fall.', 'Je sicherer die Diagnose, desto häufiger der Fall.'],
   'Je sicherer die Diagnose, je stärker das Symptom, desto seltener der Fall.', 'Grenzgänger Cut-off Problem')
mc('pd3-mc-06', 'In der <b>Vierfeldertafel</b>: Welche Felder sind <b>Fehler</b>?',
   ['*falsch positiv (fp)', '*falsch negativ (fn)', 'richtig positiv (rp)', 'richtig negativ (rn)'],
   'Fehler sind die Felder fp und fn.', 'Vierfeldertafel Fehler')
mc('pd3-mc-07', 'Was ist der <b>Fehler erster Art (α-Fehler)</b> in der Diagnostik?',
   ['*falsch positiv', '*Eine Person wird als geeignet bezeichnet, obwohl sie ungeeignet ist.', 'falsch negativ', 'Eine Person wird als ungeeignet diagnostiziert, obwohl sie geeignet ist.'],
   'α-Fehler = fp. Der β-Fehler (Fehler 2. Art) = fn: als ungeeignet diagnostiziert, obwohl geeignet.', 'Alpha-Fehler Fehler erster Art')
mc('pd3-mc-08', 'Ein Bewerber wird vom Test als <b>ungeeignet</b> eingestuft, hätte die Stelle aber <b>erfolgreich</b> ausgefüllt. Welcher Fehler liegt vor?',
   ['*falsch negativ', '*Fehler zweiter Art', '*β-Fehler', 'α-Fehler'],
   'Als ungeeignet diagnostiziert, obwohl geeignet = fn = Fehler 2. Art = β-Fehler.', 'Beta-Fehler falsch negativ')
mc('pd3-mc-09', 'In der Vierfeldertafel stehen die <b>Zeilen</b> für … und die <b>Spalten</b> für …',
   ['*Zeilen: wahrer Wert (Kriterium)', '*Spalten: Diagnose (Testwert)', 'Zeilen: Diagnose (Testwert)', 'Spalten: wahrer Wert (Kriterium)'],
   'Im Schuleingangs-Beispiel ist das Kriterium der Erfolg in der 1. Klasse.', 'Vierfeldertafel Zeilen Spalten')
mc('pd3-mc-10', 'Ein Test ergibt: rp = 40, fn = 10, fp = 20, rn = 30. Wie hoch ist die <b>Effektivität</b>?',
   ['*70 %', '80 %', '60 %', '40 %'],
   '(rp + rn) / alle × 100 = (40 + 30) / 100 × 100 = 70 %.', 'Effektivität berechnen')
mc('pd3-mc-11', 'Ein Test ergibt: rp = 40, fn = 10, fp = 20, rn = 30. Wie hoch ist die <b>Sensitivität</b>?',
   ['*80 %', '60 %', '67 %', '70 %'],
   'rp / (rp + fn) × 100 = 40 / 50 × 100 = 80 %.', 'Sensitivität berechnen')
mc('pd3-mc-12', 'Ein Test ergibt: rp = 40, fn = 10, fp = 20, rn = 30. Wie hoch ist die <b>Spezifität</b>?',
   ['*60 %', '75 %', '80 %', '70 %'],
   'rn / (rn + fp) × 100 = 30 / 50 × 100 = 60 %.', 'Spezifität berechnen')
mc('pd3-mc-13', 'Ein Test ergibt: rp = 45, fn = 5, fp = 10, rn = 40. Welche Aussagen stimmen?',
   ['*Effektivität = 85 %', '*Sensitivität = 90 %', '*Spezifität = 80 %', 'Die Spezifität ist höher als die Sensitivität.'],
   'Effektivität (45 + 40) / 100 = 85 %; Sensitivität 45 / 50 = 90 %; Spezifität 40 / 50 = 80 %. Die Sensitivität ist also höher.', 'Effektivität Sensitivität Spezifität berechnen')
mc('pd3-mc-14', 'Welche Formel beschreibt die <b>Sensitivität</b>?',
   ['*rp / (rp + fn) × 100', 'rn / (rn + fp) × 100', '(rp + rn) / (rp + fn + fp + rn) × 100', 'rp / (rp + fp) × 100'],
   'Anteil der korrekt als positiv Klassifizierten an allen tatsächlich Positiven.', 'Sensitivität Formel')
mc('pd3-mc-15', 'Welche Formel beschreibt die <b>Spezifität</b>?',
   ['*rn / (rn + fp) × 100', 'rp / (rp + fn) × 100', 'rn / (rn + fn) × 100', '(rp + rn) / (rp + fn + fp + rn) × 100'],
   'Anteil der korrekt als negativ Klassifizierten an allen in Wirklichkeit Negativen.', 'Spezifität Formel')
mc('pd3-mc-16', 'Welche Begriffe sind <b>Synonyme für Sensitivität</b>?',
   ['*Richtig-Positiv-Rate', '*Empfindlichkeit', '*Trefferquote', 'kennzeichnende Eigenschaft'],
   '„Kennzeichnende Eigenschaft“ und „Richtig-Negativ-Rate“ sind Synonyme für Spezifität.', 'Sensitivität Synonyme')
mc('pd3-mc-17', 'Welche Begriffe gehören zur <b>Spezifität</b>?',
   ['*Richtig-Negativ-Rate', '*kennzeichnende Eigenschaft', 'Trefferquote', 'Zielerreichungsgrad'],
   'Trefferquote = Sensitivität; Zielerreichungsgrad = Effektivität.', 'Spezifität Synonyme')
mc('pd3-mc-18', 'Was beschreibt die <b>Effektivität</b> eines Tests?',
   ['*den Anteil richtiger Entscheidungen an allen Entscheidungen', '*das Verhältnis von erreichtem zu definiertem Ziel in Prozent', 'den Anteil der richtig erkannten Geeigneten an allen Geeigneten', 'den Anteil der richtig erkannten Ungeeigneten an allen Ungeeigneten'],
   'Effektivität = Zielerreichungsgrad = (rp + rn) / alle × 100. Die beiden anderen Optionen beschreiben Sensitivität und Spezifität.', 'Effektivität Definition')
mc('pd3-mc-19', 'Der Cut-off eines Eignungstests wird <b>erhöht</b> (strenger, z. B. von 40 auf 60). Was folgt laut Folie?',
   ['*Die Spezifität verbessert sich.', '*Es gibt weniger falsch Positive.', '*Es gibt deutlich mehr falsch Negative.', 'Die Sensitivität verbessert sich.'],
   'Verschiebung in den Bereich der Eignung: rn werden sicherer erfasst, dafür sinkt die Wahrscheinlichkeit für rp.', 'Cut-off höher Spezifität')
mc('pd3-mc-20', 'Der Cut-off eines Eignungstests wird <b>gesenkt</b> (lockerer, z. B. von 40 auf 20). Was folgt laut Folie?',
   ['*Die Sensitivität verbessert sich.', '*Es gibt weniger falsch Negative.', '*Es gibt deutlich mehr falsch Positive.', 'Die Spezifität verbessert sich.'],
   'Verschiebung in den Bereich der Nicht-Eignung: rp werden sicherer erfasst, dafür sinkt die Wahrscheinlichkeit für rn.', 'Cut-off niedriger Sensitivität')
mc('pd3-mc-21', 'Ein Konzentrationstest erkennt <b>alle</b> Kinder mit ADHS, stuft aber auch <b>viele Kinder ohne ADHS</b> als auffällig ein. Was trifft zu?',
   ['*hohe Sensitivität', '*geringe Spezifität', 'hohe Spezifität', 'geringe Sensitivität'],
   'Alle ADHS-Kinder unter dem Cut-off = hohe Sensitivität; viele Gesunde ebenfalls darunter = geringe Spezifität.', 'ADHS Sensitivität Spezifität')
mc('pd3-mc-22', 'Wo liegen im <b>Streudiagramm</b> (rechts = Test „geeignet“, oben = „erfolgreich“) die einzelnen Felder?',
   ['*oben rechts: richtig positiv', '*oben links: falsch negativ', '*unten rechts: falsch positiv', 'unten links: falsch negativ'],
   'Unten links liegen die richtig Negativen (Test nicht geeignet, nicht erfolgreich).', 'Streudiagramm vier Felder')
mc('pd3-mc-23', 'Was trifft auf <b>Normwerte</b> zu?',
   ['*Sie sind ein Nebengütekriterium.', '*Sie vergleichen Ergebnisse mit denen einer Referenzpopulation.', '*Die Normierung gibt an, für welche Zielgruppe der Test gültig sein soll.', 'Sie sind ein Hauptgütekriterium.'],
   'Normwerte zählen zu den Nebengütekriterien.', 'Normwerte Nebengütekriterium')
mc('pd3-mc-24', 'Was zeigt das Beispiel der <b>Körperfett-Normtabelle</b>?',
   ['*Derselbe Rohwert wird je nach Normgruppe unterschiedlich interpretiert.', '*Ein Wert von 20 ist bei einer 35-jährigen Frau „wenig“, bei einem 11-jährigen Mädchen „normal“.', 'Ein Wert von 20 bedeutet in jedem Alter dasselbe.', 'Normtabellen braucht man nur für Intelligenztests.'],
   'Normen müssen zur Zielgruppe passen (hier: Alter).', 'Körperfett Normtabelle')
mc('pd3-mc-25', 'Was zeigt die <b>Normierungsstichprobe des WISC</b> (Deutschland, Österreich, Schweiz)?',
   ['*Die Gesamtstichprobe ist ausreichend groß.', '*Die Teilstichproben für Österreich und die Schweiz sind sehr klein.', '*Für Österreich oder die Schweiz allein wären die Normen nicht aussagekräftig.', 'Alle drei Länder sind gleich stark vertreten.'],
   'N = 1650, je Altersgruppe 75 Jungen und 75 Mädchen; Österreich und Schweiz teils nur 1 Kind pro Alters- und Geschlechtsgruppe.', 'WISC Normierungsstichprobe')
mc('pd3-mc-26', 'Welche Anforderungen stellt die Folie an eine <b>Eichstichprobe</b>?',
   ['*Sie muss repräsentativ sein.', '*Sie muss ausreichend groß sein.', 'Sie muss nur aus Studierenden bestehen.', 'Sie muss genau 100 Personen umfassen.'],
   'Repräsentativ bezüglich Alter, Geschlecht, sozioökonomischem Status, Religion, Wohnortgröße, Region usw.', 'Eichstichprobe repräsentativ groß')
mc('pd3-mc-27', 'Welche <b>Einflussfaktoren auf die Normierung</b> nennt die Folie?',
   ['*Kultur', '*Zeit', '*gesellschaftliche Veränderungen', '*Übersetzung in andere Sprachen'],
   'Alle vier sind Gründe, warum Normen veralten oder nicht übertragbar sind.', 'Normierung Einflussfaktoren')
mc('pd3-mc-28', 'Welche <b>Arten der Normierung</b> nennt die Folie?',
   ['*(Alters-)Äquivalentnormen', '*Abweichungsnormen', '*Prozentrangnormen', 'Idealnormen'],
   'Abweichungsnormen beziehen sich meist auf eine Normalverteilung.', 'Arten der Normierung')
mc('pd3-mc-29', 'Welche <b>Mittelwerte und Standardabweichungen</b> sind richtig?',
   ['*IQ: M = 100, SD = 15', '*T-Werte: M = 50, SD = 10', '*PISA: M = 500, SD = 100', 'z-Werte: M = 1, SD = 0'],
   'z-Werte haben M = 0 und SD = 1.', 'Normskalen Mittelwert SD')
mc('pd3-mc-30', 'Welchen <b>üblichen Bereich (±3 SD)</b> haben die Skalen?',
   ['*IQ: 55 bis 145', '*T-Werte: 20 bis 80', '*z-Werte: −3 bis +3', 'IQ: 0 bis 145'],
   'Auf der Folie steht „0 bis 145“ bzw. „0 bis 80“ – ein Tippfehler; richtig sind ±3 SD.', 'Normskalen Bereich')
mc('pd3-mc-31', 'Ein IQ von <b>115</b> entspricht …',
   ['*einem T-Wert von 60', '*einem z-Wert von +1', '*einem Prozentrang von 84,1', 'einem T-Wert von 65'],
   '115 liegt genau 1 SD über dem Mittelwert: z = +1, T = 60, PR 84,1.', 'Umrechnung IQ T z Prozentrang')
mc('pd3-mc-32', 'Ein <b>T-Wert von 30</b> entspricht …',
   ['*einem IQ von 70', '*einem z-Wert von −2', '*einem Prozentrang von 2,3', 'einem IQ von 85'],
   'T 30 liegt 2 SD unter dem Mittelwert: z = −2, IQ 70, PR 2,3.', 'Umrechnung T IQ z Prozentrang')
mc('pd3-mc-33', 'Wie viel Prozent der Personen liegen laut Normalverteilungsgrafik <b>zwischen 0 und +1 SD</b>?',
   ['*34,13 %', '13,59 %', '50 %', '2,14 %'],
   'Zwischen −1 und 0 sowie zwischen 0 und +1 SD liegen jeweils 34,13 %.', 'Normalverteilung Prozent')
mc('pd3-mc-34', 'Wie viel Prozent der Personen liegen laut Normalverteilungsgrafik <b>zwischen +1 und +2 SD</b>?',
   ['*13,59 %', '34,13 %', '2,14 %', '0,13 %'],
   'Zwischen +2 und +3 SD liegen 2,14 %, über +3 SD 0,13 %.', 'Normalverteilung Prozent')
mc('pd3-mc-35', 'Im Beispiel <b>Legasthenie</b>: Lese-Rechtschreibtest T = 40, Intelligenztest T = 55. Was folgt?',
   ['*Die Differenz beträgt 1,5 SD.', '*Es liegt Legasthenie vor.', 'Die Differenz beträgt 15 SD.', 'Es liegt keine Legasthenie vor, weil der Rechtschreibwert im Durchschnitt liegt.'],
   '55 − 40 = 15 T-Punkte = 1,5 SD (SD der T-Skala = 10). 1,5 SD ≥ 1,3 SD → Legasthenie.', 'Legasthenie T-Werte')
mc('pd3-mc-36', 'Warum kann man einen IQ-Wert und einen Rechtschreib-Rohwert <b>nicht direkt vergleichen</b>, und was tut man?',
   ['*Die Werte liegen auf unterschiedlichen Skalen.', '*Man transformiert beide in eine gemeinsame Normskala.', '*Dann vergleicht man die Differenz in SD mit dem Kriterium.', 'Man vergleicht einfach die Rohwerte.'],
   'Legasthenie: Lese-/Rechtschreibleistung mindestens 1,3 SD unter der Intelligenzleistung.', 'Legasthenie Normskala Transformation')
mc('pd3-mc-37', 'Was trifft auf den <b>Prozentrang</b> zu?',
   ['*Er gibt die relative Stellung in einer Gruppe an.', '*Er ist ein Rang und kein Messwert.', '*Er ist verteilungsunabhängig.', 'Er sagt etwas über die tatsächliche Leistung aus.'],
   'Der Prozentrang sagt nichts über die tatsächliche Leistung aus. Vorteile: anschaulich, leicht zu ermitteln, verteilungsunabhängig.', 'Prozentrang')
mc('pd3-mc-38', 'Ein Kind hat <b>Prozentrang 90</b>. Was bedeutet das?',
   ['*90 % der Gleichaltrigen sind gleich gut oder schlechter.', 'Das Kind hat 90 % der Aufgaben gelöst.', '90 % der Gleichaltrigen sind besser.', 'Das Kind hat einen IQ von 90.'],
   'Der PR gibt an, wie viele Personen der Vergleichsgruppe gleiche oder niedrigere Werte erreicht haben.', 'Prozentrang 90')

# ---- Richtig/Falsch
tf('pd3-tf-01', 'Grenzgänger sind beim Setzen von Cut-off-Werten am seltensten.', False,
   'Grenzgänger sind am häufigsten, und bei ihnen ist die Diagnose am wenigsten sicher.', 'Grenzgänger')
tf('pd3-tf-02', 'Der Fehler erster Art (α-Fehler) entspricht einem falsch positiven Ergebnis.', True,
   'α-Fehler = fp: als geeignet bezeichnet, obwohl ungeeignet.', 'Alpha-Fehler')
tf('pd3-tf-03', 'Der β-Fehler bedeutet, dass eine ungeeignete Person als geeignet eingestuft wird.', False,
   'Das ist der α-Fehler. Der β-Fehler (fn): als ungeeignet diagnostiziert, obwohl geeignet.', 'Beta-Fehler')
tf('pd3-tf-04', 'Die Effektivität gibt an, wie viel Prozent aller Entscheidungen eines Tests richtig sind.', True,
   'Effektivität = (rp + rn) / alle × 100.', 'Effektivität')
tf('pd3-tf-05', 'Die Sensitivität bezieht sich auf alle tatsächlich Positiven (rp + fn).', True,
   'Sensitivität = rp / (rp + fn) × 100.', 'Sensitivität')
tf('pd3-tf-06', 'Die Spezifität berechnet man als rn / (rn + fn) × 100.', False,
   'Spezifität = rn / (rn + fp) × 100 – bezogen auf alle in Wirklichkeit Negativen.', 'Spezifität Formel')
tf('pd3-tf-07', 'Verschiebt man den Cut-off in den Bereich der Eignung (höher), verbessert sich die Spezifität.', True,
   'Dann werden rn sicherer erfasst; es gibt weniger fp, aber deutlich mehr fn.', 'Cut-off Spezifität')
tf('pd3-tf-08', 'Senkt man den Cut-off, verbessern sich Sensitivität und Spezifität gleichzeitig.', False,
   'Senken verbessert die Sensitivität, dafür gibt es mehr fp – die Spezifität sinkt.', 'Cut-off Sensitivität Spezifität')
tf('pd3-tf-09', '„Je höher die Sensitivität, desto sicherer werden alle rp erfasst.“', True,
   'Entsprechend: Je höher die Spezifität, desto sicherer werden alle rn erfasst.', 'Sensitivität rp')
tf('pd3-tf-10', 'Erkennt ein Konzentrationstest alle ADHS-Kinder, liegen aber auch viele Kinder ohne ADHS unter dem Cut-off, hat er eine hohe Spezifität.', False,
   'Er hat eine hohe Sensitivität, aber eine geringe Spezifität.', 'ADHS Spezifität')
tf('pd3-tf-11', 'Derselbe Rohwert kann in verschiedenen Altersgruppen Unterschiedliches bedeuten.', True,
   'Beispiele: IQ-Test (60 von 100 Punkten bei 7 vs. 14 Jahren) und Körperfett-Normtabelle.', 'Rohwert Normgruppe')
tf('pd3-tf-12', 'Kleine Stichproben bilden die Verteilung in der Population zuverlässig ab.', False,
   'Kleine Stichproben können stark verzerren (Beispiel Brillenträger: 30 % in der großen Gruppe, 66 % in der kleinen).', 'kleine Stichprobe')
tf('pd3-tf-13', 'Bei der WISC-Normierung sind Österreich und die Schweiz ähnlich stark vertreten wie Deutschland.', False,
   'Deutschland ca. 58–70 pro Geschlecht und Altersgruppe, Österreich nur 1–9, Schweiz nur 1–10.', 'WISC Länder')
tf('pd3-tf-14', 'Übersetzung in andere Sprachen ist ein Einflussfaktor auf die Normierung.', True,
   'Weitere: Kultur, Zeit, gesellschaftliche Veränderungen.', 'Normierung Einflussfaktoren')
tf('pd3-tf-15', 'Bei der Testauswahl sollte man auch prüfen, wie aktuell die Normen sind.', True,
   'Außerdem: Referenzgruppen, Größe und Repräsentativität der Eichungsstichprobe, Art der Normierung.', 'Testauswahl Normen')
tf('pd3-tf-16', 'T-Werte haben einen Mittelwert von 50 und eine Standardabweichung von 10.', True,
   'IQ: 100/15; z: 0/1; PISA: 500/100.', 'T-Werte')
tf('pd3-tf-17', 'Ein IQ von 85 entspricht einem T-Wert von 40.', True,
   'Beide liegen 1 SD unter dem Mittelwert (z = −1, PR 15,9).', 'Umrechnung IQ T')
tf('pd3-tf-18', 'Für die Diagnose Legasthenie muss die Lese-/Rechtschreibleistung laut Folie mindestens 1,3 SD unter der Intelligenzleistung liegen.', True,
   'Vergleich erst nach Transformation in eine gemeinsame Normskala.', 'Legasthenie Kriterium')
tf('pd3-tf-19', 'Der Prozentrang ist ein Messwert, der die tatsächliche Leistung angibt.', False,
   'Er ist ein Rang und kein Messwert; er gibt nur die relative Stellung in der Gruppe an.', 'Prozentrang Rang')
tf('pd3-tf-20', 'Prozentrangnormen setzen eine Normalverteilung voraus.', False,
   'Der Prozentrang ist eine Norm ohne Verteilungsannahme (verteilungsunabhängig).', 'Prozentrang verteilungsunabhängig')

# ---- Lückentext (keine Zahlen, Formeln oder Symbole als Antwort)
gap('pd3-gap-01', 'Ein festgelegter Testtrennwert, der z. B. kranke von gesunden Personen trennt, heißt {{Cut-off-Wert|Cut-off|Cutoff-Wert|Cutoff|Trennwert}}.',
    'Er ermöglicht die Interpretation des Testergebniswertes.', 'Cut-off-Wert')
gap('pd3-gap-02', 'Wird eine Person als geeignet bezeichnet, obwohl sie ungeeignet ist, spricht man von einem {{falsch positiven|falsch-positiven}} Ergebnis.',
    'Das ist der Fehler erster Art (α-Fehler).', 'falsch positiv')
gap('pd3-gap-03', 'Die Effektivität wird auch als {{Zielerreichungsgrad}} bezeichnet.',
    'Verhältnis von erreichtem Ziel zu definiertem Ziel in %.', 'Effektivität Zielerreichungsgrad')
gap('pd3-gap-04', 'Die Richtig-Positiv-Rate heißt auch {{Sensitivität|Sensitivitaet}}.',
    'Weitere Synonyme: Empfindlichkeit, Trefferquote.', 'Sensitivität')
gap('pd3-gap-05', 'Die Richtig-Negativ-Rate heißt auch {{Spezifität|Spezifitaet}}.',
    'Synonym: kennzeichnende Eigenschaft.', 'Spezifität')
gap('pd3-gap-06', 'Verschiebt man den Cut-off in den Bereich der Nicht-Eignung, verbessert sich die {{Sensitivität|Sensitivitaet}}.',
    'Dafür gibt es deutlich mehr falsch Positive.', 'Cut-off Sensitivität')
gap('pd3-gap-07', 'Normwerte vergleichen Testergebnisse mit denen einer {{Referenzpopulation|Referenzgruppe|Vergleichsgruppe}}.',
    'Normwerte sind ein Nebengütekriterium.', 'Normwerte Referenzpopulation')
gap('pd3-gap-08', 'Eine Eichstichprobe muss ausreichend groß und {{repräsentativ|repraesentativ}} sein.',
    'Faktoren: Alter, Geschlecht, sozioökonomischer Status, Religion, Wohnortgröße, Region usw.', 'Eichstichprobe')
gap('pd3-gap-09', 'Abweichungsnormen beziehen sich meist auf eine {{Normalverteilung}}.',
    'Weitere Normarten: (Alters-)Äquivalentnormen und Prozentrangnormen.', 'Abweichungsnormen')
gap('pd3-gap-10', 'Um Werte von unterschiedlichen Skalen vergleichbar zu machen, transformiert man sie in eine gemeinsame {{Normskala}}.',
    'Beispiel Legasthenie: IQ und Rechtschreibtest.', 'Normskala Transformation')
gap('pd3-gap-11', 'Der Prozentrang ist ein Rang und kein {{Messwert}}.',
    'Er gibt nur die relative Stellung in einer Gruppe an.', 'Prozentrang Messwert')
gap('pd3-gap-12', 'Ein Vorteil des Prozentrangs: Er ist {{verteilungsunabhängig|verteilungsunabhaengig}}.',
    'Außerdem anschaulich und leicht zu ermitteln.', 'Prozentrang verteilungsunabhängig')
