class Product:

    def __init__(self, base_price, tax_rate):
        self.base_price = base_price
        self.tax_rate = tax_rate

    def get_product_price(self):
        return self.base_price * (1 + self.tax_rate)