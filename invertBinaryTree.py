# Program to invert a binary tree
# Make all left elements as right & vice versa
# Courtesy:
# Twitter > https://twitter.com/mxcl/status/608682016205344768?lang=en
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.


class Bubble:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


class Tree:
    def __init__(self, root):
        self.root = root

    def traverse(self, root):
        # Pre-order traversal
        if root:
            print(root.value, end=" ")
            self.traverse(root.left)
            self.traverse(root.right)

    def invert(self, root):
        # Invert. Convert left to right & vice-versa
        # if root.left is None and root.right is None:
        #     return
        # else:
        if root:
            self.invert(root.left)
            self.invert(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp


root = Bubble(None, None, 0)
first = Bubble(None, None, 1)
second = Bubble(None, None, 2)
third = Bubble(None, None, 3)
fourth = Bubble(None, None, 4)
fifth = Bubble(None, None, 5)
sixth = Bubble(None, None, 6)

root.left = first
root.right = second
first.left = third
first.right = fourth
second.left = fifth
second.right = sixth

'''
        0
      1  2
    3  4 5 6
'''

w = Tree(root)
print("Before")
w.traverse(w.root)
print()

w.invert(w.root)
w.traverse(w.root)
print()
