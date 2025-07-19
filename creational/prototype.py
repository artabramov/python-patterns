"""
Прототип - паттерн, порождающий объекты

Позволяет копировать объекты, не вдаваясь в подробности их реализации.
Особенно полезен, когда создание новых экземпляров ресурсоёмко или
требует сложной настройки.
"""

import copy


class Shape:
    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print("Круг радиусом", self.radius)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def draw(self):
        print("Квадрат со стороной", self.side)


if __name__ == "__main__":
    circle1 = Circle(5)
    square1 = Square(10)

    circle2 = circle1.clone()
    square2 = square1.clone()

    circle1.draw()
    circle2.draw()
    square1.draw()
    square2.draw()
