# -*- coding: utf-8 -*-

import cart
from cart._compatibility import utf8


def test_valid_cart_from_csv():
    _cart = cart.cart_from_csv('test/cart_files/default_cart.csv')
    assert _cart._product_prices == {'apple': 0.15,
                                     'ice cream': 3.49,
                                     'strawberries': 2.00,
                                     'snickers bar': 0.70}


def test_unicode_cart_from_csv():
    _cart = cart.cart_from_csv('test/cart_files/unicode_cart.csv')
    assert _cart._product_prices == {utf8('somethingä'): 1.0}
