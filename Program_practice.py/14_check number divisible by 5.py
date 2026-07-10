number=int(input("Enter the value of number:"))
last_digit=number%10
if last_digit in (0,5):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")