class Customer:
    def __init__(self, *args, **kwargs):
        if args:
            self.name, self.address, self.dob = args
        else:
            self.name = kwargs.get('name', '')
            self.address = kwargs.get('address', '')
            self.dob = kwargs.get('dob', '')

    def __str__(self):
        return f"Customer: {self.name}, Address: {self.address}, DOB: {self.dob}"


class Account:
    def __init__(self, *args, **kwargs):
        if args:
            self.acc_number, self.balance, self.owner = args
        else:
            self.acc_number = kwargs.get('acc_number', '')
            self.balance = kwargs.get('balance', 0)
            self.owner = kwargs.get('owner', None)

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. Current balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. Current balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def __str__(self):
        return f"Account Number: {self.acc_number}, Balance: ${self.balance}, Owner: {self.owner.name if self.owner else 'None'}"


class Bank:
    def __init__(self, name=""):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        return "Account added successfully."

    def list_accounts(self):
        if self.accounts:
            return "\n".join(str(account) for account in self.accounts)
        else:
            return "No accounts in the bank."

    def __str__(self):
        return f"Bank: {self.name}, Number of Accounts: {len(self.accounts)}"


def create_account():
    # Prompt user for account details
    acc_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    dob = input("Enter customer date of birth (YYYY-MM-DD): ")

    # Create customer object
    customer = Customer(name, address, dob)

    # Create account object
    account = Account(acc_number, initial_balance, customer)

    return account


# Example usage:

# Create a bank
bank = Bank(name="XYZ Bank")

# Add accounts to the bank
while True:
    choice = input("Do you want to create an account or list accounts? (create/list/exit): ").lower()
    if choice == 'create':
        account = create_account()
        bank.add_account(account)
        print("Account created and added to the bank.")
    elif choice == 'list':
        print("\nAccounts in the bank:")
        print(bank.list_accounts())
    elif choice == 'exit':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 'create', 'list', or 'exit'.")