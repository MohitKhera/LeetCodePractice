class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # n = len(nums)
        # cache = [-1] * n

        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = max(dfs(i+1), nums[i] + dfs(i+2))
        #     return cache[i]

        # return dfs(0)

        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [-1] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]





