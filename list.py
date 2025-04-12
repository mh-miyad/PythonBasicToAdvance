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