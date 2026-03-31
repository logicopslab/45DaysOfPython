# config_loader.py

import json


def load_config(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print("Error: Config file not found")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return None


def validate_config(config):
    required_keys = ["host", "port", "debug"]

    for key in required_keys:
        if key not in config:
            print(f"Missing required key: {key}")
            return False

    return True


def display_config(config):
    print("\nConfiguration Loaded:")
    for key, value in config.items():
        print(f"{key}: {value}")


def main():
    file_name = input("Enter config file name: ")

    config = load_config(file_name)

    if config and validate_config(config):
        display_config(config)
    else:
        print("Invalid configuration")


main()
