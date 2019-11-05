# cook your dish here
def checkSeq(x, arr):
	pos1 = 0
	pos1notFound = True
	pos2 = 0
	for i in range(len(arr) - 1, -1, -1):
		if arr[i] == x:
			if pos1notFound is True:
				pos1 = i
				pos1notFound = False
			else:
				pos2 = i
				# print("diff", pos1 - pos2)
				return (pos1 - pos2)

	return False

cases = int(input())

for cas in range(cases):
	#Code here
	
	n = int(input())
	
	arr = [0]
	
	for i in range(n):
		x = arr[-1]
		
		# Returns false if not found otherwise length
		present = checkSeq(x, arr)
		
		if present == False:
			arr.append(0)
		else:
			arr.append(present)
	
	# print(arr)
	arr = arr[:n]
	c = arr.count(arr[-1])
	print(c)
		
			
			
			
			
			
		