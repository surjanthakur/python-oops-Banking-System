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
        return "new customer added ✅"

    def remove_customer(self, customer_id: str):
        """
        Docstring for remove_customer

        :param self: accept's current Customer object that is named self
        :param customer_id: accept's a customer_id string
        """

        cstmr = next((c for c in self.customers if c.customer_id == customer_id), None)
        if cstmr is None:
            return "wrong customer check again ❌"
        self.customers.remove(cstmr)
        return "customer deleted successfully ✅"

    def add_employee(self, employee: Employee):
        """
        Docstring for add_employee

        :param self: accept's current Employee object that is named self
        :param employee: accept's employee object
        """

        self.employees.add(employee)
        return "new employee added ✅"

    def create_account(self, customer_name: str, customer_id: str, ac_type: str):
        normalized_name = customer_name.strip().lower()

        account = next(
            (
                a
                for a in self.accounts
                if a.owner.strip().lower() == normalized_name
                and a.owner_id == customer_id
            ),
            None,
        )
        if account is None:
            new_account = Account(customer_name, customer_id, ac_type)
            self.accounts.add(new_account)
            return f"new account is created✅  AC-NO: {new_account.account_number}"

        return "account already exist's ❌"

    def remove_account(self, customer_id: str, account_no: int):
        # verify the customer id and the account number match in the accounts object
        # if match delete account else:
        #  return error
        pass

    def view_account(self, customer_id: str, account_no: int):
        # verify the customer id and the account number match in the accounts object
        # if match return info else error msg
        pass
