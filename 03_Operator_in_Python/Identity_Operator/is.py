# Identity Operator is used to check if two variables
# are located on the same part of the memory.
# is=return true if both refer same object in memory
list1=[1,2,3]
list2=list1
if list1 is list2:
    print("Both refer same object")
else:
    print("Both refer different object")
    # values list me same hai lekin memory location alag hai 
    # isliye output me different object print hoga