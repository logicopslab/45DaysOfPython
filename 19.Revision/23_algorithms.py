# ============================================================
# Program 23: Classic Algorithms
# Covers: Sorting (bubble, merge, quick), Binary Search,
#         Dynamic Programming (knapsack, LCS), Dijkstra
# ============================================================

import heapq
import time

# =============================================
# SORTING ALGORITHMS
# =============================================

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    pivot  = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

data = [64, 34, 25, 12, 22, 11, 90, 45, 3, 77]
print("SORTING ALGORITHMS")
print(f"  Input  : {data}")
print(f"  Bubble : {bubble_sort(data)}")
print(f"  Merge  : {merge_sort(data)}")
print(f"  Quick  : {quick_sort(data)}")

# =============================================
# BINARY SEARCH
# =============================================

def binary_search(arr, target):
    """Iterative binary search. Returns index or -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:   return mid
        elif arr[mid] < target:  lo = mid + 1
        else:                    hi = mid - 1
    return -1

sorted_data = sorted(data)
print("\nBINARY SEARCH")
print(f"  Sorted : {sorted_data}")
for target in [22, 45, 99]:
    idx = binary_search(sorted_data, target)
    print(f"  Search {target:>3}: index={idx}")

# =============================================
# DYNAMIC PROGRAMMING
# =============================================

# 1. 0/1 Knapsack
def knapsack(weights, values, capacity):
    n  = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w],
                               dp[i-1][w - weights[i-1]] + values[i-1])
    return dp[n][capacity]

weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]
cap     = 8
print("\nDYNAMIC PROGRAMMING")
print(f"  0/1 Knapsack (cap={cap}): max value = {knapsack(weights, values, cap)}")

# 2. Longest Common Subsequence
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # Reconstruct
    seq, i, j = [], m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            seq.append(s1[i-1]); i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]: i -= 1
        else: j -= 1
    return "".join(reversed(seq))

a, b = "AGGTAB", "GXTXAYB"
print(f"  LCS('{a}', '{b}') = '{lcs(a, b)}'  (len={len(lcs(a,b))})")

# 3. Coin change (min coins)
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

print(f"  Coins [1,5,10,25] → amount 67: {coin_change([1,5,10,25], 67)} coins")

# =============================================
# DIJKSTRA'S SHORTEST PATH
# =============================================

def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 6)],
    "C": [("D", 3), ("E", 5)],
    "D": [("E", 1)],
    "E": [],
}
print("\nDIJKSTRA — shortest paths from A")
for node, d in dijkstra(graph, "A").items():
    print(f"  A → {node}: {d}")