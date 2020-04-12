import csv
from random import seed
from random import random
### Perceptron ###
class Neuron(object):
    def __init__(self, learningRate, bias):
        self.features = []
        self.learningRate = learningRate
        self.bias = bias
    def addFeatures(self, labels, weights):
        for i in range(0, len(weights)):
            self.features.append( [labels[i], float(weights[i])] )
    def checkCharge(self, values):
        charge = 0
        for i in range(0, len(self.features)):
            charge += self.features[i][1] * float(values[i])
        if charge - self.bias > 0: return -1
        else: return 1
    def errorCorrection(self, values, error):
        for i in range(0, len(self.features)):
            self.features[i][1] -= self.learningRate * float(values[i]) * error
        self.bias -= self.learningRate * error
### Data read, and Assignment###
file = 'iris.csv'
with open(file, newline='') as csvfile:
    data = []
    for row in csv.reader( csvfile, delimiter=',' ):
        data.append(row)
    #remove labels
    labels = data.pop(0)
### Training Setup ###
seed(1)
learningRate = 0.1
numberOfEpochs = 100
weights = [random() for i in range(5)]
bias = weights.pop(4)
neuron = Neuron(learningRate, bias)
neuron.addFeatures(labels, weights)
### Supervised Training  ###
for epoch in range(numberOfEpochs):
    errors = 0
    perdictions = []
    for dataPoint in data:
        trigger = 0
        values = dataPoint[:4]
        key = dataPoint[4]
        perdiction = neuron.checkCharge(values)
        perdictions.append( perdiction )
        if int(key) != perdiction:
            errors += 1
            neuron.errorCorrection(values, (float(key) - perdiction))
    # Calc. and Print accuracy
    print("EPOCH {}: Accuracy is {}%".format(epoch + 1, '%.2f'%( (len(perdictions) - errors) /  len(perdictions) * 100 ) ))
