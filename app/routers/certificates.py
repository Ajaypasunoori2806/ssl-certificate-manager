from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.database.database import SessionLocal
from app.database.crud import (
    create_certificate_request,
    get_all_certificate_requests,
)
from app.services.certificate_service import (
    generate_key_and_csr,
    save_private_key,
    save_csr,
)

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


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

    return {
        "message": "CSR generated successfully!",
        "private_key": key_file,
        "csr": csr_file,
    }


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