# Medium Program: Compare two lists using sets

list1 = input("Enter numbers for list1 separated by space: ").split()
list2 = input("Enter numbers for list2 separated by space: ").split()

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)
only_list1 = set1.difference(set2)
only_list2 = set2.difference(set1)

print("Common elements:", common)
print("Only in list1:", only_list1)
print("Only in list2:", only_list2)
