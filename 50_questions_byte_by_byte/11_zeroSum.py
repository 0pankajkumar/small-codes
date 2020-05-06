# Question​ : Given an array, write a function to find any subarray that sums to zero, if one exists

def zeroSum(arr):
	s=dict(); su=arr[0]
	s[arr[0]]=0
	for i in range(1,len(arr)):
		su+=arr[i]
		if su not in s:
			s[su]=i
		else:
			return arr[s[su]+1:i+1]

arr = [1,2,-5,1,2,-1]
arr2 = [33,44,55,-99,2,1,-9]
print(zeroSum(arr2))
