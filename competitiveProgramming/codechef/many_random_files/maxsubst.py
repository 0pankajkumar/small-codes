
cases = int(input())

class element:
	def __init__(self, val):
		self.prev = None
		self.next = None
		self.val = val






for cas in range(cases):
	leng = int(input())
	ar = input().split()

	arr = [int(a) for a in ar]

	

	for i in range(leng):
		start = i
		if arr[i+1] == arr[i]:
			end = i+1
		elif arr[i+1] + 1 == arr[i]:
			arr[i+1] += 1
			end = i+1
		elif arr[i] + 1 == arr[i+1]:
			arr[i] += 1
			start = i
	print(f"i={i} , j={j}")
