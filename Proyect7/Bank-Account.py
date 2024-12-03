class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Customer(Person):
    def __init__(self, first_name, last_name, account_number, balance=0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name}\nAccount balance {self.account_number}: ${self.balance}"

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Deposit accepted")

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print("Withdrawal completed")
        else:
            print("Insufficient funds")


def create_customer():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    account_number = input("Enter your account number: ")
    customer = Customer(first_name, last_name, account_number)
    return customer


def start():
    my_customer = create_customer()
    print(my_customer)
    option = 0

    while option != 'E':
        print('Choose: Deposit (D), Withdraw (W), or Exit (E)')
        option = input()

        if option == 'D':
            deposit_amount = int(input("Amount to deposit: "))
            my_customer.deposit(deposit_amount)
        elif option == 'W':
            withdraw_amount = int(input("Amount to withdraw: "))
            my_customer.withdraw(withdraw_amount)
        print(my_customer)

    print("Thank you for banking with Python Bank")


start()
