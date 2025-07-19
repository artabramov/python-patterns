"""
Стратегия (Strategy) - паттерн поведения объектов

Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их
взаимозаменяемыми. Позволяет изменять поведение программы без изменения
клиентов, которые используют эти алгоритмы.
"""


class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self._card_number = card_number
        self._cvv = cvv

    def pay(self, amount):
        print(f"Pay {amount:.2f} from card ****{self._card_number[-4:]}")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self._email = email

    def pay(self, amount):
        print(f"Pay {amount:.2f} from PayPal {self._email}")


class ShoppingCart:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def checkout(self, amount):
        self._payment_strategy.pay(amount)


if __name__ == "__main__":
    credit_card_details = CreditCardPayment("1234-5678-9012-3456", "123")
    cart1 = ShoppingCart(credit_card_details)
    cart1.checkout(90)

    paypal_account = PayPalPayment("user@example.com")
    cart2 = ShoppingCart(paypal_account)
    cart2.checkout(25)

    initial_paypal = PayPalPayment("another_user@example.com")
    cart3 = ShoppingCart(initial_paypal)
    cart3.checkout(75)

    new_credit_card_details = CreditCardPayment("9876-5432-1098-7654", "456")
    cart3.set_payment_strategy(new_credit_card_details)
    cart3.checkout(50)
