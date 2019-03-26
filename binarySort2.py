def binarySort(istack,num):
	print("Function called\n")
	i = 0
	first = 0
	last = len(istack)
	
	found = False
	print("Entering Loop \n")
	print("i \t first \t mid \t Last")
	while (i<len(istack)):
		mid = (last - first) // 2
		if (mid == 1):
			mid = first+1
			
		i+=1
		print("%d \t %d \t %d \t %d \t " %(i,first,mid,last))
		
		if (istack[mid] == num):
			found = True
			print("Found at %d" %i)
			break
			
		else:
			if (istack[mid] < num):
				first = mid
			if (istack[mid] > num):
				last = mid
				
		
	return i
				
istack = [0, 1, 2, 8, 13, 17, 19, 32, 42]
num = 17
print("\nAbout to call function\n")
pos = binarySort(istack,num)
print("%d" %pos)
			
	