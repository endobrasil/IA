from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Andre', max_lenght=50)]