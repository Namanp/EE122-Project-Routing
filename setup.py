import network
import random
import copy

class Setup:
	def __init__(self, numDevices, numNodes, configuration=0): #makes nodes and connections between them
		if not random:
			self.numDevices = numDevices
			self.numNodes = numNodes
			self.initNodes(numDevices, numNodes)
			self.makeConnections()
		else: #for testing
			self.manual(configuration)

	def manual(self, configuration):
		if configuration == "Simple":
			self.numDevices = 2
			self.numNodes = 2
			self.initNodes(2,2)
			self.genLink(self.networkMap["Device"][0], self.networkMap["Router"][0])
			self.genLink(self.networkMap["Device"][1], self.networkMap["Router"][1])
			self.genLink(self.networkMap["Router"][0], self.networkMap["Router"][1])
		elif configuration == "Diamond": #0 and 3
			self.numDevices = 5
			self.numNodes = 4
			self.initNodes(5,4)
			self.genLink(self.networkMap["Device"][0], self.networkMap["Router"][3])
			self.genLink(self.networkMap["Device"][1], self.networkMap["Router"][0])
			self.genLink(self.networkMap["Device"][2], self.networkMap["Router"][2])
			self.genLink(self.networkMap["Device"][3], self.networkMap["Router"][0])
			self.genLink(self.networkMap["Device"][4], self.networkMap["Router"][1])
			self.genLink(self.networkMap["Router"][0], self.networkMap["Router"][1])
			self.genLink(self.networkMap["Router"][0], self.networkMap["Router"][2])
			self.genLink(self.networkMap["Router"][1], self.networkMap["Router"][2])
			self.genLink(self.networkMap["Router"][1], self.networkMap["Router"][3])
			self.genLink(self.networkMap["Router"][2], self.networkMap["Router"][3])
		elif configuration == "6x6":
			self.numDevices = 19
			self.numNodes = 36
			self.initNodes(19,36)

			for i in range(0,36,2): #Want to look at devices #30 and #35
				self.genLink(self.networkMap["Device"][i//2], self.networkMap["Router"][i])
			self.genLink(self.networkMap["Device"][18], self.networkMap["Router"][35])

			self.genLink(self.networkMap["Router"][0], self.networkMap["Router"][1])
			self.genLink(self.networkMap["Router"][1], self.networkMap["Router"][2])
			self.genLink(self.networkMap["Router"][2], self.networkMap["Router"][3])
			self.genLink(self.networkMap["Router"][3], self.networkMap["Router"][4])
			self.genLink(self.networkMap["Router"][4], self.networkMap["Router"][5])

			self.genLink(self.networkMap["Router"][0], self.networkMap["Router"][6])
			self.genLink(self.networkMap["Router"][7], self.networkMap["Router"][8])
			self.genLink(self.networkMap["Router"][9], self.networkMap["Router"][10])
			self.genLink(self.networkMap["Router"][5], self.networkMap["Router"][11])

			self.genLink(self.networkMap["Router"][6], self.networkMap["Router"][12])
			self.genLink(self.networkMap["Router"][12], self.networkMap["Router"][13])
			self.genLink(self.networkMap["Router"][7], self.networkMap["Router"][13])
			self.genLink(self.networkMap["Router"][8], self.networkMap["Router"][14])
			self.genLink(self.networkMap["Router"][13], self.networkMap["Router"][14])
			self.genLink(self.networkMap["Router"][14], self.networkMap["Router"][15])
			self.genLink(self.networkMap["Router"][9], self.networkMap["Router"][15])
			self.genLink(self.networkMap["Router"][10], self.networkMap["Router"][16])
			self.genLink(self.networkMap["Router"][15], self.networkMap["Router"][16])
			self.genLink(self.networkMap["Router"][16], self.networkMap["Router"][17])
			self.genLink(self.networkMap["Router"][11], self.networkMap["Router"][17])

			self.genLink(self.networkMap["Router"][12], self.networkMap["Router"][18])
			self.genLink(self.networkMap["Router"][18], self.networkMap["Router"][19])
			self.genLink(self.networkMap["Router"][13], self.networkMap["Router"][19])
			self.genLink(self.networkMap["Router"][19], self.networkMap["Router"][20])
			self.genLink(self.networkMap["Router"][14], self.networkMap["Router"][20])

			self.genLink(self.networkMap["Router"][15], self.networkMap["Router"][21])
			self.genLink(self.networkMap["Router"][21], self.networkMap["Router"][22])
			self.genLink(self.networkMap["Router"][16], self.networkMap["Router"][22])
			self.genLink(self.networkMap["Router"][22], self.networkMap["Router"][23])
			self.genLink(self.networkMap["Router"][17], self.networkMap["Router"][23])

			self.genLink(self.networkMap["Router"][18], self.networkMap["Router"][24])
			self.genLink(self.networkMap["Router"][24], self.networkMap["Router"][25])
			self.genLink(self.networkMap["Router"][19], self.networkMap["Router"][25])
			self.genLink(self.networkMap["Router"][25], self.networkMap["Router"][26])
			self.genLink(self.networkMap["Router"][20], self.networkMap["Router"][26])

			self.genLink(self.networkMap["Router"][21], self.networkMap["Router"][27])
			self.genLink(self.networkMap["Router"][27], self.networkMap["Router"][28])
			self.genLink(self.networkMap["Router"][22], self.networkMap["Router"][28])
			self.genLink(self.networkMap["Router"][28], self.networkMap["Router"][29])
			self.genLink(self.networkMap["Router"][23], self.networkMap["Router"][29])

			self.genLink(self.networkMap["Router"][24], self.networkMap["Router"][30])
			self.genLink(self.networkMap["Router"][30], self.networkMap["Router"][31])
			self.genLink(self.networkMap["Router"][25], self.networkMap["Router"][31])
			self.genLink(self.networkMap["Router"][31], self.networkMap["Router"][32])
			self.genLink(self.networkMap["Router"][26], self.networkMap["Router"][32])

			self.genLink(self.networkMap["Router"][27], self.networkMap["Router"][33])
			self.genLink(self.networkMap["Router"][33], self.networkMap["Router"][34])
			self.genLink(self.networkMap["Router"][28], self.networkMap["Router"][34])
			self.genLink(self.networkMap["Router"][34], self.networkMap["Router"][35])
			self.genLink(self.networkMap["Router"][29], self.networkMap["Router"][35])

		else:
			return
		for dev in self.networkMap["Device"]:
			dev.dijikstra()

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
				print(currNode.ID, currConn)
				#print("upperBound", upperBound)
				numConn = random.randint(1, upperBound)
				newConn = numConn - currConn
				if newConn > 0:
					copy = list(self.networkMap["Router"])
					copy.remove(currNode)
					print(copy)
					newNodes = random.sample(copy, newConn)
					for newNode in newNodes:
						self.genLink(currNode, newNode)
			else: #connect device to router
				if not currNode.isConnected(): #connect only if the device is not already connected
					newNode = random.sample(self.networkMap["Router"], 1)
					self.genLink(currNode,newNode[0])

		for dev in self.networkMap["Device"]:
			dev.dijikstra()

	def pickDevice(self, currDevice, shape): #return a destination for a new packet
		if shape == "6x6":
			if currDevice.ID == 15:
				return self.networkMap["Device"][18]
			if currDevice.ID == 18:
				return self.networkMap["Device"][15]
		if shape == "Diamond":
			if currDevice.ID == 0:
				return self.networkMap["Device"][3]
			if currDevice.ID == 3:
				return self.networkMap["Device"][0]
		deviceList = list(self.networkMap["Device"])
		deviceList.remove(currDevice)
		return random.sample(deviceList, 1)[0]

	def allEmpty(self):
		for router in self.networkMap["Router"]:
			if not router.isEmpty():
				print("Failure")
				return
		print("Success")

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
				print("router", currNode.ID)
				print("devices", [device.ID for device in currNode.devices.keys()])
				print("routers", [router.ID for router in currNode.linkList.keys()])
			else: #connect device to router
				print("device id", currNode.ID)
				print("router", currNode.router.ID)


	def simulate(self, time, protocol=False, shape=False):
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
				dest = self.pickDevice(currDevice, shape)
				currDevice.timePass(minTime, dest, protocol)
			for i in range(self.numNodes):
				self.networkMap["Router"][i].timePass(minTime, protocol)
			time -= minTime
			#print("minTime", minTime)
			# repeat until time is up or becomes negative
		timeElapsed = requestedRuntime - time
		return timeElapsed #can return more information as needed later

	def getCompleted(self):
		for device in self.networkMap["Device"]:
			print(device.ID)
			print(device.completed)

	def completeForDevice(self, device1ID, device2ID):
		return self.networkMap["Device"][device2ID].completed[device1ID]

	def testD(self):
		dev = self.networkMap["Device"][0]
		dev.dijikstra()
		path = dev.findPath(self.networkMap["Device"][3])
		print(path)

	def computeAvg(self, timeLsts):
		return sum([time[1]/time[0] for time in timeLsts])/len(timeLsts)


s = Setup(5, 4, "6x6") #Simple, Diamond, or 6x6
#s.getMap()
# s.testD()
sCopy = copy.deepcopy(s)
avg1 = []
avg2 = []
s.simulate(10,False, "6x6")
for i in range(1):
	s.simulate(100, True, "6x6")
	sCopy.simulate(100, False, "6x6")
	completed1 = s.getCompleted()
	completed2 = sCopy.getCompleted() 
	avg1.append(s.computeAvg(completed1))
	avg2.append(sCopy.computeAvg(completed2))
print("avg1", avg1)
print("avg2", avg2)


