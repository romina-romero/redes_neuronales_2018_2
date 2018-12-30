from neural_network.NeuralNetwork import NeuralNetwork
import random


class Individual:

    def __init__(self, neural_network):
        self.neural_network = neural_network

    def crossover(self, individual2, fitness):
        fitness1 = fitness(self)
        fitness2 = fitness(individual2)
        vector1 = self.neural_network.get_neuron_vector()
        vector2 = individual2.neural_network.get_neuron_vector()
        layer_sizes = self.neural_network.get_layer_sizes()
        #ver proporcion segun fitness
        central_point = int(round(fitness1*len(vector1)/max(fitness1+fitness2,1)))
    # print("crsover f1 = %.3f, f2 = %.3f, cp = %d, len=%d" % (fitness1, fitness2, central_point, len(vector1)))
        #crossover
        neurons_final = vector1[:central_point]+vector2[central_point:]
        neural_network = NeuralNetwork()
        neural_network.make_from_neuron_vector(neurons_final,layer_sizes)
        return Individual(neural_network)

    def mutate(self):
        neuron_vector = self.neural_network.get_neuron_vector()
        mneuron = neuron_vector[random.randint(0, len(neuron_vector)-1)]
        bias = random.randint(0,1)
        if bias == 1:
            mneuron.bias = random.uniform(-2,2)
        else:
            mneuron.weights[random.randint(0, len(mneuron.weights)-1)] = random.uniform(-2, 2)

