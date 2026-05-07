# circuit_retry_combo.py

import time
import random


class CircuitBreaker:
    def __init__(self, threshold):
        self.threshold = threshold
        self.failures = 0
        self.open = False

    def call(self, func):
        if self.open:
            return "Circuit open"

        try:
            result = func()
            self.failures = 0
            return result

        except Exception:
            self.failures += 1

            if self.failures >= self.threshold:
                self.open = True
                print("Circuit opened")

            raise


def unreliable():
    if random.choice([True, False]):
        raise Exception("Fail")
    return "Success"


def call_with_retry(cb):
    for _ in range(3):
        try:
            return cb.call(unreliable)
        except:
            print("Retrying...")
            time.sleep(1)

    return "Failed after retries"


def main():
    cb = CircuitBreaker(threshold=2)

    for i in range(6):
        print(f"\nRequest {i+1}:")
        print(call_with_retry(cb))


main()
