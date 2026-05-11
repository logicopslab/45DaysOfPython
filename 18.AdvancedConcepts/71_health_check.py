# health_check.py

import random


services = {
    "Database": True,
    "API": True,
    "Cache": True,
    "AuthService": True
}


def check_service(service_name):
    # Simulate random failures
    return random.choice([True, True, False])


def run_health_checks():
    report = {}

    for service in services:
        status = check_service(service)
        report[service] = "UP" if status else "DOWN"

    return report


def display_report(report):
    print("\nSystem Health Report")
    print("---------------------")

    overall = "HEALTHY"

    for service, status in report.items():
        print(f"{service}: {status}")

        if status == "DOWN":
            overall = "UNHEALTHY"

    print("\nOverall System Status:", overall)


def main():
    report = run_health_checks()
    display_report(report)


main()