"""
Декоратор (Decorator) - паттерн, структурирующий объекты

Позволяет динамически добавлять объектам новую функциональность, не
изменяя их исходный класс. Оборачивает объект в другой объект, который
расширяет его поведение.
"""


class Notifier:
    def send(self, message):
        raise NotImplementedError


class BaseNotifier(Notifier):
    def send(self, message):
        print(message)


class SMSDecorator(Notifier):
    def __init__(self, notifier):
        self._notifier = notifier

    def send(self, message):
        self._notifier.send(message)
        print("SMS:", message)


class EmailDecorator(Notifier):
    def __init__(self, notifier):
        self._notifier = notifier

    def send(self, message):
        self._notifier.send(message)
        print("Email:", message)


if __name__ == "__main__":
    notifier = BaseNotifier()
    notifier = SMSDecorator(notifier)
    notifier = EmailDecorator(notifier)
    notifier.send("Встреча в 18:00")
