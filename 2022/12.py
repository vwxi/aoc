from math import inf
from sys import argv
from graph import *

f=open(argv[1],"r")
b=[list(k) for k in f.read().lstrip().rstrip().split("\n")]

E=lambda e: b[e[1]][e[0]]

def S(e):
	if E(e) == 'S': return 0
	elif E(e) == 'E': return ord('z')-ord('a')
	else: return ord(E(e)) - ord('a')

class Graph:
	def __init__(self):
		self.graph = {}
	
	def add_vertex(self, v):
		self.graph[v] = {}

	def add_edge(self, p1, p2, d):
		self.graph[p1][p2] = d
		self.graph[p2][p1] = d

def dijkstra(g: Graph, s):
	dist = {i: inf for i in g.graph}
	Q = [i for i in g.graph]
	dist[s] = 0

	while len(Q) != 0:
		_t = {i: dist[i] for i in dist if i in Q}
		u = min(_t, key=_t.get)
		Q.remove(u)

		nn=[i for i in g.graph[u] if i in Q]
		for n in nn:
			alt = dist[u] + 1
			if alt < dist[n] and S(u) - S(n) <= 1: #p1: and S(n) - S(u) <= 1:
				dist[n] = alt

	return dist

start=None
end=None
for ii,i in enumerate(b):
	for jj,j in enumerate(i):
		if j=='S': start = (jj,ii)
		if j=='E': end = (jj,ii)

g=Graph()
[g.add_vertex((jj,ii)) for jj,_ in enumerate(i) for ii,i in enumerate(b)]

adj=[[-1,0],[1,0],[0,-1],[0,1]]
for ii,i in enumerate(b):
	for jj,j in enumerate(i):
		for ax,ay in adj:
			if 0 <= jj+ax < len(b[0]) and 0 <= ii+ay < len(b):
				g.add_edge((jj,ii), (jj+ax,ii+ay), S((jj+ax,ii+ay)))

#print(dijkstra(g,start)[end]) #p1
p2=dijkstra(g,end)
al={j: p2[j] for j in p2 if j in [i for i in g.graph.keys() if E(i) == 'a']}
print(p2[min(al,key=al.get)]) #p2
