import sys
sys.stdin = open("input.txt", 'r')

'''
010 
101 Good

else bad
'''

for ssss in range(int(input())):
	st = input()
	flag1 = False
	flag2 = False
	i = 0

	# while i < len(st):
	# 	if st[i] == '0':
	# 		if i+1 < len(st):
	# 			if st[i+1] == '1':
	# 				if i+2 < len(st):
	# 					if st[i+2] == '0':
	# 						flag = True
	# 						break

	# 	if st[i] == '1':
	# 		if i+1 < len(st):
	# 			if st[i+1] == '0':
	# 				if i+2 < len(st):
	# 					if st[i+2] == '1':
	# 						flag = True
	# 						break

	# 	i += 1

	try:
		st.index("010")
		flag1 = True
	except:
		flag1 = False

	try:
		st.index("101")
		flag2 = True
	except:
		flag2 = False


	if flag1 or flag2:
		print("Good")
	else:
		print("Bad")