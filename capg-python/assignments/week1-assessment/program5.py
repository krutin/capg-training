

class shopping():
    def __init__(self):
        print("welcome to xyz shop what would you like to shop today")
        self.cart = {}
    def add_item(self,item,price):
        self.cart[item] = price
    def view_cart(self):
        items = list(self.cart.keys())
        print("The items in cart are:\n", items)
    def items_price(self):
        price = sum(self.cart.values())
        print("The price of items in cart is:\n", price)

bag = shopping()
bag.add_item("pen",20)
bag.add_item("pencil",20)
bag.add_item("phone",20)
bag.add_item("watch",20)
bag.items_price()
bag.view_cart()
