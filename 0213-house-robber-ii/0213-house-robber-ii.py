class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # n = len(nums)
        # cache = [[-1] * 2 for i in range(n)]
        # def dfs(i, flag):
        #     if i >= n or (flag and i == n - 1):
        #         return 0
        #     if cache[i][flag] != -1:
        #         return cache[i][flag]
        #     cache[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag or i == 0))
        #     return cache[i][flag]

        # return max(dfs(0, False), dfs(1, False))

        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        def helper(sub_nums):
            n = len(sub_nums)
            if not sub_nums:
                return 0
            if n == 1:
                return sub_nums[0]
            dp = [-1] * n
            dp[0], dp[1] = sub_nums[0], max(sub_nums[0], sub_nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], sub_nums[i] + dp[i - 2])
            return dp[n-1]

        return max(helper(nums[1:]), helper(nums[:-1]))