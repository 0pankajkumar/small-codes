import sys  
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')  

# def checkCHEF(s, index):
# 	chef = 'HEF'
# 	j = 0
# 	found = False
# 	for i in range(index + 1, index + 4):
# 		if s[i] == chef[j]:
# 			found = True
# 		else:
# 			found = False
# 			return found
# 		j += 1
# 	return found

# def analysisQ(s, index):
# 	s[index] == 'C'
# 	chef = 'HEF'
# 	j = 0
# 	for i in range(index + 1, index + 4):
# 		if s[i] == '?':
# 			s[i] = chef[j]
# 		else:
# 			for k in range(index, index + 4):
# 				s[k] = 'A'
# 			return False
# 		j += 1
# 	return True


def chefify(s, start, end):
	print(f"chefify({start}, {end})")
	chef = 'CHEF'
	j = 0
	for i in range(start, end):
		s[i] = chef[j]
		print(f"j = {j}")
		j += 1
def lookForChef(s, start, end):
	print(f"lookForChef( {start}, {end})")
	chef = 'CHEF'
	j = 0
	for i in range(start, end):
		if s[i] == '?' or s[i] == chef[j]:
			continue
		else:
			return False
		j += 1
	chefify(s, start, end)
	return True

def aefy(s):
	for i in range(len(s)):
		if s[i] == '?':
			s[i] = 'A'

for t in range(int(input())):
	s = list(input())
	for i in range(len(s)):
		lookForChef(s, i, i + 4)

	aefy(s)
	print(''.join(s))



