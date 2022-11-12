from shoppingcart import Shopping_cart

class Customer:

    def __init__(self, customers_name, shopping_cart, view_products):
        self.name = customers_name
        self.shopping_cart = Shopping_cart()
        self.view_prodcuts = view_products