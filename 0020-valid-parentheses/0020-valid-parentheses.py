class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in dict:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if dict[top] != i:
                    return False
        return not stack