class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance for {self.name}: ${self.balance}")


def main():
    print("Welcome to Simple Banking System")
    name = input("Enter your name: ")
    account = BankAccount(name)
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
