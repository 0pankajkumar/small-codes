def consecutive(arr):
	s = set()
	ans = 0
	ansArray=[]

	for a in arr:
		s.add(a)

	for i in range(len(arr)):
		j = arr[i]
		tarr=[]

		while j in s:
			tarr.append(j)
			j+=1

		if j-arr[i] >= ans:
			ansArray.append(tarr)
			ans = j-arr[i]
		# ans=max(ans, j-arr[i])

	return ans,ansArray


arr = [4,2,1,6,5]
arr2 = [5,5,3,1]
print(consecutive(arr2))