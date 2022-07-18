'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''
mark = int(input('How many marks attained: '))

if mark < 25 :
  grade = 'F'

elif mark >= 80 :
  grade = 'A'

elif mark >= 60 :
  grade = 'B'

elif mark >= 50 :
  grade = 'C'

elif mark >= 45 :
  grade = 'D'

elif mark >= 25 :
  grade = 'E'

print (f'The grade achieved is {grade} ')