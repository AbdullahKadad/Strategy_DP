# Payment Processing System

This system provides various payment methods for purchasing products.

## Classes

### `Payment`

Abstract base class for payment methods.

- `process_payment(self, product)`: Abstract method to process a payment.

### `Cash`

A class representing a cash payment.

- `process_payment(self, product)`: Process a cash payment.

### `Credit`

A class representing a credit card payment.

- `process_payment(self, product)`: Process a credit card payment.
  - `Args`:
    - `product (Product)`: The product being purchased.

### `Paypal`

A class representing a PayPal payment.

- `process_payment(self, product)`: Process a PayPal payment.
  - `Args`:
    - `product (Product)`: The product being purchased.

### `Context`

A class representing the context in which a payment is processed.

- `__init__(self, payment)`: Initialize the context with a payment method.
  - `Args`:
    - `payment (Payment)`: The payment method to be used.
- `set_payment(self, payment)`: Set a new payment method.
  - `Args`:
    - `payment (Payment)`: The new payment method to be set.
- `execute_payment(self, product)`: Execute the payment process.
  - `Args`:
    - `product (Product)`: The product being purchased.
  - `Returns`:
    - `str`: A message indicating the result of the payment process.

### `Product`

A class representing a product.

- `__init__(self, name, price)`: Initialize the product with a name and price.
  - `Parameters`:
    - `name (str)`: The name of the product.
    - `price (float)`: The price of the product.
- `__str__(self)`: Returns a string representation of the product.
