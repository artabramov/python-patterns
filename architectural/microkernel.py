"""
Микроядро (Microkernel) — архитектурный паттерн

Ядро определяет минимальную функциональность системы. Дополнительные
возможности реализуются как плагины, взаимодействующие с ядром.
"""

class MicrokernelEditor:
    def __init__(self):
        self.text = ""
        self.plugins = []

    def load_text(self, text):
        self.text = text
        print(f"[Core] Текст загружен: {self.text}")

    def register_plugin(self, plugin):
        self.plugins.append(plugin)
        print(f"[Core] Зарегистрирован плагин: {plugin.__class__.__name__}")

    def run_plugins(self):
        for plugin in self.plugins:
            print(f"[Core] Запуск плагина: {plugin.__class__.__name__}")
            plugin.run(self)


class WordCountPlugin:
    def run(self, editor):
        words = len(editor.text.split())
        print(f"[WordCountPlugin] Количество слов: {words}")


class UppercasePlugin:
    def run(self, editor):
        editor.text = editor.text.upper()
        print(f"[UppercasePlugin] Текст преобразован в ВЕРХНИЙ РЕГИСТР.")


if __name__ == "__main__":
    editor = MicrokernelEditor()
    editor.load_text("Привет из микроядра!")

    editor.register_plugin(WordCountPlugin())
    editor.register_plugin(UppercasePlugin())

    editor.run_plugins()
    print(f"[Core] Финальный текст: {editor.text}")
