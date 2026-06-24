from uuid import uuid4
from datetime import datetime


class Transaction:
    def __init__(
        self,
        amount: int,
        ac_type: str,
        ac_no: int,
        owner: str,
        transaction_type: str,
        curr_balance: int,
    ):
        self.transaction_id = str(uuid4())
        self.amount: int = amount
        self.current_balance: int = curr_balance
        self.account_type: str = ac_type
        self.account_no: str = ac_no
        self.owner: str = owner
        self.transaction_type: str = transaction_type
        self.transaction_date: str = datetime.now().strftime("%d-%m-%Y")

    def generate_receipt(self):
        return f"""
        account_no: {self.account_no}
        account_type: {self.account_type}
        account_owner: {self.owner}
        transaction type: {self.transaction_type}
        transaction on date: {self.transaction_date}
        amount is: {self.amount}$ now current balance is: {self.current_balance}$
"""
