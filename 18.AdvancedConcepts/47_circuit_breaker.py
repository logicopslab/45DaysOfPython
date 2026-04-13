# circuit_breaker.py

import time


class CircuitBreaker:
    def __init__(self, failure_threshold, recovery_time):
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        self.failure_count = 0
        self.state = "CLOSED"
        self.last_failure_time = None

    def call(self, func):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_time:
                print("Trying again (HALF-OPEN state)")
                self.state = "HALF-OPEN"
            else:
                return "Request blocked (Circuit OPEN)"

        try:
            result = func()
            self.failure_count = 0
            self.state = "CLOSED"
            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                print("Circuit opened due to repeated failures")

            return f"Error: {e}"


# Simulated unstable service
def unstable_service():
    import random
    if random.choice([True, False]):
        raise Exception("Service failure")
    return "Service success"


def main():
    cb = CircuitBreaker(failure_threshold=3, recovery_time=5)

    for i in range(10):
        print(f"Request {i+1}:", cb.call(unstable_service))
        time.sleep(1)


main()
