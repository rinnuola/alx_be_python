class BankAccount:
    """A simple Bank Account class."""

    def __init__(self, initial_balance=0):
        """Initialize account with an optional initial balance."""
        self.__account_balance = initial_balance  # encapsulated balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display current balance."""
        print(f"Current Balance: ${self.__account_balance}")
