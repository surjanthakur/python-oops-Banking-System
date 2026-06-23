from Person import Person
from Account import Account

from uuid import uuid4


class Customer(Person):

    def __init__(self):
        self.customer_id = str(uuid4())
        self.accounts: set[Account] = {}
