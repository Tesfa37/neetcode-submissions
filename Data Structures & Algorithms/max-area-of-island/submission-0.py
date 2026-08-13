class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        rows= len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return (1 + dfs(r+1, c)+ dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c-1))
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count = max(count, dfs(r,c))
        return count
