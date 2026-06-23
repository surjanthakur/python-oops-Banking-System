from datetime import datetime
import random


class Account:
    def __init__(self, owner: str, owner_id: str, account_type: str):
        self.account_number: int = random.randint(1000000000, 9999999999)
        self.owner: str = owner
        self.owner_id: str = owner_id
        self.__balance: int = 0
        self.account_status: str = "active"
        self.account_type: str = account_type
        self.created_at: str = datetime.now().strftime("%d-%m-%Y")

    def deposite(self, amount: int):
        pass

    def widraw(self, amount: int):
        pass

    def get_balance(self):
        return self.__balance
