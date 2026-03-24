# exception_handling_medium.py

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be greater than 0")

    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")

    return balance - amount


def deposit(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Deposit amount must be greater than 0")

    return balance + amount


def main():
    balance = 1000

    try:
        print("Current Balance:", balance)

        choice = input("Enter transaction (deposit/withdraw): ").lower()
        amount = float(input("Enter amount: "))

        if choice == "deposit":
            balance = deposit(balance, amount)
        elif choice == "withdraw":
            balance = withdraw(balance, amount)
        else:
            print("Invalid transaction type")

        print("Updated Balance:", balance)

    except InvalidAmountError as e:
        print("Error:", e)

    except InsufficientBalanceError as e:
        print("Error:", e)

    except ValueError:
        print("Error: Please enter a valid number")

    finally:
        print("Transaction process completed")


main()
