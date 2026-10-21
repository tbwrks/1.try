# SEO-Audit: foundation.maschinenring.de/de/

*Erstellt am 21.10.2026. Methodischer Hinweis: Der direkte Abruf von foundation.maschinenring.de (und aller anderen externen Hosts) war aus dieser Umgebung durch die Netzwerk-Policy der Cloud-Sitzung blockiert (Proxy-Antwort 403 auf CONNECT). Alle On-Page-Befunde stützen sich deshalb auf das, was Suchmaschinen über die Seite ausgeben (indexierte URLs, angezeigte Titel, Snippets, Mitbewerber-Rankings) sowie auf Drittquellen. Rein technische Prüfungen (HTML-Quelltext, robots.txt, Sitemap, Core Web Vitals, strukturierte Daten, hreflang-Tags) konnten nicht durchgeführt werden und sind in Abschnitt 8 als Checkliste für den Direktzugriff hinterlegt.*

---

## 0. Kurzfazit

Die Seite der Maschinenring Foundation gGmbH ist eine kleine Spenden- und Projektseite (ca. 7 bis 9 indexierte URLs) mit guter inhaltlicher Substanz, aber deutlichen strukturellen SEO-Schwächen. Die wichtigsten Befunde, nach Dringlichkeit:

| Prio | Befund | Wirkung |
|---|---|---|
| 1 | **Gleicher Inhalt auf mehreren Hosts indexiert**: `foundation.maschinenring.de`, `entwicklungszusammenarbeit.maschinenring.de`, `preview.maschinenring.de` sowie `www.maschinenring.de/foundation`. Keine erkennbare kanonische Konsolidierung. | Rankingsignale verteilen sich auf drei bis vier Domains, Google wählt selbst, welche Version erscheint. Eine Preview-/Staging-Umgebung ist für Google erreichbar. |
| 2 | **Title-Tags fehlen oder sind generisch.** Startseite /de/ erscheint nur als „Maschinenring“, die EN-Startseite wechselnd als „DE \| EN \| FR“ oder „donate now - zur Maschinenring Foundation“, die Kenia-Seite teils nur als nackte URL. | Google generiert Titel selbst; Klickrate und Markenerkennung in den Suchergebnissen leiden. Die deutsche Startseite erscheint bei der Markensuche gar nicht. |
| 3 | **Vertrauensrisiko durch widersprüchliche Angaben**: zwei unterschiedliche IBANs auf verschiedenen Unterseiten, sich widersprechende Projektkennzahlen (Anzahl Ringe/Mitglieder), eine Spendenkampagne mit abgelaufenem Stichtag (Oktober 2025) weiterhin live. | Für eine Spendenseite der kritischste Punkt: Zweifel am Spendenkonto kostet unmittelbar Conversions, widersprüchliche Zahlen schwächen E-E-A-T-Signale. |
| 4 | **Sprach- und URL-Struktur inkonsistent**: `/de/`, `/en/`, aber `/kenia/en/`, `/senegal/en/` und `/de/einfach15.html`. Französische Version wird im Sprachmenü angeboten, ist aber nicht indexiert. Google liefert auf deutsche Suchanfragen die englischen Seiten aus. | Deutet auf fehlende oder fehlerhafte hreflang-Auszeichnung hin. Deutsche Zielgruppe landet auf englischen Seiten. |
| 5 | **Dünne Indexierung, fehlende Vertrauensseiten**: Impressum, Datenschutz, Kontakt und Team sind nicht indexiert; keine Projektnews, keine Transparenzinformationen (Jahresbericht, Mittelverwendung) auf der Subdomain. Die zweite Satzungsaufgabe (Nothilfe für Landwirte in Deutschland) fehlt auf der Subdomain komplett. | Geringe thematische Autorität, kaum Rankingchancen jenseits der Marke. |
| 6 | **Markensichtbarkeit**: Bei „Maschinenring Foundation“ rankt ein topagrar-Artikel vor der eigenen Seite; bei „Maschinenring Afrika“ liegen t3n und Tagesspiegel vorn. | Markensuchende werden zu Dritten geführt. |

