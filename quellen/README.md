# Bauquellen

Aus diesen Dateien entstehen `index.html`, `app.css`, `app.js`, `content.js`, die Weiterleitungsseiten, `sw.js`, Manifest und Icons.

Aufruf im Ordner `quellen`: `python3 build.py` (braucht pandoc, bs4 und PIL). Ausgabe nach `/home/claude/out2` (oder `LERNKISTE_OUT`), von dort ins Repo-Wurzelverzeichnis kopieren.

- `app.js`, `app.css`: die App (Router, Datenspeicher, Karten, Tests, Suche, Verlauf, Einstellungen)
- `quelle.html`: Diff1-Karteikarten (TeX), feste Karten-IDs stehen in `build.py` (`CARD_IDS`)
- `data_*.py`: Testfragen, `tex.py`: TeX nach MathML
- Nach Änderungen die Cache-Version in `sw.js` (in `build.py`, `lernkiste-v4`) erhöhen, sonst holen sich Geräte nichts Neues.
