import multiprocessing
import time
def calc_square(number):
    print('Square:' , number * number)
    result = number * number
    print(result)
def calc_quad(number):
    print('Quad:' , number * number * number * number)
    
if __name__ == "__main__":
    number = 7
    result = None

number = 7

p1 = multiprocessing.Process(target=calc_square, args=(number,))
p2 = multiprocessing.Process(target=calc_quad, args=(number,))

t1 = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
t2 = time.time()

# Wont print because processes run using their own memory location                     
print(result)
print("Time : ", t2 - t1)