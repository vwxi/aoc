def p(s,l):
	k=""
	for i in range(len(s)):
		k+=s[i]
		if len(k) == l:
			if len(set(k)) == len(k): return i+1
			k=k[1:]

from sys import argv
f=open(argv[1],"r")
b=f.read().lstrip().rstrip()
print(p(b,4)) #p1
print(p(b,14)) #p2
