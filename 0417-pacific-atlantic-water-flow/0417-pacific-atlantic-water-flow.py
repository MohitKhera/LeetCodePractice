class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        atlantic_visited = set()
        pacific_visited = set()
        def dfs(r, c, visited):
            visited.add((r,c))
            for i in directions:
                temp_row = r + i[0]
                temp_col = c + i[1]
                if 0 <= temp_row < len(heights) and 0 <= temp_col < len(heights[0]) and heights[temp_row][temp_col] >= heights[r][c] and (temp_row, temp_col) not in visited:
                    dfs(temp_row, temp_col, visited)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    dfs(i, j, pacific_visited)
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    dfs(i, j, atlantic_visited)
        result = []
        for i in atlantic_visited:
            if i in pacific_visited:
                result.append(i)
        return result