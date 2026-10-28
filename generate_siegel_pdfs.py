#!/usr/bin/env python3
"""Generiert Empfehlungssiegel-PDFs für alle Finanzierungsberater."""

import base64
import html as html_mod
import subprocess
from pathlib import Path

SIEGEL_URL = "https://www.regionalimmobilien24.de/ressource/img/siegel/top_finanzierungsexperte.svg"
TEMPLATE   = Path(__file__).parent / "siegel_template.html"
LOGO_PATH  = Path("/home/null/Downloads/Doppelvorlage-2023-klein-weiss.png")

with LOGO_PATH.open("rb") as _f:
    LOGO_SRC = "data:image/png;base64," + base64.b64encode(_f.read()).decode()

BERATER = [
    ("Philipp Steppohn",              "https://www.regionalimmobilien24.de/vogtland/baufinanzierung/philipp-steppohn/"),
    ("Patrick Thier",                 "https://www.regionalimmobilien24.de/vogtland/baufinanzierung/patrick-thier/"),
    ("Lars Rupprecht",                "https://www.regionalimmobilien24.de/vogtland/baufinanzierung/lars-rupprecht/"),
    ("Wilfried Hoh",                  "https://www.regionalimmobilien24.de/zwickau/baufinanzierung/wilfried-hoh/"),
    ("Gert Holdschick",               "https://www.regionalimmobilien24.de/zwickau/baufinanzierung/gert-holdschick/"),
    ("Silvia Liebeskind",             "https://www.regionalimmobilien24.de/chemnitz/baufinanzierung/silvia-liebeskind/"),
    ("Peggy Rodewald",                "https://www.regionalimmobilien24.de/leipzig/baufinanzierung/peggy-rodewald/"),
    ("Mike Schmidt",                  "https://www.regionalimmobilien24.de/leipzig/baufinanzierung/mike-schmidt/"),
    ("Claudia Hausdorf",              "https://www.regionalimmobilien24.de/leipzig/baufinanzierung/claudia-hausdorf/"),
    ("Daniela May",                   "https://www.regionalimmobilien24.de/leipzig/baufinanzierung/daniela-may/"),
    ("Frank Lohse",                   "https://www.regionalimmobilien24.de/nordsachsen/baufinanzierung/frank-lohse/"),
    ("Max Riesenberg",                "https://www.regionalimmobilien24.de/nordsachsen/baufinanzierung/max-riesenberg/"),
    ("Diana Helm",                    "https://www.regionalimmobilien24.de/nordsachsen/baufinanzierung/diana-helm/"),
    ("Matthias Dickes",               "https://www.regionalimmobilien24.de/nordsachsen/baufinanzierung/matthias-dickes/"),
    ("Jan Philip de la Motte",        "https://www.regionalimmobilien24.de/mittelfranken/baufinanzierung/philip-delamotte/"),
    ("Christine de la Motte",         "https://www.regionalimmobilien24.de/mittelfranken/baufinanzierung/christine-delamotte/"),
    ("Niklas Lechner",                "https://www.regionalimmobilien24.de/mittelfranken/baufinanzierung/niklas-lechner/"),
    ("Jean-Claude Kühne",             "https://www.regionalimmobilien24.de/mittelfranken/baufinanzierung/jean-claude-kuehne/"),
    ("Peter Reuter",                  "https://www.regionalimmobilien24.de/mittelfranken/baufinanzierung/peter-reuter/"),
    ("Dominic Hoffmann",              "https://www.regionalimmobilien24.de/suedhessen/baufinanzierung/dominic-hoffmann/"),
    ("Rainer Veigel",                 "https://www.regionalimmobilien24.de/erzgebirge/baufinanzierung/rainer-veigel/"),
    ("Sören Uhlig",                   "https://www.regionalimmobilien24.de/erzgebirge/baufinanzierung/soeren-uhlig/"),
    ("Claudia Volke-Herrmann",        "https://www.regionalimmobilien24.de/dresden/baufinanzierung/claudia-volke-herrmann/"),
    ("Hans-Dieter Döll",              "https://www.regionalimmobilien24.de/rheintal/baufinanzierung/hans-dieter-doell/"),
    ("Stephan Klammt",                "https://www.regionalimmobilien24.de/rheintal/baufinanzierung/stephan-klammt/"),
    ("Harald Strobel",                "https://www.regionalimmobilien24.de/rheinpfalz/baufinanzierung/harald-strobel/"),
    ("Andreas Beitzen",               "https://www.regionalimmobilien24.de/koeln/baufinanzierung/andreas-beitzen/"),
    ("Ralph Schneider",               "https://www.regionalimmobilien24.de/stuttgart/baufinanzierung/ralph-schneider/"),
    ("Johannes Friedt",               "https://www.regionalimmobilien24.de/stuttgart/baufinanzierung/johannes-friedt/"),
    ("Dirk Schwarz",                  "https://www.regionalimmobilien24.de/frankfurt/baufinanzierung/dirk-schwarz/"),
    ("Tom Sander",                    "https://www.regionalimmobilien24.de/spreewald/baufinanzierung/tom-sander/"),
    ("Melanie Gmeiner",               "https://www.regionalimmobilien24.de/muenchen/baufinanzierung/melanie-gmeiner/"),
    ("Miroslav Papac",                "https://www.regionalimmobilien24.de/muenchen/baufinanzierung/miroslav-papac/"),
    ("Christiana Kurczyk",            "https://www.regionalimmobilien24.de/muenchen/baufinanzierung/christiana-kurczyk/"),
    ("Guido Allmich",                 "https://www.regionalimmobilien24.de/oberbayern/baufinanzierung/guido-allmich/"),
    ("Hubert Ebertseder",             "https://www.regionalimmobilien24.de/muenchen/baufinanzierung/hubert-ebertseder/"),
    ("Anton Neumeier",                "https://www.regionalimmobilien24.de/muenchen/baufinanzierung/anton-neumeier/"),
    ("Horst Grüger",                  "https://www.regionalimmobilien24.de/rhein-erft-kreis/baufinanzierung/horst-grueger/"),
    ("Thomas Nicolas",                "https://www.regionalimmobilien24.de/rhein-erft-kreis/baufinanzierung/thomas-nicolas/"),
    ("Marc Stoll",                    "https://www.regionalimmobilien24.de/muensterland/baufinanzierung/marc-stoll/"),
    ("Jörg Edelbrock",                "https://www.regionalimmobilien24.de/muensterland/baufinanzierung/joerg-edelbrock/"),
    ("Florian Gleißner",              "https://www.regionalimmobilien24.de/oberbayern/baufinanzierung/florian-gleissner/"),
    ("William Schwaß",                "https://www.regionalimmobilien24.de/oberbayern/baufinanzierung/william-schwass/"),
    ("Mariana Cecilia Wehrhahn",      "https://www.regionalimmobilien24.de/oberbayern/baufinanzierung/mariana-wehrhahn/"),
    ("Andreas Berndt",                "https://www.regionalimmobilien24.de/oberbayern/baufinanzierung/andreas-berndt/"),
    ("Thorsten Stehmann",             "https://www.regionalimmobilien24.de/oberbayern/baufinanzierung/thorsten-stehmann/"),
    ("Jürgen Schott",                 "https://www.regionalimmobilien24.de/oberpfalz/baufinanzierung/juergen-schott/"),
    ("Ewald Madl",                    "https://www.regionalimmobilien24.de/oberpfalz/baufinanzierung/ewald-madl/"),
    ("Andreas Engelbrecht-Eichstädt", "https://www.regionalimmobilien24.de/erfurt/baufinanzierung/andreas-engelbrecht-eichstaedt/"),
    ("Christian Schmid",              "https://www.regionalimmobilien24.de/schwarzwald/baufinanzierung/christian-schmid/"),
    ("Thomas Grosshans",              "https://www.regionalimmobilien24.de/schwarzwald/baufinanzierung/thomas-grosshans/"),
    ("Andreas Janz",                  "https://www.regionalimmobilien24.de/schwarzwald/baufinanzierung/andreas-janz/"),
    ("Katrin Johst-Mandel",           "https://www.regionalimmobilien24.de/berlin/baufinanzierung/katrin-johst-mandel/"),
    ("Andreas Schulze",               "https://www.regionalimmobilien24.de/berlin/baufinanzierung/andreas-schulze/"),
    ("Christian Appel",               "https://www.regionalimmobilien24.de/unterfranken/baufinanzierung/christian-appel/"),
    ("Uwe Madeja",                    "https://www.regionalimmobilien24.de/havelland/baufinanzierung/uwe-madeja/"),
    ("Jörg Kintzel",                  "https://www.regionalimmobilien24.de/havelland/baufinanzierung/joerg-kintzel/"),
    ("Sven Harth",                    "https://www.regionalimmobilien24.de/westpfalz/baufinanzierung/sven-harth/"),
    ("Michael Branetzki",             "https://www.regionalimmobilien24.de/niederrhein/baufinanzierung/michael-branetzki/"),
    ("André Stempel",                 "https://www.regionalimmobilien24.de/niederrhein/baufinanzierung/andre-stempel/"),
    ("Jan Doberenz",                  "https://www.regionalimmobilien24.de/mittelsachsen/baufinanzierung/jan-doberenz/"),
    ("Marie Nagel",                   "https://www.regionalimmobilien24.de/mittelsachsen/baufinanzierung/marie-nagel/"),
    ("Moritz Doberenz",               "https://www.regionalimmobilien24.de/mittelsachsen/baufinanzierung/moritz-doberenz/"),
    ("Jürgen Stengel",                "https://www.regionalimmobilien24.de/schwaebische-alb/baufinanzierung/juergen-stengel/"),
    ("Jörg Lübben",                   "https://www.regionalimmobilien24.de/oberlausitz/baufinanzierung/joerg-luebben/"),
    ("Peter Klima",                   "https://www.regionalimmobilien24.de/ruhrgebiet/baufinanzierung/peter-klima/"),
    ("Lars Nitsche",                  "https://www.regionalimmobilien24.de/ruhrgebiet/baufinanzierung/lars-nitsche/"),
    ("Oliver Wewering",               "https://www.regionalimmobilien24.de/ruhrgebiet/baufinanzierung/oliver-wewering/"),
    ("Thomas Zenker",                 "https://www.regionalimmobilien24.de/magdeburg/baufinanzierung/thomas-zenker/"),
    ("Nicole Hartig",                 "https://www.regionalimmobilien24.de/magdeburg/baufinanzierung/nicole-hartig/"),
    ("Ron Westphal",                  "https://www.regionalimmobilien24.de/holstein/baufinanzierung/ron-westphal/"),
    ("Lambert Adams",                 "https://www.regionalimmobilien24.de/holstein/baufinanzierung/lambert-adams/"),
    ("Willi Schikora",                "https://www.regionalimmobilien24.de/holstein/baufinanzierung/willi-schikora/"),
    ("Nancy Radde",                   "https://www.regionalimmobilien24.de/halle/baufinanzierung/nancy-radde/"),
    ("Oliver Thier",                  "https://www.regionalimmobilien24.de/hamburg/baufinanzierung/oliver-thier/"),
    ("Robert Regler",                 "https://www.regionalimmobilien24.de/bayerisch-schwaben/baufinanzierung/robert-regler/"),
    ("Daniel Albert",                 "https://www.regionalimmobilien24.de/bayerisch-schwaben/baufinanzierung/daniel-albert/"),
    ("Murat Güneser",                 "https://www.regionalimmobilien24.de/sauerland/baufinanzierung/murat-gueneser/"),
    ("Oliver Gehrk",                  "https://www.regionalimmobilien24.de/kiel/baufinanzierung/oliver-gehrk/"),
    ("Michael Christ",                "https://www.regionalimmobilien24.de/rostock/baufinanzierung/michael-christ/"),
    ("Dana Reibe",                    "https://www.regionalimmobilien24.de/harz/baufinanzierung/dana-reibe/"),
    ("Tobias Erler",                  "https://www.regionalimmobilien24.de/rhein-siegkreis/baufinanzierung/tobias-erler/"),
    ("Jürgen Lösch",                  "https://www.regionalimmobilien24.de/rheinneckar/baufinanzierung/juergen-loesch/"),
    ("Benjamin Fuhr",                 "https://www.regionalimmobilien24.de/bergisches-dreieck/baufinanzierung/benjamin-fuhr/"),
    ("Wolfram Aller",                 "https://www.regionalimmobilien24.de/westerwald/baufinanzierung/wolfram-aller/"),
    ("Kilian de Vries",               "https://www.regionalimmobilien24.de/weserems/baufinanzierung/kilian-de-vries/"),
    ("Axel Scholz",                   "https://www.regionalimmobilien24.de/suedwestthueringen/baufinanzierung/axel-scholz/"),
    ("Steffen Simon",                 "https://www.regionalimmobilien24.de/suedwestthueringen/baufinanzierung/steffen-simon/"),
    ("Karl-Heinz Schuh",              "https://www.regionalimmobilien24.de/oderland/baufinanzierung/karl-heinz-schuh/"),
    ("Marcus Brinkwirth",             "https://www.regionalimmobilien24.de/lueneburg/baufinanzierung/marcus-brinkwirth/"),
    ("Christoph Soetebeer",           "https://www.regionalimmobilien24.de/lueneburg/baufinanzierung/christoph-soetebeer/"),
    ("Stefan Palme",                  "https://www.regionalimmobilien24.de/augsburg/baufinanzierung/stefan-palme/"),
    ("Bernd Kreie",                   "https://www.regionalimmobilien24.de/duisburg/baufinanzierung/bernd-kreie/"),
    ("Jasmin Baruschke",              "https://www.regionalimmobilien24.de/braunschweig/baufinanzierung/jasmin-baruschke/"),
    ("Kevin Helms",                   "https://www.regionalimmobilien24.de/teutoburger-wald/baufinanzierung/kevin-helms/"),
    ("Daniel Schwan",                 "https://www.regionalimmobilien24.de/mittelhessen/baufinanzierung/daniel-schwan/"),
    ("Patrick Funke",                 "https://www.regionalimmobilien24.de/mainz/baufinanzierung/patrick-funke/"),
    ("Jan Bollenbach",                "https://www.regionalimmobilien24.de/rheinhessen/baufinanzierung/jan-bollenbach/"),
    ("Andreas Coutandin",             "https://www.regionalimmobilien24.de/rheinhessen/baufinanzierung/andreas-coutandin/"),
    ("Ronni Swatek",                  "https://www.regionalimmobilien24.de/uckermark/baufinanzierung/ronni-swatek/"),
]


