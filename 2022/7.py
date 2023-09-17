class node:
	def __init__(self, parent, val=None, size=0, end=False):
		self.val = val
		self.size = size
		self.parent = parent
		self.children = {}
		self.end = end

	def __repr__(self):
		s="node(val={}, size={}, parent={}, children=[{}], end={})".format(
			self.val, self.size, self.parent.__repr__(), ", ".join([i.__repr__() for i in self.children]), self.end
		)
		return s

from sys import argv
f=open(argv[1],"r")
b=f.read().lstrip().rstrip().split("\n")
n=node(None, "/")
k=n
for i in range(len(b)):
	if b[i][0]=="$":
		d=b[i].split(" ")[1:]
		if d[0]=="cd":
			if d[1]=="..":
				n=n.parent
			else:
				n.children[d[1]] = node(n, d[1])
				n = n.children[d[1]]
		elif d[0]=="ls":
			for j in range(len(b[i+1:])):
				fn=b[i+1:][j].split(" ")
				if fn[0]=="$":
					break
				elif fn[0]=="dir":
					n.children[fn[1]] = node(n)
				else:
					n.children[fn[1]] = node(n, fn[1], int(fn[0]), True)

c=0
def sizes(n):
	global c

	if n.end: 
		n.parent.size += n.size
		return

	for i in n.children:
		sizes(n.children[i])

	if n.parent != None:
		n.parent.size += n.size

	if n.size <= 100000:
		c += n.size

d=0
def remove(n):
	global d
	q = 70000000 - k.size
	
	if n.end: return
	for i in n.children: remove(n.children[i])
	if q+n.size > 30000000:
		d = n.size if d == 0 else min(d, n.size)

sizes(k)
remove(k)
print(c) #p1
print(d) #p2
