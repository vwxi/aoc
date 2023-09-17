from sys import argv
from functools import reduce
from operator import mul
class monkey:
	def __init__(self, a):
		self.id, self.items, self.op, self.div, self.true, self.false = a
		self.ins = 0

f=open(argv[1],"r")
b=[*filter(''.__ne__, f.read().lstrip().rstrip().split("\n"))]
parse = [
	lambda s: int(s.split("Monkey ")[1][:-1]),
	lambda s: [int(i) for i in s.split("Starting items: ")[1].split(", ")],
	lambda s: s.split("Operation: new = ")[1].split(" ")[1:],
	lambda s: int(s.split("Test: divisible by ")[1]),
	lambda s: int(s.split("If true: throw to monkey ")[1]),
	lambda s: int(s.split("If false: throw to monkey ")[1]),
]

def mr(n,p):
	monkeys=[b[n:n+6] for n in range(0, len(b), 6)]
	monkeys=[monkey([parse[i](l) for i, l in enumerate(m)]) for m in monkeys]
	mod = reduce(mul, [m.div for m in monkeys])
	for _ in range(n):
		for i in range(len(monkeys)):
			tt = [] # to toss
			for j in range(len(monkeys[i].items)):
				a=0
				if monkeys[i].op[1] == "old": a = monkeys[i].items[j]
				else: a=int(monkeys[i].op[1])
				if monkeys[i].op[0] == "+": monkeys[i].items[j] += a
				if monkeys[i].op[0] == "*": monkeys[i].items[j] *= a
				if p == 1: monkeys[i].items[j] //= 3
				else: monkeys[i].items[j] %= mod
				th = monkeys[i].true if monkeys[i].items[j] % monkeys[i].div == 0 else monkeys[i].false
				t = monkeys[i].items[j]
				tt += [j]
				monkeys[th].items += [t]
				monkeys[i].ins += 1
			monkeys[i].items = [monkeys[i].items[it] for it in tt if it not in tt]

	l=sorted([m.ins for m in monkeys])[::-1]
	return l[0]*l[1]

print(mr(20,1)) #p1
print(mr(10000,2)) #p2
