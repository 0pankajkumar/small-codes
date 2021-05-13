import sys  
sys.stdin = open('input.txt', 'r') 


for testcases in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))

	freq = dict()
	for a in arr:
		if a in freq:
			freq[a] += 1
		else:
			freq[a] = 1

	revFreq = dict()
	for key, value in freq.items():
		if value in revFreq:
			revFreq[value] += 1
		else:
			revFreq[value] = 1

	largest = -1
	for key, value in revFreq.items():
		if value > largest:
			largest = value

	smallest = 10e9
	for key, value in revFreq.items():
		if value == largest:
			if key < smallest:
				smallest = key

	print(smallest)

