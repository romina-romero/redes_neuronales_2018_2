import random
import math
class SimpleLine:
    def __init__(self,m,n):
        self.m = m
        self.n = n

    def isUpperLine(self,x,y):
        calc_y = self.m*x+self.n
        if y>calc_y:
            return 1
        return 0
    def getY(self,x):
        return self.m*x+self.n

def generateRandomPoins(n):
    pointsList = []
    for i in range(n):
        pointsList.append((random.randint(-10000,10000),random.randint(-10000,10000)))
    return pointsList