class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combs = []
        def dfs(i, curComb, total):
            if total == target:
                combs.append(curComb.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curComb.append(candidates[i])
            dfs(i+1, curComb, total + candidates[i])

            curComb.pop()
            while i != len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curComb, total)


        dfs(0, [], 0)
        return combs