from Payment.payment import Payment
from Product.product import Product

class Context:
    """
    A class representing the context in which a payment is processed.
    """
    def __init__(self, payment: Payment):
        """
        Initialize the context with a payment method.

        Args:
            payment (Payment): The payment method to be used.
        """
        self.payment = payment

    def set_payment(self, payment: Payment):
        """
        Set a new payment method.

        Args:
            payment (Payment): The new payment method to be set.
        """
        self.payment = payment

    def execute_payment(self, product: Product):
        """
        Execute the payment process.

        Args:
            product (Product): The product being purchased.

        Returns:
            str: A message indicating the result of the payment process.
        """
        return self.payment.process_payment(product)
