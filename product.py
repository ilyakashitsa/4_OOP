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


    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products_list: list):
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
        return cls(name, description, price, quantity)

    def __str__(self):
        """
        Возвращает строковое представление продукта.
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Перегрузка оператора сложения для продуктов.
        Результатом является сумма стоимостей продуктов, умноженных на их количество.
        """
        return (self.__price * self.quantity) + (other.__price * other.quantity)