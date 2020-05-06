# Question​ : Given k sorted arrays, merge them into a single sorted array

from queue import PriorityQueue

def mergeKArrays(arrArr):
	ans = list()
	PQ = PriorityQueue()

	for i in range(len(arrArr)):
		t = dict()
		t["arrayNo"] = i
		t["index"] = 0
		PQ.put((arrArr[i][0],t))

	while PQ.qsize() > 0:
		t = PQ.get_nowait()
		ans.append(t[0])
		listNumber = t[1]["arrayNo"]
		innerIndex = t[1]["index"]

		if innerIndex+1 < len(arrArr[listNumber]):
			t= dict()
			t["arrayNo"] = listNumber
			t["index"] = innerIndex+1
			v = arrArr[listNumber][innerIndex+1]
			PQ.put((v,t))

	return ans


arrArr = [
	[1,4,7],
	[2,5,8],
	[3,6,9]
]

print(mergeKArrays(arrArr))