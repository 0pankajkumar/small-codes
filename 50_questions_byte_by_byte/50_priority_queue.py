# Implement a priority queue

# Assuming we are making max heap type ds
class PQ():
    def __init__(self):
        self.heap = list()

    def enqueue(self, value):
        self.heap.append(value)
        self.heapify()

    def deque(self):
        ele = self.heap.pop(0)
        self.heapify()
        return ele

    def heapify(self):
        i = 0
        length = len(self.heap)
        h = self.heap
        while i < length-2:
            if 2*i+1 < length:
                if h[2*i + 1] > h[i]:
                    t = h[2*i + 1]
                    h[2*i + 1] = h[i]
                    h[i] = t
            if 2*i+2 < length:
                if h[2*i + 2] > h[i]:
                    t = h[2*i + 2]
                    h[2*i + 2] = h[i]
                    h[i] = t 
            i += 1

mypq = PQ()
mypq.enqueue(10)
mypq.enqueue(2)
mypq.enqueue(3)
mypq.enqueue(4)
mypq.enqueue(20)
mypq.heapify()
print(mypq.heap)
print(mypq.deque())


print(mypq.heap)
print(mypq.deque())
print(mypq.heap)
print(mypq.deque())
