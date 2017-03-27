import random
import util

class Router:
	i = 0
	alpha = 0.1
	def __init__():
		self.id = Router.i #Assign unique ID
		Router.i += 1
		self.linkList = {}
		self.qValues = util.Counter()

	def connect(router2, throughput): #Forms a link/edge between two routers, can add more stuff later
		link = Link.__init__(self, router2, throughput)
		self.linkList[link] = (throughput)
		router2.linkList[self] = (throughput)

	def getNeighbors():
		return linkList.keys()

	def minQValue(dest): #used in updating Q-values
		return min([self.qValues[(dest, neighbor)] for neighbor in self.getNeighbors()])

	def qUpdate(nextQ, nextLink, dest):
		diff = (nextQ) - self.qValues[(dest, nextLink)] #can add queueing time here
		self.qValues[(dest,nextLink)] += Router.alpha * diff

	def route(packet): #Work in progress
		dest = packet.dest
		if dest == self:
			return 0

		yield self.minQValue(dest)

		minQ = 1e100
		minLink = None
		for neighbor in self.getNeighbors(): #finds minimum Q value neighbor
			nextQ = self.qValues[(dest, neighbor)]
			if nextQ < minQ:
				minQ = nextQ
				minLink = neighbor
		if minLink != None:
			neighborMinQ = minLink.route(packet)
			self.qUpdate(neighborminQ, minLink, dest)

class Packet:
	def __init__(source, destination, data):
		self.src = source
		self.dest = destination
		self.data = data
		