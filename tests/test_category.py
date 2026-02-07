from src.category import Category
from src.product import Product


def test_category_str():
    products = [
        Product("Телефон", 50000, 10),
        Product("Ноутбук", 100000, 5)
    ]
    category = Category("Электроника", products)
    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_category_products_getter():
    products = [
        Product("Телефон", 50000, 10),
        Product("Ноутбук", 100000, 5)
    ]
    category = Category("Электроника", products)
    expected = "Телефон, 50000 руб. Остаток: 10 шт.\nНоутбук, 100000 руб. Остаток: 5 шт."
    assert category.products == expected
