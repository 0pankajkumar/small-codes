import sys  
sys.stdin = open('input.txt', 'r') 

# def solve(a, b):
# 	ans = 0
# 	divider = 10

# 	while divider > 0:
# 		if a / divider >= 1:
# 			ans += (a // divider)
# 			a %= divider

# 		divider -= 1

# 	return ans


# def solve2(gap):

# 	while divider > 0:
# 		if a / divider >= 1:
# 			ans += (a // divider)
# 			a %= divider

# 		divider -= 1

# 	return ans
	

def solve3(gap):
	ans = 0

	for divider in range(10,0,-1):
		ans += (gap // divider)
		gap %= divider


	return ans





for testcases in range(int(input())):
	a, b = map(int, input().split())
	print(solve3(abs(a-b)))