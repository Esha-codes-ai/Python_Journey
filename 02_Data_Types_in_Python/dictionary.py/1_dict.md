# ==========================================
# PYTHON DICTIONARY METHODS WITH EXAMPLES
# ==========================================

# Original Dictionary
student = {
    "name": "Esha",
    "age": 20,
    "course": "Python"
}

print("Original Dictionary:")
print(student)
print()


# ==========================================
# 1. get() - Returns the value of a key.
# If the key does not exist, it returns the default value.
# ==========================================

print("1. get() Method")
print(student.get("name"))              # Esha
print(student.get("marks"))             # None
print(student.get("marks", "Not Found"))# Not Found
print()


# ==========================================
# 2. keys() - Returns all keys in the dictionary.
# ==========================================

print("2. keys() Method")
print(student.keys())
print()


# ==========================================
# 3. values() - Returns all values in the dictionary.
# ==========================================

print("3. values() Method")
print(student.values())
print()


# ==========================================
# 4. items() - Returns key-value pairs as tuples.
# ==========================================

print("4. items() Method")
print(student.items())
print()


# ==========================================
# 5. update() - Updates existing values or adds new key-value pairs.
# ==========================================

print("5. update() Method")

student.update({"age": 21})
print("After updating age:")
print(student)

student.update({"city": "Delhi"})
print("After adding city:")
print(student)
print()


# ==========================================
# 6. pop() - Removes the specified key and returns its value.
# ==========================================

print("6. pop() Method")

removed_value = student.pop("city")
print("Removed Value:", removed_value)
print(student)
print()


# ==========================================
# 7. popitem() - Removes and returns the last inserted key-value pair.
# ==========================================

print("7. popitem() Method")

last_item = student.popitem()
print("Removed Item:", last_item)
print(student)
print()


# ==========================================
# 8. setdefault() - Returns the value of the key.
# If the key doesn't exist, it adds the key with the default value.
# ==========================================

print("8. setdefault() Method")

student.setdefault("country", "India")
print(student)

student.setdefault("name", "Rahul")   # Will not change because 'name' already exists
print(student)
print()


# ==========================================
# 9. copy() - Creates a shallow copy of the dictionary.
# ==========================================

print("9. copy() Method")

new_student = student.copy()

print("Original Dictionary:")
print(student)

print("Copied Dictionary:")
print(new_student)
print()


# ==========================================
# 10. fromkeys() - Creates a new dictionary using given keys
# with the same default value.
# ==========================================

print("10. fromkeys() Method")

keys = ["Math", "Science", "English"]

marks = dict.fromkeys(keys, 0)

print(marks)
print()


# ==========================================
# 11. clear() - Removes all elements from the dictionary.
# ==========================================

print("11. clear() Method")

temp = student.copy()

print("Before clear():")
print(temp)

temp.clear()

print("After clear():")
print(temp)
print()


# ==========================================
# BONUS: Looping through a dictionary
# ==========================================

print("Bonus: Looping through Dictionary")

employee = {
    "id": 101,
    "name": "John",
    "salary": 50000
}

for key, value in employee.items():
    print(key, ":", value)