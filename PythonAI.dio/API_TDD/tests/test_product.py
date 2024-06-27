from uuid import UUID
import pytest
from store.schemas.factories import product_data
from store.schemas.product import ProductIn

def test_chemas_validated():
    data=product_data
    product=ProductIn(data)

    assert product.name=="Iphones"
    assert isinstance(product.id,UUID)

    def test_schemas_return_raise():
        data={'name':'Iphones', 'quantity':10,'price':8.500,'status':True}
        with pytest.raises(ValidationError) as err:
            ProductIn.model_validate(data)

        assert err.value.errors()[0] == {"enfim... sei lá"}