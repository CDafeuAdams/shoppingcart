from shoppingcart import Shopping_cart

class Customer:

    def __init__(self, customers_name_passed_in, shopping_cart_passed_in, view_products_passed_in):
        self.name = customers_name_passed_in
        self.shopping_cart = shopping_cart_passed_in
        self.view_prodcuts = view_products_passed_in