# 09_reflection.py

class Person:
    def __init__(self):
        self.name = "Ravi"

    def greet(self):
        print("Hello from Person")


obj = Person()

# getattr
print(getattr(obj, "name"))

# setattr
setattr(obj, "age", 25)
print(obj.age)

# hasattr
print(hasattr(obj, "name"))

# dynamic method call
method = getattr(obj, "greet")
method()
