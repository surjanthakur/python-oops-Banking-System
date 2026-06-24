from datetime import datetime
import random

from Transaction import Transaction


class Account:
    def __init__(self, owner: str, owner_id: str, account_type: str):
        self.account_number: int = random.randint(1000000000, 9999999999)
        self.owner: str = owner
        self.owner_id: str = owner_id
        self.__balance: int = 0
        self.__transactions: set[Transaction] = set()
        self.account_status: str = "active"
        self.account_type: str = account_type
        self.created_at: str = datetime.now().strftime("%d-%m-%Y")

    def deposite(self, amount: int) -> str:
        if amount >= 100000:
            return "too large amount to Deposite ❌"
        self.__balance += amount
        new_transaction = Transaction(
            amount,
            self.account_type,
            self.account_number,
            self.owner_id,
            "Deposite",
            self.__balance,
        )
        self.__transactions.add(new_transaction)

        return new_transaction.generate_receipt()

    def widraw(self, amount: int):
        if amount >= self.__balance:
            return "inEfficient amount to widraw ❌"
        self.__balance -= amount
        new_transaction = Transaction(
            amount,
            self.account_type,
            self.account_number,
            self.owner_id,
            "Widraw",
            self.__balance,
        )
        self.__transactions.add(new_transaction)

        return new_transaction.generate_receipt()

    def get_balance(self):
        return self.__balance
