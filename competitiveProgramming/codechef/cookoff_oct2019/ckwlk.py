
cases = int(input())

for cas in range(cases):

	n = int(input())

	x = 0
	y = 0

	# By 10
	while(n % 10 == 0):
		# print(n)
		n /= 10
		x += 1

	# print(n)

	# By 20
	while(n % 2 == 0):
		n /= 2
		y += 1

	# print(n)

	# while(n % 200 == 0):
	# 	n/=200
	# print(n)

	# print(f"x = {x}, y = {y}")

	if n != 1 or y > x:
		print("No")
	else:
		print("Yes")