# 1. Find the second-largest unique element in an array without using sort() or max()
# numbers = [10, 20, 40, 30, 40, 20]

# largest = float('-inf')
# second_largest = float('-inf')

# for i in numbers:
#     if i > largest:
#         second_largest = largest
#         largest = i

#     elif i > second_largest and i != largest:
#         second_largest = i

# if second_largest == float('-inf'):
#     print("Second largest element does not exist")
# else:
#     print("Second largest unique element:", second_largest)

# 2. Find all pairs in an array whose sum equals a given target. 
# numbers = [2, 4, 3, 5, 7, 1]
# target = 6

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])

# 3. Move all zeros to the end of an array without changing the order of other elements. 
# numbers = [0, 1, 0, 3, 12]

# result = []

# for i in numbers:
#     if i != 0:
#         result.append(i)

# for i in numbers:
#     if i == 0:
#         result.append(i)

# print("Updated array:", result)

# 4. Find the missing number from an array containing numbers from 1 to N. 
# numbers = [1, 2, 4, 5, 6]

# n = 6

# total = n * (n + 1) // 2

# missing = total - sum(numbers)

# print("Missing number:", missing)

# 5. Find all duplicate elements in a list without using nested loops.
# numbers = [10, 20, 30, 10, 40, 20]

# duplicates = []

# for i in numbers:
#     if numbers.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)

# print("Duplicate elements:", duplicates)

# 6. Find the first non-repeating character in a string.
# text = "swiss"

# for i in text:
#     if text.count(i) == 1:
#         print("First non-repeating character:", i)
#         break

#  7. Check whether two strings are anagrams without using sorted().
# str1 = "listen"
# str2 = "silent"

# if len(str1) == len(str2):
#     for i in str1:
#         if str1.count(i) != str2.count(i):
#             print("Not Anagrams")
#             break
#     else:
#         print("Anagrams")
# else:
#     print("Not Anagrams")

# 8. Merge two sorted arrays without using sort().
# a = [1, 3, 5]
# b = [2, 4, 6]

# result = []
# i = 0
# j = 0

# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         result.append(a[i])
#         i += 1
#     else:
#         result.append(b[j])
#         j += 1

# result.extend(a[i:])
# result.extend(b[j:])

# print("Merged array:", result)

# 9. Rotate an array to the right by K positions. 
# numbers = [1, 2, 3, 4, 5]

# k = 2

# k = k % len(numbers)

# result = numbers[-k:] + numbers[:-k]

# print("Rotated array:", result)

# 10. Find the intersection of two arrays, including duplicate occurrences. 
# a = [1, 2, 2, 3, 4]
# b = [2, 2, 3, 5]

# result = []

# for i in a:
#     if i in b:
#         result.append(i)
#         b.remove(i)

# print("Intersection:", result)

# 11. Find the maximum sum of a contiguous subarray. 
# numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# current_sum = numbers[0]
# max_sum = numbers[0]

# for i in numbers[1:]:
#     current_sum = max(i, current_sum + i)

#     if current_sum > max_sum:
#         max_sum = current_sum

# print("Maximum subarray sum:", max_sum)


# 12. Find the longest substring without repeating characters. 
# text = "abcabcbb"

# longest = ""

# for i in range(len(text)):
#     temp = ""

#     for j in range(i, len(text)):
#         if text[j] in temp:
#             break
#         temp = temp + text[j]

#     if len(temp) > len(longest):
#         longest = temp

# print("Longest substring:", longest)
# print("Length:", len(longest))

# 13. Find the longest common prefix among multiple strings. 
# words = ["flower", "flow", "flight"]

# prefix = words[0]

# for i in words[1:]:
#     while not i.startswith(prefix):
#         prefix = prefix[:-1]

# print("Longest common prefix:", prefix)

# 14. Group a list of strings into anagram groups. 
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# groups = {}

# for i in words:
#     key = "".join(sorted(i))

#     if key in groups:
#         groups[key].append(i)
#     else:
#         groups[key] = [i]

# print("Anagram groups:", list(groups.values()))


# 15. Find the Kth largest element in an unsorted array. 
# numbers = [3, 2, 1, 5, 6, 4]

# k = 2

# numbers.sort(reverse=True)

# print("Kth largest element:", numbers[k - 1])

# 16. Check whether a given string contains balanced parentheses using a stack.
# text = "{[()]}"

# stack = []

