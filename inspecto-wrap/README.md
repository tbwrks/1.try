# inspecto Fahrzeugbeschriftung – realistische Mockups

Ausgangsmaterial: `Opel_888_3_chat.pdf` (Illustrator-Export) mit drei flachen Design-Varianten
(Fahrerseite + Heck) und einem Referenzfoto (schwarzer Opel Vivaro vor Betonwand).

## Eingaben (`input/`)

| Datei | Inhalt |
|---|---|
| `ref_photo.png` | Originalfoto aus dem PDF (2184 x 988 px) |
| `design1_side.png` / `design1_rear.png` | Variante 1: Wortmarke dunkelgrau mit Cyan-Kontur, Logo auf dem hinteren Seitenfenster bzw. Heckfenster links, Doppelstrich am Kotflügel |
| `design2_side.png` / `design2_rear.png` | Variante 2: wie 1, aber ohne Logo und ohne Kotflügel-Marke |
| `design3_side.png` / `design3_rear.png` | Variante 3: Wortmarke vollflächig Cyan, ohne Logo |

## Ergebnisse

Gerendert mit Higgsfield, Modell GPT Image 2 (Qualität medium, 1k).
Seite: 21:9 (1344 x 576 px), Heck: 4:3 (1168 x 880 px), Heck mit Flügeltüren (vertikale Teilung).

| Variante | Fahrerseite | Heck |
|---|---|---|
| 1 | https://d8j0ntlcm91z4.cloudfront.net/user_3HvfqVzZIDlcgC7Ck2ThrDDr5Ni/hf_20261026_143500_254d2e9b-75fd-49ee-8bbe-c946aec5ba08.png | https://d8j0ntlcm91z4.cloudfront.net/user_3HvfqVzZIDlcgC7Ck2ThrDDr5Ni/hf_20261026_150109_d5f1fcec-0569-4bfa-8db9-94678f054e7d.png |
| 2 | https://d8j0ntlcm91z4.cloudfront.net/user_3HvfqVzZIDlcgC7Ck2ThrDDr5Ni/hf_20261026_150941_cd806c7a-43a4-4650-9bb4-fcab4f5a9f14.png | https://d8j0ntlcm91z4.cloudfront.net/user_3HvfqVzZIDlcgC7Ck2ThrDDr5Ni/hf_20261026_155949_d24f6033-52e4-44de-b9b6-03025855f45a.png |
| 3 | https://d8j0ntlcm91z4.cloudfront.net/user_3HvfqVzZIDlcgC7Ck2ThrDDr5Ni/hf_20261026_151532_aed298c3-d3ff-43b7-8e70-c01877c4fcd6.png | https://d8j0ntlcm91z4.cloudfront.net/user_3HvfqVzZIDlcgC7Ck2ThrDDr5Ni/hf_20261026_160319_90475076-1968-43a2-b0a1-c2c97a7a0e4e.png |

Die Bilder liegen zusätzlich in der Higgsfield-Bibliothek des Kontos (Job-IDs siehe Tabelle unten).

| Variante | Ansicht | Job-ID |
|---|---|---|
| 1 | Seite | 254d2e9b-75fd-49ee-8bbe-c946aec5ba08 |
| 1 | Heck | d5f1fcec-0569-4bfa-8db9-94678f054e7d |
| 2 | Seite | cd806c7a-43a4-4650-9bb4-fcab4f5a9f14 |
| 2 | Heck | d24f6033-52e4-44de-b9b6-03025855f45a |
| 3 | Seite | aed298c3-d3ff-43b7-8e70-c01877c4fcd6 |
| 3 | Heck | 90475076-1968-43a2-b0a1-c2c97a7a0e4e |

## Hinweise

- Die PNGs konnten nicht in dieses Repo gelegt werden: die Netzwerk-Policy der Cloud-Umgebung
  blockiert `d8j0ntlcm91z4.cloudfront.net` (Download) und `upload.higgsfield.ai` (Upload).
  Wird einer dieser Hosts unter "Allowed domains" freigegeben, lassen sich die Dateien in einer
  weiteren Session direkt ablegen.
- Visuell geprüft: Seite 1, 2, 3 und Heck 1. Heck 2 und Heck 3 wurden nicht mehr gesichtet.
- Der Free-Plan erlaubt nur GPT Image 2 (1 Credit pro Bild, ein Job gleichzeitig). Restguthaben: 4 Credits.