Quick Wins (unter einem Tag Aufwand): IBAN vereinheitlichen, Kampagnen-Stichtag aktualisieren, Title-Tags und Meta-Descriptions für alle Seiten setzen, Preview-Host sperren, `entwicklungszusammenarbeit.*` per 301 auf `foundation.*` umleiten.

---

## 1. Prüfumfang und Methodik

**Geprüft wurde** (indirekt über Suchmaschinen und Drittquellen):

- Welche URLs des Hosts indexiert sind und unter welchem Titel sie erscheinen
- Duplikate auf anderen Hosts der Marke
- URL- und Sprachstruktur
- Inhaltliche Konsistenz der indexierten Snippets (Kennzahlen, Bankdaten, Fristen)
- Sichtbarkeit für Marken- und erste generische Suchanfragen
- Erwähnungen und Verlinkungen durch Dritte

**Nicht geprüft werden konnte** (siehe Abschnitt 8):

- HTML-Quelltext: `<title>`, Meta-Description, Canonical, hreflang, `lang`-Attribut, Überschriftenstruktur, Alt-Texte, strukturierte Daten, Open Graph
- robots.txt und XML-Sitemap
- HTTP-Status, Weiterleitungsketten (http→https, www, Trailing Slash), 404-Verhalten
- Ladezeit und Core Web Vitals, Bildoptimierung, Mobile-Darstellung
- Interne Verlinkung, Sicherheits-Header, Consent/Tracking

---

## 2. Indexierung und Domain-Architektur

### 2.1 Indexierte URLs auf foundation.maschinenring.de

| URL | Titel laut Suchergebnis | Bemerkung |
|---|---|---|
| `/de/` | „Maschinenring“ | Startseite DE. Titel nicht aussagekräftig, identisch mit anderen Seiten. |
| `/en/` | „donate now - zur Maschinenring Foundation“ bzw. „DE \| EN \| FR“ | Zwei verschiedene Titel für dieselbe URL: Google generiert den Titel offenbar aus Seitentext (Sprachumschalter bzw. Spenden-Button). Ein klarer Hinweis, dass das `<title>`-Element fehlt oder unbrauchbar ist. |
| `/de/einfach15.html` | „Werde auch du Teil dieser Mission mit „Einfach15€““ | Kampagnenseite. Einzige DE-Unterseite mit eigenem Titel, aber ohne Markenzusatz. `.html`-Endung passt nicht zur restlichen Struktur. |
| `/en/einfach15.html` | „Maschinenring Entwicklungszusammenarbeit“ | Titel trägt den alten Projektnamen statt der Marke „Foundation“. |
| `/kenia/de/` | „Wir unterstützen kleinbäuerliche Betriebe in Kenia - Foundation“ | Einzige Seite mit sauberem, beschreibendem Titel samt Suffix. Dieses Muster sollte Standard werden. |
| `/kenia/en/` | „Maschinenring“ / „We support smallholder family farms in Kenya.“ / „foundation.maschinenring.de“ | Drei verschiedene Darstellungen, einmal nur die Domain: Google findet keinen verwertbaren Titel. |
| `/senegal/en/` | „The mechanization of agriculture in Senegal. - Foundation“ bzw. „DE \| EN \| FR“ | Wechselnde Titel, siehe oben. |
| `/senegal/de/` | nicht in den Ergebnissen | Vermutlich vorhanden, aber nicht (mehr) indexiert oder von der EN-Version verdrängt. |
| `/fr/…` | nicht in den Ergebnissen | Französische Version im Sprachmenü, aber nicht indexiert. |
| Impressum / Datenschutz / Kontakt | nicht in den Ergebnissen | Werden laut Snippets im Footer verlinkt, sind aber nicht indexiert. |

### 2.2 Duplikate auf anderen Hosts

| Host | Gefundene URLs | Einordnung |
|---|---|---|
| `entwicklungszusammenarbeit.maschinenring.de` | `/en`, `/senegal/en`, `/kenia/en` | Inhaltlich identisch mit der Foundation-Seite (gleiche Texte, gleiche Spendenaufforderung, teils andere Kennzahlen). Offenbar der frühere Projekt-Host, der nie umgeleitet wurde. |
| `preview.maschinenring.de` | `/en/projekte/kenia.html` | Eine Preview-/Staging-Umgebung ist öffentlich erreichbar und taucht in Suchergebnissen auf. Zeigt zudem eine andere URL-Logik (`/en/projekte/kenia.html`), also vermutlich ein Relaunch-Stand. |
| `www.maschinenring.de` | `/foundation`, `/foundation-deutschland`, mehrere Blog-Beiträge zu Senegal/Kenia | Die Hauptdomain mit deutlich mehr Autorität trägt eigene Foundation-Seiten und veröffentlicht die Projektnews. Die Subdomain konkurriert damit um dieselben Begriffe. |

