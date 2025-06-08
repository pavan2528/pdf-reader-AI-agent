import pdfplumber

def extract_pdf_content(pdf_path):
    content = {"title": "", "abstract": "", "sections": {}, "tables": [], "references": ""}
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""
            # Extract tables
            tables = page.extract_tables()
            for table in tables:
                content["tables"].append(table)
        # Simple heuristics for title, abstract, etc.
        lines = full_text.split('\n')
        content["title"] = lines[0] if lines else ""
        content["abstract"] = next((l for l in lines if "abstract" in l.lower()), "")
        # Further parsing for sections, references, etc. can be added here
        content["full_text"] = full_text
    return content
