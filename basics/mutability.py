# Python Mutable and Immutable Types Explained
# মিউটেবল এবং ইমিউটেবল টাইপের ব্যাখ্যা

# Immutable Types (অপরিবর্তনীয় টাইপ)
# Strings, tuples, numbers, booleans
str_example = "hello"
print(f"Original string id: {id(str_example)}")
str_example += " world"
print(f"Modified string id: {id(str_example)}\n")  # New ID

num = 10
print(f"Original number id: {id(num)}")
num += 5
print(f"Modified number id: {id(num)}\n")  # New ID

# Mutable Types (পরিবর্তনীয় টাইপ)
# Lists, dictionaries, sets
list_example = [1, 2, 3]
print(f"Original list id: {id(list_example)}")
list_example.append(4)
print(f"Modified list id: {id(list_example)}\n")  # Same ID

dict_example = {'a': 1}
print(f"Original dict id: {id(dict_example)}")
dict_example['b'] = 2
print(f"Modified dict id: {id(dict_example)}\n")  # Same ID

# Practical Implications in Functions
def modify_immutable(x):
    x += 10
    print(f"Inside function (immutable): {x} id: {id(x)}")

def modify_mutable(lst):
    lst.append(4)
    print(f"Inside function (mutable): {lst} id: {id(lst)}")

# Testing immutability
value = 5
print(f"\nBefore function (immutable): {value} id: {id(value)}")
modify_immutable(value)
print(f"After function (immutable): {value} id: {id(value)}")

# Testing mutability
my_list = [1, 2, 3]
print(f"\nBefore function (mutable): {my_list} id: {id(my_list)}")
modify_mutable(my_list)
print(f"After function (mutable): {my_list} id: {id(my_list)}")

# Tuple Example (Immutable)
tuple_example = (1, 2, 3)
try:
    tuple_example[0] = 4
except TypeError as e:
    print(f"\nTuple modification error: {e}")

# Set Example (Mutable)
set_example = {1, 2, 3}
print(f"\nOriginal set id: {id(set_example)}")
set_example.add(4)
print(f"Modified set id: {id(set_example)}")