from sys import argv
from graph import *
from math import *

class gg(Digraph):
	def __init__(self): super().__init__()
	def add_vertex(self,v,f):
		super().add_vertex(v)
		self.graph[v]["flow"] = f
	def neighbors(self,n,v):
		if n not in g.graph: return []
		return [i for i in g.graph[n] if i != "flow" and i not in v]

g=gg()
f=open(argv[1],"r")
b=f.read().strip().split("\n")
bb=[i.split(";") for i in b]
for nf,nb in bb:
	nnf=nf.split()
	nnb=nb.split()
	vn=nnf[1]
	fr=int(nnf[-1].split("=")[1])
	nb=[i.replace(",","") for i in nnb[4:]]
	g.add_vertex(vn,fr)
	for n in nb:
		g.add_edge(vn,n,1)

def problem(g, c={}, n='AA', time=30, opened=[]):
	if time == 0: return 0
	a = 0
	if (n,time,"".join(opened)) in [*c.keys()]:
		return c[(n,time,"".join(opened))]

	if n not in opened and g.graph[n]["flow"] > 0:
		a = max(a, (time-1)*g.graph[n]["flow"]+problem(g,c,n,time-1,opened+[n]))
	else:
		for nn in g.neighbors(n,opened):
			a = max(a, problem(g,c,nn,time-1,opened))

	c[(n,time,"".join(opened))] = a

	return a

print(problem(g)) #p1
