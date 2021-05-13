# cook your dish here
import time

def calculate():
    N,K = list(map(int,input().split()))

    t1 = time.time()
    
    # Subtract K from N exactly K times
    # If N == 0, successfully distributed
    # If N < 0, unsucessful
    # If N > 0, repeat

    while(N > 0):
        N = N - (K * K)

        if N < 0:
            print("YES")
            t2 = time.time()
            print(f"Time taken : {t2- t1}")
            return
        elif N == 0:
            print("NO")
            t2 = time.time()
            print(f"Time taken : {t2- t1}")
            return


    # if N == 0 and i == K:
    #     print("NO")
    # else:
    #     print("YES")


cases = int(input())

for cas in range(cases):
    calculate()
