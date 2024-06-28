from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='Centro rei', max_lenght=20)]
    enredeco: Annotated[str, Field(description='Nome do centro de treinamento', example='Rua dos girassois', max_lenght=60)]
    proprietário: Annotated[str, Field(description='Nome do centro de treinamento', example='André', max_lenght=30)]
    
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]    