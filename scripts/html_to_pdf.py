import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

html_path = Path(sys.argv[1]).resolve()
pdf_path = Path(sys.argv[2]).resolve()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(html_path.as_uri())
    page.pdf(path=str(pdf_path), format="Letter", print_background=True)
    browser.close()

print(f"Wrote {pdf_path}")
