class Graph:
	def __init__(self):
		self.graph = {}
	
	def add_vertex(self, v):
		self.graph[v] = {}

	def add_edge(self, p1, p2, d):
		self.graph[p1][p2] = d
		self.graph[p2][p1] = d

class Digraph(Graph):
	def __init__(self):
		super().__init__()

	# single direction only
	def add_edge(self, p1, p2, d):
		self.graph[p1][p2] = d
