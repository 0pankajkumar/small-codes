# import sys  
# sys.stdin = open('input.txt', 'r') 
# sys.stdout = open('output.txt', 'w')
def fi(a):
	a = list(a)
	a.sort()
	a = ''.join(a)
a = input()
b = input()

if a == b:
	print("YES")
elif ((len(a) % 2 == 0)):
	# tram
	t1 = int(len(a) / 2)
	t2 = int(len(b) / 2)
	# print(t1, t2)

	a1 = a[:t1]
	fi(a1)

	a2 = a[t1 :]
	fi(a2)

	b1 = b[:t2]
	fi(b1)

	b2 = b[t2:]
	fi(b2)
	# print(a1, a2, b1, b2)
	
	if a1 == b1 or a2 == b2:
		print("YES")
	elif a1 == b2 or a2 == b1:
		print("YES")
	else:
		print("NO")
else:
	print("NO")


# raily
# Odd will not pass
