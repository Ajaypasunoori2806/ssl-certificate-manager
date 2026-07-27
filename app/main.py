from fastapi import Form
from app.services.certificate_service import (
    generate_key_and_csr,
    save_private_key,
    save_csr,
)
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="SSL Certificate Manager",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request},
    )


@app.get("/create-request", response_class=HTMLResponse)
async def create_request(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="create_request.html",
        context={"request": request},
    )


# 👇 Add this entire block below the create_request() function
@app.post("/generate-csr")
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

    return {
        "message": "CSR generated successfully!",
        "private_key": key_file,
        "csr": csr_file,
    }