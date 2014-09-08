"""
This is a very simple example of a shopping cart. It's well documented and
tested.

You can use it like this:

    >>> # Create a shopping cart with a price list
    >>> cart = Cart({'banana': 1.0, 'apple': 2.0})
    >>> cart.add_to_cart('banana', 1)
    >>> cart.price
    1.0
    >>> cart.add_to_cart('apple', 3)
    >>> cart.price
    7.0

You can specify discounts:

    >>> from cart.offers import ThreeForTwo
    >>> cart.add_offer(ThreeForTwo('apple'))
    >>> cart.price
    5.0
"""

__version__ = '0.1.0'

import csv
import abc

from cart._compatibility import utf8, use_metaclass


class MalformedCSV(Exception):
    """
    A price definition file should contain ``name,product`` file, separated
    by a comma.
    """


def cart_from_csv(csv_file_path):
    """
    Reads a CSV file with product names and prices and returns a shopping cart.

    The CSV file should roughly look like this::

        apple,0.15
        ice cream,3.49
        ...

    :type csv_file_path: str
    :rtype: :py:class:`Cart`
    """
    prices = {}
    with open(csv_file_path) as csvfile:
        for i, row in enumerate(csv.reader(csvfile, delimiter=',')):
            if len(row) != 2:
                raise MalformedCSV('Each CSV row should contain exactly 2'
                                   '  rows, not %s. -> name,price')
            prices[utf8(row[0])] = float(row[1])
    return Cart(prices)


class Cart(object):
    """
    A shopping cart.

    :param product_prices: A dictionary to define product prices.
    :type product_prices: dict of str -> float
    """
    def __init__(self, product_prices):
        self._product_prices = product_prices
        self._offers = []
        self._shopping_list = {}

    def add_offer(self, offer):
        """
        :type offer: :py:class:`Offer`
        """
        # It's possible to add multiple offers of the same type. This might
        # make sense, but it could also lead to strange - even negative -
        # prices. We're trusting the people who are using the API.
        self._offers.append(offer)

    def add_to_cart(self, product_name, quantity):
        if product_name not in self._product_prices:
            raise KeyError('')

        try:
            self._shopping_list[product_name] += quantity
        except KeyError:
            self._shopping_list[product_name] = quantity

    @property
    def price(self):
        price = 0
        # First calculate the normal price.
        for product_name, quantity in self._shopping_list.items():
            price += self._product_prices[product_name] * quantity

        # Apply discounts.
        for offer in self._offers:
            price -= offer.discount(self)
        return price

    def __repr__(self):
        return '<%s: %s products; %s$>' % (type(self).__name__,
                                           len(self._product_prices), self.price)


class Offer(use_metaclass(abc.ABCMeta)):
    @abc.abstractmethod
    def discount(self, cart):
        """
        Returns a price discount as a simple float value.
        """

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Offer:
            if any("discount" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
