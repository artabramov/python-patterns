"""
Модуль (Module) — структурный паттерн

Инкапсулирует связанный набор функций и данных в единый объект или
пространство имён. Часто реализуется как singleton или namespace.
Позволяет организовать код в виде независимых блоков с чётким API.
"""

class Logger:
    _enabled = True

    @staticmethod
    def enable():
        Logger._enabled = True

    @staticmethod
    def disable():
        Logger._enabled = False

    @staticmethod
    def log(message):
        if Logger._enabled:
            print("[LOG]", message)


if __name__ == "__main__":
    Logger.log("Старт программы")
    Logger.disable()
    Logger.log("Этого не видно")
    Logger.enable()
    Logger.log("Видно снова")
