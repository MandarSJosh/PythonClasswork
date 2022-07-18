from turtle import *

fillcolor('black')

begin_fill()
for i in range(2):
  forward(20)
  right(90)
  forward(40)
  right(90)
end_fill()

penup()
right(90)
forward(40)
left(90)
forward(50)
pendown()
begin_fill()
for i in range(2):
  forward(20)
  left(90)
  forward(80)
  left(90)
end_fill()

penup()
forward(50)
pendown()
begin_fill()
for i in range(2):
  forward(20)
  left(90)
  forward(120)
  left(90)
end_fill()

penup()
forward(50)
pendown()
begin_fill()
for i in range(2):
  forward(20)
  left(90)
  forward(160)
  left(90)
end_fill()