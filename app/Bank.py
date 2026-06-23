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
        """
        Docstring for add_customer

        :param self: accept's current Customer object that is named self
        :param customer: accept's a customer object
        """
        self.customers.add(customer)
        return "new customer added"

    def remove_customer(self, customer_id: str):
        """
        Docstring for remove_customer

        :param self: accept's current Customer object that is named self
        :param customer_id: accept's a customer_id string
        """

        cstmr = next((c for c in self.customers if c.customer_id == customer_id), None)
        if cstmr is None:
            return "wrong customer check again"
        self.customers.remove(cstmr)
        return "customer deleted successfully"

    def add_employee(self, employee: Employee):
        """
        Docstring for add_employee

        :param self: accept's current Employee object that is named self
        :param employee: accept's employee object
        """

        self.employees.add(employee)
        return "new employee added"

    def create_account(self, customer: Customer):
        # check if customer exists or not
        # check if account exists with the customer id
        # create a new Account object
        # update the accounts set
        # return message
        pass

    def remove_account(self, customer_id: str, account_no: int):
        # verify the customer id and the account number match in the accounts object
        # if match delete account else return error
        pass

    def view_account(self, customer_id: str, account_no: int):
        # verify the customer id and the account number match in the accounts object
        # if match return info else error msg
        pass
