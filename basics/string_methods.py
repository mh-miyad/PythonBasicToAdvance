# স্ট্রিং মেথডস (String Methods)
# পাইথনে সবচেয়ে বেশি ব্যবহৃত স্ট্রিং মেথডস

# ১. স্ট্রিং ম্যানিপুলেশন (String Manipulation)

# কেস চেঞ্জিং (Case Changing)
text = "Hello, World!"
print(text.upper())      # সব অক্ষর আপারকেসে: HELLO, WORLD!
print(text.lower())      # সব অক্ষর লোয়ারকেসে: hello, world!
print(text.title())      # প্রতিটি শব্দের প্রথম অক্ষর ক্যাপিটাল: Hello, World!
print(text.capitalize()) # শুধু প্রথম অক্ষর ক্যাপিটাল: Hello, world!

# স্ট্রিং স্প্লিটিং এবং জয়েনিং (String Splitting and Joining)
words = "Python,Java,JavaScript"
word_list = words.split(",")  # কমা দিয়ে স্প্লিট: ['Python', 'Java', 'JavaScript']
print("-".join(word_list))     # হাইফেন দিয়ে জয়েন: Python-Java-JavaScript

# স্ট্রিং সার্চিং (String Searching)
sentence = "Python is amazing and Python is powerful"
print(sentence.count("Python"))    # Python শব্দটি কতবার আছে: 2
print(sentence.find("Python"))     # Python শব্দটির প্রথম পজিশন: 0
print(sentence.rfind("Python"))    # Python শব্দটির শেষ পজিশন: 23

# স্ট্রিং রিপ্লেসমেন্ট (String Replacement)
old_text = "I like Java"
print(old_text.replace("Java", "Python"))  # Java কে Python দিয়ে রিপ্লেস: I like Python

# স্ট্রিং চেকিং (String Checking)
num_str = "12345"
text_str = "Hello"
space_str = "   "

print(num_str.isdigit())    # সব অক্ষর কি ডিজিট: True
print(text_str.isalpha())   # সব অক্ষর কি আলফাবেট: True
print(space_str.isspace())  # শুধু স্পেস আছে কিনা: True

# হোয়াইটস্পেস হ্যান্ডলিং (Whitespace Handling)
text_with_space = "   Hello World   "
print(text_with_space.strip())      # উভয় দিক থেকে স্পেস রিমুভ: "Hello World"
print(text_with_space.lstrip())     # বাম দিক থেকে স্পেস রিমুভ: "Hello World   "
print(text_with_space.rstrip())     # ডান দিক থেকে স্পেস রিমুভ: "   Hello World"

# স্ট্রিং ফরম্যাটিং (String Formatting)

# ১. f-string (Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")

# ২. format() মেথড
print("My name is {} and I am {} years old".format(name, age))

# ৩. % অপারেটর
print("My name is %s and I am %d years old" % (name, age))

# স্ট্রিং প্যাডিং (String Padding)
num = "42"
print(num.zfill(5))        # জিরো প্যাডিং: 00042
print(num.ljust(5, "*"))   # বাম দিকে প্যাডিং: 42***
print(num.rjust(5, "*"))   # ডান দিকে প্যাডিং: ***42
print(num.center(5, "*"))  # মাঝখানে এলাইন: *42**

# স্ট্রিং এনকোডিং/ডিকোডিং (String Encoding/Decoding)
text = "Hello, 世界"
encoded = text.encode("utf-8")    # UTF-8 এনকোডিং
print(encoded)
print(encoded.decode("utf-8"))    # UTF-8 ডিকোডিং

# রেগুলার এক্সপ্রেশন সাপোর্ট (Regular Expression Support)
import re

text = "My email is example@email.com and phone is 123-456-7890"

# ইমেইল খোঁজা
email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
if email:
    print(f"Found email: {email.group()}")

# ফোন নাম্বার খোঁজা
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
if phone:
    print(f"Found phone: {phone.group()}")

# স্ট্রিং স্লাইসিং (String Slicing)
text = "Python Programming"
print(text[0:6])       # প্রথম ৬টি অক্ষর: Python
print(text[-11:])      # শেষের ১১টি অক্ষর: Programming
print(text[::-1])      # উল্টো করা: gnimmargorP nohtyP

# মাল্টিলাইন স্ট্রিং (Multiline String)
multiline = """This is a
    multiline string
    example."""
print(multiline)

# স্ট্রিং কম্পারিজন (String Comparison)
str1 = "hello"
str2 = "Hello"
print(str1 == str2)            # কেস সেনসিটিভ কম্পারিজন: False
print(str1.lower() == str2.lower())  # কেস ইনসেনসিটিভ কম্পারিজন: True

# স্ট্রিং ভ্যালিডেশন (String Validation)
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# টেস্ট কেস
print(is_valid_email("example@email.com"))  # True
print(is_valid_email("invalid.email"))      # False