### 2.3 Bewertung und Empfehlung

Für Google existieren derzeit mindestens drei gleichwertige Quellen für „Maschinenring Foundation Afrika“. Das verteilt Verlinkungen und Nutzersignale, und Google entscheidet pro Suchanfrage selbst, welche Variante erscheint (sichtbar daran, dass bei Markensuchen mal `/en/`, mal `/senegal/en/`, mal die Hauptdomain auftaucht).

Empfehlung:

1. **Eine kanonische Domain festlegen.** Zwei vertretbare Wege:
   - *Variante A (empfohlen bei eigenständiger Spendenmarke):* `foundation.maschinenring.de` als alleiniger Host. Alle Projektnews der Foundation werden dort veröffentlicht; `www.maschinenring.de/foundation` wird zu einer kurzen Teaser-Seite mit prominentem Link.
   - *Variante B (empfohlen bei knappen Ressourcen):* Foundation als Verzeichnis `www.maschinenring.de/foundation/…` in die Hauptdomain integrieren und die Subdomain per 301 umleiten. Profitiert sofort von der Autorität der Hauptdomain, verliert aber die Eigenständigkeit der Marke.
2. **`entwicklungszusammenarbeit.maschinenring.de` per 301** seitenweise auf die entsprechenden Foundation-URLs umleiten (nicht pauschal auf die Startseite).
3. **`preview.maschinenring.de` sperren**: HTTP-Basic-Auth oder IP-Beschränkung, zusätzlich `X-Robots-Tag: noindex` und Entfernung aus dem Index über die Search Console. Prüfen, ob der Preview-Host versehentlich irgendwo öffentlich verlinkt ist (z. B. im Sprachumschalter oder in Newslettern).
4. **Canonical-Tags** auf jeder Seite auf die eigene kanonische URL setzen (selbstreferenzierend), damit künftige Kopien nicht erneut konkurrieren.

---

## 3. Title-Tags, Meta-Descriptions und Snippets

### 3.1 Befund

Die wechselnden Titel für dieselbe URL (Abschnitt 2.1) zeigen, dass Google keinen brauchbaren `<title>` findet und stattdessen sichtbaren Seitentext verwendet, konkret den Sprachumschalter („DE | EN | FR“), den Spenden-Button („donate now“) oder nur den Hostnamen. Wo ein Titel existiert, ist er entweder generisch („Maschinenring“ auf mindestens drei Seiten) oder ohne Markenzusatz.

Wahrscheinliche Ursachen (im Direktzugriff zu bestätigen):

- `<title>` fehlt auf einzelnen Templates oder enthält nur „Maschinenring“
- Der Sprachumschalter steht im Quelltext vor dem eigentlichen Inhalt und ist möglicherweise als Überschrift ausgezeichnet
- Keine oder identische Meta-Descriptions

### 3.2 Vorschläge

Zielwerte: Title bis ca. 60 Zeichen, Description 140 bis 160 Zeichen, jede Seite eindeutig, Marke konsistent als „Maschinenring Foundation“.

