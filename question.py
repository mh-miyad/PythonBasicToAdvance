# ============================================================
# পাইথন প্র্যাকটিস প্রশ্নাবলী (Python Practice Questions)
# ============================================================

# ১. বেসিক ভেরিয়েবল ও স্ট্রিং (Basic Variables and Strings)
# একটি ফাংশন লিখুন যা ব্যবহারকারীর নাম নিয়ে "Hello, [name]!" ফরম্যাটে রিটার্ন করবে।
# এবং নামের প্রথম অক্ষর বড় হাতের হবে, বাকি অক্ষরগুলো ছোট হাতের হবে।
# উদাহরণ: "john" -> "Hello, John!"
# JavaScript এ এটি করতে হলে: const greet = (name) => `Hello, ${name.charAt(0).toUpperCase() + name.slice(1).toLowerCase()}!`;
def greet(name):
    return f"hi {name} Welcome to My Python Practice Class"
# print(greet("John"))
# ২. লিস্ট ম্যানিপুলেশন (List Manipulation)
# একটি ফাংশন লিখুন যা একটি সংখ্যার লিস্ট নিয়ে শুধুমাত্র জোড় সংখ্যাগুলো ফিল্টার করে একটি নতুন লিস্ট রিটার্ন করবে।
# উদাহরণ: [1, 2, 3, 4, 5, 6] -> [2, 4, 6]
# JavaScript এ এটি করতে হলে: const getEvenNumbers = (numbers) => numbers.filter(num => num % 2 === 0);

arr = [1, 2, 3, 4, 5, 6]
def getEvenNumbers(arr):
    even_numbers = []
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
print(getEvenNumbers(arr))


# ৩. ডিকশনারি ব্যবহার (Dictionary Usage)
# একটি ফাংশন লিখুন যা একটি বাক্য নিয়ে প্রতিটি শব্দের কতবার উপস্থিত হয়েছে তা গণনা করে একটি ডিকশনারি রিটার্ন করবে।
# উদাহরণ: "I love Python because Python is fun" -> {"I": 1, "love": 1, "Python": 2, "because": 1, "is": 1, "fun": 1}
# JavaScript এ এটি করতে হলে: const wordCount = (sentence) => sentence.split(' ').reduce((acc, word) => ({...acc, [word]: (acc[word] || 0) + 1}), {});

def word_count(sentence):
    word_dict = {}
    for word in sentence.split():
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

# print(word_count("I love Python because Python is fun"))
# ৪. ফাইল হ্যান্ডলিং (File Handling)
# একটি ফাংশন লিখুন যা একটি টেক্সট ফাইল পড়বে এবং সেই ফাইলে কতটি লাইন, কতটি শব্দ এবং কতটি অক্ষর আছে তা গণনা করে রিটার্ন করবে।
# উদাহরণ: "hello.txt" -> {"lines": 3, "words": 10, "characters": 50}
# JavaScript এ এটি করতে হলে: const fileStats = (filename) => {
#   const content = fs.readFileSync(filename, 'utf-8');
#   return {
#     lines: content.split('\n').length,
#     words: content.split(/\s+/).length,
#     characters: content.length
#   };
# };

def file_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return {
        "lines": len(content.splitlines()),
        "words": len(content.split()),
        "characters": len(content)
    }

# print(file_stats("hello.txt"))


# ৫. এক্সেপশন হ্যান্ডলিং (Exception Handling)
# একটি ফাংশন লিখুন যা দুটি সংখ্যা নিয়ে ভাগ করবে, কিন্তু শূন্য দিয়ে ভাগ করার সময় একটি উপযুক্ত এরর মেসেজ দেখাবে।
# try-except ব্লক ব্যবহার করুন।
# উদাহরণ: divide(10, 2) -> 5, divide(10, 0) -> "Error: Division by zero is not allowed"
# JavaScript এ এটি করতে হলে: const divide = (a, b) => { try {...} catch (error) { return error.message; } };

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

# print(divide(10, 2))  # 5.0
# print(divide(10, 0))  # Error message


