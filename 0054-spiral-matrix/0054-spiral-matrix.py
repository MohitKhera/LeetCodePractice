class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            for i in range(right - left):
                res.append(matrix[top][left + i])
            top += 1
            for i in range(bottom - top):
                res.append(matrix[top + i][right - 1])
            right -= 1

            if (left >= right or top >= bottom):
                break
                
            for i in range(right - left):
                res.append(matrix[bottom - 1][right - 1 - i])
            bottom -= 1
            for i in range(bottom - top):
                res.append(matrix[bottom - 1 - i][left])
            left += 1

        return res