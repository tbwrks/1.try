# Google Search Console – wiederkehrender Auswertungsprozess

Dieser Ordner ist die feste Struktur für die laufende GSC-Auswertung – für tbwrks selbst
und für die Kundenseiten (aktuell in Aufbau: bis zu drei Kunden, z. B. Ferber Monheim).
Ziel: immer nach demselben Muster auswerten, damit (a) die eigene/Kunden-Seite gezielt
verbessert werden kann ("pushen") und (b) die Ergebnisse in 2 Minuten so erklärt werden
können, dass sie auch ein Kunde ohne SEO-Vorwissen versteht ("Handwerker-Version").

## Wie oft: wöchentlich oder monatlich?

**Beides, aber mit unterschiedlicher Aufgabe – nicht dieselbe Analyse doppelt:**

- **Wöchentlicher Kurz-Check (5 Min):** nur der Zeitverlauf (`Diagramm.csv`) und die
  Top-Suchanfragen überfliegen. Zweck: Ausreißer und Reputationsrisiken sofort erkennen
  (z. B. plötzlich eine negative Suchanfrage wie „…insolvenz“, ein Einbruch bei Klicks/CTR,
  ein technischer Fehler). Keine tiefe Keyword-Arbeit – dafür ist eine Woche bei einem
  kleinen lokalen Betrieb (100–200 Klicks/Woche) statistisch zu wackelig.
- **Monatliche Tiefenanalyse (die eigentliche Auswertung, siehe Vorlage unten):**
  vollen Kalendermonat exportieren, mit dem Vormonat und – bei saisonalen Betrieben
  (Biergarten, Hotel) – mit demselben Monat im Vorjahr vergleichen. Auf dieser Basis werden
  Maßnahmen entschieden, weil erst ab ~30 Tagen genug Klicks pro Keyword/Seite
  zusammenkommen, um echte Muster von Zufall zu unterscheiden.

Faustregel: **Wochendaten = Frühwarnsystem, Monatsdaten = Entscheidungsgrundlage.**

## Fixer Export (jedes Mal identisch)

In der Google Search Console: **Leistung → Suchergebnisse**
- Suchtyp: **Web**
- Zeitraum: **voller Kalendermonat** (bei Wochen-Check: letzte 7 Tage) – Zeitraum im
  Export-Dialog *aktiv prüfen*, nicht dem Default-Label vertrauen (siehe Hinweis oben)
- Export → CSV (Excel), das liefert immer diese 7 Dateien:
  `Diagramm.csv`, `Suchanfragen.csv`, `Seiten.csv`, `Länder.csv`, `Geräte.csv`,
  `Darstellung in der Suche.csv`, `Filter.csv`

Ablage: `gsc-analysen/<kunde>/<zeitraum>/rohdaten/` – die Rohdaten bleiben liegen,
damit sich Perioden später exakt vergleichen lassen (Trend über mehrere Monate).

## Ablauf der Analyse (immer dieselben 6 Schritte)

1. **Gesamt-KPIs & Trend:** Klicks, Impressionen, CTR, Position aus `Diagramm.csv` –
   Richtung seit letzter Periode?
2. **Seiten-Check:** `Seiten.csv` – welche Seite bringt Klicks, welche hat viele
   Impressionen aber kaum Klicks (= Titel/Meta-Beschreibung überzeugt nicht, obwohl
   Google die Seite zeigt)?
3. **Keyword-Chancen ("Striking Distance"):** in `Suchanfragen.csv` nach Begriffen mit
   Position 4–15 UND nennenswerten Impressionen suchen – das sind die Wörter, bei denen
   sich Optimierung am schnellsten auszahlt (kleiner Schubs auf Seite-1-Top).
4. **Marke vs. generisch trennen:** Marken-Suchen (Name des Betriebs) zeigen nur, dass
   Bekannte wiederkommen. Generische Suchen (z. B. „biergarten monheim“) zeigen, ob
   *neue* Kunden gefunden werden – die sind für „pushen“ relevanter.
5. **Geräte-Check:** `Geräte.csv` – bei Mobil-Dominanz (Standard bei lokalen Betrieben)
   Ladezeit/Buchungs-Button auf dem Handy testen.
6. **Auffälligkeiten:** ungewöhnliche/negative Suchbegriffe, neue Konkurrenz-Begriffe,
   Länder-Ausreißer mit echtem Volumen (nicht 1–2 Klicks Zufallsstreuung).

Danach werden die Ergebnisse in zwei Dokumenten festgehalten:

- **`analyse.md`** (Vorlage: `VORLAGE-analyse.md`) – die technische Auswertung mit
  Zahlen und priorisierten Maßnahmen. Für die eigene Arbeit/Umsetzung.
- **`kunde-zusammenfassung.md`** (Vorlage: `VORLAGE-kundenzusammenfassung.md`) – dieselben
  Erkenntnisse in einfacher Sprache mit Alltags-Vergleichen, ohne Fachbegriffe. Zum
  Vorlesen/Schicken an den Kunden – das ist gleichzeitig das Verkaufsargument
  ("guck, dafür bezahlst du mich").

## Ordnerstruktur

```
gsc-analysen/
  README.md                          ← dieser Prozess
  VORLAGE-analyse.md                 ← Kopiervorlage: technische Auswertung
  VORLAGE-kundenzusammenfassung.md   ← Kopiervorlage: Kundenversion
  ferber-monheim/
    2026-09-02_bis_2026-09-08/
      rohdaten/*.csv
      analyse.md
      kunde-zusammenfassung.md
  tbwrks/                            ← eigene Seite, sobald Export vorliegt
  <naechster-kunde>/                 ← analog anlegen
```

Für die nächste Runde: Ordner `<kunde>/<zeitraum>/rohdaten/` anlegen, CSVs reinlegen,
die beiden Vorlagen hineinkopieren und mit den neuen Zahlen sowie einem Vergleich zur
Vorperiode befüllen.