# ৬. ক্লাস ও অবজেক্ট (Classes and Objects)
# একটি "BankAccount" ক্লাস তৈরি করুন যেখানে অ্যাকাউন্ট নম্বর, অ্যাকাউন্ট হোল্ডারের নাম এবং ব্যালেন্স থাকবে।
# deposit() ও withdraw() মেথড যোগ করুন যা ব্যালেন্স আপডেট করবে।
# withdraw() মেথডে চেক করুন যে উত্তোলনের পরিমাণ ব্যালেন্সের চেয়ে বেশি কিনা।
# JavaScript এ এটি করতে হলে: class BankAccount { constructor() { ... } }

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return amount

# টেস্ট কেস
# account = BankAccount("123456", "Rahim")
# account.deposit(1000)
# account.withdraw(500)
# print(account.balance)  # 500


# ৭. ইনহেরিটেন্স (Inheritance)
# "Vehicle" নামে একটি বেস ক্লাস তৈরি করুন এবং "Car" ও "Motorcycle" নামে দুটি সাবক্লাস তৈরি করুন।
# Vehicle ক্লাসে make, model, year প্রোপার্টি এবং একটি display_info() মেথড থাকবে।
# Car ও Motorcycle ক্লাসে নিজস্ব প্রোপার্টি এবং মেথড যোগ করুন এবং display_info() মেথড ওভাররাইড করুন।
# JavaScript এ এটি করতে হলে: class Car extends Vehicle { ... }

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()} with {self.doors} doors"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def display_info(self):
        return f"{super().display_info()} ({self.engine_size}cc)"

# টেস্ট কেস
# car = Car("Toyota", "Corolla", 2020, 4)
# print(car.display_info())  # 2020 Toyota Corolla with 4 doors
# bike = Motorcycle("Honda", "CBR500R", 2021, 500)
# print(bike.display_info())  # 2021 Honda CBR500R (500cc)


# ৮. ডেকোরেটর (Decorators)
# একটি টাইমিং ডেকোরেটর তৈরি করুন যা কোন ফাংশন কতক্ষণ সময় নিয়ে এক্সিকিউট হয় তা মাপবে এবং প্রিন্ট করবে।
# এই ডেকোরেটর ব্যবহার করে fibonacci সিরিজ জেনারেট করার একটি ফাংশন লিখুন।
# JavaScript এ এটি করতে হলে: const timerDecorator = (fn) => { ... };

import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# টেস্ট কেস
# list(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ৯. জেনারেটর (Generators)
# একটি জেনারেটর ফাংশন লিখুন যা প্রাইম নাম্বার জেনারেট করবে।
# ব্যবহারকারী যত সংখ্যক প্রাইম নাম্বার চায় তা জেনারেট করতে হবে।
# উদাহরণ: list(generate_primes(5)) -> [2, 3, 5, 7, 11]
# JavaScript এ এটি করতে হলে: function* generatePrimes(count) { ... }

def generate_primes(count):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    num = 2
    found = 0
    while found < count:
        if is_prime(num):
            yield num
            found += 1
        num += 1

# টেস্ট কেস
# print(list(generate_primes(5)))  # [2, 3, 5, 7, 11]


# ১০. API ইন্টিগ্রেশন (API Integration)
# requests লাইব্রেরি ব্যবহার করে একটি ফাংশন লিখুন যা একটি পাবলিক API থেকে ডাটা ফেচ করবে
# (যেমন: https://jsonplaceholder.typicode.com/posts)৷
# ফেচ করা ডাটা প্রসেস করে একটি নির্দিষ্ট ফরম্যাটে রিটার্ন করুন৷
# এরর হ্যান্ডলিং যোগ করুন যদি API কল ব্যর্থ হয়৷
# JavaScript এ এটি করতে হলে: const fetchData = async (url) => { try {...} };

import requests

def fetch_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return [{
            'id': item['id'],
            'title': item['title'][:50], 
            'body': item['body']
        } for item in response.json()]
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}

# টেস্ট কেস
# print(fetch_api_data('https://jsonplaceholder.typicode.com/posts'))
