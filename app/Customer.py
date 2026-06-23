from Person import Person

from uuid import uuid4


class Customer(Person):

    def __init__(self):
        self.customer_id = str(uuid4())
        self.accounts = {}
