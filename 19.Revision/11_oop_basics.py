# ============================================================
# Program 11: Object-Oriented Programming — Basics
# Concepts: class, __init__, instance/class/static methods,
#           properties, __str__, __repr__, __eq__, __lt__
# ============================================================

class BankAccount:
    """A simple bank account with deposit/withdraw/interest."""

    bank_name  = "PyBank"          # class variable (shared)
    _count     = 0                 # private class variable

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner   = owner
        self._balance = float(balance)   # protected attribute
        BankAccount._count += 1
        self._id = BankAccount._count

    # ---- Properties ----------------------------------------
    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value

    # ---- Instance methods ----------------------------------
    def deposit(self, amount: float) -> "BankAccount":
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"  [+] Deposited £{amount:,.2f}  → Balance: £{self._balance:,.2f}")
        return self   # fluent interface

    def withdraw(self, amount: float) -> "BankAccount":
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds (balance £{self._balance:,.2f}).")
        self._balance -= amount
        print(f"  [-] Withdrew  £{amount:,.2f}  → Balance: £{self._balance:,.2f}")
        return self

    def apply_interest(self, rate: float = 0.03) -> "BankAccount":
        interest = self._balance * rate
        self._balance += interest
        print(f"  [~] Interest  £{interest:,.2f} ({rate*100:.1f}%)  → Balance: £{self._balance:,.2f}")
        return self

    # ---- Class & static methods ----------------------------
    @classmethod
    def total_accounts(cls) -> int:
        return cls._count

    @staticmethod
    def is_valid_amount(amount) -> bool:
        return isinstance(amount, (int, float)) and amount > 0

    # ---- Dunder methods ------------------------------------
    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance=£{self._balance:,.2f})"

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance!r})"

    def __eq__(self, other):
        return isinstance(other, BankAccount) and self._balance == other._balance

    def __lt__(self, other):
        return self._balance < other._balance

    def __add__(self, other):
        """Merge two accounts into a new one."""
        return BankAccount(f"{self.owner}+{other.owner}", self._balance + other._balance)


# ---- Demo --------------------------------------------------
print(f"{'='*45}")
print(f"  {BankAccount.bank_name} Account System")
print(f"{'='*45}")

acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

print(f"\nAccounts created: {BankAccount.total_accounts()}")
print(acc1)
print(acc2)

print("\nAlice's transactions (fluent chain):")
acc1.deposit(200).deposit(300).apply_interest(0.05).withdraw(150)

print("\nBob's transactions:")
acc2.deposit(1000).withdraw(200).apply_interest()

print(f"\nAlice: {acc1}")
print(f"Bob  : {acc2}")
print(f"Alice > Bob? {acc1 > acc2}")

print("\nMerging accounts:")
merged = acc1 + acc2
print(f"Merged: {merged}")

print(f"\nValid amount  £50 ? {BankAccount.is_valid_amount(50)}")
print(f"Valid amount -£10 ? {BankAccount.is_valid_amount(-10)}")

print(f"\nrepr: {repr(acc1)}")