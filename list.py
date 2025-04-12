# পাইথন লিস্ট মেথডস এবং ম্যানিপুলেশন (Python List Methods and Manipulation)

# ১. লিস্ট তৈরি (List Creation)
fruits = ["আপেল", "কলা", "আম"]  # সাধারণ লিস্ট
numbers = list(range(1, 6))     # রেঞ্জ থেকে লিস্ট: [1, 2, 3, 4, 5]
mixed = [1, "দুই", 3.0, True]    # মিক্সড টাইপের লিস্ট

# ২. লিস্টে এলিমেন্ট যোগ করা (Adding Elements)

# append() - লিস্টের শেষে একটি এলিমেন্ট যোগ করে
fruits.append("আঙ্গুর")
print("append() পরে:", fruits)  # ['আপেল', 'কলা', 'আম', 'আঙ্গুর']

# insert() - নির্দিষ্ট পজিশনে এলিমেন্ট যোগ করে
fruits.insert(1, "কমলা")
print("insert() পরে:", fruits)  # ['আপেল', 'কমলা', 'কলা', 'আম', 'আঙ্গুর']

# extend() - একটি লিস্টের সাথে আরেকটি লিস্ট যোগ করে
more_fruits = ["লিচু", "পেয়ারা"]
fruits.extend(more_fruits)
print("extend() পরে:", fruits)  # ['আপেল', 'কমলা', 'কলা', 'আম', 'আঙ্গুর', 'লিচু', 'পেয়ারা']

# ৩. লিস্ট থেকে এলিমেন্ট রিমুভ করা (Removing Elements)

# remove() - নির্দিষ্ট এলিমেন্ট রিমুভ করে
fruits.remove("কমলা")
print("remove() পরে:", fruits)  # ['আপেল', 'কলা', 'আম', 'আঙ্গুর', 'লিচু', 'পেয়ারা']

# pop() - নির্দিষ্ট ইনডেক্সের এলিমেন্ট রিমুভ করে এবং রিটার্ন করে
removed_fruit = fruits.pop(1)  # 'কলা' রিমুভ করা হবে
print("pop() পরে:", fruits)    # ['আপেল', 'আম', 'আঙ্গুর', 'লিচু', 'পেয়ারা']

# clear() - পুরো লিস্ট খালি করে দেয়
temp_list = [1, 2, 3]
temp_list.clear()
print("clear() পরে:", temp_list)  # []

# ৪. লিস্ট সার্চিং (List Searching)

# index() - এলিমেন্টের পজিশন খোঁজে
print("'আম' এর পজিশন:", fruits.index("আম"))

# count() - একটি এলিমেন্ট কতবার আছে তা গণনা করে
repeated_list = [1, 2, 2, 3, 2, 4]
print("2 সংখ্যাটি আছে:", repeated_list.count(2), "বার")

# in অপারেটর - এলিমেন্ট আছে কিনা চেক করে
print("'আপেল' আছে কি:", "আপেল" in fruits)

# ৫. লিস্ট সর্টিং (List Sorting)

# sort() - লিস্টকে সর্ট করে (মূল লিস্ট পরিবর্তন করে)
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nums.sort()
print("sort() পরে:", nums)

# reverse() - লিস্টকে উল্টো করে
nums.reverse()
print("reverse() পরে:", nums)

# sorted() - নতুন সর্টেড লিস্ট রিটার্ন করে (মূল লিস্ট অপরিবর্তিত থাকে)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print("Original:", original)
print("Sorted:", sorted_list)

# ৬. লিস্ট স্লাইসিং (List Slicing)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("প্রথম তিনটি:", letters[:3])    # ['a', 'b', 'c']
print("শেষ তিনটি:", letters[-3:])    # ['e', 'f', 'g']
print("মাঝের তিনটি:", letters[2:5])  # ['c', 'd', 'e']

# ৭. লিস্ট কমপ্রিহেনশন (List Comprehension)

# সাধারণ লিস্ট কমপ্রিহেনশন
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# কন্ডিশনাল লিস্ট কমপ্রিহেনশন
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

# নেস্টেড লিস্ট কমপ্রিহেনশন
matrix = [[i+j for j in range(3)] for i in range(3)]

