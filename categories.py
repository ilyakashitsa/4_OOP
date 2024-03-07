from product import Product


class Category:
    """
    Класс, представляющий категорию продуктов в магазине.
    """
    total_categories = 0  # общее количество категорий
    total_unique_products = set()  # общее количество уникальных продуктов

    def __init__(self, name: str, description: str):
        """
        Инициализирует новый экземпляр класса Category.

        name: Название категории.
        description: Описание категории.
        """
        self.name = name
        self.description = description
        self.__products = []  # список продуктов в категории
        Category.total_categories += 1

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию.
        """
        self.__products.append(product)
        Category.total_unique_products.add(product.name)

    def remove_product(self, product: Product):
        """
        Удаляет продукт из категории.
        """
        self.__products.remove(product)
        if product.name in Category.total_unique_products:
            Category.total_unique_products.remove(product.name)

    @property
    def products(self):
        """
        Геттер для списка продуктов в категории.
        """
        return self.__products

    def get_products_info(self):
        """
        Возвращает информацию о продуктах в категории в формате "Продукт, Цена руб. Остаток: количество шт."
        """
        products_info = []
        for product in self.__products:
            products_info.append(
                f"{product.get_name()}, {product.get_price()} руб. Остаток: {product.get_quantity()} шт.")
        return products_info
