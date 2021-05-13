
import sys
sys.stdin = open("input.txt", 'r')

import math
def solver1():
	for ssss in range(int(input())):
		l,d,s,c = map(int, input().split())
		suma = 0
		d1 = s
		t = s
		if d == 1:
			t = (d1 + c * d1)
		else:
			for i in range(d-1):
				t = (d1 + c * d1)
				d1 = t
				if t >= l:
					break
				print(t,"=",d1,"+",c,"*",d1)
				
		print("ALIVE AND KICKING" if t >= l else "DEAD AND ROTTING")

def solver11():
	for ssss in range(int(input())):
		l,d,s,c = map(int, input().split())
		tmp = s
		i = 2
		# if d == 1:
		# 	tmp = s + tmp * c
		# else:
		while i <= d:
			tmp = tmp + tmp * c
			# print(tmp,"+",tmp,"*",c)
			if tmp >= l:
				break
			i += 1
		print("ALIVE AND KICKING" if tmp >= l else "DEAD AND ROTTING")		


def solver2():
	for ssss in range(int(input())):
		l,d,s,c = map(int, input().split())
		suma = 0
		d1 = s
		t = 0

		if d == 1:
			suma = (d1 + c * d1)
		else:
			d1 = (d1 + c * d1)
			d2 = (d1 + c * d1)
			d3 = (d2 + c * d2)
			r = d3 / d2
			suma = d1 * (int)(math.pow(r,d-2))
			# print(suma)
		
		print("ALIVE AND KICKING" if (suma) >= l else "DEAD AND ROTTING")


def solver3():
	for ssss in range(int(input())):
		l,d,s,c = map(int, input().split())
		suma = 0
		d1 = l
		t = 0
		if d == 1:
			suma = (d1 + c * d1)
		else:
			for i in range(d-1):
				t = (d1 + c / d1)
				suma += t
				d1 = t
				# print(t,"=",d1,"+",c,"*",d1)
				# print("suma =",suma)
		
		print("ALIVE AND KICKING" if round(suma) <= s else "DEAD AND ROTTING")

def handle():
	solver11()

handle()