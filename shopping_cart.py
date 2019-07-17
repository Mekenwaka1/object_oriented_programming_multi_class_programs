from product import Product

class Shopping_cart:

    def __init__(self):
        self.cart  = []

    def add_product(self, new_product): 
        self.cart.append(new_product)
    
    def remove_product(self, product_to_remove):
        self.cart.remove(product_to_remove)
    
    def cost_of_products_before_tax(self):
        sum = 0

        for product in self.cart:
            sum += product.base_price

        return sum 

    def cost_of_products_after_tax(self):
        sum = 0

        for product in self.cart:
            sum += product.base_price * (1 + product.tax_rate)

        return sum 