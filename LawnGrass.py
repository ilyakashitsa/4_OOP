from product import Product


class LawnGrass(Product):
    """
    Класс, представляющий газонную траву.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country_of_origin: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """
        Возвращает строковое представление газонной травы.
        """
        return f"{self.name}, {self.get_price()} руб. Остаток: {self.quantity} шт. " \
               f"Характеристики: {self.country_of_origin}, {self.germination_period}, {self.color}"
