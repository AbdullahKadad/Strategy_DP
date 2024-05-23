from Payment.payment import Payment
from Product.product import Product

class Cash(Payment):
    """
    A class representing a cash payment.
    """
    def process_payment(self, product : Product):
        """
        Process a cash payment.
        """
        print(f"The product : {product.name} has been purchased, total price is : {product.price}")
