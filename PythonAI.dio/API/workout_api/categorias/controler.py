from uuid import uuid4
from fastapi import APIRouter, Body,status
from workout_api.contrib.dependencies import DatabaseDependency
from workout_api.categorias.schemas import CategoriaIn, CategoriaOut
from workout_api.categorias.models import CategoriaModel
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

outer=APIRouter()

@router.post(path='/', 
             summary='Criar novo Categoria',
             status_code=status.HTTP_201_CREATED,
             response_model=CategoriaOut,
             )
async def post(db_session: DatabaseDependency, 
               categoria_in: CategoriaIn=Body(...)
               )-> CategoriaOut:    
    categoria_out=CategoriaOut(id=uuid4(),**categoria_in)
    categoria_model=CategoriaModel()
    
    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out

@router.get(path='/', 
             summary='Consultar todas as Categorias',
             status_code=status.HTTP_200_CREATED,
             response_model=list(CategoriaOut),
             )
async def query(
    db_session: DatabaseDependency,
)->list[CategoriaOut]:
    categorias: list[CategoriaOut]=[await db_session.execute(select(CategoriaModel))].scalars().all()
    return categorias

    

@router.get(path='/(id)', 
             summary='Consultar Categorias pelo id',
             status_code=status.HTTP_200_CREATED,
             response_model=list(CategoriaOut),
             )
async def query(
    id: UUID4, db_session: DatabaseDependency,
)->CategoriaOut:
    categoria: list[CategoriaOut]=[await db_session.execute(select(CategoriaModel).filter_by(id=id))
                                   ].scalars().first()
    
    if not categoria:
        raise HTTPException(Status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Categoria não encontrada no id: {id}")
    return categoria
