# Countdown-Timer

Ein einfacher Countdown-Timer mit grafischer Oberfläche, geschrieben in Python mit Tkinter.

## Funktionen

- **Dauer-Modus:** Stunden, Minuten und Sekunden eingeben
- **Zieldatum-Modus:** Datum (`TT.MM.JJJJ`) und Uhrzeit (`HH:MM`) festlegen
- Start, Pause, Fortsetzen und Zurücksetzen
- Fortschrittsbalken und Tagesanzeige bei langen Zeiträumen
- Signalton und Meldung, wenn die Zeit abgelaufen ist
- Genaue Zeitmessung, da die Restzeit aus der Systemuhr berechnet wird

 Voraussetzungen

- Python 3.10 oder neuer
- Tkinter (in den meisten Python-Installationen enthalten)

Unter Linux muss Tkinter eventuell nachinstalliert werden:

```bash
sudo apt install python3-tk
``` Starten

```bash
python countdown_timer.py
```

 Verwendung

1. Wähle den Tab **Dauer** oder **Zieldatum**.
2. Gib die gewünschte Zeit ein.
3. Klicke auf **Start**.
4. Mit **Pause** hältst du den Timer an, mit **Fortsetzen** läuft er weiter.
5. **Zurücksetzen** stellt den Timer auf den Anfang zurück.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Eine `LICENSE`-Datei kannst du beim Anlegen des Repositorys auf GitHub direkt auswählen.
