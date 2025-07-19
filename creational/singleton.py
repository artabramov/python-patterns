"""
Одиночка (Singleton) - паттерн, порождающий объекты

Гарантирует, что у класса есть только один экземпляр, и предоставляет
глобальную точку доступа к нему.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def operation(self):
        pass


if __name__ == "__main__":
    a = Singleton()
    b = Singleton()

    print("a is b:", a is b)
    a.operation()
    b.operation()
