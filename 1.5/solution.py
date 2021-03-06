import heapq

class PriorityQueue:
    def _init_(self):
        self._queue=[]
        self._index=0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index +=1

    def pop(self):
        return heapq.heappop(self._queue)[-1]