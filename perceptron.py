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
    def checkCharge(self, values):
        charge = 0
        for i in range(0, len(self.features)):
            charge += self.features[1] * float(values[i])
        if charge - self.bias > 0: return -1
        else: return 1
    def errorCorrection(self, values, error):
        for i in range(0, len(self.features)):
            self.features[i] -= self.learningRate * float(values[i]) * error
        self.bias -= self.learningRate * error
### Data read, and Assignment###
file = 'iris.csv'
with open(file, newline='') as csvfile:
    data = []
    for row in csv.reader( csvfile, delimiter=',' ):
        data.append(row)
### Neuron Creation ###
seed(1)
learningRate = 0.1
numberOfEpochs = 100
weights = [random() for i in range(5)]
bias = weights.pop(4)
neuron = Neuron(learningRate, bias)
neuron.addFeatures( weights)
### Supervised Training  ###
for epoch in range(numberOfEpochs):
    errors = 0
    perdictions = []
    for dataPoint in data:
        values = dataPoint[:4]
        label = dataPoint[4]
        perdiction = neuron.checkCharge(values)
        perdictions.append( perdiction )
        if int(label) != perdiction:
            errors += 1
            neuron.errorCorrection(values, (float(label) - perdiction))
    # Calc. and Print accuracy
    print("EPOCH {}: Accuracy is {}%".format(epoch + 1, '%.2f'%( (len(perdictions) - errors) /  len(perdictions) * 100 ) ))
