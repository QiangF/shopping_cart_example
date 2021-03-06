# -*- coding: utf-8 -*-

import cart
from cart._compatibility import utf8, is_py3
from cart import offers

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
    if is_py3:
        error = FileNotFoundError
    else:
        error = IOError
    with pytest.raises(error):
        cart.cart_from_csv('test/cart_files/inexistant.csv')


def test_invalid_cart_from_csv_file():
    with pytest.raises(cart.MalformedCSV):
        cart.cart_from_csv('test/cart_files/invalid_cart.csv')


# ---------
#  Cart tests
# ---------
def test_add_to_cart():
    def _cart(prices, name, quantity):
        c = cart.Cart(prices)
        c.add_to_cart(name, quantity)
        return c

    assert _cart({'apple': 1.0}, 'apple', 2)._shopping_list == {'apple': 2}
    with pytest.raises(KeyError):
        _cart({}, 'apple', 2)

    # Multiple adds of apples
    c = _cart({'apple': 1.0}, 'apple', 2)
    c.add_to_cart('apple', 2)
    assert c._shopping_list == {'apple': 4}


def test_cart_price():
    c = cart.Cart({'a': 1, 'b': 2})
    assert c.price == 0
    c.add_to_cart('b', 2)
    assert c.price == 4
    c.add_to_cart('a', 1)
    assert c.price == 5


# ---------
#  cart.Offer tests
# ---------

def test_offer_type():
    assert isinstance(offers.ThreeForTwo('a'), cart.Offer)

    class Something(object):
        def discount(self):
            pass

    assert isinstance(Something(), cart.Offer)
    assert not isinstance(object(), cart.Offer)
