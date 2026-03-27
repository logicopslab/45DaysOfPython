# log_analyzer.py

def analyze_log(file_name):
    event_count = {}

    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(" - ")

                if len(parts) >= 2:
                    event_type = parts[1]

                    if event_type in event_count:
                        event_count[event_type] += 1
                    else:
                        event_count[event_type] = 1

        return event_count

    except FileNotFoundError:
        print("Error: File not found")
        return {}


def display_results(results):
    print("\nLog Analysis Result")
    print("-------------------")

    for event, count in results.items():
        print(f"{event}: {count}")


def main():
    file_name = input("Enter log file name: ")

    results = analyze_log(file_name)

    if results:
        display_results(results)


main()
