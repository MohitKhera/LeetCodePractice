class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo = {}
        # def dfs(amount):
        #     res = 9999999999999999
        #     if amount == 0:
        #         return 0
        #     if amount in memo:
        #         return memo[amount]
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
        #     memo[amount] = res
        #     return res
        # minCoins = dfs(amount)
        # if minCoins >= 9999999999999999:
        #     return -1
        # else:
        #     return minCoins

        dp = [9999999999] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        if dp[amount] >= 9999999999:
            return -1
        else:
            return dp[amount]

