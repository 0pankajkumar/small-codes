def coins(arr, coin, left, pk):
	print(arr, coin, left)
	# Base cases
	if left == 0:
		return 1
	elif left < 0:
		return 0
	
	if coin <= 0:
		return 0

	if pk[left] != None:
		return pk[left]
	
	# Choose + Not Choose	
	holder = coins(arr[:coin], coin, left-arr[-1], pk) + coins(arr[:coin-1], coin-1, left, pk)
	pk[left] = holder
	return holder

left = 10
pk = [None] * (left+1)
arr = [2,5,3,6]
coin = len(arr)
print(coins(arr, coin, left, pk))
print(pk)