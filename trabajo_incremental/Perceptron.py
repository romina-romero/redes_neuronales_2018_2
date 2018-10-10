import unittest
from Neuron import Neuron
class Perceptron(Neuron):
    def activation_function(self,z):
        if z>0:
            return 1
        return 0

class Binary_op:
    def __init__(self):
        self.perceptron = Perceptron([],0)
    def result(self,x,y):
        return self.perceptron.feed([x,y]) == 1

class And(Binary_op):
    def __init__(self):
        self.perceptron = Perceptron([2,2],-3)

class Or(Binary_op):
    def __init__(self):
        self.perceptron = Perceptron([3,3],-2)

class Nand(Binary_op):
    def __init__(self):
        self.perceptron = Perceptron([-2,-2],3)
class Not(Binary_op):
    def __init__(self):
        self.perceptron = Perceptron([-2],1)
    def result(self,x):
        return self.perceptron.feed([x])

class Sum_result:
    def __init__(self,result=0,carry=0):
        self.result = result
        self.carry = carry
    def __eq__(self,other):
        return (self.result==other.result) and (self.carry == other.carry)

class Sum_bits:
    def  __init__(self):
        self.nand_obj = Nand()
        
    def result(self,x1,x2):
        r1 = self.nand_obj.result(x1,x2)
        r2_1 = self.nand_obj.result(x1,r1)
        r2_2 = self.nand_obj.result(r1,x2)
        carry = self.nand_obj.result(r1,r1)
        result = self.nand_obj.result(r2_1,r2_2)
        return Sum_result(result,carry)

class TestStringMethods(unittest.TestCase):
    def test_and(self):
        and_obj = And()
        self.assertEqual(and_obj.result(1,1),1)
        self.assertEqual(and_obj.result(1,0),0)
        self.assertEqual(and_obj.result(0,1),0)
        self.assertEqual(and_obj.result(0,0),0)

    def test_or(self):
        or_obj = Or()
        self.assertEqual(or_obj.result(1,1),1)
        self.assertEqual(or_obj.result(1,0),1)
        self.assertEqual(or_obj.result(0,1),1)
        self.assertEqual(or_obj.result(0,0),0)

    def test_nand(self):
        nand_obj = Nand()
        self.assertEqual(nand_obj.result(1,1),0)
        self.assertEqual(nand_obj.result(1,0),1)
        self.assertEqual(nand_obj.result(0,1),1)
        self.assertEqual(nand_obj.result(0,0),1)

    def test_not(self):
        not_obj = Not()
        self.assertEqual(not_obj.result(1),0)
        self.assertEqual(not_obj.result(0),1)

    def test_sum_bits(self):
        sum_bits_obj = Sum_bits()
        self.assertEqual(sum_bits_obj.result(0,0),Sum_result(0,0))
        self.assertEqual(sum_bits_obj.result(1,0),Sum_result(1,0))
        self.assertEqual(sum_bits_obj.result(0,1),Sum_result(1,0))
        self.assertEqual(sum_bits_obj.result(1,1),Sum_result(0,1))

if __name__ == '__main__':
    unittest.main()