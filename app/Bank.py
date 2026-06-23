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

    def add_customer(self, customer: Customer) -> str:
        """
        Add a new customer to the bank.

        :param customer: Customer instance to add.
        :return: Confirmation message string.
        """
        self.customers.add(customer)
        return "new customer added ✅"

    def remove_customer(self, customer_id: str) -> str:
        """
        Remove a customer by their ID.

        :param customer_id: ID of the customer to remove.
        :return: Success or error message string.
        """

        cstmr = next((c for c in self.customers if c.customer_id == customer_id), None)
        if cstmr is None:
            return "wrong customer check again ❌"
        self.customers.remove(cstmr)
        return "customer deleted successfully ✅"

    def add_employee(self, employee: Employee) -> str:
        """
        Add a new employee to the bank.

        :param employee: Employee instance to add.
        :return: Confirmation message string.
        """

        self.employees.add(employee)
        return "new employee added ✅"

    def create_account(self, customer_name: str, customer_id: str, ac_type: str) -> str:
        """
        Create a new account for a customer if one doesn't already exist.

        :param customer_name: Name of the account owner.
        :param customer_id: ID of the account owner.
        :param ac_type: Account type (e.g. 'savings', 'current').
        :return: Account creation message or error string.
        """

        account = next(
            (
                a
                for a in self.accounts
                if a.owner.strip().lower()
                == customer_name  # here the name is also normalized ok
                and a.owner_id == customer_id
            ),
            None,
        )
        if account is None:
            new_account = Account(customer_name, customer_id, ac_type)
            self.accounts.add(new_account)
            return f"new account is created✅  AC-NO: {new_account.account_number}"

        return "account already exist's ❌"

    def remove_account(self, customer_id: str, account_no: int) -> str:
        """
        Remove an account belonging to a customer.

        :param customer_id: Owner's customer ID.
        :param account_no: Account number to remove.
        :return: Success or error message string.
        """
        account = next(
            (
                a
                for a in self.accounts
                if a.owner_id == customer_id and a.account_number == account_no
            ),
            None,
        )
        if account is None:
            return "wrong data try again ❌"
        self.accounts.remove(account)
        return "account removed ✅"

    def view_account(self, customer_id: str, account_no: int):
        """
        Return account information for a given customer and account number.

        :param customer_id: Owner's customer ID.
        :param account_no: Account number to view.
        :return: `Account` instance if found, otherwise an error message string.
        """
        account = next(
            (
                a
                for a in self.accounts
                if a.owner_id == customer_id and a.account_number == account_no
            ),
            None,
        )
        if account is None:
            return "wrong data try again ❌"
        return account
