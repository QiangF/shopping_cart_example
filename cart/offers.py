"""
:py:class:`cart.Offer` implementations.
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
        quantity = cart._shopping_list[self._product_name]
        discounts_on = int(float(quantity) / self._x) * (self._x - self._y)
        return discounts_on * cart._product_prices[self._product_name]


class ThreeForTwo(XForY):
    """
    Buy three, pay for two.

    >>> c = cart.Cart({'strawberries': 1})
    >>> c.add_to_cart('strawberries', 3)
    >>> c.price
    3
    >>> c.add_offer(ThreeForTwo('strawberries'))
    >>> c.price
    2
    >>> c.add_to_cart('strawberries', 1)  # Four strawberries
    >>> c.price
    3
    """
    def __init__(self, product_name):
        super(ThreeForTwo, self).__init__(product_name, 3, 2)


class TwoForOne(XForY):
    """
    Buy two, pay for one.

    >>> c = cart.Cart({'icecream': 1})
    >>> c.add_offer(TwoForOne('icecream'))
    >>> c.add_to_cart('icecream', 1)
    >>> c.price
    1
    >>> c.add_to_cart('icecream', 1)
    >>> c.price
    1
    >>> c.add_to_cart('icecream', 1)
    >>> c.price
    2
    >>> c.add_to_cart('icecream', 1)
    >>> c.price
    2
    """
    def __init__(self, product_name):
        super(TwoForOne, self).__init__(product_name, 2, 1)


class PercentForOther(cart.Offer):
    """
    Buy something and get a price reduction on something else, for example:

    >>> c = cart.Cart({'snickers': 1, 'mars': 1})
    >>> c.add_to_cart('mars', 1)
    >>> c.add_to_cart('snickers', 1)
    >>> c.price
    2
    >>> c.add_offer(PercentForOther('mars', 'snickers', 0.2))
    >>> c.price
    1.8
    >>> c.add_to_cart('snickers', 1)
    >>> c.price
    2.8
    >>> c.add_to_cart('mars', 2)
    >>> c.price
    4.6
    """
    def __init__(self, product_name, reduction_product, percentage):
        self._product_name = product_name
        self._reduction_product = reduction_product
        self._percentage = percentage

    def discount(self, cart):
        product_quantity = cart._shopping_list[self._product_name]
        red_product_quantity = cart._shopping_list[self._reduction_product]
        actual_reductions = min(product_quantity, red_product_quantity)
        return actual_reductions * self._percentage
