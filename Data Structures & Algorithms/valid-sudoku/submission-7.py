class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_tracker = [set() for _ in range(9)]
        y_tracker = [set() for _ in range(9)]
        subgrid_tracker = {}

        for x in range(9):
            for y in range(9):
                # We only care about numbers
                if board[x][y] == ".":
                    continue

                # Check if we saw this number in this row
                if board[x][y] in x_tracker[x]:
                    return False

                # Check if we saw this number in this column
                if board[x][y] in y_tracker[y]:
                    return False

                # Track it
                x_tracker[x].add(board[x][y])

                # Track it
                y_tracker[y].add(board[x][y])

                # Sub-boards are tracked as tuples which are hashable
                subgrid_key = (int(x/3), int(y/3))

                if subgrid_key not in subgrid_tracker:
                    subgrid_tracker[subgrid_key] = {}

                # Check if we saw this number in this sub board
                if board[x][y] in subgrid_tracker[subgrid_key]:
                    return False

                #Track it
                subgrid_tracker[subgrid_key][board[x][y]] = None

        return True