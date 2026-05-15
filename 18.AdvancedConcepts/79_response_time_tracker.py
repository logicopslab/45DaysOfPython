# response_time_tracker.py

import time
import random


response_times = []


def simulate_api_call():
    start = time.time()

    # Simulate API processing
    delay = random.uniform(0.5, 2.0)
    time.sleep(delay)

    end = time.time()

    response_time = end - start

    response_times.append(response_time)

    print(f"Response Time: {response_time:.2f}s")


def show_metrics():
    avg = sum(response_times) / len(response_times)
    maximum = max(response_times)
    minimum = min(response_times)

    print("\nPerformance Metrics")
    print("-------------------")
    print(f"Average: {avg:.2f}s")
    print(f"Max: {maximum:.2f}s")
    print(f"Min: {minimum:.2f}s")


def main():
    for _ in range(5):
        simulate_api_call()

    show_metrics()


main()