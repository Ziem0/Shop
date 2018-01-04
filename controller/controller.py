import os, sys
from controller.order_controller import OrderController

class Controller:

    def __init__(self, ui, dao):
        self.ui = ui
        self.dao = dao
        self.dao.load()
        self.start_controller()

    def start_controller(self):
        while 1:
            self.ui.print(self.ui.create_menu(self.ui.title, self.ui.menu))
            self.choice = self.ui.user_choice(self.ui.menu)
            self.handle_menu()

    def handle_menu(self):
        if self.choice == 1:
            OrderController(self.ui)
        elif self.choice == 2:
            self.dao.save()
            sys.exit('Goodbye!')
