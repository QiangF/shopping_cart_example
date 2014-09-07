# -*- coding: utf-8 -*-

import cart
from cart._compatibility import utf8

import pytest


# ---------
#  cart_from_csv tests
# ---------

def test_valid_cart_from_csv():
    _cart = cart.cart_from_csv('test/cart_files/default_cart.csv')
    assert _cart._product_prices == {'apple': 0.15,
                                     'ice cream': 3.49,
                                     'strawberries': 2.00,
                                     'snickers bar': 0.70}


def test_unicode_cart_from_csv():
    _cart = cart.cart_from_csv('test/cart_files/unicode_cart.csv')
    assert _cart._product_prices == {utf8('somethingä'): 1.0}


def test_non_existing_cart_from_csv_file():
    with pytest.raises(FileNotFoundError):
        cart.cart_from_csv('test/cart_files/inexistant.csv')


def test_invalid_cart_from_csv_file():
    with pytest.raises(cart.MalformedCSV):
        cart.cart_from_csv('test/cart_files/invalid_cart.csv')

# ---------
#  Cart tests
# ---------

def test_add_to_cart():
    def content(prices, name, quantity):
        c = cart.Cart(prices)
        c.add_to_cart(name, quantity)
        return c._added_products

    assert content({'apple': 1.0}, 'apple', 2) == {'apple', 2}
    with pytest.raises(KeyError):
        assert content({}, 'apple', 2) == {'apple', 2}
