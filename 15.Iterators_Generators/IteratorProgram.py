# Iterator Program: Custom number iterator

class NumberIterator:

    def __init__(self, max_num):
        self.max = max_num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


# Using the iterator
nums = NumberIterator(5)

for n in nums:
    print(n)
