# Question:​ Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.

def maxSquare(arr):
	n=len(arr)
	m=len(arr[0])
	flow = 0; cnt=0; maxCnt=0

	for i in range(n):
		for j in range(m):
			a=0; b=0; cnt=0
			while (1):
				if arr[i][j] == 1:
					flow = 0
					if i+a<n:
						flow += 1
						if arr[i+a][b] != 1:
							break
					if j+b<m:
						flow += 1
						if arr[i][j+b] != 1:
							break
					if i+a<n and j+b<m:
						flow += 1
						if arr[i+a][j+b] != 1:
							break
				if flow == 3:
					cnt+=1
				else:
					break
				a+=1
				b+=1
			maxCnt = max(maxCnt, cnt)

	return maxCnt







mat = (
	[1,1,1,0],
	[1,1,1,1],
	[1,1,0,0]
)

print(maxSquare(mat))