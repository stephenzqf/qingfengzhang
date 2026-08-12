import sys
from PyPDF2 import PdfReader

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

if len(sys.argv) < 2:
    print("Usage: python extract_cert.py <path-to-certificate.pdf>")
    sys.exit(1)

path = sys.argv[1]
try:
    reader = PdfReader(path)
except Exception as e:
    print(f"Failed to open PDF: {e}")
    sys.exit(1)

print("=== PDF ===")
for i, page in enumerate(reader.pages):
    try:
        text = page.extract_text()
    except Exception as e:
        text = None
        print(f"Page {i}: [extract error: {e}]")
        continue
    print(f"Page {i}: {text if text else '[No extractable text]'}")
