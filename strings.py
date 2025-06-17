#concatanation of string
name = "virda" + " " + "Mahavir"
print(name)

#length of the string
print(len(name))

#Slicing in string with positive index
print(name[6:10])

#slicing in strings with negative index
print(name[-7 : -3])

#string functions 

# 1
print("\nReturn true if strng start or end with the value")
print(name.endswith("r"))
print(name.startswith("V"))

# 2
print("\nthis function returns the first character of the string in uppercase")
print(name.capitalize())

# 3
print("\nAFter replacing old value with new value")
print(name.replace("virda Mahavir","Khushal"))

# 4 
print("\nReturns index when value appear first time")
print(name.find("a"))
print("Return -1 if don`t in string -> Ex. x",name.find("x"))

# 5 
print("\nReturn the number of character of times it is coming ")
print(name.count("a"))
