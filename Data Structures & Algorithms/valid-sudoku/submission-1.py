class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for c in range(9):
            for r in range(9):
                d = board[c][r]
                if d == ".":
                    continue
                if (d in row[r] or d in col[c] or d in box[(c//3, r//3)]):
                    return False
                row[r].add(d)
                col[c].add(d)
                box[(c//3,r//3)].add(d)
        return True