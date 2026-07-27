from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.database import Base, engine

from app.routers.dashboard import router as dashboard_router
from app.routers.certificates import router as certificates_router

app = FastAPI(
    title="SSL Certificate Manager",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

Base.metadata.create_all(bind=engine)

app.include_router(dashboard_router)
app.include_router(certificates_router)