| URL | Vorschlag Title | Vorschlag Meta-Description |
|---|---|---|
| `/de/` | Maschinenring Foundation \| Hilfe für Kleinbauern in Afrika | Die gemeinnützige Maschinenring Foundation gGmbH baut Maschinenringe im Senegal und in Kenia auf. Spenden Sie für Pflüge, Dreschmaschinen und Mühlen, die Kleinbauern direkt helfen. |
| `/de/einfach15.html` | Einfach 15 € spenden: Maschinenringe für den Senegal | 15.000 € Startkapital gründen einen Maschinenring für bis zu 300 Betriebe. Mit 15 € werden Sie Teil der Mission. Jetzt per PayPal oder Überweisung spenden. |
| `/kenia/de/` | Projekt Kenia: Maschinenringe für Kleinbauern \| MR Foundation | In Westkenia teilen sich Kleinbauern über Maschinenringe moderne Bodenbearbeitungsgeräte. Erfahren Sie, wie das Projekt wirkt und wie Sie unterstützen können. |
| `/senegal/de/` | Projekt Senegal: Mechanisierung für Kleinbauern \| MR Foundation | Seit 2017 entstehen im Senegal Maschinenringe nach deutschem Vorbild. Zahlen, Partner und Spendenmöglichkeiten im Überblick. |
| `/en/` | Maschinenring Foundation \| Supporting Smallholders in Africa | The non-profit Maschinenring Foundation sets up machinery rings in Senegal and Kenya. Donate to fund ploughs, threshers and mills for smallholder farmers. |

Ergänzend: Open-Graph- und Twitter-Card-Tags mit eigenem Bild pro Seite. Spendenkampagnen werden überwiegend über Social Media und Messenger geteilt; ohne OG-Tags erscheint dort der gleiche unbrauchbare Titel wie bei Google.

---

## 4. URL-Struktur und Sprachversionen

### 4.1 Befund

| Beobachtung | Problem |
|---|---|
| Sprachkürzel an unterschiedlichen Positionen: `/de/` vs. `/kenia/de/` vs. `/senegal/en/` | Keine einheitliche Hierarchie; Sprachversionen lassen sich nicht sauber per Verzeichnis in der Search Console trennen. |
| `.html`-Endung nur bei der Kampagnenseite | Uneinheitlich, deutet auf statisch generierte Einzelseiten neben CMS-Seiten hin. |
| Französische Version nicht indexiert | Entweder nicht verlinkt, per `noindex` gesperrt, hinter JavaScript versteckt oder als Duplikat verworfen. |
| Deutsche Suchanfragen („Maschinenring Afrika“, „Maschinenring Foundation spenden“) liefern `/en/` und `/senegal/en/` | Google kann die Sprachzuordnung nicht erkennen: hreflang fehlt oder ist fehlerhaft, oder die DE-Seiten gelten als Duplikat der EN-Seiten. |
| Preview-Host nutzt `/en/projekte/kenia.html` | Ein Relaunch mit neuer Struktur ist offenbar in Arbeit; Chance, die Struktur jetzt richtig zu setzen. |

### 4.2 Empfehlung

Zielstruktur (Beispiel):

```
/de/                          Startseite
/de/projekte/senegal/
/de/projekte/kenia/
/de/einfach-15/               Kampagne
/de/spenden/                  zentrale Spendenseite
/de/ueber-uns/                Team, Aufsichtsrat, Transparenz
/de/aktuelles/…               Projektnews
/de/impressum/  /de/datenschutz/  /de/kontakt/
/en/… und /fr/… spiegelgleich
```

- Pro Seite `hreflang` für de, en, fr plus `x-default` (auf /de/ oder eine Sprachauswahl), wechselseitig und selbstreferenzierend
- `<html lang="de">` je Sprachversion korrekt setzen
- Sprachumschalter als normale `<a href>`-Links (nicht per JavaScript), damit die FR-Seiten gefunden werden
- Alte URLs (inkl. `.html`-Varianten und `/kenia/en/`) per 301 auf die neue Struktur umleiten

---

## 5. Inhalte, Aktualität und Vertrauen (E-E-A-T)

Für eine Spendenorganisation sind Vertrauenssignale das zentrale Rankingkriterium und zugleich der wichtigste Conversion-Faktor. Hier liegen die gravierendsten Befunde.

### 5.1 Widersprüchliche Bankverbindung

In den indexierten Snippets erscheinen zwei verschiedene IBANs für denselben Empfänger „Maschinenring Foundation gGmbH“:

| Seite(n) | Bank laut Snippet | IBAN |
|---|---|---|
| Startseite, Senegal-Seite | Sparkasse Altbayern | DE13 7205 1210 0005 9690 19 |
| Kenia-Seite | Sparkasse Neuburg-Rain | DE89 7215 2070 0005 9690 19 |

