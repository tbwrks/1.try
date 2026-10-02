#!/usr/bin/env python3
"""Prüft ferber/posts.json und erzeugt ferber/redaktionsplan-q4-2026.md.

Aufruf:  python3 ferber/build.py
Nur Standardbibliothek. Bei Fehlern Exit-Code 1 und eine Liste der Probleme.
"""
import datetime as dt
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "posts.json"
OUT = HERE / "redaktionsplan-q4-2026.md"

SLOT_WEEKDAY = {"di": 1, "do": 3, "so": 6}          # Montag = 0
SLOT_FORMAT = {"di": "statisch", "do": "animiert", "so": "statisch"}
SLOT_NAME = {"di": "Di", "do": "Do", "so": "So"}
BOTSCHAFT = {"essen": "Gut essen", "feiern": "Gut feiern", "sein": "Gut sein", "beweis": "Beweis"}
TYPEN = {"Feed", "Carousel", "Reel"}
REQUIRED = ["id", "datum", "uhrzeit", "kw", "slot", "format", "typ", "kampagne",
            "botschaft", "titel", "asset", "caption", "hashtag_sets", "link", "status"]
EXPECTED_WEEKS = [(2026, kw) for kw in range(41, 53)]
MIN_TAGS, MAX_TAGS, MAX_CHARS = 8, 15, 2200


def resolve_tags(post, sets):
    tags = []
    for name in post["hashtag_sets"]:
        tags.extend(sets.get(name, []))
    tags.extend(post.get("hashtags_extra", []))
    return tags


def validate(data):
    errors = []
    sets = data["hashtag_sets"]
    wochen = data["wochen"]
    posts = data["posts"]
    seen_dates, seen_ids = set(), set()
    per_week = defaultdict(list)

    for p in posts:
        pid = p.get("id", "?")
        for f in REQUIRED:
            if f not in p or p[f] in ("", [], None):
                errors.append(f"{pid}: Feld '{f}' fehlt oder ist leer")
        if pid in seen_ids:
            errors.append(f"{pid}: id doppelt")
        seen_ids.add(pid)
        try:
            d = dt.date.fromisoformat(p["datum"])
        except (KeyError, ValueError):
            errors.append(f"{pid}: Datum ungültig")
            continue
        if p["datum"] in seen_dates:
            errors.append(f"{pid}: Datum {p['datum']} doppelt")
        seen_dates.add(p["datum"])
        iso_year, iso_week, _ = d.isocalendar()
        if iso_week != p.get("kw"):
            errors.append(f"{pid}: kw {p.get('kw')} passt nicht zum Datum (ISO-KW {iso_week})")
        slot = p.get("slot")
        if slot not in SLOT_WEEKDAY:
            errors.append(f"{pid}: slot '{slot}' unbekannt")
        elif d.weekday() != SLOT_WEEKDAY[slot]:
            errors.append(f"{pid}: {p['datum']} ist kein {SLOT_NAME[slot]}")
        elif p.get("format") != SLOT_FORMAT[slot]:
            errors.append(f"{pid}: Slot {SLOT_NAME[slot]} verlangt Format '{SLOT_FORMAT[slot]}', ist '{p.get('format')}'")
        if p.get("typ") not in TYPEN:
            errors.append(f"{pid}: typ '{p.get('typ')}' unbekannt (erlaubt: {sorted(TYPEN)})")
        if p.get("botschaft") not in BOTSCHAFT:
            errors.append(f"{pid}: botschaft '{p.get('botschaft')}' unbekannt")
        try:
            dt.datetime.strptime(p.get("uhrzeit", ""), "%H:%M")
        except ValueError:
            errors.append(f"{pid}: uhrzeit '{p.get('uhrzeit')}' nicht HH:MM")
        for name in p.get("hashtag_sets", []):
            if name not in sets:
                errors.append(f"{pid}: Hashtag-Set '{name}' existiert nicht")
        tags = resolve_tags(p, sets)
        if len(tags) != len(set(tags)):
            errors.append(f"{pid}: doppelte Hashtags: {[t for t, c in Counter(tags).items() if c > 1]}")
        if not MIN_TAGS <= len(tags) <= MAX_TAGS:
            errors.append(f"{pid}: {len(tags)} Hashtags (erlaubt {MIN_TAGS}–{MAX_TAGS})")
        for t in tags:
            if not t.startswith("#") or " " in t or "-" in t:
                errors.append(f"{pid}: Hashtag '{t}' ungültig")
        total = len(p.get("caption", "")) + 2 + len(" ".join(tags))
        if total > MAX_CHARS:
            errors.append(f"{pid}: Caption + Hashtags {total} Zeichen (max {MAX_CHARS})")
        if "[" in p.get("caption", "") and "]" not in p.get("caption", ""):
            errors.append(f"{pid}: Platzhalter-Klammer in der Caption nicht geschlossen")
        per_week[(iso_year, iso_week)].append(p)

    for wk in EXPECTED_WEEKS:
        ps = per_week.get(wk, [])
        if len(ps) != 3:
            errors.append(f"KW {wk[1]}: {len(ps)} Posts statt 3")
        slots = sorted(p.get("slot", "") for p in ps)
        if slots != ["di", "do", "so"]:
            errors.append(f"KW {wk[1]}: Slots {slots} statt ['di', 'do', 'so']")
        if str(wk[1]) not in wochen:
            errors.append(f"KW {wk[1]}: kein Eintrag unter 'wochen' (Zeitraum/Fokus)")
    for wk in per_week:
        if wk not in EXPECTED_WEEKS:
            errors.append(f"KW {wk}: liegt außerhalb des Planungszeitraums")
    return errors, per_week


