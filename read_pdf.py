import sys
import subprocess

try:
    import pypdf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf", "--quiet"])
    import pypdf

def extract_text(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = []
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text.append(f"--- Page {i+1} ---\n{page_text}")
        print("\n".join(text))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = "/Users/chenyinbing/Documents/trae_projects/428/视量科技产品介绍资料V1.5.pdf"
    extract_text(pdf_path)