class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = {}
        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
        s2_count = {}
        for i in range(len(s1)):
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)
        if s2_count == s1_count:
            return True
        for i in range(len(s1), len(s2)):
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)
            old_char = s2[i - len(s1)]
            s2_count[old_char] -= 1
            if s2_count[old_char] == 0:
                del s2_count[old_char]
            if s2_count == s1_count:
                return True
        return False

