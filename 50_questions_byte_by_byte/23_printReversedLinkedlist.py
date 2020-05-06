# Question​ : Given a linked list, write a function that prints the nodes of the 
#list in reverse order.

from collections import deque

def printReverse(i, li):
	if i >= len(li):
		return
	printReverse(i+1, li)
	print(li[i])

# making the queue
li = deque()
for i in range(1,4):
	li.append(i)

# Triggering the recursive print
printReverse(0, li)