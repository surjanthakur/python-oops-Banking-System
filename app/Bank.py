from Customer import Customer
from Account import Account


class Bank:
    bank_name: str = "SBI-limited"

    def __init__(self):
        self.customers: set[Customer] = set()
        self.accounts: set[Account] = set()

    def add_customer(self, customer: Customer) -> str:
        """
        Add a new customer to the bank.

        :param customer: Customer instance to add.
        :return: Confirmation message string.
        """
        self.customers.add(customer)
        return f"new customer: {customer.customer_id} added ✅"

    def create_account(self, customer_name: str, customer_id: str, ac_type: str):
        """
        Create a new account for a customer if one doesn't already exist.

        :param customer_name: Name of the account owner.
        :param customer_id: ID of the account owner.
        :param ac_type: Account type (e.g. 'savings', 'current').
        :return: Account creation message or error string.
        """
        normalize_name = customer_name.strip().lower()

        account = next(
            (
                a
                for a in self.accounts
                if a.owner.strip().lower() == normalize_name
                and a.owner_id == customer_id
            ),
            None,
        )
        if account is None:
            customer = next(
                (cust for cust in self.customers if cust.customer_id == customer_id),
                None,
            )
            if customer:
                new_account = Account(customer_name, customer_id, ac_type)
                self.accounts.add(new_account)
                customer.accounts.add(new_account)

                return new_account

            return "customer not exist's ❌"

        return "account already exist's ❌"

    def delete_account(self, customer_id: str, account_no: int) -> str:
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
        return f"account {account.owner} ,{account.account_number} removed ✅"

    def view_personal_account(self, customer_id: str, account_no: int):
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
        return f"owner:{account.owner} , id={account.owner_id} , ac_no={account.account_number} , balance={account.get_balance()} , created_at={account.created_at}"
