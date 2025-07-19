"""
Фасад (Facade) - паттерн, структурирующий объекты

Предоставляет упрощённый интерфейс к сложной системе. Вместо того чтобы
взаимодействовать с множеством классов напрямую, клиент работает с
одним объектом-фасадом, который инкапсулирует всю внутреннюю логику.
"""


class CPU:
    def execute(self):
        print("CPU: execute command")


class Memory:
    def load(self, address, data):
        print(f"Memory: load {data} at {address}")


class HardDrive:
    def read(self, sector):
        print(f"HardDrive: read sector {sector}")
        return "boot data"


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hdd = HardDrive()

    def start(self):
        data = self.hdd.read(sector=1)
        self.memory.load(address=0, data=data)
        self.cpu.execute()


if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start()
