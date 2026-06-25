# Logical And operator is used to 
# return the TRUE if n=both the values are true
# if one is false then the result also false.
# it return the boolean values either true or false.

# Vote eligibility
age=int(input("enter your age:"))
if age>=18 and age<=100:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Student pass or fail
Student=str(input("Enter your name:"))
Marks= int(input("Enter your marks:"))
if Marks>40 and Marks<=100:
    print("Congratulations",Student,"You are pass")
else:
    print("Keep HardWorking", Student,"Do well at next time")    