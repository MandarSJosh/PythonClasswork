age = int(input('What is your age: '))
citi = input('Are you a citizen of India[Y/N]: ')

if age >= 18:
  if citi == 'Y':
    print("You are eligible to vote in India")

  else:
    print("You are not eligible to vote in India")
else:
    print("You are not eligible to vote in India")