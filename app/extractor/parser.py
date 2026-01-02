import re
import pdfplumber
from app.extractor.template import PDF_TEMPLATE_FIELDS

def extract_data_from_pdf(file_path: str) -> dict:
    """
    Extracts text from a PDF file and applies regex patterns to find structured data.
    Returns a dictionary with keys matching template fields. 
    Missing fields are set to None.
    """
    # Initialize with None for all expected fields to ensure consistent structure
    extracted_data = {field: None for field in PDF_TEMPLATE_FIELDS.keys()}
    full_text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            # Aggregate text from all pages
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
        
        # Apply regex patterns
        # Using re.IGNORECASE for case-insensitive matching
        for field, pattern in PDF_TEMPLATE_FIELDS.items():
            match = re.search(pattern, full_text, re.IGNORECASE)
            if match:
                extracted_data[field] = match.group(1).strip()
            # No else needed as defaults are already None
            
    except Exception as e:
        print(f"Error extracting data from PDF: {e}")
        # In case of error, we still return the initialized dict (all None or partial)
        # preventing a crash in the caller which expects specific keys in 'data'
        return extracted_data

    return extracted_data
