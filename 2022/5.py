import re
from sys import argv
f=open(argv[1],"r")
b=f.read().lstrip().rstrip()
p=b.split("\n\n")
ops=[[int(j) for j in i.split(" ")[1::2]] for i in p[1].split("\n")]
k=[i.replace("    ", " ").split(" ") for i in p[0].split("\n")]
k[-1]=list(filter("".__ne__, k[-1]))
w=[[*filter("".__ne__, [k[j][i].replace("[","").replace("]","") for j in range(len(k[-1])-1)])][::-1] for i in range(len(k[-1]))]

def p1():
	for i in ops:
		q=i[0]
		s=i[1]-1
		d=i[2]-1
		w[d] += w[s][-q:][::-1]
		w[s] = w[s][:-q]

def p2():
	for i in ops:
		q=i[0]
		s=i[1]-1
		d=i[2]-1
		w[d] += w[s][-q:]
		w[s] = w[s][:-q]

#p1()
p2()
print("".join([i[-1] for i in w if len(i) != 0]))
