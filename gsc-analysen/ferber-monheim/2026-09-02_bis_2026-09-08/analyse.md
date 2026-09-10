# GSC-Auswertung: Ferber Monheim – 02.09.–08.09.2026 (7 Tage)

*Quelle: Google Search Console Export, Suchtyp Web. Kein Vorperiode-Vergleich möglich,
da dies der erste Export ist – dient als Basislinie für künftige Vergleiche.*

**Hinweis zur Datenqualität:** Der Export-Filter (`Filter.csv`) nennt fälschlich
„Letzte 12 Monate“, tatsächlich zeigen Diagramm/Seiten/Geräte übereinstimmend nur 7 Tage
(151 Klicks, 1.843 Impressionen). Beim nächsten Export im GSC-Dialog aktiv den Zeitraum
prüfen. Zusätzlich: `Suchanfragen.csv` summiert nur 87 der 151 Klicks – die Differenz
(64 Klicks) verteilt sich auf sehr seltene Suchbegriffe, die Google aus Datenschutz-
gründen nicht einzeln ausweist. Das ist normal, kein Datenfehler.

## 1. Gesamt-KPIs (7 Tage)

| Kennzahl | Wert |
|---|---|
| Klicks | 151 |
| Impressionen | 1.843 |
| CTR | 8,19 % |
| Ø Position | ~6,9 (Deutschland: 6,92; dominiert das Gesamtbild, da 144 von 151 Klicks aus DE) |

CTR und Position sind für eine lokale Gastro-/Hotel-Seite solide. Der Zeitverlauf
schwankt zwischen 5–12,5 % CTR und Position 5,5–9,6 – bei diesem Klickvolumen (~20/Tag)
normal starkes Rauschen, kein Alarmsignal. Erst ab ~1 Monat Daten lässt sich ein echter
Trend von Zufall unterscheiden.

## 2. Seiten-Performance

| Seite | Klicks | Impr. | CTR | Position | Einschätzung |
|---|---|---|---|---|---|
| / (Startseite) | 116 | 1.614 | 7,19 % | 6,41 | Trägt 77 % aller Klicks – funktioniert, aber auch fast alle Impressionen laufen hier auf. Content-Seiten sind noch zu schwach angebunden. |
| /restaurant | 19 | 267 | 7,12 % | 11,32 | Nur knapp außerhalb Seite 1 (Top 10) – mit gezielter Optimierung realistisch auf Seite-1-Top zu bringen. |
| /hotel | 11 | 219 | 5,02 % | 5,05 | Gute Position, aber schwache CTR – Titel/Snippet überzeugt nicht im Verhältnis zur Platzierung. |
| /metzgerei | 7 | 173 | 4,05 % | 4,2 | Gleiches Muster: gute Position, schwache CTR. |
| /der-metzger | 5 | 147 | 3,4 % | 2,54 | **Auffälligster Fall:** Position 2,5 (Top der ersten Seite!) aber nur 3,4 % CTR – der Titel/Meta-Text verschenkt hier sichtbar Klicks. |
| /stadtstadl | 4 | 86 | 4,65 % | 4,76 | Ähnlich: gute Position, mittelmäßige CTR. |
| /ueber-uns | 3 | 61 | 4,92 % | 6,05 | Unauffällig, geringes Volumen. |
| **/zimmer** | **0** | **62** | **0 %** | **5,24** | **Kritisch:** 62 Impressionen bei Position 5 (Seite 1!), aber null Klicks in 7 Tagen. Hotelzimmer-Interessenten sehen die Seite, klicken aber nicht. |
| /impressum | 0 | 13 | 0 % | 5,38 | Erwartungsgemäß, keine Maßnahme nötig. |

## 3. Keyword-Chancen (Striking Distance & Impressionsstark, aber klickschwach)

| Suchanfrage | Klicks | Impr. | CTR | Position | Maßnahme |
|---|---|---|---|---|---|
| biergarten monheim | 1 | 62 | 1,6 % | 7,15 | Größte Einzelchance im ganzen Export: hohe Nachfrage, Seite 1 knapp verfehlt/erreicht, kaum Klicks. Vermutlich keine eigene Biergarten-Seite vorhanden (nicht in `Seiten.csv` gelistet) → Inhalt wird generisch mitbedient statt gezielt. |
| biergarten monheim schwaben | 1 | 51 | 2,0 % | 6,33 | Gleiches Thema, zweite Variante desselben Suchbedürfnisses. |
| biergarten monheim bayern | 0 | 15 | 0 % | 3,33 | Sehr gute Position, aber 0 Klicks – Snippet/Titel überzeugt nicht. |
| monheim biergarten | 0 | 18 | 0 % | 10,83 | Knapp Seite 2 – mit Optimierung Richtung Seite-1-Top. |
| metzgerei monheim | 1 | 28 | 3,6 % | 3,0 | Top-3-Position, aber CTR verschenkt – Snippet/Angebot im Titel schärfen. |
| restaurant monheim | 2 | 25 | 8,0 % | 13,08 | Generischster, wichtigster Suchbegriff fürs Restaurant – Seite 2, klar ausbaufähig. |
| donauwörth hotel | 0 | 26 | 0 % | 7,19 | Regionale Hotel-Nachfrage (Nachbarstadt) wird komplett verschenkt. |
| pension donauwörth | 0 | 21 | 0 % | 4,52 | Gute Position, 0 Klicks – passt zum /zimmer-Befund oben. |
| monheim hotel | 0 | 19 | 0 % | 8,68 | Ebenfalls Hotel-Nachfrage ohne Konversion. |
| restaurant in der nähe | 0 | 14 | 0 % | 1,57 | Rang 1–2, aber 0 Klicks – Näheanfragen laufen oft über das Google-Maps-Kartenpaket statt den Weblink; Google Unternehmensprofil separat prüfen. |

