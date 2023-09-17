from string import ascii_letters as al

def r(q):
	d=0
	for s in q:
		l=len(s)//2
		k=list(set(s[:l]).intersection(s[l:]))[0]
		d+=al.index(k)+1

	return d

def v(q):
	w=[q[i:i+3] for i in range(0,len(q),3)]
	return sum([al.index(list(set.intersection(*map(set,i)))[0])+1 for i in w])

from sys import argv
f=open(argv[1], "r")
b=f.read().lstrip().rstrip().split("\n")
print(r(b))
print(v(b))
