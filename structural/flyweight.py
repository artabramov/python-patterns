"""
Приспособленец (Flyweight) - паттерн, структурирующий объекты

Позволяет эффективно поддерживать множество мелких объектов, разделяя
повторяющееся внутреннее состояние. Это уменьшает потребление памяти.
"""


class Glyph:
    def __init__(self, symbol):
        self.symbol = symbol

    def draw(self, position):
        print(f"Рисуем '{self.symbol}' в позиции {position}")


class GlyphFactory:
    def __init__(self):
        self._glyphs = {}

    def get_glyph(self, symbol):
        if symbol not in self._glyphs:
            self._glyphs[symbol] = Glyph(symbol)
        return self._glyphs[symbol]


if __name__ == "__main__":
    factory = GlyphFactory()
    text = "hello"

    for i, char in enumerate(text):
        glyph = factory.get_glyph(char)
        glyph.draw(i)
