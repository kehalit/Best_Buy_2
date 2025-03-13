from itertools import product
import unittest
from ..products import Product


def test_create_valid_product():
    """ Test if creating a normal product works. """

    product = Product("Laptop",price=1000, quantity=5)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 5
    assert product.active is True


def test_create_prod_invalid_details():
    """Test by creating a product with invalid details (empty name, negative price, negative quantity)
 invokes an exception."""
    product = Product("Laptop",price=1000, quantity=5)

    with pytest.raises(ValueError):
        Product("",price=1000, quantity=5)
    with pytest.raises(ValueError):
        Product("Laptop",price=-1000, quantity=5)
    with pytest.raises(ValueError):
        Product("Laptop",price=1000, quantity=-5)


def test_prod_becomes_inactive():
    """Test  when a product reaches 0 quantity, it becomes inactive."""

    product = Product("Laptop", price=1000, quantity=5)
    product.set_quantity(0)
    assert product.active is False

def test_buy_modifies_quantity():
    """Test that buying a larger quantity than exists invokes exception."""

    product = Product("Laptop", price=1000, quantity=5)
    total_price = product.buy(3)
    assert product.quantity == 2
    assert total_price == 3000


def test_to_buy_too_much():
    product = Product("Laptop", price=1000, quantity=5)

    with pytest.raises(ValueError):
        product.buy(6)
