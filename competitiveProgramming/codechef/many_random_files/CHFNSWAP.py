import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

# def getTarget(A, B):
# 	a = sum(A)
# 	b = sum(B)
# 	if (a-b) % 2 != 0:
# 		return 0
# 	return (a-b) / 2

# def findCounts(A, B):
# 	print(A,B)
# 	return 0
# 	target = getTarget(A, B)
# 	count = 0
# 	i,j = 0,0

# 	while i < len(A) and j < len(B):
# 		diff = A[i] - B[j]
# 		if diff == target:
# 			count += 1
# 		elif diff < target:
# 			i += 1
# 		else:
# 			j += 1

# 	return count

def getTarget(A,B): 
	# Calculations of sumd from both lists 
	sum1=sum(A) 
	sum2=sum(B) 

	# Because that target must be an integer 
	if( (sum1-sum2)%2!=0): 
		return 0
	return (sum1-sum2)/2

# Prints elements to be swapped 
def findSwapValues(A,B): 
	# Call for sorting the lists 
	# A.sort() 
	# B.sort() 
	count = 0

	if sum(A) == sum(B):
		count += 1

	#Note that target can be negative 
	target=getTarget(A,B) 

	# target 0 means, answer is not possible 
	if(target==0): 
		return count
	i,j=0,0
	

	while(i<len(A) and j<len(B)): 
		diff=A[i]-B[j] 
		if diff == target: 
			count += 1
			# print(target, A[i], B[j])
			i+=1
		# Look for a greater value in list A 
		elif diff <target: 
			i+=1
		# Look for a greater value in list B 
		else: 
			j+=1

	return count


for t in range(int(input())):
	n = int(input())

	arr = [i for i in range(1, n+1)]
	count = 0
	
	for i in range(0,n-1):
		# print(arr[:i+1], arr[i+1:])
		count += findSwapValues(arr[:i+1], arr[i+1:])

	print(count)
	# print()




	# 1 2 3

	# 3 2 1

	# 2 1 3