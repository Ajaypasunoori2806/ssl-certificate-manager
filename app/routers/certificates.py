from app.database.crud import (
    create_certificate_request,
    get_all_certificate_requests,
    get_certificate_by_id,
    update_certificate_file,
)
from app.services.self_signed_service import generate_self_signed_certificate
from fastapi import (
    APIRouter,
    Form,
    Request,
    UploadFile,
    File,
)
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os
import shutil

from app.database.database import SessionLocal
from app.database.crud import (
    create_certificate_request,
    get_all_certificate_requests,
    get_certificate_by_id,
    update_certificate_file,
)

from app.services.certificate_service import (
    generate_key_and_csr,
    save_private_key,
    save_csr,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# ----------------------------
# Generate CSR
# ----------------------------
@router.post("/generate-csr")
async def generate_csr(
    common_name: str = Form(...),
    organization: str = Form(...),
    organizational_unit: str = Form(""),
    country: str = Form(...),
    state: str = Form(...),
    locality: str = Form(...),
    email: str = Form(""),
):
    private_key, csr = generate_key_and_csr(
        common_name,
        organization,
        organizational_unit,
        country,
        state,
        locality,
        email,
    )

    key_file = f"certificates/{common_name}.key"
    csr_file = f"certificates/{common_name}.csr"

    save_private_key(private_key, key_file)
    save_csr(csr, csr_file)

    db = SessionLocal()

    create_certificate_request(
        db=db,
        common_name=common_name,
        organization=organization,
        organizational_unit=organizational_unit,
        country=country,
        state=state,
        locality=locality,
        email=email,
        key_path=key_file,
        csr_path=csr_file,
    )

    db.close()

    return RedirectResponse(
        url="/certificates",
        status_code=303,
    )


# ----------------------------
# Certificate Inventory
# ----------------------------
@router.get("/certificates", response_class=HTMLResponse)
async def list_certificates(request: Request):

    db = SessionLocal()
    certificates = get_all_certificate_requests(db)
    db.close()

    return templates.TemplateResponse(
        request=request,
        name="certificates.html",
        context={
            "request": request,
            "certificates": certificates,
        },
    )


# ----------------------------
# Upload Certificate Page
# ----------------------------
@router.get("/upload-certificate", response_class=HTMLResponse)
async def upload_certificate_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="upload_certificate.html",
        context={
            "request": request,
        },
    )


# ----------------------------
# Download CSR
# ----------------------------
@router.get("/download/csr/{certificate_id}")
def download_csr(certificate_id: int):

    db = SessionLocal()
    certificate = get_certificate_by_id(db, certificate_id)
    db.close()

    if not certificate:
        return {"error": "Certificate not found"}

    return FileResponse(
        path=certificate.csr_path,
        media_type="application/octet-stream",
        filename=os.path.basename(certificate.csr_path),
    )


# ----------------------------
# Download Private Key
# ----------------------------
@router.get("/download/key/{certificate_id}")
def download_key(certificate_id: int):

    db = SessionLocal()
    certificate = get_certificate_by_id(db, certificate_id)
    db.close()

    if not certificate:
        return {"error": "Certificate not found"}

    return FileResponse(
        path=certificate.key_path,
        media_type="application/octet-stream",
        filename=os.path.basename(certificate.key_path),
    )
# ----------------------------
# Generate Self-Signed Certificate
# ----------------------------
@router.get("/generate-self-signed/{certificate_id}")
def generate_self_signed(certificate_id: int):

    db = SessionLocal()

    certificate = get_certificate_by_id(db, certificate_id)

    if not certificate:
        db.close()
        return {"error": "Certificate not found"}

    certificate_path = generate_self_signed_certificate(
        certificate.key_path,
        certificate.common_name,
    )

    update_certificate_file(
        db=db,
        certificate_id=certificate_id,
        certificate_path=certificate_path,
    )

    db.close()

    return RedirectResponse(
        url="/certificates",
        status_code=303,
    )