import sys
import math
from collections import deque
sys.stdin = open("input.txt", 'r')

source, destination = map(int, input().split())
n, m =  map(int, input().split())
flash_time = list(map(int, input().split()))
flash_time.insert(0,0)

edge_info = []
for i in range(m):
    t = tuple(map(int, input().split()))
    edge_info.append(t)


# Making the graph
graph = {}
for e in edge_info:
    if e[0] in graph:
        graph[e[0]].append((e[1], e[2]))
    else:
        graph[e[0]] = [(e[1], e[2])]

    if e[1] in graph:
        graph[e[1]].append((e[0], e[2]))
    else:
        graph[e[1]] = [(e[0], e[2])]

#print(graph)



visited = {source}
dist = [999999]*(n+1)
dist[source] = 0
current = source
queue = deque()
queue.append(source)

def signal_time(till_now, interval):
    ans = (interval - till_now % interval) % interval
    #return ans if ans != interval else 0
    return ans

while len(visited) < n:
    if dist[current] == 999999:
        break
    for ver in graph[current]:
        if ver[0] not in visited:
            till_now =  dist[current]+ ver[1]
            if ver[0] != destination:
                dist[ver[0]] = min(dist[ver[0]], till_now + signal_time(till_now, flash_time[ver[0]]))
            else:
                dist[ver[0]] = min(dist[ver[0]], till_now)


            #if ver[0] != destination:
            #    till_now = flash_time[ver[0]] * ((till_now + flash_time[ver[0]] - 1) / flash_time[ver[0]])
            #dist[ver[0]] = min(dist[ver[0]], till_now)

            #if till_now < dist[ver[0]]:
            #    dist[ver[0]] = till_now


            queue.append(ver[0])


    print("Visited",current, "weight", dist[current])
    visited.add(current)
    current = queue.popleft()

print(dist[destination], end="")
















