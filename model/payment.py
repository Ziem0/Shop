class Payment:

    def __init__(self):
        self.status = False

    def change_status_positive(self):
        self.status = True
    
    def change_status_negative(self):
        self.status = False

    @staticmethod
    def calculate_payment(basket):
        cost = sum([item.price for item in basket])
        return cost

    def __str__(self):
        if self.status:
            return 'Good(s) paid'
        else:
            return 'Unpaid item(s)'

    