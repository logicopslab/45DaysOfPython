# Base Class
class BankAccount:

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance   # Encapsulation (private variable)

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    # Getter method (Encapsulation)
    def get_balance(self):
        return self.__balance

    # Display account information
    def display_account(self):
        print("\nAccount Number:", self.account_number)
        print("Owner:", self.owner)
        print("Balance:", self.__balance)


# Derived Class (Inheritance)
class SavingsAccount(BankAccount):

    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    # Method to add interest
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added:", interest)


# Another Derived Class
class CurrentAccount(BankAccount):

    def __init__(self, account_number, owner, balance, overdraft_limit):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    # Override withdraw method
    def withdraw(self, amount):

        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance = self.get_balance() - amount
            self._BankAccount__balance = new_balance
            print("Withdrawn:", amount)
        else:
            print("Overdraft limit exceeded")


# Creating Objects
acc1 = SavingsAccount("SA101", "Alice", 5000, 5)
acc2 = CurrentAccount("CA202", "Bob", 3000, 2000)


# Using methods
acc1.display_account()
acc1.deposit(1000)
acc1.apply_interest()
acc1.display_account()


acc2.display_account()
acc2.withdraw(4500)
acc2.display_account()
