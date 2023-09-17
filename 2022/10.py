from sys import argv
f=open(argv[1],"r")
ops=[i.split(" ") for i in f.read().lstrip().rstrip().split("\n")]
X=1
ax=0
c=0
j=20
s=0
scr=[['.' for _ in range(40)] for _ in range(6)]
def cc():
	global c,j,s
	c+=1
	if c == j:
		j+=40
		s+=X*c

	if abs(((c-1)%40)-X) <= 1:
		scr[(c//40)][((c-1)%40)] = "#"

for o in ops:
	cc()
	if o[0] == "addx":
		cc()
		X+=int(o[1])

print(s) #p1
print("\n".join(["".join([q for q in w]) for w in scr])) #p2
