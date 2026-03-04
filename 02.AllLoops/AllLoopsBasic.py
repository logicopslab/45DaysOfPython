print("1. FOR LOOP EXAMPLE")
# for loop iterating over a range
for i in range(5):
    print("Iteration:", i)

print("\n2. FOR LOOP OVER A LIST")
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print("Fruit:", fruit)

print("\n3. WHILE LOOP EXAMPLE")
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

print("\n4. NESTED LOOP EXAMPLE")
for i in range(3):
    for j in range(2):
        print("i =", i, "j =", j)

print("\n5. BREAK STATEMENT EXAMPLE")
for i in range(10):
    if i == 5:
        print("Breaking loop at", i)
        break
    print("Number:", i)

print("\n6. CONTINUE STATEMENT EXAMPLE")
for i in range(5):
    if i == 2:
        print("Skipping", i)
        continue
    print("Number:", i)

print("\n7. PASS STATEMENT EXAMPLE")
for i in range(3):
    if i == 1:
        pass   # placeholder, does nothing
    print("Value:", i)

print("\n8. LOOP WITH ELSE EXAMPLE")
for i in range(3):
    print("Iteration:", i)
else:
    print("Loop finished normally")

print("\n9. WHILE LOOP WITH ELSE")
num = 0
while num < 3:
    print("Number:", num)
    num += 1
else:
    print("While loop completed")
