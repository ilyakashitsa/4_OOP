from product import Product


class Smartphone(Product):
    """
    Класс, представляющий смартфон.
    capacity: производительность,
    model: модель,
    internal memory: объем встроенной памяти,
    color: цвет.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 capacity: str, model: str, internal_memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.capacity = capacity
        self.model = model
        self.internal_memory = internal_memory
        self.color = color

    def __str__(self):
        """
        Возвращает строковое представление смартфона.
        """
        return f"{self.name}, {self.get_price()} руб. Остаток: {self.quantity} шт. " \
               f"Характеристики: {self.capacity}, {self.model}, {self.internal_memory}GB, {self.color}"
