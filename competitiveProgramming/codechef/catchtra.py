cases = int(input())

for cas in range(cases):
	ve = int(input())
	vy = int(input())
	L = int(input())
	T = int(input())

	t_standing = L / ve
	t_walking = L / (ve + vy)

	prob = (t_standing - t_walking) / T

	if prob > 1:
		prob = 1

	print(prob)