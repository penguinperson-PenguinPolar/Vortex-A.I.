import numpy

class NeuralNetwork:
	def __init__(self, numberOfOutputNerons, numberOfInputs, hiddenLayers=0, numberOfNeronsInEachHiddenLayer=0):
		self.numberOfOutputNerons = numberOfOutputNerons
		self.hiddenLayers = [[[[0 for k in range(numberOfInputs)] if i == 0 else [0 for k in range(numberOfNeronsInEachHiddenLayer)], 0] for j in range(numberOfNeronsInEachHiddenLayer)] for i in range(hiddenLayers)]
		self.neronsIn = [[[0 for j in range(numberOfNeronsInEachHiddenLayer)], 0] for i in range(numberOfInputs)]
		self.neronsOut = [[[0 for j in range(numberOfNeronsInEachHiddenLayer)], 0] for i in range(numberOfOutputNerons)]
	def calculate(self, datas):
		output0 = []
		for neron in self.neronsIn:
			sum = 0
			for i in range(len(neron[0])):
				sum += neron[0][i] * datas[self.neronsIn.index(neron)][i]	
			output0.append(1 / (1 + numpy.exp(-(sum + neron[1]))))
		outputs = []
		for hiddenLayer in self.hiddenLayers:
			for neron in hiddenLayer:
				sum = 0
				for i in range(len(neron[0])):
					sum += neron[0][i] * output0[i]
				outputs.append(1 / (1 + numpy.exp(-(sum + neron[1]))))
		print(outputs)
		output = []
		for neron in self.neronsOut:
			sum = 0
			for i in range(len(neron[0])):
				sum += neron[0][i] * datas[self.neronsIn.index(neron)][i]	
			output.append(1 / (1 + numpy.exp(-(sum + neron[1]))))
		return output

nn = NeuralNetwork(numberOfOutputNerons=1, numberOfInputs=3, hiddenLayers=1, numberOfNeronsInEachHiddenLayer=2)
print(nn.calculate([[1, 1], ]))
