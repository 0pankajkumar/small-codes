

def hanoi(n, beg, aux, end):
	print(beg, aux, end)
	# Base case
	if n > 0:
		hanoi(n-1, beg, end, aux)
		if beg:
			end.append(beg.pop())
		hanoi(n-1, aux, beg, end)





n = 3
beg = [3,2,1]
end = []
aux = []
hanoi(n, beg, aux, end)
print(beg)

print(aux)

print(end)