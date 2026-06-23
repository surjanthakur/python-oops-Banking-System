from uuid import uuid4
from datetime import datetime


class Transaction:
    def __init__(self):
        self.transaction_id = str(uuid4())
        self.amount: int
        self.account_type: str = "saving"
        self.transaction_type: str
        self.transaction_date: str = datetime.now().strftime("%d-%m-%Y")
