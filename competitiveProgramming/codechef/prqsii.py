# cook your dish here
cases, le = map(int, input().split())
#print(cases)
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

b = input().split()
a = [0.5]
for sd in b:
    a.append(sd)

for cas in range(cases):
	#q,n = map(int, input().split())
	
	one, two, three = input().split()

	#print(type(one))
	if one == '1':
		#Prime wala
		start = int(two)
		#start -= 1
		end = int(three)

		count = 0
		#print(start)
		#print(end)

		for i in range(start, end+1,1):
			if Prime(int(a[i])) is True:
				count += 1
			#print(i)
				
		#print()

		print(count)



    
	if one == '2':
		#Replace wala
		a[int(two)] = (three)
		
	#print(a)
