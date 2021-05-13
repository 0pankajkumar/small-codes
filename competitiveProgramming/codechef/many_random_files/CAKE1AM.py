import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

for t in range(int(input())):
    a, b, p, q = map(int, input().split())
    c, d, r, s = map(int, input().split())

    if c > p:
        if d > q:
            case = 0
        else:
            case = 1
    elif c < p and r < p:
