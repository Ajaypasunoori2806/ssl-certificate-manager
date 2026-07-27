from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.database import Base


class CertificateRequest(Base):
    __tablename__ = "certificate_requests"

    id = Column(Integer, primary_key=True, index=True)

    common_name = Column(String, nullable=False)
    organization = Column(String, nullable=False)
    organizational_unit = Column(String)
    country = Column(String)
    state = Column(String)
    locality = Column(String)
    email = Column(String)

    key_path = Column(String)
    csr_path = Column(String)

    status = Column(String, default="Generated")

    created_at = Column(DateTime, default=datetime.utcnow)