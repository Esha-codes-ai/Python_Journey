# Right shift bitwise operator (>>) shifts the bits of the number 
# to the right by the specified number of positions.
# Each shift to the right effectively divides the number by 2.
# Right shift=n/2**k
num1=int(input("Enter the value of num1:"))
k=int(input("Enter the value of k:"))
result=num1>>k
print("The result of right shift is:", result)