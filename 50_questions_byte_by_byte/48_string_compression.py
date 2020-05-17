'''
Question​ : Given a string, write a function to compress it by shortening every sequence
of the same character to that character followed by the number of repetitions. If the
compressed string is longer than the original, you should return the original string.
'''

def compressor(stree):
	if stree is None or len(stree) == 0:
		return
	a = stree[0]
	cou = 0
	ans = [a]
	for s in stree:
		if s==a:
			cou += 1
		else:
			ans.append(str(cou))
			ans.append(s)
			a=s
			cou = 1
	ans.append(str(cou))

	# returning the compressed string only if it's shorter than original string
	ans = ''.join(ans)
	return ans if len(ans) < len(stree) else stree


stree1 = "a"
stree2 = "aaa"
stree3 = "aaabbb"
stree4 = "aaabccc"
ans = compressor(stree1)
print(ans)