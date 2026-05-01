# token_auth.py

import base64
import time


SECRET_KEY = "mysecret"


def generate_token(username):
    expiry = int(time.time()) + 10  # token valid for 10 seconds
    token_data = f"{username}:{expiry}:{SECRET_KEY}"

    token_bytes = token_data.encode()
    token = base64.b64encode(token_bytes).decode()

    return token


def validate_token(token):
    try:
        decoded = base64.b64decode(token).decode()
        username, expiry, secret = decoded.split(":")

        if secret != SECRET_KEY:
            return "Invalid token (tampered)"

        if time.time() > int(expiry):
            return "Token expired"

        return f"Valid token for user: {username}"

    except Exception:
        return "Invalid token format"


def simulate():
    username = "Ravi"

    token = generate_token(username)
    print("Generated Token:", token)

    for i in range(12):
        print(f"\nCheck {i+1}:")
        print(validate_token(token))
        time.sleep(1)


def main():
    simulate()


main()
