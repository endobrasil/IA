class pydantic import Field
from store.schemas.base import BaseSchemaMixin

class ProductIn(BaseSchemaMixin):
    name: str=Field(...,description="Nome do produto")
    quantity: str=Field(...,description="quantidde do produto")
    price: str=Field(...,description="preço do produto")
    status: str=Field(...,description="status do produto")
    