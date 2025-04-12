# ============================================================
# পাইথন বেসিক থেকে অ্যাডভান্সড (Python Basic to Advanced)
# ============================================================

# ============================================================
# ১. বেসিক সিনট্যাক্স (Basic Syntax)
# ============================================================

# ভেরিয়েবল (Variables)
# পাইথন: snake_case ব্যবহার করে - পাইথনে আমরা ভেরিয়েবল ডিক্লেয়ার করার সময় কোন কিওয়ার্ড ব্যবহার করি না
user_name = "John"  # স্ট্রিং ভেরিয়েবল
age = 25            # ইন্টিজার ভেরিয়েবল
salary = 50000.50   # ফ্লোট ভেরিয়েবল

# জাভাস্ক্রিপ্ট: camelCase ব্যবহার করে এবং let/const/var কিওয়ার্ড ব্যবহার করে
# let userName = "John";
# const age = 25;
# let salary = 50000.50;

# ডাটা টাইপস (Data Types)
# পাইথনে ডাটা টাইপ অটোমেটিক্যালি ডিটেক্ট হয়, টাইপ অ্যানোটেশন অপশনাল
text = "Hello"       # স্ট্রিং (String) - টেক্সট ডাটা
number = 42          # ইন্টিজার (Integer) - পূর্ণসংখ্যা
pi = 3.14            # ফ্লোট (Float) - দশমিক সংখ্যা
is_valid = True      # বুলিয়ান (Boolean) - সত্য/মিথ্যা
my_list = [1, 2, 3]  # লিস্ট (List) - অর্ডার্ড কালেকশন (জাভাস্ক্রিপ্টের অ্যারে)
my_tuple = (1, 2, 3) # টাপল (Tuple) - ইমিউটেবল অর্ডার্ড কালেকশন
my_dict = {"name": "John", "age": 25}  # ডিকশনারি (Dictionary) - কী-ভ্যালু পেয়ার (জাভাস্ক্রিপ্টের অবজেক্ট)
my_set = {1, 2, 3}   # সেট (Set) - ইউনিক আইটেমের কালেকশন

# টাইপ চেক করা
print(type(text))    # <class 'str'>
print(type(number))  # <class 'int'>
print(type(my_dict)) # <class 'dict'>

# জাভাস্ক্রিপ্ট:
# const text = "Hello";
# const number = 42;
# const pi = 3.14;
# const isValid = true;
# const myArray = [1, 2, 3];
# const myObject = {name: "John", age: 25};
# const mySet = new Set([1, 2, 3]);
# console.log(typeof text);    // "string"
# console.log(typeof number);  // "number"
# console.log(typeof myObject); // "object"

# অপারেটরস (Operators)
x = 10
y = 3
sum = x + y      # যোগ (Addition)
diff = x - y     # বিয়োগ (Subtraction)
prod = x * y     # গুণ (Multiplication)
div = x / y      # ভাগ (Division) - পাইথনে এটি সবসময় ফ্লোট রিটার্ন করে
floor_div = x // y  # ফ্লোর ডিভিশন - পূর্ণসংখ্যা ভাগফল
mod = x % y      # মডুলাস (Modulus) - ভাগশেষ
power = x ** y   # এক্সপোনেনশিয়েশন (x^y)

# কম্পারিজন অপারেটর
print(x == y)    # সমান কিনা (Equality)
print(x != y)    # সমান নয় কিনা (Inequality)
print(x > y)     # বড় কিনা (Greater than)
print(x >= y)    # বড় বা সমান কিনা (Greater than or equal)
print(x < y)     # ছোট কিনা (Less than)
print(x <= y)    # ছোট বা সমান কিনা (Less than or equal)

# লজিকাল অপারেটর
a = True
b = False
print(a and b)   # লজিকাল AND - দুটোই সত্য হলে সত্য
print(a or b)    # লজিকাল OR - যেকোনো একটি সত্য হলে সত্য
print(not a)     # লজিকাল NOT - বিপরীত মান

# ইনপুট/আউটপুট (Input/Output)
name = input("Enter your name: ")  # ইনপুট নেওয়া - সবসময় স্ট্রিং হিসেবে রিটার্ন করে
age = int(input("Enter your age: "))  # স্ট্রিং থেকে ইন্টিজারে কনভার্ট করা
print(f"Hello, {name}! You are {age} years old.")  # f-string ফরম্যাটিং (Python 3.6+)
print("Hello, {}! You are {} years old.".format(name, age))  # .format() মেথড

# জাভাস্ক্রিপ্ট:
# const name = prompt("Enter your name:");
# const age = parseInt(prompt("Enter your age:"));
# console.log(`Hello, ${name}! You are ${age} years old.`);

# ============================================================
# ২. কন্ট্রোল স্ট্রাকচার (Control Structures)
# ============================================================

# কন্ডিশনাল স্টেটমেন্টস (Conditional Statements)
# if-elif-else স্টেটমেন্ট - পাইথনে ইন্ডেন্টেশন (স্পেস) দিয়ে ব্লক নির্ধারণ করা হয়
age = 18
if age >= 18:  # যদি শর্ত সত্য হয়
    print("Adult")
