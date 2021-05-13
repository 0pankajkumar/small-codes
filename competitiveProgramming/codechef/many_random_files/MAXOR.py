import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

bank = dict()


def check(a, b):
    if (a, b) in bank:
        return bank[(a, b)]
    else:
        if (a | b) <= max(a, b):
            bank[(a, b)] = True
            return True
        else:
            bank[(a, b)] = False
            return False


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    for i in range(n):
        for j in range(i, n):
            if j+1 < n:
                if check(arr[i], arr[j+1]):
                    count += 1

    print(count)
