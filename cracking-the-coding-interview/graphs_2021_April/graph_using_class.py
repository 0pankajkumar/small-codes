class Node:
    def __init__(self, value):
        self.value = value
        self.next = []

# Can be defined like this
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)

# Or this
nodes = []
for i in range(1,9):
    nodes.append(Node(i))

one.next = [two, three, four]
two.next = [one]
three.next = [six]
four.next = [one, five]
five.next = [four, seven, eight]
six.next = [three]
seven.next = [five]
eight.next = [five]

def dfs(root, visited):
    # if root is None:
    #     return
    visited.add(root.value)
    print(root.value, end=" ")
    for n in root.next:
        if n.value not in visited:
            dfs(n, visited)


dfs(one, set())

