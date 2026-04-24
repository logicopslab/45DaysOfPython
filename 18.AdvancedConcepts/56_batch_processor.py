# batch_processor.py

def process_batch(batch):
    print(f"Processing batch: {batch}")
    # Simulate processing delay
    import time
    time.sleep(1)


def create_batches(data, batch_size):
    batches = []

    for i in range(0, len(data), batch_size):
        batches.append(data[i:i + batch_size])

    return batches


def process_data(data, batch_size):
    batches = create_batches(data, batch_size)

    for index, batch in enumerate(batches):
        print(f"\nBatch {index + 1}")
        process_batch(batch)


def main():
    data = list(range(1, 21))  # Sample data

    batch_size = int(input("Enter batch size: "))

    process_data(data, batch_size)


main()
