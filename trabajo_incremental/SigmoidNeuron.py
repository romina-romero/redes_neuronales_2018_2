from Neuron import Neuron
import numpy as np

class SigmoidNeuron(Neuron):
	def activation_function(self,z):
		return 1/(1+np.exp(-1*z))