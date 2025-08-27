class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        RPN = []
        for i in tokens:
            if i == "+":
                RPN.append(RPN.pop() + RPN.pop())
            elif i == "-":
                second = RPN.pop() 
                first = RPN.pop()
                RPN.append(first - second)
            elif i == "*":
                RPN.append(RPN.pop() * RPN.pop())
            elif i == "/":
                second = RPN.pop() 
                first = RPN.pop()
                RPN.append(int(first / second))
            else:
                RPN.append(int(i))
        return RPN[0]  