from product import Product

products_name = Product('chips, salsa, macaroni noodles, cheese, milk', 2.29, 3.89, 1.99, 2.79, 4.29, 'snacks, pasta, dairy')

class Shopping_cart:

    def __init__(self, shopping_cart_products_passed_in, empty_products_from_shopping_cart_passed_in, new_product_passed_in, product_total_passed_in):
        self.shopping_cart = shopping_cart_products_passed_in
        self.total += product_total_passed_in
        self.new_product = new_product_passed_in
        self.empty_products = empty_products_from_shopping_cart_passed_in