def make_code_html(name, url):
    esc_name   = html_mod.escape(name)
    esc_url    = html_mod.escape(url)
    esc_siegel = html_mod.escape(SIEGEL_URL)
    return (
        f'<span class="c-tag">&lt;a</span> '
        f'<span class="c-attr">href</span><span class="c-txt">=</span>'
        f'<span class="c-val">&quot;{esc_url}&quot;</span>\n'
        f'   <span class="c-attr">rel</span><span class="c-txt">=</span>'
        f'<span class="c-val">&quot;follow&quot;</span>\n'
        f'   <span class="c-attr">target</span><span class="c-txt">=</span>'
        f'<span class="c-val">&quot;_blank&quot;</span><span class="c-tag">&gt;</span>\n'
        f'  <span class="c-tag">&lt;img</span> '
        f'<span class="c-attr">src</span><span class="c-txt">=</span>'
        f'<span class="c-val">&quot;{esc_siegel}&quot;</span>\n'
        f'       <span class="c-attr">alt</span><span class="c-txt">=</span>'
        f'<span class="c-val">&quot;Top Finanzierungsexperte – {esc_name}&quot;</span>\n'
        f'       <span class="c-attr">width</span><span class="c-txt">=</span>'
        f'<span class="c-val">&quot;200&quot;</span> <span class="c-tag">/&gt;</span>\n'
        f'<span class="c-tag">&lt;/a&gt;</span>'
    )


