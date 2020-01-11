from itertools import permutations
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def check(arr):
    c = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            arr[j]

            # for _ in range(int(input())):
n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

count = 0
bank = permutations(arr)
for b in bank:
    count += check(b)
