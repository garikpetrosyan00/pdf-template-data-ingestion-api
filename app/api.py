from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil

router = APIRouter()

@router.post("/api/v1/pdf/extract")
async def extract_pdf_data(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    return {
        "status": "success",
        "filename": file.filename,
        "document_type": "unknown",
        "data": {}
    }
