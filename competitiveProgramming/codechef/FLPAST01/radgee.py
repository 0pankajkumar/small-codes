# import sys  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w') 

from collections import deque
test = int(input())

for t in range(test):
	n, q = map(int, input().split())
	radhesh = deque(map(int, input().split()))
	geetha = deque(map(int, input().split()))
	extra = deque(map(int, input().split()))
	radheshPoints = 0
	geethaPoints = 0

	while(len(radhesh) != 0):
		one = radhesh.popleft()
		two = geetha.popleft()

		if one > two:
			radheshPoints += 1
			if len(extra) > 0:
				three = extra.popleft()
				radhesh.append(three)
				four = extra.popleft()
				geetha.append(four)
		else:
			geethaPoints += 1
			if len(extra) > 0:
				four = extra.popleft()
				geetha.append(four)
				three = extra.popleft()
				radhesh.append(three)

	if radheshPoints > geethaPoints:
		print("Radhesh wins")
	elif geethaPoints > radheshPoints:
		print("Geethakoomaree wins")
	else:
		print("Tie")


