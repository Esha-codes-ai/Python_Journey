# Python Loops - Complete Guide

# Table of Contents

1. Introduction
2. Why Loops?
3. Types of Loops
4. for Loop
5. while Loop
6. Loop Control Statements
7. Nested Loops
8. Range Function
9. Iterating Over Different Data Types
10. Loop Else
11. Infinite Loops
12. Common Interview Questions
13. Time Complexity
14. Practice Questions
15. Summary

---

# 1. Introduction

A loop is used to execute a block of code repeatedly.

Instead of writing:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

We can write:

```python
for i in range(5):
    print("Hello")
```

Output

```
Hello
Hello
Hello
Hello
Hello
```

---

# 2. Why Use Loops?

Loops help to

- Reduce code repetition
- Save time
- Make programs cleaner
- Process collections easily
- Automate repetitive tasks

---

# 3. Types of Loops

Python has only two loops.

1. for loop
2. while loop

---

# 4. for Loop

A for loop is used to iterate over an iterable.

An iterable can be

- List
- Tuple
- String
- Dictionary
- Set
- Range
- File

Syntax

```python
for variable in iterable:
    statements
```

Example

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output

```
Apple
Banana
Mango
```

---

# Example 2

```python
for number in [10,20,30]:
    print(number)
```

Output

```
10
20
30
```

---

# Example 3

```python
name = "Python"

for ch in name:
    print(ch)
```

Output

```
P
y
t
h
o
n
```

---

# Example 4

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

# 5. range()

range() creates a sequence of numbers.

Syntax

```python
range(stop)
```

```python
range(start, stop)
```

```python
range(start, stop, step)
```

---

## range(stop)

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

## range(start, stop)

```python
for i in range(2,8):
    print(i)
```

Output

```
2
3
4
5
6
7
```

---

## range(start, stop, step)

```python
for i in range(2,20,3):
    print(i)
```

Output

```
2
5
8
11
14
17
```

---

# Negative Step

```python
for i in range(10,0,-2):
    print(i)
```

Output

```
10
8
6
4
2
```

---

# 6. while Loop

A while loop runs until the condition becomes False.

Syntax

```python
while condition:
    statements
```

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

# Another Example

```python
number = 10

while number > 0:
    print(number)
    number -= 2
```

Output

```
10
8
6
4
2
```

---

# Infinite while Loop

```python
while True:
    print("Running")
```

This loop never stops until interrupted.

---

# 7. Loop Control Statements

Python provides

- break
- continue
- pass

---

# break

Terminates the loop immediately.

Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

---

# continue

Skips the current iteration.

```python
for i in range(6):

    if i == 3:
        continue

    print(i)
```

Output

```
0
1
2
4
5
```

---

# pass

pass does nothing.

It is a placeholder.

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

Output

```
0
1
2
3
4
```

---

# 8. Nested Loops

A loop inside another loop.

Syntax

```python
for i in range(3):
    for j in range(2):
        print(i,j)
```

Output

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

# Multiplication Table

```python
for i in range(1,6):

    for j in range(1,11):
        print(i*j,end=" ")

    print()
```

Output

```
1 2 3 ...
2 4 6 ...
...
```

---

# Star Pattern

```python
for i in range(5):

    for j in range(i+1):
        print("*",end="")

    print()
```

Output

```
*
**
***
****
*****
```

---

# Reverse Star Pattern

```python
for i in range(5,0,-1):

    for j in range(i):
        print("*",end="")

    print()
```

Output

```
*****
****
***
**
*
```

---

# Pyramid

```python
rows = 5

for i in range(rows):

    print(" "*(rows-i-1),end="")

    print("*"*(2*i+1))
```

Output

```
    *
   ***
  *****
 *******
*********
```

---

# 9. Loop with Strings

```python
text = "Python"

for ch in text:
    print(ch)
```

---

# Loop with List

```python
numbers = [2,4,6,8]

for num in numbers:
    print(num)
```

---

# Loop with Tuple

```python
colors = ("Red","Green","Blue")

for color in colors:
    print(color)
```

---

# Loop with Set

```python
nums = {1,2,3,4}

for i in nums:
    print(i)
```

Order is not guaranteed.

---

# Loop with Dictionary

Dictionary Keys

```python
student = {
    "name":"John",
    "age":20
}

for key in student:
    print(key)
```

