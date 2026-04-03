# rate_limiter.py

import time

request_times = []


def is_allowed(limit, window_seconds):
    current_time = time.time()

    # Remove old requests outside window
    while request_times and request_times[0] < current_time - window_seconds:
        request_times.pop(0)

    if len(request_times) < limit:
        request_times.append(current_time)
        return True
    else:
        return False


def simulate_requests():
    for i in range(10):
        if is_allowed(3, 5):
            print(f"Request {i+1}: Allowed")
        else:
            print(f"Request {i+1}: Blocked")

        time.sleep(1)


def main():
    simulate_requests()


main()