elif age >= 13:  # অন্যথায় যদি এই শর্ত সত্য হয়
    print("Teenager")
else:  # অন্যথায়
    print("Child")

# জাভাস্ক্রিপ্ট: কার্লি ব্রেসেস {} দিয়ে ব্লক নির্ধারণ করা হয়
# if (age >= 18) {
#     console.log("Adult");
# } else if (age >= 13) {
#     console.log("Teenager");
# } else {
#     console.log("Child");
# }

# টার্নারি অপারেটর (Ternary Operator)
status = "Adult" if age >= 18 else "Minor"  # একলাইনে কন্ডিশন চেক

# জাভাস্ক্রিপ্ট:
# const status = age >= 18 ? "Adult" : "Minor";

# লুপস (Loops)

# ফর লুপ (For Loop)
for i in range(5):  # 0 থেকে 4 পর্যন্ত লুপ চালায়
    print(i)

# range() ফাংশনের বিভিন্ন ব্যবহার
for i in range(2, 5):  # 2 থেকে 4 পর্যন্ত (2, 3, 4)
    print(i)

for i in range(1, 10, 2):  # 1 থেকে 9 পর্যন্ত, 2 ধাপে (1, 3, 5, 7, 9)
    print(i)

# লিস্ট/অ্যারে নিয়ে লুপ
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # লিস্টের প্রতিটি আইটেম নিয়ে লুপ
    print(fruit)

# জাভাস্ক্রিপ্ট:
# for (let i = 0; i < 5; i++) {
#     console.log(i);
# }
#
# লিস্ট/অ্যারে নিয়ে লুপ
# const fruits = ["apple", "banana", "cherry"];
# for (const fruit of fruits) {
#     console.log(fruit);
# }

# হোয়াইল লুপ (While Loop)
count = 0
while count < 3:  # যতক্ষণ শর্ত সত্য থাকে ততক্ষণ লুপ চলবে
    print(count)
    count += 1  # কাউন্টার বাড়ানো

# জাভাস্ক্রিপ্ট:
# let count = 0;
# while (count < 3) {
#     console.log(count);
#     count++;
# }

# ব্রেক এবং কন্টিনিউ (Break and Continue)
for i in range(10):
    if i == 3:
        continue  # 3 এর জন্য লুপের বাকি অংশ স্কিপ করে পরবর্তী ইটারেশনে যাবে
    if i == 7:
        break  # 7 এ পৌঁছালে লুপ থেকে বেরিয়ে যাবে
    print(i)  # আউটপুট: 0, 1, 2, 4, 5, 6

# জাভাস্ক্রিপ্ট:
# for (let i = 0; i < 10; i++) {
#     if (i === 3) {
#         continue;
#     }
#     if (i === 7) {
#         break;
#     }
#     console.log(i);
# }

# ফাংশনস (Functions)

# রেগুলার ফাংশন (Regular Function)
def greet(name):
    return f"Hello, {name}!"
# জাভাস্ক্রিপ্ট:
# function greet(name) {
#     return `Hello, ${name}!`;
# }

# ল্যাম্বডা ফাংশন (Lambda Function)
square = lambda x: x * x
# জাভাস্ক্রিপ্ট:
# const square = x => x * x;

# অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং (Object-Oriented Programming)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I am {self.name}, {self.age} years old"
# জাভাস্ক্রিপ্ট:
# class Person {
#     constructor(name, age) {
#         this.name = name;
#         this.age = age;
#     }
#
#     introduce() {
#         return `I am ${this.name}, ${this.age} years old`;
#     }
# }

# ইনহেরিটেন্স (Inheritance)
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
# জাভাস্ক্রিপ্ট:
# class Student extends Person {
#     constructor(name, age, grade) {
#         super(name, age);
#         this.grade = grade;
#     }
# }

# এডভান্সড টপিকস (Advanced Topics)

# ডেকোরেটর (Decorator)
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# থ্রেডিং (Threading)
import threading

def print_numbers():
    for i in range(5):
        print(f"Number {i}")

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter {letter}")

# থ্রেড তৈরি ও চালু করা
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# কনটেক্সট ম্যানেজার (Context Manager)
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# মেটাক্লাস (Metaclass)
class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # সব মেথড আপারকেসে রূপান্তর
        uppercase_attrs = {
            key.upper(): value
            for key, value in attrs.items()
            if not key.startswith('__')
        }
        return super().__new__(cls, name, bases, uppercase_attrs)

# প্রবলেম সলভিং (Problem Solving)

# ১. ফিবোনাচ্চি সিরিজ (Fibonacci Series)
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# ২. বাইনারি সার্চ (Binary Search)
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

# ৩. বাবল সর্ট (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ৪. প্যালিনড্রোম চেক (Palindrome Check)
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# ডিজাইন প্যাটার্ন (Design Patterns)

# ১. সিঙ্গেলটন প্যাটার্ন (Singleton Pattern)
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# ২. ফ্যাক্টরি প্যাটার্ন (Factory Pattern)
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()

# জেনারেটর (Generator)
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1