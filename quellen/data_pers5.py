# Psycho 2 · Persönlichkeitspsychologie · Teil 5, geteilt in Kap. 5a (Stabilität, Genom und Umwelt)
# und 5b (Geschlechtsunterschiede, Persönlichkeit von Lehrkräften).
# Quelle: Zusammenfassung_PersPsych_Teil1-5.md, Teil 5. Klärungen von Konsti (21. Nov. 2026, Chat 1.16):
# - Beide Kapitel tragen den Vermerk „Voraussichtlich nicht klausurrelevant“ (Feld note in build.py).
# - Aus Grafiken geschätzte Werte (Huesmann-Balken, Dunedin-Prozente, Cadoret-Balken, Lehrer-Karikaturen,
#   Mayr-Verläufe, IQ-Korrelationen im Kindesalter) nur als Hinweis auf Karten; abgefragt wird nur das Muster.
# - Tabelle geteilte/nicht geteilte Umwelt: Spaltenköpfe unklar → ohne Zahlen, nur Kernaussage abfragen.
# - Exakt abgefragt werden nur: gemeinsames Genom (100/50/25/12,5/0 %), Heritabilitäts-Grenzen, Rechnen mit d.
#   Alle anderen Studienwerte nur auf Karten, abgefragt höchstens als Muster/Rangfolge. Autoren/Jahre nur anzeigen.
# MC im echten Klausurformat: genau 4 Optionen, 1–4 richtig. Richtige Optionen sind unten mit „*“ markiert.

def C(key, src, q, a, kw=''):
    return dict(key=key, src=src, q=q, a=a, kw=kw)

def H(t):
    return '<p><i>Hinweis (nicht auf der Folie): ' + t + '</i></p>'

ST = 'Teil 5 · Stabilität'
GU = 'Teil 5 · Genom und Umwelt'
GE = 'Teil 5 · Geschlechtsunterschiede'
LK = 'Teil 5 · Lehrkräfte'

