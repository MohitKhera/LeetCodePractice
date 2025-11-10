class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    q.append([val, time + n])
            if q:
                if q[0][1] == time:
                    num = q.popleft()
                    heapq.heappush(maxHeap, num[0])
        return time