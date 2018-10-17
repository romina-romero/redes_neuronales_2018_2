from Neuron import Neuron
import numpy as np
import unittest

def sigmoidFun(z):
    if z >= 0:
        a = np.exp(-1*z)
        return 1 / (1 +a)
    # if x is less than zero then z will be small, denom can't be
    # zero because it's 1+z.
    a = np.exp(z)
    return a / (1 + a)
    #return 1/(1+np.exp(-1*z)

class SigmoidNeuron(Neuron):
    def activation_function(self,z):
        return sigmoidFun(z)


class TestSigmoidNeuronMethods(unittest.TestCase):
    def testConstruct(self):
        sigmoidNeuron = SigmoidNeuron([1,2],3)
        self.assertEqual(sigmoidNeuron.weights[0],1)
        self.assertEqual(sigmoidNeuron.weights[1],2)
        self.assertEqual(sigmoidNeuron.bias,3)

    def testOutput(self):
        sigmoidNeuron = SigmoidNeuron([-1,2],3)
        self.assertAlmostEqual(sigmoidNeuron.feed([-10,-3]),sigmoidFun(-10*-1+-3*2+3))
        self.assertAlmostEqual(sigmoidNeuron.feed([5,6]),sigmoidFun(5*-1+6*2+3))

if __name__ == '__main__':
    unittest.main()