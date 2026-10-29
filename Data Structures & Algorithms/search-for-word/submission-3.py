class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if len(word) == 1:
                        return True
  
                    explored = {(x, y)}

                    if self.is_present((x, y), word, 1, board, explored) is True:
                        return True

        return False

    def is_present(
        self, 
        start_point: (int, int), 
        word: str, 
        word_index: int, 
        board: List[List[str]], 
        explored: dict[(int, int)]
    ) -> bool:
        max_width = len(board[0])
        max_height = len(board)

        up = start_point[0] - 1
        down = start_point[0] + 1
        left = start_point[1] - 1
        right = start_point[1] + 1

        candidates = []

        if up >= 0 and (up, start_point[1]) not in explored and board[up][start_point[1]] == word[word_index]:
            candidates.append((up, start_point[1]))
        
        if down < max_height and (down, start_point[1]) not in explored and board[down][start_point[1]] == word[word_index]:
            candidates.append((down, start_point[1]))
        
        if left >= 0 and (start_point[0], left) not in explored and board[start_point[0]][left] == word[word_index]:
            candidates.append((start_point[0], left))
        
        if right < max_width and (start_point[0], right) not in explored and board[start_point[0]][right] == word[word_index]:
            candidates.append((start_point[0], right))

        if len(candidates) == 0:
            return False
        elif word_index == len(word) - 1:
            return True

        for candidate in candidates:
            explored.add(candidate)
            if self.is_present(candidate, word, word_index + 1, board, explored) is True:
                return True
            explored.remove(candidate)

        return False
