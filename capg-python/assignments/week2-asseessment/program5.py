class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def check_availability(self, quantity):
        return self.stock >= quantity
    

product = Product(name="Laptop", price=1200, stock=10)

requested_quantity = 5
if product.check_availability(requested_quantity):
    print(f"{requested_quantity} {product.name}s are available.")
else:
    print(f"{requested_quantity} {product.name}s are not available.")