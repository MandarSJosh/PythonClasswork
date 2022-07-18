from turtle import *

fillcolor('black')

def bar(size):
  pendown()
  begin_fill()
  for i in range(2):
    forward(20)
    left(90)
    forward(size)
    left(90)
  end_fill()
  penup()

length = 40
for i in range(4):
  bar(length)
  forward(40)
  length += 40

