# Ord and Chr

# Converting code to ASCII code

char = "~"
print(ord(char))

# Converting ASCII code to character
code= 71
print(chr(code))

#Printing upper case alphabets
for i in range(65, 65+26):
  print(chr(i))
  
#Printing alphabets in reverse order
print( "Reverse order")
for i in range(64+26, 64,-1):
    print(chr(i))
