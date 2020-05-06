'''
Question​ : Given an input amount of change x, write a function to determine the
minimum number of coins required to make that amount of change.
'''

def minCoins(coins, i, amount, fing):
	if amount == 0:
		return fing
	if amount < 0:
		return 9999
	if i >= len(coins):
		return 0
	# if flag and amount-coins[i]>=0:

	# if amount-coins[i] >= 0:
	# 	print(amount, " - ", coins[i], " = ", amount-coins[i])
	# 	amount -= coins[i]

	x = minCoins(coins, i, amount-coins[i], fing+1)
	y = minCoins(coins, i+1, amount, fing)
	print("min (",x,",",y,")")
	return 1+min(x,y)


# The woking solution
def minCoins22(coins, amount):
	if amount == 0:
		return 0
	if amount < 0:
		return 9999
	bucket = 9999
	for i in range(len(coins)):
		bucket = min(bucket, 1+minCoins22(coins, amount-coins[i]))
	return bucket

coins = [9,6,5,1]
amount = 11
fing = 0
# print(minCoins(coins,0,amount, fing))
print(minCoins22(coins,amount))