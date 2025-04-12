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


# ৪. ফাইল হ্যান্ডলিং (File Handling)
# একটি ফাংশন লিখুন যা একটি টেক্সট ফাইল পড়বে এবং সেই ফাইলে কতটি লাইন, কতটি শব্দ এবং কতটি অক্ষর আছে তা গণনা করে রিটার্ন করবে।
# উদাহরণ: "hello.txt" -> {"lines": 3, "words": 10, "characters": 50}


# ৫. এক্সেপশন হ্যান্ডলিং (Exception Handling)
# একটি ফাংশন লিখুন যা দুটি সংখ্যা নিয়ে ভাগ করবে, কিন্তু শূন্য দিয়ে ভাগ করার সময় একটি উপযুক্ত এরর মেসেজ দেখাবে।
# try-except ব্লক ব্যবহার করুন।
# উদাহরণ: divide(10, 2) -> 5, divide(10, 0) -> "Error: Division by zero is not allowed"


# ৬. ক্লাস ও অবজেক্ট (Classes and Objects)
# একটি "BankAccount" ক্লাস তৈরি করুন যেখানে অ্যাকাউন্ট নম্বর, অ্যাকাউন্ট হোল্ডারের নাম এবং ব্যালেন্স থাকবে।
# deposit() ও withdraw() মেথড যোগ করুন যা ব্যালেন্স আপডেট করবে।
# withdraw() মেথডে চেক করুন যে উত্তোলনের পরিমাণ ব্যালেন্সের চেয়ে বেশি কিনা।


# ৭. ইনহেরিটেন্স (Inheritance)
# "Vehicle" নামে একটি বেস ক্লাস তৈরি করুন এবং "Car" ও "Motorcycle" নামে দুটি সাবক্লাস তৈরি করুন।
# Vehicle ক্লাসে make, model, year প্রোপার্টি এবং একটি display_info() মেথড থাকবে।
# Car ও Motorcycle ক্লাসে নিজস্ব প্রোপার্টি এবং মেথড যোগ করুন এবং display_info() মেথড ওভাররাইড করুন।


# ৮. ডেকোরেটর (Decorators)
# একটি টাইমিং ডেকোরেটর তৈরি করুন যা কোন ফাংশন কতক্ষণ সময় নিয়ে এক্সিকিউট হয় তা মাপবে এবং প্রিন্ট করবে।
# এই ডেকোরেটর ব্যবহার করে fibonacci সিরিজ জেনারেট করার একটি ফাংশন লিখুন।


# ৯. জেনারেটর (Generators)
# একটি জেনারেটর ফাংশন লিখুন যা প্রাইম নাম্বার জেনারেট করবে।
# ব্যবহারকারী যত সংখ্যক প্রাইম নাম্বার চায় তা জেনারেট করতে হবে।
# উদাহরণ: list(generate_primes(5)) -> [2, 3, 5, 7, 11]


# ১০. API ইন্টিগ্রেশন (API Integration)
# requests লাইব্রেরি ব্যবহার করে একটি ফাংশন লিখুন যা একটি পাবলিক API থেকে ডাটা ফেচ করবে
# (যেমন: https://jsonplaceholder.typicode.com/posts)।
# ফেচ করা ডাটা প্রসেস করে একটি নির্দিষ্ট ফরম্যাটে রিটার্ন করুন।
# এরর হ্যান্ডলিং যোগ করুন যদি API কল ব্যর্থ হয়।
