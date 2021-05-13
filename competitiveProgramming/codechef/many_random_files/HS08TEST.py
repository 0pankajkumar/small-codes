# your code goes here

need, balance = map(int, input().split())

if need > balance:
	print(balance)
elif need % 5 != 0:
	print(balance)
else:
	balance -= need
	balance -= 0.5
	print(balance)