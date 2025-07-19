"""
Мост (Bridge) - паттерн, структурирующий объекты

Отделяет абстракцию от её реализации, позволяя изменять их независимо.
Используется для разделения иерархий интерфейсов и реализаций.
"""


class TV:
    def tune_channel(self, channel):
        raise NotImplementedError


class SonyTV(TV):
    def tune_channel(self, channel):
        print('Sony TV: выбран %d канал' % channel)


class SharpTV(TV):
    def tune_channel(self, channel):
        print('Sharp TV: выбран %d канал' % channel)


class RemoteControl:
    def __init__(self, tv):
        self._tv = tv

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class SonyRemoteControl(RemoteControl):
    def __init__(self):
        super().__init__(SonyTV())
        self._channel = 0

    def tune_channel(self, channel):
        super().tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)


if __name__ == "__main__":
    remote_control = SonyRemoteControl()
    remote_control.tune_channel(5)
    remote_control.next_channel()
