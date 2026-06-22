class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n
        # steps = [0] * (n+1)
        # steps[1] = 1
        # steps[2] = 2
        # for i in range(3, n + 1):
        #     steps[i] = steps[i - 1] + steps[i - 2]
        # return steps[n]
        cache = [-1] * (n)
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)