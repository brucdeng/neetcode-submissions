class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if r in rows:
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                else:
                    rows[r] = set(board[r][c])
                if c in cols:
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])
                else:
                    cols[c] = set(board[r][c])
                if (r//3, c//3) in boxes:
                    if board[r][c] in boxes[(r//3, c//3)]:
                        return False
                    else:
                        boxes[(r//3, c//3)].add(board[r][c])
                else:
                    boxes[(r//3, c//3)] = set(board[r][c])
        return True