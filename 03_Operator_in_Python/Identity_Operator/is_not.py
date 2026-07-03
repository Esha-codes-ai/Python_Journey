# is not operator returns True if both variables are not the same object
list1=[1,2,3]
list2=[1,2,3]
if list1 is not list2:  
    print("Both refer different object")
else:
    print("Both refer same object")
    # values list me same hai lekin memory location alag hai 
    # isliye output me different object print hoga