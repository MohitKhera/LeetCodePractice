class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Check if there is a zero in the first row/column
        first_row_zero = False
        first_col_zero = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                first_row_zero = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Mark in the first row/column what rows and columns need to be zeroed out 
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        # Check every cell in the inner matrix, if a row or column is set to be zeroed out + cell is in that row or column, set the cell to zero
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # If the first row/column was set to be zeroed out, zero the row/column out
        if first_row_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0                   