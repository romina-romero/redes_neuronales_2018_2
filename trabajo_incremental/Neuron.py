class Neuron:
    def __init__(self,weights,bias,lr=0.1):
        self.weights = weights
        self.bias = bias
        self.lr = lr
    def activation_function(self,z):
        '''interfaz'''
        return 0

    def feed(self,input_values):
        z = 0
        for index in range(len(self.weights)):
            z+=self.weights[index]*input_values[index]
        return self.activation_function(z)

    def train(self,input_values,real_output):
        desired_output = self.feed(input_values)
        diff = real_output - desired_output

        for index in range(len(self.weights)):
            self.weights[index] = self.weights[index]+self.lr*input_values[index]*diff
        self.bias = self.bias+self.lr*diff