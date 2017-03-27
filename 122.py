import random

class Router:
	i = 0
	def __init__():
		self.id = Router.i #Assign unique ID
		Router.i += 1
		self.linkList = []

	def connect(router2, throughput):
		link = Link.__init__(self, router2, throughput)
		self.linkList.append(link)
		router2.linkList.append(link)

class Link:
	def __init__(router1, router2, throughput):
		self.r1 = router1
		self.r2 = router2
		self.throughput = throughput
		self.relMean = random.random() #Reliability in [0,1)