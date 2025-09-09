class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row - 1
        while top <= bottom:
            mid_row = top + ((bottom - top) // 2)
            if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                break
            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
        if not (top <= bottom):
            return False
        
        l, r = 0, col - 1
        while l <= r:
            mid = l + ((r-l)//2)
            if target < matrix[mid_row][mid]:
                r = mid - 1
            elif target > matrix[mid_row][mid]:
                l = mid + 1
            else:
                return True
        return False