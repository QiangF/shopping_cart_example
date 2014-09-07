"""
``cart.Offer`` implementations.
"""

import cart


class XForY(cart.Offer):
    """
    Buy X, pay for Y.
    """
    def __init__(self, product_name, x, y):
        self._product_name = product_name
        self._x = x
        self._y = y

    def discount(self, cart):
        # I know that accessing protected attributes is not proper. However,
        # here it makes actually sense: Otherwise I would have to expand the
        # public API.
        cart._product_prices


class ThreeForTwo(cart.Offer):
    """
    Buy three, pay for two.

    >>> c = cart.Cart({'strawberries': 1})
    >>> c.add_to_cart('strawberries', 1)
    >>> assert c.price == 1
    >>> c.add_to_cart('strawberries', 1)
    >>> assert c.price == 2
    >>> c.add_to_cart('strawberries', 1)
    >>> assert c.price == 2
    >>> c.add_to_cart('strawberries', 1)
    >>> assert c.price == 3
    """
    def __init__(self, product_name):
        super(ThreeForTwo, self).__init__(product_name, 2, 3)


class TwoForOne(cart.Offer):
    """
    Buy two, pay for one.

    >>> c = cart.Cart({'icecream': 1})
    >>> c.add_to_cart('icecream', 1)
    >>> assert c.price == 1
    >>> c.add_to_cart('icecream', 1)
    >>> assert c.price == 1
    >>> c.add_to_cart('icecream', 1)
    >>> assert c.price == 2
    >>> c.add_to_cart('icecream', 1)
    >>> assert c.price == 2
    """
    def __init__(self, product_name):
        super(TwoForOne, self).__init__(product_name, 1, 2)
