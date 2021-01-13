# 289. Game of Life
# Medium

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1))

        def get_live(r, c):
            live = 0
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] == 1 or board[nr][nc] == 'D'):
                    live += 1
            return live

        for r in range(rows):
            for c in range(cols):
                live_count = get_live(r, c)
                # Rule 1 and 3
                if board[r][c] == 1 and (live_count < 2 or live_count > 3):
                    board[r][c] = 'D'
                # Rule 4
                if board[r][c] == 0 and live_count == 3:
                    board[r][c] = 'L'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'D':
                    board[r][c] = 0
                if board[r][c] == 'L':
                    board[r][c] = 1
