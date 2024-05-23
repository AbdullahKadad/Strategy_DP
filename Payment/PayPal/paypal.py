from Payment.payment import Payment
from Product.product import Product

class Paypal(Payment):
    """
    A class representing a PayPal payment.
    """
    def process_payment(self, product: Product):
        """
        Process a PayPal payment.

        Args:
            product (Product): The product being purchased.
        """
        verification_code = "0012"
        print("Verification code:", verification_code)
        code = input("Enter verification code: ")
    
        while code != str(verification_code): 
            code = input("Invalid verification code. Please enter the correct code: ")
        print(f"The product: {product.name} has been purchased. Total price is: {product.price}")

