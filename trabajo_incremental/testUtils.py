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
def ifhalf(x):
    if x>0.5:
        return 1
    return 0

def generateRandomPoints(n):
    pointsList = []
    for i in range(n):
        pointsList.append((random.randint(-10000,10000),random.randint(-10000,10000)))
    return pointsList


def trainXOR(perceptron):
    xs = [0,0,1,1]
    ys = [0,1,0,1]
    rs = [0,1,1,0]
    index = random.randint(0,3)
    perceptron.train([xs[index],ys[index]],rs[index])

def trainAND(perceptron):
    xs = [0,0,1,1]
    ys = [0,1,0,1]
    rs = [0,0,0,1]
    index = random.randint(0,3)
    perceptron.train([xs[index],ys[index]],rs[index])

def trainOR(perceptron):
    xs = [0,0,1,1]
    ys = [0,1,0,1]
    rs = [0,1,1,1]
    index = random.randint(0,3)
    perceptron.train([xs[index],ys[index]],rs[index])