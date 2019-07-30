import math
cases = int(input())

for cas in range(cases):
	n = int(input())
	k = int(input())
	rough_division = math.ceil(k / n)
	distro_list = [0] * n
	for i in range(n - 1):
		distro_list[i] = rough_division

	distro_list[n - 1] = k - (rough_division * (n - 1))
	# print(distro_list)

	# Now find max difference part of question
	distro_list.sort()
	new_distro_list = [None] * n
	i = 0
	j = n - 1
	k = 0
	while(i <= j):
		if i == j and (n % 2 != 0):
			new_distro_list[n - 1] = distro_list[math.ceil(n/2)]
			break
		new_distro_list[k] = distro_list[i]
		new_distro_list[k+1] = distro_list[j]
		i += 1
		j -= 1
		k += 2
	print(new_distro_list)




