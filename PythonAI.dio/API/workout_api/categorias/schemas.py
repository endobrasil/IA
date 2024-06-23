from typing import Annotated
from pydantic import Field,UUID4
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Andre', max_lenght=50)]

class CategoriaIn(Categoria):
    pass

class CategoriaOut(Categoria):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]