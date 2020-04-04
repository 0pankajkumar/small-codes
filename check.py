
# ls = [1, 2, 3, 4, 5, 7, 0, 0, 5]


# flag1 = False
# flag2 = False
# flag3 = False
# for l in ls:
# 	if l == 0:
# 		flag1 = True
# 	if l == 0 and flag1 == True:
# 		flag2 = True
# 	if l == 7 and flag2 == True:
# 		flag3 = True
# 		print(True)
# 		break
# if flag3 == False:
# 	print(False)





ls = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [1, 2, 3]]
# Check repetion
# Output : True 2

banks = list()
bigCount = 0

for l in ls:
	# Making a temp dict of all elemets in current list
	temp = dict()
	for i in range(len(l)):
		temp[i] = l[i]

	# Check whether we have same elemet in bank
	count = 0
	for ban in banks:
		for k,v in ban.items():
			if ban[k] == temp[k]:
				count += 1
	if count == 3:
		if bigCount == 0:
			bigCount += 2
		else:
			bigCount += 1
	else:
		banks.append(temp)

if bigCount > 0:
	print(True, bigCount)
else:
	print(False)



