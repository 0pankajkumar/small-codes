'''
Question: Given a list of items with values and weights, as well as a max weight, find the
maximum value you can generate from items where the sum of the weights is less than
the max.
eg.
items​ = {(​ w:1​ , ​ v:6​ ), (​ w:2​ , ​ v:10​ ), (​ w:3​ , ​ v:12​ )}
maxWeight = ​ 5
knapsack(​ items​ , maxWeight) = ​ 22
Solution​ : ​https://www.byte-by-byte.com/01knapsack/
'''


def knap(n,W,val,wt):
	if W <= 0 or n <= 0:
		return 0
	if wt[n] > W:
		return 0

	return max(val[n] + knap(n-1, W-wt[n-1],val,wt), knap(n-1,W,val,wt))



if __name__ == "__main__":
	# val = [60, 100, 120]
	# wt = [10, 20, 30]
	val = [6,10,12]
	wt = [1,2,3]
	W = 50
	n = len(val)
	print(knap(n-1,W,val,wt))