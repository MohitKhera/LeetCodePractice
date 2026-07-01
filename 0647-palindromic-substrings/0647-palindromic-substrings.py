class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        if n == 0:
            return ""
        cache = []
        for i in range(n):
            cache.append([False] * n)
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (j - i <= 2 and s[i] == s[j]) or (s[i] == s[j] and j-i >= 2 and (cache[i+1][j-1] == True)):
                    cache[i][j] = True
                    res += 1
        return res