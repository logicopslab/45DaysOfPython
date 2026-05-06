# retry_backoff.py

import time
import random


def unreliable():
    if random.choice([True, False]):
        raise Exception("Failure")
    return "Success"


def retry_with_backoff(max_attempts):
    delay = 1

    for attempt in range(1, max_attempts + 1):
        try:
            return unreliable()

        except Exception as e:
            print(f"Attempt {attempt} failed")

            if attempt == max_attempts:
                return "All attempts failed"

            print(f"Retrying in {delay}s...\n")
            time.sleep(delay)
            delay *= 2


def main():
    print(retry_with_backoff(4))


main()