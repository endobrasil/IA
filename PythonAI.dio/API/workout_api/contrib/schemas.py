from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from sqlalchemy import DateTime


class BaseSchema(BaseModel):
    class Config:
        extra='forbid'
        from_attibutes=True

class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[DateTime, Field(description='Data de criação')]
    
