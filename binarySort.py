n = int(input("Please enter your guess number"))
i=0
max=30
min=0
x=0
print("\n %d \n" %n)
for x in range(0, int(n/2)):
	i=i+1
	mid=(max-min)//2
	if(n<mid):
		max=mid
	elif(n>mid):
		min=mid
	elif(mid==n):
		print("Your guess found at %d" %(i))