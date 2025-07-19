# coding: utf-8

"""
Строитель (Builder) - паттерн, порождающий объекты

Отделяет конструирование сложного объекта от его представления, позволяя
использовать один и тот же процесс создания для разных объектов. От
абстрактной фабрики отличается тем, что делает акцент на пошаговом
конструировании объекта. Строитель возвращает объект на последнем шаге,
тогда как абстрактная фабрика возвращает объект немедленно.
"""


class Burger:
    def __init__(self):
        self.ingredients = []

    def add(self, ingredient):
        self.ingredients.append(ingredient)

    def show(self):
        print("Бутерброд:", ", ".join(self.ingredients))


class SandwichBuilder:
    def __init__(self):
        self.burger = Burger()

    def add_toast(self):
        self.burger.add("тост")
        return self

    def add_ham(self):
        self.burger.add("ветчина")
        return self

    def add_cheese(self):
        self.burger.add("сыр")
        return self

    def build(self):
        return self.burger


if __name__ == "__main__":
    builder = SandwichBuilder()
    sandwich = builder.add_toast().add_ham().add_cheese().build()
    sandwich.show()