**Muster:** Die komplette Hotel-/Zimmer-Nachfrage (donauwörth/monheim hotel, pension
donauwörth, /zimmer-Seite) rankt ordentlich bis gut, konvertiert aber praktisch nicht zu
Klicks. Dasselbe Muster bei Biergarten-Suchen. Das ist kein Sichtbarkeits-, sondern ein
**Attraktivitäts-Problem der Snippets** (Title-Tag/Meta-Beschreibung) bzw. fehlender
dedizierter Content (Biergarten).

## 4. Marke vs. generisch

- Eindeutig markenbezogene Klicks (Suchen mit „Ferber“ im Begriff): **64 von 151 Klicks
  (≈ 42 %)** – wahrscheinlich mehr, da weitere 64 Klicks auf nicht einzeln ausgewiesene
  Suchbegriffe entfallen.
- Stärkste generische Neukunden-Signale: „biergarten monheim“ (+Varianten), „restaurant
  monheim“, „metzgerei monheim“, Hotel-Suchen rund um Donauwörth.
- Top-Marken-Suchbegriff „ferber monheim“: 37 Klicks bei 53 Impressionen, CTR 69,8 %,
  Position 1,02 – die Marke selbst funktioniert einwandfrei.

## 5. Geräte

| Gerät | Klicks | Impr. | CTR | Position |
|---|---|---|---|---|
| Mobil | 115 | 1.455 | 7,9 % | 6,55 |
| Computer | 35 | 362 | 9,67 % | 9,7 |
| Tablet | 1 | 26 | 3,85 % | 4,04 |

76 % der Klicks kommen vom Handy (typisch für Gastro/Hotel „spontan unterwegs“-Suchen).
Mobile CTR liegt leicht unter Desktop – auf dem Handy prüfen: Ladezeit, ist die
Öffnungszeiten-/Telefon-/Buchungsinfo ohne Scrollen sichtbar?

## 6. Auffälligkeiten / Risiken

- **„ferber monheim insolvenzverfahren“** – 3 Klicks, 17 Impressionen, Position 2,24.
  Das ist eine Reputationsfrage, keine SEO-Frage: bitte mit dem Kunden direkt klären, ob
  das eine aktuelle/reale Angelegenheit ist (dann PR-/Kommunikationsthema) oder ein
  veralteter Suchbegriff, der noch nachwirkt (dann prüfen, ob eine sachliche
  Richtigstellungsseite sinnvoll ist). Nicht ignorieren – 17 Impressionen/Woche sind
  keine Einzelanfrage.
- **„krone monheim“ / „hotel krone monheim“** – 3+1 Klicks. Unklar, ob „Krone“ ein
  früherer Name des Hauses, ein Gebäudename oder ein anderer Betrieb ist – beim Kunden
  nachfragen, ggf. gezielt bedienen (Weiterleitung/Erwähnung) oder als Fremdbegriff
  einordnen.
- Keine „Darstellung in der Suche“-Erweiterungen aktiv (Datei ist leer) – keine Rich-
  Snippets/Sternebewertungen sichtbar. Strukturierte Daten (schema.org Restaurant/
  Hotel/LocalBusiness, Öffnungszeiten, Bewertungen) könnten CTR branchenweit spürbar
  heben.
- Internationale Impressionen (Englisch/Spanisch/Italienisch „near me“-Suchen) sind
  Streuverluste mit 1–3 Impressionen – keine Handlungsrelevanz, nur zur Einordnung.

## 7. Priorisierte Maßnahmen

1. **Quick Win (diese Woche):**
   - Title-Tag & Meta-Beschreibung für `/zimmer`, `/der-metzger`, `/hotel`, `/metzgerei`
     überarbeiten (klarer Nutzen/Call-to-Action im Snippet – Position ist schon gut,
     die Klicks fehlen nur wegen der Textwirkung).
   - Reputationsfrage „insolvenzverfahren“ mit dem Kunden klären.
2. **Mittelfristig (dieser Monat):**
   - Eigene Landingpage „Biergarten“ erstellen/ausbauen (Fotos, Öffnungszeiten, Karte,
     Lagebeschreibung) – bündelt aktuell zersplitterte ~150 Impressionen/Woche ohne
     eigene Zielseite.
   - Strukturierte Daten (LocalBusiness/Restaurant/Hotel-Schema) einbauen für
     Rich-Snippet-Potenzial.
   - Google-Unternehmensprofil (Maps) für „restaurant in der nähe“-Muster gegenprüfen.
3. **Beobachten:**
   - Nächsten vollen Monat exportieren und mit dieser Basislinie vergleichen, um aus
     dem Wochenrauschen einen echten Trend abzulesen.
   - „krone monheim“-Suchvolumen weiterverfolgen.
