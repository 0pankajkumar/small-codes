import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


# for _ in range(int(input())):
n, m = map(int, input().split())
s1 = input().split()
s2 = input().split()
s1.insert(0, s1[-1])
s2.insert(0, s2[-1])
#print(n, m)
for _ in range(int(input())):
    y = int(input())
    y1 = y % n
    y2 = y % m

    # y1 = n if y1 == 0 else y1
    # y2 = n if y2 == 0 else y1

    # ans = s1[y1] + s2[y2]  # + " " + str(y1) + " " + str(y2)
    ans = ''.join(s1[y1] + s2[y2])
    print(ans)
