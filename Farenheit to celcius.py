far = int(input('Please enter temperature in Farenheit: '))
# C = (F-32)*5/9
celcius = round ( (far - 32) * (5 / 9), 1)

print(f'{far} degree Farenheit is {celcius} degree celcius')
