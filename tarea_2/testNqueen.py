from Tester import Tester
from Board import Board
import random

N=20
alphabeth = [0,1]
genSize = N*N
populationSize = 200

def fitnessFunction(l):
    b = Board()
    b.setFromList(l.gens,N)
    cost = b.reviewHorizontals()+b.reviewVerticals()+b.reviewDiagonals()+abs(b.nqueens()-N)
    return -1*cost


def visualizationFuncion(l):
    b = Board()
    b.setFromList(l.gens,N)
    b.show()


def main():

    tester = Tester(fitnessFunction=fitnessFunction,alphabeth=alphabeth,genSize=genSize,populationSize=populationSize,threshold=0,visualizationFunction=visualizationFuncion)
    tester.test()
if __name__=='__main__':
    main()