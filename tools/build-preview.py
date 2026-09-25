"""Build the preview copy of the landing page for publishing as a Claude Artifact.

The Artifact wraps the page in its own <!doctype>/<html>/<head>/<body>, so this script
strips those tags from `Olena Bozhenko.html` and copies the assets the page uses next to it.
Usage: python tools/build-preview.py <out_dir>
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Olena Bozhenko.html"
ASSETS = [
    "assets/about/olena-bozhenko.jpg",
    "assets/work/dron/dron-order-screen.png",
    "assets/work/dron/drone-flight-camera.png",
    "assets/Olena-Bozhenko-Resume.pdf",
    "assets/music.mp3",  # optional: copied only if present
]


def main(out: Path) -> None:
    html = SRC.read_text(encoding="utf-8")
    html = re.sub(r"<!doctype[^>]*>\s*", "", html, flags=re.I)
    html = re.sub(r"</?html[^>]*>\s*", "", html, flags=re.I)
    html = re.sub(r"</?head>\s*", "", html, flags=re.I)
    html = re.sub(r"</?body[^>]*>\s*", "", html, flags=re.I)
    html = re.sub(r'<meta (charset|name="viewport")[^>]*>\s*', "", html, flags=re.I)
    # a testimonial marked DRAFT is not the person's approved words: never publish it
    html = re.sub(r"\s*<!-- DRAFT.*?-->\s*<figure[^>]*>.*?</figure>", "", html, flags=re.S)
    # the gallery shows the name only
    html = re.sub(r"<title>.*?</title>", "<title>Olena Bozhenko</title>", html, count=1, flags=re.S)
    # sticky nav sits below the phone's safe area inside the Artifact frame
    html = html.replace(".nav{position:sticky;top:0;", ".nav{position:sticky;top:env(safe-area-inset-top,0px);")
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    for rel in ASSETS:
        src = ROOT / rel
        if src.exists():
            dst = out / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print("asset", rel)
    print("page", out / "index.html")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