# for i in text:
#     if i in "({[":
#         stack.append(i)

#     elif i in ")}]":
#         if len(stack) == 0:
#             print("Not Balanced")
#             break

#         top = stack.pop()

#         if (i == ")" and top != "(") or \
#            (i == "}" and top != "{") or \
#            (i == "]" and top != "["):
#             print("Not Balanced")
#             break
# else:
#     if len(stack) == 0:
#         print("Balanced")
#     else:
#         print("Not Balanced")

# 17. Find all subarrays whose sum equals a given target. 
# numbers = [1, 2, 3, 4, 2]
# target = 5

# for i in range(len(numbers)):
#     total = 0

#     for j in range(i, len(numbers)):
#         total = total + numbers[j]

#         if total == target:
#             print(numbers[i:j+1])

# 18. Merge overlapping intervals in a list. 
# intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

# intervals.sort()

# result = []

# for i in intervals:
#     if not result or i[0] > result[-1][1]:
#         result.append(i)
#     else:
#         result[-1][1] = max(result[-1][1], i[1])

# print("Merged intervals:", result)

# 19. Search for an element in a rotated sorted array. 
# numbers = [4, 5, 6, 7, 0, 1, 2]

# target = 0

# left = 0
# right = len(numbers) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         print("Element found at index:", mid)
#         break

#     elif numbers[left] <= numbers[mid]:
#         if numbers[left] <= target < numbers[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1

#     else:
#         if numbers[mid] < target <= numbers[right]:
#             left = mid + 1
#         else:
#             right = mid - 1
# else:
#     print("Element not found")

# 20. Find the longest consecutive sequence in an unsorted array. 
# numbers = [100, 4, 200, 1, 3, 2]

# s = set(numbers)

# longest = 0

# for i in s:
#     if i - 1 not in s:
#         count = 1
#         num = i

#         while num + 1 in s:
#             count = count + 1
#             num = num + 1

#         if count > longest:
#             longest = count

# print("Longest consecutive sequence length:", longest)

# 21. Find the trapped rainwater between elevation bars.
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# left = 0
# right = len(height) - 1

# left_max = 0
# right_max = 0

# water = 0

# while left < right:

#     if height[left] < height[right]:

#         if height[left] >= left_max:
#             left_max = height[left]
#         else:
#             water = water + left_max - height[left]

#         left = left + 1

#     else:

#         if height[right] >= right_max:
#             right_max = height[right]
#         else:
#             water = water + right_max - height[right]

#         right = right - 1

# print("Trapped rainwater:", water)

# 22. Find the median of two sorted arrays in O(log(m+n)) time. 
# a = [1, 3]
# b = [2]

# if len(a) > len(b):
#     a, b = b, a

# m = len(a)
# n = len(b)

# left = 0
# right = m

# while left <= right:

#     i = (left + right) // 2
#     j = (m + n + 1) // 2 - i

#     a_left = float('-inf') if i == 0 else a[i - 1]
#     a_right = float('inf') if i == m else a[i]

#     b_left = float('-inf') if j == 0 else b[j - 1]
#     b_right = float('inf') if j == n else b[j]

#     if a_left <= b_right and b_left <= a_right:

#         if (m + n) % 2 == 0:
#             median = (max(a_left, b_left) +
#                       min(a_right, b_right)) / 2
#         else:
#             median = max(a_left, b_left)

#         break

#     elif a_left > b_right:
#         right = i - 1

#     else:
#         left = i + 1

# print("Median:", median)

# 23. Find the maximum product of a contiguous subarray. 
# numbers = [2, 3, -2, 4]

# max_product = numbers[0]
# min_product = numbers[0]
# result = numbers[0]

# for i in numbers[1:]:
#     if i < 0:
#         max_product, min_product = min_product, max_product

#     max_product = max(i, max_product * i)
#     min_product = min(i, min_product * i)

#     result = max(result, max_product)

# print("Maximum product:", result)


# 24. Find the smallest missing positive integer from an unsorted array. 
# numbers = [3, 4, -1, 1]

# i = 1

# while i in numbers:
#     i = i + 1

# print("Smallest missing positive number:", i)

# 25. Count the number of subarrays whose sum equals K. 
# numbers = [1, 2, 3, 2]
# k = 3

# count = 0

# for i in range(len(numbers)):
#     total = 0

#     for j in range(i, len(numbers)):
#         total = total + numbers[j]

