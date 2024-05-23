class Product:
    """
    A class to represent a product.

    Attributes:
    -----------
    name : str
        The name of the product.
    price : float
        The price of the product.
    """

    def __init__(self, name, price):
        """
        Parameters:
        -----------
        name : str
            The name of the product.
        price : float
            The price of the product.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return f"Product(name={self.name}, price={self.price})"
