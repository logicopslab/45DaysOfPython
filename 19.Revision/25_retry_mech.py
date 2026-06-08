import time

attempt = 1

while attempt <= 3:
    try:
        raise Exception("Failure")

    except Exception:
        print(f"Attempt {attempt}")

        if attempt == 3:
            print("Failed")

        time.sleep(2 ** attempt)

    attempt += 1