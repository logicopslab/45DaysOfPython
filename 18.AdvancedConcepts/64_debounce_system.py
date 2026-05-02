# debounce_system.py

import time
import threading


def debounce(wait_time):
    def decorator(func):
        timer = None

        def wrapper(*args, **kwargs):
            nonlocal timer

            def delayed():
                func(*args, **kwargs)

            if timer:
                timer.cancel()

            timer = threading.Timer(wait_time, delayed)
            timer.start()

        return wrapper
    return decorator


@debounce(2)  # wait 2 seconds after last call
def handle_event(event):
    print(f"Processed event: {event}")


def simulate():
    events = ["click1", "click2", "click3", "click4"]

    for event in events:
        print(f"Triggering {event}")
        handle_event(event)
        time.sleep(0.5)  # rapid calls

    # Wait to allow last event to process
    time.sleep(3)


def main():
    simulate()


main()
