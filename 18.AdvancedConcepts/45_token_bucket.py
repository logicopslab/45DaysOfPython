# token_bucket.py

import time


class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity          # max tokens
        self.tokens = capacity            # current tokens
        self.refill_rate = refill_rate    # tokens per second
        self.last_refill = time.time()

    def refill(self):
        current_time = time.time()
        elapsed = current_time - self.last_refill

        added_tokens = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + added_tokens)

        self.last_refill = current_time

    def allow_request(self):
        self.refill()

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False


def simulate_requests():
    bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 requests max, refill 1/sec

    for i in range(10):
        if bucket.allow_request():
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: Blocked")

        time.sleep(0.5)


def main():
    simulate_requests()


main()
