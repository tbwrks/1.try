# FERBER · Instagram-Workflow: InDesign → Adobe Express → Instagram

Stand 02.10.2026 · tbwrks für FERBER Monheim (Restaurant · Stadt.Stadl · Hotel)

Dieser Ordner ist das Arbeitssystem für drei Instagram-Posts pro Woche vom 06.10. bis 27.12.2026 (KW 41–52). Er setzt auf dem FERBER Social-Fahrplan vom 04.09.2026 auf (Leitidee, drei Ebenen, sechs Kampagnen, Wochenroutine) und macht daraus einen Ablauf, der montags in 30 Minuten durchläuft.

## Was hier liegt

| Datei | Was sie ist |
|---|---|
| `posts.json` | Die einzige Datenquelle: 36 Posts von Di 06.10.2026 bis So 27.12.2026 mit Datum, Format, Kampagne, Botschaft, Material-Hinweis, Caption-Entwurf, Hashtag-Sets, Linkziel und Hinweisen. |
| `redaktionsplan-q4-2026.md` | Lesbare Wochenübersicht, aus `posts.json` erzeugt. Nicht von Hand ändern. |
| `hashtags.md` | Die Hashtag-Sets mit Begründung und Regeln. |
| `build.py` | Prüft `posts.json` (3 Posts je Woche, Slots, Zeichen, Hashtags) und schreibt den Redaktionsplan neu. |
| Artefakt **FERBER Post-Planer** (https://claude.ai/artifact/41k3JQ1duDaw4C8vcKePmf) | Die Seite zum Arbeiten: Woche aufrufen, Caption und Hashtags mit einem Klick kopieren, Status und Notiz je Post setzen. Liest dieselbe `posts.json`. |

## Der Weg eines Posts

1. **Montag, Planungsblock:** Die drei Posts der Woche im Post-Planer öffnen. Platzhalter in eckigen Klammern klären (Gericht, Termine, Preise), Freigaben prüfen.
2. **Gestalten in InDesign:** Statische Posts aus den Mastern exportieren. Animierte Posts aus dem Export in Adobe Express animieren oder als Reel aus den 9:16-Clips schneiden.
3. **In Adobe Express terminieren:** Datei oder Express-Dokument in den Content-Planer, Caption aus dem Post-Planer kopieren und in eigene Worte bringen, Hashtag-Block anhängen, Datum und Uhrzeit aus dem Plan setzen.
4. **Status setzen:** Im Post-Planer auf „terminiert“, nach dem Erscheinen auf „veröffentlicht“.
5. **Kontrolle:** Der Kalender im Express-Planer zeigt, was ansteht. In der Meta Business Suite und auf Instagram erscheinen Express-Posts erst, sobald sie veröffentlicht sind (Express schickt sie zur Postzeit über die Meta-Schnittstelle). Stories bleiben live aus dem Haus (Fr/Sa) und laufen nicht über diesen Plan.

## 0. Einmalig einrichten

- **Adobe Express mit Instagram verbinden:** In Express den Content-Planer (Bereich „Planen“ bzw. „Inhalte planen“) öffnen und das Instagram-Konto von FERBER über den Meta-Login verbinden. Dafür braucht es den Zugang, mit dem du heute in der Meta Business Suite postest (Facebook-Seite mit verknüpftem Instagram-Business-Konto). Die Bezeichnungen in Express ändern sich gelegentlich, der Weg bleibt: Planen → Konto verbinden → Meta/Facebook anmelden → FERBER-Seite und Instagram-Konto auswählen.
- **Bio-Link mit UTM:** `https://www.ferber-monheim.de/?utm_source=instagram&utm_medium=bio` als Website-Link im Profil. Jeder Post im Plan hat zusätzlich ein eigenes Linkziel mit `utm_campaign`; das ist für Link-Sticker in Stories und für die Auswertung gedacht, in der Caption steht immer nur „Link in der Bio“.
- **InDesign-Master anlegen** (laut Fahrplan): Feed und Carousel 1080 × 1350 px, Reel-Cover und Story 1080 × 1920 px. Hurme Geometric Sans, Logo-Grün #6A8586, Kampagnenfarbe nur als Akzentfläche (Rot Weihnachten, Karamell Restaurant, Nachtblau Silvester/Hotel, Pflaume Hochzeit/Familie).
- **Testlauf:** Der erste echte Post (Di 06.10., 17:30) ist der Test. Exportieren, auf Content Credentials prüfen (siehe unten), in Express importieren und terminieren, um 17:30 auf Instagram nachsehen. Erscheint er, bleibt Express der Weg. Erscheint er nicht, zeigt Express im Kalender einen Fehler; dann den Post von Hand in der Meta Business Suite einstellen und die Verbindung neu herstellen. Danach ist der Weg bekannt und der Montag dauert 30 Minuten.

## 1. Montag: der 30-Minuten-Block

| Minuten | Was |
|---|---|
| 0–5 | Post-Planer öffnen, „Diese Woche“. Drei Posts lesen, Hinweise beachten (Freigabe, Material, Abstimmung mit dem Kunden). |
| 5–10 | Platzhalter klären: Gericht mit der Küche, freie Termine, Preise. Antworten als Notiz am Post eintragen. |
| 10–20 | Dateien aus InDesign exportieren (statisch) bzw. in Express animieren oder Reel schneiden. |
| 20–28 | In Express terminieren: Datei rein, Caption kopieren und umschreiben, Hashtags anhängen, Datum und Uhrzeit setzen, Vorschau prüfen. |
| 28–30 | Status auf „terminiert“. Kommentare und DMs der Woche beantworten (Community-Block aus dem Fahrplan). |

## 2. Statische Posts: Export aus InDesign

- Export als **PNG** (Typo bleibt scharf) oder **JPG** in Qualität „Maximum“. 1080 × 1350 px für Feed und Carousel, 1080 × 1920 px für Story-Versionen. Farbraum **sRGB**. Keine Beschnittzugabe, keine Druckmarken.
- Carousels: jede Seite als eigene Datei, Reihenfolge im Dateinamen (`01_`, `02_` …). Bis zu zehn Bilder pro Carousel.
- Bildmaterial vorher im Look nach Look-Vorschlag angleichen (Weiß bleibt weiß, Salbei und Nachtblau naturtreu).
- **Keine Firefly-Elemente** in den Post-Dateien (Generative Füllung, generativ erweiterte Hintergründe), sonst trägt der Export Content Credentials und Instagram zeigt das KI-Label. Firefly ist laut Fahrplan nur für Querformate der Website gedacht.

## 3. Animierte Posts

Zwei Wege, je nach Material:

- **Animierter Post aus dem InDesign-Layout:** Ebenen aus InDesign als einzelne PNGs (oder als PDF) exportieren, in Adobe Express als Dokument 1080 × 1920 anlegen, Elemente platzieren und mit den Express-Animationen (Einblenden, Schrift-Animation) versehen. Export als **MP4**, H.264, 30 fps, 6–15 Sekunden. Das ist der Weg für Typo-Posts wie „Save the Date“ oder „Wir sind die Antwort auf die Frage: Wo?“.
- **Reel aus den 9:16-Clips:** Die 416 Clips aus dem Shooting liegen nativ in 2160 × 3840 vor. Zusammenschnitt in Express (Video) oder Premiere, 20–45 Sekunden, Cover aus dem Reel-Cover-Master als erstes Bild oder als separates Cover hochladen.
- Limits im Content-Planer vor dem ersten Reel im eigenen Konto prüfen: Dateigröße und Länge (Quellen nennen bis zu 60 Sekunden / 100 MB für Instagram-Posts; Reels können länger sein). Bei Unsicherheit: Video als Reel direkt in der Meta Business Suite planen, der Rest bleibt in Express.
- Ton: Küchengeräusche und Raum schlagen Musik. Wenn Musik, dann aus der lizenzfreien Express-Bibliothek, nicht aus der Instagram-Musikbibliothek (die funktioniert bei geplanten Posts nicht zuverlässig).

## 4. Im Content-Planer terminieren

1. Planen → neuer Post → Instagram-Konto FERBER wählen.
2. Datei hochladen (oder das Express-Dokument direkt wählen). Bei Carousels alle Seiten in der richtigen Reihenfolge.
3. Im Post-Planer „Caption + Hashtags kopieren“, in das Textfeld einfügen. **Caption in eigene Worte bringen:** erster Satz muss tragen, ein Gedanke, ein Aufruf. Platzhalter ersetzen. Hashtag-Block mit Leerzeile unter der Caption lassen.
4. Datum und Uhrzeit aus dem Plan: Di und Do 17:30, So 11:00 (Ausnahmen stehen am Post).
5. Vorschau prüfen: Bildausschnitt, Zeilenumbrüche, kein abgeschnittener Text.
6. Terminieren. Status im Post-Planer auf „terminiert“.

Wenn der Content-Planer etwas nicht kann (Stories, zu lange oder zu große Reels), diesen einen Post in der Meta Business Suite planen: Datei aus Express herunterladen, dort hochladen, dieselbe Caption. Es bleibt bei einem Plan und einer Caption-Quelle. Nie denselben Post in beiden Werkzeugen terminieren, sonst erscheint er doppelt.

## 5. Checkliste vor jedem Terminieren

- **Botschaft:** Trägt der Post genau eine der drei Botschaften (Gut essen, Gut feiern, Gut sein) oder ist er Beweis? Steht der passende Bereich im Bild? Wenn nein: kein FERBER-Post.
- **Content Credentials:** Datei ohne C2PA-Metadaten (siehe unten).
- **Freigaben:** Erkennbare Gäste, Team, Hochzeitspaare nur mit Zustimmung. Die vier Stills unter `_Personen-pruefen/` und der Clip mit „Nicole & Peter“ auf der Torte bleiben draußen, bis das geklärt ist.
- **Fakten:** Öffnungszeiten in der entschiedenen Fassung (Restaurant Do–Sa ab 17 Uhr, Ruhetage So–Mi), Preise und Termine vom Kunden bestätigt.
- **Link:** Bio-Link aktuell, bei Stories Link-Sticker mit dem UTM-Ziel des Posts.
- **Ortsmarkierung** FERBER Monheim gesetzt, Alt-Text mit Ortsbezug.

## Das KI-Label auf Instagram

Instagram zeigt „KI-Info“, wenn die **Bild- oder Videodatei** Content Credentials (C2PA-Metadaten) trägt oder Metas eigene Erkennung anschlägt. Ausgelöst wird das von Firefly, von generativen Funktionen in Express und Photoshop und von anderen KI-Bildgeneratoren. **Der Caption-Text spielt dafür keine Rolle.** Einen mit KI vorformulierten Text in eigene Worte zu bringen ist trotzdem richtig, weil er dann nach FERBER klingt und nicht nach Vorlage.

So bleibt die Datei sauber:

- Fotos und Layouts ohne generative Elemente aus InDesign exportieren. InDesign schreibt keine Content Credentials.
- In Photoshop die Voreinstellung „Content Credentials“ ausgeschaltet lassen, solange keine Kennzeichnung gewünscht ist.
- Prüfen: Datei auf contentcredentials.org/verify ziehen, oder im Terminal `exiftool -a -G1 datei.jpg | grep -i -E "c2pa|jumbf"` (keine Ausgabe = keine Credentials).
- Firefly-Erweiterungen nur für die Website-Querformate, nicht für Instagram-Dateien.

## Pflege des Plans

- Änderungen immer in `posts.json` (Datum, Caption, Hinweis, Hashtag-Sets). Danach `python3 ferber/build.py` ausführen: Das Skript prüft die Regeln und schreibt `redaktionsplan-q4-2026.md` neu.
- Das Artefakt lädt `posts.json` als mitveröffentlichte Datei. Nach einer Änderung Claude bitten, den Post-Planer mit der neuen `posts.json` neu zu veröffentlichen; der Status je Post bleibt dabei erhalten, weil er in der Artefakt-Datenbank liegt und nicht in der Seite.
- Neue Wochen: Posts ans Ende von `posts.json` hängen, `wochen` um die Kalenderwoche ergänzen, `EXPECTED_WEEKS` in `build.py` erweitern.

## Offene Punkte, die den Plan beeinflussen

- Silvester-Format (Gala im Restaurant oder Party im Stadl), Preis, Menü: bis Anfang November mit dem Kunden festzurren (Posts ab 26.11.).
- Hochzeitspakete: Namen, Umfang, Preise (Posts ab 19.11.).
- Gutschein: Bezugsweg (nur vor Ort, per Mail, online?) für die Posts am 01.12. und 20.12.
- Hotel: Zimmeranzahl, Frühstücks- und Check-in-Zeiten (Post am 08.12.), laut Relaunch-Befund noch widersprüchlich.
- Feiertagsöffnungszeiten 24.–26.12., 31.12., 01.01. (Posts ab 13.12.).
- Content-Tag 2 im Oktober: Metzgerei, neues Interior, Familienfeier-Gerichte (Posts am 27.10. und 22.12. hängen daran).

## Für den Januar-Plan vorgemerkt

Der Plan endet am So 27.12. mit „Verlobt? Feiert bei uns.“ Diese drei Posts aus der ursprünglichen KW 53 sind gestrichen und gehören in den nächsten Plan:

- **Di 29.12. · 2026 in Bildern** (Carousel, Jahresrückblick und Danke an Gäste und Team).
- **Do 31.12. · Heute Abend** (Reel am Mittag, der Abend selbst läuft laut Fahrplan live in Stories).
- **So 03.01. · So ging 2026 zu Ende** (Danke nach Silvester, Hinweis auf Taufe, Kommunion, Firmung: Januar ist Buchungsmonat).
