# config_versioning.py

config = {}
history = []


def update_config(key, value):
    config[key] = value

    # Save snapshot
    history.append(config.copy())

    print(f"Updated {key} = {value}")


def show_current():
    print("\nCurrent Config:")
    print(config)


def show_history():
    print("\nConfig History:")

    for i, version in enumerate(history):
        print(f"Version {i+1}: {version}")


def main():
    update_config("timeout", 30)
    update_config("retries", 5)
    update_config("debug", True)

    show_current()
    show_history()


main()