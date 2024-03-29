from turtle import *

pensize(5)
pencolor('wheat')
bgcolor('skyblue')

penup()
backward(142)
right(90)
forward(110)
left(90)

pendown()
def square():
  fillcolor('moccasin')
  begin_fill()
  pendown()
  #right(45)
  for i in range(4):
    forward(35)
    left(90)
  end_fill()
  penup()
  
def rectangle():
  pendown()
  for i in range(2):
    forward(280)
    left(90)
    forward(150)
    left(90)
  penup()
fillcolor('darksalmon')  
begin_fill()
rectangle()
end_fill()

left(90)
forward(67)
right(90)
forward(45)
square()
forward(150)
square()
left(90)
forward(150-67)
right(90)
forward(85)
fillcolor('sienna')
def triangle():
  pendown()
  begin_fill()
  left(150)
  forward(163)
  left(60)
  forward(163)
  penup()
  end_fill()
  
triangle()
penup()
left(60)
forward(150)
left(90)
forward(121)
pendown()

def door():
  left(90)
  fillcolor('sandybrown')
  begin_fill()
  for i in range(2):
    forward(height)
    right(90)
    forward(45)
    right(90)

  end_fill()
height = 75
door()
forward(height-5)
left(90)
fillcolor('olivedrab')
penup()
backward(160)
begin_fill()
pendown()
backward(200)
left(90)
forward(600)
right(90)
forward(700)
right(90)
forward(600)
right(90)
forward(220)
right(90)
forward(height)
left(90)
forward(280)
left(90)
forward(height-5)
end_fill()
penup()