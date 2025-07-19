"""
Цепочка обязанностей (Chain of Responsibility) — паттерн поведения
объектов.

Позволяет передавать запрос последовательно по цепочке обработчиков,
пока один из них не обработает его. Исключает жёсткую привязку
отправителя запроса к получателю, делая систему гибкой и расширяемой.
Каждый обработчик сам решает — обработать запрос или передать дальше.
Паттерн подходит, когда получатель заранее неизвестен или их может быть
несколько.

Применяется в маршрутизации, фильтрации, обработке событий, middleware.
"""


class BaseHandler:
    def handle(self, code):
        raise NotImplementedError


class Http404Handler(BaseHandler):
    def handle(self, code):
        if code == 404:
            return "Not found"


class Http500Handler(BaseHandler):
    def handle(self, code):
        if code == 500:
            return "Server error"


class Client:
    def __init__(self, *handlers):
        self._handlers = handlers

    def process(self, code):
        for handler in self._handlers:
            msg = handler.handle(code)
            if msg:
                print (code, msg)
                break
        else:
            print(code, "Not processed")


if __name__ == "__main__":
    client = Client(Http404Handler(), Http500Handler())
    client.process(404)
    client.process(500)
    client.process(418)
