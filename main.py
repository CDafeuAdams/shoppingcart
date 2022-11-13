from product import Product

product_one = Product('chips', 2.29, 'snacks')
product_two = Product('milk', 4.89, 'dairy')
product_three = Product('spaghetti noodles', 1.99, 'pasta')
product_four = Product ('ground turkey', 5.39, 'meat')
product_five = Product ('marinara sauce', 2.89, 'sauces')
product_six = Product ('oregano', 3.65, 'seasonings')


print(f"{product_one.name} : {product_one.price} : {product_one.category}")
print(f"{product_two.name} : {product_two.price} : {product_two.category}")
print(f"{product_three.name} : {product_three.price} : {product_three.category}")
print(f"{product_four.name} : {product_four.price} : {product_four.category}")
print(f"{product_five.name} : {product_five.price} : {product_five.category}")
print(f"{product_six.name} : {product_six.price} : {product_six.category}")