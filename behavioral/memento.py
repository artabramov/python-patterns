"""
Хранитель (Memento) - паттерн поведения объектов

Не нарушая инкапсуляции, фиксирует и выносит за пределы объекта его
внутреннее состояние так, чтобы позже можно было восстановить объект
из этого состояния.
"""


class Memento:
    def __init__(self, color):
        self._color = color

    def get_state(self):
        return self._color


class ColorPicker:
    def __init__(self):
        self._color = "white"

    def set_color(self, color):
        self._color = color
        print("Выбран цвет:", self._color)

    def save(self):
        return Memento(self._color)

    def restore(self, memento):
        self._color = memento.get_state()
        print("Откат к цвету:", self._color)


class History:
    def __init__(self):
        self._stack = []

    def add(self, memento):
        self._stack.append(memento)

    def undo(self):
        if self._stack:
            return self._stack.pop()
        return None


if __name__ == "__main__":
    picker = ColorPicker()
    history = History()

    picker.set_color("red")
    history.add(picker.save())

    picker.set_color("green")
    history.add(picker.save())

    picker.set_color("blue")

    picker.restore(history.undo())
    picker.restore(history.undo())
