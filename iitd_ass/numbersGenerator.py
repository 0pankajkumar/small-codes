from random import random

n = 1000

with open("input1.txt", 'w', encoding='utf-8') as f:
	for i in range(n):
		t = str(random())+"\n"
		f.write(t)