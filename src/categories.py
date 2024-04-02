from src.product import Product


class Category:
    """
    Класс, представляющий категорию продуктов в магазине.
    """
    total_categories = 0  # общее количество категорий
    total_unique_products = set()  # общее количество уникальных продуктов
    Category.total_unique_products_counter = len(Category.total_unique_products) # счетчик уникальных продуктов

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

    def add_product(self, product):
        """
        Добавляет продукт в категорию.

        Проверяет, является ли объект экземпляром класса Product или его подкласса.
        Если объект не является продуктом, вызывается исключение TypeError.
        """
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только экземпляры продукта или его подклассов.")
        if product.get_quantity() == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
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

    def __len__(self):
        """
        Возвращает общее количество продуктов в категории.
        """
        return len(self.__products)

    def __str__(self):
        """
        Возвращает строковое представление категории.
        """
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def calculate_average_price(self):
        """
        Рассчитывает средний ценник всех товаров в категории.

        Возвращает средний ценник или 0, если в категории нет товаров.
        """
        total_price = sum(product.get_price() for product in self.__products)
        try:
            average_price = total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
        return average_price
