class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                if (d in rows[r] or d in cols[c] or d in box[(r//3,c//3)]):
                    return False
                rows[r].add(d)
                cols[c].add(d)
                box[(r//3, c//3)].add(d)
        
        return True
                