Die identische Kontonummer bei unterschiedlicher Bankleitzahl spricht für eine alte und eine neue Bankverbindung nach einer Sparkassenfusion. Das ist intern zu klären und auf **eine** IBAN zu vereinheitlichen, idealerweise in einer zentralen, wiederverwendeten Komponente statt in jedem Template einzeln. Wird die alte Verbindung noch geführt, sollte dennoch nur die aktuelle veröffentlicht werden. Dieser Punkt hat Vorrang vor allen anderen Maßnahmen.

### 5.2 Widersprüchliche Kennzahlen

| Angabe | Quelle |
|---|---|
| Kenia: 24 Maschinenringe, ca. 9.000 Mitglieder | `/kenia/en/` |
| Kenia: ca. 283 Mitglieder | `/kenia/en/` (anderer Abschnitt) |
| Senegal: 258 Maschinenringe in sieben Jahren | `/de/einfach15.html` |
| Senegal: 36.364 Mitglieder bzw. 5.379 Mitglieder, 66.000 ha | `/senegal/en/` (zwei Abschnitte derselben Seite) |
| Senegal und Kenia gesamt: 130 Ringe, 30.500 Betriebe in fünf Jahren | Foundation-Seiten |
| Senegal: 111 Ringe, 23.000 Mitglieder | `entwicklungszusammenarbeit.maschinenring.de` |
| Senegal: 3 regionale, 21 lokale Ringe, knapp 3.000 Mitglieder | `maschinenring.de`-Blog |

Teils sind das Momentaufnahmen aus verschiedenen Jahren, teils ist unklar, ob Ringe, Mitglieder oder Betriebe gemeint sind. Für Leser und für Google wirkt es widersprüchlich. Empfehlung: eine zentrale Kennzahlentabelle mit Stand-Datum („Stand: Monat Jahr“) pflegen und auf allen Seiten aus dieser Quelle ausspielen; alte Hosts abschalten (Abschnitt 2).

### 5.3 Abgelaufene Kampagne

Die Kampagne „Einfach 15 €“ nennt laut Snippet einen Stichtag im Oktober 2025, der verstrichen ist. Die Seite ist weiterhin indexiert und rankt für Markensuchen. Empfehlung: Seite behalten (sie hat Verlinkungen und einen eigenen Titel), aber den Stand aktualisieren: erreichter Betrag, Anzahl gegründeter Ringe, nächste Etappe. Eine erledigte Kampagne mit Ergebnis ist ein stärkeres Vertrauenssignal als ein abgelaufener Countdown.

### 5.4 Auszeichnung korrekt benennen

Die Seite verweist laut Snippet auf den SDG Innovation Award 2024 (Senat der Wirtschaft / UNIDO). Die UNIDO-Nominiertenliste führt die Foundation als Nominierte; ob sie Preisträgerin wurde, war aus den Suchergebnissen nicht zu belegen. Die Formulierung auf der Seite sollte dem tatsächlichen Status entsprechen („nominiert für“ oder „ausgezeichnet mit“) und auf die offizielle Quelle verlinken.

### 5.5 Fehlende Vertrauens- und Transparenzinhalte

Auf der Subdomain nicht auffindbar:

- Impressum, Datenschutz, Kontakt (verlinkt, aber nicht indexiert; Impressum und Kontakt sollten indexierbar sein)
- Team und Gremien (Geschäftsführung, Aufsichtsrat, Koordination Westafrika) mit Namen, Foto, Funktion
- Transparenz: Jahresbericht, Mittelverwendung, Freistellungsbescheid/Gemeinnützigkeit, Spendenquittung, Mitgliedschaft in Transparenzinitiativen (z. B. Initiative Transparente Zivilgesellschaft) oder ein DZI-Spendensiegel, sofern vorhanden oder angestrebt
- Partner und Förderer (Bayerisches Landwirtschaftsministerium, sequa/BMZ, UNIDO, HSWT) mit Logo und Link: diese Nennungen existieren in Drittquellen, aber nicht als eigene Seite
- Die zweite Satzungsaufgabe (Nothilfe für Landwirte in Deutschland, Hochwasserhilfe) liegt nur auf `www.maschinenring.de/foundation-deutschland`. Wer über die Subdomain kommt, erfährt nichts davon.

### 5.6 Strukturierte Daten

Empfohlen (im Direktzugriff prüfen, ob bereits vorhanden):

