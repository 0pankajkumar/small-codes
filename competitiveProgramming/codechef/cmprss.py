import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')  

def sendForPacking(l, ans):
	if len(l) <= 2:
		# Comma
		for q in l:
			ans.append(str(q))
			ans.append(',')
	else:
		# Dot 
		ans.append(str(l[0]))
		ans.append("...")
		ans.append(str(l[-1]))
		ans.append(',')
	# ans.append(',')

for cas in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n == 1:
    	print(arr[0])
    else:
	    prev = arr[0]
	    ans = list()
	    arr = arr[1:]
	    l = [prev]
	    for i in range(len(arr)):
	    	if prev+1 == arr[i]:
	    		l.append(arr[i])
	    		prev = arr[i]
	    		if arr[i] == arr[-1]:
	    			sendForPacking(l, ans)
	    	elif len(l) >= 2:
	    		sendForPacking(l, ans)
	    		l = list()
	    		l.append(arr[i])
	    		prev = arr[i]
	    		if arr[i] == arr[-1]:
	    			sendForPacking(l, ans)
	    	else:
	    		if i+1 < len(arr):
	    			if arr[i+1] != arr[i]+1:
			    		l.append(arr[i])
			    		prev = arr[i]
			    		sendForPacking(l, ans)
			    		l = list()
			    	else:
			    		l.append(arr[i])
			    		prev = arr[i]
		    	else:
		    		l.append(arr[i])
		    		prev = arr[i]
		    		sendForPacking(l, ans)
		    		l = list()

	    # if len(l) != 0:
	    # 	sendForPacking(l, ans)
	    ans = ans[:-1]
	    print(''.join(ans))