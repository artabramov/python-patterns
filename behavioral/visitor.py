"""
Постетитель (Visitor) - паттерн поведения объектов

Определяет операцию, применяемую к каждому объекту в структуре, при этом
отделяя саму операцию от классов этих объектов. Это позволяет добавлять
новые действия без изменения исходных классов элементов структуры.
"""


class Shape:
    def accept(self, visitor):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def accept(self, visitor):
        visitor.visit_square(self)


class ShapeVisitor:
    def visit_circle(self, circle):
        raise NotImplementedError

    def visit_square(self, square):
        raise NotImplementedError


class DrawVisitor(ShapeVisitor):
    def visit_circle(self, circle: Circle):
        print("Рисуем круг радиусом", circle.radius)

    def visit_square(self, square: Square):
        print("Рисуем квадрат со стороной", square.side)


if __name__ == "__main__":
    shapes = [Circle(5), Square(10)]
    visitor = DrawVisitor()
    for shape in shapes:
        shape.accept(visitor)
