# ডিকশনারি মেথডস (Dictionary Methods)
# পাইথনে ডিকশনারি ম্যানিপুলেশন টেকনিক

# ১. বেসিক অপারেশনস (Basic Operations)
student = {"name": "Rahim", "age": 25, "department": "CSE"}

# কীসের লিস্ট পাওয়া
print(student.keys())   # dict_keys(['name', 'age', 'department'])
# জাভাস্ক্রিপ্ট: Object.keys(student)

# ভ্যালুর লিস্ট পাওয়া
print(student.values()) # dict_values(['Rahim', 25, 'CSE'])

# আইটেমস পাওয়া
print(student.items())  # dict_items([('name', 'Rahim'), ('age', 25)...])

# ২. গেট মেথড (Get Method)
print(student.get("age", 30))     # 25
print(student.get("grade", "A")) # "A" (ডিফল্ট ভ্যালু)

# ৩. আপডেট মেথড (Update Method)
new_info = {"age": 26, "email": "rahim@example.com"}
student.update(new_info)
print(student) # আপডেটেড ডিকশনারি

# ৪. পপ মেথড (Pop Method)
removed = student.pop("department")
print(f"Removed: {removed}, Remaining: {student}")

# ৫. সেটডিফল্ট মেথড (Setdefault Method)
student.setdefault("courses", ["Math", "Python"])
print(student) # নতুন কী অ্যাড করবে যদি না থাকে

# ব্যবহারিক উদাহরণ (Configuration Settings)
app_config = {
    "debug_mode": False,
    "max_users": 100,
    "allowed_ips": ["192.168.1.1", "127.0.0.1"]
}

# কন্ডিশনাল চেক
if app_config.get("debug_mode"):
    print("Debugging enabled")

# মাল্টিলেভেল ডিকশনারি
employee = {
    "id": 123,
    "personal": {"name": "Karim", "age": 30},
    "professional": {"position": "Developer", "skills": ["Python", "JS"]}
}

print(employee["personal"]["name"]) # Karim

# এরর হ্যান্ডলিং উদাহরণ
try:
    print(student["address"])
except KeyError as e:
    print(f"Key error: {e}")