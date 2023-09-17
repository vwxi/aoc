z = lambda k: max([sum([int(j) for j in i.split("\n")]) for i in k.lstrip().rstrip().split("\n\n")])
w = lambda k: sorted([sum([int(j) for j in i.split("\n")]) for i in k.lstrip().rstrip().split("\n\n")])[::-1]

from sys import argv
f=open(argv[1],"r")
b=f.read()
print(z(b))
m=w(b)
print(m[0]+m[1]+m[2])
