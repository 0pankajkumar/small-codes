import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

import math
for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = k*math.floor(n/k) + min(n%k, math.floor(k/2))
    print(ans)
