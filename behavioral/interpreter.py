"""
Интерпретатор (Interpreter) - паттерн поведения классов.

Определяет представление грамматики заданного языка и описывает его
правила в виде классов. Эти классы позволяют интерпретировать выражения,
написанные на этом языке. Подходит для реализации простых языков, формул,
фильтров и логических выражений.

Применяется в шаблонизаторах, парсерах, скриптах и языках запросов.
"""


class Expression:
    def interpret(self) -> bool:
        raise NotImplementedError


class Literal(Expression):
    def __init__(self, value: bool):
        self.value = value

    def interpret(self) -> bool:
        return bool(self.value)


class Not(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def interpret(self) -> bool:
        return not self.expr.interpret()


class And(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> bool:
        return self.left.interpret() and self.right.interpret()


class Or(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> bool:
        return self.left.interpret() or self.right.interpret()


if __name__ == "__main__":
    # True and (not False)
    expr = And(Literal(1), Not(Literal(0)))
    print(expr.interpret())

    # not (True or False)
    expr2 = Not(Or(Literal(1), Literal(0)))
    print(expr2.interpret())
