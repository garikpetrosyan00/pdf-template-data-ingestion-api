# PDF Template Data Ingestion API

> **Automated PDF Data Extraction & Persistence Pipeline**

This project is a robust, lightweight API designed to automatically ingest PDF documents (such as invoices), extract structured data using pre-defined templates, and persist the results into a database. It serves as a foundational component for automating document processing workflows.

## Overview

Manually keying data from PDFs is slow, error-prone, and expensive. This solution addresses that problem by providing an automated pipeline that:
1.  Accepts PDF uploads via a REST API.
2.  Extracts key business fields (e.g., Invoice Number, Date, Total Amount) using flexible regex templates.
3.  Validates and stores the structured data in a database for downstream processing or analysis.

## Features

-   **RESTful API**: Simple, standard HTTP interface for easy integration with web and mobile apps.
-   **Structured Extraction**: transform unstructured PDF text into JSON data.
-   **Robust Handling**: gracefully handles missing fields or extraction failures without crashing.
-   **Database Persistence**: Automatically saves every processed record to a SQLite database.
-   **Extensible Design**: Built to easily support new document types by adding regex templates.

## Tech Stack

-   **Python 3.10+**: Core logic.
-   **FastAPI**: High-performance web framework.
-   **pdfplumber**: Precise PDF text extraction.
-   **SQLAlchemy**: Robust ORM for database interaction.
-   **SQLite**: Lightweight, serverless database for immediate deployment.

## Project Structure

-   `app/api.py`: API endpoints for handling file uploads.
-   `app/extractor/`: Core logic for PDF processing and regex pattern matching.
-   `app/db/`: Database configuration and data models.
-   `data.db`: Automatically generated SQLite database file.

## How to Run (Local Demo)

Follow these steps to get the API running on your local machine:

1.  **Create a Virtual Environment**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the Server**:
    ```bash
    uvicorn app.main:app --reload
    ```
    The server will start at `http://127.0.0.1:8000`. The database `data.db` will be created automatically on the first run.

## API Usage Example

**Endpoint**: `POST /api/v1/pdf/extract`

You can test the API using `curl` or any HTTP client.

**Request:**
```bash
curl -X POST -F "file=@/path/to/your/invoice.pdf" http://127.0.0.1:8000/api/v1/pdf/extract
```

**Response (Success):**
```json
{
  "status": "success",
  "filename": "invoice_1024.pdf",
  "document_type": "invoice",
  "data": {
    "invoice_number": "INV-1024",
    "invoice_date": "2023-10-27",
    "customer_name": "Acme Corp",
    "total_amount": "1,250.00"
  }
}
```

## Notes

-   **Template Assumption**: This demo is optimized for PDFs that follow a consistent layout (e.g., generated invoices).
-   **Customization**: Regex patterns in `app/extractor/template.py` can be easily modified to match specific vendor formats.
-   **Production Readiness**: While this demo uses SQLite, the use of SQLAlchemy allows effortless switching to PostgreSQL or MySQL for production environments.
