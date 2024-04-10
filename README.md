# Bitte lies mich!

## Installationsanleitung

- lade dir den Ordner herunter unter öffne den Ordner in VS Code
- Öffne ein Terminal
- Erstelle eine neue Python-Umgebung
    - `python -m venv .venv`
- Aktiviere die Umgebung
    - Windows: `.venv\Scripts\Activate`
    - Linux: `source .venv/bin/activate`
- Installiere die Pakete
    - Entweder mit `pip install <paketname>`
    - Oder mit `pip install -r requirement.txt`
    
## LeistungsanalyseApp
### Beschreibung:
Mt dem Programm kann ein Experiment angelegt werden (Name,Thema, datum, Versuchsleiter) und naschließend in dieses mehrere Teilnehmer des Experiments eingefügt werden (Name, Alter). Auf grundlage dieser Daten ermittelt das Programm eine Abschätzung der maximalen Herzfrequenz der Teilnehmer.
Die Daten werden in einem Dictionary als File gespeichert

### Benutzung:
- Starte das Programm mit `python main.py`
- Das programm frägt nun Schritt für Schritt die Daten ab
- Am Ende wird das Experiment als Dictionary ausgegeben

