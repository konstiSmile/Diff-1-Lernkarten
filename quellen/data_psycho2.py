# Psycho2 – Gerüst mit Beispielfragen (Platzhalter, noch kein Skript)
ITEMS = []

def add(**k):
    k['placeholder'] = True
    ITEMS.append(k)

add(id='p-mc-01', type='mc', q='Beispielfrage: Wer beschrieb die <b>klassische Konditionierung</b> zuerst?',
    options=['Iwan Pawlow', 'B. F. Skinner', 'Albert Bandura', 'Jean Piaget'], correct=0,
    expl='Platzhalter. Pawlow koppelte einen neutralen Reiz mit einem unbedingten Reiz.', src='Beispiel', kw='')
add(id='p-mc-02', type='mc', q='Beispielfrage: Was ist ein <b>Verstärker</b> in der operanten Konditionierung?',
    options=['Eine Konsequenz, die die Auftretenswahrscheinlichkeit eines Verhaltens erhöht', 'Ein Reiz, der Verhalten immer verhindert', 'Ein angeborener Reflex', 'Ein Gedächtnisinhalt'], correct=0,
    expl='Platzhalter.', src='Beispiel', kw='')
add(id='p-mc-03', type='mc', q='Beispielfrage: Wofür steht „n“ in einer Stichprobe?',
    options=['Stichprobengröße', 'Standardabweichung', 'Mittelwert', 'Signifikanzniveau'], correct=0,
    expl='Platzhalter.', src='Beispiel', kw='')
add(id='p-tf-01', type='tf', statement='Beispielaussage: Das Arbeitsgedächtnis hat eine unbegrenzte Kapazität.', answer=False,
    expl='Platzhalter. Die Kapazität gilt als stark begrenzt.', src='Beispiel', kw='')
add(id='p-tf-02', type='tf', statement='Beispielaussage: Ein größerer Stichprobenumfang verringert in der Regel den Standardfehler des Mittelwerts.', answer=True,
    expl='Platzhalter.', src='Beispiel', kw='')
add(id='p-tf-03', type='tf', statement='Beispielaussage: Korrelation beweist Kausalität.', answer=False,
    expl='Platzhalter. Zusammenhang heißt nicht Ursache.', src='Beispiel', kw='')
add(id='p-gap-01', type='gap', text='Beispiel: Bei der klassischen Konditionierung wird ein neutraler Reiz mit einem {{unbedingten|unkonditionierten}} Reiz gekoppelt.',
    expl='Platzhalter.', src='Beispiel', kw='')
add(id='p-gap-02', type='gap', text='Beispiel: Der Mittelwert einer Verteilung wird auch {{arithmetisches Mittel|Durchschnitt|Mittelwert}} genannt.',
    expl='Platzhalter.', src='Beispiel', kw='')
add(id='p-gap-03', type='gap', text='Beispiel: Ein Verhalten, das nicht mehr verstärkt wird, verschwindet allmählich. Dieser Vorgang heißt {{Extinktion|Löschung}}.',
    expl='Platzhalter.', src='Beispiel', kw='')

DATA = dict(
    subject='Psycho2', key='psy2', title='Psycho2', sub='Test-Gerüst: Multiple Choice, Lückentext, Richtig/Falsch, Zeit-Simulation',
    accent='#c58fb8', placeholder=True, items=ITEMS,
)
