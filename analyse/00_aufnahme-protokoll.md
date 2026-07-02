# Aufnahme-Protokoll — tbwrks Wissensarchitektur

Lebendes Arbeitsdokument. Zweck: nachvollziehbar festhalten, welches Dokument
verarbeitet wurde und welche Muster daraus stammen — jede Ableitung mit Beleg.

**Methode (nach deiner Vorgabe):** analysieren → Muster extrahieren → verdichten
→ System erst am Ende. Keine Erfindung, keine fremden Frameworks, keine
Interpretation ohne Belegstelle. Lücken werden markiert, Widersprüche beide dokumentiert.

**Wichtiger Vorbehalt zur Belegstärke:** Ein Muster gilt erst als „wiederkehrend",
wenn es in **mindestens 2–3 Dokumenten** unabhängig auftaucht. Alles unten aus nur
einem Dokument ist als **Kandidat** markiert, nicht als gesichertes Prinzip.

---

## Status

- Werk-Evidenz empfangen: **10 Projekte / 786 reale Seiten** (Ordner `dokumente/`)
- Selbstauskunft eingebunden: **10 Dateien** inkl. bereits vorhandener Selbst-
  Kodifizierung (`SKILL.md`, `prozessmodell.md`, `prinzipien.md`, `wording.md`,
  `case-library.md`) + 5 Interview-Dateien.
- Hinweis: „1.500 Seiten" aus dem Auftrag war ein Zählartefakt (Bild-Assets je
  Seite). Realer Umfang der Werk-Evidenz: **786 Seiten**.
- Aktuelle Phase: **2 — Validierung der Selbst-Kodifizierung gegen Werk-Evidenz**

## Korpus-Register (Werk-Evidenz)

