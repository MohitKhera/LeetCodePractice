class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        visited = set() 
        def dfs(r, c):
            if (r, c) not in visited:
                visited.add((r,c))
                for i in directions:  
                    temp_row = r + i[0] 
                    temp_col = c + i[1] 
                    if 0 <= temp_row < len(board) and 0 <= temp_col < len(board[0]) and board[temp_row][temp_col] == "O" and (temp_row, temp_col) not in visited: 
                        dfs(temp_row, temp_col) 

        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if ((i == 0) or (i == len(board) - 1) or (j == 0) or (j == len(board[0]) - 1)) and (board[i][j] == "O"): 
                    dfs(i, j) 
                    
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if (i, j) not in visited and board[i][j] == "O": 
                    board[i][j] = "X"