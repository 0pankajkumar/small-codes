import sys
sys.stdin = open("input.txt", 'r')

for ssss in range(int(input())):
	k,d0,d1 = map(int, input().split())
	# suma = d0 + d1
	# for i in range(k-2):
	# 	temp = suma % 10
	# 	suma += temp

	# print("Yes" if suma % 3 == 0 else "No")
	print("Yes" if ((d0+d1)*(k-2)) % 3 == 0 else "No")


