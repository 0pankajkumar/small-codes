'''
Find median of two sorted arrays
arr1 = [​ 1 ​ , ​ 3 ​ , ​ 5 ​ ]
arr2 = [​ 2 ​ , ​ 4 ​ , ​ 6 ​ ]
median(arr1, arr2) = ​ 3.5
Solution​ : ​https://www.byte-by-byte.com/median/
'''
import math

# Divides a,b without implicit conversion to float
def intDivide(a,b):
	return int(a/b)

# Returns first half of array
def partFirstHalf(arr):
	n = len(arr)
	if n%2==0:
		return arr[:math.ceil(n/2)+1]
	else:
		return arr[:math.ceil(n/2)]

# Returns second half of array
def partSecondHalf(arr):
	n = len(arr)
	if n%2==0:
		return arr[intDivide(n,2)-1:]
	else:
		return arr[math.floor(n/2):]

# Calculates median
def getMedian(arr):
	n = len(arr)
	if n % 2 == 0:
		a = arr[intDivide(n,2)-1]
		b = arr[intDivide(n,2)]
		return (a+b)/2
	else:
		return arr[n//2]

def median(arr1,arr2):
	if len(arr1) == 2:
		return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
	
	m1 = getMedian(arr1)
	m2 = getMedian(arr2)

	if m1 > m2:
		return median(partFirstHalf(arr1), partSecondHalf(arr2))
	elif m2 > m1:
		return median(partSecondHalf(arr1), partFirstHalf(arr2))
	else:
		return m1

if __name__ == "__main__":
	arr1 = [1,3,5]
	arr2 = [2,4,6]
	print(median(arr1,arr2))
