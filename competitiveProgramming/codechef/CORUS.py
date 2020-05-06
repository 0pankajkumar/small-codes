import sys
sys.stdin = open('input.txt', 'r')


def haish(stree, bank):
    tem = [0]*26
    for s in stree:
        ind = ord(s)-97
        tem[ind] += 1

    for t in tem:
        if t > 1:
            bank.append(t)


for ss in range(int(input())):
    n, q = map(int, input().split())
    stree = input()
    bank = list()
    haish(stree, bank)
    for i in range(q):
        c = int(input())
        q = 0
        if c == 0:
            q = n
        else:
            for b in bank:
                if c < b:
                    q += (b-c)
        print(q)
