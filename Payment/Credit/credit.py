from Payment.payment import Payment
from Product.product import Product

class Credit(Payment):
    """
    A class representing a credit card payment.
    """
    def process_payment(self, product: Product):
        """
        Process a credit card payment.

        Args:
            product (Product): The product being purchased.
        """
        cvv = input("Enter your card CVV: ")
        while not (cvv.isdigit() and len(cvv) == 3):
            cvv = input("Invalid CVV. Please enter the 3-digit CVV from your card: ")
        print(f"The product: {product.name} has been purchased. Total price is: {product.price}")
