import Testing
import NeuralNet
import NeuralNetUtil

penData = Testing.buildExamplesFromPenData()


print "|&&&&&&&&&&&&&&&&&&&&|   PEN DATA TEST   |&&&&&&&&&&&&&&&&&&&&|"
penAcc = []
for i in range(5):
    print "Interation Number: ", i+1
    penNNet, accuracy = Testing.testPenData()
    penAcc.append(accuracy)
print "Results for Pen:"
print "Pen Max: ", max(penAcc)
print "Pen Average: ", Testing.average(penAcc)
print "Pen Standard Deviation: ", Testing.stDeviation(penAcc)
print "________________________________________________________________"
print "                           END OF PEN                           "
print "________________________________________________________________"



print "|&&&&&&&&&&&&&&&&&&&&|   CAR DATA TEST   |&&&&&&&&&&&&&&&&&&&&|"
carData = Testing.buildExamplesFromCarData()
carAcc = []
for i in range(5):
    print  "Interation Number: ", i+1
    carNNet, accuracy = Testing.testCarData()
    carAcc.append(accuracy)
print "Results for Car:"
print "Car Max: ", max(carAcc)
print "Car Average: ", Testing.average(carAcc)
print "Car Standard Deviation: ", Testing.stDeviation(carAcc)
print "________________________________________________________________"
print "                           END OF CAR                           "
print "________________________________________________________________"
