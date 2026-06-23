from datetime import datetime
import random


class Account:
    def __init__(self):
        self.account_number: int = random.randint(1000000000, 9999999999)
        self.__balance: int = 0
        self.account_status: str = "active"
        self.created_at: str = datetime.now().strftime("%d %m %y")

    def deposite(self, amount: int):
        pass

    def widraw(self, amount: int):
        pass

    def get_balance(self):
        return self.__balance