# ---------------------------------------------------------------- Kapitel 5a
CARDS_K5A = [
    C('befunde', ST, 'Welche <b>allgemeinen Befunde zur Stabilität</b> von Eigenschaften nennt die Folie?',
      '<ul><li>Die Stabilität zwischen der ersten Messung (T1) und weiteren Messungen <b>sinkt kontinuierlich</b> – je größer der Abstand, desto geringer die Retest-Korrelation.</li><li>Die Stabilität ist für verschiedene Persönlichkeitsbereiche <b>unterschiedlich hoch</b>; <b>am stabilsten ist der IQ</b>.</li><li>Für viele Eigenschaften <b>sinkt die Stabilität mit zunehmend instabiler Umwelt</b>.</li><li>Bei Kindern und Jugendlichen ist die Stabilität meist <b>umso geringer, je jünger die Stichprobe zu T1</b> ist.</li></ul>',
      'Stabilität Retest Abstand IQ am stabilsten instabile Umwelt jünger'),
    C('iq-matrix', ST, 'Was zeigt die Korrelationsmatrix zur <b>Stabilität des IQ bei Kindern von 2–9 Jahren</b>?',
      '<table><tr><th>T1 ↓ / T2 →</th><th>2</th><th>3</th><th>5</th><th>9</th></tr><tr><td>1</td><td>.48</td><td>.40</td><td>.38</td><td>.33</td></tr><tr><td>2</td><td>–</td><td>.74</td><td>.63</td><td>.56</td></tr><tr><td>4</td><td>–</td><td>–</td><td>.80</td><td>.71</td></tr><tr><td>6</td><td>–</td><td>–</td><td>–</td><td>.84</td></tr><tr><td>8</td><td>–</td><td>–</td><td>–</td><td>.90</td></tr></table><p>(Auszug.) Links oben <b>geringe</b> Stabilität (z. B. .31–.48 bei T1 = 1 Jahr), rechts unten <b>hohe</b> (bis .90).</p><p>Merksätze: <b>Je älter bei T1, desto stabiler. Je größer der Abstand, desto geringer die Stabilität.</b></p>',
      'IQ Stabilität Kinder Korrelationsmatrix Alter T1 T2 Abstand'),
    C('aggr-verurteilung', ST, 'Huesmann (1984): Was sagt <b>Aggressivität mit 8 Jahren</b> über <b>Verurteilungen mit 30</b> voraus?',
      '<p>Je <b>aggressiver mit 8 Jahren</b>, desto häufiger <b>Verurteilungen mit 30</b> – bei <b>Männern deutlich stärker</b> als bei Frauen.</p>' + H('Werte aus dem Balkendiagramm abgelesen (niedrige / mittlere / hohe Aggressivität): Männer ca. .20 / .25 / .82, Frauen ca. .02 / .05 / .37.'),
      'Huesmann Aggressivität 8 Jahre Verurteilung 30 Männer Frauen'),
    C('aggr-generationen', ST, 'Huesmann (1984): Wie stabil ist Aggressivität <b>über Generationen</b>?',
      '<table><tr><th>Zusammenhang</th><th>r</th></tr><tr><td>Eltern – Person (30)</td><td>.58</td></tr><tr><td>Eltern – Person (8)</td><td>.55</td></tr><tr><td>Eltern – Kind (8)</td><td>.26</td></tr><tr><td>Person (30) – Person (8)</td><td>.46</td></tr><tr><td>Person (30) – Kind (8)</td><td>.55</td></tr><tr><td>Person (8) – Kind (8)</td><td>.65</td></tr></table><p>Aggressivität ist über die <b>Lebensspanne</b> und über <b>Generationen</b> hinweg bemerkenswert stabil.</p>',
      'Huesmann Aggressivität Generationen Eltern Kind Stabilität'),
    C('vorhersage', ST, 'Welche Frage stellt die Folie zur <b>langfristigen Vorhersagekraft</b> der Persönlichkeit?',
      '<p>Wenn Eigenschaften in der frühen Kindheit <b>instabil</b> sind, müsste ihre Vorhersagekraft gering sein. Lassen sich aus Eigenschaften in der Kindheit <b>trotzdem Prognosen</b> auf die Entwicklung ableiten?</p><p>Antwort gibt u. a. die <b>Dunedin-Studie</b>.</p>',
      'Vorhersagekraft Kindheit Prognose instabil'),
    C('dunedin', ST, 'Wie war die <b>Dunedin-Studie</b> (Caspi & Silva, 1995) aufgebaut? Welche drei Gruppen fand man?',
      '<p><b>90 % eines Geburtsjahrgangs (1139 Kinder)</b> der Stadt Dunedin wurden <b>mit 3 Jahren</b> auf zahlreichen Persönlichkeitsdimensionen beurteilt, später mit <b>21 Jahren</b> erneut untersucht.</p><ol><li><b>Unterkontrollierte</b>: motorische Unruhe, hohe Ablenkbarkeit</li><li><b>Gehemmte</b>: hohe Schüchternheit und Ängstlichkeit</li><li><b>Gut angepasste</b>: keine Auffälligkeiten (<b>Kontrollgruppe</b>)</li></ol>',
      'Dunedin Caspi Silva Unterkontrollierte Gehemmte Gut angepasste 3 Jahre'),
    C('dunedin-befunde', ST, 'Dunedin-Studie: Was zeigte sich <b>mit 21 Jahren</b>? Was sind die Kernaussagen?',
      '<ul><li><b>Gehemmte</b> zeigten am häufigsten <b>Depression</b>.</li><li><b>Unterkontrollierte</b> zeigten häufiger <b>Alkoholismus, Suizidversuche, antisoziale Persönlichkeitsstörung</b> und waren häufiger <b>Rückfall- und Gewalttäter</b>.</li></ul><p><b>Kernaussagen:</b> Unterkontrolliertheit und Gehemmtheit mit 3 Jahren sind <b>Risikofaktoren</b>. <b>Aber: Die meisten Unterkontrollierten und Gehemmten entwickeln sich normal.</b></p>' + H('Depression laut Balkendiagramm grob: Gut angepasste ca. 16 %, Gehemmte ca. 30 %, Unterkontrollierte ca. 20 %.'),
      'Dunedin 21 Jahre Depression Gehemmte Alkoholismus Suizid antisozial Unterkontrollierte Risikofaktor normal'),
    C('meeus', ST, 'Was zeigen die <b>Übergangswahrscheinlichkeiten</b> für Persönlichkeitstypen (Meeus et al., 2011)?',
      '<p>N = 1000, Startalter 12, Typ zu Beginn → Typ 4 Jahre später:</p><table><tr><th>Start ↓ / später →</th><th>Resil.</th><th>Überk.</th><th>Unterk.</th></tr><tr><td>Resilient</td><td><b>.92</b></td><td>.07</td><td>.01</td></tr><tr><td>Überkontrolliert</td><td>.21</td><td><b>.76</b></td><td>.03</td></tr><tr><td>Unterkontrolliert</td><td><b>.50</b></td><td>.34</td><td>.15</td></tr></table><ul><li><b>74 %</b> der Zuordnungen sind stabil.</li><li><b>Zunahme der resilienten Typen.</b></li><li>Übergänge <b>U → R</b> bzw. <b>Ü → R</b> sind häufiger als <b>R → U</b> bzw. <b>R → Ü</b>.</li></ul>',
      'Meeus Übergangswahrscheinlichkeit resilient überkontrolliert unterkontrolliert stabil'),
    C('resilient', ST, 'Was bedeutet <b>resilient</b> bei Meeus et al. (2011)?',
      '<p>Resilient = Typ mit <b>sozial erwünschten Eigenschaften</b>: <b>emotionale Stabilität</b>, <b>kognitive und soziale Kompetenz</b>.</p><p>Die beiden anderen Typen: <b>überkontrolliert</b> und <b>unterkontrolliert</b>.</p>',
      'resilient sozial erwünscht emotionale Stabilität Kompetenz'),
    C('anna', GU, '„<b>Warum ist Anna schüchtern?</b>“ – welche Antworten nennt die Folie, und was folgt daraus?',
      '<p>Jüngste von 9 Geschwistern (keine Zuwendung); wird vom Vater verprügelt; hat es von der Mutter <b>geerbt</b>; Peers ärgern sie; kaum Kontakte; Familie wohnt weit ab auf einem Bauernhof.</p><p>→ Man muss <b>Genom- und Umwelteinflüsse</b> unterscheiden.</p>',
      'Anna schüchtern Ursachen Genom Umwelt geerbt'),
    C('differenziell', GU, 'Was kennzeichnet die <b>differenzielle Perspektive</b> auf Genom und Umwelt?',
      '<ul><li>Gesucht werden <b>Einflüsse, die Personen derselben Population unterschiedlich machen</b>.</li><li>Erklärt werden <b>nicht Eigenschaftswerte einer Person</b>, sondern einer <b>Population</b> (Unterschiede/Varianz).</li><li>Gesucht sind <b>Prädiktoren</b>, mit denen die Eigenschaft möglichst hoch korreliert.</li><li><b>Eine kausale Interpretation ist nicht möglich</b> (Beispiel: Aggressivität der Mutter, des Kindes, des Vaters).</li></ul>',
      'differenzielle Perspektive Population Varianz Prädiktoren nicht kausal'),
    C('geno-phaeno', GU, 'Was ist der Unterschied zwischen <b>Genotyp</b> und <b>Phänotyp</b>?',
      '<ul><li><b>Genotyp</b>: <b>Gesamtheit der genetischen Ausstattung</b> eines Individuums, repräsentiert durch die <b>DNA</b>.</li><li><b>Phänotyp</b>: <b>Gesamtheit aller Merkmale</b> eines Individuums.</li></ul>',
      'Genotyp Phänotyp DNA Merkmale'),
    C('heritabilitaet', GU, 'Was ist die <b>Heritabilität (h²)</b>?',
      '<p><b>Schätzwert des durchschnittlichen Anteils genetisch bedingter Varianz an der Gesamtvarianz</b> eines Verhaltens <b>in einer Population</b>; die Varianz besteht aus Anteilen von <b>Genom und Umwelt</b>.</p><p><b>Wichtig: nur Schätzungen von Durchschnittswerten!</b></p><p>Beispiel der Folie: Intelligenz h² = .50 → 50 % der <b>Unterschiede</b> in der Intelligenz sind genetisch bedingt.</p>' + H('Gemeint sind 50 % der Varianz in der Population, nicht „50 % der Intelligenz einer Person“.'),
      'Heritabilität h² Varianz Population Schätzwert Durchschnitt Intelligenz'),
    C('h2-regeln', GU, 'Wann <b>steigt</b>, wann <b>sinkt</b> die Heritabilität?',
      '<ul><li>Werden die <b>eigenschaftswirksamen Umwelten</b> der Populationsmitglieder <b>homogener</b> → genetischer Einfluss steigt → <b>h² steigt</b>.</li><li>Werden die <b>eigenschaftswirksamen genetischen Unterschiede geringer</b> → Umwelteinfluss steigt → <b>h² sinkt</b>.</li></ul>',
      'Heritabilität steigt sinkt homogene Umwelt genetische Unterschiede'),
    C('genom-anteile', GU, 'Wie viel <b>Genom</b> teilt eine Person mit ihren Verwandten?',
      '<table><tr><th>Verwandtschaft</th><th>Genom</th></tr><tr><td>Eineiiger Zwilling</td><td><b>100 %</b></td></tr><tr><td>Eltern, Geschwister</td><td><b>50 %</b></td></tr><tr><td>Halbgeschwister, Großeltern, Tanten, Onkel, Nichten, Neffen</td><td><b>25 %</b></td></tr><tr><td>Cousinen, Cousins</td><td><b>12,5 %</b></td></tr><tr><td>Partner, Adoptiveltern</td><td><b>0 %</b></td></tr></table>',
      'gemeinsames Genom Zwilling Eltern Geschwister Halbgeschwister Großeltern Cousin Partner Adoptiveltern Prozent'),
    C('h2-grenzen', GU, 'Ab wann gilt eine Heritabilität als <b>hoch, mittel, gering</b>?',
      '<ul><li><b>Hoch</b>: über 0,45</li><li><b>Mittel</b>: 0,2 bis 0,4</li><li><b>Gering</b>: 0,01 bis 0,15</li></ul>',
      'Heritabilität hoch mittel gering Grenzen'),
    C('methoden', GU, 'Welche drei <b>Methoden der Verhaltensgenetik</b> gibt es?',
      '<table><tr><th>Methode</th><th>Prinzip</th></tr><tr><td><b>Zwillingsstudie</b></td><td>Eineiige Zwillinge teilen <b>100 % der Gene und 100 % der Umwelt</b> (Vergleich eineiig vs. zweieiig).</td></tr><tr><td><b>Adoptionsstudie</b></td><td>Adoptivkinder teilen mit ihren <b>leiblichen Geschwistern 50 % der Gene, aber 0 % der Umwelt</b>.</td></tr><tr><td><b>Kombinationsstudie</b></td><td>Eineiige Zwillinge, die <b>getrennt bei Adoptiveltern</b> aufwachsen: <b>100 % der Gene, 0 % der Umwelt</b>.</td></tr></table>' + H('Mit den Adoptiveltern teilen Adoptivkinder 0 % der Gene, aber die Umwelt.'),
      'Verhaltensgenetik Zwillingsstudie Adoptionsstudie Kombinationsstudie getrennt aufgewachsen'),
    C('korrelationen', GU, 'Wie ähnlich sind sich <b>Verwandte</b> in Intelligenz und Big Five (McCartney et al., 1997; Plomin et al., 1980)?',
      '<table><tr><th></th><th>EZ</th><th>ZZ</th><th>LG</th><th>AG</th></tr><tr><td>Intelligenz</td><td><b>.81</b></td><td>.59</td><td>.49</td><td>.25</td></tr><tr><td>Extraversion</td><td>.51</td><td>.19</td><td>.20</td><td>−.03</td></tr><tr><td>Neurotizismus</td><td>.54</td><td>.19</td><td>.14</td><td>.07</td></tr><tr><td>Gewissenh.</td><td>.42</td><td>.17</td><td>.19</td><td>.02</td></tr><tr><td>Verträglichk.</td><td>.49</td><td>.28</td><td>.20</td><td>.06</td></tr><tr><td>Offenheit</td><td>.47</td><td>.23</td><td>.24</td><td>.09</td></tr></table><p>EZ = eineiige, ZZ = zweieiige Zwillinge, LG = leibliche Geschwister, AG = Adoptivgeschwister.</p><ul><li><b>Eineiige Zwillinge ähneln sich am meisten</b>, <b>Adoptivgeschwister am wenigsten</b> (nahe null).</li><li><b>Intelligenz</b> hat in allen Gruppen die <b>höchsten</b> Korrelationen.</li><li>Teilweise große Unterschiede zwischen Heritabilitäten, zurückzuführen auf unterschiedliche <b>Vererblichkeit von Allelkombinationen</b>.</li></ul>',
      'Zwillinge Geschwister Adoptivgeschwister Korrelation Intelligenz Big Five McCartney Plomin Allelkombinationen'),
    C('iq-kindheit', GU, 'Wie entwickeln sich die <b>IQ-Korrelationen</b> von Zwillingen und Geschwistern <b>im Verlauf der Kindheit</b>?',
      '<p>Grafik über Monate (0–36) und Jahre (4–16):</p><ul><li><b>Eineiige Zwillinge</b> am höchsten.</li><li><b>Zweieiige Zwillinge</b> in der Mitte.</li><li><b>Sonstige Geschwister</b> am niedrigsten.</li><li>Mit zunehmendem Alter <b>nähern sich zweieiige Zwillinge und sonstige Geschwister an</b>, eineiige bleiben deutlich höher.</li></ul>' + H('Werte abgelesen: EZ ca. .7 → .9, ZZ ca. .65–.7 → .5, sonstige Geschwister ca. .35 → .5. Laut Zusammenfassung Huesmann (1984).'),
      'IQ Korrelation Kindheit Zwillinge Geschwister Verlauf annähern'),
    C('umwelten', GU, 'Welche Umwelten sind bei Geschwistern <b>eher geteilt</b>, welche <b>eher nicht geteilt</b>?',
      '<table><tr><th>Eher geteilt</th><th>Eher nicht geteilt</th></tr><tr><td>Soziale Schicht</td><td>Schwangerschaftsverlauf</td></tr><tr><td>Wohnumgebung</td><td>Geburtsumstände</td></tr><tr><td>Verwandte und Bekannte der Familie</td><td><b>Geschwisterposition</b></td></tr><tr><td>Qualität der Ehe der Eltern</td><td><b>Elterliche Bevorzugung</b> eines Kindes</td></tr><tr><td>Arbeitsbedingungen der Eltern</td><td>Soziale Beziehungen des Kindes</td></tr><tr><td><b>Erziehungsstil</b></td><td>Kindergarten, Schulklasse</td></tr><tr><td><b>Familienklima</b></td><td>Krankheiten, Unfälle</td></tr><tr><td></td><td>Unterricht</td></tr></table>',
      'geteilte Umwelt nicht geteilte Umwelt Geschwister Erziehungsstil Familienklima Geschwisterposition Bevorzugung Schulklasse'),
    C('umwelt-einfluss', GU, 'Welche Umwelt hat den größeren Einfluss auf Eigenschaftsunterschiede: <b>geteilte</b> oder <b>nicht geteilte</b>?',
      '<p>Der Einfluss der <b>nicht geteilten Umwelt ist größer</b> als der der geteilten.</p><p>Die Folie zeigt dazu eine Tabelle mit Prozentwerten für IQ und die Big Five, getrennt nach Adoptions-, Zwillings- und Kombinationsmethode.</p>' + H('Die Spaltenköpfe der Tabelle sind auf der Folie unübersichtlich; die Zahlen werden deshalb hier nicht wiedergegeben.'),
      'nicht geteilte Umwelt größerer Einfluss Varianz Tabelle'),
    C('umwelt-warum', GU, '<b>Warum</b> wirkt die nicht geteilte Umwelt stärker als die geteilte?',
      '<p>Bisherige Annahme: Die prägenden Umweltbedingungen sind <b>familientypisch</b>, der <b>Erziehungsstil</b> der Eltern ist entscheidend.</p><p><b>Aber:</b></p><ol><li><b>Dieselbe Mutter verhält sich unterschiedlich</b> gegenüber verschiedenen Kindern (= nicht geteilte Umwelt).</li><li><b>Schule und Peers</b> als Einflussfaktoren.</li><li>Das Kind <b>sucht sich eine Umwelt, die zu seiner Persönlichkeit passt</b> → <b>Verstärkung</b> der relevanten Eigenschaften.</li></ol>',
      'warum nicht geteilte Umwelt Mutter unterschiedlich Schule Peers Umwelt suchen Verstärkung'),
    C('interaktion', GU, 'Was ist die <b>Interaktion von Genom und Umwelt</b>? Was zeigte Cadoret et al. (1983)?',
      '<p>Es <b>hängt vom Genom ab, welchen Einfluss Umweltunterschiede haben – und umgekehrt</b>.</p><p>Studie an <b>367 Adoptivkindern</b>: Antisoziales Verhalten je nach genetischem Risikofaktor (−/+) und Umweltfaktor (−/+). Am häufigsten, wenn <b>genetischer Risikofaktor UND ungünstige Umwelt zusammentreffen</b>; die Kombination wirkt deutlich stärker als jeder Faktor allein.</p>' + H('Balkenhöhen abgelesen: −/− ca. 1; nur Umwelt ca. 1,6; nur Gene ca. 1,9; beides ca. 4.'),
      'Interaktion Genom Umwelt Cadoret Adoptivkinder antisozial'),
    C('kovarianz', GU, 'Was ist die <b>Kovarianz von Genom und Umwelt</b>? Welche drei Arten gibt es?',
      '<p>Phänomen: <b>Bestimmte Genome treten gehäuft in bestimmten Umwelten auf.</b></p><table><tr><th>Art</th><th>Definition</th><th>Beispiel</th></tr><tr><td><b>Aktiv</b></td><td>Genetisch beeinflusste Tendenz, passende Umwelten <b>aufzusuchen, zu verändern, herzustellen</b></td><td>Intelligente suchen die Gesellschaft Intelligenter, lesen anspruchsvolle Bücher</td></tr><tr><td><b>Reaktiv</b></td><td>Die <b>Umwelt reagiert</b> auf bestimmte Eigenschaften</td><td>Kinder werden je nach Intelligenz verschiedenen Schulformen zugeteilt</td></tr><tr><td><b>Passiv</b></td><td>Umwelt kommt <b>ohne Zutun</b> der Genomträger zustande</td><td>Intelligente Kinder wachsen in anregenden Umwelten auf, weil ihre Eltern sie aufgrund ihrer eigenen Intelligenz schaffen</td></tr></table>',
      'Kovarianz Genom Umwelt aktiv reaktiv passiv Schulform Eltern'),
    C('kovarianz-alter', GU, 'Welche Art der Genom-Umwelt-Kovarianz <b>nimmt mit dem Alter zu</b>, und was folgt daraus?',
      '<p>Die <b>aktive</b> Genom-Umwelt-Kovarianz nimmt mit dem Alter zu → <b>Anstieg der Heritabilität des IQ</b>.</p>',
      'aktive Kovarianz Alter Heritabilität IQ steigt'),
    C('lebensereignisse', GU, 'Wie bedeutsam sind <b>kritische Lebensereignisse</b> (Insel & Roth, 1985)?',
      '<p>Stärke-Skala, verankert bei <b>Tod naher Angehöriger = 100</b>:</p><table><tr><th>Ereignis</th><th>Stärke</th></tr><tr><td>Tod naher Angehöriger</td><td><b>100</b></td></tr><tr><td>Tod enger Freunde</td><td>73</td></tr><tr><td>Scheidung der Eltern</td><td>65</td></tr><tr><td>Gefängnisaufenthalt</td><td>63</td></tr><tr><td>Schwere Krankheit</td><td>63</td></tr><tr><td>Eheschließung</td><td>58</td></tr><tr><td>Verlust des Arbeitsplatzes</td><td>50</td></tr><tr><td>Schwangerschaft</td><td>45</td></tr><tr><td>Zu viele verpasste Seminare</td><td>25</td></tr><tr><td>Wechsel der Ausbildungsstätte</td><td>24</td></tr></table>',
      'kritische Lebensereignisse Insel Roth Tod Scheidung Gefängnis Krankheit Eheschließung'),
    C('magnus', GU, 'Ist das Auftreten kritischer Lebensereignisse <b>persönlichkeitsabhängig</b> (Magnus et al., 1995)?',
      '<p>Ja. Studenten, Big Five und Lebensereignisse über <b>4 Jahre</b> erfasst:</p><ul><li><b>Extraversion × positive Ereignisse: r = .24</b></li><li>Extraversion × negative Ereignisse: r = .07</li><li><b>Neurotizismus × negative Ereignisse: r = .23</b></li><li>Negative × positive Ereignisse: r = .36</li></ul><p>Extravertierte erleben eher <b>positive</b>, Neurotische eher <b>negative</b> Ereignisse.</p>',
      'Magnus Lebensereignisse persönlichkeitsabhängig Extraversion positiv Neurotizismus negativ'),
    C('verwechslung', GU, '<b>Verwechslungsgefahr</b> Kap. 5a',
      '<ul><li><b>Genotyp</b> (DNA) ≠ <b>Phänotyp</b> (alle Merkmale).</li><li><b>Heritabilität</b> = Anteil genetisch bedingter <b>Varianz in einer Population</b>, nicht der Anteil bei einer einzelnen Person.</li><li>Umwelten <b>homogener</b> → h² <b>steigt</b>; genetische Unterschiede <b>geringer</b> → h² <b>sinkt</b>.</li><li><b>Zwillingsstudie</b> (100 % Gene, 100 % Umwelt) ≠ <b>Adoptionsstudie</b> (50 % Gene, 0 % Umwelt mit leiblichen Geschwistern) ≠ <b>Kombinationsstudie</b> (getrennte EZ: 100 % Gene, 0 % Umwelt).</li><li><b>Interaktion</b> (Wirkung der Umwelt hängt vom Genom ab) ≠ <b>Kovarianz</b> (bestimmte Genome gehäuft in bestimmten Umwelten).</li><li><b>Aktiv</b> (Person sucht Umwelt) ≠ <b>reaktiv</b> (Umwelt reagiert) ≠ <b>passiv</b> (Eltern schaffen Umwelt).</li><li>Dunedin: <b>unterkontrolliert / gehemmt / gut angepasst</b>; Meeus: <b>resilient / überkontrolliert / unterkontrolliert</b>.</li></ul>',
      'Verwechslung Genotyp Phänotyp Heritabilität Interaktion Kovarianz Zwillingsstudie Adoptionsstudie'),
]

