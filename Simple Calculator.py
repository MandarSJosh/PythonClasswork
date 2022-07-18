type = input('Which arithmetic operation would you like to perform( a, s, m, d): ')

if type == 'a' :
  num1 = int(input('Please enter the first number: '))
  num2 = int(input('Please enter the second number: '))
  sum = num1 + num2
  print(f'The sum of {num1} and {num2} is {sum}')

elif type == 's' :
  num1 = int(input('Please enter the first number: '))
  num2 = int(input('Please enter the second number: '))
  diff= num1 - num2
  print(f'The difference of {num1} and {num2} is {diff}')

elif type == 'm' :
  num1 = int(input('Please enter the first number: '))
  num2 = int(input('Please enter the second number: '))
  prod = num1 * num2
  print(f'The product of {num1} and {num2} is {prod}')

elif type == 'd' :
  num1 = int(input('Please enter the first number: '))
  num2 = int(input('Please enter the second number: '))
  quo = num1 / num2
  print(f'The quotient of {num1} and {num2} is {round(quo, 2)} rounded to 2 places of decimal')

else :
  print('Invalid input, you must enter either a, s, m or d.')