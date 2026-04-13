# data_pipeline.py

def clean_data(data):
    # Remove leading/trailing spaces and lowercase
    return [item.strip().lower() for item in data]


def remove_empty(data):
    return [item for item in data if item]


def transform_data(data):
    # Capitalize each word
    return [item.capitalize() for item in data]


def validate_data(data):
    # Keep only alphabetic entries
    return [item for item in data if item.isalpha()]


def pipeline(data, steps):
    for step in steps:
        data = step(data)
    return data


def main():
    raw_data = [
        "  apple ",
        "banana",
        "",
        "Cherry123",
        " mango "
    ]

    steps = [
        clean_data,
        remove_empty,
        validate_data,
        transform_data
    ]

    result = pipeline(raw_data, steps)

    print("Processed Data:", result)


main()
