from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """
    Абстрактный класс, представляющий общий функционал для всех продуктов.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует новый экземпляр класса AbstractProduct.

        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продукта в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_additional_info(self):
        """
        Абстрактный метод, возвращающий дополнительную информацию о продукте.
        Каждый подкласс должен реализовать этот метод.
        """
        pass
