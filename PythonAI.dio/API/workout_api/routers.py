from fastapi import APIRouter
from workout_api.atletas.controller import router as atleta
from workout_api.categorias.controller import router as categoria
from workout_api.centros_treinamento import router as centro_treinamento

api_router=APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centros_treinamento', tags=['centros_treinamento'])