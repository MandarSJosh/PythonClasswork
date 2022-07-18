celcius = int(input('Please enter temperature in Celcius: '))
# C = (F-32)*5/9 F = 9/5 C + 32
far = round((celcius * 9 / 5) + 32, 1)

print(f'{celcius} degree Celcius is {far} degree Farenheit')
