# throttle_system.py

import time


def throttle(interval):
    def decorator(func):
        last_called = 0

        def wrapper(*args, **kwargs):
            nonlocal last_called

            current_time = time.time()

            if current_time - last_called >= interval:
                last_called = current_time
                return func(*args, **kwargs)
            else:
                print("Call throttled")

        return wrapper
    return decorator


@throttle(2)  # allow once every 2 seconds
def send_request(i):
    print(f"Request {i} sent at {time.strftime('%X')}")


def simulate():
    for i in range(6):
        send_request(i)
        time.sleep(0.5)  # rapid calls


def main():
    simulate()


main()
