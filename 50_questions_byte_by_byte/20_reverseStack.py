# Question​ : Given a stack, reverse the items without creating any additional data structures.


def revStack(arr):
	i = 0
	j = len(arr)-1
	while(i<=j):
		t = arr[i]
		arr[i] = arr[j]
		arr[j] = t
		i+=1
		j-=1

arr = [1,2,3,4,5]
revStack(arr)
print(arr)
# the above was made assuming we had a list


# Now using an actual stack
def revActualStack(stack):
	if stack.qsize() == 0:
		return False
	t = stack.get_nowait()
	revActualStack(stack)
	stack.put_nowait(t)

from queue import LifoQueue
stack = LifoQueue()
for i in range(5):
	stack.put_nowait(i)

revActualStack(stack)

for i in range(5):
	print(stack.get_nowait(),end="->")