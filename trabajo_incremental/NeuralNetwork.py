import random
from SigmoidNeuron import SigmoidNeuron
from NeuronLayer import NeuronLayer
import unittest

class NeuralNetwork:
    def __init__(self,layers=[]):
        self.layers = layers
    def feed(self,input_values):
        prev_outputs = input_values
        for index in range(len(self.layers)):
            prev_outputs = self.layers[index].feed(prev_outputs)
        return prev_outputs
    
    def print_arch(self):
        for layer in self.layers:
            print "***layer********"
            for neuron in layer.neurons:
                print "neurona*"
                print "pesos:",neuron.weights
                print "bias:",neuron.bias
                print "*"
            print "***end-layer****"

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

    def train(self,input_values,output_values,nbepoch=None):
        if nbepoch is not None:
            return self.train_with_dataset(input_values,output_values,nbepoch)
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
        return error

    def train_with_dataset(self,dataset,outputs_values,nbepoch):
        #entrenar con dataset entero. calcular error cuadratico sum(exp-real)2
        errors = []
        for epoch in range(nbepoch):
            error = 0
            for index in range(len(dataset)):
                error+=self.train(dataset[index],outputs_values[index])**2
            errors.append(error)
        return errors   
    def diff(self,n2):
        l = []
        for il in range(len(self.layers)):
            dneurons = []
            for ine in range(len(self.layers[il].neurons)):
                w = []
                for iw in range(len(self.layers[il].neurons[ine].weights)):
                    w.append(abs(self.layers[il].neurons[ine].weights[iw]-n2.layers[il].neurons[ine].weights[iw]))
                dneurons.append(SigmoidNeuron(w,abs(self.layers[il].neurons[ine].bias-n2.layers[il].neurons[ine].bias),self.layers[il].neurons[ine].lr))
            l.append(NeuronLayer(dneurons))
        return NeuralNetwork(l)
    def copy(self):
        l = []
        for layer in self.layers:
            neurons = []
            for neuron in layer.neurons:
                w = []
                for we in neuron.weights:
                    w.append(we)
                neurons.append(SigmoidNeuron(w,neuron.bias,neuron.lr))
            l.append(NeuronLayer(neurons))
        return NeuralNetwork(l)
        
class TestMakeNeuralNetwork(unittest.TestCase):
    def testMake(self):
        n = NeuralNetwork()
        n.make(5,[2,3],0.5)
        self.assertEqual(len(n.layers),2)
        #capa 1
        self.assertEqual(len(n.layers[0].neurons),2)
        self.assertEqual(len(n.layers[0].neurons[0].weights),5)
        self.assertEqual(len(n.layers[0].neurons[1].weights),5)
        #capa 2
        self.assertEqual(len(n.layers[1].neurons),3)
        self.assertEqual(len(n.layers[1].neurons[0].weights),2)
        self.assertEqual(len(n.layers[1].neurons[1].weights),2)
        self.assertEqual(len(n.layers[1].neurons[2].weights),2)
        #salidas
        self.assertEqual(len(n.feed([1,2,3,4,5])),3)

    def testCase1(self):
        n = NeuralNetwork()
        n.make(2,[1,1],0.5)
        neuron1 = n.layers[0].neurons[0]
        neuron1.bias = 0.5
        neuron1.weights = [0.4,0.3]

        neuron2 = n.layers[1].neurons[0] 
        neuron2.bias = 0.4
        neuron2.weights = [0.3]

        n.train([1,1],[1])

        self.assertAlmostEqual(neuron1.bias,0.502101508999489)
        self.assertAlmostEqual(neuron1.weights[0],0.40210150899948904)
        self.assertAlmostEqual(neuron1.weights[1],0.302101508999489)

        self.assertAlmostEqual(neuron2.bias,0.43937745312797394)
        self.assertAlmostEqual(neuron2.weights[0],0.33026254863991883)

    def testCase2(self):
        n = NeuralNetwork()
        n.make(2,[2,2],0.5)
        neuron1 = n.layers[0].neurons[0]
        neuron2 = n.layers[0].neurons[1]
        neuron3 = n.layers[1].neurons[0]
        neuron4 = n.layers[1].neurons[1]

        neuron1.bias = 0.5
        neuron1.weights = [0.7,0.3]
        neuron2.bias = 0.4
        neuron2.weights = [0.3,0.7]
        neuron3.bias = 0.3
        neuron3.weights = [0.2,0.3]
        neuron4.bias = 0.6
        neuron4.weights = [0.4,0.2]
        n.train([1,1],[1,1])
        self.assertAlmostEqual(neuron1.bias,0.5025104485493278)
        self.assertAlmostEqual(neuron1.weights[0],0.7025104485493278)
        self.assertAlmostEqual(neuron1.weights[1],0.3025104485493278)

        self.assertAlmostEqual(neuron2.bias,0.40249801135748337)
        self.assertAlmostEqual(neuron2.weights[0],0.30249802235748333)
        self.assertAlmostEqual(neuron2.weights[1],0.7024980113574834)
        
        self.assertAlmostEqual(neuron3.bias,0.3366295422515899)
        self.assertAlmostEqual(neuron3.weights[0],0.22994737881955657)
        self.assertAlmostEqual(neuron3.weights[1],0.32938362863950127)
        
        self.assertAlmostEqual(neuron4.bias,0.6237654881509048)
        self.assertAlmostEqual(neuron4.weights[0],0.41943005652646226)
        self.assertAlmostEqual(neuron4.weights[1],0.21906429169838573)
        
if __name__ == '__main__':
    unittest.main()