#         if total == k:
#             count = count + 1

# print("Number of subarrays:", count)


# 26. Find the longest increasing subsequence in an array. 
# numbers = [10, 9, 2, 5, 3, 7, 101, 18]

# dp = [1] * len(numbers)

# for i in range(len(numbers)):
#     for j in range(i):
#         if numbers[i] > numbers[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print("Longest increasing subsequence length:", max(dp))

# 27. Solve the Coin Change problem using dynamic programming.
# coins = [1, 2, 5]
# amount = 11

# dp = [amount + 1] * (amount + 1)

# dp[0] = 0

# for i in range(1, amount + 1):
#     for coin in coins:
#         if coin <= i:
#             dp[i] = min(dp[i], dp[i - coin] + 1)

# if dp[amount] > amount:
#     print("Change not possible")
# else:
#     print("Minimum coins required:", dp[amount])

# 28. Solve the Word Break problem using dynamic programming. 
# text = "leetcode"

# words = ["leet", "code"]

# dp = [False] * (len(text) + 1)

# dp[0] = True

# for i in range(1, len(text) + 1):
#     for j in range(i):
#         if dp[j] and text[j:i] in words:
#             dp[i] = True
#             break

# if dp[len(text)]:
#     print("Word Break Possible")
# else:
#     print("Word Break Not Possible")

# 29. Find the minimum number of jumps required to reach the last index.
# numbers = [2, 3, 1, 1, 4]

# jumps = 0
# current_end = 0
# farthest = 0

# for i in range(len(numbers) - 1):

#     farthest = max(farthest, i + numbers[i])

#     if i == current_end:
#         jumps = jumps + 1
#         current_end = farthest

# print("Minimum jumps:", jumps)

# 30. Find the maximum profit from buying and selling stocks with multiple transactions. 
# prices = [7, 1, 5, 3, 6, 4]

# profit = 0

# for i in range(1, len(prices)):
#     if prices[i] > prices[i - 1]:
#         profit = profit + prices[i] - prices[i - 1]

# print("Maximum profit:", profit)

# 31. Implement an LRU Cache with O(1) time complexity for get() and put().
# from collections import OrderedDict

# cache = OrderedDict()

# def get(key):
#     if key not in cache:
#         return -1

#     cache.move_to_end(key)
#     return cache[key]


# def put(key, value):
#     if key in cache:
#         cache.move_to_end(key)

#     cache[key] = value

#     if len(cache) > 3:
#         cache.popitem(last=False)


# put(1, 10)
# put(2, 20)
# put(3, 30)

# print(get(1))

# put(4, 40)

# print(cache)

# 32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1). 
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, val):
#         self.stack.append(val)

#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)

#     def pop(self):
#         val = self.stack.pop()

#         if val == self.min_stack[-1]:
#             self.min_stack.pop()

#     def top(self):
#         return self.stack[-1]

#     def getMin(self):
#         return self.min_stack[-1]


# s = MinStack()

# s.push(5)
# s.push(3)
# s.push(7)

# print("Top:", s.top())
# print("Minimum:", s.getMin())

# s.pop()

# print("Minimum after pop:", s.getMin())

# 33. Find the number of islands in a 2D matrix using DFS or BFS. 
# grid = [
#     [1, 1, 0, 0],
#     [1, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 0, 0, 1]
# ]

# rows = len(grid)
# cols = len(grid[0])

# def dfs(r, c):

#     if r < 0 or r >= rows or c < 0 or c >= cols:
#         return

#     if grid[r][c] == 0:
#         return

#     grid[r][c] = 0

#     dfs(r + 1, c)
#     dfs(r - 1, c)
#     dfs(r, c + 1)
#     dfs(r, c - 1)


# count = 0

# for i in range(rows):
#     for j in range(cols):

#         if grid[i][j] == 1:
#             count += 1
#             dfs(i, j)

# print("Number of islands:", count)


# 34. Find the shortest path in a weighted graph using Dijkstra's algorithm. 
# import heapq

# graph = {
#     'A': [('B', 4), ('C', 2)],
#     'B': [('A', 4), ('C', 1), ('D', 5)],
#     'C': [('A', 2), ('B', 1), ('D', 8)],
#     'D': [('B', 5), ('C', 8)]
# }

# distance = {node: float('inf') for node in graph}

# distance['A'] = 0

# queue = [(0, 'A')]

# while queue:
#     dist, node = heapq.heappop(queue)

