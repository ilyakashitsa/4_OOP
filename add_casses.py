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
        self.__price = price
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
        return self.__price

    def set_price(self, new_price):
        """
        Устанавливает новую цену продукта.
        """
        if new_price <= 0:
            print("Цена введена некорректно")
        else:
            self.__price = new_price

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

    @staticmethod
    def create_product(name: str, description: str, price: float, quantity: int, products_list: list):
        """
        Создает новый продукт. Если товар с таким именем уже существует, увеличивает количество и проверяет цену.
        """
        for product in products_list:
            if product.name == name:
                print("Товар уже существует. Увеличиваем количество и проверяем цену.")
                product.quantity += quantity
                if price > product.get_price():
                    product.set_price(price)
                return product

        # Если товар не найден, создает новый
        return Product(name, description, price, quantity)


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

    def get_products(self):
        """
        Возвращает список продуктов в категории.
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