- `Organization` bzw. `NGO` mit `name`, `legalName` (Maschinenring Foundation gGmbH), `address`, `logo`, `sameAs` (Hauptdomain, LinkedIn, Register-Einträge), `nonprofitStatus`
- `DonateAction` auf den Spendenseiten
- `BreadcrumbList` auf Unterseiten
- Optional `Project` für Senegal und Kenia

---

## 6. Markensichtbarkeit und Rankings

| Suchanfrage | Was erscheint | Bewertung |
|---|---|---|
| „Maschinenring Foundation“ | Platz 1: topagrar-Artikel zur Gründung; danach `/en/` mit Titel „DE \| EN \| FR“; die DE-Startseite fehlt | Eigene Seite verliert die Markensuche gegen Presse. Ursache: fehlender Titel, Duplikate, keine Sprachzuordnung. |
| „Maschinenring Afrika“ | t3n, Tagesspiegel Background, dann `/en/` und `/senegal/en/` | Englische Seiten für deutsche Anfrage; DE-Seiten unsichtbar. |
| „Maschinenring Foundation spenden Afrika Senegal“ | topagrar, `/en/`, bayern.de-PDF, `/senegal/en/`, `entwicklungszusammenarbeit.*` | Drei eigene Hosts konkurrieren in einer Ergebnisliste. |
| „Kleinbauern Afrika spenden Landwirtschaft Mechanisierung“ (generisch) | Forschungs- und Nachrichtenquellen, keine Foundation-Seite | Erwartbar bei aktuellem Content-Umfang. Potenzial liegt in Nischenbegriffen rund um „Maschinenring“, „Mechanisierung Kleinbauern“, „Senegal Landwirtschaft spenden“. |

Nach der Konsolidierung (Abschnitt 2) und sauberen Titeln (Abschnitt 3) sollte die Markensuche innerhalb weniger Wochen die DE-Startseite auf Platz 1 zeigen. Generische Sichtbarkeit setzt zusätzlichen Content voraus (Abschnitt 5.5 und 9).

---

## 7. Off-Page: Erwähnungen und Verlinkungspotenzial

Gefundene Erwähnungen (Verlinkung im Direktzugriff zu prüfen):

- topagrar.com: Gründung der Foundation und Reportage Senegal
- t3n.de und background.tagesspiegel.de: Kampagne #ItsUpToYouElon bzw. Maschinenringe für Afrika
- isrg.bayern.de: PDF „Bayerisches Afrikapaket“
- hswt.de: Forschungsprojekt FAMFISK (Senegal und Kenia)
- unido.org: Nominiertenliste SDG Innovation Award 2024
- maschinenring.de: Blog-Beiträge (Millionen-Zuschuss, Landesverband Senegal, Kooperation mit UNIDO, Aufsichtsrat)
- maschinenring.at: PDF-Downloads
- dnb.com, getbaito.com: Firmenprofile

Empfehlungen:

1. Alle internen Verweise auf `maschinenring.de` und `maschinenring.at` auf die kanonische Foundation-URL und die passende Sprachversion umstellen (derzeit verweisen Dritte teils auf `/en/`).
2. Partner (HSWT, UNIDO, Ministerium, sequa) um Verlinkung auf die Projektseiten bitten; Gegenverlinkung über eine Partnerseite anbieten.
3. Pressebereich mit Logo, Bildmaterial, Kurzprofil und der korrekten URL anlegen, damit künftige Berichte sauber verlinken.
4. Einheitliche Firmendaten (Name, Adresse, Telefon) in allen Verzeichnissen: „Maschinenring Foundation gGmbH, Am Maschinenring 1, 86633 Neuburg an der Donau“ (Adresse laut Drittquellen, intern bestätigen).

---

## 8. Nicht prüfbare Punkte: Checkliste für den Direktzugriff

Sobald der Zugriff auf den Host möglich ist (Netzwerkfreigabe für `foundation.maschinenring.de` in den Einstellungen der Cloud-Umgebung oder Prüfung von einem anderen Rechner), sind folgende Punkte nachzuholen:

