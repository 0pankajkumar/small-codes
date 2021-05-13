# Binary search tree with minimum height from an array

# Assumptions
# While inserting:
# Our inserting action is the only way to disturb a BST
# And this distrubance happens only at the end of tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, current_root, node):
        # TODO add a check to balance out skewness
        if self.root.value <= node.value:
            if root.left is None:
                root.left = node
                return True
            self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
                return True
            self.insert(root.right, node)

    def find(self, current_root=self.root, target):
        if current_root is None:
            return False

        elif current_root.value == target.value:
            return True
        
        elif current_root.value < target.value:
            self.find(current_root.left, target)
            
        elif current_root.value > target.value:
            self.find(current_root.right, target)


def make_bst(arr):
    bst = None
    for a in arr:
        if bst is None:
            bst = BST(a)
        else:
            bst.insert(a)





arr = [1, 2, 3, 4, 5, 6, 7]

print(make_bst(arr))


