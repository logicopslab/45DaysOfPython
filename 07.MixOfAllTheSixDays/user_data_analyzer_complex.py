def analyze_users(users):

    adults = []
    minors = []
    names_starting_a = []

    for user in users:

        name = user[0]
        age = int(user[1])

        if age >= 18:
            adults.append(name)
        else:
            minors.append(name)

        if name.lower().startswith("a"):
            names_starting_a.append(name)

    return adults, minors, names_starting_a


def display_summary(users):

    print("\nAll Users:")
    for i in range(len(users)):
        name = users[i][0]
        age = users[i][1]
        print(i, ":", name, "-", age)

    print("\nFirst two users:", users[:2])
    print("Last two users:", users[-2:])


users = []

n = int(input("How many users? "))

for i in range(n):

    data = input("Enter name and age: ").split()

    name = data[0]
    age = int(data[1])

    users.append([name, age])


display_summary(users)

adults, minors, a_names = analyze_users(users)

print("\nAdults:", adults)
print("Minors:", minors)
print("Names starting with A:", a_names)