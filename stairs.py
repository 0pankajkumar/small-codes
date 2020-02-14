
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