"""
Черная доска (Blackboard) — архитектурный паттерн

Обеспечивает централизованное хранилище знаний (доску), к которому
имеют доступ разные модули (источники знаний). Каждый модуль наблюдает
за доской и при определённых условиях добавляет новую информацию. Все
уведомления происходят автоматически при каждом обновлении данных.

Часто используется в системах с высокой неопределённостью и несколькими
независимыми экспертами — например, в ИИ, экспертных системах, системах
распознавания.
"""


class Blackboard:
    def __init__(self):
        self.data = {}
        self.subscribers = []

    def subscribe(self, module):
        self.subscribers.append(module)

    def update(self, key, value):
        self.data[key] = value
        for subscriber in self.subscribers:
            subscriber.notify(self)


class KnowledgeSource:
    def notify(self, blackboard):
        raise NotImplementedError


class Analyzer(KnowledgeSource):
    def notify(self, blackboard):
        if "input" in blackboard.data and "analysis" not in blackboard.data:
            text = blackboard.data["input"]
            blackboard.update("analysis", f"Анализ: {text.upper()}")


class DecisionMaker(KnowledgeSource):
    def notify(self, blackboard):
        if "analysis" in blackboard.data and "decision" not in blackboard.data:
            result = blackboard.data["analysis"]
            blackboard.update("decision", f"Решение по '{result}'")


if __name__ == "__main__":
    blackboard = Blackboard()
    blackboard.subscribe(Analyzer())
    blackboard.subscribe(DecisionMaker())

    blackboard.update("input", "сигнал от датчика")

    print("Содержимое доски:")
    for key, value in blackboard.data.items():
        print(f"{key}: {value}")
