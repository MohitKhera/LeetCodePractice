class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 1
        n = len(s)
        if n == 0:
            return ""
        cache = []
        for i in range(n):
            cache.append([False] * n)
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[j] == s[i] and (j - i <= 2 or cache[i+1][j-1] == True):
                    cache[i][j] = True
                    if (j - i + 1) > resLen:
                        resLen = j - i + 1
                        resIdx = i
        return s[resIdx: resIdx + resLen]