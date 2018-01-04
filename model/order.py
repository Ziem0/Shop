class Order:

    all_orders = []    
    number = 1

    def __init__(self, customer, email, payment, adress):
        self.order_number = Order.number
        self.customer = customer
        self.email = email
        self.payment = payment
        self.adress = adress
        Order.number += 1
        Order.all_orders.append(self)


