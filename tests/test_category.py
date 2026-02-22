import pytest
from src.category import Category
from src.product import Product


def test_category_initialization():
    Category.category_count = 0
    Category.product_count = 0

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

    category = Category(
        "Смартфоны",
        ("Смартфоны, как средство не только коммуникации, "
         "но и получения дополнительных функций"),
        [product1, product2]
    )

    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций"
    )
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_str():
    Category.category_count = 0
    Category.product_count = 0

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

    category = Category("Смартфоны", "Описание", [product1, product2])
    assert str(category) == "Смартфоны, количество продуктов: 2 шт."


def test_category_products_property():
    Category.category_count = 0
    Category.product_count = 0

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

    category = Category("Смартфоны", "Описание", [product1, product2])

    expected = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )
    assert category.products == expected


def test_category_count_increment():
    Category.category_count = 0
    Category.product_count = 0

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
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )

    Category("Смартфоны", "Описание", [product1, product2])
    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("Книги", "Описание", [product3])
    assert Category.category_count == 2
    assert Category.product_count == 3
