import sys
sys.stdin = open('input.txt', 'r')


# your code goes here
def check(i,j,brr):
	i += 1
	if brr[i][j] == 'l':
		j += 1
		if brr[i][j] == 'l':
			return True
	return False

for _ in range(int(input())):
	# n = int(input())
	brr = list()
	for i in range(3):
		arr = input()
		# arr = list(map(int, input().split()))
		brr.append(arr)
		
	# n, p, q = map(int, input().split())
	# arr = list(map(int, input().split()))
	
	flag = False
	i = 0
	j = 0
	
	while i < 2:
		while j < 2:
			if brr[i][j] == 'l':
				if check(i,j,brr):
					flag = True
					break
			j += 1
		if flag is True:
			break
		i += 1
				
	print("yes" if flag is True else "no")
	