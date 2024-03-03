class Product:
    """
    Класс, представляющий продукт в магазине.
    """
    total_products = 0  # общее количество продуктов
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует новый экземпляр класса Product.

        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продукта в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        Product.total_products += 1

    def get_name(self):
        """
        Возвращает название продукта.
        """
        return self.name

    def get_price(self):
        """
        Возвращает цену продукта.
        """
        return self.price

    def get_quantity(self):
        """
        Возвращает количество продуктов в наличии.
        """
        return self.quantity

    def get_description(self):
        """
        Возврощает описание продукта
        """
        return self.description
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
        self.products = []  # список продуктов в категории
        Category.total_categories += 1
    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию.
        """
        self.products.append(product)
        Category.total_unique_products.add(product.name)

    def remove_product(self, product: Product):
        """
        Удаляет продукт из категории.
        """
        self.products.remove(product)
        if product.name in Category.total_unique_products:
            Category.total_unique_products.remove(product.name)
    def get_products(self):
        """
        Возвращает список продуктов в категории.
        """
        return self.products
