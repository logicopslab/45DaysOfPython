# ============================================================
# Program 10: Exception Handling
# Concepts: try/except/else/finally, raise, custom exceptions,
#           exception chaining, context managers
# ============================================================

# ---- Basic try/except/else/finally -------------------------
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  [Error] Cannot divide {a} by zero!")
        return None
    except TypeError as e:
        print(f"  [Error] Type error: {e}")
        return None
    else:
        print(f"  {a} / {b} = {result:.4f}")
        return result
    finally:
        print(f"  (divide attempted with a={a}, b={b})")

print("SAFE DIVIDE")
print("-" * 40)
safe_divide(10, 3)
safe_divide(5, 0)
safe_divide("x", 2)

# ---- Catching multiple exceptions --------------------------
print("\nMULTIPLE EXCEPTIONS")
print("-" * 40)

def parse_index(data, idx_str):
    try:
        idx    = int(idx_str)
        result = data[idx]
        return result
    except (ValueError, TypeError):
        print(f"  '{idx_str}' is not a valid integer index.")
    except IndexError:
        print(f"  Index {idx_str} out of range (len={len(data)}).")

data = [10, 20, 30]
parse_index(data, "1")
parse_index(data, "hello")
parse_index(data, "99")

# ---- Custom exceptions -------------------------------------
print("\nCUSTOM EXCEPTIONS")
print("-" * 40)

class AppError(Exception):
    """Base class for application errors."""

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"Validation failed on '{field}': {message}")

class InsufficientFundsError(AppError):
    def __init__(self, balance, amount):
        self.shortfall = amount - balance
        super().__init__(f"Need £{self.shortfall:.2f} more (balance=£{balance:.2f}, amount=£{amount:.2f})")

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("age", "must be an integer")
    if age < 0 or age > 150:
        raise ValidationError("age", f"value {age} is out of realistic range")
    return True

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

for age in [25, -3, "old"]:
    try:
        validate_age(age)
        print(f"  Age {age!r}: valid ✓")
    except ValidationError as e:
        print(f"  {e}")

try:
    new_balance = withdraw(100.0, 150.0)
except InsufficientFundsError as e:
    print(f"  {e} (shortfall=£{e.shortfall:.2f})")

# ---- Exception chaining ------------------------------------
print("\nEXCEPTION CHAINING")
print("-" * 40)

def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file '{path}' is missing") from e

try:
    load_config("/nonexistent/config.json")
except RuntimeError as e:
    print(f"  RuntimeError  : {e}")
    print(f"  Caused by     : {e.__cause__}")

# ---- Context manager for resource safety -------------------
print("\nCONTEXT MANAGER (suppress)")
from contextlib import suppress

with suppress(FileNotFoundError):
    open("/tmp/ghost_file.txt")   # silently ignored
print("  File not found suppressed gracefully.")