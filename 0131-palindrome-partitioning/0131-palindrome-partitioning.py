class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(j, i):
            while j < i:
                if s[j] != s[i]:
                    return False
                j += 1
                i -= 1
            return True
        start, path = 0, []
        result = []
        def explorePartition(start, path):
            if start >= len(s):
                result.append(path.copy())
                return
            for i in range(start, len(s)):
                if isPalindrome(start,i):
                    path.append(s[start:i+1])
                    explorePartition(i+1, path)
                    path.pop()
        explorePartition(start, path)
        return result