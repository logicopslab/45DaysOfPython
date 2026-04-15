# api_key_auth.py

import time


# Simulated API key database
api_keys = {
    "key123": {
        "expires_at": time.time() + 60,   # valid for 60 seconds
        "usage_limit": 5,
        "used": 0
    },
    "key456": {
        "expires_at": time.time() + 120,
        "usage_limit": 3,
        "used": 0
    }
}


def validate_api_key(key):
    if key not in api_keys:
        return "Invalid API Key"

    key_data = api_keys[key]

    # Check expiration
    if time.time() > key_data["expires_at"]:
        return "API Key expired"

    # Check usage limit
    if key_data["used"] >= key_data["usage_limit"]:
        return "API Key usage limit exceeded"

    # Update usage
    key_data["used"] += 1

    return "Access Granted"


def simulate_requests():
    key = input("Enter API key: ")

    for i in range(6):
        result = validate_api_key(key)
        print(f"Request {i+1}: {result}")
        time.sleep(1)


def main():
    simulate_requests()


main()
