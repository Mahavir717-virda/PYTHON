marks = [9,2,10,8,5,6,7,4,1,3]
print(marks)
# Slicing like string
print(marks[5:8])

# Appending
print("\nAfter append ->")
marks.append(11)
print(marks)

# Sorting
print("\nAfter sorting ->")
marks.sort()
print(marks)

# Reversing
print("\nAfter reversing ->")       
marks.reverse()
print(marks)

# Inserting
print("\nAfter inserting 17 at index 2 ->")
marks.insert(2, 17)
print(marks)    

# Removing
print("\nAfter removing 12 ->")
marks.remove(17)
print(marks)

# Popping
print("\nAfter popping last element ->")    
marks.pop()
print(marks)

# Extending 
print("\nAfter extending with [13, 14] ->")
marks.extend([13, 14])
print(marks)    

# Counting
print("\nCount of 10 ->")
print(marks.count(10))

# Indexing
print("\nIndex of 10 ->")
print(marks.index(8))  