# ---------------------------------------------------------------- Kapitel 5b
CARDS_K5B = [
    C('themen', GE, 'Was ist der Unterschied zwischen <b>Geschlechtsunterschieden</b> und <b>Geschlechtsstereotypen</b>?',
      '<ul><li><b>Geschlechtsunterschiede</b>: empirisch gefundene Unterschiede.</li><li><b>Geschlechtsstereotype</b>: Überzeugungen über Unterschiede.</li></ul>',
      'Geschlechtsunterschiede Geschlechtsstereotype empirisch Überzeugungen'),
    C('effektstaerke', GE, 'Was ist die <b>Effektstärke d</b>?',
      '<p><b>d = Mittelwertsdifferenz geteilt durch Standardabweichung.</b></p><p>Beispiel der Folie: IQ Mädchen M = 106, Jungen M = 109, SD = 15 → d = 3 / 15 = <b>0,2</b>.</p>',
      'Effektstärke d Mittelwertsdifferenz Standardabweichung'),
    C('mathe', GE, 'Gibt es Geschlechtsunterschiede bei <b>mathematischen Fähigkeiten</b>?',
      '<ul><li>Erwachsene: <b>Mentale Rotation d = .94</b>, <b>räumliche Wahrnehmung d = .44</b> (Vorteil Männer).</li><li>Metaanalyse (259 Studien): <b>keine Unterschiede im Schulalter</b>, erst im <b>Erwachsenenalter</b>.</li><li><b>Mehr männliche Hoch- und Minderleister</b>.</li><li>Gründe: Vorteile in <b>Rotationsaufgaben</b>; <b>Geschlechtsstereotyp</b> (höheres Fähigkeitsselbstkonzept der Jungen).</li></ul>',
      'mathematische Fähigkeiten mentale Rotation räumliche Wahrnehmung Metaanalyse Schulalter Hochleister Minderleister'),
    C('verbal', GE, 'Gibt es Geschlechtsunterschiede bei <b>verbalen Fähigkeiten</b>?',
      '<p><b>Keine nennenswerten Unterschiede.</b></p><table><tr><th>Fähigkeit</th><th>d</th></tr><tr><td>Alle Tests</td><td>.11</td></tr><tr><td>Wortschatz</td><td>.02</td></tr><tr><td>Analogie</td><td>−.16</td></tr><tr><td>Leseverständnis</td><td>.03</td></tr><tr><td>Sprachlicher Ausdruck</td><td>.33</td></tr><tr><td>Textqualität</td><td>.09</td></tr><tr><td>SAT, Verbaler Wert</td><td>−.03</td></tr></table><p>Auch über die Altersgruppen (unter 6 bis über 25) liegen die d-Werte zwischen .06 und .20.</p>',
      'verbale Fähigkeiten keine Unterschiede Wortschatz Leseverständnis'),
    C('aggression', GE, 'Was sagt die Folie zu Geschlechtsunterschieden bei <b>Aggressivität</b> und <b>Gewalt in Beziehungen</b>?',
      '<ul><li><b>Aggressivität: d = .54</b>, Männer aggressiver (Knight et al., 1996).</li><li><b>Beziehungsaggression</b>: <b>keine Unterschiede im Kindesalter</b> (Crick & Grotpeter, 1995).</li><li><b>Körperliche Gewalt in Beziehungen</b>: Frauen schlagen <b>etwas öfter, aber weniger hart</b> und tragen <b>mehr Verletzungen</b> davon (Archer, 2000).</li></ul>',
      'Aggressivität Männer Beziehungsaggression Kindesalter Gewalt Beziehungen Frauen Verletzungen'),
    C('sexualitaet', GE, 'Männer berichten <b>häufiger Geschlechtsverkehr</b> als Frauen – „wie soll das gehen?“ Welche Erklärungen nennt die Folie?',
      '<ul><li><b>Überschätzung</b> der Männer / <b>Unterschätzung</b> der Frauen</li><li><b>Überzahl von Frauen</b> im Erwachsenenalter</li><li><b>Unterschätzung weiblicher Prostitution</b></li><li><b>Häufigere männliche Homosexualität</b></li></ul>',
      'Sexualität Geschlechtsverkehr Überschätzung Unterschätzung Prostitution Homosexualität'),
    C('lehrer-machen', LK, 'Kann man gute Lehrkräfte „machen“? Welche <b>zwei Positionen</b> stellt die Folie gegenüber?',
      '<ul><li><b>Härle (1983)</b>: Pädagogisches Handeln ist <b>nicht unabhängig von der Person des Lehrers</b> erlernbar oder trainierbar; seine <b>Einstellungen, Orientierungen, Lebensgrundausrichtung</b> bestimmen sein Handeln viel stärker als das Studium.</li><li><b>Mayr & Neuweg (2006)</b>: Der Idealtyp des Lehrers zeichnet sich <b>nicht durch angeborene Persönlichkeitsmerkmale</b>, sondern durch die <b>lebenslange Aneignung pädagogischer Kompetenzen</b> aus. <b>Dass</b> man Lehrer „machen“ kann, scheint außer Frage; strittig ist das <b>Wie</b> im Spannungsfeld von Theorie und Praxis.</li></ul>',
      'Lehrer machen Härle Mayr Neuweg erlernbar angeboren Kompetenzen'),
    C('positionen', LK, 'Welche <b>Positionen zur Lehrerpersönlichkeit</b> unterscheidet Mayr (2014)?',
      '<table><tr><th>Gruppe</th><th>Position</th></tr><tr><td><b>Fast alle Praktiker/innen</b></td><td>Persönlichkeit ist wichtig: „Man hat’s oder man hat’s nicht.“ bzw. „Die Persönlichkeit entwickeln!“</td></tr><tr><td><b>Die meisten Erziehungswissenschaftler/innen</b></td><td>Der Persönlichkeitsansatz ist „historisch überholt“ bzw. <b>gefährlich</b>: „Er betont das Nichtlernbare.“</td></tr><tr><td><b>Viele Psycholog/inn/en</b></td><td>Persönlichkeit ist <b>interessant</b> als Forschungsfeld bzw. <b>nützlich</b> für Beratung und Bewerberauswahl.</td></tr></table>',
      'Mayr Positionen Lehrerpersönlichkeit Praktiker Erziehungswissenschaftler Psychologen'),
    C('ulm', LK, 'Was ergab die Befragung <b>Ulmer Lehrer</b> (Herrmann & Hertramph, 1997)?',
      '<p><b>Fast alle</b> Befragten (unabhängig von Alter, Geschlecht, Schultyp, Berufserfahrung) nennen die <b>Persönlichkeit des Lehrers</b> als Faktor, der entscheidet, ob man den Beruf gut und zufrieden ausübt.</p><p>Damit gilt ein Faktor als elementar, der <b>nicht Teil der Aus-/Fortbildung</b> und <b>nicht erlernbar</b> ist (Herzog, 2001). Diese Position ist von der Erziehungswissenschaft <b>empirisch keinesfalls belegt</b> und wird <b>kontrovers diskutiert</b>.</p>',
      'Ulmer Lehrer Herrmann Hertramph Persönlichkeit nicht erlernbar Herzog kontrovers'),
    C('karikaturen', LK, '„Was ist ein guter Lehrer?“ – welches <b>Big-Five-Muster</b> zeigen die fünf <b>Karikaturen</b>?',
      '<table><tr><th>Typ</th><th>Auffällig</th></tr><tr><td><b>Der Strenge</b></td><td>Gewissenhaftigkeit <b>sehr hoch</b>; Verträglichkeit und Offenheit <b>sehr niedrig</b></td></tr><tr><td><b>Der Eitle</b></td><td>Neurotizismus <b>hoch</b></td></tr><tr><td><b>Der Öko</b></td><td>Extraversion <b>hoch</b>, Gewissenhaftigkeit <b>niedrig</b></td></tr><tr><td><b>Der Kumpel</b></td><td>Extraversion <b>hoch</b>, Verträglichkeit eher hoch, Gewissenhaftigkeit <b>niedrig</b></td></tr><tr><td><b>Der Ängstliche</b></td><td>Extraversion <b>sehr niedrig</b>, Verträglichkeit eher hoch, Gewissenhaftigkeit <b>hoch</b></td></tr></table><p>Die Folien sagen nicht, welcher Typ „gut“ ist – Diskussionsfrage.</p>' + H('Profile aus Balkengrafiken (Skala 0–4) grob abgelesen; nur das Muster ist gemeint.'),
      'guter Lehrer Karikaturen Strenge Eitle Öko Kumpel Ängstliche Big Five Profil'),
    C('schueler', LK, '<b>Das sagen Schüler</b>: Was macht einen guten Lehrer aus?',
      '<p>Ein guter Lehrer liebt seine Arbeit; kann gut erklären; macht abwechslungsreichen Unterricht; ist gut gelaunt; ist streng, aber gerecht; kümmert sich um die Schüler; hat natürliche Autorität.</p>',
      'guter Lehrer Schüler erklären abwechslungsreich streng gerecht Autorität'),
    C('schema', LK, 'Welche <b>Merkmale von Lehrkräften</b> machen laut Schema einen Unterschied, und worauf wirken sie?',
      '<p><b>Kognitive</b> und <b>nicht-kognitive Merkmale</b> → <b>pädagogisch-didaktisches Handeln</b> und <b>Befinden</b>.</p><p>Zur Beschreibung der Lehrerpersönlichkeit dient das <b>Fünf-Faktoren-Modell (NEO-FFI)</b>: N, E, O, A, C. Facetten von C (Gewissenhaftigkeit): Kompetenz, Ordnungsliebe, Pflichtbewusstsein, Leistungsstreben, Selbstdisziplin, Besonnenheit.</p>',
      'Merkmale Lehrkräfte kognitiv nicht-kognitiv pädagogisch-didaktisches Handeln Befinden NEO-FFI'),
    C('mayr-stabil', LK, 'Wie <b>stabil</b> ist die Persönlichkeit von <b>Lehramtsstudierenden</b> (Mayr, 2006)?',
      '<p>Retest-Korrelationen Studienanfang × Studienende (<b>3 Jahre</b> Abstand):</p><p>Neurotizismus .76 · Extraversion .76 · Offenheit .72 · Verträglichkeit .69 · Gewissenhaftigkeit .71</p><p>→ <b>hohe Stabilität</b> aller fünf Faktoren.</p>',
      'Mayr Lehramtsstudierende Stabilität Retest Big Five'),
    C('mayr-erfolg', LK, 'Welche Big-Five-Faktoren hängen bei Lehramtsstudierenden mit <b>Erfolgen</b> und <b>Schwierigkeiten</b> zusammen (Mayr, 2006)?',
      '<table><tr><th>Faktor</th><th>Erfolge</th><th>Schwierigk.</th></tr><tr><td>Extraversion</td><td>.29</td><td>−.22</td></tr><tr><td>Neurotizismus</td><td>−.20</td><td>.23</td></tr><tr><td>Gewissenhaftigkeit</td><td><b>.36</b></td><td><b>−.35</b></td></tr><tr><td>Offenheit</td><td>–</td><td>–</td></tr><tr><td>Verträglichkeit</td><td>–</td><td>–</td></tr></table><ul><li><b>Extraversion</b> und <b>Gewissenhaftigkeit</b>: mehr Erfolge, weniger Schwierigkeiten (Gewissenhaftigkeit am stärksten).</li><li><b>Neurotizismus</b>: weniger Erfolge, mehr Schwierigkeiten.</li><li><b>Offenheit und Verträglichkeit</b>: <b>keine</b> Zusammenhänge.</li></ul>',
      'Mayr Erfolge Schwierigkeiten Extraversion Neurotizismus Gewissenhaftigkeit Offenheit Verträglichkeit'),
    C('urban', LK, 'Welche Faktoren erwiesen sich bei <b>Urban (1984, 1992)</b> als bedeutsam, und was fand <b>Mayr (2002)</b>?',
      '<ul><li><b>Urban</b> (Hauptschullehramtsstudenten und Folgestudie): Für <b>Unterrichtsqualität, Berufszufriedenheit und Berufsbelastung</b> waren <b>Extraversion, Stabilität</b> (Gegenpol zu Neurotizismus) und <b>Gewissenhaftigkeit</b> bedeutsam.</li><li><b>Mayr (2002)</b>, andere Lehrergruppen und längere Prognosezeiträume: <b>Introversion, neurotische Tendenzen und wenig Selbstkontrolle</b> wirken sich <b>generell negativ</b> auf Unterrichtsgestaltung und Lehrer-Schüler-Interaktion aus.</li></ul>',
      'Urban Berufszufriedenheit Berufsbelastung Unterrichtsqualität Extraversion Stabilität Gewissenhaftigkeit Mayr Introversion Selbstkontrolle'),
    C('lpa', LK, 'Welche Dimensionen haben die <b>LPA – Lehrer-Persönlichkeits-Adjektiv-Skalen</b> (Mayr, 1994)?',
      '<table><tr><th>Dimension</th><th>Adjektivpaare</th></tr><tr><td><b>Kontaktbereitschaft</b></td><td>ruhig – lebhaft; sachbezogen – kontaktfreudig; kühl – warmherzig; gerne unabhängig – gerne mit anderen</td></tr><tr><td><b>Stabilität</b></td><td>angespannt – gelassen; an mir zweifelnd – mit mir zufrieden; scheu – selbstsicher; seelisch wenig belastbar – seelisch widerstandsfähig</td></tr><tr><td><b>Selbstkontrolle</b></td><td>wechselhaft – selbstbeherrscht; sorglos – gewissenhaft; unbeherrscht – diszipliniert; leichtlebig – prinzipientreu</td></tr></table>',
      'LPA Lehrer-Persönlichkeits-Adjektiv-Skalen Mayr Kontaktbereitschaft Stabilität Selbstkontrolle'),
    C('veraenderung', LK, 'Wie <b>verändert</b> sich die Persönlichkeit von Lehrkräften in <b>Studium und Beruf</b> (Mayr, Längsschnitt 1995–2005)?',
      '<p>Messzeitpunkte: Anfang Studium, Ende Studium, 3. und 7. Dienstjahr (LPA-Skalen).</p><ul><li><b>Selbstkontrolle steigt</b> und bleibt dann hoch.</li><li><b>Stabilität</b> bleibt etwa gleich bzw. steigt leicht.</li><li><b>Kontaktbereitschaft sinkt</b>.</li></ul>' + H('Werte grob abgelesen: Selbstkontrolle ca. 6,6 → 7,1; Kontaktbereitschaft ca. 6,7 → 6,3.'),
      'Mayr Längsschnitt Veränderung Selbstkontrolle steigt Kontaktbereitschaft sinkt Stabilität'),
    C('mayr2010', LK, 'Wie verlaufen <b>Extraversion, Belastbarkeit und Gewissenhaftigkeit</b> vom Studienbeginn bis zum 7. Berufsjahr (Mayr, 2010)?',
      '<ul><li><b>Extraversion sinkt</b> (vor allem nach dem Studienende).</li><li><b>Belastbarkeit steigt</b> zunächst und bleibt dann etwa konstant.</li><li><b>Gewissenhaftigkeit steigt stark</b>.</li></ul>' + H('z-Werte grob abgelesen: Extraversion ca. +0,1 → −0,15; Gewissenhaftigkeit ca. −0,3 → +0,1.'),
      'Mayr 2010 Extraversion sinkt Belastbarkeit Gewissenhaftigkeit steigt Berufsjahr'),
    C('verwechslung', LK, '<b>Verwechslungsgefahr</b> Kap. 5b',
      '<ul><li><b>d</b> (Effektstärke = Mittelwertsdifferenz / SD) ≠ <b>r</b> (Korrelation).</li><li>Mathe: <b>im Schulalter keine</b> Unterschiede, erst bei Erwachsenen; verbal: <b>keine nennenswerten</b> Unterschiede.</li><li><b>Härle</b>: Lehrerhandeln hängt an der Person ≠ <b>Mayr & Neuweg</b>: Lehrer kann man „machen“, strittig ist das Wie.</li><li>Praktiker: Persönlichkeit wichtig ≠ Erziehungswissenschaftler: überholt/gefährlich ≠ Psychologen: interessant/nützlich.</li><li>Wichtig für Lehrkräfte: <b>Extraversion, Stabilität, Gewissenhaftigkeit</b>; <b>Offenheit und Verträglichkeit</b> ohne Zusammenhang (Mayr, 2006).</li><li>Im Beruf: Selbstkontrolle/Gewissenhaftigkeit <b>steigen</b>, Kontaktbereitschaft/Extraversion <b>sinken</b>.</li></ul>',
      'Verwechslung Effektstärke Korrelation Härle Mayr Lehrkräfte Offenheit Verträglichkeit'),
]

