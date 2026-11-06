# Bauquellen
Aus diesen Dateien werden `index.html`, `diff1.html`, `querschnitt.html`, `psycho2.html` und `sw.js` erzeugt.
Aufruf (im Ordner `quellen`): `python3 build.py` (braucht pandoc und bs4). Ausgabe nach `/home/claude/out`, von dort ins Repo-Wurzelverzeichnis kopieren.
- `quelle.html`: Diff1-Karteikarten (TeX), `data_*.py`: Testfragen, `*_template.html`: Seitengerüste, `tex.py`: TeX → MathML.
- Nach Änderungen die Versionsnummer in `sw.js` (in `build.py`) erhöhen.
