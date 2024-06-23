from fastapi import APIRouter, Body,status
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.atletas.schemas import AtletaIn
router=APIRouter()

@router.post(path='/', 
             summary='Criar novo atleta',
             status_code=status.HTTP_201_CREATED
             )
async def post(db_session: DatabaseDependency, 
               atleta_in: AtletaIn=Body(...)):
    pass