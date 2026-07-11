Age=int(input("Enter your age: "))
day=input("Enter the day of the week: ")
price=12 if Age>=18 else 8
if day=="Wednesday":
    price=price-2
print(price)