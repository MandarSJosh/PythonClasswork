Inp = str(input("Enter sentence: "))

def beautify(input):
  i = 0
  for i in input:
    cord = ord(i)
    if cord >= 97:
      letter = (chr(cord-32))
      break
    else:
      letter = i
      break
  output = letter
  print(output, end ="")

  '''i = 2
  c = i + 1
  for i in input:    
    bord = ord(i)
    if bord >= 97:
      fet = i
      print(fet, end = "")
      i = c
    elif bord >= 65:
      fet = (chr(bord+32))
      print(fet, end = "")
      i = c
    '''
 
  for elem in input[1:len(input)]:    
    bord = ord(elem)
    if bord >= 97:
      fet = elem
      print(fet, end = "")
    
    elif bord >= 65:
      fet = (chr(bord+32))
      print(fet, end = "")
  
    else:
      fet = elem
      print(fet, end = "")
  
beautify(Inp)



#print(chr(ord('X')+32))
#print(ord('a'))






#for i in string:

#joining sting

#print, end =''
'''Input = how ARE YoU?


Output = How are you?

output = beautify(input)
print(output)
'''