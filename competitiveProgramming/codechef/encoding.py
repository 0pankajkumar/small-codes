# cook your dish here
import time

# takes a number & puts zeros wherever it finds a repeat
def putZerosOnRepeat(a):
    b = list(str(a))
    temp = "X"
    for i in range(len(b)):
        if b[i] == temp:
            b[i] = "0"
        else:
            temp = b[i]
    c = ''.join(b)
    return (int(c))

# Calculates modulus of a large number
def modu(num, a): 
    num = str(num)
    # Initialize result 
    res = 0

    # One by one process all digits 
    # of 'num' 
    for i in range(0, len(num)): 
        res = (res * 10 + int(num[i])) % a; 

    return round(res)


def calculate():
    NL,L = list(map(int,input().split()))
    NR,R = list(map(int,input().split()))

    suma = 0

    for i in range(L, R + 1):
        suma += putZerosOnRepeat(i)

    print(modu(suma,7+1e9))

    
    
cases = int(input())

for cas in range(cases):
    calculate()