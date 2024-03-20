from product import Product
from abstract_product import AbstractProduct
from creation_logger_mixin import ObjectCreationLoggerMixin


class LawnGrass(Product, AbstractProduct, ObjectCreationLoggerMixin):
    """
    Класс, представляющий газонную траву в магазине.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country_of_origin: str, germination_period: str, color: str):
        """
        Инициализирует новый экземпляр класса LawnGrass.
        """
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def get_additional_info(self):
        """
        Возвращает дополнительную информацию о газонной траве.
        """
        return f"Характеристики: {self.country_of_origin}, {self.germination_period}, {self.color}"
