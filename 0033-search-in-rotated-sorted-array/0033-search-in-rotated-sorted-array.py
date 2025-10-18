class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        start, end = 0, len(nums) - 1

        while start <= end:
            m = start + (end - start) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[start]:
                if nums[start] <= target < nums[m]:
                    end = m - 1
                else:
                    start = m + 1
            elif nums[m] <= nums[start]:
                if nums[m] < target <= nums[end]:
                    start = m + 1
                else: 
                    end = m - 1
        return res