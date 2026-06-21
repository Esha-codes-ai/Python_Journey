# List store data in a continuos way.
# Its data is in brackets[].
# List starts it count from zero 
# List is mutable 
# eg

list=[1,2,3,4,5]
print(list)
len(list)

# create a list of 10 numbers and calculate its smallest number , largest number, and average


List1=[1,2,3,4,5,6,7,8,9,10]
Smallest=min(List1)
print("The smallest Number of List1", Smallest)
Largest=max(List1)
print("The Largest number of the List1 is:", Largest)
Average=sum(List1)/len(List1)
print("The average of the List1 is:", Average)

# reference one list with other 
L1=[1,2,3]
L2=L1
print(L1)
L1[0]=55
print(L1)
print(L2)

# both reference of object is different
n=[1,2,3]
m=n
m==n
m is n
# 