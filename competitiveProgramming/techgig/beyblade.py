import sys
sys.stdin = open("input.txt", 'r')

for ssss in range(int(input())):
	n = int(input())
	gTeam = list(map(int,input().split()))
	opponent = list(map(int,input().split()))

	gTeam.sort(reverse=True)
	opponent.sort(reverse=True)

	opponentVisitedIndexes = set()
	p1 = 0
	p2 = n
	ans = 0
	bigBreak = False
 
	for i in range(n):
		for j in range(p1,p2):
			# print("p1 p1 j ", p1,p2, j)
			if opponent[j] < gTeam[i]:
				if j-1 >= 0:
					k = j-1
					while opponent[k] in opponentVisitedIndexes:
						# print("whiling")
						k -= 1
						# print("whiled")
					opponentVisitedIndexes.add(k)
					# print(opponent[k], end=" ")
					ans += 1
					p1 = j+1
				else:
					opponentVisitedIndexes.add(0)
					ans += 1
					p1 = 1
				break
			if j+1 == p2:
				biBreak = True
		if bigBreak:
			break



		
		
	print(ans)
	# print(opponentVisitedIndexes)
		
