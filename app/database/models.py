from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.database import Base


class CertificateRequest(Base):
    __tablename__ = "certificate_requests"

    id = Column(Integer, primary_key=True, index=True)

    # Request Information
    common_name = Column(String, nullable=False)
    organization = Column(String, nullable=False)
    organizational_unit = Column(String)
    country = Column(String)
    state = Column(String)
    locality = Column(String)
    email = Column(String)

    # Generated Files
    key_path = Column(String)
    csr_path = Column(String)

    # Uploaded Certificate
    certificate_path = Column(String, nullable=True)

    # Certificate Details
    issuer = Column(String, nullable=True)
    serial_number = Column(String, nullable=True)
    valid_from = Column(DateTime, nullable=True)
    valid_until = Column(DateTime, nullable=True)
    signature_algorithm = Column(String, nullable=True)

    # Status
    status = Column(String, default="Generated")

    created_at = Column(DateTime, default=datetime.utcnow)