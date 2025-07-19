"""
Команда (Command) — паттерн поведения объектов.

Инкапсулирует запрос как объект, полностью отделяя инициатора действия
от его исполнителя. Это делает систему гибкой, расширяемой и управляемой.
Позволяет реализовать отмену, повтор, логирование, макрокоманды и
динамическое изменение поведения.

Применяется в интерфейсах, обработке событий и автоматизации.
"""


class Light:
    def turn_on(self):
        print("Light on")

    def turn_off(self):
        print("Light off")


class BaseCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        raise NotImplementedError


class TurnOn(BaseCommand):
    def execute(self):
        self.light.turn_on()


class TurnOff(BaseCommand):
    def execute(self):
        self.light.turn_off()


class Toolbar:
    def __init__(self, turn_on, turn_off):
        self.turn_on = turn_on
        self.turn_off = turn_off

    def light_on(self):
        self.turn_on.execute()

    def light_off(self):
        self.turn_off.execute()


if __name__ == "__main__":
    light = Light()
    toolbar = Toolbar(TurnOn(light), TurnOff(light))
    toolbar.light_on()
    toolbar.light_off()
