class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0

        for i in s:
            if i == "(":
                leftMin += 1
                leftMax += 1
            if i == ")":
                leftMin -= 1
                leftMax -= 1
            if i == "*":
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        if leftMin == 0:
            return True
        else:
            return False