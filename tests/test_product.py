import pytest
from src.product import Product


def test_product_initialization():
    product = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str():
    product = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
    assert str(product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_addition():
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
    result = product1 + product2
    assert result == (180000.0 * 5) + (210000.0 * 8)


def test_product_addition_type_error():
    product = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )
    with pytest.raises(TypeError):
        _ = product + 100
