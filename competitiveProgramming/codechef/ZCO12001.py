import sys  
sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')  

'''
Author : pankaj2kumar@codechef
'''


def problemSolver1(n,arr):
	maxDepth=0
	posMaxDepth=0
	lenOfMaxSeq=0
	maxLenOfMaxSeq=0
	balance=0
	temp=0
	startIndex=0
	reqIndex=0
	indexFoundMaxSymbols=False

	for i in range(n):
		if arr[i] == 1:
			if balance == 0:
				startIndex = i

			# if balance%2!=0:
			# 	if balance > maxDepth:
			# 		# print("balance is", balance)
			# 		maxDepth = balance 
			# 		posMaxDepth = i
			if balance > maxDepth:
				# print("balance is", balance)
				maxDepth = balance 
				posMaxDepth = i
			
			balance += 1
			lenOfMaxSeq += balance
			# print(balance,end="-")

			
		else:
			balance -= 1
			# print(balance,end="-")
		if balance == 0:
			if temp > maxLenOfMaxSeq:
				maxLenOfMaxSeq = temp
				reqIndex = startIndex
			temp=0
		else:
			temp+=1
			# print()


	print(maxDepth+1, posMaxDepth+1, maxLenOfMaxSeq+1, reqIndex+1)
	

def inputHandler1():
	n = int(input())
	arr = list(map(int, input().split()))
	problemSolver1(n, arr)


inputHandler1()