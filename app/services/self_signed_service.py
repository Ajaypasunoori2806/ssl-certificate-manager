from datetime import datetime, timedelta
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def generate_self_signed_certificate(
    key_path: str,
    common_name: str,
) -> str:
    """
    Generate a self-signed certificate using an existing private key.
    Returns the generated certificate path.
    """

    # Load private key
    with open(key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Telangana"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Hyderabad"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "SSL Certificate Manager"),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ]
    )

    certificate = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365))
        .add_extension(
            x509.BasicConstraints(ca=False, path_length=None),
            critical=True,
        )
        .sign(private_key, hashes.SHA256())
    )

    certificate_path = f"certificates/{common_name}.crt"

    with open(certificate_path, "wb") as cert_file:
        cert_file.write(
            certificate.public_bytes(serialization.Encoding.PEM)
        )

    return certificate_path