import Testing
import NeuralNet
import NeuralNetUtil

#penData = Testing.buildExamplesFromPenData()


print "|&&&&&&&&&&&&&&&&&&&&|   PEN DATA TEST   |&&&&&&&&&&&&&&&&&&&&|"
penPerceptAcc =[]
numPerceptrons = 0
while numPerceptrons <= 40:
    print "Number of Perceptrons: ", numPerceptrons
    penAcc = []
    for i in range(5):
        print "Interation Number: ", i+1
        penNNet, accuracy = NeuralNet.buildNeuralNet(Testing.penData, maxItr=200, hiddenLayerList=[numPerceptrons])
        penAcc.append(accuracy)
    penPerceptAcc.append(penAcc)
    numPerceptrons = numPerceptrons + 5
print "Results of Pen Test:"
for i in range(len(penPerceptAcc)):
    print i
    print "Max Accuracy: ", max(penPerceptAcc[i])
    print "Average Accuracy: ", Testing.average(penPerceptAcc[i])
    print "Standard Deviation: ", Testing.stDeviation(penPerceptAcc[i])
print "________________________________________________________________"
print "                           END OF PEN                           "
print "________________________________________________________________"



print "|&&&&&&&&&&&&&&&&&&&&|   CAR DATA TEST   |&&&&&&&&&&&&&&&&&&&&|"

#carData = Testing.buildExamplesFromCarData()
carPerceptAcc =[]
numPerceptrons = 0
while numPerceptrons <= 40:
    print "Number of Perceptrons: ", numPerceptrons
    carAcc = []
    for i in range(5):
        print "Interation Number: ", i+1
        carNNet, accuracy = NeuralNet.buildNeuralNet(Testing.carData, maxItr=200, hiddenLayerList=[numPerceptrons])
        carAcc.append(accuracy)
    carPerceptAcc.append(carAcc)
    numPerceptrons = numPerceptrons + 5
print "Results of Car Test:"
for i in range(len(carPerceptAcc)):
    print i
    print "Max Accuracy: ", max(carPerceptAcc[i])
    print "Average Accuracy: ", Testing.average(carPerceptAcc[i])
    print "Standard Deviation: ", Testing.stDeviation(carPerceptAcc[i])
print "________________________________________________________________"
print "                           END OF CAR                           "
print "________________________________________________________________"
