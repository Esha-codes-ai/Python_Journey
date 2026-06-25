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