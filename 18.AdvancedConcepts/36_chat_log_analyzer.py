# chat_log_analyzer.py

def analyze_chat(file_name, keyword):
    count = 0
    lines_with_keyword = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    count += 1
                    lines_with_keyword.append(line.strip())

        return count, lines_with_keyword

    except FileNotFoundError:
        print("File not found")
        return 0, []


def display_results(count, lines):
    print(f"\nKeyword found {count} times\n")

    print("Matching lines:")
    for line in lines:
        print(line)


def main():
    file_name = input("Enter chat log file: ")
    keyword = input("Enter keyword to search: ")

    count, lines = analyze_chat(file_name, keyword)

    display_results(count, lines)


main()
