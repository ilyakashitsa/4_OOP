class ObjectCreationLoggerMixin:
    """
    Миксин для логирования создания объектов.
    """
    def __repr__(self):
        """
        Магический метод, вызываемый при создании объекта.
        Выводит информацию о созданном объекте в консоль.
        """
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attributes})"
