# Python 2 

arr = []

with open("input1.txt", 'r') as f:
	for num in f:
		arr.append(float(num))

print arr