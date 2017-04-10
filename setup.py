import network
import random

class Setup:
    def __init__(self, numDevices, numNodes): #makes nodes and connections between them
    	self.numDevices = numDevices
    	self.numNodes = numNodes
    	self.initNodes(numDevices, numNodes)
    	self.makeConnections(lowerConnect, upperConnect)

    def pickDevice(self):
        

    def initNodes(self, numDevices, numNodes): #creates routers and devices
    	self.networkMap = {"Device": {}, "Router": {}}

    	for i in range(numDevices):
    		d = network.Device()
    		self.networkMap["Device"][d.ID] = d

    	for j in range(numNodes):
    		n = network.Router()
    		self.networkMap["Router"][n.ID] = n

    def genLink(self, node1, node2): #connects 2 things
    	lowerThroughput = 100
    	higherThroughput = 10e6
    	stepSize = 100
    	throughput = random.randrange(lowerThroughput, higherThroughput, stepSize)
    	node1.connect(node2, throughput)

    def makeConnections(self): #should randomly create connections between the current devices and routers
    	upperBound = int(self.numNodes * 0.75)
    	for i in range(self.numDevices + self.numNodes):
    		#find the thing
    		if i < self.numDevices:
    			currNode = self.networkMap["Device"][i]
    			isRouter = False
    		else:
    			currNode = self.networkMap["Router"][i - self.numDevices]
    			isRouter = True
    		#add connections depending on if it's a router or device
    		if isRouter: #connect router to random number of other routers
	    		currConn = currNode.numConnects()
	    		numConn = random.randint(1, upperBound)
	    		newConn = numConn - currConn
	    		if newConn > 0:
	    			newIDs = random.sample(self.networkMap["Router"], newConn)
	    			for newID in newIDs:
	    				node2 = self.networkMap["Router"][newID]
	    				self.genLink(currNode, node2)
	    	else: #connect device to router
	    		if not currNode.isConnected(): #connect only if the device is not already connected
		    		newID = random.sample(self.networkMap["Router"], 1)
		    		self.genLink(currNode,newID)


    def simulate(self, time):
    	# check all devices if they want to transmit
    	for i in range(self.numDevices):
            self.networkMap["Device"][i].transmit
    		
    	# find shortest action
   		# fast forward time
   		# check if any packets made it to destination
   		# repeat until time is up 







s = Setup(3, 7)
        

