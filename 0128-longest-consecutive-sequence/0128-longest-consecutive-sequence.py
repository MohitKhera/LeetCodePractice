class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        streak = 0
        for num in seq:
            if (num-1) not in seq:
                length = 1
                while (num+length) in seq:
                    length += 1
                streak = max(streak, length)
        return streak