# monkey_patching_medium.py

class PaymentProcessor:

    def process_payment(self, amount):
        return f"Processing payment of ${amount}"


# Original behavior
processor = PaymentProcessor()
print(processor.process_payment(100))


# New behavior to inject (logging + validation)
def patched_process_payment(self, amount):

    print("[LOG] Payment initiated")

    if amount <= 0:
        return "Invalid payment amount"

    result = f"Processing payment of ${amount}"

    print("[LOG] Payment successful")

    return result


# Monkey patching the class
PaymentProcessor.process_payment = patched_process_payment


print("\n--- After Monkey Patching ---")

processor2 = PaymentProcessor()

print(processor2.process_payment(200))
print(processor2.process_payment(-50))
