from controller.controller import Controller
from dao.dao import Dao
from view.order_ui import OrderUI


def main():
    ui = OrderUI()
    dao = Dao()
    Controller(ui, dao)


if __name__ == '__main__':
    main()
