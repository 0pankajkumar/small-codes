import sys
sys.stdin = open("input.txt", 'r')


import math
mo = 1000000007


# ~~~~~~~~~~~~~~~
def SieveOfEratosthenes(n, prime,primesquare, a): 
    # Create a boolean array "prime[0..n]"  
    # and initialize all entries it as  
    # true. A value in prime[i] will finally  
    # be false if i is not a prime, else true. 
    for i in range(2,n+1): 
        prime[i] = True
  
    # Create a boolean array "primesquare[0..n*n+1]" 
    # and initialize all entries it as false.  
    # A value in squareprime[i] will finally be  
    # true if i is square of prime, else false. 
    for i in range((n * n + 1)+1): 
        primesquare[i] = False
  
    # 1 is not a prime number 
    prime[1] = False
  
    p = 2
    while(p * p <= n): 
        # If prime[p] is not changed,  
        # then it is a prime 
        if (prime[p] == True): 
            # Update all multiples of p 
            i = p * 2 
            while(i <= n): 
                prime[i] = False
                i += p 
        p+=1
      
  
    j = 0
    for p in range(2,n+1):  
        if (prime[p]==True):  
            # Storing primes in an array 
            a[j] = p 
  
            # Update value in primesquare[p*p], 
            # if p is prime. 
            primesquare[p * p] = True
            j+=1
  
# Function to count divisors 
def countDivisors(n): 
    # If number is 1, then it will 
    # have only 1 as a factor. So, 
    # total factors will be 1. 
    if (n == 1): 
        return 1
  
    prime = [False]*(n + 2) 
    primesquare = [False]*(n * n + 2) 
      
    # for storing primes upto n 
    a = [0]*n 
  
    # Calling SieveOfEratosthenes to  
    # store prime factors of n and to  
    # store square of prime factors of n 
    SieveOfEratosthenes(n, prime, primesquare, a) 
  
    # ans will contain total 
    # number of distinct divisors 
    ans = 1
  
    # Loop for counting factors of n 
    i=0
    while(1):  
        # a[i] is not less than cube root n 
        if(a[i] * a[i] * a[i] > n): 
            break
  
        # Calculating power of a[i] in n. 
        cnt = 1 # cnt is power of  
                # prime a[i] in n. 
        while (n % a[i] == 0): # if a[i] is a factor of n 
            n = n / a[i] 
            cnt = cnt + 1 # incrementing power 
  
        # Calculating number of divisors 
        # If n = a^p * b^q then total  
        # divisors of n are (p+1)*(q+1) 
        ans = ans * cnt 
        i+=1
  
    # if a[i] is greater than 
    # cube root of n 
      
    n=int(n) 
    # First case 
    if (prime[n]==True): 
        ans = ans * 2
  
    # Second case 
    elif (primesquare[n]==True): 
        ans = ans * 3
  
    # Third casse 
    elif (n != 1): 
        ans = ans * 4
  
    return ans # Total divisors

# ~~~~~~~~~~~~~~~~~~~~








def factors(n):
	count = 0
	# print("n is",n)
	for i in range(1,(int)(math.sqrt(n))+1):
		if n%i == 0:
			if n/i == i:
				count += 1
			else:
				count += 2

	# print("factors count",count%mo)
	return count

# gfg
def printPath(stack, arr): 
	ans = 1
	# print(stack)

	for s in stack:
		ans *= arr[s-1]

	# print("ans",ans)
	# print(ans)
	# print(factors(ans))
	print(countDivisors(ans)%mo)

# An utility function to do 
# DFS of graph recursively 
# from a given vertex x. 
def DFS(vis, x, y, stack, v, arr): 
	stack.append(x) 
	if (x == y): 

		# print the path and return on 
		# reaching the destination node 
		printPath(stack, arr) 
		return
	vis[x] = True

	# A flag variable to keep track 
	# if backtracking is taking place 
	flag = 0
	if (len(v[x]) > 0): 
		for j in v[x]: 
			
			# if the node is not visited 
			if (vis[j] == False): 
				DFS(vis, j, y, stack, v, arr) 
				flag = 1

	if (flag == 0): 

		# If backtracking is taking 
		# place then pop 
		del stack[-1] 

# A utility function to initialise 
# visited for the node and call 
# DFS function for a given vertex x. 
def DFSCall(x, y, n, stack, gr, arr): 
	
	# visited array 
	vis = [0 for i in range(n + 1)] 

	# DFS function call 
	DFS(vis, x, y, stack, gr, arr) 


















from collections import defaultdict
def makeTree(a,b,gr):
	gr[a].add(b)
	gr[b].add(a)


def inputTaker():
	for ssss in range(int(input())):
		n = int(input())
		gr = defaultdict(set)
		flag = True
		root = None
		for i in range(n-1):
			a,b = map(int, input().split())
			if flag:
				root = a
				flag = False
			makeTree(a,b,gr)

		arr = list(map(int, input().split()))
		q = int(input())

		for i in range(q):
			u,v = map(int, input().split())
			# solver1(n,gr,root,arr,u,v)

			stack = []
			DFSCall(u,v,n, stack, gr, arr)





def handle():
	inputTaker()

handle()