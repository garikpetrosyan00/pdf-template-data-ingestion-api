from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import tempfile
from app.extractor.parser import extract_data_from_pdf

router = APIRouter()

@router.post("/api/v1/pdf/extract")
async def extract_pdf_data(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    tmp_path = None
    try:
        # Save uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        
        # Extract data
        extracted_data = extract_data_from_pdf(tmp_path)
        
        return {
            "status": "success",
            "filename": file.filename,
            "document_type": "invoice",
            "data": extracted_data
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
        
    finally:
        # Clean up temporary file
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
