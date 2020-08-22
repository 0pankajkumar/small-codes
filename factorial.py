def fact(num):
	if num <= 1:
		return 1
	else:
		nu = num -1
		return num*fact(nu)


num = int(input())
f = fact(num)
print(f"Factorial is {f}")

