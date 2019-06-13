# cook your dish here
cases, le = map(int, input().split())
print(cases)
def Prime(n):
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return True

a = input().split()

for cas in range(cases):
	#q,n = map(int, input().split())
	
	one, two, three = map(int, input().split())

	if one == '1':
		#Prime wala
		start = int(two)
		end = int(three)

		count = 0 

		for i in range(start, end+1):
			if Prime(a[i]):
				count += 1
		print(count)



	if one == '2':
		#Replace wala
		a[int(two)] = int(three)