CARDS5 = {'k5a': CARDS_K5A, 'k5b': CARDS_K5B}

# ---------------------------------------------------------------- Tests
ITEMS5 = []
SA = 'Teil 5 · Kap. 5a'
SB = 'Teil 5 · Kap. 5b'
def mc(id, src, q, options, expl, kw):
    assert len(options) == 4, id
    corr = [i for i, o in enumerate(options) if o.startswith('*')]
    assert 1 <= len(corr) <= 4, id
    opts = [o[1:] if o.startswith('*') else o for o in options]
    ITEMS5.append(dict(id=id, type='mc', q=q, options=opts, correct=corr[0] if len(corr) == 1 else corr, expl=expl, src=src, kw=kw))
def tf(id, src, statement, answer, expl, kw):
    ITEMS5.append(dict(id=id, type='tf', statement=statement, answer=answer, expl=expl, src=src, kw=kw))
def gap(id, src, text, expl, kw):
    ITEMS5.append(dict(id=id, type='gap', text=text, expl=expl, src=src, kw=kw))

# ---- 5a Multiple Choice
mc('p5a-mc-01', SA, 'Welche <b>allgemeinen Befunde zur Stabilität</b> von Eigenschaften nennt die Folie?',
   ['*Je größer der Abstand zwischen zwei Messungen, desto geringer die Stabilität.', '*Am stabilsten ist der IQ.', '*Für viele Eigenschaften sinkt die Stabilität mit zunehmend instabiler Umwelt.', 'Alle Persönlichkeitsbereiche sind gleich stabil.'],
   'Die Stabilität ist für verschiedene Persönlichkeitsbereiche <b>unterschiedlich</b> hoch.', 'Stabilität Befunde')
