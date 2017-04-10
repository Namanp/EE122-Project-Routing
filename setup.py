import network
import random

class Setup:
    def __init__(self, numDevices, numNodes): #makes nodes and connections between them
    	self.numDevices = numDevices
    	self.numNodes = numNodes
    	self.initNodes(numDevices, numNodes)
    	self.makeConnections()

    def pickDevice(self,currDevice): #return a destination for a new packet
    	deviceList = dict(self.networkMap["Device"])
    	deviceList.remove(currDevice)
    	return random.sample(deviceList, 1)

    def initNodes(self, numDevices, numNodes): #creates routers and devices
    	self.networkMap = {"Device": [], "Router": []}

    	for i in range(numDevices):
    		d = network.Device()
    		self.networkMap["Device"].append(d)

    	for j in range(numNodes):
    		n = network.Router()
    		self.networkMap["Router"].append(n)

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
	    			newNodes = random.sample(self.networkMap["Router"], newConn)
	    			for newNode in newNodes:
	    				self.genLink(currNode, newNode)
	    	else: #connect device to router
	    		if not currNode.isConnected(): #connect only if the device is not already connected
		    		newNode = random.sample(self.networkMap["Router"], 1)
		    		self.genLink(currNode,newNode)


    def simulate(self, time):
        requestedRuntime = time

    	while time > 0:	
	    	# find shortest action
	    	minTime = 1e100
	    	for i in range(self.numDevices):
	    		time = self.networkMap["Device"][i].poll()
	    		if time < minTime:
	    			minTime = time
	    	for i in range(self.numNodes):
	    		time = self.networkMap["Router"][i].poll()
	    		if time < minTime:
	    			minTime = time
	   		# fast forward time
	   		for i in range(self.numDevices):
	   			currDevice = self.networkMap["Device"][i]
	   			destID = self.pickDevice(currDevice)
	   			currDevice.timePass(minTime, destID)
	   		for i in range(self.numNodes):
				self.networkMap["Router"][i].timePass(minTime)
			time -= minTime
   			# repeat until time is up or becomes negative


		timeElapsed = requestedRuntime - time
		return timeElapsed #can return more information as needed later



s = Setup(3, 7)
s.simulate(10e6)
        