| Prüfpunkt | Erwartung |
|---|---|
| HTTP-Status und Weiterleitungen: `http://`, `https://`, mit/ohne `www`, `/`, `/de`, `/de/` | Jeweils genau eine 301 auf die kanonische URL, keine Ketten |
| `robots.txt` | Vorhanden, keine versehentliche Sperre, Sitemap-Verweis |
| XML-Sitemap | Alle kanonischen URLs aller Sprachen, korrekte `lastmod` |
| `<title>`, Meta-Description pro Seite | Eindeutig, siehe Abschnitt 3 |
| `rel="canonical"` | Selbstreferenzierend, absolut, https |
| `hreflang` und `<html lang>` | de/en/fr + x-default, wechselseitig |
| Überschriften | Genau eine H1 pro Seite, Sprachumschalter nicht als Überschrift |
| Strukturierte Daten | Organization/NGO, DonateAction, BreadcrumbList; Validierung ohne Fehler |
| Open Graph / Twitter Cards | Titel, Beschreibung, Bild pro Seite |
| Core Web Vitals (PageSpeed Insights / Lighthouse mobil) | LCP < 2,5 s, INP < 200 ms, CLS < 0,1 |
| Bilder | Alt-Texte, moderne Formate (WebP/AVIF), `width`/`height`, Lazy Loading unterhalb des Viewports |
| Mobile | Viewport-Meta, keine horizontalen Scrollbalken, Tap-Ziele |
| Interne Verlinkung | Jede Seite in max. 3 Klicks von der Startseite; Footer-Links zu Impressum/Datenschutz/Kontakt indexierbar |
| 404-Seite | Echter 404-Status, hilfreiche Seite mit Navigation |
| Sicherheit | HSTS, keine Mixed-Content-Warnungen |
| Consent / Tracking | Nur nach Einwilligung, Analytics vorhanden (Search Console, Spenden-Conversion-Tracking) |
| Search Console | Abdeckungsbericht: Duplikate ohne Canonical, hreflang-Fehler, Soft-404 |

Befehle für die Nachprüfung:

```bash
# Weiterleitungen und Status
for u in http://foundation.maschinenring.de/ https://foundation.maschinenring.de/ \
         https://foundation.maschinenring.de/de https://foundation.maschinenring.de/de/ \
         https://www.foundation.maschinenring.de/ https://entwicklungszusammenarbeit.maschinenring.de/ \
         https://preview.maschinenring.de/; do
  curl -sSIL -o /dev/null -w "$u -> %{http_code} %{redirect_url}\n" "$u"
done

# Crawl-Steuerung
curl -sS https://foundation.maschinenring.de/robots.txt
curl -sS https://foundation.maschinenring.de/sitemap.xml | head -50

# Head-Elemente der Startseite
curl -sS https://foundation.maschinenring.de/de/ \
  | grep -iE '<title|name="description"|rel="canonical"|hreflang|<html|og:|ld\+json|<h1'

# Performance (benötigt Node und Chromium)
npx lighthouse https://foundation.maschinenring.de/de/ --preset=desktop --only-categories=performance,seo,accessibility --output=html --output-path=./lh-desktop.html
npx lighthouse https://foundation.maschinenring.de/de/ --form-factor=mobile --only-categories=performance,seo --output=html --output-path=./lh-mobile.html
```

---

## 9. Priorisierter Maßnahmenplan

