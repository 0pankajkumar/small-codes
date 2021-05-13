testCases = int(input())

for t in range(testCases):
	no_of_nos = int(input())
	nos = list(map(int,input().split()))
	
	sum = 0
	could_steal_coin_position = None
	for i in range(no_of_nos):
		sum += nos[i]

	mean = sum / no_of_nos

	for i in range(no_of_nos):
		if ((sum - nos[i]) / (no_of_nos -1)) == mean:
			could_steal_coin_position = i
			break

	if could_steal_coin_position is not None:
		print(could_steal_coin_position + 1)
	else:
		print("Impossible")



