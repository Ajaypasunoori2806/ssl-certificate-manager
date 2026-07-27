from sqlalchemy.orm import Session

from app.database.models import CertificateRequest


def create_certificate_request(
    db: Session,
    common_name: str,
    organization: str,
    organizational_unit: str,
    country: str,
    state: str,
    locality: str,
    email: str,
    key_path: str,
    csr_path: str,
):
    certificate = CertificateRequest(
        common_name=common_name,
        organization=organization,
        organizational_unit=organizational_unit,
        country=country,
        state=state,
        locality=locality,
        email=email,
        key_path=key_path,
        csr_path=csr_path,
    )

    db.add(certificate)
    db.commit()
    db.refresh(certificate)

    return certificate
def get_all_certificate_requests(db: Session):
    return db.query(CertificateRequest).all()