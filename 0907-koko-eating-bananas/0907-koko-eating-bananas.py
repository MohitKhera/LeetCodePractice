class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            middle = (r+l) // 2
            total_time = 0
            for i in piles:
                time = i // middle
                if i % middle != 0:
                    time += 1
                total_time += time
            if total_time <= h:
                ans = middle
                r = middle - 1    
            elif total_time > h:
                l = middle + 1
        return ans