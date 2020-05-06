'''
Question​ : Given an n x m array where all rows and columns are in sorted order, write a
function to determine whether the array contains an element x
'''

def binSearch(start, end, arr, x):
	if start==end:
		return True if arr[start]==x else False
	mid = (start+end)//2
	if arr[mid] < x:
		return binSearch(mid+1, end, arr, x)
	elif arr[mid] > x:
		return binSearch(start,mid-1, arr, x)
	else:
		return True

def findRow(Arr, x, start, end):
	if start == end:
		return start
		if binSearch(0, len(Arr[start]), Arr[start],x):
			return True
		else:
			return False
	mid=(start+end)//2
	if Arr[mid][0] > x:
		return findRow(Arr, x, start, mid-1)
	elif Arr[mid][0] <= x:
		if Arr[mid][-1] >= x:
			return mid
		else:
			return findRow(Arr,x, mid+1, end)
	else:
		return mid

Arr=[
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15],
	[16, 17, 18]
]

# print(binSearch(0,3,Arr[0],4))
print(findRow(Arr, 16, 0, 4))