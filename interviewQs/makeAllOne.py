# import sys  
# sys.stdin = open('input.txt', 'r') 

# arr = list(map(int, input().split()))

arr = [1, 0, 1, 0, 1]
count = 0

for i in range(len(arr)):
	if (arr[i] == 0 and count % 2 == 0) or (arr[i] == 1 and count % 2 != 0):
		count += 1

print(count)


'''
Expected
10101
11010
11101
11110
11111

Dry Run
count = 4
10101
11010
11101
11110
11111

'''
