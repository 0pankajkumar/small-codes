import math
s = '1100'

i = 0
totSum = 0
while(len(s) != 0):
	temp = s[-1]

	p = math.pow(2,i) * int(temp)

	totSum += p 

	i += 1

	s = s[:-1]

print(totSum)

