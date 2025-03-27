import pytest
from products import Product, NonStockedProduct, LimitedProduct

def test_create_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100

def test_create_product_with_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=100, quantity=10)
    with pytest.raises(ValueError):
        Product("Invalid Product", price=-1, quantity=10)
    with pytest.raises(ValueError):
        Product("Invalid Product", price=100, quantity=-1)

def test_product_inactive_when_quantity_zero():
    product = Product("MacBook Air M2", price=1450, quantity=0)
    assert not product.is_active()

def test_buy_product_modifies_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert product.get_quantity() == 90
    assert total_price == 14500

def test_buy_more_than_available_quantity():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(200)

def test_non_stocked_product():
    product = NonStockedProduct("Windows License", price=125)
    assert product.get_quantity() == 0
    assert product.show() == "Windows License, Price: 125 (Non-Stocked)"

def test_limited_product():
    product = LimitedProduct("Shipping Fee", price=10, quantity=250, maximum=1)
    assert product.buy(1) == 10
    with pytest.raises(ValueError):
        product.buy(2)
    assert product.show() == "Shipping Fee, Price: 10, Quantity: 249, Max allowed: 1"