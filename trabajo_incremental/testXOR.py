from Perceptron import Perceptron
from testUtils import trainXOR
from Tester import Tester
import random
def main():
	XORperceptron = Perceptron([random.randint(-2,2),random.randint(-2,2)],random.randint(-2,2),0.1)
	train_set_sizes = range(1,1000,10)
	presitions = []
	tester = Tester()
	#entrenar
	for train_size in train_set_sizes:
		for i in range(train_size):
			trainXOR(XORperceptron)
		presitions.append(tester.test(XORperceptron,[[0,0],[0,1],[1,0],[1,1]],[0,1,1,0]))
	
	tester.plot(train_set_sizes,presitions, "Perceptron entrenado con XOR")


if __name__ == '__main__':
    main()