mc('p5a-mc-02', SA, 'Wovon hängt die Stabilität des IQ bei Kindern laut Korrelationsmatrix ab?',
   ['*Je älter das Kind bei der ersten Messung, desto stabiler.', '*Je größer der Abstand zwischen den Messungen, desto geringer die Stabilität.', 'Je jünger das Kind bei der ersten Messung, desto stabiler.', 'Der Abstand zwischen den Messungen spielt keine Rolle.'],
   'Links oben (T1 = 1 Jahr) geringe, rechts unten (benachbarte höhere Altersstufen) hohe Stabilität.', 'IQ Stabilität Kinder')
mc('p5a-mc-03', SA, 'Was zeigen die Befunde von Huesmann (1984) zur <b>Aggressivität</b>?',
   ['*Hohe Aggressivität mit 8 Jahren geht mit mehr Verurteilungen mit 30 Jahren einher.', '*Der Zusammenhang ist bei Männern stärker als bei Frauen.', '*Aggressivität ist auch über Generationen hinweg stabil.', 'Aggressivität mit 8 Jahren sagt spätere Verurteilungen nicht vorher.'],
   'Je aggressiver mit 8, desto häufiger Verurteilungen mit 30, bei Männern deutlich stärker. Auch zwischen Eltern, Person und Kind bestehen deutliche Korrelationen.', 'Huesmann Aggressivität')
mc('p5a-mc-04', SA, 'Welche drei Gruppen bildete die <b>Dunedin-Studie</b> bei den 3-Jährigen?',
   ['*Unterkontrollierte', '*Gehemmte', '*Gut angepasste', 'Resiliente'],
   'Resilient ist ein Typ bei Meeus et al. (2011), nicht in der Dunedin-Studie.', 'Dunedin Gruppen')
mc('p5a-mc-05', SA, 'Dunedin-Studie: Wie werden die <b>Unterkontrollierten</b> mit 3 Jahren beschrieben?',
   ['*motorische Unruhe', '*hohe Ablenkbarkeit', 'hohe Schüchternheit', 'hohe Ängstlichkeit'],
   'Schüchternheit und Ängstlichkeit kennzeichnen die <b>Gehemmten</b>.', 'Unterkontrollierte Unruhe Ablenkbarkeit')
mc('p5a-mc-06', SA, 'Dunedin-Studie: Was zeigte sich <b>mit 21 Jahren</b>?',
   ['*Gehemmte zeigten am häufigsten Depression.', '*Unterkontrollierte zeigten häufiger Alkoholismus und antisoziale Persönlichkeitsstörung.', '*Die meisten Unterkontrollierten und Gehemmten entwickelten sich normal.', 'Gut angepasste waren am häufigsten Gewalttäter.'],
   'Gewalt- und Rückfalltäter waren vor allem unter den Unterkontrollierten. Trotz Risiko entwickelten sich die meisten normal.', 'Dunedin 21 Jahre')
mc('p5a-mc-07', SA, 'Welche Aussagen zu den <b>Übergangswahrscheinlichkeiten</b> (Meeus et al., 2011) stimmen?',
   ['*Die Mehrheit der Zuordnungen ist über 4 Jahre stabil.', '*Der Anteil resilienter Typen nimmt zu.', '*Übergänge von unterkontrolliert zu resilient sind häufiger als von resilient zu unterkontrolliert.', 'Der unterkontrollierte Typ ist der stabilste.'],
   'Am stabilsten ist der resiliente Typ; Unterkontrollierte wechseln häufig, vor allem zu resilient.', 'Meeus Übergänge')
mc('p5a-mc-08', SA, 'Welche Eigenschaften kennzeichnen den <b>resilienten</b> Typ?',
   ['*emotionale Stabilität', '*kognitive Kompetenz', '*soziale Kompetenz', 'hohe Schüchternheit'],
   'Resilient = sozial erwünschte Eigenschaften: emotionale Stabilität, kognitive und soziale Kompetenz.', 'resilient')
mc('p5a-mc-09', SA, 'Was kennzeichnet die <b>differenzielle Perspektive</b> auf Genom und Umwelt?',
   ['*Gesucht werden Einflüsse, die Personen derselben Population unterschiedlich machen.', '*Erklärt wird die Varianz in einer Population, nicht der Wert einer einzelnen Person.', '*Eine kausale Interpretation ist nicht möglich.', 'Sie erklärt, warum eine bestimmte Person einen bestimmten Eigenschaftswert hat.'],
   'Erklärt werden Unterschiede in einer Population über Prädiktoren, nicht Eigenschaftswerte einzelner Personen.', 'differenzielle Perspektive')
mc('p5a-mc-10', SA, 'Welche Zuordnungen stimmen?',
   ['*Genotyp: Gesamtheit der genetischen Ausstattung, repräsentiert durch die DNA', '*Phänotyp: Gesamtheit aller Merkmale eines Individuums', 'Phänotyp: Gesamtheit der genetischen Ausstattung', 'Genotyp: Gesamtheit aller beobachtbaren Merkmale'],
   'Genotyp = genetische Ausstattung (DNA), Phänotyp = alle Merkmale.', 'Genotyp Phänotyp')
mc('p5a-mc-11', SA, 'Intelligenz hat eine Heritabilität von h² = .50. Was bedeutet das?',
   ['*50 % der Unterschiede in der Intelligenz innerhalb der Population sind genetisch bedingt.', '*Es handelt sich um einen Schätzwert für einen Durchschnitt.', 'Die Intelligenz jeder einzelnen Person ist zur Hälfte vererbt.', 'Die Intelligenz ist bei der Hälfte der Menschen vererbt.'],
   'Heritabilität = geschätzter durchschnittlicher Anteil genetisch bedingter Varianz an der Gesamtvarianz in einer Population – keine Aussage über Einzelpersonen.', 'Heritabilität Bedeutung')
mc('p5a-mc-12', SA, 'Wann <b>steigt</b> die Heritabilität einer Eigenschaft?',
   ['*wenn die eigenschaftswirksamen Umwelten in der Population homogener werden', 'wenn die eigenschaftswirksamen genetischen Unterschiede geringer werden', 'wenn die Umwelten in der Population vielfältiger werden', 'wenn sich die Population genetisch angleicht'],
   'Homogenere Umwelten → genetischer Einfluss steigt → h² steigt. Geringere genetische Unterschiede → Umwelteinfluss steigt → h² sinkt.', 'Heritabilität steigt')
mc('p5a-mc-13', SA, 'Wie viel <b>Genom</b> teilt eine Person mit diesen Verwandten?',
   ['*Großeltern: 25 %', '*Cousins: 12,5 %', '*Adoptiveltern: 0 %', 'Halbgeschwister: 50 %'],
   'Halbgeschwister teilen 25 %. 50 % teilt man mit Eltern und (Voll-)Geschwistern.', 'gemeinsames Genom')
mc('p5a-mc-14', SA, 'Wie viel Genom teilt eine Person mit ihrem <b>eineiigen Zwilling</b> und mit ihren <b>Eltern</b>?',
   ['*eineiiger Zwilling 100 %, Eltern 50 %', 'eineiiger Zwilling 100 %, Eltern 25 %', 'eineiiger Zwilling 50 %, Eltern 50 %', 'eineiiger Zwilling 75 %, Eltern 50 %'],
   'Eineiige Zwillinge 100 %, Eltern und Geschwister 50 %.', 'Genom Zwilling Eltern')
mc('p5a-mc-15', SA, 'Welche Einordnungen der Heritabilität stimmen?',
   ['*hoch: über 0,45', '*mittel: 0,2 bis 0,4', '*gering: 0,01 bis 0,15', 'hoch: erst ab 0,8'],
   'Hoch über 0,45, mittel 0,2–0,4, gering 0,01–0,15.', 'Heritabilität Grenzen')
mc('p5a-mc-16', SA, 'Eineiige Zwillinge wachsen <b>getrennt voneinander bei Adoptiveltern</b> auf. Welche Methode ist das, und was teilen sie?',
   ['*Kombinationsstudie', '*100 % der Gene, 0 % der Umwelt', 'Zwillingsstudie mit 100 % der Gene und 100 % der Umwelt', 'Adoptionsstudie mit 50 % der Gene'],
   'Zwillingsstudie: EZ gemeinsam aufgewachsen (100 % Gene, 100 % Umwelt). Adoptionsstudie: Adoptivkind und leibliche Geschwister (50 % Gene, 0 % Umwelt).', 'Kombinationsstudie')
mc('p5a-mc-17', SA, 'Was teilen <b>Adoptivkinder</b> in Adoptionsstudien mit ihren <b>leiblichen Geschwistern</b>?',
   ['*50 % der Gene', '*0 % der Umwelt', '100 % der Gene', '100 % der Umwelt'],
   'Laut Folie 50 % der Gene, aber 0 % der Umwelt.', 'Adoptionsstudie')
