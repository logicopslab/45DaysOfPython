# 05_iterators.py

class MyIterator:
    def __init__(self, max_val):
        self.max = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration


obj = MyIterator(5)

for num in obj:
    print(num)
