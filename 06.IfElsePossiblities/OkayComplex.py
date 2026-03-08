def check_admission(math, physics, english, age):

    # Basic eligibility
    if age >= 17:

        if math >= 60 and physics >= 60:
            print("Eligible for Engineering")

        elif english >= 70 and (math >= 50 or physics >= 50):
            print("Eligible for Arts Program")

        elif math >= 40 and physics >= 40 and english >= 40:
            print("Eligible for General Studies")

        else:
            print("Not eligible for admission")

    else:
        print("Rejected: Age below requirement")


def main():
    math = int(input("Enter Math marks: "))
    physics = int(input("Enter Physics marks: "))
    english = int(input("Enter English marks: "))
    age = int(input("Enter Age: "))

    check_admission(math, physics, english, age)


main()