def safe_filename(name):
    chars = {' ': '_', 'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'Ä': 'Ae', 'Ö': 'Oe',
             'Ü': 'Ue', 'ß': 'ss', '/': '-', '\\': '-', '.': ''}
    return "".join(chars.get(c, c) for c in name if c.isalnum() or c in '_- ')


def generate_pdf(name, url, out_dir, tmp_dir):
    template = TEMPLATE.read_text(encoding="utf-8")
    html = (template
            .replace("__NAME__",      html_mod.escape(name))
            .replace("__URL__",       url)
            .replace("__LOGO_SRC__",  LOGO_SRC)
            .replace("__CODE_HTML__", make_code_html(name, url)))

    fname    = safe_filename(name)
    html_path = tmp_dir / f"{fname}.html"
    pdf_path  = out_dir / f"{fname}.pdf"
    html_path.write_text(html, encoding="utf-8")

    r = subprocess.run(
        ["chromium", "--headless=new", "--no-sandbox", "--disable-gpu",
         "--disable-dev-shm-usage",
         f"--print-to-pdf={pdf_path}",
         "--print-to-pdf-no-header", "--no-pdf-header-footer",
         f"file://{html_path}"],
        capture_output=True, text=True,
    )
    return r.returncode == 0


def main():
    out_dir = Path.home() / "pdfs"
    tmp_dir = out_dir / "_html"
    out_dir.mkdir(exist_ok=True)
    tmp_dir.mkdir(exist_ok=True)

    total = len(BERATER)
    ok = 0
    for i, (name, url) in enumerate(BERATER, 1):
        print(f"[{i:3}/{total}] {name} ...", end=" ", flush=True)
        if generate_pdf(name, url, out_dir, tmp_dir):
            print("OK"); ok += 1
        else:
            print("FEHLER")

    print(f"\nFertig: {ok}/{total} PDFs in {out_dir}")


if __name__ == "__main__":
    main()
