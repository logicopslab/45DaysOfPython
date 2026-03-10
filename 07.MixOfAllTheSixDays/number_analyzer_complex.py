def analyze_numbers(num_list):
    even = []
    odd = []
    greater_than_50 = []

    for n in num_list:

        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

        if n > 50:
            greater_than_50.append(n)

    return even, odd, greater_than_50


numbers = input("Enter numbers separated by space: ")

num_list = [int(x) for x in numbers.split()]

even, odd, gt50 = analyze_numbers(num_list)

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Numbers > 50:", gt50)

print("First 3 numbers:", num_list[:3])
print("Last 3 numbers:", num_list[-3:])