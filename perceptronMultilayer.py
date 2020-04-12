import math
import csv
from random import seed
from random import random
### Perceptron ###
class Neuron(object):
    def __init__(self, learningRate, bias):
        self.features = []
        self.learningRate = learningRate
        self.bias = bias
    def addFeatures(self, weights):
        for i in range(0, len(weights)):
            self.features.append( float(weights[i]) )
    def totalCharge(self, values):
        charge = 0
        for i in range(0, len(self.features)):
            charge += self.features[1] * float(values[i])
        return charge - self.bias
    def errorCorrection(self, values, error):
        for i in range(0, len(self.features)):
            self.features[i] -= self.learningRate * float(values[i]) * error
        self.bias -= self.learningRate * error
### Layer ###
class Layer(object):
    def __init__(self):
        self.neurons = []
    def addNeuron(self, learningRate, bias, weights):
        neuron = Neuron(learningRate, bias)
        neuron.addFeatures(weights)
        self.neurons.append(neuron)
    def activationOutput(self, value):
        return (1 / (1+ math.exp(-1 * value) ))
    def neuronCorrection(self, values, errors):
        for i in range(0, len(neurons)):
            self.neurons[i].errorCorrection(values, float(errors[i]))
### Data read, and Assignment###
file = 'irisMulti.csv'
with open(file, newline='') as csvfile:
    data = []
    for row in csv.reader( csvfile, delimiter=',' ):
        data.append(row)
### Layer Creation ###
seed(1)
learningRate = 0.1
numberOfEpochs = 1
numOutputs = 3
numFeatures = 4
hiddenLayer = Layer()
outputLayer = Layer()
for i in range(numOutputs):
    weights = [random() for i in range(5)]
    bias = weights.pop(4)
    hiddenLayer.addNeuron(learningRate, bias, weights)
### Supervised Training  ###
for epoch in range(numberOfEpochs):
    absSumDeviation = 0
    for dataPoint in data:
        perdictions = [ 1.1,1.1,1.1 ]
        values = dataPoint[:numFeatures]
        labels = []
        for i in range(numOutputs):
            labels.append( dataPoint[numFeatures+i] )
        #for i in range(numOutputs):
            #perdiction = cluster[i].totalCharge(values)
            #perdictions[].append( perdoctopm )
        for i in range(numOutputs):
            if int(labels[i]) != perdictions[i]:
                error = (float(labels[i]) - perdictions[i])
                absSumDeviation += abs(error)
                hiddenLayer.neurons[i].errorCorrection(values, error)
    # Calc. and Print accuracy
    print("EPOCH {} Results: MAD = {}".format(epoch + 1, '%.2f'%(absSumDeviation / len(data[0])) ))
