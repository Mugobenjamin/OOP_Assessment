class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance


account = BankAccount(100)

account.deposit(50)

account.withdraw(30)

account.withdraw(200)

print(f"Final balance: ${account.get_balance()}")
