class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_island_area = 0

        def bfs(r, c):
            nonlocal max_island_area
            q = deque()
            visit.add((r,c))
            q.append((r, c))
            cur_area = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [0,1], [-1, 0], [0, -1]]
                for dr, dc in directions:
                    if ((row + dr) in range(rows)) and ((col + dc) in range(cols)) and grid[row + dr][col + dc] == 1 and (row + dr, col + dc) not in visit:
                        q.append((row + dr, col + dc))
                        visit.add((row + dr, col + dc))
                        cur_area += 1
            max_island_area = max(cur_area, max_island_area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    bfs(r,c)
        return max_island_area