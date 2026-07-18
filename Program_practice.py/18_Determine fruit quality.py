Fruit=input(" Please enter the fruit name you want to check:")
color=input("Please enter the color of the fruit:")
if Fruit == "Apple" and color == "Green":
    print("The fruit is unripe.")
elif Fruit == "Apple" and color == "Brown":
    print("The fruit is overripe.")
elif Fruit == "Apple" and color == "Red":
    print("The fruit is ripe.")
else:
    print("The fruit is not an apple or the color is not recognized.")