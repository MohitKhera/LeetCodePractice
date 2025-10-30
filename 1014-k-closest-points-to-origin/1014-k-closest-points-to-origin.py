class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            tmp = heapq.heappop(minHeap)
            res.append([tmp[1], tmp[2]])
        return res     