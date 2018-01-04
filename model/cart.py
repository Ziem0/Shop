from model.item import Item

class Cart:

    def __init__(self):
        self.basket = []

    def add_item(self, thing):
        item = Item.create_item(thing)
        self.basket.append(item)

    def remove_item(self, thing):
        for item in self.basket:
            if item.thing == thing:
                self.basket.remove(item)
                Item.shop[item.thing][0] += 1