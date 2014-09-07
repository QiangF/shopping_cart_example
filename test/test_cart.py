import cart

def test_valid_cart_from_csv():
    _cart = cart.cart_from_csv('test/cart_files/default_cart.csv')
    assert _cart._product_prices == {'apple': 0.15,
                                     'ice cream': 3.49,
                                     'strawberries': 2.00,
                                     'snickers bar': 0.70}
