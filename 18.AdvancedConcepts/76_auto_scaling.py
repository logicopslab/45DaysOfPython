# auto_scaling.py

import random
import time


servers = 2
MAX_SERVERS = 5
MIN_SERVERS = 1


def monitor_load():
    # Simulate CPU usage %
    return random.randint(10, 100)


def scale_system(load):
    global servers

    print(f"Current Load: {load}%")

    if load > 70 and servers < MAX_SERVERS:
        servers += 1
        print("Scaling UP")

    elif load < 30 and servers > MIN_SERVERS:
        servers -= 1
        print("Scaling DOWN")

    else:
        print("No scaling needed")

    print("Active Servers:", servers)


def main():
    for _ in range(10):
        load = monitor_load()
        scale_system(load)

        print("----------------")
        time.sleep(1)


main()