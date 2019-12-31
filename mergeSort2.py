# With help from https://en.wikipedia.org/wiki/Merge_sort
def merge(left, right):
	l = list()
	while(len(left) > 0 and len(right) > 0):
		if left[0] <= right[0]:
			l.append(left[0])
			left = left[1:]
		else:
			l.append(right[0])
			right = right[1:]
	while len(left) > 0:
		l.append(left[0])
		left = left[1:]
	while len(right) > 0 :
		l.append(right[0])
		right = right[1:]
	return l

def merge_sort(p):
	if len(p) <= 1:
		return p
	else:
		left = list()
		right = list()
		mid = len(p) // 2
		for i in range(len(p)):
			if i < mid:
				left.append(p[i])
			else:
				right.append(p[i])
		left = merge_sort(left)
		right = merge_sort(right)

		return merge(left, right)

p = [6,5,4,3,2,1]
q = merge_sort(p)
print(q)