from NeuralNetwork import NeuralNetwork
from Tester import Tester
import random

def trainXORWithNetwork(network):
    xs = [0,0,1,1]
    ys = [0,1,0,1]
    rs = [0,1,1,0]
    index = random.randint(0,3)
    if rs[index] == 1:
        network.train([xs[index],ys[index]],[1,0])
    else:
        network.train([xs[index],ys[index]],[0,1])

def main():
    neuralNetwork = NeuralNetwork()
    neuralNetwork.make(2,[2,2],0.1)
    train_set_sizes = range(1,5000,10)
    presitions = []
    tester = Tester()
    #entrenar
    for train_size in train_set_sizes:
        for i in range(train_size):
            trainXORWithNetwork(neuralNetwork)
        presitions.append(tester.testNetwork(neuralNetwork,[[0,0],[0,1],[1,0],[1,1]],[[0,1],[1,0],[1,0],[0,1]]))
    
    tester.plot(train_set_sizes,presitions, "Red neuronal con 2 neuronas en c.o. y 2 salidas, entrenada con XOR")


if __name__ == '__main__':
    main()