import math

class Coordinate:
  x = None
  y = None

  # this is initialization method / constructor
  def __init__(self, x_value, y_value):
    self.x = x_value
    self.y = y_value

  # special method for printing  
  def __str__(self):
    mystr = "(" + str(self.x) + " , " + str(self.y) + ")"
    return(mystr)

  # distance formula
  def distance(self, other_point):
    X1 = self.x
    Y1 = self.y
    X2 = other_point.x
    Y2 = other_point.y
    
    sumSquare = (X2 - X1) ** 2 + (Y2 - Y1) ** 2
    distance = round(math.sqrt(sumSquare),1)
    return(distance)

    
point1 = Coordinate(10, 20)
#point1.x = 10
#point1.y = 20
print(point1.x)
print(point1.y)

point2 = Coordinate(30, 40)
print(point2.x)
print(point2.y)
print(point2)

print(point1.distance(point2))

