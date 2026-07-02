# Der Angebots-Prozess: vom Kundengespräch zum fertigen PDF

So kommst du für jeden neuen Kunden wieder zu genau diesem Ergebnis. Alles Nötige liegt in diesem Ordner — Preise, Texte, Design, Schriften. Das Repo ist das Gedächtnis; jede Claude-Session kann daraus reproduzieren.

## Dein Teil (unter 10 Minuten)

1. **Kundengespräch führen** wie immer.
2. **Briefing-Block ausfüllen** (aus `03-briefing-vorlage.md`: Kunde, Segment, Anlass, Wunsch, Empfehlung, Stufen — ~8 Felder, Klartext reicht) und an Claude schicken. In einer neuen Session genügt als Kontext ein Satz: *„Lies `angebotsprozess/` im Repo tbwrks/1.try und erstelle daraus ein Angebot: [Briefing]"*
3. **Kurzübersicht freigeben** — Claude antwortet zuerst mit ~5 Zeilen (Stufen, Module, Preise). Du sagst „passt" oder korrigierst („Website eine Nummer größer", „Retainer nur S").
4. **PDF prüfen und verschicken.**

## Claudes Teil (automatisch, immer gleich)

1. **Briefing → Module:** Wunsch/Empfehlung in Bausteine + Größen aus `02-baukasten.md` übersetzen, Segment-Faktor anwenden, auf 50 € runden, Realisation 12 % einrechnen.
2. **Kurzübersicht** zur Freigabe zeigen (nichts wird ausformuliert, bevor du nicht bestätigt hast).
3. **Angebotstext** nach `04-angebotsvorlage.md` schreiben und als Markdown ablegen: `angebotsprozess/angebote/A-000XX-nachname.md`.
4. **PDF rendern:** Design-Vorlage `design/angebot_glaser.html` (Referenz-Layout mit Original-Avenir, Logo, Lavendel-Titeln, Zebra-Tabellen) mit den neuen Inhalten befüllen und per Headless-Chromium nach `angebotsprozess/pdf/Angebot_A000XX_Nachname.pdf` rendern.
5. **Querrechnen und prüfen** (Pflicht, vor jedem Versand):
   - Brutto = Netto × 1,19, aus dem Netto gerechnet, nie kopiert
   - Zwischensummen = Summe der Positionen
   - Datum real, Gültigkeit = Angebotsdatum + 14 Tage
   - ein einziger Prozentsatz für Abschlag im ganzen Dokument
   - laufende Leistungen nur als €/Monat, nie im Einmalpreis
   - Angebotsnummer fortlaufend (letzte prüfen: Dateinamen in `angebotsprozess/pdf/` bzw. `angebote/`)
6. **Committen und pushen** — jedes Angebot bleibt als Markdown + PDF im Repo nachvollziehbar.

## Nummernkreis

Fortlaufend `A-000XX`. Zuletzt vergeben: **A-00097** (Glaser). Claude prüft vor jeder Vergabe die vorhandenen Dateien und zählt hoch.

## Was wo liegt

| Datei/Ordner | Zweck |
|---|---|
| `01-analyse-angebote.md` | Ausgangsanalyse der alten Angebote (Referenz) |
| `02-baukasten.md` | Preise, Module, Standardkonditionen — die einzige Preisquelle |
| `03-briefing-vorlage.md` | Das Formular, das du ausfüllst |
| `04-angebotsvorlage.md` | Struktur + Checkliste für den Angebotstext |
| `design/` | HTML-Vorlage, Original-Avenir (repariert), Mulish-Fallback, Logo |
| `angebote/` | Ausformulierte Angebote als Markdown (Archiv) |
| `pdf/` | Fertige, versandfähige PDFs |

## Preise ändern

Nur `02-baukasten.md` anpassen (Rate Card, Modulgrößen, Segment-Faktoren) — alle künftigen Angebote rechnen automatisch mit den neuen Werten. Nie Preise direkt im Angebot „freihändig" ändern, sonst driftet das System wieder auseinander.
