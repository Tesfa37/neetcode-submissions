class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we will want to use BFS 
        q = deque()
        fresh = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        output = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            output += 1
        return output if fresh == 0 else -1
