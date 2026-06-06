# ============================================================
# Program 22: Data Structures from Scratch
# Implements: Linked List, Binary Search Tree, Min-Heap, Graph
# ============================================================

# =============================================
# 1. SINGLY LINKED LIST
# =============================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def prepend(self, data):
        node      = Node(data)
        node.next = self.head
        self.head = node

    def delete(self, data):
        if not self.head: return
        if self.head.data == data:
            self.head = self.head.next; return
        cur = self.head
        while cur.next and cur.next.data != data:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt      = cur.next
            cur.next = prev
            prev     = cur
            cur      = nxt
        self.head = prev

print("1. LINKED LIST")
ll = LinkedList()
for v in [10, 20, 30, 40, 50]:
    ll.append(v)
ll.prepend(5)
print(f"   List     : {ll.to_list()}")
ll.delete(30)
print(f"   Del 30   : {ll.to_list()}")
ll.reverse()
print(f"   Reversed : {ll.to_list()}")

# =============================================
# 2. BINARY SEARCH TREE
# =============================================
class BSTNode:
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _ins(node, k):
            if not node: return BSTNode(k)
            if k < node.key:   node.left  = _ins(node.left, k)
            elif k > node.key: node.right = _ins(node.right, k)
            return node
        self.root = _ins(self.root, key)

    def search(self, key) -> bool:
        node = self.root
        while node:
            if   key == node.key: return True
            elif key < node.key:  node = node.left
            else:                 node = node.right
        return False

    def inorder(self) -> list:
        result = []
        def _walk(node):
            if node:
                _walk(node.left)
                result.append(node.key)
                _walk(node.right)
        _walk(self.root)
        return result

    def height(self) -> int:
        def _h(node):
            if not node: return 0
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self.root)

print("\n2. BINARY SEARCH TREE")
bst = BST()
for v in [50, 30, 70, 20, 40, 60, 80, 10]:
    bst.insert(v)
print(f"   In-order : {bst.inorder()}")
print(f"   Height   : {bst.height()}")
print(f"   Search 40: {bst.search(40)}")
print(f"   Search 99: {bst.search(99)}")

# =============================================
# 3. MIN-HEAP
# =============================================
class MinHeap:
    def __init__(self):
        self._h = []

    def push(self, val):
        self._h.append(val)
        self._sift_up(len(self._h) - 1)

    def pop(self):
        if len(self._h) == 1:
            return self._h.pop()
        top         = self._h[0]
        self._h[0] = self._h.pop()
        self._sift_down(0)
        return top

    def peek(self): return self._h[0]

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self._h[i] < self._h[p]:
                self._h[i], self._h[p] = self._h[p], self._h[i]
                i = p
            else: break

    def _sift_down(self, i):
        n = len(self._h)
        while True:
            smallest, l, r = i, 2*i+1, 2*i+2
            if l < n and self._h[l] < self._h[smallest]: smallest = l
            if r < n and self._h[r] < self._h[smallest]: smallest = r
            if smallest == i: break
            self._h[i], self._h[smallest] = self._h[smallest], self._h[i]
            i = smallest

    def __len__(self): return len(self._h)

print("\n3. MIN-HEAP (heap sort demo)")
heap = MinHeap()
import random; random.seed(7)
data = random.sample(range(1, 50), 10)
print(f"   Input    : {data}")
for v in data: heap.push(v)
sorted_data = [heap.pop() for _ in range(len(heap))]
print(f"   Sorted   : {sorted_data}")

# =============================================
# 4. GRAPH (adjacency list) + BFS/DFS
# =============================================
class Graph:
    def __init__(self, directed=False):
        self._adj      = {}
        self._directed = directed

    def add_edge(self, u, v, weight=1):
        self._adj.setdefault(u, []).append((v, weight))
        if not self._directed:
            self._adj.setdefault(v, []).append((u, weight))

    def bfs(self, start):
        from collections import deque
        visited, order = {start}, []
        q = deque([start])
        while q:
            node = q.popleft()
            order.append(node)
            for nb, _ in self._adj.get(node, []):
                if nb not in visited:
                    visited.add(nb); q.append(nb)
        return order

    def dfs(self, start):
        visited, order = set(), []
        def _dfs(node):
            visited.add(node); order.append(node)
            for nb, _ in self._adj.get(node, []):
                if nb not in visited: _dfs(nb)
        _dfs(start)
        return order

print("\n4. GRAPH — BFS & DFS")
g = Graph()
edges = [(1,2),(1,3),(2,4),(2,5),(3,6),(4,7),(5,7)]
for u, v in edges: g.add_edge(u, v)
print(f"   BFS from 1: {g.bfs(1)}")
print(f"   DFS from 1: {g.dfs(1)}")