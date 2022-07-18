from turtle import *

number = int(input("How many petals would you like: "))
pensize(5)
pencolor('hotpink')
bgcolor('skyblue')
fillcolor('orange')

def bar():
  pendown()
  #right(45)
  for i in range(4):
    forward(60)
    left(90)
  penup()
'''
if number < 10:
  angle = 180/ number
else:
  angle = 50 / number
'''
begin_fill()
angle = 360 / number
for i in range(number):
  bar()
  left(angle)
end_fill()

 