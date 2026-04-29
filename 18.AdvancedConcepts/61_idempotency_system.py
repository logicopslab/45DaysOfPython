# idempotency_system.py

processed_requests = {}


def process_payment(request_id, amount):
    # Check if request already processed
    if request_id in processed_requests:
        print(f"[DUPLICATE] Returning previous result for {request_id}")
        return processed_requests[request_id]

    print(f"[PROCESSING] Payment of ${amount} for request {request_id}")

    # Simulate processing result
    result = f"Payment of ${amount} successful"

    # Store result
    processed_requests[request_id] = result

    return result


def simulate():
    requests = [
        ("req1", 100),
        ("req2", 200),
        ("req1", 100),  # duplicate
        ("req3", 300),
        ("req2", 200)   # duplicate
    ]

    for req_id, amount in requests:
        print("\nRequest:", req_id)
        result = process_payment(req_id, amount)
        print("Result:", result)


def main():
    simulate()


main()
