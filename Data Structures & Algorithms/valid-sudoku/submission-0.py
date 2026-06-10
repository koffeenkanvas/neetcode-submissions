class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board : List[list[str]]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in rows[r]:
                    return False

                if val in cols[c]:
                    return False

                rows[r].add(val)
                cols[c].add(val)

                box_key=(r//3,c//3)
                val = board[r][c]
                if box_key not in boxes:
                    boxes[box_key] = set()

                if val in boxes[box_key]:
                    return False

                boxes[box_key].add(val)
        return True
