print("Hello and welcome to Tic Tac Toe!")
print("These are the respective tile numbers of the tiles on the board and entering a number will fill the tile with the letter of the current turn:")
print("")


def display_grid(positions):
  line1 = positions['1'] + "|" + positions['2'] + "|" +   positions['3']
  line2 = positions['4'] + "|" + positions['5'] + "|" + positions['6']
  line3 = positions['7'] + "|" + positions['8'] + "|" + positions['9']
  seperator =" --+-+-+-- "
  print(line1)
  print(seperator)
  print(line2)
  print(seperator)
  print(line3)


Game = ''
ggg = {
  '1':" 1 ",
  '2':" 2 ",
  '3':" 3 ",
  '4':" 4 ",
  '5':" 5 ",
  '6':" 6 ",
  '7':" 7 ",
  '8':" 8 ",
  '9':" 9 "
}

display_grid(ggg)

ttt = {
  '1':"   ",
  '2':"   ",
  '3':"   ",
  '4':"   ",
  '5':"   ",
  '6':"   ",
  '7':"   ",
  '8':"   ",
  '9':"   "
}
 

def isValid(position):
  if ttt[position] == "   ":
    return True
  else:
    return False

def isWin():
    global Game    
    #Horizontal winning condition    
    if(ttt['1'] == ttt['2'] and ttt['2'] == ttt['3'] and ttt['1'] != "   "):    
      Game = 'Win'    
    elif(ttt['4'] == ttt['5'] and ttt['5'] == ttt['6'] and ttt['4'] != "   "):    
      Game = 'Win'     
    elif(ttt['7'] == ttt['8'] and ttt['8'] == ttt['9'] and ttt['7'] != "   "):    
      Game = 'Win'      
    #Vertical Winning Condition    
    elif(ttt['1'] == ttt['4'] and ttt['4'] == ttt['7'] and ttt['1'] != "   "):    
      Game = 'Win'     
    elif(ttt['2'] == ttt['5'] and ttt['5'] == ttt['8'] and ttt['2'] != "   "):    
      Game = 'Win'      
    elif(ttt['3'] == ttt['6'] and ttt['6'] == ttt['9'] and ttt['3'] != "   "):
      Game='Win'     
    #Diagonal Winning Condition    
    elif(ttt['1'] == ttt['5'] and ttt['5'] == ttt['9'] and ttt['5'] != "   "):    
      Game = 'Win'    
    elif(ttt['3'] == ttt['5'] and ttt['5'] == ttt['7'] and ttt['5'] != "   "):    
      Game='Win'     
    #Match Tie or Draw Condition    
    elif(ttt['1']!='   ' and ttt['2']!='   ' and ttt['3']!='   ' and ttt['4']!='   ' and ttt['5']!='   ' and ttt['6']!='   ' and ttt['7']!='   ' and ttt['8']!='   ' and ttt['9']!='   '):    
      Game = 'Draw'
    
print("")
print("")
current_turn = ' X '
#for i in range(100):
while True:
  print(f"It is {current_turn}'s turn")
  pos = input("Where do you want to play: ")
  print("")
  if isValid(pos) == True:
    ttt[pos] = current_turn
    display_grid(ttt)
    if  current_turn == ' X ':
      current_turn = ' O '
    else:
      current_turn = ' X '
  else:
    continue
  print("")
  isWin()
  if Game == 'Win':
    if  current_turn == ' X ':
      current_turn = ' O '
    else:
      current_turn = ' X '
    print(f'{current_turn} has won')
    break
  if Game == 'Draw':
    print('The game is a draw')
    
 

'''
Versions

Version# 1
- define tt dictionary
- collect the input
- mark the cell
- show the output

Version# 2 
- Check if valid move
- if invalid ask again until correct move made


Version# 3
- After every move
- Check if someone has won
'''
