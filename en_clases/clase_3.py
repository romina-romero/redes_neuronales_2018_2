import clase_2
import math

class SigmoidNeuron(clase_2.TrainablePerceptron):
	def activation_function(self,z):
		return 1/(1+math.exp(z*-1))