#     if dist > distance[node]:
#         continue

#     for neighbour, weight in graph[node]:
#         new_dist = dist + weight

#         if new_dist < distance[neighbour]:
#             distance[neighbour] = new_dist
#             heapq.heappush(queue, (new_dist, neighbour))

# print("Shortest distances:", distance)


# 35. Detect a cycle in a directed and undirected graph
# graph = {
#     0: [1, 2],
#     1: [0, 2],
#     2: [0, 1]
# }

# visited = set()

# def dfs(node, parent):

#     visited.add(node)

#     for neighbour in graph[node]:

#         if neighbour not in visited:
#             if dfs(neighbour, node):
#                 return True

#         elif neighbour != parent:
#             return True

#     return False


# if dfs(0, -1):
#     print("Cycle detected")
# else:
#     print("No cycle")

# 36. Implement topological sorting for a directed acyclic graph. 
# a.
# graph = {
#     0: [1, 2],
#     1: [0, 2],
#     2: [0, 1]
# }

# visited = set()

# def dfs(node, parent):

#     visited.add(node)

#     for neighbour in graph[node]:

#         if neighbour not in visited:
#             if dfs(neighbour, node):
#                 return True

#         elif neighbour != parent:
#             return True

#     return False


# if dfs(0, -1):
#     print("Cycle detected")
# else:
#     print("No cycle")
    
# b.
# graph = {
#     0: [1],
#     1: [2],
#     2: [0]
# }

# visited = set()
# path = set()

# def dfs(node):

#     visited.add(node)
#     path.add(node)

#     for neighbour in graph[node]:

#         if neighbour not in visited:
#             if dfs(neighbour):
#                 return True

#         elif neighbour in path:
#             return True

#     path.remove(node)
#     return False


# cycle = False

# for node in graph:
#     if node not in visited:
#         if dfs(node):
#             cycle = True
#             break

# if cycle:
#     print("Cycle detected")
# else:
#     print("No cycle")

# 37. Solve the N-Queens problem using backtracking.
# n = 4

# board = [["." for j in range(n)] for i in range(n)]

# def safe(row, col):

#     for i in range(row):
#         if board[i][col] == "Q":
#             return False

#     i = row - 1
#     j = col - 1

#     while i >= 0 and j >= 0:
#         if board[i][j] == "Q":
#             return False
#         i -= 1
#         j -= 1

#     i = row - 1
#     j = col + 1

#     while i >= 0 and j < n:
#         if board[i][j] == "Q":
#             return False
#         i -= 1
#         j += 1

#     return True


# def solve(row):

#     if row == n:
#         for r in board:
#             print(" ".join(r))
#         return True

#     for col in range(n):

#         if safe(row, col):
#             board[row][col] = "Q"

#             if solve(row + 1):
#                 return True

#             board[row][col] = "."

#     return False


# solve(0)


# 38. Generate all permutations of a given string or array without duplicates.
# def permutations(text):

#     if len(text) == 0:
#         return [""]

#     result = []

#     for i in range(len(text)):

#         if text[i] in text[:i]:
#             continue

#         remaining = text[:i] + text[i+1:]

#         for p in permutations(remaining):
#             result.append(text[i] + p)

#     return result


# text = "AAB"

# print("Permutations:", permutations(text))

# 39. Serialize and deserialize a binary tree. 
# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def serialize(root):

#     if not root:
#         return []

#     result = []
#     queue = deque([root])

#     while queue:
#         node = queue.popleft()

#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)

#     while result and result[-1] is None:
#         result.pop()

#     return result


# def deserialize(data):

#     if not data:
#         return None

#     root = Node(data[0])
#     queue = deque([root])
#     i = 1

#     while queue and i < len(data):

#         node = queue.popleft()

#         if i < len(data) and data[i] is not None:
#             node.left = Node(data[i])
#             queue.append(node.left)
#         i += 1

#         if i < len(data) and data[i] is not None:
#             node.right = Node(data[i])
#             queue.append(node.right)
#         i += 1

#     return root


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

# data = serialize(root)

# print("Serialized tree:", data)

# new_root = deserialize(data)

# print("Deserialized root:", new_root.val)


# 40. Find the lowest common ancestor of two nodes in a binary tree. 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca(root, p, q):

    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    if left:
        return left

    return right


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print("Lowest Common Ancestor:", lca(root, 4, 5).val)