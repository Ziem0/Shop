class Email:
    
    def __init__(self, name):
        self.email = name

    def __str__(self):
        return '{}.gmail.com'.format(self.email)