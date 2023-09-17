from sys import argv
from intervaltree import *
f=open(argv[1],"r")
b=f.read().lstrip().rstrip().split("\n")
sensors=[]
beacons=[]

for i in b:
	k=i.split(":")
	s=[j.split(", ") for j in k[0].strip("Sensor at ").split(",")]
	s=[int(s[0][0].split("x=")[1]), int(s[1][0].split("y=")[1])]
	b=[j.split(", ") for j in k[1].strip(" closest beacon is at ").split(",")]
	b=[int(b[0][0].split("x=")[1]), int(b[1][0].split("y=")[1])]
	sensors += [s]
	beacons += [b]

def man(a,b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def itv(a,b,c):
	return (a[0] - man(a,b) + abs(c - a[1]), a[0] + man(a,b) - abs(c - a[1]) + 1)

def p1(y):
	tree = IntervalTree()

	for s,b in zip(sensors, beacons):
		it=itv(s,b,y)
		if it[0] < it[1]:
			print(s,b,man(s,b),it)	
			tree[it[0]:it[1]] = it # add an interval

	for b in beacons:
		if b[1] == y:
			tree.chop(b[0],b[0]+1) # remove beacons from intervals

	k=0
	for i in range(min(tree).begin, max(tree).end):
		if tree[i]: k+=1

	return k

def p2(mn,mx):
	global beacons
	bb=[*filter(lambda i: i[0] in range(mn,mx+1) and i[1] in range(mn,mx+1), beacons)]
	bb=[i[0]*int(4e6)+i[1] for i in bb]
	print(bb)

#print(p1(int(2e6)))
print(p2(0,20))
