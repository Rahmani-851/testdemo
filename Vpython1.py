from vpython import *
from time import *
#ball = vpython.sphere(color = color.red)
mRadius = 1
wallThickness = 1
wallHeight = 15
wallLength = 5
wallDepth = 50
floor = box(pos = vector(0,-wallHeight/2,0),color = color.green, size = vector(wallLength,wallThickness,wallDepth))
sleep(3)
floor1 = box(pos = vector(0,-wallHeight/2,0),color = color.white, size = vector(wallLength,wallThickness,wallDepth))
roof = box(pos = vector(0,wallHeight/2,0), color = color.white, size = vector(wallLength,wallThickness,wallDepth))
wallright = box(pos = vector(wallLength/2,0,0), color = color.yellow, size = vector(wallThickness,wallHeight,wallDepth))
wallleft = box(pos = vector(-wallLength/2,0,0), color = color.yellow, size = vector(wallThickness,wallHeight,wallDepth))
wallback = box(pos = vector(0,0,-wallDepth/2), color = color.white, size = vector(wallLength,wallHeight,wallThickness))
marble = sphere(radius = 1, color = color.red)
#button = vpython.button(color = color.blue)
deltax = .1
xpos = 0
while True:
    rate(15)
    xpos = xpos + deltax
    marble.pos = vector(xpos,0,0)
    if xpos > (wallLength/2)-mRadius-(wallThickness) or xpos <= -(wallLength/2)+mRadius+(wallThickness):
        deltax = deltax * -1

