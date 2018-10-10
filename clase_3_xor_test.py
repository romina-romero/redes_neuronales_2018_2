from clase_2 import TrainablePerceptron
import matplotlib.pyplot as plt
import random

def getXORpresition(perceptron):
	xs = (0,0,1,1)
	ys = (0,1,0,1)
	real = (0,1,1,0)
	corrects = 0

	for index in range(4):
		result = perceptron.feed([xs[index],ys[index]])
		if result == real[index]:
			corrects+=1
	return corrects*1.0/4

def trainXOR(perceptron):
	xs = [0,0,1,1]
	ys = [0,1,0,1]
	rs = [0,1,1,0]
	index = random.randint(0,3)
	perceptron.train([xs[index],ys[index]],rs[index])

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