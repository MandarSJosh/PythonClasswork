# Using dictionaries to store board positions

turn = 1
output = ''
output1 =" "
output2 =" "
output3 =" "
output4 =" "
output5 =" "
output6 =" "
output7 =" "
output8 =" "
output9 =" "
ttt = {
  "1": output1 ,
  "2":output2 ,
}
if turn == 1:
  output = 'X'
elif turn == 2:
  output = 'O'
elif turn == 3:
  output = 'X'
elif turn == 4:
  output = 'O'
elif turn == 5:
  output = 'X'
elif turn == 6:
  output = 'O'
elif turn == 7:
  output = 'X'
elif turn == 8:
  output = 'O'
elif turn == 9:
  output = 'X'



for i in range(9):
  tile = int(input('Enter the tile you want to play at: '))
  if turn == 1:
    output = 'X'
  elif turn == 2:
    output = 'O'
  elif turn == 3:
    output = 'X'
  elif turn == 4:
    output = 'O'
  elif turn == 5:
    output = 'X'
  elif turn == 6:
    output = 'O'
  elif turn == 7:
    output = 'X'
  elif turn == 8:
    output = 'O'
  elif turn == 9:
    output = 'X'
  if tile == 1:
    output1 = output
    
  if tile == 2:
    output2 = output
  
  if tile == 3:
    output3 = output
  
  if tile == 4:
    output4 = output
  
  if tile == 5:
    output5 = output
  
  if tile == 6:
    output6 = output
  
  if tile == 7:
    output7 = output
  
  if tile == 8:
    output8 = output
  
  if tile == 9:
    output9 = output
  
  ttt = {
  "1": output1 ,
  "2":output2 ,
  "3":output3,
  "4":output4 ,
  "5":output5 ,
  "6":output6 ,
  "7":output7 ,
  "8":output8 ,
  "9":output9 ,
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
  print(turn)
  
  turn += 1
 


#Use variable to see turn number, string,etc





