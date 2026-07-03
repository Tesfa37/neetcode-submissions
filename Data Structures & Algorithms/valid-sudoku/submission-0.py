class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        piece = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].add(board[r][c])
                if board[r][c] in column[c]:
                    return False
                else:
                    column[c].add(board[r][c])
                ro = r//3
                co = c//3
                if board[r][c] in piece[(ro,co)]:
                    return False
                else:
                    piece[(ro, co)].add(board[r][c])
        return True