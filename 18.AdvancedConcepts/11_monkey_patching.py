# 11_monkey_patching.py

class Dog:
    def speak(self):
        return "Bark"


def new_speak(self):
    return "Meow (patched)"


# Monkey patching
Dog.speak = new_speak

d = Dog()
print(d.speak())
