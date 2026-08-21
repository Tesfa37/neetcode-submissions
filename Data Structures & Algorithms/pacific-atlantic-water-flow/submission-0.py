class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c, visit, prevHeight):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col, visit, heights[r][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows -1][c])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res