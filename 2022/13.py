from sys import argv
from functools import cmp_to_key
f=open(argv[1],"r")
d=f.read().lstrip().rstrip()
b=[[eval(j) for j in i.split("\n")] for i in d.split("\n\n")]
def check(l,r):
	if type(l) == int and type(r) == int:
		if l == r: return None
		return l < r
	if type(l) == list and type(r) == list:
		for ll,rr in zip(l,r):
			q=check(ll,rr)
			if q != None: return q
		return check(len(l),len(r))
	if type(l) == list and type(r) == int:
		return check(l,[r])
	if type(l) == int and type(r) == list:
		return check([l],r)
				
	return False

class e:
	def __init__(self, ar):
		self.ar = ar

	def __lt__(self, o):
		return check(self.ar,o.ar)

c=[*[e(eval(i)) for i in [*filter(''.__ne__, d.split("\n"))]], e([[2]]), e([[6]])]
r=0
for ii,i in enumerate(b):
	if check(i[0],i[1]): r+=ii+1
print(r) #p1
c.sort()
v=1
for ii,i in enumerate(c):
	if i.ar==[[2]] or i.ar==[[6]]:
		v *= ii+1
print(v) #p2
