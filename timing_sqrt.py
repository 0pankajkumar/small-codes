import time, math

pp = [1, 2, 3, 4, 5, 6]
t = 0
for p in pp:
	t1 = time.time()
	math.sqrt(p)
	t2 = time.time()
	t += t2 - t1

print(t / len(pp))




