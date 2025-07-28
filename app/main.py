from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="KPA Form API", version="1.0")
app.include_router(router)
