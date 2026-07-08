# ternary operator check the condition and return the value 
# based on the condittion
# uses if and else statement in a single line
a=int(input())
num="Even" if a%2==0 else "Odd"
print(num)

age=int(input("Enter your age:"))
result="Eligible to vote" if age>=18 else "Not Eligible to vote"
print(result)