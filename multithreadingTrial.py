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

thread1 = threading.Thread(target=calc_square, args=(number,))
thread2 = threading.Thread(target=calc_quad, args=(number,))# Will execute both in parallel

t1 = time.time()
thread1.start()
thread2.start()# Joins threads back to the parent process, which is this
	# program
thread1.join()
thread2.join()# This program reduces the time of execution by running tasks in parallel
t2 = time.time()
print("Time : ", (t2 - t1)*1000)