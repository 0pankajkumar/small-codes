import sys
sys.stdin = open('input.txt', 'r')


def solve22():
    pass
    # prev = arr[1]
    # mini = 9999
    # maxi = -9999
    # if arr[1]-arr[0] <= 2:
    #     mini = 2
    #     maxi = 2
    # else:
    #     mini = 1
    #     maxi = 1

    # chain = 0
    # ans = []
    # flag = None
    # firstLove = False

    # for i in range(2, n):
    #     # print("arr[i]", arr[i], end=" ")
    #     if arr[i]-prev <= 2:
    #         # sequence is forming, continue
    #         flag = False
    #         chain += 1
    #     else:
    #         if firstLove:
    #             flag = True
    #             ans.append(chain)
    #             chain = 0
    #             print("index, ans", i, ans)
    #             firstLove = False

    #     prev = arr[i]

    # if len(ans) == 0 or flag is False:
    #     ans.append(chain)
    # print("ans", ans)
    # print(min(ans)+1, max(ans)+1)


for ss in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    pev = None
    conn = 0
    ans = list()
    lastKiss = None

    for i in range(n):
        if pev is not None:
            if arr[i]-pev <= 2.0:
                conn += 1
                lastKiss = True
                pev = arr[i]
            else:
                pev = arr[i]
                ans.append(conn)
                conn = 0
                lastKiss = False
        else:
            pev = arr[i]
    if lastKiss:
        ans.append(conn)
    print(min(ans)+1, max(ans)+1)
