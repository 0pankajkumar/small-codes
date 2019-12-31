import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')

import datetime
for _ in range(int(input())):
	h, m= map(int, input().split())

	a = datetime.datetime.strptime(f"28 12 2019 {h} {m}", "%d %m %Y %H %M")
	b = datetime.datetime(2020,1,1,0,0)
	c = b-a
	# minutes = c.total_seconds / 60
	print(int(c.seconds/60))