Output

```
name
age
```

---

Dictionary Values

```python
for value in student.values():
    print(value)
```

Output

```
John
20
```

---

Dictionary Items

```python
for key,value in student.items():
    print(key,value)
```

Output

```
name John
age 20
```

---

# 10. enumerate()

Returns both index and value.

```python
fruits = ["Apple","Banana","Mango"]

for index,fruit in enumerate(fruits):
    print(index,fruit)
```

Output

```
0 Apple
1 Banana
2 Mango
```

---

# 11. zip()

Iterate multiple lists together.

```python
names = ["A","B","C"]

marks = [90,80,70]

for n,m in zip(names,marks):
    print(n,m)
```

Output

```
A 90
B 80
C 70
```

---

# 12. else with Loop

The else block executes only if the loop finishes normally.

```python
for i in range(5):
    print(i)
else:
    print("Finished")
```

Output

```
0
1
2
3
4
Finished
```

---

Example with break

```python
for i in range(5):

    if i==3:
        break

    print(i)

else:
    print("Finished")
```

Output

```
0
1
2
```

The else block is skipped.

---

# 13. Iterating Backwards

```python
for i in range(10,0,-1):
    print(i)
```

---

# 14. Common Operations

## Sum

```python
numbers = [2,4,6]

total = 0

for num in numbers:
    total += num

print(total)
```

---

## Maximum

```python
numbers = [4,9,1,12]

largest = numbers[0]

for num in numbers:

    if num > largest:
        largest = num

print(largest)
```

---

## Count Even Numbers

```python
numbers = [1,2,3,4,5,6]

count = 0

for num in numbers:

    if num%2==0:
        count += 1

print(count)
```

---

## Reverse String

```python
text = "Python"

reverse = ""

for ch in text:
    reverse = ch + reverse

print(reverse)
```

---

## Factorial

```python
n = 5

fact = 1

for i in range(1,n+1):
    fact *= i

print(fact)
```

Output

```
120
```

---

# 15. Time Complexity

| Operation | Complexity |
|------------|------------|
| Single loop | O(n) |
| Nested loop | O(n²) |
| Triple nested | O(n³) |
| while loop | Depends on condition |

---

# 16. Common Mistakes

## Forgetting Colon

Wrong

```python
for i in range(5)
```

Correct

```python
for i in range(5):
```

---

## Wrong Indentation

Wrong

```python
for i in range(5):
print(i)
```

Correct

```python
for i in range(5):
    print(i)
```

---

## Infinite Loop

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

Forgot

```python
count += 1
```

---

# 17. Interview Questions

1. Difference between for and while loop.
2. What is range()?
3. Difference between break and continue.
4. What does pass do?
5. What is nested loop?
6. Explain loop else.
7. What is enumerate()?
8. What is zip()?
9. What is an infinite loop?
10. Can we iterate over a dictionary?

---

# 18. Practice Questions

Easy

1. Print numbers from 1 to 100.
2. Print even numbers.
3. Print odd numbers.
4. Print multiplication table.
5. Calculate factorial.
6. Sum first N numbers.
7. Reverse a string.
8. Count vowels.
9. Count even and odd numbers.
10. Find largest element.

Medium

11. Fibonacci series.
12. Prime number check.
13. Print all prime numbers in a range.
14. Armstrong number.
15. Palindrome check.
16. Reverse digits of a number.
17. Count digits.
18. Sum of digits.
19. Pattern printing.
20. Remove duplicates from a list using loops.

Hard

21. Pascal Triangle.
22. Floyd Triangle.
23. Diamond Pattern.
24. Matrix multiplication using nested loops.
25. Bubble Sort.
26. Selection Sort.
27. Insertion Sort.
28. Frequency of characters.
29. Word counter.
30. Custom implementation of max(), min(), and sum() using loops.

---

# 19. Summary

✔ Loops repeat code.

✔ Python provides two loops:
- for
- while

✔ range() generates numbers.

✔ break exits a loop.

✔ continue skips an iteration.

✔ pass is a placeholder.

✔ Nested loops are used for patterns and matrices.

✔ else executes only when the loop finishes without break.

✔ enumerate() provides index and value.

✔ zip() iterates over multiple iterables simultaneously.

✔ Practice loops regularly—they are one of the most important topics in Python and coding interviews.