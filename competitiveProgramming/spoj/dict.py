# This is implemetation of trie which works fine
class Node:
    def __init__(self, alpha):
        self.alpha = alpha
        self.isWord = False
        self.next = dict()

class Trie:
    def __init__(self, node):
        self.start = node

    def insert(self, word):
        node = self.start

        length = len(word)
        i = 0

        for w in word:
            i += 1
            
            if w in node.next:
                node = node.next[w]
            else:
                node.next[w] = Node(w)
                node = node.next[w]

            if i == length:
                node.isWord = True

    def check(self, word):
        node = self.start
        for w in word:
            if w in node.next:
                node = node.next[w]
            else:
                return False

        # Bfs from this point
        bfsRoot = node
        Q = list() # the queue
        Q.append(bfsRoot)

        while(len(Q) != 0):
            curr = Q.pop()
            curr.




        # if node.isWord == True:
        #     return True

t = Trie(Node("*"))
t.insert('ant')
t.insert('axe')
t.insert('axex')
print(t.check('axex'))
