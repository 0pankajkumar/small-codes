"""
Implement a function to check whether a tree is BST or not
"""

class Node:
    """Node structure for each node of tree"""
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value



def check(root, get):
    if root is None:
        # assuming all elements in BST are natural nos or > 0
        return 0

    high = check(root.left, "high")
    low = check(root.right, "low")

    if high is False or low is False:
        return False

    if high > root.value:
        return False
    elif low < root.value:
        return False
    else:
        return low if get == "high" else high


def checkStarter(root):
    ans = check(root)
    if isinstance(ans, int):
        return True
    else:
        return False
































