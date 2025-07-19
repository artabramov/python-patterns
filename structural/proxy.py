"""
Заместитель (Proxy, Surrogate) - паттерн, структурирующий объекты.

Предоставляет суррогат объекта, контролируя доступ к нему. Может
добавлять дополнительную логику — кэширование, ленивую загрузку,
логирование, проверку прав и др.
"""


class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print("Загрузка", self.filename)

    def display(self):
        print("Показ", self.filename)


class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if not self._real_image:
            self._real_image = RealImage(self.filename)
        self._real_image.display()


if __name__ == "__main__":
    image = ImageProxy("photo.png")
    image.display()
    image.display()
