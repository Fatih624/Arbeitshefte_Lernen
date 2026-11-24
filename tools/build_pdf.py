#!/usr/bin/env python3
"""Baut aus den Markdown-Kapiteln eines Hefts ein druckfertiges A4-PDF (schwarz-weiß).

Aufruf:  python3 tools/build_pdf.py hefte/01_okamoto_sales_schleifmaschinen [--teil A]

Kurzbefehle im Markdown:
  [[LINIEN 5]]   -> 5 Schreiblinien
  [[FELD 60]]    -> Zeichenfeld, 60 mm hoch
  [[KARO 50]]    -> Rechenfeld mit Karos, 50 mm hoch
  [[UMBRUCH]]    -> Seitenumbruch
Dateien in kapitel/ werden alphabetisch zusammengefügt. Mit --teil A nur Dateien,
deren Name mit "A" beginnt (z. B. A00_titel.md, A01_..., A90_loesungen.md).
"""
import argparse
import pathlib
import re

import markdown
from weasyprint import CSS, HTML

ROOT = pathlib.Path(__file__).resolve().parent
CSS_FILE = ROOT / "heft.css"


def shortcodes(text: str) -> str:
    text = re.sub(
        r"\[\[LINIEN (\d+)\]\]",
        lambda m: '<div class="linien">' + "<div></div>" * int(m.group(1)) + "</div>",
        text,
    )
    text = re.sub(r"\[\[FELD (\d+)\]\]", r'<div class="feld" style="height:\1mm"></div>', text)
    text = re.sub(r"\[\[KARO (\d+)\]\]", r'<div class="karo" style="height:\1mm"></div>', text)
    text = text.replace("[[UMBRUCH]]", '<div class="umbruch"></div>')
    text = re.sub(r"_{4,}", '<span class="blank"></span>', text)  # Ausfüllfeld
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("heft")
    ap.add_argument("--teil", default="")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    heft = pathlib.Path(args.heft).resolve()
    kap = heft / "kapitel"
    files = sorted(p for p in kap.glob("*.md") if p.name.startswith(args.teil))
    md = markdown.Markdown(extensions=["tables", "attr_list", "md_in_html", "sane_lists"])
    parts = []
    for f in files:
        parts.append(f'<section class="datei">{md.convert(shortcodes(f.read_text(encoding="utf-8")))}</section>')
        md.reset()
    html = f'<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"></head><body>{"".join(parts)}</body></html>'

    out = pathlib.Path(args.out) if args.out else heft / "pdf" / f"Heft_{heft.name}{'_Teil_' + args.teil if args.teil else ''}.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html, base_url=str(kap)).write_pdf(out, stylesheets=[CSS(filename=str(CSS_FILE))])
    print(out)


if __name__ == "__main__":
    main()
