from src.product import Product


class Category:
    def __init__(self, name, products):
        self.name = name
        self.__products = products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)
