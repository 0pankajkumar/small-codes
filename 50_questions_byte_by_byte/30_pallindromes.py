'''
Question​ : Given a linked list, write a function to determine whether the list is a
palindrome.
'''

class Node():
	def __init__(self, value, nextt):
		self.value = value
		self.nextt = nextt


def pallindrome(p1, p2):
	if p1 is None:
		return True

	t = pallindrome(p1.nextt, p2)
	ans = False
	if (p1.value == p2[0].value):
		ans =  True & t
	else:
		ans = False & t
	p2[0] = p2[0].nextt
	return ans


four = Node(1,None)
three = Node(2,four)
two = Node(2,three)
one = Node(1,two)

p1=one
p2 =[one]
ans = pallindrome(p1,p2)
print(ans)


