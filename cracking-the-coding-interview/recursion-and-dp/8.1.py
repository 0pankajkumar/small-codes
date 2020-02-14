# triple step

# brute force
rec_depth = 0
def stairs(remaining):
	rec_depth += 1
	if remaining <= 1:
		return 1
	if remaining < 3:
		return 2
	else:
		return stairs(remaining - 1) + stairs(remaining - 2) + stairs(remaining - 3)

ans = stairs(10)
print("ans=",ans,"--- recursion depth=", rec_depth)








# optimzed

memo = dict()
def stairs(remaining):
	if remaining in memo:
		return memo[remaining]
	if remaining <= 1:
		memo[remaining] = 1
		return 1
	if remaining < 3:
		memo[remaining] = 2
		return 2
	else:
		qu = stairs(remaining - 1) + stairs(remaining - 2) + stairs(remaining - 3)
		memo[remaining] = qu
		return qu

ans = stairs(10)
print(ans)
