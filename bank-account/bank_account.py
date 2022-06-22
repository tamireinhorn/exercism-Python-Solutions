class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        self.__verify_open()
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError("account already open")
        self.is_open = True

    def deposit(self, amount):
        self.__verify_open()
        self.__validate_value(amount)
        self.balance += amount

    def withdraw(self, amount):
        self.__verify_open()
        self.__validate_value(amount)
        if self.balance < amount:
            raise ValueError("amount must be less than balance")
        self.balance -= amount

    def close(self):
        self.__verify_open()
        self.is_open = False
        self.balance = 0

    def __verify_open(self):
        if not self.is_open:
            raise ValueError("account not open")
    
    def __validate_value(self, amount):
        if amount < 0:
            raise ValueError("amount must be greater than 0")
