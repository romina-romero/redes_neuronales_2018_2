from Tester import Tester
from SigmoidNeuron import SigmoidNeuron



def main():
	XORperceptron = TrainablePerceptron([random.randint(-2,2),random.randint(-2,2)],random.randint(-2,2),0.1)

	train_set_sizes = range(1,1000,10)

	presitions = []

	#entrenar
	for train_size in train_set_sizes:
		for i in range(train_size):
			trainXOR(XORperceptron)
		presitions.append(getXORpresition(XORperceptron))
	plt.plot(train_set_sizes,presitions)
	plt.show()


if __name__ == '__main__':
    main()