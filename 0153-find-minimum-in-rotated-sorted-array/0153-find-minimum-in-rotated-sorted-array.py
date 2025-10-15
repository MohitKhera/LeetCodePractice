class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break
            m = (end+start)//2
            res = min(res, nums[m])
            if nums[m] >= nums[start]:
                start = m+1
            else:
                end = m-1
        return res