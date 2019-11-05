import time

d = dict()
for i in range(10000000):
	d[i] = True
	
e = list()
for i in range(10000000):
	e.append(i)

t1 = time.time()
print("Found :)" if 45423 in d else "Not found :(")
t2 = time.time()
print("Time taken by dict : ", (t2 - t1))


t1 = time.time()
print("Found :)" if 45423 in e else "Not found :(")
t2 = time.time()
print("Time taken by list : ", (t2 - t1))
