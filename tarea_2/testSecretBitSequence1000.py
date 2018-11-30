from Tester import Tester
import random

alphabeth = [0,1]
genSize = 1000
populationSize = 200

real = []
for i in range(genSize):
    real.append(random.choice(alphabeth))

def fitnessFunction(l):
    s = 0
    for index in range(len(l.gens)):
        if l.gens[index]==real[index]:
            s+=1
    return s


def main():
    tester = Tester(fitnessFunction,alphabeth,genSize,populationSize,genSize)
    tester.test()
    print "vector original"
    print real

if __name__=='__main__':
    main()