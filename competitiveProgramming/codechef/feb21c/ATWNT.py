import sys
sys.stdin = open('input.txt', 'r')

# class Node(object):
#     def __init__(self, roll_no):
#         self.roll_no = roll_no

def make_graph():
    for i in range(n-1):
        current_index = pss[i]
        try: 
            graph[current_index].append(i+2)
        except KeyError:
            graph[current_index] = [i+2]


def dfs(cur, no_of_tasks):
    global incomplete_count
    if cur in graph:
        no_of_children = len(graph[cur])
        if no_of_tasks % no_of_children == 0:
            task_divided_into = no_of_tasks // no_of_children
            no_of_tasks = task_divided_into
            # incomplete_count += no_of_tasks
        else:
            incomplete_count += no_of_tasks
            return
        for individual in graph[cur]:
            # print(individual, end=" ")
            dfs(individual, no_of_tasks)




n = int(input())
pss = list(map(int, input().split()))
q = int(input())

graph = {1: []}
make_graph()
# print(graph)

incomplete_count = 0

for i in range(q):
    node, no_of_tasks = map(int, input().split())

    if node not in graph:
        print(no_of_tasks)
    else:
        incomplete_count = 0
        dfs(node, no_of_tasks)
        print(incomplete_count)
