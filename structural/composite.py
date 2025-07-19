"""
Компоновщик (Composite) - паттерн, структурирующий объекты. 

Позволяет объединять объекты в древовидную структуру и работать с ними
одинаково — как с единичными объектами, так и с группами объектов.
Паттерн используется, когда объекты могут быть как простыми, так и
составными, а клиентский код должен одинаково взаимодействовать с
обоими типами.
"""


class Graphic:
    def draw(self):
        raise NotImplementedError


class Circle(Graphic):
    def draw(self):
        print("Рисуем круг")


class Square(Graphic):
    def draw(self):
        print("Рисуем квадрат")


class GraphicGroup(Graphic):
    def __init__(self):
        self._children = []

    def add(self, graphic: Graphic):
        self._children.append(graphic)

    def draw(self):
        for child in self._children:
            child.draw()


if __name__ == "__main__":
    simple1 = Circle()
    simple2 = Square()
    group = GraphicGroup()
    group.add(simple1)
    group.add(simple2)

    print("Рисуем группу:")
    group.draw()
