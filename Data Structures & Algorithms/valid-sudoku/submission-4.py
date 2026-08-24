class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_tracker = [{} for _ in range(9)]
        y_tracker = [{} for _ in range(9)]
        subgrid_tracker = {}

        for x in range(0, 9):
            for y in range(0, 9):
                # We only care about numbers
                if board[x][y] == ".":
                    continue

                # Check if we saw this number in this row
                if board[x][y] in x_tracker[x]:
                    return False
                else:
                    # Track it
                    x_tracker[x][board[x][y]] = None

                # Check if we saw this number in this column
                if board[x][y] in y_tracker[y]:
                    return False
                else:
                    # Track it
                    y_tracker[y][board[x][y]] = None

                # Sub-boards are tracked as tuples which are hashable
                subgrid_key = (int(x/3), int(y/3))

                if subgrid_key not in subgrid_tracker:
                    subgrid_tracker[subgrid_key] = {}

                # Check if we saw this number in this sub board
                if board[x][y] in subgrid_tracker[subgrid_key]:
                    return False
                else:
                    #Track it
                    subgrid_tracker[subgrid_key][board[x][y]] = None

        return True