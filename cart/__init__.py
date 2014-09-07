import csv

from cart._compatibility import utf8

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
        self._added_products = {}

    def add_offer(self, offer):
        """
        :type offer: :py:class:`Offer`
        """
        self._offers.append(offer)

    def add_to_cart(self, product_name, price):
        pass

    @property
    def price(self):
        return 0

    def __repr__(self):
        return '<%s: %s products; %s$>' % (type(self).__class__.__name__,
                                           len(self._product_prices), self.price)


class Offer(object):
    pass
