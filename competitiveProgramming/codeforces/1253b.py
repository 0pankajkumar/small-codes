# import sys  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')

# for t in range(int(input())):

n = int(input())
arr = list(map(int, input().split()))
days = 0
cCountList = []
cList = []

summ = 0
reg = set()

for i in range(n):
	# If value not in set 
		# Check whether -value in the set
		# If yes 
			# remove that value
			# cList.append(arr[i])
		# add it
		# Make sum += arr[i]
		# cList.append(arr[i])
	# else the day has ended
		# If summ != 0
			# invalid entry
		# else
			# cCountList.append(len(cList))
		# cList = []