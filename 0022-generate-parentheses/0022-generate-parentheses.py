class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def soln(open, close):
            if open == close == n:
                res.append("".join(stack))
                return res
            if open < n:
                stack.append("(")
                soln(open+1,close)
                stack.pop()
            if close < open:
                stack.append(")")
                soln(open,close+1)
                stack.pop()
        soln(0,0)
        return res