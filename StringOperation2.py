# String Slicing - myString[start:stop:step]
name = 'Mandar'
slice = name[1 : 4]
print(slice)

#Optional first input
slice = name[:3]
print(slice)

#Optional last input
slice = name[3:]
print(slice)

#Not providing any input

slice = name[:]
print(slice)

# Negative indexing

slice = name[-4:]
print(slice)

# Negative start index with stop 
slice = name[-4:5]
print(slice)

# Negative start index with negative stop index
slice = name[-4:-1]
print(slice)

#String multiplication
sound = "Ha "
laugh = sound * 7
print(laugh)