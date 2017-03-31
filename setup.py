import network2
import random

class Setup:
    def __init__(self, numDevices, numNodes):
    	self.numDevices = numDevices
    	self.numNodes = numNodes
    	self.initNodes(numDevices, numNodes)
    	self.makeConnections(lowerConnect, upperConnect)

    def initNodes(self, numDevices, numNodes):
    	self.networkMap = {"Device": {}, "Router": {}}

    	for i in range(numDevices):
    		d = network2.Device()
    		self.networkMap["Device"][d.nodeID] = d

    	for j in range(numNodes):
    		n = Router()
    		self.networkMap["Router"][n.nodeID] = n

    def genLink(self, node1, node2):
    	lowerThroughput = 100
    	higherThroughput = 10e6
    	stepSize = 100
    	throughput = random.randrange(lowerThroughput, higherThroughput, stepSize)
    	node1.connect(node2, throughput)

    def makeConnections(self):
    	upperBound = int(self.numNodes * 0.75)
    	for i in range(self.numDevices + self.numNodes):
    		if i < self.numDevices:
    			currNode = self.networkMap["Device"][i]
    		else:
    			currNode = self.networkMap["Router"][i - self.numDevices]
    		currConn = currNode.numConnects()
    		numConn = random.randint(1, upperBound)
    		newConn = numConn - currConn
    		if newConn > 0:
    			newIDs = random.sample(self.networkMap["Router"], newConn)
    			for newID in newIDs:
    				node2 = self.networkMap["Router"][newID]
    				self.genLink(currNode, node2)

    def simulate(self, time):
    	# check all devices if they want to transmit
    	for i in range(self.numDevices):

    	# find shortest action
   		# fast forward time
   		# repeat until time is up 







s = Setup(3, 7)
        

