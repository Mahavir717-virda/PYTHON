collection = {1,2,3,"Mahavir","Khushal","Darshan","Tirth"}
collection2 = {1,5,6,7,"Mahavir","Darshan"}

# For printing elements
print("\nPrinting the whole set")
print(collection)

# For addinng elements
print("\nPrinting after adding elements")
collection.add(4)
collection.add("Virda")
print(collection)

# For removing the elements
print("\nPrinting the set after removing elements")
collection.remove("Darshan")
print(collection)

# For poping an element
print("\nPrinting the set after popping an eleemnt")
print(collection.pop())

# UNION of set
print("\n")
print(collection.union(collection2))

# INTERSECTION of set
print("\n")
print(collection.intersection(collection2))

#For empty the set
print("\n")
collection.clear()
print(collection)