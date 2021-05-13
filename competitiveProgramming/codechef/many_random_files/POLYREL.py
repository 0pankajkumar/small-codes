import sys  
sys.stdin = open('input.txt', 'r') 

'''
Author : pankaj2kumar@codechef
'''

def get_answer(n, count):
    if n < 7:
        return count
    
    # if n % 2 == 0:
    #     n += 1

    t = n // 2
    count += t

    return get_answer(t, count)

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        s = input()

    count = get_answer(n, n)

    print(count)
