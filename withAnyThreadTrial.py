import threading
import time
def calc_square(number):
	print('Square:' , number * number)
	for i in range(1000000):
		number *= i
def calc_quad(number):
	print('Quad:' , number * number * number * number)
	for i in range(1000000):
		number *= i
if __name__ == "__main__":
	number = 7
	t1 = time.time()
	calc_square(number)
	calc_quad(number)
	t2 = time.time()
	print("Time : ", (t2 - t1)*1000)


