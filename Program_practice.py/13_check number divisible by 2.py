Number=int(input("Enter the value of number:"))
last_digit=Number%10
if last_digit in (0,2,4,6,8):
    print("The number is divisible by 2")
else:
    print("The number is not divisible by 2")