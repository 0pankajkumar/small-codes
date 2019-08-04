# cook your dish here

def calculate():
    N,K = list(map(int,input().split()))
    
    i = 1
    while(N % K == 0 and N > 0):
        if i == K:
            i = 1
        N = N - K
        i += 1

    if N == 0 and i == K:
        print("NO")
    else:
        print("YES")
    
    
cases = int(input())

for cas in range(cases):
    calculate()