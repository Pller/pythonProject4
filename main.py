from src.product import Product
from src.category import Category


def main():
    # Пример использования
    phone = Product("iPhone 15", 99999, 25)
    laptop = Product("MacBook Pro", 199999, 15)

    print("Продукты:")
    print(phone)
    print(laptop)

    print(f"\nСуммарная стоимость товаров: {phone + laptop} руб.")

    # Категория
    electronics = Category("Электроника", [phone, laptop])
    print(f"\n{electronics}")
    print("\nСписок товаров в категории:")
    print(electronics.products)


if __name__ == "__main__":
    main()
