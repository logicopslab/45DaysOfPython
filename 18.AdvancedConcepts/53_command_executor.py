# command_executor.py

import json


def start_service():
    print("Starting service...")


def stop_service():
    print("Stopping service...")


def restart_service():
    print("Restarting service...")


# Map command names to functions
command_map = {
    "start": start_service,
    "stop": stop_service,
    "restart": restart_service
}


def execute_commands(config_file):
    try:
        with open(config_file, "r") as file:
            config = json.load(file)

        commands = config.get("commands", [])

        for cmd in commands:
            action = command_map.get(cmd)

            if action:
                action()
            else:
                print(f"Unknown command: {cmd}")

    except FileNotFoundError:
        print("Config file not found")

    except json.JSONDecodeError:
        print("Invalid JSON format")


def main():
    file_name = input("Enter config file: ")
    execute_commands(file_name)


main()