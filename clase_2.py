import random
import clase_1
import matplotlib.pyplot as plt

class TrainablePerceptron (clase_1.Perceptron):
    def __init__(self,weights,bias,lr):
        clase_1.Perceptron.__init__(self,weights,bias)
        self.lr=lr

    def train(self,input_values,real_output):
        desired_output = self.feed(input_values)
        diff = desired_output-real_output

        for index in range(len(self.weights)):
            self.weights[index] = self.weights[index]+self.lr*input_values[index]*diff
        self.bias = self.bias+self.lr*diff


class SimpleLine:
    def __init__(self,m,n):
        self.m = m
        self.n = n

    def isUpperLine(self,x,y):
        calc_y = self.m*x+self.n
        if calc_y>y:
            return 1
        return 0
    def getY(self,x):
        return self.m*x+self.n

def generateRandomPoins(n):
    pointsList = []
    for i in range(n):
        pointsList.append((random.randint(-10000,10000),random.randint(-10000,10000)))
    return pointsList

class TestResult:
    def __init__(self,precision,upper_xs,upper_ys,down_xs,down_ys):
        self.precision = precision
        self.upper_xs = upper_xs
        self.upper_ys = upper_ys
        self.down_xs = down_xs
        self.down_ys = down_ys

def test(perceptron,pointsList,line):
    corrects = 0
    total = len(pointsList)
    upper_xs = []
    upper_ys = []
    down_xs = []
    down_ys = []
    for index in range(total):
        (x,y) = pointsList[index]
        is_upper_point = perceptron.feed([x,y])
        if is_upper_point==0:
            if line.isUpperLine(x,y):
                corrects+=1
            upper_xs.append(x)
            upper_ys.append(y)
        else:
            if not line.isUpperLine(x,y):
                corrects+=1
            down_xs.append(x)
            down_ys.append(y)
    return TestResult(corrects*1.0/total,upper_xs,upper_ys,down_xs,down_ys)

#grafica los puntos en el plano con colores segun clasificacion de perceptron
def plotPointsAndLine(line,test_result,title):
    plt.plot([-10000,10000],[line.getY(-10000),line.getY(10000)])
    plt.plot(test_result.upper_xs, test_result.upper_ys, 'ro')
    plt.plot(test_result.down_xs, test_result.down_ys, 'bo')
    plt.title(title)
    plt.show()

def main():

    line = SimpleLine(1.5,10)

    train_set = generateRandomPoins(1000)
    valid_set = generateRandomPoins(1000)

    train_set_sizes = [10,50,100,250,500,750,1000]
    learning_rates = [0.1,0.5,1.5]

    subplot_index = 0
    offset_plot = 0

    for lr in learning_rates:
        precisions = []
        for train_set_size in train_set_sizes:
            perceptron = TrainablePerceptron([1,1],1,lr)
            for index in range(train_set_size):
                (x,y) = train_set[index]
                perceptron.train([x,y],line.isUpperLine(x,y))
            tr = test(perceptron,valid_set,line)
            precisions.append(tr.precision)
            #descomentar para ver graficos de predicciones vs realidad
            #plotPointsAndLine(line,tr,"After %d trainings, lr=%.1f" % (train_set_size,lr))
        plt.subplot(311+offset_plot)
        plt.plot(train_set_sizes,precisions)
        plt.title("Presiciones por numero de muestras de entrenamiento, lr %.1f" % (lr))
        offset_plot+=1
    plt.subplots_adjust(hspace=1)

    plt.show()
if __name__ == '__main__':
    main()