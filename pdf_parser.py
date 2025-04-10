
import fitz  # PyMuPDF

def extract_sections(pdf_file):
    text = ""
    with fitz.open(pdf_file.name) as doc:
        for page in doc:
            text += page.get_text()

    sections = {
        "abstract": extract_between(text, "abstract", "introduction"),
        "introduction": extract_between(text, "introduction", "methodology"),
        "methodology": extract_between(text, "methodology", "results"),
        "results": extract_between(text, "results", "conclusion"),
        "conclusion": extract_between(text, "conclusion", "")
    }
    return sections

def extract_between(text, start, end):
    start_idx = text.lower().find(start)
    end_idx = text.lower().find(end) if end else len(text)
    return text[start_idx:end_idx].strip()
