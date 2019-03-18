from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import random

import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def testxor():
    dataset = [[[0,0], [0]], [[0,1], [1]], [[1,0], [1]], [[1,1],[0]]]

    dataset = dataset * 200

    random.shuffle(dataset)

    seventy = int(0.7 * len(dataset))
    trainset = dataset[:seventy]
    testset = dataset[seventy:]

    s = open("q6XorResults.txt", "w")
    for x in range(11):
        results = []
        for i in range(5):
            builtnet = buildNeuralNet((trainset, testset), maxItr=200, hiddenLayerList=[x])
            results.append(builtnet[1])

        print("Hidden Layers: " + str(x) + "\n")
        print("Maximum: " + str(max(results)) + "\n")
        print("Average: " + str(average(results)) + "\n")
        print("Standard Deviation: " + str(stDeviation(results)) + "\n")

def main():
    testxor()
main()