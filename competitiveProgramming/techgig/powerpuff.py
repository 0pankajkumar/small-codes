import sys
sys.stdin = open("input.txt", 'r')

n = int(input())
required = list(map(int,input().split()))
available = list(map(int,input().split()))
ansList = list()
ans = 0

for i in range(n):
	t = available[i] // required[i]
	ansList.append(t)

print(min(ansList))
