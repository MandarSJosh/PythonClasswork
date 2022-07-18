# Dictionary
# Definition: A dictionary is a collection which is unordered, changeable and indexed. They are written in curly brackets and have key value pair

#Creating a dictionary
myCar = {
  "brand" : "Ford",
  "model" : "Mustang",
  "year"  :  1982,
  "capacity" : 5,
  "colour" : "Space Gray"
}



mycar_brand = "Ford"
mycar_model = "Mustang"

# Printing a dictionary
print(myCar)
# Accessing items in a dictionary
print(myCar['model'])
# Adding item to a dictionary, unordered**

myCar['shade'] = 'Space Gray'
print(myCar)

# Removing item from a dictionary
myCar.pop('year')
print(myCar)

# Looping through a dictionary
for i in myCar:
  print(i, myCar[i])

for k,v in myCar.items():
  print(k,v)

# Length of a dictionary
print(len(myCar))

# Emptying a dictionary
#myCar.clear()
#print(myCar)

# Destorying a dictionary
#del myCar
#print(myCar)

# Create a copy of a dictionary
myCarCopy = myCar.copy()
print(myCarCopy)

# Using dictionaries to store board positions
ttt = {
  "1":" ",
  "2":" ",
  "3":" ",
  "4":" ",
  "5":" ",
  "6":" ",
  "7":" ",
  "8":" ",
  "9":" ",
  
}
line1 = ttt['1'] + "|" + ttt['2'] + "|" + ttt['3']
line2 = ttt['4'] + "|" + ttt['5'] + "|" + ttt['6']
line3 = ttt['7'] + "|" + ttt['8'] + "|" + ttt['9']
seperator ="-+-+-"

print(line1)
print(seperator)
print(line2)
print(seperator)
print(line3)

#Use variable to see turn number, string,etc