# Prime number checker

number = int(input('Please enter a number: '))
i = 2
while i < number:
  remainder = number % i
  i = i + 1
  if remainder == 0:
    print(f"{number}, is not a prime number.")
    break
    
else:
    print(f"{number} is a prime number.")
