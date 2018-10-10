from SigmoidNeuron import SigmoidNeuron
from testUtils import trainAND
from Tester import Tester
from testUtils import ifhalf
import random

def main():
    ANDperceptron = SigmoidNeuron([random.randint(-2,2),random.randint(-2,2)],random.randint(-2,2),0.1)
    train_set_sizes = range(1,1000,10)
    presitions = []
    tester = Tester()
    #entrenar
    for train_size in train_set_sizes:
        for i in range(train_size):
            trainAND(ANDperceptron)
        presitions.append(tester.test(ANDperceptron,[[0,0],[0,1],[1,0],[1,1]],[0,0,0,1],ifhalf))
    tester.plot(train_set_sizes,presitions, "Neurona Sigmoide entrenada con AND")

if __name__ == '__main__':
    main()