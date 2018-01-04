import os

class OrderUI:

    menu = ['Enter', 'Exit']
    menu1 = ['Add to cart', 'Buy', 'Logout']

    title = '\nWelcome at our shopping mall!\n'
    title1 = '\nShop:\n'
    title2 = 'This item is not available. Sorry!' 
    title3 = 'You added item to cart'
    title4 = "You should pay: "
    title5 = 'Incorrect payment. Try again!'

    @staticmethod
    def clear():
        os.system('clear')

    @staticmethod
    def print(it):
        print(it)

    @staticmethod
    def create_menu(title, menu):
        out = title
        for n,i in enumerate(menu,1):
            out += '{}. {}\n'.format(n,i)
        return out

    @staticmethod
    def user_choice(menu):
        user = 0
        while user < 1 or user > len(menu)+1:
            try:
                user = int(input('choose option: '))
            except ValueError:
                print('Invalid input!')
            
        return user

    @staticmethod
    def login_inputs():
        name = input('name: ').lower()
        return name

    @staticmethod
    def adress_inputs():
        town = input('town: ').lower()
        street = input('street: ').lower()
        number = input('number: ').lower()
        return town, street, number

    @staticmethod
    def create_shop(magazine):
        out = ''
        number = 1
        for k,v in magazine.shop.items():
            out += '{}. {} - available:{} price:{}\n'.format(number, k, v[0], v[1])
            number += 1
        return out

    @staticmethod
    def choose_item():
        item = input('choose item: ').lower()
        return item

    @staticmethod
    def pay():
        try:
            payment = int(input('Make a transfer: '))
            return payment
        except ValueError:
            print('Only numbers allowed!')

    @staticmethod
    def create_payment_window(title, price):
        return "{}: {}".format(title, price)

    @staticmethod
    def summary_for_email():
        pass