import uvicorn
from fastapi import FastAPI

from model_hub.config import get_config
from model_hub.db import db
from model_hub.model import models

model_hub = FastAPI(title="Async FastAPI For ModelHub")

model_hub.include_router(models.router, prefix="/api/models")


@model_hub.on_event("startup")
async def startup():
    config = get_config()
    await db.connect_to_database(path=config.db_path)


@model_hub.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


if __name__ == "__main__":
    uvicorn.run(model_hub, host="0.0.0.0", port=8000)
