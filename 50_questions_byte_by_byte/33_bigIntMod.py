'''
Question​ : Given a list of bytes a, each representing one byte of a larger integer (ie.
{0x12, 0x34, 0x56, 0x78} represents the integer 0x12345678), and an integer b, find a %
b.
'''

def combinerStr(arr):
	ans = ["0x"]
	for a in arr:
		t = hex(int(str(a)))
		ans.append(t[2:])
	return ''.join(ans)


def combinerNumerical(arr, n):
	p = 0x0
	for a in arr:
		p = p << 8
		p = p | a
		p %= n
	return p

def bigIntMod(arr, n):
	return combinerNumerical(arr,n)

arr1 = [0x12, 0x34, 0x56, 0x78]
arr2 = [0x03, 0xed]
n = 10
ans = bigIntMod(arr2, n)
print(ans)