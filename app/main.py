from Bank import Bank
from Account import Account
from Customer import Customer


def display_operations():
    return int(input("""
                     press 4 to view personal account ✅
                     press 5 to remove account ✅
                     press 2 to deposite amount ✅
                     press 3 to withraw amount ✅
                     ***************************
                     press 100 to exit ❌
"""))


def main():
    bank_obj = Bank()
    name = input("enter your name: ")
    email = input("enter your email: ")
    phone_no = input("enter your phone number: ")
    account_type = input("enter your account type e.g.[saving or current] : ")

    new_customer = Customer(name, email, phone_no)
    print(new_customer.display_profile())
    print(bank_obj.add_customer(new_customer))
    account = bank_obj.create_account(
        new_customer.name, new_customer.customer_id, account_type
    )

    while True:
        choice_no = display_operations()

        if choice_no == 100:
            break

        if choice_no == 4:
            print(
                bank_obj.view_personal_account(
                    new_customer.customer_id, account.account_number
                )
            )

        if choice_no == 5:
            print(
                bank_obj.delete_account(
                    new_customer.customer_id, account.account_number
                )
            )

        if choice_no == 2:
            amount = int(input("enter amount: "))
            print(account.deposite(amount))

        if choice_no == 3:
            amount = int(input("enter amount: "))
            print(account.widraw(amount))


main()
