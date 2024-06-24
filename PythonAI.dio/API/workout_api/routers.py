from fastapi import APIRouter
from workout_api.atletas.controller import router as atleta
from workout_api.categorias.controler import router as categoria

api_router=APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])