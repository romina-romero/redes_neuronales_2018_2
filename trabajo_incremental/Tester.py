import matplotlib.pyplot as plt

def mirror(x):
	return x

class Tester:
	def __init__(self):
		pass

	def test(self,neuron,test_set,results, result_fun=mirror):
		corrects = 0
		total = len(test_set)
		for index in range(total):
			input_values = test_set[index]
			output_val = neuron.feed(input_values)
			if result_fun(output_val)==results[index]:
				corrects+=1
		return corrects*1.0/total

	def plot(self,x,y,title=''):
		plt.plot(x,y)
		plt.title(title)
		plt.show()