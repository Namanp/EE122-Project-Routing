import random
import util

class Router:
	nodeID = 0

	def __init__(self):
		self.nodeID = Router.nodeID
		Router.nodeID += 1

		self.links = {} 
		self.qValues = util.Counter()
		self.queue = util.Queue()

		self.state = 0 
		self.target = None
		self.currThroughput = 0
		self.bitsRemaining = 0
		self.currentPacket = None

	def connect(self, router2, throughput): 
		self.links[router2.routeID] = throughput
		router2.links[self.nodeID] = throughput

	def getNeighbors(self):
		return self.links.keys()

	def minQValue(self, dest): 
		neighbors = self.getNeighbors()
		return min([self.qValues[(dest, neighbor)] for neighbor in neighbors])

	def qUpdate(self, nextRouter, dest):
		nextQ = nextRouter.minQValue(dest) 
		diff = (nextQ) - self.qValues[(dest, nextLink)] 
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
		if self.state == 0: 
			if not self.queue.isEmpty():
				self.currentPacket = self.queue.pop()
				self.state = 1 
				self.bitsRemaining = self.currentPacket.size
				dest = packet.destID
				minQ = 1e100
				minLink = None
				for neighbor in self.getNeighbors(): 
					nextQ = self.qValues[(dest, neighbor)]
					if nextQ <= minQ:
						minQ = nextQ
						minLink = neighbor
				self.target = minLink
				self.throughput = self.links[minLink][0]

		if self.state == 1: 
			self.bitsRemaining -= time * self.throughput 
			
			if bitsRemaining <= 0: 
				self.state = 0
				self.target.enqueue(self.currentPacket) 
				self.qUpdate(minLink, dest) 
				self.target = None
				self.throughput = 0
				self.bitsRemaining = 0
				self.currentPacket = None

	def poll():
		if bitsRemaining != 0 and self.throughput != 0: 
			return self.bitsRemaining / self.linkThroughput
		else: 
			return 1e100 

class Device(Router):

	def genPacket(self, device):
		return Packet(self.routeID, device.routeID, random.randint(160, 524280))

	def canTransmit(self):
		return self.state == 0

	def pickDevice(self, numDevices):
		a = 

	def transmit(self, numDevices):
		if self.state == 0 and random.random() < 0.5::
			packet = self.genPacket(device)
			self.enqueue(packet)

class Packet:

	def __init__(self, source, destination, size):
		self.srcID = source
		self.destID = destination
		self.size = size
		self.delay = 0




