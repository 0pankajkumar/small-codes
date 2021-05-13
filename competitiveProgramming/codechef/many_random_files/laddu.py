import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')

def getBonus(rank):
	if rank > 20:
		return 0
	else:
		return 20-rank

for t in range(int(input())):
	events, indi = input().split()
	indi = 200 if indi == "INDIAN" else 400
	ladd=0
	for ss in range(int(events)):
		eve = list(input().split())

		if eve[0] == "CONTEST_WON":
			ladd += (300 + getBonus(int(eve[1])))
		elif eve[0] == "TOP_CONTRIBUTOR":
			ladd += 300
		elif eve[0] == "BUG_FOUND":
			ladd += int(eve[1])
		elif eve[0] == "CONTEST_HOSTED":
			ladd += 50

	print(ladd//indi)
