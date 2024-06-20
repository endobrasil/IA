from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Andre', max_lenght=50)]
    cpf: Annotated[str, Field(description='cpf do atleta', example='12376523491', max_lenght=11)]
    idade: Annotated[int, Field(description='idade do atleta', example=12)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=45.0)]
    altura: Annotated[PositiveFloat, Field(description='alturae do atleta', example=1.72)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='F', max_lenght=1)]

