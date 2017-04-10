import random
import util

class Thing:
	i = 0
	def __init__(self):
		self.id = Thing.i #Assign unique ID
		Thing.i += 1

class Device(Thing):
	def __init__(self):
		self.router = None
		self.throughput = 0
		#The following are for time_pass
		self.state = 0 #0 is free, 1 is busy
		self.bitsRemaining = 0
		self.packet = None
		Thing.__init__(self)

	def connect(self, router, throughput):
		self.router = router
		self.throughput = throughput
		router.devices[self] = throughput

	def time_pass(self, time, destination): #takes in time and destination ID
		if self.router and self.state == 0: #free and connected to internet
			if random.random() < 0.5: #with 50% probability, generate packet and send
				self.state = 1
				self.packet = Packet(self.id, destination, random.randint(160,524280))
				self.bitsRemaining = self.packet.size

		if self.state == 1: #transmitting, subtracts from bits remaining
			self.bitsRemaining -= time * self.throughput

			if bitsRemaining <= 0: #done transmitting
				self.state = 0
				self.router.enqueue(self.packet) #pushed to router
				self.bitsRemaining = 0
				self.packet = None

	def poll(): #return remaining time for event
		if bitsRemaining != 0 and self.throughput != 0: #how much time left to finish transmission
			return self.bitsRemaining / self.throughput
		else: #don't pick this event as taking minimum time because there's nothing going on here
			return 1e100

	def receive(self, packet):
		return True

class Router(Thing):
	alpha = 0.1
	def __init__(self):
		self.linkList = {} #dictionary of neighbors and the links to them
		self.qValues = util.Counter()
		self.queue = util.Queue()
		self.devices = {}
		#The following are for time_pass
		self.state = 0 #0 is free, 1 is busy
		self.target = None
		self.linkThroughput = 0
		self.bitsRemaining = 0
		self.currentPacket = None
		Thing.__init__(self)

	def connect(self, router2, throughput): #Forms a link/edge between two routers, can add more stuff later
		link = Link.__init__(self, router2, throughput)
		self.linkList[link] = (throughput)
		router2.linkList[self] = (throughput)

	def getNeighbors(self):
		return linkList.keys()

	def minQValue(self, dest): #used in updating Q-values
		neighbors = self.getNeighbors()
		return min([self.qValues[(dest, neighbor)] for neighbor in neighbors])

	def qUpdate(self, nextLink, dest):
		nextQ = nextLink.minQValue(dest) #gets t, the min Q-value from neighbor
		diff = (nextQ) - self.qValues[(dest, nextLink)] #can add queueing time here
		self.qValues[(dest,nextLink)] += Router.alpha * diff

	def sendToDevice(self, packet):
		return packet.dest.receive(packet)

	def enqueue(self, packet):
		self.queue.push(packet)

	def connected(self):
		return len(self.links.keys()) > 0

	def numConnects(self):
		return len(self.links.keys())

	def time_pass(self, time):
		if self.state == 0: #free
			self.currentPacket = self.queue.pop()
			if self.currentPacket: #packet actually exists and got dequeued
				self.state = 1 #busy
				self.bitsRemaining = self.currentPacket.size
				dest = packet.destID

				for device,throughput in self.devices: 
					if device.id == dest: #if the destination device is connected to router
						self.target = dest
						self.linkThroughput = throughput

				if self.target == None: #if we have to forward to a different router
					minQ = 1e100
					minLink = None
					for neighbor in self.getNeighbors(): #finds minimum Q-value neighbor
						nextQ = self.qValues[(dest, neighbor)]
						if nextQ <= minQ:
							minQ = nextQ
							minLink = neighbor
					if minLink != None: #set up to transmit to neighbor router
						self.target = minLink
						self.throughput = self.linkList[minLink][0]
					else: #no neighbors, reset state and discard packet
						self.state = 0
						self.packet = None
						self.bitsRemaining = 0

		if self.state == 1: #transmitting
			self.bitsRemaining -= time * self.throughput #actually transmit
			
			if bitsRemaining <= 0: #done transmitting, reset everything
				self.state = 0
				if type(self.target) == Router:
					self.target.enqueue(self.currentPacket) #puts packet in next router's queue
					self.qUpdate(minLink, dest) #updates Q value based on the neighbor
				self.target = None
				self.throughput = 0
				self.bitsRemaining = 0
				self.currentPacket = None

	def poll(): #return remaining time for event
		if bitsRemaining != 0 and self.throughput != 0: #how much time left to finish transmission
			return self.bitsRemaining / self.linkThroughput
		else: #don't pick this event as taking minimum time because there's nothing going on here
			return 1e100

class Packet:
	def __init__(self, source, destination, size):
		self.srcID = source
		self.destID = destination
		self.size = size
		self.delay = 0
		