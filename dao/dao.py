
from model.item import Item
from os import path
import csv

class Dao:

    def __init__(self):
        self.magazine = Item.shop

    def load(self):
        if not path.isfile('static/magazine.csv'):
            raise FileNotFoundError
        else:
            with open('static/magazine.csv', 'r', encoding="utf16") as f:
                reader = csv.reader(f)
                for thing in reader:
                    name = thing[0]
                    amount = thing[1]
                    price = thing[2]
                    self.magazine[name] = [int(amount), int(price)]

    def save(self):
        with open('static/magazine.csv', 'w', encoding='utf16') as f:
            writer = csv.writer(f)
            for k,v in self.magazine.items():
                writer.writerow([k, v[0], v[1]])

