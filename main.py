from Product.product import Product
from Payment.Context.context import Context
from Payment.Cash.cash import Cash
from Payment.Credit.credit import Credit
from Payment.PayPal.paypal import Paypal


if __name__ == "__main__":

    product = Product("Car", 4000)

    context = Context(Cash())
    context.execute_payment(product)

    context.set_payment(Credit())
    context.execute_payment(product)

    context.set_payment(Paypal())
    context.execute_payment(product)