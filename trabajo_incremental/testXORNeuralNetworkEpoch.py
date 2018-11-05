from NeuralNetwork import NeuralNetwork
from Tester import Tester
import random

def main():
    neuralNetwork = NeuralNetwork()
    neuralNetwork.make(2,[2,1],0.5)
    nbepoch = 5000
    dataset = [[0,0],[0,1],[1,0],[1,1]]
    outputs = [[0],[1],[1],[0]]
    train_set_sizes = range(1,5000,10)
    errors = neuralNetwork.train(dataset,outputs,nbepoch)
    tester = Tester()
    tester.plotError(range(5000),errors, "Red neuronal entrenada con XOR, 5000 epocas")


if __name__ == '__main__':
    main()