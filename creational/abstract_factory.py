"""
Абстрактная фабрика (Abstract factory) - паттерн, порождающий объекты

Предоставляет интерфейс для создания семейств взаимосвязанных или
взаимозависимых объектов, не привязываясь к конкретным классам.

Классы абстрактной фабрики часто реализуются фабричными методами,
но могут быть реализованы и с помощью паттерна прототип.
"""


class AbstractFactory:
    def create_drink(self):
        raise NotImplementedError

    def create_food(self):
        raise NotImplementedError


class Drink:
    def __init__(self, name):
        self.name = name


class Food:
    def __init__(self, name):
        self.name = name


class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Coca-cola')

    def create_food(self):
        return Food('Hamburger')


class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Pepsi')

    def create_food(self):
        return Food('Cheeseburger')


def get_factory(ident):
    if ident == 0:
        return ConcreteFactory1()
    elif ident == 1:
        return ConcreteFactory2()


if __name__ == "__main__":
    factory = get_factory(1)
    drink = factory.create_drink()
    food = factory.create_food()

    print(drink.name, food.name)
