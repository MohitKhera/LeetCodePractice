class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        path = []
        def dfs(dig_index):
            if dig_index >= len(digits):
                result.append("".join((path)))
                return
            for i in phone[digits[dig_index]]:
                path.append(i)
                dfs(dig_index + 1)
                path.pop()
        
        dfs(0)

        return result

            
