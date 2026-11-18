"""Build the practice website from article.txt into the site folder."""

from html import escape
from pathlib import Path

from reading import reading_time

SOURCE = Path("article.txt")
OUTPUT = Path("site") / "index.html"


def build() -> None:
    title, _, body = SOURCE.read_text(encoding="utf-8").partition("\n")
    paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
    minutes = reading_time(len(body.split()))
    html_paragraphs = "\n".join(f"<p>{escape(p)}</p>" for p in paragraphs)
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
</head>
<body style="max-width: 40rem; margin: 2rem auto; padding: 0 1rem; font-family: sans-serif; line-height: 1.6">
<h1>{escape(title)}</h1>
<p><em>{minutes} minute read</em></p>
{html_paragraphs}
</body>
</html>
"""
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUTPUT} ({minutes} minute read)")


if __name__ == "__main__":
    build()
