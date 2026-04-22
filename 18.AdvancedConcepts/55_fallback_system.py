# fallback_system.py

import random


def primary_service():
    # Simulate failure randomly
    if random.choice([True, False]):
        raise Exception("Primary service failed")
    return "Primary service response"


def secondary_service():
    return "Secondary service response (fallback)"


def get_data():
    try:
        print("Trying primary service...")
        return primary_service()

    except Exception as e:
        print("Error:", e)
        print("Switching to fallback service...")
        return secondary_service()


def main():
    for i in range(5):
        print(f"\nRequest {i+1}:")
        result = get_data()
        print("Result:", result)


main()
