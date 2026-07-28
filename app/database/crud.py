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


def get_certificate_by_id(
    db: Session,
    certificate_id: int,
):
    return (
        db.query(CertificateRequest)
        .filter(CertificateRequest.id == certificate_id)
        .first()
    )


def update_certificate_file(
    db: Session,
    certificate_id: int,
    certificate_path: str,
):
    certificate = get_certificate_by_id(
        db,
        certificate_id,
    )

    if certificate:
        certificate.certificate_path = certificate_path
        certificate.status = "Signed"

        db.commit()
        db.refresh(certificate)

    return certificate


def update_certificate_metadata(
    db: Session,
    certificate_id: int,
    issuer: str,
    serial_number: str,
    valid_from,
    valid_until,
    signature_algorithm: str,
):
    certificate = get_certificate_by_id(
        db,
        certificate_id,
    )

    if certificate:
        certificate.issuer = issuer
        certificate.serial_number = serial_number
        certificate.valid_from = valid_from
        certificate.valid_until = valid_until
        certificate.signature_algorithm = signature_algorithm

        db.commit()
        db.refresh(certificate)

    return certificate