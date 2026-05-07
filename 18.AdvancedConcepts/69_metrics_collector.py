# metrics_collector.py

metrics = {
    "requests": 0,
    "errors": 0
}


def record_request(success=True):
    metrics["requests"] += 1

    if not success:
        metrics["errors"] += 1


def get_stats():
    total = metrics["requests"]
    errors = metrics["errors"]

    error_rate = (errors / total) * 100 if total > 0 else 0

    return {
        "total_requests": total,
        "errors": errors,
        "error_rate": error_rate
    }


def simulate():
    import random

    for _ in range(10):
        success = random.choice([True, True, False])
        record_request(success)

    stats = get_stats()

    print("\nMetrics:")
    for k, v in stats.items():
        print(f"{k}: {v}")


simulate()
