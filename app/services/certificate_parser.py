from cryptography import x509
from cryptography.hazmat.primitives import hashes


def parse_certificate(certificate_path: str) -> dict:
    """
    Parse a PEM certificate and return its metadata.
    """

    with open(certificate_path, "rb") as cert_file:
        cert = x509.load_pem_x509_certificate(cert_file.read())

    return {
        "issuer": cert.issuer.rfc4514_string(),
        "serial_number": str(cert.serial_number),
        "valid_from": cert.not_valid_before,
        "valid_until": cert.not_valid_after,
        "signature_algorithm": cert.signature_hash_algorithm.name,
        "fingerprint": cert.fingerprint(hashes.SHA256()).hex().upper(),
    }