| Datei | Seiten | Projekttyp lt. Selbstauskunft |
|---|---|---|
| DEHOGA_..._Identity-Konzeption_xs.pdf | 145 | E (Event-Identity, Phasentrichter) |
| Fetsch_..._Branding-Konzeption_xs.pdf | 121 | B (volles Rebranding, „inspecto") |
| ERC_..._Branding-Konzeption.pdf | 97 | C (Varianten/Sondertrikot, Panther) |
| Ferber_..._Konzeption_xs.pdf | 89 | B (Gastro/Hotel, nur Phase 1) |
| init_..._Branding-Konzeption_xs.pdf | 65 | B (INIT, 14-Punkte-Briefing) |
| BWAgrar_..._ArtDirection.pdf | 59 | (noch nicht in Selbstauskunft) |
| tws_..._Identity-Konzeption_xs.pdf | 47 | B (Tanzschule, Moods) |
| MaWi_..._Vermarktungs-Konzeption_xs.pdf | 34 | A (reines Consulting) |
| Natugena_..._Produktdesign-Konzpetion.pdf | 17 | D (schnelle Exploration) |
| BiSchw_..._Identity-Konzeption.pdf | 15 | (Packaging, „Pickplatz") — s. Dok 01 |

**Auffälligkeit:** `BWAgrar` (59 S.) taucht in der Selbstauskunft nirgends auf —
potenziell neues, noch nicht kodifiziertes Projekt/Projekttyp. Zu prüfen.

## Zwei Quell-Ebenen (strikt getrennt)

1. **Werk-Evidenz** — `dokumente/`: was Tobias *nachweislich* tut. Primärbasis des Systems.
2. **Selbstauskunft** — `kontext/`: was Tobias *sagt* (Interview 01.07.2026). Dient
   zum Steuern und Gegenprüfen, ersetzt aber **nie** fehlende Werk-Belege.
   Regel: Deckung beider Ebenen = gesichertes Prinzip; Abweichung = dokumentierter Befund.

**Offen:** Eine gestern erstellte „Skill-MD" ist in keinem Branch auffindbar —
Speicherort noch zu klären, dann nachziehen.

## Dokument-Register

| # | Datei | Datum | Kunde | Typ | Seiten | Status |
|---|-------|------|-------|-----|--------|--------|
| 01 | BiSchw_tbwrks_Identity-Konzeption.pdf | 26.06.2026 | Birkenschwaige (BiSchw) | Creative Direction / Identity-Konzeption (Case „Pickplatz", Bio-Vogelfutter-Packaging) | 15 | analysiert |

---

## Dok 01 — Struktur (Seiten-Skelett, beobachtet)

Kapitel werden über nummerierte Trenn-Seiten in Fliederfarbe eingeführt.
Kapitelfolge: **01_Strategie → 02_Visualität → 03_Packaging → Fortentwicklung**.

| Seite | Rubrik (Kopfzeile) | Inhalt |
|---|---|---|
| 1 | Cover „Creative Direction / 01_Strategie" + „Briefing" | Aufgabe + Produktfakten (Zutaten in %), Besonderheiten |
| 2 | „Produkt" | Umdeutung Produktnutzen → Emotion; Großzitat „Die Natur zu Gast am Fenster oder Balkon" |
| 3 | „Strategie" | Werte (Bullet-Liste) · **Warum / Wie / Was** · Produktkern (Statement+Bild) · 3 Namensoptionen m. Begründung · 3 Claim-Optionen |
| 4 | Zutaten-Begründung / „Herausforderung" | Zielgruppen-Vögel (Meisen, Finken, Spatzen); Kernsatz „Das schönere Erlebnis ist der echte Vogel, nicht der auf der Packung" |
| 5 | Trenner „01_Strategie / 02_Visualität" | Kapitelwechsel |
| 6 | „Visu Bild" | Moodboard Vogel-Illustrationen + Art-Direction-Begründung (Story/Form/Umsetzung) |
| 7 | „Visu Bild" | Wortmarke „Pickplatz", Farbe (Orange), Schrift-Specimen (Animal Condensed) |
| 8 | „Visu Zeichen" | Reduziertes Vogel-Zeichen, Explorationen |
| 9 | „Visu Zeichen" | Finale Handschrift-Wortmarke + Vogel-Icon (Negativform „P"), Schrift „News Junkie" |
| 10 | Trenner „…/03_Packaging" | Kapitelwechsel |
| 11 | „Packung Bild" | Verpackungs-Stanzkontur / Reinzeichnung, Mockup |
| 12 | „Packung Zeichen" | Verpackung mit Zeichen-Variante |
| 13 | Trenner (leer „_") | Übergang |
| 14 | „Fort Entwicklung" | Kommunikations-Ausbau: Plakat, Web/Tablet, Merch (T-Shirt), Sticker, Hashtags #keingartenistkeingrund #gartenambalkon |
| 15 | Rückseite | Datum 26.06.2026, Copyright-Hinweis |

## Muster-Rohsammlung (Kandidaten aus Dok 01)

- **[K1] Golden-Circle-Kern „Warum / Wie / Was"** als Herzstück der Strategieseite.
  Beleg: Dok 01, S. 3. (Deckt sich mit „Golden Why", das in der früheren
  Web-Recherche als tbwrks-Signatur genannt wurde → erste interne Bestätigung.)
- **[K2] Reframe rational → emotional:** Produktnutzen wird bewusst von der
  Funktion („man kann Vögel füttern") auf einen emotionalen Kern gehoben
  („kleiner, schöner, hörbarer Gruß der Natur"). Beleg: Dok 01, S. 2.
- **[K3] Prinzip „Klarheit":** wiederholt als Leitwert — „nicht in Schönheit
  sterben, sondern für Erfolg sorgen … das geht nur über Klarheit. Klarheit im
  Produkt, in der Zielgruppe, im Nutzen und Sinn." Beleg: Dok 01, S. 3.
- **[K4] Optionen-Prinzip / Entscheidungslogik:** Namen und Claims werden als
  **mehrere Varianten mit Begründung** angeboten (3 Namen, 3 Claims), nicht als
  Einzellösung. Beleg: Dok 01, S. 3.
- **[K5] Kapitel-Architektur:** Strategie → Visualität → Packaging/Umsetzung →
  Fortentwicklung, eingeleitet über nummerierte Trenn-Seiten. Beleg: Dok 01,
  S. 1/5/10/13.
- **[K6] Rubriken-Zweiteilung „Bild vs. Zeichen":** Visualität wird konsequent in
  „Visu Bild" (Bildwelt) und „Visu Zeichen" (Wort-/Bildmarke) getrennt; analog
  „Packung Bild / Packung Zeichen". Beleg: Dok 01, S. 6–9, 11–12.
- **[K7] Typo-System der Kopfzeilen:** zweiteilige Überschriften, zweites Wort in
  Akzentfarbe (Flieder) — „Visu **Bild**", „Packung **Zeichen**", „Fort
  **Entwicklung**". Beleg: Dok 01, S. 6–14.
- **[K8] Art-Direction-Raster „Story / Form / Umsetzung":** Bildwelt wird über
  diese drei Achsen begründet. Beleg: Dok 01, S. 4/6.
- **[K9] „Herausforderung" als eigener Denk-Schritt:** die zentrale gestalterische
  Spannung wird explizit benannt („echter Vogel vs. Vogel auf der Packung").
  Beleg: Dok 01, S. 4.
- **[K10] Fortentwicklung/Skalierung mitgedacht:** Kommunikation (Plakat, Web,
  Merch, Hashtags) wird ab Konzeptbeginn mitgeplant. Beleg: Dok 01, S. 14.
- **[K11] Wiederkehrende Wertesprache:** Naturverbundenheit, Sinn+Nutzen+Freude,
  Tierliebe & Verantwortung, Nachhaltigkeit, „Echt & praktisch". Beleg: Dok 01, S. 3.
- **[K12] Designsignatur:** Kraftpapier/Naturmaterial, natürliche Farben +
  ein kräftiger Akzentton (Orange), Illustration statt Foto im Kern, Flieder als
  Präsentations-Akzentfarbe. Beleg: Dok 01, S. 1/7/11/14.

## Deckungs-Abgleich Werk ↔ Selbstauskunft (laufend)

- **[D1] Reihenfolge Kernlogik → Claim → Oberfläche bestätigt.**
  Selbstauskunft: „Markenarbeit folgt der Reihenfolge: erst Kernlogik (Golden Why),
  dann Claim, dann Oberfläche/Gestaltung" (kontext/arbeitsweise-mit-claude.md).
  Werk-Evidenz: Dok 01 folgt exakt Warum/Wie/Was (S.3) → Claim-Optionen (S.3) →
  Visualität (S.6–9) → Packaging (S.11–12). → **Deckung, Prinzip gestützt.**
- **[D2] „Golden Why" als durchgängiges Werkzeug** (kontext/unternehmen-tbwrks.md)
  ↔ Warum/Wie/Was im Werk (Dok 01, S.3). Erste Werk-Bestätigung.
- **[D3] „Kein Kommunikationslärm / erst das Richtige sagen, dann gestalten"**
  (Positionierung, kontext/unternehmen-tbwrks.md) ↔ „nicht in Schönheit sterben,
  sondern für Erfolg sorgen … nur über Klarheit" (Dok 01, S.3). → Deckung.

## Offene Lücken / Widersprüche

- Noch **keine** Aussage über wiederkehrende Muster möglich — dafür fehlen weitere
  Dokumente (Zielumfang ~1.500 Seiten). Alle Punkte oben sind Kandidaten aus n=1.
- Unklar, ob die Kapitelfolge (K5) projekttypisch oder nur für Packaging-Cases gilt.
  Zu prüfen an Marken-/Positionierungsprojekten ohne Verpackung.
