# cook your dish here
def makeItDict(rad):
    temp = dict()
    for ra in rad:
        if ra not in temp:
            temp[ra] = 1
        else:
            temp[ra] += 1
    return temp

def increment(rad, lower_limit, upper_limit):
    for i in range(lower_limit,upper_limit + 1):
        rad[i] += 1

def calculate():
    N = int(input())
    C = list(map(int,input().split()))
    H = list(map(int,input().split()))

    rad = [0] * (N + 1)
    rad[0] = "X"

    for i in range(1,N + 1):
        lower_limit = (i - C[i - 1]) if (i - C[i - 1]) > 0 else 1
        upper_limit = (i + C[i - 1]) if (i + C[i - 1]) < N + 1 else N
        # print(lower_limit)
        # print(upper_limit)
        increment(rad, lower_limit, upper_limit)
    # print(rad)

    # print(rad)
    xList = makeItDict(rad)
    # print(xList)
    for i in range(0,N):
        if H[i] not in xList:
            print("NO")
            return
        else:
            if xList[H[i]] == 0:
                print("NO")
                return
            else:
                xList[H[i]] -= 1

    print("YES")
    
    
    
cases = int(input())

for cas in range(cases):
    calculate()