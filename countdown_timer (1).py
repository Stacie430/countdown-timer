"""Countdown-Timer mit Tkinter-Oberfläche.

Zwei Modi:
  1. Dauer:      Stunden / Minuten / Sekunden eingeben
  2. Zieldatum:  Datum (TT.MM.JJJJ) und Uhrzeit (HH:MM) eingeben
"""

import math
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta


class CountdownApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Countdown-Timer")
        self.resizable(False, False)

        self.end_time: datetime | None = None     # Zielzeitpunkt (läuft)
        self.remaining: timedelta | None = None   # Restzeit (pausiert)
        self.total_seconds = 0
        self.job: str | None = None
        self.running = False

        self._build_ui()

    # ------------------------------------------------------------------ UI
    def _build_ui(self) -> None:
        main = ttk.Frame(self, padding=15)
        main.grid()

        # Anzeige
        self.display = ttk.Label(main, text="00:00:00", font=("Helvetica", 40, "bold"))
        self.display.grid(row=0, column=0, pady=(0, 5))

        self.progress = ttk.Progressbar(main, length=320, maximum=100)
        self.progress.grid(row=1, column=0, pady=(0, 10))

        # Tabs für die beiden Eingabemodi
        self.tabs = ttk.Notebook(main)
        self.tabs.grid(row=2, column=0, pady=(0, 10), sticky="ew")

        # --- Tab 1: Dauer
        tab_duration = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(tab_duration, text="Dauer")

        self.hours = tk.StringVar(value="0")
        self.minutes = tk.StringVar(value="5")
        self.seconds = tk.StringVar(value="0")

        for col, (label, var, upper) in enumerate(
            [("Stunden", self.hours, 99),
             ("Minuten", self.minutes, 59),
             ("Sekunden", self.seconds, 59)]
        ):
            ttk.Label(tab_duration, text=label).grid(row=0, column=col, padx=5)
            ttk.Spinbox(
                tab_duration, from_=0, to=upper, width=5,
                textvariable=var, wrap=True, justify="center",
            ).grid(row=1, column=col, padx=5)

        # --- Tab 2: Zieldatum
        tab_date = ttk.Frame(self.tabs, padding=10)
        self.tabs.add(tab_date, text="Zieldatum")

        tomorrow = datetime.now() + timedelta(days=1)
        self.date_var = tk.StringVar(value=tomorrow.strftime("%d.%m.%Y"))
        self.time_var = tk.StringVar(value="08:00")

        ttk.Label(tab_date, text="Datum (TT.MM.JJJJ)").grid(row=0, column=0, padx=5)
        ttk.Label(tab_date, text="Uhrzeit (HH:MM)").grid(row=0, column=1, padx=5)
        ttk.Entry(tab_date, textvariable=self.date_var, width=14,
                  justify="center").grid(row=1, column=0, padx=5)
        ttk.Entry(tab_date, textvariable=self.time_var, width=10,
                  justify="center").grid(row=1, column=1, padx=5)

        # Buttons
        buttons = ttk.Frame(main)
        buttons.grid(row=3, column=0)

        self.start_btn = ttk.Button(buttons, text="Start", command=self.start_or_resume)
        self.start_btn.grid(row=0, column=0, padx=4)
        self.pause_btn = ttk.Button(buttons, text="Pause", command=self.pause,
                                    state="disabled")
        self.pause_btn.grid(row=0, column=1, padx=4)
        ttk.Button(buttons, text="Zurücksetzen", command=self.reset).grid(
            row=0, column=2, padx=4)

    # ------------------------------------------------------------ Eingaben
    def _read_duration(self) -> timedelta:
        try:
            h = int(self.hours.get())
            m = int(self.minutes.get())
            s = int(self.seconds.get())
        except ValueError:
            raise ValueError("Bitte ganze Zahlen für Stunden, Minuten und Sekunden eingeben.")
        if min(h, m, s) < 0:
            raise ValueError("Negative Werte sind nicht erlaubt.")
        return timedelta(hours=h, minutes=m, seconds=s)

    def _read_target(self) -> timedelta:
        text = f"{self.date_var.get().strip()} {self.time_var.get().strip()}"
        try:
            target = datetime.strptime(text, "%d.%m.%Y %H:%M")
        except ValueError:
            raise ValueError("Bitte Datum als TT.MM.JJJJ und Uhrzeit als HH:MM eingeben.")
        return target - datetime.now()

    # ------------------------------------------------------------ Steuerung
    def start_or_resume(self) -> None:
        if self.running:
            return

        if self.remaining is None:  # neuer Start
            try:
                if self.tabs.index(self.tabs.select()) == 0:
                    delta = self._read_duration()
                else:
                    delta = self._read_target()
            except ValueError as err:
                messagebox.showerror("Ungültige Eingabe", str(err))
                return
            if delta.total_seconds() <= 0:
                messagebox.showerror("Ungültige Eingabe",
                                     "Die Zeit muss in der Zukunft liegen.")
                return
            self.total_seconds = math.ceil(delta.total_seconds())
        else:  # Fortsetzen nach Pause
            delta = self.remaining

        self.end_time = datetime.now() + delta
        self.remaining = None
        self.running = True
        self.start_btn.config(state="disabled", text="Start")
        self.pause_btn.config(state="normal")
        self.tabs.state(["disabled"])
        self._tick()

    def pause(self) -> None:
        if not self.running:
            return
        self._cancel_job()
        self.remaining = self.end_time - datetime.now()
        self.running = False
        self.start_btn.config(state="normal", text="Fortsetzen")
        self.pause_btn.config(state="disabled")

    def reset(self) -> None:
        self._cancel_job()
        self.running = False
        self.end_time = None
        self.remaining = None
        self.total_seconds = 0
        self.display.config(text="00:00:00", foreground="")
        self.progress["value"] = 0
        self.start_btn.config(state="normal", text="Start")
        self.pause_btn.config(state="disabled")
        self.tabs.state(["!disabled"])

    def _cancel_job(self) -> None:
        if self.job is not None:
            self.after_cancel(self.job)
            self.job = None

    # ------------------------------------------------------------ Anzeige
    @staticmethod
    def _format(seconds: int) -> str:
        days, rest = divmod(seconds, 86400)
        hours, rest = divmod(rest, 3600)
        mins, secs = divmod(rest, 60)
        base = f"{hours:02d}:{mins:02d}:{secs:02d}"
        return f"{days}T {base}" if days else base

    def _tick(self) -> None:
        left = self.end_time - datetime.now()
        secs_left = math.ceil(left.total_seconds())

        if secs_left <= 0:
            self._finish()
            return

        self.display.config(text=self._format(secs_left))
        done = 1 - secs_left / self.total_seconds
        self.progress["value"] = max(0, min(100, done * 100))
        self.job = self.after(200, self._tick)  # häufig prüfen, bleibt genau

    def _finish(self) -> None:
        self.job = None
        self.running = False
        self.end_time = None
        self.display.config(text="00:00:00", foreground="red")
        self.progress["value"] = 100
        self.start_btn.config(state="disabled")
        self.pause_btn.config(state="disabled")
        self.tabs.state(["!disabled"])
        self.bell()
        messagebox.showinfo("Countdown-Timer", "Zeit abgelaufen!")


if __name__ == "__main__":
    CountdownApp().mainloop()
