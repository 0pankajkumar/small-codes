import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')



def dfs(start):
    #if start is None:
    #    return

    if len(graph[start]) == 0:
        return start

    prev = start

    for e in graph[start]:
        dfs(e)
        #print(e, "-", prev, "=", e-prev)
        print(wealth[prev], "-", wealth[e], "=", wealth[prev] - wealth[e])
        #maxi[0] = max(wealth[prev] - wealth[e], maxi[0])

        maxi[0] = max(maxi[1] - wealth[e], maxi[0])
        maxi[1] = max(maxi[1], wealth[e])
        prev = e
    return start


def dfs2(start):
    #if start is None:
    #    return

    if len(graph[start]) == 0:
        return start

    maxi[1] = max(maxi[1], wealth[start])
    prev = start

    for e in graph[start]:
        dfs2(e)
        #print(wealth[prev], "-", wealth[e], "=", wealth[prev] - wealth[e])

        maxi[0] = max(maxi[1] - wealth[e], maxi[0])
        prev = e
    return start





n = int(input())
wealth = list(map(int, input().split()))
wealth.insert(0,0)
managers = list(map(int, input().split()))

# Making the graph
graph = {}
for i in range(n+1):
    graph[i] = list()

i = 1
for m in managers:
    if m == -1:
        graph[0].append(i)
    else:
        graph[m].append(i)
    i += 1

def dfs3(start, maxval):
    maxval = max(maxval, wealth[start])
    maxi[0] = max(maxi[0], maxval - wealth[start])

    for e in graph[start]:
        dfs3(e, maxval)


maxi = [-9999999, wealth[0]]
dfs3(0, wealth[0])
print(maxi[0], end="")

    