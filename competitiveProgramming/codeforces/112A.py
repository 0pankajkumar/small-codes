
first = input().lower()
second = input().lower()
equality = 0
for i in range(len(first)):
	if first[i] < second[i]:
		equality = -1
		break
	elif first[i] > second[i]:
		equality = 1
		break

print(equality)