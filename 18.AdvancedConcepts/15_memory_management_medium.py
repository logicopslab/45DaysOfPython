# memory_management_medium.py

import sys
import gc


class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None

    def __del__(self):
        print(f"Node with value {self.value} is being garbage collected")


def reference_count_demo():
    a = [1, 2, 3]

    print("Initial reference count:", sys.getrefcount(a))

    b = a
    print("After assigning b:", sys.getrefcount(a))

    c = a
    print("After assigning c:", sys.getrefcount(a))

    del b
    print("After deleting b:", sys.getrefcount(a))

    del c
    print("After deleting c:", sys.getrefcount(a))


def circular_reference_demo():
    print("\n--- Circular Reference Demo ---")

    node1 = Node(1)
    node2 = Node(2)

    # Creating circular reference
    node1.ref = node2
    node2.ref = node1

    del node1
    del node2

    print("Objects deleted, forcing garbage collection...")
    gc.collect()


def main():
    print("--- Reference Count Demo ---")
    reference_count_demo()

    circular_reference_demo()


main()
