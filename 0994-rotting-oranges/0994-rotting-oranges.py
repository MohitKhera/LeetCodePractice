class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
        minutes = 0
        group = len(q)
        while len(q) != 0:
            v = q.popleft()
            group -= 1
            for i in directions:
                temp_row = v[0] + i[0]
                temp_col = v[1] + i[1]
                if 0 <= temp_row < len(grid) and 0 <= temp_col < len(grid[0]) and grid[temp_row][temp_col] == 1:
                    grid[temp_row][temp_col] = 2
                    q.append([temp_row, temp_col])
            if group == 0 and len(q) != 0:
                minutes += 1
                group = len(q)
        for i in grid:
            if 1 in i:
                return -1
        return minutes