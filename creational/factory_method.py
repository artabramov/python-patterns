"""
Фабричный метод (Factory Method) - паттерн, порождающий классы

Определяет интерфейс для создания объекта, но позволяет подклассам
решать, какой класс инстанцировать.
"""


class Document:
    def show(self):
        raise NotImplementedError


class PDFDocument(Document):
    def show(self):
        print("PDF document format")


class RTFDocument(Document):
    def show(self):
        print("RTF document format")


class Application:
    def create_document(self, doc_type):
        raise NotImplementedError


class MyApplication(Application):
    def create_document(self, doc_type):
        mapping = {
            "pdf": PDFDocument,
            "rtf": RTFDocument,
        }
        return mapping.get(doc_type, Document)()


if __name__ == "__main__":
    app = MyApplication()
    app.create_document("pdf").show()
    app.create_document("rtf").show()
