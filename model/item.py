class Item:

    shop = {}

    def __init__(self, thing, price):
        self.thing = thing
        self.price = price

    @classmethod
    def create_item(cls, thing):
        for k,v in Item.shop.items():
            if thing == k:
                return cls(thing, v[1])
