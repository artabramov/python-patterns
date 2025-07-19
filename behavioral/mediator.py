"""
Медиатор (Mediator) — паттерн поведения объектов

Уменьшает прямые связи между объектами, заставляя их общаться через
специальный объект-посредник. Он содержит логику для координации их
поведения и предотвращает непосредственные ссылки этих объектов друг
на друга. Это снижает связанность (loose coupling) и упрощает
управление сложными действиями.

Паттерн особенно полезен в пользовательских интерфейсах, где множество
компонентов должны взаимодействовать друг с другом.
"""


class Mediator:
    """
    Определяет методы для взаимодействия компонентов друг с другом.
    Знает, какие компоненты существуют, и как они должны реагировать
    на действия друг друга.
    """
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
        c1.set_mediator(self)
        c2.set_mediator(self)

    def notify(self, sender, event):
        """
        Получает сообщения от компонентов и определяет,
        как на них должны реагировать другие компоненты.
        """
        if sender == self.c1 and event == "action1":
            self.c2.react()
        elif sender == self.c2 and event == "action2":
            self.c1.react()


class BaseComponent:
    """
    Компоненты должны знать о медиаторе, чтобы отправлять
    ему уведомления, но не должны знать друг о друге.
    """
    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator):
        self._mediator = mediator


class Component1(BaseComponent):
    def do_action(self):
        self._mediator.notify(self, "action1")

    def react(self):
        print("C1: реагирую на C2")


class Component2(BaseComponent):
    def do_action(self):
        self._mediator.notify(self, "action2")

    def react(self):
        print("C2: реагирую на C1")


if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = Mediator(c1, c2)

    c1.do_action()
    c2.do_action()
