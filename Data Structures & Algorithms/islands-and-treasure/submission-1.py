class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS approach
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        INF = 2147483647
        def addnode(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        distance = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = distance
                addnode(row + 1, col)
                addnode(row, col + 1)
                addnode(row - 1, col)
                addnode(row, col - 1)
            distance += 1
        