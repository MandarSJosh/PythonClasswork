from turtle import *

num_of_petals = int(input('How many petals would you like: '))

penup()
left(90)
forward(210)
right(90)
pendown()

def draw_QuarterCircle(sides, size):
  for i in range(sides):
    forward(size)
    right(90/sides)

def petal(sides, size):
  draw_QuarterCircle(sides, size)
  right(90)
  draw_QuarterCircle(sides, size)
  right(90) 

speed(6)
angle = 360 / num_of_petals

for i in range(num_of_petals):
  petal(100,2)
  right(angle)

def leaf(sides, size):
  petal(sides, size)
  right(45)
  forward(140)
  
right(90)
forward(520)
left(180)

forward(230)
right(99)
leaf(100, 1.5)

backward(140)
left(143.7)
forward(90)
left(135)
leaf(100, 1.5)
