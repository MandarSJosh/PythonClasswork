import math

X1 = int(input('Please enter the first x coordinate: '))
Y1 = int(input('Please enter the first y coordinate: '))

X2 = int(input('Please enter the second x coordinate: '))
Y2 = int(input('Please enter the second y coordinate: '))

sumSquare = (X2 - X1) ** 2 + (Y2 - Y1) ** 2
distance = round(math.sqrt(sumSquare),1)
print(f'The distance is {distance}.')


