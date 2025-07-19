"""
Entity Manager — архитектурный паттерн

Паттерн централизует управление жизненным циклом объектов. Один
универсальный менеджер работает с разными типами сущностей через общий
интерфейс — загрузка, сохранение, удаление, отслеживание изменений.
"""


class User:
    def __init__(self, name):
        self.name = name


class EntityManager:
    def __init__(self):
        self._storage = []

    def persist(self, entity):
        print(f"Сохраняем '{entity.name}' в хранилище")
        self._storage.append(entity)

    def remove(self, entity):
        print(f"Удаляем '{entity.name}' из хранилища")
        self._storage.remove(entity)


if __name__ == "__main__":
    manager = EntityManager()

    user1 = User("Алиса")
    user2 = User("Боб")

    manager.persist(user1)
    manager.persist(user2)

    manager.remove(user1)
