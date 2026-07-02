# Angebots-Briefing — das füllst du aus (mehr nicht)

Kopiere den Block nach dem Kundengespräch, fülle die Werte, schick ihn an Claude. Alles, was du weglässt, wird mit dem Standard aus dem Baukasten (`02-baukasten.md`) gefüllt. Du kannst überall **Klartext ODER Modul-Kürzel** schreiben — Claude übersetzt Klartext selbst in Module und schlägt sie zur Bestätigung vor.

```
KUNDE:      [Name, Firma, Straße, PLZ Ort]
ANSPRACHE:  [Du / Sie] + [Anrede, z. B. „Lieber Christoph"]
SEGMENT:    [GRÜNDER / BESTAND / PREMIUM]
ANLASS:     [1–2 Sätze: worum geht's, was ist das Ziel des Kunden]

WUNSCH:     [Was der Kunde konkret angefragt hat — Klartext oder Module]
EMPFEHLUNG: [Was du glaubst, was es wirklich braucht — Klartext, Module
             oder „Vorschlag von Claude": dann leite ich es aus ANLASS ab]
STUFEN:     [2 / 3]   ← 2 = Wunsch + Empfehlung; 3 = zusätzlich Ausbaustufe mit Betreuung

BUDGET:     [optional: Budgetsignal aus dem Gespräch, z. B. „hat 5k genannt"]
START:      [KW oder Datum]
ZAHLUNG:    [Standard / 50-50 / individuell: …]
NUTZUNG:    [Standard / Buyout inkl. (+ Aufpreis einrechnen)]
BESONDERES: [Freitext: Rabatt-Deal, Ausschlüsse, Versprechen aus dem Gespräch]
```

## Die Stufen-Logik (Skalierung in jedem Angebot)

Jedes Angebot geht mit 2 oder 3 Stufen raus. Die Stufen sind keine drei getrennten Angebote, sondern eine Treppe im selben Dokument:

| Stufe | Name im Angebot | Inhalt | Preis-Logik |
|---|---|---|---|
| 1 | **Basis** | Der Kundenwunsch — sauber abgegrenzt, ehrlich, funktioniert für sich | kleinster Umfang, nie unter Mindestprojektwert (2.500 €) |
| 2 | **Empfehlung** | Dein Setup — das, was es aus deiner Sicht wirklich braucht | Zielpaket, ca. Faktor 1,3–1,6 zur Basis. Das Anschreiben argumentiert für diese Stufe |
| 3 | **Ausbau** | Empfehlung + laufende Betreuung (M5-Retainer und/oder M8) | Einmalpreis der Empfehlung + €/Monat. Wirkt als Anker und macht Stufe 2 „vernünftig" |

Regeln:
- Der **Unterschied zwischen den Stufen muss in einer Zeile benennbar sein** (konkrete Deliverables: „+ Bildproduktion erweitert, + 24 Posts/Jahr als Retainer"), sonst wirkt die höhere Stufe wie Aufschlag ohne Gegenwert.
- Laufende Leistungen (Posts, Hosting, Betreuung) tauchen **nur in Stufe 3 und nur als €/Monat** auf — nie im Einmalpreis versteckt.
- Bei STUFEN=2 entfällt der Ausbau; die Empfehlung steht dann als zweite Option über der Basis.
- Wenn WUNSCH und EMPFEHLUNG identisch sind: Basis = abgespeckte Variante (kleinere Modul-Größen), Empfehlung = das Besprochene.

## Beispiel (hätte das Fetsch-Angebot erzeugt — jetzt mit Stufen)

```
KUNDE:      Dominik Fetsch, Donaustraße 64, 86633 Neuburg
ANSPRACHE:  Du + „Lieber Dominik"
SEGMENT:    GRÜNDER
ANLASS:     Unternehmensgründung; braucht professionellen Auftritt und danach
            kontinuierlich Reichweite/Anfragen ohne eigenen Aufwand.

WUNSCH:     Logo + Website („was Gescheites zum Starten")
EMPFEHLUNG: Vorschlag von Claude
STUFEN:     3

BUDGET:     —
START:      Februar
ZAHLUNG:    Standard
NUTZUNG:    Standard
BESONDERES: —
```

Daraus macht Claude z. B.:
- **Stufe 1 | Basis:** M2-M (Branding) + M4-S (Onepager) ≈ 4.950 € netto
- **Stufe 2 | Empfehlung:** M1-S (Strategie) + M2-M + M3-S (Bilder) + M4-M (Website 5 Seiten) ≈ 6.950 € netto
- **Stufe 3 | Ausbau:** Stufe 2 + M5-S (Kommunikation, 350 €/Monat, 12 Monate) + Hosting 35 €/Monat

## Was Claude daraus macht (Ablauf)

1. WUNSCH und EMPFEHLUNG in Module + Größen übersetzen (bei „Vorschlag von Claude" aus ANLASS abgeleitet) und **erst als Kurzübersicht zur Freigabe zeigen**: Stufen, Module, Preise — 5 Zeilen.
2. Nach deinem „passt" (oder deinen Korrekturen): komplettes Angebot nach `04-angebotsvorlage.md` ausformulieren — Anschreiben personalisiert aus ANLASS, argumentiert für die Empfehlung.
3. Alle Summen querrechnen (Brutto = Netto × 1,19), Daten prüfen, Standardkonditionen anhängen.
4. Du liest Korrektur, setzt es in dein Layout, fertig. Zieldauer für dich: **unter 10 Minuten pro Angebot.**
