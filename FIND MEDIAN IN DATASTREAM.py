import heapq

class MedianFinder:
    def __init__(self):
        self.small_heap = [] # for the smaller half numbers
        self.large_heap = [] # for the larger half numbers
    
    def addNum(self, num):
        if len(self.small_heap) == len(self.large_heap):
            heapq.heappush(self.large_heap, -heapq.heappushpop(self.small_heap, -num))
        else:
            heapq.heappush(self.small_heap, -heapq.heappushpop(self.large_heap, num))
    
    def findMedian(self):
        if len(self.small_heap) == len(self.large_heap):
            return float(-self.small_heap[0] + self.large_heap[0]) / 2
        else:
            return float(self.large_heap[0])
