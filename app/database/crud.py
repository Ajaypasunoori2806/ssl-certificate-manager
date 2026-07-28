def get_dashboard_statistics(db):
    certificates = db.query(models.CertificateRequest).all()

    total = len(certificates)

    active = 0
    expiring = 0
    expired = 0

    from datetime import datetime, timedelta

    today = datetime.utcnow()

    for cert in certificates:

        if cert.valid_until:

            expiry = cert.valid_until

            if expiry < today:
                expired += 1

            elif expiry <= today + timedelta(days=30):
                expiring += 1

            else:
                active += 1

    return {
        "total": total,
        "active": active,
        "expiring": expiring,
        "expired": expired,
    }