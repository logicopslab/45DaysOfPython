# Base Class
class Person:

    def __init__(self, name, age):   # Constructor
        self.name = name             # Instance variable
        self.age = age               # Instance variable

    def display_info(self):          # Method
        print("Name:", self.name)
        print("Age:", self.age)


# Derived Class (Inheritance)
class Student(Person):

    def __init__(self, name, age, marks):
        super().__init__(name, age)  # Call parent constructor
        self.__marks = marks         # Encapsulation (private variable)

    def calculate_average(self):     # Method
        total = 0
        for m in self.__marks:
            total += m
        return total / len(self.__marks)

    def display_student(self):       # Method
        self.display_info()
        print("Marks:", self.__marks)
        print("Average:", self.calculate_average())


# Creating Objects
student1 = Student("Alice", 20, [85, 90, 88])
student2 = Student("Bob", 22, [75, 80, 78])

# Using methods
student1.display_student()
print()

student2.display_student()
