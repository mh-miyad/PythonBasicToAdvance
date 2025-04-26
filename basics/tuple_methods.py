# টাপল মেথডস (Tuple Methods)
# পাইথনে টাপলের বৈশিষ্ট্য এবং মেথডসমূহ

# ১. বেসিক অপারেশনস (Basic Operations)
my_tuple = (1, 2, 3, 2, 4)

# কাউন্ট মেথড (Count Method)
print(my_tuple.count(2))  # 2 রিটার্ন করবে
# জাভাস্ক্রিপ্ট: Array.prototype.filter() ব্যবহার করে
# const count = arr.filter(x => x === 2).length;

# ইনডেক্স মেথড (Index Method)
print(my_tuple.index(3))  # 2 রিটার্ন করবে

# ২. ইমিউটেবিলিটি ডেমো (Immutability Demo)
try:
    my_tuple[0] = 5  # এরর হবে কারণ টাপল মডিফাই করা যায় না
except TypeError as e:
    print("Error:", e)

# ৩. টাপল আনপ্যাকিং (Tuple Unpacking)
a, b, c, d, e = my_tuple
print(f"a={a}, b={b}, c={c}")  # a=1, b=2, c=3

# ৪. টাপল কনকাটেনেশন (Tuple Concatenation)
new_tuple = my_tuple + (5, 6)
print(new_tuple)  # (1, 2, 3, 2, 4, 5, 6)

# ৫. টাপল কনভার্শন (Tuple Conversion)
my_list = [7, 8, 9]
tuple_from_list = tuple(my_list)
print(tuple_from_list)  # (7, 8, 9)

# ৬. প্র্যাকটিক্যাল ইউস কেস (Practical Use Cases)
# স্থানাঙ্ক সিস্টেম
coordinates = (23.8103, 90.4125)
latitude, longitude = coordinates
print(f"Lat: {latitude}, Long: {longitude}")

# ফাংশন থেকে মাল্টিপল রিটার্ন ভ্যালু
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

stats = get_stats((10, 20, 30))
print(f"Min: {stats[0]}, Max: {stats[1]}, Avg: {stats[2]}")