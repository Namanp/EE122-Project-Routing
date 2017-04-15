import network
import random

class Setup:
	def __init__(self, numDevices, numNodes, random=True): #makes nodes and connections between them
		if random:
			self.numDevices = numDevices
			self.numNodes = numNodes
			self.initNodes(numDevices, numNodes)
			self.makeConnections()
		else: #for testing
			self.manual()

	def manual(self):
		self.numDevices = 2
		self.numNodes = 2
		self.initNodes(2,2)
		self.genLink(self.networkMap["Device"][0], self.networkMap["Router"][0])
		self.genLink(self.networkMap["Device"][1], self.networkMap["Router"][1])
		self.genLink(self.networkMap["Router"][0], self.networkMap["Router"][1])

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
		upperBound = max([1, int(self.numNodes * 0.75)])
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
				print("upperBound", upperBound)
				numConn = random.randint(1, upperBound)
				newConn = numConn - currConn
				if newConn > 0:
					newNodes = random.sample(self.networkMap["Router"], newConn)
					for newNode in newNodes:
						self.genLink(currNode, newNode)
			else: #connect device to router
				if not currNode.isConnected(): #connect only if the device is not already connected
					newNode = random.sample(self.networkMap["Router"], 1)
					self.genLink(currNode,newNode[0])

	def pickDevice(self,currDevice): #return a destination for a new packet
		deviceList = list(self.networkMap["Device"])
		deviceList.remove(currDevice)
		return random.sample(deviceList, 1)[0]

	def getMap(self):
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
				print("router id", currNode.ID)
				print("devices", currNode.devices)
				print("routers", currNode.linkList)
			else: #connect device to router
				print("device id", currNode.ID)
				print("router", currNode.router)


	def simulate(self, time):
		requestedRuntime = time
		while time > 0:	
			# find shortest action
			minTime = 1e100
			for i in range(self.numDevices):
				pollTime = self.networkMap["Device"][i].poll()
				if pollTime < minTime:
					minTime = pollTime
			for i in range(self.numNodes):
				pollTime = self.networkMap["Router"][i].poll()
				if pollTime < minTime:
					minTime = pollTime
			# fast forward time
			for i in range(self.numDevices):
				currDevice = self.networkMap["Device"][i]
				dest = self.pickDevice(currDevice)
				currDevice.timePass(minTime, dest)
			for i in range(self.numNodes):
				self.networkMap["Router"][i].timePass(minTime)
			time -= minTime
			print("minTime", minTime)
			# repeat until time is up or becomes negative
		timeElapsed = requestedRuntime - time
		return timeElapsed #can return more information as needed later

	def getCompleted(self):
		for device in self.networkMap["Device"]:
			print(device.ID)
			print(device.completed)


s = Setup(2, 1, False)
s.getMap()
s.simulate(10e1)
s.getCompleted()


        

