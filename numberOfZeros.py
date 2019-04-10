# cook your dish here


box = []

t = int(input())

while(t > 0):
    n = int(input())
 
    count = 0 
    while(n>0):
    	count += (n//5)
    	n = n / 5

    count = int(count)
    box.append(count)
    t -= 1
    
for i in box:
    print(i)


