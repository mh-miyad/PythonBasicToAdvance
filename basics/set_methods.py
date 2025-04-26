# সেট মেথডস (Set Methods)
# পাইথনে সেট অপারেশন এবং মেথডসমূহ

# ১. বেসিক অপারেশনস (Basic Operations)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# ইউনিয়ন (Union)
print(set_a | set_b)  # {1, 2, 3, 4, 5, 6}
# জাভাস্ক্রিপ্ট: new Set([...setA, ...setB])

# ইন্টারসেকশন (Intersection)
print(set_a & set_b)  # {3, 4}

# ডিফারেন্স (Difference)
print(set_a - set_b)  # {1, 2}

# সিমেট্রিক ডিফারেন্স (Symmetric Difference)
print(set_a ^ set_b)  # {1, 2, 5, 6}

# ২. কমন মেথডস (Common Methods)
my_set = {1, 2, 3}

# অ্যাড মেথড (Add Method)
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# রিমুভ vs ডিসকার্ড (Remove vs Discard)
my_set.remove(3)    # এলিমেন্ট না থাকলে এরর
my_set.discard(5)   # এলিমেন্ট না থাকলে এরর না

# পপ মেথড (Pop Method)
popped = my_set.pop()
print(f"Popped: {popped}, Remaining: {my_set}")

# ৩. সাবসেট/সুপারসেট চেক (Subset/Superset Check)
print({1, 2}.issubset(set_a))    # True
print(set_a.issuperset({1, 2}))  # True

# ৪. প্র্যাকটিক্যাল ইউস কেস (Practical Use Cases)
# ইউনিক এলিমেন্ট ফিল্টারিং
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(f"Unique numbers: {unique}")

# ভোটার আইডি চেকিং
registered_voters = {101, 102, 103, 104}
current_voters = {102, 103, 105}
invalid_voters = current_voters - registered_voters
print(f"Invalid voter IDs: {invalid_voters}")

# ৫. ফ্রোজেনসেট (FrozenSet)
immutable_set = frozenset([1, 2, 3])
try:
    immutable_set.add(4)
except AttributeError as e:
    print(f"Error: {e}")

# ৬. জাভাস্ক্রিপ্ট কম্পেরিজন (JavaScript Comparison)
# জাভাস্ক্রিপ্ট সেট
# const setA = new Set([1, 2, 3]);
# const setB = new Set([3, 4, 5]);
# নতুন সেট তৈরি: new Set([...setA].filter(x => x > 2));
# ইউনিয়ন: new Set([...setA, ...setB])
# ইন্টারসেকশন: new Set([...setA].filter(x => setB.has(x)));