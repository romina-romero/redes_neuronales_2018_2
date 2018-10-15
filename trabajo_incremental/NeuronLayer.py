class NeuronLayer:
    def __init__(self,neurons):
        self.neurons = neurons

    def feed(self,input_values):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.feed(input_values))

        return outputs
    def train(self,input_values):
        outputs = []
        for neuron in self.neurons:
            neuron.train(input_values)
            outputs.append(neuron.current_output)
        return outputs