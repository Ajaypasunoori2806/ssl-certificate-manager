from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request},
    )


@router.get("/create-request", response_class=HTMLResponse)
async def create_request(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="create_request.html",
        context={"request": request},
    )