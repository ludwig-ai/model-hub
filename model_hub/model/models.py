from fastapi import APIRouter, Depends

from model_hub.db import get_database
from model_hub.db.database_manager import DatabaseManager
from model_hub.db.models import Model

router = APIRouter()


@router.get("/")
async def all_models(db: DatabaseManager = Depends(get_database)):
    models = await db.get_models()
    return models


@router.get("/one/model")
async def one_model(model_url: str,
                    db: DatabaseManager = Depends(get_database)):
    model = await db.get_model(model_url=model_url)
    return model


@router.put("/{model_url}")
async def update_model(model_url: str,
                       model: Model,
                       db: DatabaseManager = Depends(get_database)):
    post = await db.update_model(model=model, model_url=model_url)
    return post


@router.post("/", status_code=201)
async def add_model(post_response: Model,
                    db: DatabaseManager = Depends(get_database)):
    post = await db.add_model(post_response)
    return post


@router.delete("/{model_url}")
async def delete_model(model_url: str,
                       db: DatabaseManager = Depends(get_database)):
    await db.delete_model(model_url=model_url)
