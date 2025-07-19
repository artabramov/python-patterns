"""
Data Mapper — архитектурный паттерн

Паттерн разделяет бизнес-логику и слой доступа к данным. Для каждой
сущности создаётся отдельный маппер, который отвечает за преобразование
между объектами и базой данных.
"""


class User:
    def __init__(self, id=None, name=""):
        self.id = id
        self.name = name

class UserMapper:
    def __init__(self):
        self._db = {}  # имитация БД

    def insert(self, user):
        user.id = len(self._db) + 1
        self._db[user.id] = user
        print(f"User '{user.name}' сохранён с id={user.id}")

    def find(self, user_id):
        user = self._db.get(user_id)
        if user:
            print(f"Найден пользователь: {user.name}")
        return user

    def delete(self, user):
        if user.id in self._db:
            del self._db[user.id]
            print(f"Пользователь '{user.name}' удалён")


if __name__ == "__main__":
    mapper = UserMapper()

    user = User(name="Алиса")
    mapper.insert(user)

    found = mapper.find(user.id)
    mapper.delete(user)
