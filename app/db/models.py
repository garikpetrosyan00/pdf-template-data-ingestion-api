from sqlalchemy import Column, Integer, String, DateTime, Text, JSON
from datetime import datetime
from app.db.database import Base

class DocumentExtraction(Base):
    __tablename__ = "document_extractions"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    document_type = Column(String)
    # Storing extracted_data as JSON. 
    # Note: SQLite supports JSON type in SQLAlchemy, but it's often stored as Text under the hood. 
    # Using JSON type for better compatibility if we switch DBs later or if SQLAlchemy handles it.
    extracted_data = Column(JSON) 
    created_at = Column(DateTime, default=datetime.utcnow)
