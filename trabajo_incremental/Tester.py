import matplotlib.pyplot as plt
import math
from scipy.spatial import distance

def mirror(x):
    return x

class Tester:
    def __init__(self):
        pass

    def test(self,neuron,test_set,results, result_fun=mirror):
        corrects = 0
        total = len(test_set)
        for index in range(total):
            input_values = test_set[index]
            output_val = neuron.feed(input_values)
            if result_fun(output_val)==results[index]:
                corrects+=1
        return corrects*1.0/total

    def testNetwork(self,network,test_set,results,max_dist=0.5):
        corrects = 0
        total = len(test_set)
        for index in range(total):
            input_values = test_set[index]
            output_values = network.feed(input_values)
            if distance.euclidean(output_values,[results[index]])<=max_dist:
                corrects+=1
        return corrects*1.0/total

    def plot(self,x,y,title=''):
        plt.ylim([0,1])
        plt.plot(x,y)
        plt.title(title)
        plt.xlabel("cantidad de entrenamientos")
        plt.ylabel("Presicion")
        plt.show()