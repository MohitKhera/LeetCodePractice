class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        for i, count in hm.items():
            freq[count].append(i)
        
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res