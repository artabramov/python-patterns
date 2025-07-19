"""
Наблюдатель (Observer) - паттерн поведения объектов

Определяет зависимость один-ко-многим между объектами таким образом,
что при изменении состояния одного объекта все зависящие от него
объекты оповещаются и могут соответствующим образом отреагировать.
"""


class Observable:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class Observer:
    def update(self, state):
        raise NotImplementedError


class ObserverA(Observer):
    def update(self, state):
        print("Наблюдатель A:", state)


class ObserverB(Observer):
    def update(self, state):
        print("Наблюдатель B:", state)


if __name__ == "__main__":
    observer_a = ObserverA()
    observer_b = ObserverB()

    subject = Observable()
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.state = 1
    subject.detach(observer_b)
    subject.state = 2
    subject.state = 3