# ৮. লিস্ট অপারেশনস (List Operations)

# কপি করা
list1 = [1, 2, 3]
list2 = list1.copy()  # শ্যালো কপি
list3 = list1[:]      # স্লাইস কপি

# লিস্ট জয়েন করা
list4 = [4, 5, 6]
combined = list1 + list4  # [1, 2, 3, 4, 5, 6]

# লিস্ট রিপিটিশন
repeated = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# ৯. লিস্টের লেনথ (List Length)
print("ফলের লিস্টের দৈর্ঘ্য:", len(fruits))

# ১০. লিস্ট ম্যাপিং এবং ফিল্টারিং (List Mapping and Filtering)

# ম্যাপ ফাংশন
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x*2, numbers))  # [2, 4, 6, 8, 10]

# ফিল্টার ফাংশন
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# ১১. নেস্টেড লিস্ট (Nested Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# নেস্টেড লিস্ট অ্যাক্সেস
print("ম্যাট্রিক্সের দ্বিতীয় রো:", matrix[1])      # [4, 5, 6]
print("ম্যাট্রিক্সের (1,1) এলিমেন্ট:", matrix[1][1])  # 5

# ১২. লিস্ট পারফরম্যান্স টিপস (List Performance Tips)

# append() vs. insert(): append() বেশি দক্ষ কারণ এটি শেষে যোগ করে
# remove() vs. pop(): pop() বেশি দক্ষ কারণ এটি ইনডেক্স ব্যবহার করে
# in অপারেটর: বড় লিস্টের জন্য set() ব্যবহার করা বেশি দক্ষ
# লিস্ট কমপ্রিহেনশন: for লুপের চেয়ে বেশি দক্ষ এবং পঠনযোগ্য

# ১৩. সার্চিং অ্যালগরিদম (Searching Algorithms)

# লিনিয়ার সার্চ (Linear Search) - O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# বাইনারি সার্চ (Binary Search) - O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ১৪. সর্টিং অ্যালগরিদম (Sorting Algorithms)

# বাবল সর্ট (Bubble Sort) - O(n²)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# কুইক সর্ট (Quick Sort) - O(n log n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# মার্জ সর্ট (Merge Sort) - O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ১৫. ডাইনামিক প্রোগ্রামিং (Dynamic Programming)

# ফিবোনাচ্চি সিরিজ (Fibonacci Series) - O(n)
def fibonacci_dp(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0] * n
    fib[1] = 1
    
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib

# LCS (Longest Common Subsequence) - O(mn)
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# ১৬. গ্রাফ অ্যালগরিদম (Graph Algorithms)

# BFS (Breadth First Search) - O(V + E)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return result

# DFS (Depth First Search) - O(V + E)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# ১৭. ট্রি অ্যালগরিদম (Tree Algorithms)

# বাইনারি সার্চ ট্রি (Binary Search Tree)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node:
            result.extend(self.inorder_traversal(node.left))
            result.append(node.value)
            result.extend(self.inorder_traversal(node.right))
        return result

# ১৮. অ্যাডভান্সড লিস্ট অপারেশনস (Advanced List Operations)

# স্লাইডিং উইন্ডো (Sliding Window)
def sliding_window_max(arr, k):
    if not arr or k <= 0:
        return []
    
    n = len(arr)
    result = []
    window = deque()
    
    for i in range(n):
        while window and window[0] < i - k + 1:
            window.popleft()
        
        while window and arr[window[-1]] < arr[i]:
            window.pop()
        
        window.append(i)
        
        if i >= k - 1:
            result.append(arr[window[0]])
    
    return result

# টু পয়েন্টার টেকনিক (Two Pointer Technique)
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# ১৯. প্র্যাকটিক্যাল এক্সাম্পল (Practical Examples)

# ১. ডুপ্লিকেট এলিমেন্ট খোঁজা
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

# ২. সাবঅ্যারে সাম
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# ৩. ম্যাট্রিক্স রোটেশন
def rotate_matrix(matrix):
    n = len(matrix)
    # ট্রান্সপোজ
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # প্রতিটি রো রিভার্স
    for i in range(n):
        matrix[i].reverse()
    return matrix