# PDF Template Data Ingestion API

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the development server:
```bash
uvicorn app.main:app --reload
```
The server will start at `http://127.0.0.1:8000`.

## Endpoints

### Health Check
`GET /health`
```json
{"status": "ok"}
```

### Upload PDF
`POST /api/v1/pdf/extract`

Example using `curl`:
```bash
curl -X POST -F "file=@/path/to/your/document.pdf" http://127.0.0.1:8000/api/v1/pdf/extract
```

Expected Output:
```json
{
  "status": "success",
  "filename": "document.pdf",
  "document_type": "unknown",
  "data": {}
}
```
*Note: Non-PDF files will return a 400 error.*
