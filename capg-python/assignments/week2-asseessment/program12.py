class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using a default payment method.")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using Credit Card.")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using PayPal.")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using Bitcoin.")


amount = 100.50

payment = Payment()
payment.process_payment(amount)

credit_card_payment = CreditCardPayment()
credit_card_payment.process_payment(amount)

paypal_payment = PayPalPayment()
paypal_payment.process_payment(amount)

bitcoin_payment = BitcoinPayment()
bitcoin_payment.process_payment(amount)