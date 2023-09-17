from sys import argv
from functools import reduce
from operator import mul
f=open(argv[1],"r")
b=[[int(j) for j in i] for i in f.read().lstrip().rstrip().split("\n")]
lx=len(b[0])
ly=len(b)
v=0
wall = lambda x, y: x <= 0 or x == lx-1 or y <= 0 or y == ly-1
up   = lambda x, y: [i[x] for i in b[0:y]][::-1]
down = lambda x, y: [i[x] for i in b[y+1:ly]]
left = lambda x, y: b[y][0:x][::-1]
right = lambda x, y:b[y][x+1:lx]
dirc = lambda x, y: [up(x,y),down(x,y),left(x,y),right(x,y)]
s=[]
for y in range(len(b)):
	for x in range(len(b[y])):
		if wall(x,y):
			v+=1
		else:
			t=b[y][x]
			d=dirc(x,y)
			vis=[True]*4
			n=[0]*4
			for i, l in enumerate(d):
				for ll in l:
					if ll >= t:
						vis[i]=False
						n[i]+=1
						break
					else: n[i]+=1

			s.append(reduce(mul, n, 1))
			if vis.count(True) != 0: v += 1

print(v) #p1
print(max(s)) #p2
