import math

test = int(input())
# ertyu
for t in range(test):
	s = input()

	partition = len(s) / 2
	if partition % 2 == 0:
		partition1 += 1
	else:
		partition1 = math.floor(partition)
		partition2 = partition + 1


	print(s[:partition1], s[partition2:])