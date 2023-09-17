o = {'X': {'A': 0, 'B': -1, 'C': 1}, 'Y': {'A': 1, 'B': 0, 'C': -1}, 'Z': {'A': -1, 'B': 1, 'C': 0}}
a = {'A': {'X': 0, 'Y': 1, 'Z': -1}, 'B': {'X': -1, 'Y': 0, 'Z': 1}, 'C': {'X': 1, 'Y': -1, 'Z': 0}}
r = {'X': 1, 'Y': 2, 'Z': 3, -1: 0, 0: 3, 1: 6}
p = {'X': -1, 'Y': 0, 'Z': 1}
h = lambda k,v: list(k.keys())[list(k.values()).index(v)]
def q(s):
	w=[[j for j in k.split(' ')] for k in s.split('\n')]
	z=[r[w[i][1]]+r[o[w[i][1]][w[i][0]]] for i in range(len(w))]
	e=[r[h(a[w[i][0]],p[w[i][1]])]+r[p[w[i][1]]] for i in range(len(w))]
	return sum(e)

from sys import argv
f=open(argv[1],"r")
b=f.read().lstrip().rstrip()
print(q(b))
