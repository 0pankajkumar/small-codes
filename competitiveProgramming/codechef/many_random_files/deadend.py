# import sys  
# sys.stdin = open('input.txt', 'r') 

for cas in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	plantedAt = -11
	count = 0
	if n == 1:
		print(1)
	elif n == 2:
		count = 0 if arr[0]+1 == arr[1] else 1
		print(count)
	else:
		for i in range(1,len(arr)-1):
			if arr[i]-1 == plantedAt or arr[i-1] == arr[i]-1 or arr[i+1] == arr[i]+1:
				#safe
				continue
			elif arr[i] != arr[-1]:
				plantedAt = arr[i]+1
				count += 1
			
		print(count)