mc('p5a-mc-18', SA, 'Welche Aussagen zu den <b>Korrelationen von Eigenschaften nach Verwandtschaft</b> stimmen?',
   ['*Eineiige Zwillinge ähneln sich am meisten.', '*Adoptivgeschwister ähneln sich am wenigsten.', '*Intelligenz hat in allen Gruppen die höchsten Korrelationen.', 'Zweieiige Zwillinge ähneln sich in allen Eigenschaften stärker als eineiige.'],
   'Rangfolge: eineiige Zwillinge &gt; zweieiige Zwillinge bzw. leibliche Geschwister &gt; Adoptivgeschwister (nahe null).', 'Korrelationen Verwandtschaft')
mc('p5a-mc-19', SA, 'Worauf führt die Folie <b>große Unterschiede zwischen Heritabilitäten</b> zurück?',
   ['*auf unterschiedliche Vererblichkeit von Allelkombinationen', 'auf Messfehler der Fragebögen', 'auf unterschiedliche soziale Schichten', 'auf die Geschwisterposition'],
   'Laut Folie: unterschiedliche Vererblichkeit von Allelkombinationen.', 'Heritabilitäten Allelkombinationen')
mc('p5a-mc-20', SA, 'Wie entwickeln sich die <b>IQ-Korrelationen</b> im Verlauf der Kindheit?',
   ['*Eineiige Zwillinge haben durchgehend die höchsten Korrelationen.', '*Zweieiige Zwillinge und sonstige Geschwister nähern sich mit dem Alter an.', 'Sonstige Geschwister haben durchgehend die höchsten Korrelationen.', 'Eineiige und zweieiige Zwillinge nähern sich mit dem Alter an.'],
   'EZ bleiben deutlich höher; ZZ sinken und sonstige Geschwister steigen, bis sie sich annähern.', 'IQ Korrelationen Kindheit')
mc('p5a-mc-21', SA, 'Welche Umwelten sind bei Geschwistern <b>eher geteilt</b>?',
   ['*Erziehungsstil', '*Familienklima', '*soziale Schicht', 'Geschwisterposition'],
   'Die Geschwisterposition ist eher <b>nicht geteilt</b>, ebenso elterliche Bevorzugung, Schulklasse, Krankheiten.', 'geteilte Umwelt')
mc('p5a-mc-22', SA, 'Welche Umwelten sind bei Geschwistern <b>eher nicht geteilt</b>?',
   ['*elterliche Bevorzugung eines Kindes', '*Kindergarten, Schulklasse', '*Geburtsumstände', 'Qualität der Ehe der Eltern'],
   'Die Qualität der Ehe der Eltern ist eher geteilt (wie Wohnumgebung, Arbeitsbedingungen der Eltern).', 'nicht geteilte Umwelt')
mc('p5a-mc-23', SA, 'Warum wirkt die <b>nicht geteilte Umwelt</b> stärker als die geteilte?',
   ['*Dieselbe Mutter verhält sich gegenüber verschiedenen Kindern unterschiedlich.', '*Schule und Peers sind Einflussfaktoren.', '*Kinder suchen sich Umwelten, die zu ihrer Persönlichkeit passen.', 'Der Erziehungsstil ist die entscheidende Umweltbedingung.'],
   'Dass der Erziehungsstil entscheidend sei, war die <b>bisherige</b> Annahme, die die Befunde in Frage stellen.', 'nicht geteilte Umwelt warum')
mc('p5a-mc-24', SA, 'Cadoret et al. (1983) untersuchten antisoziales Verhalten bei Adoptivkindern. Wann trat es am häufigsten auf?',
   ['*wenn genetischer Risikofaktor und ungünstige Umwelt zusammentrafen', 'wenn nur der genetische Risikofaktor vorlag', 'wenn nur die ungünstige Umwelt vorlag', 'wenn keiner der beiden Faktoren vorlag'],
   'Die Kombination wirkt deutlich stärker als jeder Faktor allein – ein Beispiel für die <b>Interaktion</b> von Genom und Umwelt.', 'Cadoret Interaktion')
mc('p5a-mc-25', SA, 'Welche Aussage beschreibt die <b>Interaktion</b> von Genom und Umwelt?',
   ['*Es hängt vom Genom ab, welchen Einfluss Umweltunterschiede haben – und umgekehrt.', 'Bestimmte Genome treten gehäuft in bestimmten Umwelten auf.', 'Die Umwelt reagiert auf bestimmte Eigenschaften.', 'Eltern schaffen eine Umwelt, die zu ihren eigenen Genen passt.'],
   'Gehäuftes Auftreten bestimmter Genome in bestimmten Umwelten ist die <b>Kovarianz</b>; die beiden letzten Optionen sind reaktive bzw. passive Kovarianz.', 'Interaktion Kovarianz')
mc('p5a-mc-26', SA, 'Kinder werden je nach Intelligenz <b>verschiedenen Schulformen</b> zugeteilt. Welche Genom-Umwelt-Kovarianz ist das?',
   ['*reaktive', 'aktive', 'passive', 'keine Kovarianz, sondern Interaktion'],
   'Reaktiv: Die Umwelt reagiert auf bestimmte Eigenschaften.', 'reaktive Kovarianz Schulform')
mc('p5a-mc-27', SA, 'Welche Zuordnungen zu den Arten der <b>Genom-Umwelt-Kovarianz</b> stimmen?',
   ['*Aktiv: Intelligente suchen die Gesellschaft Intelligenter.', '*Passiv: Intelligente Eltern schaffen ihren Kindern eine anregende Umwelt.', '*Die aktive Kovarianz nimmt mit dem Alter zu.', 'Passiv: Die Umwelt reagiert auf die Intelligenz des Kindes.'],
   'Reagiert die Umwelt auf eine Eigenschaft, ist das die <b>reaktive</b> Kovarianz.', 'Kovarianz aktiv passiv Alter')
mc('p5a-mc-28', SA, 'Wie bedeutsam sind <b>kritische Lebensereignisse</b> (Insel & Roth, 1985)?',
   ['*Der Tod naher Angehöriger gilt als bedeutsamstes Ereignis.', '*Der Tod enger Freunde wiegt schwerer als die Eheschließung.', 'Die Eheschließung wiegt schwerer als die Scheidung der Eltern.', 'Ein Wechsel der Ausbildungsstätte wiegt schwerer als eine schwere Krankheit.'],
   'Die Skala ist bei Tod naher Angehöriger verankert; Scheidung der Eltern und schwere Krankheit liegen über der Eheschließung, der Wechsel der Ausbildungsstätte ganz unten.', 'Lebensereignisse Rangfolge')
mc('p5a-mc-29', SA, 'Magnus et al. (1995): Welche Zusammenhänge zwischen Persönlichkeit und <b>Lebensereignissen</b> zeigten sich?',
   ['*Extraversion hing mit positiven Ereignissen zusammen.', '*Neurotizismus hing mit negativen Ereignissen zusammen.', '*Das Auftreten kritischer Lebensereignisse ist persönlichkeitsabhängig.', 'Extraversion hing stärker mit negativen als mit positiven Ereignissen zusammen.'],
   'Extraversion × positive Ereignisse deutlich, × negative kaum; Neurotizismus × negative Ereignisse.', 'Magnus Lebensereignisse')

# ---- 5a Richtig/Falsch
tf('p5a-tf-01', SA, 'Je größer der zeitliche Abstand zwischen zwei Messungen, desto höher ist die Retest-Korrelation einer Eigenschaft.', False,
   'Die Stabilität <b>sinkt</b> mit zunehmendem Abstand.', 'Stabilität Abstand')
tf('p5a-tf-02', SA, 'Bei Kindern ist die Stabilität einer Eigenschaft meist umso geringer, je jünger sie bei der ersten Messung sind.', True,
   'Beispiel IQ: bei T1 = 1 Jahr nur geringe Korrelationen.', 'Stabilität jünger')
tf('p5a-tf-03', SA, 'Laut Folie ist der IQ die stabilste Eigenschaft.', True,
   'Die Stabilität ist für verschiedene Bereiche unterschiedlich hoch, am höchsten beim IQ.', 'IQ stabil')
tf('p5a-tf-04', SA, 'In der Dunedin-Studie wurden die Kinder im Alter von 3 Jahren beurteilt.', True,
   '90 % eines Geburtsjahrgangs, erneut untersucht mit 21 Jahren.', 'Dunedin 3 Jahre')
tf('p5a-tf-05', SA, 'Laut Dunedin-Studie entwickeln sich die meisten unterkontrollierten und gehemmten Kinder problematisch.', False,
   'Beides sind Risikofaktoren, <b>aber die meisten entwickeln sich normal</b>.', 'Dunedin normal')
tf('p5a-tf-06', SA, 'Bei Meeus et al. (2011) wechseln Jugendliche häufiger vom resilienten zum unterkontrollierten Typ als umgekehrt.', False,
   'Umgekehrt: Übergänge U → R bzw. Ü → R sind häufiger; der Anteil resilienter Typen nimmt zu.', 'Meeus Richtung')
tf('p5a-tf-07', SA, 'Die differenzielle Perspektive erlaubt keine kausale Interpretation.', True,
   'Gesucht werden Prädiktoren, die mit der Eigenschaft korrelieren.', 'differenziell nicht kausal')
tf('p5a-tf-08', SA, 'Die Heritabilität gibt an, welcher Anteil einer Eigenschaft bei einer bestimmten Person vererbt ist.', False,
   'Sie ist ein Schätzwert für den durchschnittlichen Anteil genetisch bedingter <b>Varianz in einer Population</b>.', 'Heritabilität Person')
tf('p5a-tf-09', SA, 'Werden die eigenschaftswirksamen genetischen Unterschiede in einer Population geringer, sinkt die Heritabilität.', True,
   'Der Umwelteinfluss steigt dann.', 'Heritabilität sinkt')
tf('p5a-tf-10', SA, 'Mit Partnern und Adoptiveltern teilt man 0 % des Genoms.', True,
   'Cousins 12,5 %, Halbgeschwister, Großeltern, Tanten, Onkel, Nichten, Neffen 25 %.', 'Genom Partner Adoptiveltern')
tf('p5a-tf-11', SA, 'Eine Heritabilität von 0,3 gilt laut Folie als hoch.', False,
   '0,2 bis 0,4 gilt als <b>mittel</b>; hoch ist über 0,45.', 'Heritabilität mittel')
tf('p5a-tf-12', SA, 'In Zwillingsstudien teilen eineiige Zwillinge 100 % der Gene und 100 % der Umwelt.', True,
   'Sie werden mit zweieiigen Zwillingen verglichen.', 'Zwillingsstudie')
tf('p5a-tf-13', SA, 'Adoptivgeschwister ähneln sich in den Big Five kaum.', True,
   'Ihre Korrelationen liegen nahe null.', 'Adoptivgeschwister Big Five')
