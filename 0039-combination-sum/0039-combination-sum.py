class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        def dfs(i, curComb, total):
            if total == target:
                combs.append(curComb.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curComb.append(candidates[i])
            dfs(i, curComb, total + candidates[i])

            curComb.pop()
            dfs(i+1, curComb, total)

        dfs(0, [], 0)
        return combs