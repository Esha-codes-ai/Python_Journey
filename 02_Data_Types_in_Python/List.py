# List is a built-in data structure used to store an ordered collection of items. 
# They are dynamic, resizable and capable of storing multiple data types.
List1=["Python","mutable", "indexing"]
print(List1) # it print whole list
print(List1[0]) # only print zero index of List1
print(List1[1]) # print the first index element
print(List1[2]) #print the second index element

# -------------slicing of list---------------
Companies=["Google","Amazon", "Microsoft","TCS", "Tata","Zomato", "Blinkit", "Apple"]
print(Companies[:]) # whole list
print(Companies[0:]) # start to end
print(Companies[:-1]) # skip last element
print(Companies[0:8:2]) # start 0 to 8 skip 1 element
print(Companies[:6]) # start to six 


# -------append() to add the new element in list---------
#  append(): Adds an element at the end of the list.
Companies.append("infosis")
print(Companies)


# -----extend---------------
# extend(): Adds multiple elements to the end of the list.
Companies.extend(["Mahindra","clarity"])
print(Companies)


# -------insert---------
Companies.insert(2,"Hello")
print(Companies)
