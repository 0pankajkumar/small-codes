import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')

def cal(n): 
      
    count0, count1 = 0, 0
    while (n != 0): 
      
        # calculating count of zeros and ones 
        if(n % 2 == 0):  
            count0 += 1
        else: 
            count1 += 1
        n //= 2
    return "even" if count1 % 2 == 0 else "odd"

def sol():
	for _ in range(int(input())):
		n, q = map(int, input().split())
		a = list(map(int, input().split()))
		
		for qq in range(q):
			p = int(input())
			
			evenCount = 0
			oddCount = 0
			mo = a.copy()
			for i in range(len(a)):
				mo[i] = mo[i] ^ p
				r = cal(mo[i])
				
				if r == "even":
					evenCount += 1
				else:
					oddCount += 1
			
			print(evenCount, oddCount)
		
sol()
		