class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}
        for node, target, length in times:
            adj[node].append([target, length])
        dist = [float('inf')] * (n+1)
        dist[k] = 0

        heap = []
        heapq.heappush(heap, [0, k])

        while len(heap) != 0:
            top = heapq.heappop(heap)
            d = top[0]
            u = top[1]

            if d > dist[u]:
               continue;

            for i in adj[u]:
                v = i[0]
                w = i[1]

                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, [dist[v], v])

        if float('inf') in dist[1::]:
            return -1
        
        return max(dist[1::])