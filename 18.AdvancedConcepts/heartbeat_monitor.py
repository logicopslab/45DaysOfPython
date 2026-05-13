# heartbeat_monitor.py

import time


heartbeats = {}


def send_heartbeat(service_name):
    heartbeats[service_name] = time.time()
    print(f"{service_name} heartbeat received")


def check_services(timeout=5):
    current_time = time.time()

    print("\nService Status:")

    for service, last_seen in heartbeats.items():

        if current_time - last_seen > timeout:
            print(f"{service}: DOWN")
        else:
            print(f"{service}: UP")


def main():
    send_heartbeat("API")
    send_heartbeat("Database")

    time.sleep(3)

    check_services()

    time.sleep(4)

    check_services()


main()