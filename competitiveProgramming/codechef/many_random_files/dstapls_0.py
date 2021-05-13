# cook your dish here

def calculate():
    N,K = list(map(int,input().split()))

    tmp = N / K
    tmp %= K

    if tmp == 0:
        print("NO")
    else:
        print("YES")


cases = int(input())

for cas in range(cases):
    calculate()
