# cook your dish here
import time

def calculate():
    N,K = list(map(int,input().split()))
    
    t1 = time.time()

    i = 1
    while(N % K == 0 and N > 0):
        if i == K:
            i = 1
        N = N - K
        i += 1

        # print(N, K)

    # print(f"N = {N}") 


    
    if N == 0 and i == K:
        print("NO")
    else:
        print("YES")
    t2 = time.time()
    print(f"Time taken : {t2- t1}")
    
    
cases = int(input())

for cas in range(cases):
    calculate()