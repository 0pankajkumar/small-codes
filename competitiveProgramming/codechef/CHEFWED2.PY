#                        __           _                    __       
#     ____  ____ _____  / /______ _  (_)  _________  _____/ /_______
#    / __ \/ __ `/ __ \/ //_/ __ `/ / /  / ___/ __ \/ ___/ //_/ ___/
#   / /_/ / /_/ / / / / ,< / /_/ / / /  / /  / /_/ / /__/ ,< (__  ) 
#  / .___/\__,_/_/ /_/_/|_|\__,_/_/ /  /_/   \____/\___/_/|_/____/  
# /_/                          /___/                                


import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

family = list()
n = 0
k = 0


def get_inefficiency(cur, ineff, bank, isFirst):
	# print(f"cur {cur} ineff {ineff}")
	if cur >= n:
		return ineff

	for i in range(cur, n):
		if family[i] not in bank:
			bank.add(family[i])
			cur += 1
		else:
			newBank = set()

			add = 0
			if isFirst:
				add = 2
				isFirst = False
			else:
				add = 1
			ans1 = get_inefficiency(cur+1, ineff+add, bank, isFirst)
			ans2 = get_inefficiency(cur, ineff+k, newBank, isFirst)

			# print(f"ans1={ans1} cur={cur+1} ineff={ineff+1} bank={bank}")
			# print(f"ans2={ans2} cur={cur+1} ineff={ineff+k} newBank={newBank}")

			ineff = min(ans1, ans2)
			return ineff
	return ineff

for sss in range(int(input())):
	n,k = map(int, input().split())
	family = list(map(int, input().split()))

	bank = set()

	ans = get_inefficiency(0, k, bank, True)
	print(ans)