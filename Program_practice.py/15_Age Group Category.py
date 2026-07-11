Age=int(input("Enter your age:"))
if Age<13:
    print("child")
elif 13<=Age<=19:
    print("Teenager")
elif 20<=Age<=59:
    print("Adult")
else:
    print("Senior")