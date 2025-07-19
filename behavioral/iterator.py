"""
Итератор (Iterator) — паттерн поведения объектов.

Позволяет последовательно обходить элементы коллекции, не раскрывая
внутреннего представления этой коллекции. Выносит логику обхода за
пределы самой структуры данных, обеспечивая единообразный доступ
к элементам.

Упрощает работу с коллекциями, делает код чище и поддерживает
множество способов обхода.

Применяется в структурах данных, генераторах, потоках данных.
"""


class NumberCollection:
    def __init__(self, items):
        self._items = items

    def create_iterator(self):
        return NumberIterator(self)


class NumberIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < len(self._collection._items)

    def next(self):
        item = self._collection._items[self._index]
        self._index += 1
        return item


if __name__ == "__main__":
    collection = NumberCollection([10, 20, 30])
    iterator = collection.create_iterator()

    while iterator.has_next():
        print(iterator.next())
