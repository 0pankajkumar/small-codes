import sys
sys.stdin = open('input.txt', 'r')

for testcases in range(int(input())):
	n,k,l = map(int, input().split())
	limitArray = [l]*k

	schedule = list()
	bowlerNumber = 0
	prevBowler = -1
	neverPossible = False

	for i in range(n):
		if prevBowler == i:
			neverPossible = True
			print("Never ever")
			break
		prevBowler = i

		# print(bowlerNumber, limitArray)

		if limitArray[bowlerNumber] > 0:
			schedule.append(i)
			limitArray[bowlerNumber] -= 1


		bowlerNumber += 1
		if bowlerNumber > k-1:
			bowlerNumber = 0

	if neverPossible:
		print(-1)
		continue

	print(schedule)