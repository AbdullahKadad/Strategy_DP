import pytest
from Product.product import Product
from Payment.Context.context import Context
from Payment.Cash.cash import Cash
from Payment.Credit.credit import Credit
from Payment.PayPal.paypal import Paypal


@pytest.fixture
def cash_payment():
    return Cash()

@pytest.fixture
def credit_payment():
    return Credit()

@pytest.fixture
def paypal_payment():
    return Paypal()

@pytest.fixture
def product():
    return Product("Test Product", 50.0)

# Test functions to verify the behavior of payment processing
def test_cash_payment(cash_payment, product, capsys):
    context = Context(cash_payment)
    context.execute_payment(product)
    captured = capsys.readouterr()
    assert "Test Product" in captured.out
    assert "50.0" in captured.out

def test_credit_payment(credit_payment, product, monkeypatch, capsys):
    # Mock user input for CVV
    monkeypatch.setattr('builtins.input', lambda _: '123')
    context = Context(credit_payment)
    context.execute_payment(product)
    captured = capsys.readouterr()
    assert "Test Product" in captured.out
    assert "50.0" in captured.out

def test_paypal_payment(paypal_payment, product, monkeypatch, capsys):
    # Mock user input for verification code
    monkeypatch.setattr('builtins.input', lambda _: '0012')
    context = Context(paypal_payment)
    context.execute_payment(product)
    captured = capsys.readouterr()
    assert "Test Product" in captured.out
    assert "50.0" in captured.out
