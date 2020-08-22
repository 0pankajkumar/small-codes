# st = "I LIKE TO plaY FooTBall"

# temp = st.split()

# ans = list()


# for i in range(len(temp)):
# 	if i == 0:
# 		ans.append(temp[0].lower())
# 	else:
# 		ans.append(temp[i].capitalize())

# print(''.join(ans))




# st = "{{}}"

# def find(st):
# 	if len(st) % 2 != 0 :
# 		return False

# 	curly = 0
# 	rnd = 0
# 	square = 0

# 	for s in st:
# 		if s == "{":
# 			curly += 1
# 		elif s == "}":
# 			if curly != 0:
# 				curly -= 1
# 			else:
# 				return False

# 		elif s == "(":
# 			rnd += 1
# 		elif s == ")":
# 			if rnd != 0:
# 				rnd -= 1
# 			else:
# 				return False

# 		elif s == "[":
# 			square += 1
# 		elif s == "]":
# 			if square != 0: 
# 				square -= 1
# 			else:
# 				return False

# 	if curly == 0 and square == 0 and rnd == 0:
# 		return True
# 	else:
# 		return False


# print(find(st))


req = 6
# arr = [1, 5, 7, -1, 5]
arr = [2, 1, 5, 7, -1, 4]
count = 0

bank = set()

for a in arr:
	
	t = req - a
	if t in bank:
		count += 1

	bank.add(a)


print(count)



















