| Prio | Maßnahme | Aufwand | Wirkung |
|---|---|---|---|
| 1 | IBAN auf allen Seiten vereinheitlichen, Spendenblock als zentrale Komponente | Stunden | Conversion, Vertrauen |
| 1 | Kampagne „Einfach 15 €“ aktualisieren (Ergebnis statt abgelaufener Frist) | Stunden | Vertrauen, Markensuche |
| 1 | `preview.maschinenring.de` sperren (Auth + noindex), aus Index entfernen | Stunden | Duplikate, Sicherheit |
| 1 | `entwicklungszusammenarbeit.maschinenring.de` per 301 seitenweise umleiten | Stunden | Konsolidierung der Signale |
| 2 | Title und Meta-Description für alle Seiten setzen; Sprachumschalter aus dem Titelbereich/Überschriften nehmen | 1 Tag | Klickrate, Markensuche |
| 2 | Canonical, hreflang (de/en/fr/x-default), `lang`-Attribut | 1 Tag | Sprachzuordnung, Duplikate |
| 2 | Kennzahlen zentral pflegen, mit Stand-Datum ausspielen; Zahlen auf Senegal- und Kenia-Seite bereinigen | 1 Tag | E-E-A-T |
| 2 | Impressum, Kontakt indexierbar machen; Team-/Gremienseite anlegen | 1 bis 2 Tage | Vertrauen |
| 3 | Rollenverteilung `www.maschinenring.de/foundation` vs. Subdomain festlegen (Variante A oder B, Abschnitt 2.3); Nothilfe Deutschland auf der Subdomain abbilden oder klar verlinken | 2 bis 5 Tage | Autorität, Vollständigkeit |
| 3 | URL-Struktur vereinheitlichen (Abschnitt 4.2) mit 301-Konzept, idealerweise im anstehenden Relaunch | im Relaunch | Struktur, Wartbarkeit |
| 3 | Strukturierte Daten (Organization/NGO, DonateAction), Open Graph | 1 Tag | Rich Results, Social Sharing |
| 3 | Transparenzseite (Jahresbericht, Mittelverwendung, Gemeinnützigkeit, Partner) | 2 bis 3 Tage | E-E-A-T, Spendenbereitschaft |
| 4 | Projektnews auf der Foundation-Domain veröffentlichen (statt nur im Hauptdomain-Blog), 1 bis 2 Beiträge pro Monat | laufend | Generische Sichtbarkeit |
| 4 | Partner und Presse um Verlinkung auf kanonische DE-URLs bitten; Pressebereich | laufend | Autorität |
| 4 | Technische Nachprüfung gemäß Abschnitt 8 (CWV, Bilder, Mobile) | 1 Tag | Performance |

---

## 10. Quellen

Eigene Hosts (aus Suchergebnissen):

- https://foundation.maschinenring.de/de/
- https://foundation.maschinenring.de/en/
- https://foundation.maschinenring.de/de/einfach15.html
- https://foundation.maschinenring.de/en/einfach15.html
- https://foundation.maschinenring.de/kenia/de/
- https://foundation.maschinenring.de/kenia/en/
- https://foundation.maschinenring.de/senegal/en/
- https://entwicklungszusammenarbeit.maschinenring.de/en
- https://entwicklungszusammenarbeit.maschinenring.de/senegal/en
- https://entwicklungszusammenarbeit.maschinenring.de/kenia/en
- https://preview.maschinenring.de/en/projekte/kenia.html
- https://www.maschinenring.de/foundation
- https://www.maschinenring.de/foundation-deutschland
- https://www.maschinenring.de/blog/zuschuss-fuer-br-den-aufbau-von-maschinenringen
- https://www.maschinenring.de/blog/maschinenringe-im-senegal-gruenden-landesverband
- https://www.maschinenring.de/blog/kooperation-fuer-nachhaltige-landwirtschaft

Drittquellen:

- https://www.topagrar.com/panorama/news/maschinenring-buendelt-entwicklungs-und-kathastrophenhilfe-13171662.html
- https://www.topagrar.com/management-und-politik/aus-dem-heft/wie-maschinenringe-senegals-bauern-helfen-12665165.html
- https://t3n.de/news/landwirte-musk-welthunger-1435118/
- https://background.tagesspiegel.de/agrar-und-ernaehrung/briefing/maschinenringe-fuer-afrikas-landwirtschaft
- https://isrg.bayern.de/wp-content/uploads/2025/07/StME-Beisswenger-FINAL-Bayerisches-Afrikapaket.pdf
- https://hswt.de/en/research/research-profile/forschungsprojekte/projekt/2343-famfisk
- https://unido.org/sdg-awards
- https://www.dnb.com/business-directory/company-profiles.maschinenring_foundation_ggmbh.41b8780bd1bf14b888ed0a482b225720.html
- https://getbaito.com/en/orga/maschinenring-de-f3u60vdn
- https://www.bayern-innovativ.de/en/kompetenznetzwerk-digitale-landwirtschaft/maschinenringe-deutschland-gmbh

*Hinweis: Snippet-basierte Angaben (Titel, Zahlen, IBANs) geben den Indexstand der Suchmaschine wieder und können vom aktuellen Live-Zustand abweichen. Vor Umsetzung der Maßnahmen ist jeder Befund im Direktzugriff zu verifizieren.*
