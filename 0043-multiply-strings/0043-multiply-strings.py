class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        res = [0] * (len(num1) + len(num2))

        rev_num1 = num1[::-1]
        rev_num2 = num2[::-1]

        for d1 in range(len(num1)):
            for d2 in range(len(num2)):
                digit = int(rev_num1[d1]) * int(rev_num2[d2])
                # Ensure the every digit that is added during subsequent multi-level mulitiplication is accounted for in the carry over
                res[d1 + d2] += digit                  
                res[d1 + d2 + 1] += res[d1 + d2] // 10
                res[d1 + d2] = res[d1 + d2] % 10
        res = res[::-1]
        beginning = 0
        while beginning < len(res) and res[beginning] == 0:
            beginning += 1
        res = map(str, res[beginning:])
        return "".join(res)
                
                