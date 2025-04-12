// ============================================================
// জাভাস্ক্রিপ্ট প্র্যাকটিস প্রশ্নাবলী (JavaScript Practice Questions)
// ============================================================

// ১. বেসিক ভেরিয়েবল ও স্ট্রিং (Basic Variables and Strings)
const greet = (name) => {
  const formattedName =
    name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  return `Hello, ${formattedName}!`;
};
// Python vs JS:
// - Python uses f-strings, JS uses template literals with ${}
// - String methods (upper(), lower()) vs JS toUpperCase(), toLowerCase()

// ২. অ্যারে ম্যানিপুলেশন (Array Manipulation)
const getEvenNumbers = (numbers) => numbers.filter((num) => num % 2 === 0);
// Python vs JS:
// - Python list comprehensions vs JS array methods (filter)

// ৩. অবজেক্ট ব্যবহার (Object Usage)
const wordCount = (sentence) => {
  return sentence.split(" ").reduce(
    (acc, word) => ({
      ...acc,
      [word]: (acc[word] || 0) + 1,
    }),
    {}
  );
};
// Python vs JS:
// - Python dict vs JS object
// - split() similar, but JS uses reduce for accumulation

// ৪. ফাইল হ্যান্ডলিং (File Handling - Node.js)
const fs = require("fs");
const fileStats = (filename) => {
  const content = fs.readFileSync(filename, "utf-8");
  return {
    lines: content.split("\n").length,
    words: content.split(/\s+/).length,
    characters: content.length,
  };
};
// Python vs JS:
// - Python built-in file handling vs Node.js fs module

// ৫. এরর হ্যান্ডলিং (Error Handling)
const divide = (a, b) => {
  try {
    if (b === 0) throw new Error("Division by zero");
    return a / b;
  } catch (error) {
    return error.message;
  }
};
// Python vs JS:
// - try/except vs try/catch
// - Python exceptions vs JS Error objects

// ৬. ক্লাস ও অবজেক্ট (Classes and Objects)
class BankAccount {
  constructor(accountNumber, holderName, balance = 0) {
    this.accountNumber = accountNumber;
    this.holderName = holderName;
    this.balance = balance;
  }

  deposit(amount) {
    this.balance += amount;
  }

  withdraw(amount) {
    if (amount > this.balance) throw new Error("Insufficient balance");
    this.balance -= amount;
  }
}
// Python vs JS:
// - Python explicit __init__ vs JS constructor
// - Method declaration syntax differences

// ৭. ইনহেরিটেন্স (Inheritance)
class Vehicle {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  displayInfo() {
    return `${this.year} ${this.make} ${this.model}`;
  }
}

class Car extends Vehicle {
  constructor(make, model, year, doors) {
    super(make, model, year);
    this.doors = doors;
  }

  displayInfo() {
    return `${super.displayInfo()} with ${this.doors} doors`;
  }
}
// Python vs JS:
// - Inheritance syntax (extends vs Python's class Child(Parent))
// - super() usage differences

// ৮. টাইমিং ফাংশন (Timing Functions)
const timerDecorator = (fn) => {
  return (...args) => {
    const start = Date.now();
    const result = fn(...args);
    console.log(`Execution time: ${Date.now() - start}ms`);
    return result;
  };
};
// Python vs JS:
// - Decorator syntax differences
// - Python time module vs JS Date

// ৯. প্রাইম নাম্বার জেনারেটর (Prime Number Generator)
function* generatePrimes(count) {
  let found = 0;
  let num = 2;

  while (found < count) {
    if (isPrime(num)) {
      yield num;
      found++;
    }
    num++;
  }
}

const isPrime = (num) => {
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return num > 1;
};
// Python vs JS:
// - Generator syntax differences (function* vs def)
// - yield keyword usage

// ১০. API ইন্টিগ্রেশন (API Integration)
const fetchData = async (url) => {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    return await response.json();
  } catch (error) {
    return { error: error.message };
  }
};
// Python vs JS:
// - Python requests vs JS fetch API
// - async/await syntax similarities
// - Error handling patterns
