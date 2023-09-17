def k(a,b):
	q=set([*range(a[0],a[1]+1)])
	w=set([*range(b[0],b[1]+1)])
	m=q.issuperset(w) or w.issuperset(q)
	j=len(list(q&w))!=0
	return m #p1
	return j #p2

from sys import argv
f=open(argv[1],"r")
a=f.read().lstrip().rstrip()
c=[[[int(i) for i in j.split("-")] for j in k.split(",")] for k in a.split("\n")]
d=0
for i in c:
	if k(*i): d += 1
print(d)
