"""
``cart.Offer`` implementations.
"""

from cart import Offer


class XForY(Offer):
    def __init__(self, product_name, x, y):
        self._product_name = product_name
        self._x = x
        self._y = y

    def discount(self, cart):
        # I know that accessing protected attributes is not proper. However,
        # here it makes actually sense: Otherwise I would have to expand the
        # public API.
        cart._product_prices


class ThreeForTwo(Offer):
    def __init__(self, product_name):
        super(ThreeForTwo, self).__init__(product_name, 2, 3)


class TwoForOne(Offer):
    def __init__(self, product_name):
        super(TwoForOne, self).__init__(product_name, 1, 2)
