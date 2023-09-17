from sys import argv
from math import copysign
f=open(argv[1],"r")
ops=[[i.split(" ")[0],int(i.split(" ")[1])] for i in f.read().lstrip().rstrip().split("\n")]
moves={
  "U": [0, 1],
  "D": [0, -1],
  "L": [-1, 0],
  "R": [1, 0]
}

sign = lambda x: int(copysign(1, x))

def sim(N):
	global ops
	visited=[]
	knots=[[0,0] for _ in range(N)]
	for dr,n in ops:
		for _ in range(n):
			for k in range(len(knots)):
				if k == 0:
					knots[k][0] += moves[dr][0]
					knots[k][1] += moves[dr][1]
				else:
					dx,dy = [knots[k-1][0]-knots[k][0],knots[k-1][1]-knots[k][1]]
	
					if abs(dx) > 1 and abs(dy) > 1:
						knots[k][0] += sign(dx)
						knots[k][1] += sign(dy)
						continue
	
					if abs(dx) > 1: 
						knots[k][0] += sign(dx)
						knots[k][1] += sign(dy) if knots[k][1] != knots[k-1][1] else 0
	
					if abs(dy) > 1: 
						knots[k][1] += sign(dy)
						knots[k][0] += sign(dx) if knots[k][0] != knots[k-1][0] else 0

					visited.append(tuple(knots[N-1]))
	return visited

print(len(list(set(sim(2))))) #p1
print(len(list(set(sim(10))))) #p2
