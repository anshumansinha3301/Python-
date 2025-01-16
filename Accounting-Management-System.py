class Account:
    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")
        print(f"Successfully deposited ${amount:.2f} to {self.account_name}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f} from {self.account_name}.")

    def view_balance(self):
        print(f"Current balance for {self.account_name}: ${self.balance:.2f}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            print(f"Transactions for {self.account_name}:")
            for transaction in self.transactions:
                print(transaction)

class AccountingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_name):
        if account_name in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_name] = Account(account_name)
            print(f"Account '{account_name}' created successfully.")

    def get_account(self, account_name):
        return self.accounts.get(account_name)

def main():
    accounting_system = AccountingSystem()

    while True:
        print("\nAccounting Management System")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. View Transactions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_name = input("Enter account name: ")
            accounting_system.create_account(account_name)

        elif choice == '2':
            account_name = input("Enter account name: ")
            amount = float(input("Enter amount to deposit: "))
            account = accounting_system.get_account(account_name)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_name = input("Enter account name: ")
            amount = float(input("Enter amount to withdraw: "))
            account = accounting_system.get_account(account_name)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_name = input("Enter account name: ")
            account = accounting_system.get_account(account_name)
            if account:
                account.view_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            account_name = input("Enter account name: ")
            account = accounting_system.get_account(account_name)
            if account:
                account.view_transactions()
            else:
                print("Account not found.")

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
