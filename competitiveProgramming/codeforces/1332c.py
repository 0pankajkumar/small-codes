import sys
sys.stdin = open("input.txt", 'r')

for ssss in range(int(input())):
	n,k = map(int, input().split())
	s = input()

	f1 = period(s,n,k)

	if f1 >= 0: 
		f2 = pallindrome(s,n,k)

	if f2:
		print(f1)
	else:
		