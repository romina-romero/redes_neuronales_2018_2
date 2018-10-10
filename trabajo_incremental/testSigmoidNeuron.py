from Tester import Tester
from SigmoidNeuron import SigmoidNeuron
from testUtils import SimpleLine
from testUtils import generateRandomPoins


def main():
    tester = Tester()

    line = SimpleLine(1.5,10)
    train_set = generateRandomPoins(1000)
    valid_set = generateRandomPoins(1000)
    results_valid_set = []
    for (x,y) in valid_set:
        results_valid_set.append(line.isUpperLine(x,y)>0.5)

    train_set_sizes = range(1,1000,10) #[10,50,100,250,500,750,1000]
    learning_rates = [0.1,0.5,1.5]

    for lr in learning_rates:
        precisions = []
        for train_set_size in train_set_sizes:
            perceptron = SigmoidNeuron([2,2],2,lr)
            for index in range(train_set_size):
                (x,y) = train_set[index]
                perceptron.train([x,y],line.isUpperLine(x,y))
            precisions.append(tester.test(perceptron,valid_set,results_valid_set))
        tester.plot(train_set_sizes,precisions,"Presiciones por numero de muestras de entrenamiento, lr %.1f" % (lr))

if __name__ == '__main__':
    main()

