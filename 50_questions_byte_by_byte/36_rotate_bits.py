# Question​ : Given a number, write a function to rotate the bits (ie circular shift).

def rotate(num, n):
	# return num
	truncated_digits = num % (1<<n)
	in_the_middle = num >> n

	# return bin(truncated_digits),bin(in_the_middle)
	countBits = 0
	t = in_the_middle
	while t:
		countBits += 1
		t >>= 1

	prefix_of_ans = truncated_digits << countBits
	# return bin(truncated_digits),bin(in_the_middle), bin(prefix_of_ans)
	ans = prefix_of_ans | in_the_middle
	return ans
ans = rotate(0xffff0000, 8)
# print(ans)
print(hex(ans))