"""
Состояние (State) - паттерн поведения объектов

Позволяет объекту менять своё поведение при изменении его внутреннего
состояния. При этом создается впечатление, что объект меняет свой класс.
"""


class DoorState:
    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class ClosedState(DoorState):
    def __init__(self, door):
        self._door = door

    def open(self):
        new_state = OpenState(self._door)
        self._door.set_state(new_state)
        print("Открыть: закрыто > открыто")

    def close(self):
        print("Закрыть: уже закрыто")


class OpenState(DoorState):
    def __init__(self, door):
        self._door = door

    def open(self):
        print("Открыть: уже открыто")

    def close(self):
        new_state = ClosedState(self._door)
        self._door.set_state(new_state)
        print("Закрыть: открыто > закрыто")


class DoorContext:
    def __init__(self):
        self._state = ClosedState(self)

    def set_state(self, state: DoorState):
        self._state = state

    def open(self):
        self._state.open()

    def close(self):
        self._state.close()


if __name__ == "__main__":
    door = DoorContext()
    door.open()
    door.open()
    door.close()
    door.close()
    door.open()
