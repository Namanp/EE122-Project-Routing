import random
import util

class Router:
	i = 0
	alpha = 0.1
	def __init__(self):
		self.id = Router.i #Assign unique ID
		Router.i += 1
		self.linkList = {} #dictionary of neighbors and the links to them
		self.qValues = util.Counter()

	def connect(self, router2, throughput): #Forms a link/edge between two routers, can add more stuff later
		link = Link.__init__(self, router2, throughput)
		self.linkList[link] = (throughput)
		router2.linkList[self] = (throughput)

	def getNeighbors(self):
		return linkList.keys()

	def minQValue(self, dest): #used in updating Q-values
		return min([self.qValues[(dest, neighbor)] for neighbor in self.getNeighbors()])

	def qUpdate(self, nextLink, dest):
		nextQ = nextLink.minQValue(dest) #gets t, the min Q-value from neighbor
		diff = (nextQ) - self.qValues[(dest, nextLink)] #can add queueing time here
		self.qValues[(dest,nextLink)] += Router.alpha * diff

	def route(self, packet): #work in progress, never returns True at the moment!
		dest = packet.dest
		if dest == self:

		minQ = 1e100
		minLink = None
		for neighbor in self.getNeighbors(): #finds minimum Q-value neighbor
			nextQ = self.qValues[(dest, neighbor)]
			if nextQ < minQ:
				minQ = nextQ
				minLink = neighbor
		if minLink != None:
			self.qUpdate(minLink, dest) #updates Q value based on the neighbor
			return minLink.route(packet) #forwards packet to neighbor, can tell if it arrived
		return False #packet dropped because there are no neighbors

class Packet:
	def __init__(self, source, destination, data, size):
		self.src = source
		self.dest = destination
		self.size = size
		self.data = data
		