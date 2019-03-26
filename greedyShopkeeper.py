#Taking input 
a = raw_input("Enter Total: ")
total = int(a)

'''
1$
5$
10$
25$
'''
count = 0

while total >= 25:
	total -= 25
	count += 1

while total >= 10:
	total -= 10
	count += 1
	
while total >= 5:
	total -= 5
	count += 1

while total >= 1:
	total -= 1
	count += 1
	
print "Total coins are: %i" %count
