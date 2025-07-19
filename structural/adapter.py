"""
Адаптер - паттерн, структурирующий классы и объекты

Позволяет объекту с одним интерфейсом работать с другим, несовместимым.
Адаптер действует как переходник между двумя несвязанными классами.
"""


class Target:
    def expected_request(self):
        raise NotImplementedError


class Adaptee:
    def specific_request(self):
        return "исходные данные"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def expected_request(self):
        specific_result = self._adaptee.specific_request()
        return "измененные " + specific_result


if __name__ == "__main__":
    adaptee_instance = Adaptee()
    adapted_object = Adapter(adaptee_instance)
    result = adapted_object.expected_request()
    print(result)