def fmt_date(iso):
    d = dt.date.fromisoformat(iso)
    return d.strftime("%d.%m.%Y")


def write_markdown(data, per_week):
    sets = data["hashtag_sets"]
    meta = data["meta"]
    wochen = data["wochen"]
    posts = data["posts"]
    lines = []
    add = lines.append
    add("# FERBER · Redaktionsplan Q4 2026")
    add("")
    add(f"Generiert aus `posts.json` am {dt.date.today().strftime('%d.%m.%Y')}. "
        "Nicht von Hand bearbeiten: `posts.json` ändern und `python3 ferber/build.py` ausführen.")
    add("")
    add(f"- Kunde: {meta['kunde']}")
    add(f"- Zeitraum: {meta['zeitraum']}")
    add(f"- Takt: {meta['takt']}")
    add(f"- Grundlage: {meta['grundlage']}")
    add("")
    add("## Überblick")
    add("")
    add("| Kampagne | Posts |")
    add("|---|---|")
    for k, n in Counter(p["kampagne"] for p in posts).most_common():
        add(f"| {k} | {n} |")
    add("")
    add("| Format | Posts |")
    add("|---|---|")
    for k, n in Counter(f"{p['format']} · {p['typ']}" for p in posts).most_common():
        add(f"| {k} | {n} |")
    add("")
    add("| Botschaft | Posts |")
    add("|---|---|")
    for k, n in Counter(BOTSCHAFT[p["botschaft"]] for p in posts).most_common():
        add(f"| {k} | {n} |")
    add("")
    add("Platzhalter in eckigen Klammern (zum Beispiel `[Gericht]`) füllt Tobias beim Terminieren. "
        "Jede Caption ist ein Entwurf und wird vor dem Einstellen in eigene Worte gebracht.")
    add("")
    for wk in EXPECTED_WEEKS:
        kw = wk[1]
        w = wochen[str(kw)]
        ps = sorted(per_week[wk], key=lambda p: p["datum"])
        add(f"## KW {kw} · {w['zeitraum']}")
        add("")
        add(f"**Fokus:** {w['fokus']}")
        add("")
        add("| Datum | Slot | Format | Kampagne | Botschaft | Titel |")
        add("|---|---|---|---|---|---|")
        for p in ps:
            add(f"| {fmt_date(p['datum'])} {p['uhrzeit']} | {SLOT_NAME[p['slot']]} | {p['format']} · {p['typ']} "
                f"| {p['kampagne']} | {BOTSCHAFT[p['botschaft']]} | {p['titel']} |")
        add("")
        for p in ps:
            tags = resolve_tags(p, sets)
            add("<details>")
            add(f"<summary><b>{SLOT_NAME[p['slot']]} {fmt_date(p['datum'])} · {p['titel']}</b></summary>")
            add("")
            add(f"**Asset:** {p['asset']}")
            add("")
            add("**Caption (Entwurf):**")
            add("")
            for line in p["caption"].split("\n"):
                add(f"> {line}" if line else ">")
            add("")
            add(f"**Hashtags ({len(tags)}):** {' '.join(tags)}")
            add("")
            add(f"**Linkziel:** `{p['link']}`")
            if p.get("hinweis"):
                add("")
                add(f"**Hinweis:** {p['hinweis']}")
            add("")
            add("</details>")
            add("")
    OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    errors, per_week = validate(data)
    if errors:
        print(f"{len(errors)} Problem(e) in {SRC.name}:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    write_markdown(data, per_week)
    posts = data["posts"]
    print(f"OK: {len(posts)} Posts, {len(per_week)} Wochen, {OUT.name} geschrieben.")
    for k, n in Counter(p["kampagne"] for p in posts).most_common():
        print(f"  {k:<16} {n}")
    print("  " + ", ".join(f"{k}: {n}" for k, n in Counter(p["format"] for p in posts).items()))


if __name__ == "__main__":
    main()
