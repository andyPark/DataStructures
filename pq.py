import heapq
import time
from DataStructures.sort import merge_sort

class BadPriorityQueue:
    def __init__(self):
        self._queue = []
    
    def push(self, item):
        self._queue.append(item)
    
    def pop(self):
        min_i = len(self._queue)
        min_value = float('inf')
        for i in range(len(self._queue)):
            if self._queue[i][0] < min_value:
                min_i = i
                min_value = self._queue[i][0]
        return self._queue.pop(min_i)[-1]
    
class SortPriorityQueue:
    def __init__(self):
        self._queue = []
    
    def push(self, item):
        self._queue.append(item)
        self._queue = merge_sort(self._queue)
    
    def pop(self):
        return self._queue.pop()

class GoodPriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item):
        heapq.heappush(self._queue, item)

    def pop(self):
        return heapq.heappop(self._queue)

"""
q = GoodPriorityQueue()
start_time = time.time()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 2)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
end_time = time.time()
print("Total Elapsed Time: {0}".format((end_time - start_time) * 100000))
"""