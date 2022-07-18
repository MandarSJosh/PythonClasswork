# Creating a list
odd_numbers = [1, 3, 5, 7]
Shopping_list = ['Milk', 'Potato', 'Chips']

# Printing a list
print(odd_numbers)
print(Shopping_list)

# List is ordered, changeable, and allows duplicate


# Accessing a particular item in a list
print(Shopping_list[1])
print(odd_numbers[2])

# Adding item to a list
Shopping_list.append("Bread")
print(Shopping_list)

# Deleting from a list
Shopping_list.remove("Chips")
print(Shopping_list)

#Negative indexing
print(Shopping_list[-1])


#Range of indexes
# list_name[start: stop: step]
print(odd_numbers[2:4])

# Loop through a list
for item in Shopping_list:
  print(item)
# Length and number of the list
print(len(odd_numbers))
print(len(Shopping_list))

# Copying a list
# Equal operator just creates another
# object pointing to the original list
superheros = ["Batman","Superman","Spider-Man"]
superheros_clone = superheros
print(superheros_clone)
superheros.append("Ironman")
print(superheros_clone)

# Copy a list using copy method
animals = ['Cat', 'Dog', 'Lion' ]
animals_copy = animals.copy()
animals.append('Tiger')
print(animals_copy)