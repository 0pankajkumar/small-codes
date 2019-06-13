def Prime(n):
	if n == 2:
		return True
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return True

print(Prime(3))