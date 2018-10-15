import random
from SigmoidNeuron import SigmoidNeuron
from NeuronLayer import NeuronLayer

class NeuralNetwork:
    def __init__(self,layers=[]):
        self.layers = layers
    def feed(self,input_values):
        prev_outputs = input_values
        for index in range(len(self.layers)):
            prev_outputs = self.layers[index].feed(prev_outputs)
        return prev_outputs
    
    def make(self,input_size,layer_sizes,lr=0.1):
        self.layers = []
        for layer_index in range(len(layer_sizes)):
            neurons = []
            for neuron_index in range(layer_sizes[layer_index]):
                ws = input_size
                if layer_index>0:
                    ws = layer_sizes[layer_index-1]
                weights = []
                for weight_index in range(ws):
                    weights.append(random.randint(-2,2))
                bias = random.randint(-2,2)
                neurons.append(SigmoidNeuron(weights,bias,lr))
            self.layers.append(NeuronLayer(neurons))

    def train(self,input_values,output_values):
        #evaluar la red
        outputs = self.feed(input_values)
        #error ultima capa
        last_layer = self.layers[len(self.layers)-1]
        for index in range(len(output_values)):
            error = output_values[index]-outputs[index]
            last_layer.neurons[index].back_propagation(error)
        #propagar
        for index in range(1,len(self.layers)):
            back_index = len(self.layers)-index
            prev_layer = self.layers[back_index-1]
            current_layer = self.layers[back_index]
            errors = [0]*len(prev_layer.neurons)
            #sumar errores
            for current_neuron in current_layer.neurons:
                for neuron_index in range(len(prev_layer.neurons)):
                    errors[neuron_index] += current_neuron.weights[neuron_index]*current_neuron.current_delta
                    prev_layer.neurons[neuron_index].back_propagation(error)
            #propagar
            for neuron_index in range(len(errors)):
                prev_layer.neurons[neuron_index].back_propagation(errors[neuron_index])
        #hacer entrenamiento
        prev_outputs = input_values
        for index in range(len(self.layers)):
            prev_outputs = self.layers[index].train(prev_outputs)