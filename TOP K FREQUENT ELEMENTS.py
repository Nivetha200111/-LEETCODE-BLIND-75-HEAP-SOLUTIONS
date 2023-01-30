from collections import Counter
from heapq import heapify, heappop

def topKFrequent(nums, k):
    # count the frequency of each number in the nums list
    count = Counter(nums)

    # heapify the count dictionary
    heap = [[-val, key] for key, val in count.items()]
    heapify(heap)

    # pop the top k frequent elements from the heap
    result = []
    for _ in range(k):
        result.append(heappop(heap)[1])

    return result
