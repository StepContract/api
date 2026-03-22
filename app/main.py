from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
)
