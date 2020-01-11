
import math
import random
for _ in range(int(input())):
    n = int(input())
    a = int(input())

    maxi = math.pow(10, n) - 1
    # s = random.randint(1,maxi-a)
    # s = int(a + maxi + maxi - 2)
    # print(s, flush=True)

    # t = int(maxi - 1)
    # p = s//2
    # q = s - p
    # s = p+q
    p = int(1 * maxi)
    q = int(1 * maxi)
    s = p+q+a
    print(s, flush=True)

    b = int(input())

    c = p - b
    print(c, flush=True)

    d = int(input())
    e = q - d
    print(e, flush=True)

    # print(a,b,c,d,e, a+b+c+d+e, s)
    res = int(input())
    if res == 1:
        continue
    else:
        break
