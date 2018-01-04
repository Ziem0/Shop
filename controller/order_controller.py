from model.order import Order
from model.customer import Customer
from model.item import Item
from model.payment import Payment
from model.adress import Adress
from model.email import Email
import os, sys

class OrderController:

    def __init__(self, ui):
        self.ui = ui
        self.temporary = []
        self.create_menu()

    def create_menu(self):
        self.start = True
        while self.start:
            self.ui.print(self.ui.create_menu(self.ui.title1, self.ui.menu1))
            self.choice = self.ui.user_choice(self.ui.menu)
            self.handle_menu()
    
    def handle_menu(self):
        if self.choice == 1:
            self.create_exhibition()
        elif self.choice == 2:
            self.start_order()
        elif self.choice == 3:
            self.start = False

    def create_exhibition(self):
        self.ui.print(self.ui.create_shop(Item))
        item = self.ui.choose_item()
        self.check_available(item)

    def check_available(self, item):
        for k,v in Item.shop.items():
            if item == k and v[0] > 0:
                Item.shop[k][0] -= 1
                self.temporary.append(item)
                return self.ui.print(self.ui.title3)
        self.ui.print(self.ui.title2)

    def start_order(self):
        name = self.ui.login_inputs()
        town, street, number = self.ui.adress_inputs()
        customer = Customer(name)
        email = Email(name)
        adress = Adress(town, street, number)
        payment = Payment()
        self.order = Order(customer, email, payment, adress)
        self.add_to_cart()    

    def add_to_cart(self):
        for item in self.temporary:
            self.order.customer.add_item(item)
        self.payment_summary()

    def payment_summary(self):
        payment_required = self.order.payment.calculate_payment(self.order.customer.cart.basket)
        self.ui.print(self.ui.create_payment_window(self.ui.title4, payment_required))
        payment = 0

        while payment != payment_required:
            payment = self.ui.pay()
            if payment == payment_required:
                self.order.payment.change_status_positive()
                return self.ui.print(self.order.payment)
            self.ui.print(self.ui.title5)
