class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first > second:
                heapq.heappush(heap, -(first-second))
        if heap:
            return abs(heap[0])
        else:
            return 0   