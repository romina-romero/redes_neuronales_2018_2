class Neuron:
    def __init__(self, weights, bias, lr=0.1):
        self.weights = weights
        self.bias = bias
        self.lr = lr
        self.current_output = None
        self.current_delta = None

    def activation_function(self, z):
        return 0

    def feed(self,input_values):
        z = 0
        for index in range(len(self.weights)):
            z+=self.weights[index]*input_values[index]
        z+=self.bias
        self.current_output= self.activation_function(z)
        return self.current_output

    def _transferDerivative(self,value):
        return value*(1.0-value)
   
    def back_propagation(self,error):
        self.current_delta = error*self._transferDerivative(self.current_output)

    def trainLonely(self,input_values,real_output):
        desired_output = self.feed(input_values)
        diff = real_output - desired_output
        for index in range(len(self.weights)):
            self.weights[index] = self.weights[index]+self.lr*input_values[index]*diff
        self.bias = self.bias+self.lr*diff

    def train(self,input_values):
        #desired_output = self.feed(input_values)
        #diff = real_output - desired_output
        for index in range(len(self.weights)):
            self.weights[index] = self.weights[index]+self.lr*input_values[index]*self.current_delta
        self.bias = self.bias+self.lr*self.current_delta