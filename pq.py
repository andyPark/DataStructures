import heapq
import time
from DataStructures.sort import merge_sort

class IPriorityQueue:
    def push(self, item): # insert an element into the queue
        pass
    
    def pop(self): # return the highest priority element and remove it from the queue
        pass

class BadPriorityQueue:
    def __init__(self):
        self._queue = []
    
    def push(self, item):
        self._queue.append(item)
    
    def pop(self):
        min_i = len(self._queue)
        min_value = float('inf')
        for i in range(len(self._queue)):
            if self._queue[i] < min_value:
                min_i = i
                min_value = self._queue[i]
        return self._queue.pop(min_i)
    
class SortPriorityQueue:
    def __init__(self):
        self._queue = []
    
    def push(self, item):
        self._queue.append(-1 * item)
        self._queue = merge_sort(self._queue)
    
    def pop(self):
        return -1 * self._queue.pop()

class GoodPriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item):
        heapq.heappush(self._queue, item)

    def pop(self):
        return heapq.heappop(self._queue)

"""
bpq = pq.BadPriorityQueue()
bpq.push(5)
bpq.push(3)
bpq.push(2)
bpq.push(4)
bpq.push(1)
bpq.pop()
"""