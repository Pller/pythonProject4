import pytest
from src.product import Product


def test_product_str():
    product = Product("Телефон", 50000, 10, "Смартфон")
    assert str(product) == "Телефон, 50000 руб. Остаток: 10 шт."


def test_product_addition():
    product1 = Product("Ноутбук", 100000, 5, "Игровой ноутбук")
    product2 = Product("Планшет", 30000, 8, "Планшет для рисования")
    result = product1 + product2
    assert result == (100000 * 5) + (30000 * 8)


def test_product_addition_type_error():
    product = Product("Телефон", 50000, 10, "Телефон")
    with pytest.raises(TypeError):
        _ = product + 100


def test_product_with_description():
    product = Product("Мышь", 2500, 50, "Беспроводная мышь")
    assert product.description == "Беспроводная мышь"


def test_product_without_description():
    product = Product("Клавиатура", 5000, 30)
    assert product.description == ""
