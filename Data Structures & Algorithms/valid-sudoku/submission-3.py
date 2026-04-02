class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols={}
        rows={}
        squares={}

        for r in range(9):
            for c in range(9):
                val=board[r][c]

                if val == ".":
                    continue
                if r not in rows:
                    rows[r]=[]
                if c not in cols:
                    cols[c]=[]
                if (r//3,c//3) not in squares:
                    squares[r//3,c//3]=[]

                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[r//3,c//3]):

                    return False

                rows[r].append(val)
                cols[c].append(val)
                squares[r//3,c//3].append(val)

        return True