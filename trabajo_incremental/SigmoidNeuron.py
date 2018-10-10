from Neuron import Neuron
import math

class SigmoidNeuron(Neuron):
	def activation_function(self,z):
		return 1/(1+math.exp(z*-1))