tf('p5a-tf-14', SA, 'Die geteilte Umwelt hat einen größeren Einfluss auf Eigenschaftsunterschiede als die nicht geteilte.', False,
   'Umgekehrt: Die <b>nicht geteilte</b> Umwelt wirkt stärker.', 'geteilte nicht geteilte Umwelt')
tf('p5a-tf-15', SA, 'Die Geschwisterposition gehört zur eher geteilten Umwelt.', False,
   'Sie ist eher <b>nicht geteilt</b> – jedes Kind hat eine andere Position.', 'Geschwisterposition')
tf('p5a-tf-16', SA, 'Bei der Kovarianz von Genom und Umwelt treten bestimmte Genome gehäuft in bestimmten Umwelten auf.', True,
   'Arten: aktiv, reaktiv, passiv.', 'Kovarianz')
tf('p5a-tf-17', SA, 'Die passive Genom-Umwelt-Kovarianz nimmt mit dem Alter zu.', False,
   'Die <b>aktive</b> nimmt mit dem Alter zu – daher steigt die Heritabilität des IQ.', 'aktive Kovarianz Alter')
tf('p5a-tf-18', SA, 'Laut Magnus et al. (1995) hängt das Auftreten kritischer Lebensereignisse von der Persönlichkeit ab.', True,
   'Extraversion ↔ positive, Neurotizismus ↔ negative Ereignisse.', 'Lebensereignisse persönlichkeitsabhängig')

# ---- 5a Lückentext
gap('p5a-gap-01', SA, 'Die Gesamtheit der genetischen Ausstattung eines Individuums heißt {{Genotyp}}, die Gesamtheit aller seiner Merkmale {{Phänotyp|Phaenotyp}}.',
    'Der Genotyp ist durch die DNA repräsentiert.', 'Genotyp Phänotyp')
gap('p5a-gap-02', SA, 'Der geschätzte durchschnittliche Anteil genetisch bedingter Varianz an der Gesamtvarianz in einer Population heißt {{Heritabilität|Erblichkeit}}.',
    'Abkürzung h².', 'Heritabilität')
gap('p5a-gap-03', SA, 'Werden die eigenschaftswirksamen Umwelten homogener, {{steigt|wächst|nimmt zu}} die Heritabilität.',
    'Der genetische Einfluss steigt dann.', 'Heritabilität homogen')
gap('p5a-gap-04', SA, 'Wachsen eineiige Zwillinge getrennt bei Adoptiveltern auf, spricht man von einer {{Kombinationsstudie|Kombinationsmethode}}.',
    '100 % der Gene, 0 % der Umwelt.', 'Kombinationsstudie')
gap('p5a-gap-05', SA, 'Geschwisterposition und elterliche Bevorzugung gehören zur {{nicht geteilten|nichtgeteilten}} Umwelt.',
    'Sie hat einen größeren Einfluss als die geteilte Umwelt.', 'nicht geteilte Umwelt')
gap('p5a-gap-06', SA, 'Hängt es vom Genom ab, welchen Einfluss Umweltunterschiede haben, spricht man von einer {{Interaktion}} von Genom und Umwelt.',
    'Beispiel: antisoziales Verhalten bei Adoptivkindern (Cadoret et al.).', 'Interaktion')
gap('p5a-gap-07', SA, 'Sucht eine Person aufgrund ihrer Gene passende Umwelten auf, spricht man von {{aktiver}} Genom-Umwelt-Kovarianz.',
    'Sie nimmt mit dem Alter zu.', 'aktive Kovarianz')
gap('p5a-gap-08', SA, 'Den Persönlichkeitstyp mit emotionaler Stabilität sowie kognitiver und sozialer Kompetenz nennt man {{resilient|resilienten Typ|resilienter Typ}}.',
    'Meeus et al. (2011): Sein Anteil nimmt zu.', 'resilient')

# ---- 5b Multiple Choice
mc('p5b-mc-01', SB, 'Was unterscheidet <b>Geschlechtsunterschiede</b> von <b>Geschlechtsstereotypen</b>?',
   ['*Geschlechtsunterschiede sind empirisch gefundene Unterschiede.', '*Geschlechtsstereotype sind Überzeugungen über Unterschiede.', 'Geschlechtsstereotype sind empirisch belegte Unterschiede.', 'Beide Begriffe bedeuten dasselbe.'],
   'Unterschiede = empirisch gefunden, Stereotype = Überzeugungen.', 'Geschlechtsunterschiede Stereotype')
mc('p5b-mc-02', SB, 'Wie berechnet man die <b>Effektstärke d</b>?',
   ['*Mittelwertsdifferenz geteilt durch Standardabweichung', 'Standardabweichung geteilt durch Mittelwertsdifferenz', 'Quadrat des Korrelationskoeffizienten', 'Mittelwert geteilt durch Stichprobengröße'],
   'Das Quadrat des Korrelationskoeffizienten ist das Bestimmtheitsmaß r².', 'Effektstärke d Formel')
mc('p5b-mc-03', SB, 'Gruppe A hat im Mittel 52 Punkte, Gruppe B 48 Punkte, die Standardabweichung beträgt 10. Wie groß ist <b>d</b>?',
   ['*0,4', '4', '0,04', '2,5'],
   'd = (52 − 48) / 10 = 4 / 10 = 0,4.', 'Effektstärke rechnen')
mc('p5b-mc-04', SB, 'Was sagt die Folie zu Geschlechtsunterschieden bei <b>mathematischen Fähigkeiten</b>?',
   ['*Laut Metaanalyse gibt es im Schulalter keine Unterschiede, erst im Erwachsenenalter.', '*Es gibt mehr männliche Hoch- und Minderleister.', '*Bei Erwachsenen ist der Unterschied bei der mentalen Rotation größer als bei der räumlichen Wahrnehmung.', 'Schon im Grundschulalter haben Jungen deutliche Vorteile.'],
   'Mentale Rotation d = .94, räumliche Wahrnehmung d = .44 (Erwachsene). Im Schulalter keine Unterschiede.', 'Mathe Geschlecht')
mc('p5b-mc-05', SB, 'Welche <b>Gründe</b> für Geschlechtsunterschiede in Mathematik nennt die Folie?',
   ['*Vorteile der Männer in Rotationsaufgaben', '*Geschlechtsstereotyp (höheres Fähigkeitsselbstkonzept der Jungen)', 'bessere verbale Fähigkeiten der Mädchen', 'höhere Intelligenz der Jungen'],
   'Laut Folie: Rotationsaufgaben und Geschlechtsstereotyp.', 'Mathe Gründe')
mc('p5b-mc-06', SB, 'Was gilt für Geschlechtsunterschiede bei <b>verbalen Fähigkeiten</b>?',
   ['*Es gibt keine nennenswerten Unterschiede.', 'Frauen sind in allen verbalen Tests deutlich überlegen.', 'Männer sind beim Wortschatz deutlich überlegen.', 'Die Unterschiede sind größer als bei der mentalen Rotation.'],
   'Die d-Werte liegen überwiegend nahe null.', 'verbale Fähigkeiten')
mc('p5b-mc-07', SB, 'Welche Aussagen zu Geschlechtsunterschieden bei <b>Aggression und Gewalt</b> stimmen?',
   ['*Männer sind aggressiver als Frauen.', '*Bei Beziehungsaggression gibt es im Kindesalter keine Unterschiede.', '*Bei körperlicher Gewalt in Beziehungen tragen Frauen mehr Verletzungen davon.', 'Frauen schlagen in Beziehungen seltener, aber härter zu.'],
   'Archer (2000): Frauen schlagen <b>etwas öfter, aber weniger hart</b> und tragen mehr Verletzungen davon.', 'Aggression Gewalt Geschlecht')
mc('p5b-mc-08', SB, 'Männer berichten häufiger Geschlechtsverkehr als Frauen. Welche <b>Erklärungen</b> nennt die Folie?',
   ['*Überschätzung der Männer bzw. Unterschätzung der Frauen', '*Überzahl von Frauen im Erwachsenenalter', '*Unterschätzung weiblicher Prostitution', '*häufigere männliche Homosexualität'],
   'Alle vier stehen auf der Folie.', 'Sexualität Erklärungen')
mc('p5b-mc-09', SB, 'Welche Aussage entspricht der Position von <b>Härle (1983)</b>?',
   ['*Pädagogisches Handeln ist nicht unabhängig von der Person des Lehrers erlernbar.', 'Der Idealtyp des Lehrers zeichnet sich durch lebenslange Aneignung pädagogischer Kompetenzen aus.', 'Dass man Lehrer „machen“ kann, steht außer Frage.', 'Das Studium prägt das pädagogische Handeln stärker als die Person.'],
   'Die Optionen zu Kompetenzaneignung und „Lehrer machen“ entsprechen Mayr & Neuweg (2006).', 'Härle')
mc('p5b-mc-10', SB, 'Was sagen <b>Mayr & Neuweg (2006)</b>?',
   ['*Der Idealtyp des Lehrers zeichnet sich nicht durch angeborene Merkmale aus, sondern durch lebenslange Aneignung pädagogischer Kompetenzen.', '*Strittig ist vor allem das „Wie“ im Spannungsfeld von Theorie und Praxis.', 'Gute Lehrkräfte kann man nicht ausbilden.', 'Einstellungen und Lebensgrundausrichtung bestimmen das Handeln stärker als die Ausbildung.'],
   'Die letzte Option ist Härles Position.', 'Mayr Neuweg')
mc('p5b-mc-11', SB, 'Welche Positionen zur Lehrerpersönlichkeit ordnet Mayr (2014) den <b>Erziehungswissenschaftler/innen</b> zu?',
   ['*Der Persönlichkeitsansatz ist historisch überholt.', '*Der Persönlichkeitsansatz ist gefährlich, weil er das Nichtlernbare betont.', '„Man hat’s oder man hat’s nicht.“', 'Persönlichkeit ist nützlich für die Bewerberauswahl.'],
   '„Man hat’s oder man hat’s nicht“ vertreten Praktiker/innen; „nützlich für Beratung und Bewerberauswahl“ Psycholog/inn/en.', 'Mayr Positionen Erziehungswissenschaft')
mc('p5b-mc-12', SB, 'Was ergab die Befragung <b>Ulmer Lehrer</b> (Herrmann & Hertramph, 1997)?',
   ['*Fast alle nennen die Persönlichkeit als entscheidend für gute und zufriedene Berufsausübung.', '*Das gilt unabhängig von Alter, Geschlecht, Schultyp und Berufserfahrung.', '*Diese Position ist empirisch nicht belegt und wird kontrovers diskutiert.', 'Die meisten halten die Lehrerpersönlichkeit für im Studium erlernbar.'],
   'Die Persönlichkeit gilt den Befragten gerade als <b>nicht erlernbar</b> und nicht Teil der Ausbildung.', 'Ulmer Lehrer')
