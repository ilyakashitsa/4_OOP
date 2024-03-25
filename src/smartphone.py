from src.product import Product
from src.abstract_product import AbstractProduct
from src.creation_logger_mixin import ObjectCreationLoggerMixin


class Smartphone(Product, AbstractProduct, ObjectCreationLoggerMixin):
    """
    Класс, представляющий смартфон в магазине.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 capacity: str, model: str, internal_memory: int, color: str):
        """
        Инициализирует новый экземпляр класса Smartphone.
        """
        super().__init__(name, description, price, quantity)
        self.capacity = capacity
        self.model = model
        self.internal_memory = internal_memory
        self.color = color

    def get_additional_info(self):
        """
        Возвращает дополнительную информацию о смартфоне.
        """
        return f"Характеристики: {self.capacity}, {self.model}, {self.internal_memory}GB, {self.color}"
