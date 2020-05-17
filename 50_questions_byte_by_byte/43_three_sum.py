'''
Question​ : Given a list of integers, write a function that returns all sets of 3 numbers in
the list, a, b, and c, so that a + b + c == 0
'''

def isUnique(a,b,c, tbank):
	if len(tbank) == 0:
		tbank = set()

def threeSum(arr):
	n = len(arr)
	ans = list()
	tbank=list()
	arr.sort()

	for i in range(0,n):
		if i==0 or arr[i] > arr[i-1]:
			start = i+1
			end = n-1
			while start < end:
				if arr[i] + arr[start] + arr[end] == 0:
					t = list()
					t.append(arr[i])
					t.append(arr[start])
					t.append(arr[end])
					ans.append(t)
					# start+=1

				if arr[i] + arr[start] + arr[end] < 0:
					currStart = start
					# start+=1
					while arr[currStart] == arr[start] and start<end:
						start+=1

				else:
					currEnd = end
					# end-=1
					while arr[currEnd] == arr[end] and start<end:
						end-=1
				# print(start,end)

	return ans



arr = [-1, 0, 1, 2, -1, -4]
ans = threeSum(arr)
print(ans)