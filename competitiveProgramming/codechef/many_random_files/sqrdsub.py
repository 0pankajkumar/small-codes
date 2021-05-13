import sys
sys.stdin = open("input.txt", 'r')

from functools import reduce
def check3(prod):
    if prod % 2 != 0:
        return True
    else:
        return False

def check33(prod):
    if prod % 4 == 0:
        return True
    else:
        return False

def check2(prod):
    if prod % 2 == 0:
        if (prod/2) % 2 <= 0:
            return True
    else:
        if (prod/2) % 2 > 0:
            return True
    return False

def check1(prod):
    if prod % 4 == 2:
        return False
    else:
        return True

for ssss in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    prod = 1
    ans = 0

    bigprod = reduce((lambda x,y:x*y),arr)


    for i in range(n-1,-1,-1):
        # print()
        prod = bigprod
        for j in range(i+1):

            # print(prod, end=" ")
            if check2(prod):
                # print("prod",prod)
                ans += 1
            # elif check33(prod):
            #     ans += 1
            # else:
            #     break

            if j < i:
                prod /= arr[j]
            else:
                prod = prod

        bigprod /= arr[i]

    print(ans)
