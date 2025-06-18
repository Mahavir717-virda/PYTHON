info = {
    "Name" : "Mahavir",
    "Age" : 18,
   "score" :  {
        "Maths" : 8,
        "Python": 9 
    }
}

# For printing particular value
print(info["score"]["Python"])

# For printing the whole dictionary
print("\nPrinting all dictionary")
print(info)

# For printing all keys
print("\nPrintng keys")
print(info.keys())

#For printing values
print("\nPrinting values")
print(info.values())

# For printing all key : value pairs
print("\nPrinting All 'key : value' pairs,This pairs are in tuple form")
print(info.items())

#For printing value according to the key
print("\nPrinting value according to key")
print(info.get("Name")) # Return None if key is not in dictionary

#For insert specified items to the dictionary
New_Dict = {
    "Movie" : "Stranger Things 5"
}
print("\nPrinting new key : value")
info.update(New_Dict)
print(info)
