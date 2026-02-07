import pytest
from src.product import Product


def test_product_str():
    product = Product("Телефон", 50000, 10)
    assert str(product) == "Телефон, 50000 руб. Остаток: 10 шт."


def test_product_addition():
    product1 = Product("Ноутбук", 100000, 5)
    product2 = Product("Планшет", 30000, 8)
    result = product1 + product2
    assert result == (100000 * 5) + (30000 * 8)


def test_product_addition_type_error():
    product = Product("Телефон", 50000, 10)
    with pytest.raises(TypeError):
        _ = product + 100
