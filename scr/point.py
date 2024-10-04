import math

class Point:
    
    def __init__(self, x, y):
        
        self.xCoord = x
        self.yCoord = y
        
    
    def getX(self):
        
        return self.xCoord
        
    
    def getY(self):
        
        return self.yCoord
        
    
    def shift(self, xInc, yInc):
        
        self.xCoord += xInc
        self.yCoord += yInc
        
    
    def distance(self, otherPoint):
        
        x_diff = self.xCoord - otherPoint.xCoord
        y_diff = self.yCoord - otherPoint.yCoord
        
        return math.sqrt(x_diff**2 + y_diff**2)
        
    
    def __eq__(self, rhsPoint):
        
        return self.xCoord == rhsPoint.xCoord and self.yCoord == rhsPoint.yCoord
        
        
    def __str__(self):
        
        return "(" + str(self.xCoord) + "," + str(self.yCoord) + ")"
        