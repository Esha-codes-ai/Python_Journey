# Left Shift bitwise operator (<<) shifts the bits of the number
# to the left by the specified number of positions.
# Each shift to the left effectively multiplies the number by 2.
# Left shift=n*2**k
num1=int(input("Enter the value of num1:"))
k=int(input("Enter the value of k:"))   
result=num1<<k
print("The result of left shift is:", result)