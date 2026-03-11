# Medium Program: Separate even and odd numbers

def separate_numbers(num_list):
    even = []
    odd = []

    for n in num_list:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return even, odd


numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

even_numbers, odd_numbers = separate_numbers(numbers)

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)