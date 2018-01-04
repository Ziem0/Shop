from model.cart import Cart

class Customer:

    customers = []

    def __init__(self, name):
        self.name = name
        self.cart = Cart()

        Customer.customers.append(self)

    def add_item(self, thing):
        self.cart.add_item(thing)

    def remove_item(self, thing):
        self.cart.remove_item(thing)