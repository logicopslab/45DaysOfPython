# csv_analyzer.py

import csv


def read_csv(file_name):
    data = []

    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

        return data

    except FileNotFoundError:
        print("Error: File not found")
        return []


def analyze_sales(data):
    total = 0
    count = 0

    for row in data:
        try:
            amount = float(row["sales"])
            total += amount
            count += 1
        except (ValueError, KeyError):
            continue

    average = total / count if count > 0 else 0
    return total, average


def display_results(total, avg):
    print("\nSales Analysis")
    print("----------------")
    print("Total Sales:", total)
    print("Average Sales:", avg)


def main():
    file_name = input("Enter CSV file name: ")

    data = read_csv(file_name)

    if data:
        total, avg = analyze_sales(data)
        display_results(total, avg)


main()
