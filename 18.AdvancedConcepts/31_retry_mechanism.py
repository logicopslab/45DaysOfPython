# retry_mechanism.py

import time
import random


def unreliable_operation():
    # Simulate random failure
    if random.choice([True, False]):
        raise Exception("Operation failed")
    return "Success"


def retry_operation(max_retries, delay):
    attempt = 0

    while attempt < max_retries:
        try:
            result = unreliable_operation()
            print("Operation succeeded")
            return result

        except Exception as e:
            attempt += 1
            print(f"Attempt {attempt} failed:", e)

            if attempt < max_retries:
                print(f"Retrying in {delay} seconds...\n")
                time.sleep(delay)

    return "All retries failed"


def main():
    result = retry_operation(3, 2)
    print("Final Result:", result)


main()