mc('p5b-mc-13', SB, 'Lehrer-Karikaturen mit Big-Five-Profil: Welche Zuordnungen stimmen?',
   ['*Der Strenge: sehr hohe Gewissenhaftigkeit', '*Der Ängstliche: sehr niedrige Extraversion', 'Der Kumpel: sehr hohe Gewissenhaftigkeit', 'Der Eitle: sehr niedriger Neurotizismus'],
   'Der Kumpel hat hohe Extraversion und <b>niedrige</b> Gewissenhaftigkeit; der Eitle hat <b>hohen</b> Neurotizismus.', 'Karikaturen Big Five')
mc('p5b-mc-14', SB, 'Welche Merkmale eines guten Lehrers nennen laut Folie die <b>Schüler</b>?',
   ['*kann gut erklären', '*ist streng, aber gerecht', '*hat natürliche Autorität', 'gibt wenig Hausaufgaben'],
   'Außerdem: liebt seine Arbeit, abwechslungsreicher Unterricht, gut gelaunt, kümmert sich um die Schüler.', 'guter Lehrer Schüler')
mc('p5b-mc-15', SB, 'Worauf wirken laut Schema die <b>kognitiven und nicht-kognitiven Merkmale</b> von Lehrkräften?',
   ['*pädagogisch-didaktisches Handeln', '*Befinden', 'Intelligenz der Schüler', 'Heritabilität'],
   'Schema: Merkmale → pädagogisch-didaktisches Handeln und Befinden.', 'Schema Lehrkräfte')
mc('p5b-mc-16', SB, 'Mayr (2006): Wie stabil sind die Big Five bei Lehramtsstudierenden zwischen Studienanfang und -ende?',
   ['*Alle fünf Faktoren sind hoch stabil.', 'Nur Gewissenhaftigkeit ist stabil.', 'Alle fünf Faktoren verändern sich stark.', 'Nur Neurotizismus verändert sich nicht.'],
   'Die Retest-Korrelationen über 3 Jahre liegen für alle fünf Faktoren hoch.', 'Mayr Stabilität')
mc('p5b-mc-17', SB, 'Mayr (2006): Welche Zusammenhänge mit <b>Erfolgen und Schwierigkeiten</b> im Lehramtsstudium zeigten sich?',
   ['*Gewissenhaftigkeit: mehr Erfolge, weniger Schwierigkeiten', '*Extraversion: mehr Erfolge, weniger Schwierigkeiten', '*Neurotizismus: weniger Erfolge, mehr Schwierigkeiten', '*Offenheit und Verträglichkeit: keine Zusammenhänge'],
   'Alle vier stimmen; am stärksten hängt Gewissenhaftigkeit zusammen.', 'Mayr Erfolge Schwierigkeiten')
mc('p5b-mc-18', SB, 'Welche Faktoren erwiesen sich bei <b>Urban</b> als bedeutsam für Unterrichtsqualität, Berufszufriedenheit und Berufsbelastung?',
   ['*Extraversion', '*Stabilität (Gegenpol zu Neurotizismus)', '*Gewissenhaftigkeit', 'Offenheit für Erfahrungen'],
   'Offenheit gehört nicht dazu.', 'Urban Faktoren')
mc('p5b-mc-19', SB, 'Was wirkt sich laut <b>Mayr (2002)</b> generell negativ auf Unterrichtsgestaltung und Lehrer-Schüler-Interaktion aus?',
   ['*Introversion', '*neurotische Tendenzen', '*wenig Selbstkontrolle', 'hohe Gewissenhaftigkeit'],
   'Introversion, neurotische Tendenzen und wenig Selbstkontrolle.', 'Mayr 2002 negativ')
mc('p5b-mc-20', SB, 'Welche Dimensionen haben die <b>LPA-Skalen</b> (Mayr, 1994)?',
   ['*Kontaktbereitschaft', '*Stabilität', '*Selbstkontrolle', 'Verträglichkeit'],
   'Drei Dimensionen mit je vier bipolaren Adjektivpaaren.', 'LPA Dimensionen')
mc('p5b-mc-21', SB, 'Zu welcher LPA-Dimension gehört das Adjektivpaar „<b>sorglos – gewissenhaft</b>“?',
   ['*Selbstkontrolle', 'Stabilität', 'Kontaktbereitschaft', 'Offenheit'],
   'Selbstkontrolle: wechselhaft – selbstbeherrscht, sorglos – gewissenhaft, unbeherrscht – diszipliniert, leichtlebig – prinzipientreu.', 'LPA Selbstkontrolle')
mc('p5b-mc-22', SB, 'Wie verändert sich die Persönlichkeit von Lehrkräften vom Studienbeginn bis in die ersten Berufsjahre (Mayr)?',
   ['*Selbstkontrolle bzw. Gewissenhaftigkeit steigt.', '*Kontaktbereitschaft bzw. Extraversion sinkt.', 'Kontaktbereitschaft steigt deutlich.', 'Gewissenhaftigkeit sinkt.'],
   'Laut Verlaufsgrafiken: Selbstkontrolle/Gewissenhaftigkeit steigen, Kontaktbereitschaft/Extraversion sinken.', 'Mayr Veränderung')

# ---- 5b Richtig/Falsch
tf('p5b-tf-01', SB, 'Die Effektstärke d ist die Mittelwertsdifferenz geteilt durch die Standardabweichung.', True,
   'Beispiel der Folie: (109 − 106) / 15 = 0,2.', 'Effektstärke')
tf('p5b-tf-02', SB, 'Laut Metaanalyse unterscheiden sich Jungen und Mädchen schon im Schulalter deutlich in Mathematik.', False,
   'Im Schulalter <b>keine</b> Unterschiede, erst im Erwachsenenalter.', 'Mathe Schulalter')
tf('p5b-tf-03', SB, 'Unter Männern gibt es mehr Hoch- und mehr Minderleister in Mathematik.', True,
   'Laut Folie.', 'Hochleister Minderleister')
tf('p5b-tf-04', SB, 'Bei verbalen Fähigkeiten gibt es keine nennenswerten Geschlechtsunterschiede.', True,
   'Die d-Werte liegen überwiegend nahe null.', 'verbal')
tf('p5b-tf-05', SB, 'Bei Beziehungsaggression zeigen sich im Kindesalter deutliche Geschlechtsunterschiede.', False,
   'Crick & Grotpeter (1995): <b>keine</b> Unterschiede im Kindesalter.', 'Beziehungsaggression')
tf('p5b-tf-06', SB, 'Frauen schlagen in Beziehungen etwas öfter zu als Männer, aber weniger hart.', True,
   'Und sie tragen mehr Verletzungen davon (Archer, 2000).', 'Gewalt Beziehungen')
tf('p5b-tf-07', SB, 'Nach Härle (1983) ist pädagogisches Handeln unabhängig von der Person des Lehrers trainierbar.', False,
   'Härle sagt das Gegenteil: Es ist <b>nicht</b> unabhängig von der Person erlernbar.', 'Härle')
tf('p5b-tf-08', SB, 'Laut Mayr (2014) halten viele Psychologinnen und Psychologen die Lehrerpersönlichkeit für nützlich in Beratung und Bewerberauswahl.', True,
   'Und für interessant als Forschungsfeld.', 'Mayr Psychologen')
tf('p5b-tf-09', SB, 'Dass die Lehrerpersönlichkeit über gute Berufsausübung entscheidet, ist von der Erziehungswissenschaft empirisch klar belegt.', False,
   'Diese Position ist <b>empirisch keinesfalls belegt</b> und wird kontrovers diskutiert.', 'empirisch nicht belegt')
tf('p5b-tf-10', SB, 'Die Folien legen fest, welche der fünf Lehrer-Karikaturen der gute Lehrer ist.', False,
   'Die Folien geben keine Lösung – Diskussionsfrage.', 'Karikaturen Diskussion')
tf('p5b-tf-11', SB, 'Offenheit und Verträglichkeit hingen bei Mayr (2006) nicht mit Erfolgen und Schwierigkeiten im Lehramtsstudium zusammen.', True,
   'Zusammenhänge zeigten Extraversion, Neurotizismus und Gewissenhaftigkeit.', 'Mayr Offenheit Verträglichkeit')
tf('p5b-tf-12', SB, 'Neurotizismus geht bei Lehramtsstudierenden mit mehr Erfolgen einher.', False,
   'Neurotizismus geht mit <b>weniger</b> Erfolgen und mehr Schwierigkeiten einher.', 'Neurotizismus Erfolge')
tf('p5b-tf-13', SB, '„Ruhig – lebhaft“ ist ein Adjektivpaar der LPA-Dimension Kontaktbereitschaft.', True,
   'Weitere: sachbezogen – kontaktfreudig, kühl – warmherzig, gerne unabhängig – gerne mit anderen.', 'LPA Kontaktbereitschaft')
tf('p5b-tf-14', SB, 'Im Verlauf von Studium und Beruf steigt die Kontaktbereitschaft von Lehrkräften.', False,
   'Sie <b>sinkt</b>; die Selbstkontrolle steigt.', 'Kontaktbereitschaft sinkt')

# ---- 5b Lückentext
gap('p5b-gap-01', SB, 'Empirisch gefundene Unterschiede heißen Geschlechtsunterschiede, Überzeugungen über Unterschiede heißen {{Geschlechtsstereotype|Stereotype|Geschlechtsstereotypen}}.',
    'Beides ist Thema der Folien.', 'Geschlechtsstereotype')
gap('p5b-gap-02', SB, 'Die Mittelwertsdifferenz geteilt durch die Standardabweichung heißt {{Effektstärke|Effektgröße}} d.',
    'Nicht verwechseln mit der Korrelation r.', 'Effektstärke')
gap('p5b-gap-03', SB, 'Bei Erwachsenen ist der größte kognitive Geschlechtsunterschied bei der mentalen {{Rotation}} zu finden.',
    'Vorteil der Männer; räumliche Wahrnehmung zeigt einen kleineren Unterschied.', 'mentale Rotation')
gap('p5b-gap-04', SB, 'Mayrs LPA-Skalen umfassen Kontaktbereitschaft, Stabilität und {{Selbstkontrolle}}.',
    'Selbstkontrolle steigt im Verlauf von Studium und Beruf.', 'LPA Selbstkontrolle')
gap('p5b-gap-05', SB, 'Bei Lehramtsstudierenden hängt die {{Gewissenhaftigkeit}} am stärksten mit Erfolgen und Schwierigkeiten zusammen.',
    'Mayr (2006); daneben Extraversion und Neurotizismus.', 'Gewissenhaftigkeit')
gap('p5b-gap-06', SB, 'Introversion, neurotische Tendenzen und wenig {{Selbstkontrolle}} wirken sich generell negativ auf Unterrichtsgestaltung aus.',
    'Mayr (2002).', 'Selbstkontrolle negativ')
