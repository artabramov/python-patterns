"""
Шаблонный метод (Template method) - паттерн поведения классов

Определяет основу алгоритма и позволяет подклассам переопределить
некоторые шаги этого алгоритма, не изменяя его структуру в целом.
"""


class CocktailMaker:
    def prepare_cocktail(self):
        self.add_ice()
        self.add_alcohol()
        self.add_mixer()

    def add_ice(self):
        print("Насыпаем лед")

    def add_alcohol(self):
        raise NotImplementedError

    def add_mixer(self):
        raise NotImplementedError


class MojitoMaker(CocktailMaker):
    def add_alcohol(self):
        print("Наливаем ром")

    def add_mixer(self):
        print("Добавляем мяту, лайм и содовую")


class MargaritaMaker(CocktailMaker):
    def add_alcohol(self):
        print("Наливаем текилу")

    def add_mixer(self):
        print("Добавляем лаймовый сок и апельсиновый ликёр")


if __name__ == "__main__":
    print("Готовим мохито:")
    mojito = MojitoMaker()
    mojito.prepare_cocktail()

    print("\nГотовим маргариту:")
    margarita = MargaritaMaker()
    margarita.prepare_cocktail()
