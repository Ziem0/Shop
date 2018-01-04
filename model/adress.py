class Adress:

    def __init__(self, town, street, number):
        self.town = town
        self.street = street
        self.number = number

    def __str__(self):
        return '{}\nul.{} {}'.format(self.town, self.street, self.number)