import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


for _ in range(int(input())):
    arr = list(map(int, input().split()))

    l = len(arr)

    arr = sorted(arr)

    if arr[-1] == l - 1:
        print(arr[-2])
    else:
        print(arr[-1])
