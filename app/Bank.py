from Customer import Customer
from Employee import Employee
from Account import Account
from Transaction import Transaction


class Bank:
    bank_name: str = "SBI-limited"

    def __init__(self):
        self.customers: set[Customer] = {}
        self.employees: set[Employee] = {}
        self.accounts: set[Account] = {}
        self.transactions: set[Transaction] = {}

    def add_customer(self, customer: Customer):
        pass

    def remove_customer(self, customer_id: str):
        pass

    def add_employee(self):
        pass

    def create_account(self, customer: Customer):
        pass

    def remove_account(self, customer: Customer, account_no: int):
        pass

    def view_account(self, account_no: int):
        pass
