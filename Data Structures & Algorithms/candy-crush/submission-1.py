class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            matches = self.find_matches(board)

            if not matches:
                break

            self.crush(board, matches)
            self.drop(board)

        return board

    def crush(self, board: List[List[int]], matches: List[tuple[int, int]]) -> None:
        for (r, c) in matches:
            board[r][c] = 0

    def drop(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        for c in range(n):
            lowest_zero = -1

            # Iterate over each column
            for r in range(m - 1, -1, -1):
                if board[r][c] == 0:
                    lowest_zero = max(lowest_zero, r)

                # Swap current non-zero candy with the lowest zero.
                elif lowest_zero >= 0:
                    board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                    lowest_zero -= 1

    def find_matches(self, board: List[List[int]]) -> List[tuple[int, int]]:
        m, n = len(board), len(board[0])

        matches = set()

        # Check vertically adjacent candies
        for r in range(1, m - 1):
            for c in range(n):
                if board[r][c] == 0:
                    continue
                if board[r][c] == board[r - 1][c] == board[r + 1][c]:
                    matches.add((r, c))
                    matches.add((r - 1, c))
                    matches.add((r + 1, c))

        # Check horizontally adjacent candies
        for r in range(m):
            for c in range(1, n - 1):
                if board[r][c] == 0:
                    continue
                if board[r][c] == board[r][c - 1] == board[r][c + 1]:
                    matches.add((r, c))
                    matches.add((r, c - 1))
                    matches.add((r, c + 1))

        return matches
