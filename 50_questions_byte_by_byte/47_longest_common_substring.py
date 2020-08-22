# Question​ : Given two strings, write a function that returns the longest common substring

# Works only with same length strings
def lcs(a, b):
	bucket = [[0]*(len(a)+1)]*(len(b)+1)
	ans = ""

	for i in range(len(a)):
		for j in range(len(b)):
			if a[i] == b[j]:
				if i==0 or j == 0:
					bucket[i][j] = 1
				else:
					bucket[i][j] = bucket[i-1][j-1] + 1

				if len(ans) < bucket[i][j]:
					l = bucket[i][j]
					ans = a[i-l+1 : i+1]

	return ans


a = "maythelovebewithpankajthegreat"
b = "whyispankajnotmakingthenexthot"
ans = lcs(a, b)
print(ans)
